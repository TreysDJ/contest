#!/usr/bin/env python3
"""Cheap, deterministic repository checks for the research deliverables."""

from __future__ import annotations

import importlib.util
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []


def require(condition: bool, message: str) -> None:
    if not condition:
        ERRORS.append(message)


def check_local_links() -> None:
    pattern = re.compile(r"\[[^\]]*]\(([^)]+)\)")
    for markdown in ROOT.rglob("*.md"):
        text = markdown.read_text(encoding="utf-8")
        for raw_target in pattern.findall(text):
            target = raw_target.strip()
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = unquote(target.split("#", 1)[0])
            if not target:
                continue
            resolved = (markdown.parent / target).resolve()
            require(resolved.exists(), f"broken local link in {markdown.relative_to(ROOT)}: {raw_target}")


def check_contests() -> None:
    directories = sorted(path for path in (ROOT / "contests").iterdir() if path.is_dir())
    require(len(directories) == 18, f"expected 18 contest directories, found {len(directories)}")
    for directory in directories:
        require((directory / "README.md").is_file(), f"missing README: {directory.name}")
        require((directory / "CHECKSUMS.sha256").is_file(), f"missing checksums: {directory.name}")
        checksum_file = directory / "CHECKSUMS.sha256"
        listed = set()
        if checksum_file.is_file():
            for line in checksum_file.read_text(encoding="utf-8").splitlines():
                if not line.strip():
                    continue
                parts = line.split(maxsplit=1)
                if len(parts) == 2:
                    listed.add(parts[1].lstrip("*"))
        material = {
            str(path.relative_to(directory))
            for path in directory.rglob("*")
            if path.is_file() and path.suffix.lower() not in {".md"} and path.name != "CHECKSUMS.sha256"
        }
        require(material == listed, f"checksum inventory mismatch: {directory.name}")


def check_practice() -> None:
    catalog_path = ROOT / "research_data" / "practice-catalog.json"
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))

    generator_path = ROOT / "tools" / "generate_practice.py"
    spec = importlib.util.spec_from_file_location("generate_practice", generator_path)
    generator = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(generator)

    try:
        validated = generator.validate_catalog(catalog)
        expected = generator.render(catalog)
    except ValueError as error:
        require(False, f"practice catalog validation failed: {error}")
        return

    text = (ROOT / "PRACTICE.md").read_text(encoding="utf-8")
    require(text == expected, "PRACTICE.md is not generated from practice-catalog.json")
    require(len(validated["topics"]) == 34, "practice topic count is not 34")
    require(sum(validated["task_counts"].values()) == 282, "practice task count is not 282")
    require(validated["core_count"] == 214, "core practice route count is not 214")
    require(validated["leetcode_count"] == 63, "LeetCode foundation count is not 63")
    require(
        validated["special_practice_count"] == 2,
        "expected Java and checker special practice entries",
    )
    require(text.count("| Что тренирует |") == 34, "pattern column missing from a topic")
    hidden_count = sum(
        task["role"] in {"D", "F", "X"}
        for topic in validated["topics"]
        for task in topic["tasks"]
    )
    require(
        text.count("<details><summary>Показать после попытки</summary>") == hidden_count,
        "hidden D/F/X pattern count does not match the catalog",
    )

    audit = (ROOT / "research_data" / "practice-audit.md").read_text(encoding="utf-8")
    legacy = re.search(
        r"Из прежних 282 слотов: \*\*(\d+) KEEP\*\*, "
        r"\*\*(\d+) MOVE\*\*, \*\*(\d+) REPLACE\*\*",
        audit,
    )
    require(legacy is not None, "practice audit summary is missing")
    if legacy:
        expected_verdicts = tuple(map(int, legacy.groups()))
        require(
            sum(expected_verdicts) == 282,
            "practice audit does not classify all 282 legacy tasks",
        )
        actual_verdicts = tuple(
            len(re.findall(rf"\| `{verdict}` \|", audit))
            for verdict in ("KEEP", "MOVE", "REPLACE")
        )
        require(
            actual_verdicts == expected_verdicts,
            "practice audit verdict rows do not match its summary",
        )

    for topic in catalog["topics"]:
        start = f"## Тема {topic['number']}."
        next_start = f"## Тема {topic['number'] + 1}."
        require(start in audit, f"practice audit section is missing: topic {topic['number']}")
        section = audit.split(start, 1)[1]
        if next_start in section:
            section = section.split(next_start, 1)[0]
        require("### Новое покрытие" in section, f"new coverage is missing: topic {topic['number']}")
        coverage = section.split("### Новое покрытие", 1)[1]
        for task in topic["tasks"]:
            prefix = {"CF": "CF", "ACMP": "ACMP", "GYM": "GYM"}[task["platform"]]
            pattern = task["pattern_label"].replace("|", r"\|")
            solution = task["expected_solution"].replace("|", r"\|")
            expected_row = (
                f"| {prefix} {task['id']} — {task['title']} | `{task['role']}` | "
                f"{pattern} | {solution} |"
            )
            require(
                expected_row in coverage,
                f"practice audit coverage differs from catalog: topic {topic['number']}, "
                f"{task['platform']} {task['id']}",
            )


def main() -> None:
    for filename in [
        "research.md", "ROADMAP.md", "PRACTICE.md", "PROGRESS.md",
        "CONTEST_STRATEGY.md", "contests/MANIFEST.md", "templates/java/README.md",
        "research_data/practice-catalog.json",
        "research_data/practice-audit.md",
    ]:
        require((ROOT / filename).is_file(), f"missing deliverable: {filename}")
    check_local_links()
    check_contests()
    check_practice()
    if ERRORS:
        print("Audit failed:")
        for error in ERRORS:
            print("-", error)
        return 1
    print("Repository audit: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
