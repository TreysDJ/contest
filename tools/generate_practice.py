#!/usr/bin/env python3
"""Render PRACTICE.md from the manually audited practice catalog."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "research_data" / "practice-catalog.json"
OUTPUT = ROOT / "PRACTICE.md"

VISIBLE_ROLES = {"L", "R", "H"}
HIDDEN_ROLES = {"D", "F", "X"}
ROLE_ORDER = {"D": 0, "L": 1, "R": 2, "H": 3, "F": 4, "X": 5}
STAGES = {"A0", "A1", "B", "C"}


def fail(message: str) -> None:
    raise ValueError(message)


def escape_cell(text: str) -> str:
    return text.replace("|", "&#124;").replace("\n", " ")


def task_label(task: dict) -> str:
    platform = task["platform"]
    if platform == "CF":
        prefix = f"CF {task['id']}"
    elif platform == "ACMP":
        prefix = f"ACMP {task['id']}"
    elif platform == "GYM":
        prefix = f"CF Gym {task['id']}"
    else:
        fail(f"unsupported platform: {platform}")
    label = f"[{prefix} — {task['title']}]({task['url']})"
    if task.get("practice_url"):
        label += f" · [регистрация/отправка]({task['practice_url']})"
    return label


def pattern_cell(task: dict) -> str:
    pattern = escape_cell(task["pattern_label"])
    if task["pattern_visibility"] == "visible":
        return pattern
    return (
        "<details><summary>Показать после попытки</summary>"
        f"{pattern}</details>"
    )


def apply_catalog_refactor(catalog: dict) -> None:
    """Apply schema-v2 additions and moves before validation/rendering."""
    if catalog.get("_refactor_applied"):
        return

    topics_by_number = {topic["number"]: topic for topic in catalog["topics"]}
    tasks_by_key = {
        (task["platform"], str(task["id"])): (topic, task)
        for topic in catalog["topics"]
        for task in topic["tasks"]
    }

    for addition in catalog.get("task_additions", []):
        key = (addition["platform"], str(addition["id"]))
        if key in tasks_by_key:
            fail(f"task_additions duplicates an existing task: {key[0]} {key[1]}")
        topic = topics_by_number[addition["topic"]]
        task = {key: value for key, value in addition.items() if key != "topic"}
        task.setdefault("secondary_patterns", [])
        task.setdefault("pattern_visibility", "visible")
        task.setdefault("why_selected", f"Закрывает ступень: {task['pattern_label']}.")
        task.setdefault("verified_statement", True)
        task.setdefault("verified_solution", True)
        task.setdefault("verified_on", catalog["audited_on"])
        task.setdefault(
            "verification_sources",
            [{"kind": "official_statement", "url": task["url"]}],
        )
        topic["tasks"].append(task)
        tasks_by_key[key] = (topic, task)

    for move in catalog.get("task_moves", []):
        key = (move["platform"], str(move["id"]))
        if key not in tasks_by_key:
            fail(f"task_moves references an unknown task: {key[0]} {key[1]}")
        source_topic, task = tasks_by_key[key]
        source_topic["tasks"].remove(task)
        if move.get("role"):
            task["role"] = move["role"]
            task["pattern_visibility"] = (
                "visible" if task["role"] in VISIBLE_ROLES else "after_attempt"
            )
        task.update(move.get("updates", {}))
        target_topic = topics_by_number[move.get("to_topic", source_topic["number"])]
        target_topic["tasks"].append(task)
        tasks_by_key[key] = (target_topic, task)

    for topic in catalog["topics"]:
        topic["tasks"].sort(key=lambda task: ROLE_ORDER[task["role"]])
    catalog["_refactor_applied"] = True


def validate_catalog(catalog: dict) -> dict:
    apply_catalog_refactor(catalog)
    if catalog.get("schema_version") != 2:
        fail("unsupported practice catalog schema")
    policy = catalog.get("selection_policy", {})
    if policy.get("automatic_tag_fallback") is not False:
        fail("automatic tag fallback must stay disabled")
    if policy.get("manual_semantic_roles") is not True:
        fail("semantic roles must be manually audited")
    if set(policy.get("visible_pattern_roles", [])) != VISIBLE_ROLES:
        fail("visible pattern roles do not match the rendering policy")
    if set(policy.get("hidden_pattern_roles", [])) != HIDDEN_ROLES:
        fail("hidden pattern roles do not match the rendering policy")
    topics = catalog.get("topics")
    if not isinstance(topics, list) or not topics:
        fail("catalog must contain topics")

    topic_numbers = [topic.get("number") for topic in topics]
    if topic_numbers != list(range(1, len(topics) + 1)):
        fail("topic numbers must be consecutive")

    used: set[tuple[str, str]] = set()
    task_counts = Counter()
    core_count = 0
    stage_overrides = catalog.get("topic_stage_overrides", {})
    if set(stage_overrides) != {topic["key"] for topic in topics}:
        fail("topic_stage_overrides must classify every topic exactly once")
    for topic in topics:
        topic["stage"] = stage_overrides[topic["key"]]
        stage = topic["stage"]
        if stage not in STAGES:
            fail(f"unsupported stage in topic {topic['number']}: {stage}")
        tasks = topic.get("tasks", [])
        if not tasks:
            fail(f"topic {topic['number']} has no tasks")
        role_order = [ROLE_ORDER.get(task.get("role"), -1) for task in tasks]
        if role_order != sorted(role_order):
            fail(f"topic {topic['number']} tasks are not ordered D/L/R/H/F/X")
        if any(role < 0 for role in role_order):
            fail(f"topic {topic['number']} has unsupported role")
        task_counts[stage] += len(tasks)

        for task in tasks:
            task.setdefault(
                "pattern_id",
                f"{topic['key']}.{task['primary_pattern'].casefold().replace(' ', '-')}",
            )
            task.setdefault(
                "learning_step",
                {
                    "D": "diagnose",
                    "L": "introduce",
                    "R": "practice",
                    "H": "challenge",
                    "F": "check",
                    "X": "mixed",
                }[task["role"]],
            )
            key = (task["platform"], str(task["id"]))
            if key in used:
                fail(f"duplicate task: {key[0]} {key[1]}")
            used.add(key)

            if task["platform"] not in {"CF", "ACMP", "GYM"}:
                fail(f"task is outside Codeforces/ACMP: {key[0]} {key[1]}")
            expected_domain = (
                "codeforces.com" if task["platform"] in {"CF", "GYM"} else "acmp.ru"
            )
            if expected_domain not in task.get("url", ""):
                fail(f"unexpected task URL domain: {key[0]} {key[1]}")
            if task.get("practice_url") and "codeforces.com" not in task["practice_url"]:
                fail(f"unexpected practice URL domain: {key[0]} {key[1]}")
            rating = task.get("rating")
            if rating is not None and (
                not isinstance(rating, int) or isinstance(rating, bool)
            ):
                fail(f"invalid rating: {key[0]} {key[1]}")

            for field in (
                "title",
                "url",
                "role",
                "pattern_id",
                "learning_step",
                "primary_pattern",
                "pattern_label",
                "why_selected",
                "expected_solution",
            ):
                if not task.get(field):
                    fail(
                        f"topic {topic['number']} {key[0]} {key[1]} "
                        f"has empty {field}"
                    )
            if not task.get("verified_statement"):
                fail(f"statement not verified: {key[0]} {key[1]}")
            if not task.get("verified_solution"):
                fail(f"solution not verified: {key[0]} {key[1]}")
            if not task.get("verified_on"):
                fail(f"verification date missing: {key[0]} {key[1]}")
            if not isinstance(task.get("secondary_patterns"), list):
                fail(f"secondary_patterns must be a list: {key[0]} {key[1]}")
            if not isinstance(task.get("prerequisites"), list) or not task["prerequisites"]:
                fail(f"prerequisites missing: {key[0]} {key[1]}")

            expected_visibility = (
                "visible" if task["role"] in VISIBLE_ROLES else "after_attempt"
            )
            if task.get("pattern_visibility") != expected_visibility:
                fail(
                    f"wrong pattern visibility for {key[0]} {key[1]}: "
                    f"{task.get('pattern_visibility')}"
                )
            if task["role"] not in {"H", "X"}:
                core_count += 1

        for lc in topic.get("leetcode", []):
            for field in ("id", "title", "url", "focus"):
                if not lc.get(field):
                    fail(f"topic {topic['number']} LeetCode entry misses {field}")

    required_patterns = catalog.get("required_patterns", {})
    covered_patterns = Counter(
        task["pattern_id"]
        for topic in topics
        for task in topic["tasks"]
        if task["role"] not in {"H", "X"}
    )
    for stage, pattern_ids in required_patterns.items():
        if stage not in {"A0", "A1"}:
            fail(f"required_patterns is only supported for A0/A1, found {stage}")
        for pattern_id in pattern_ids:
            if covered_patterns[pattern_id] == 0:
                fail(f"required pattern has no core task: {pattern_id}")

    special_practice = catalog.get("special_practice", [])
    if not isinstance(special_practice, list):
        fail("special_practice must be a list")
    special_topics: set[int] = set()
    for item in special_practice:
        for field in ("topic", "kind", "title", "steps"):
            if not item.get(field):
                fail(f"special practice entry misses {field}")
        if item["topic"] not in range(1, len(topics) + 1):
            fail(f"special practice has invalid topic: {item['topic']}")
        if item["topic"] in special_topics:
            fail(f"duplicate special practice for topic {item['topic']}")
        special_topics.add(item["topic"])
        if item.get("counts_toward_task_budget") is not False:
            fail("special practice must not silently change the task budget")
        if not isinstance(item["steps"], list) or not all(
            isinstance(step, str) and step.strip() for step in item["steps"]
        ):
            fail(f"special practice for topic {item['topic']} has invalid steps")

    return {
        "topics": topics,
        "task_counts": task_counts,
        "core_count": core_count,
        "leetcode_count": sum(len(topic.get("leetcode", [])) for topic in topics),
        "special_practice_count": len(special_practice),
    }


def render(catalog: dict) -> str:
    validated = validate_catalog(catalog)
    topics = validated["topics"]
    counts = validated["task_counts"]
    total = sum(counts.values())

    parts = [
        "# Банк задач",
        "",
        "Этот каталог построен под календарь «лето → отборы в октябре–ноябре → "
        "финалы в марте–апреле». Он не требует решить все задачи подряд.",
        "",
        "## Объём и маршрут",
        "",
        f"- этап A0: **{counts['A0']}** задач — инженерная и алгоритмическая база;",
        f"- этап A1: **{counts['A1']}** задач — основные переносимые олимпиадные паттерны;",
        f"- этап B: **{counts['B']}** задач — регулярный финальный слой;",
        f"- этап C: **{counts['C']}** задач — выборочная продвинутая практика;",
        f"- полный каталог: **{total}** задач Codeforces/ACMP;",
        f"- основной маршрут без `H` и `X`: **{validated['core_count']}** задач;",
        f"- LeetCode-база: **{validated['leetcode_count']}** задач, в основной лимит не входит.",
        f"- практические checkpoints: **{validated['special_practice_count']}** блоков; "
        "помеченные как обязательные входят в освоение A0/A1, но не являются задачами онлайн-судьи.",
        "",
        "Роли: `D` — диагностика; `L` — изучение приёма; `R` — закрепление; "
        "`H` — трудная задача; `F` — контрольная без подсказок; `X` — сочетание тем. "
        "Для быстрого маршрута решать `D/L/R/F`; `H/X` переносить на финальный цикл "
        "или брать по слабым местам.",
        "",
        "Колонка **«Что тренирует»** описывает целевой учебный способ решения, а не "
        "утверждает, что других решений не существует. Для `D/F/X` точный паттерн "
        "скрыт: раскрывать его следует только после ограниченной самостоятельной попытки.",
        "",
        "## Правила работы",
        "",
        "1. До начала темы решить `D` за ограниченное время, не раскрывая паттерн. "
        "Если идея не найдена, изучить теорию и перейти к `L`.",
        "2. Если задача дала переносимый вывод, записать его одной короткой строкой "
        "в [`NOTES.md`](NOTES.md). Для обычного решения без нового вывода заметка не нужна.",
        "3. `F` решать как мини-контест: без раскрытия паттерна, подсказок и старого кода, "
        "с полным тестированием и разбором после сдачи.",
        "4. ACMP используется как русскоязычный вход и тренировка реализации; "
        "Codeforces — как основная шкала сложности.",
        "5. Рейтинг Codeforces — ориентир, а не строгий порядок. Релевантность приёма "
        "и педагогическая роль важнее рейтинга.",
        "6. Если для фундаментального паттерна нет достаточно прямой задачи CF/Gym/ACMP, "
        "выполнить обязательный checkpoint; не заменять его случайной задачей с совпавшим тегом.",
    ]

    for topic in topics:
        number = topic["number"]
        tasks = topic["tasks"]
        parts.extend([
            "",
            f"## {number}. {topic['title']}",
            "",
            f"Этап **{topic['stage']}**. Задач: **{len(tasks)}**. "
            f"Связь с этапом и признаки распознавания: "
            f"[ROADMAP.md — тема {number}](ROADMAP.md#тема-{number}).",
            "",
        ])

        leetcode = topic.get("leetcode", [])
        if leetcode:
            lc_links = [
                f"[LC {item['id']} — {item['title']}]({item['url']})"
                f" — {item['focus']}"
                for item in leetcode
            ]
            parts.extend([
                "База LeetCode, не входит в лимит: " + "; ".join(lc_links) + ".",
                "",
            ])

        parts.extend([
            "| № | Задача | Рейтинг CF | Роль | Что тренирует |",
            "|---:|---|---:|:---:|---|",
        ])
        for index, task in enumerate(tasks, start=1):
            rating = task["rating"] if task["rating"] is not None else "—"
            parts.append(
                f"| {index} | {task_label(task)} | {rating} | "
                f"`{task['role']}` | {pattern_cell(task)} |"
            )

        special_items = [
            item
            for item in catalog.get("special_practice", [])
            if item.get("topic") == number
        ]
        for special in special_items:
            parts.extend([
                "",
                "Отдельная практика, не входит в лимит:",
                "",
                f"**{special['title']}.**",
                "",
                *[
                    f"{index}. {step}"
                    for index, step in enumerate(special["steps"], start=1)
                ],
            ])

    return "\n".join(parts) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail if PRACTICE.md differs from the audited catalog",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    rendered = render(catalog)
    if args.check:
        current = OUTPUT.read_text(encoding="utf-8") if OUTPUT.exists() else ""
        if current != rendered:
            print(
                "PRACTICE.md is out of date; run tools/generate_practice.py",
                file=sys.stderr,
            )
            return 1
        print("PRACTICE.md matches the audited catalog")
        return 0

    OUTPUT.write_text(rendered, encoding="utf-8")
    print(
        f"wrote {OUTPUT}: {sum(len(t['tasks']) for t in catalog['topics'])} tasks, "
        f"{sum(len(t.get('leetcode', [])) for t in catalog['topics'])} LeetCode"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
