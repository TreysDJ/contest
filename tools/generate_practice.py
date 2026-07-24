#!/usr/bin/env python3
"""Build PRACTICE.md from the audited Codeforces snapshot and curated ACMP tasks."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CF_DATA = ROOT / "research_data" / "codeforces-candidates.json"
OUTPUT = ROOT / "PRACTICE.md"


ACMP = lambda task_id, name: ("ACMP", str(task_id), name, None)


TOPICS = [
    dict(key="01-implementation", title="Оценка сложности, Java и аккуратная реализация", priority="A", total=10,
         acmp=[ACMP(1, "A+B"), ACMP(5, "Статистика")], preferred=[] ,
         lc=[("412", "Fizz Buzz", "fizz-buzz"), ("66", "Plus One", "plus-one")]),
    dict(key="02-bruteforce", title="Полный перебор, рекурсия и отсечения", priority="A", total=10,
         acmp=[ACMP(16, "Лесенка"), ACMP(24, "Вырубка деревьев")], preferred=[],
         lc=[("46", "Permutations", "permutations"), ("78", "Subsets", "subsets")]),
    dict(key="03-sorting", title="Сортировка, компараторы и сжатие координат", priority="A", total=10,
         acmp=[ACMP(41, "Сортировка подсчетом"), ACMP(119, "Сортировка времени")], preferred=[],
         lc=[("912", "Sort an Array", "sort-an-array"), ("56", "Merge Intervals", "merge-intervals")]),
    dict(key="04-maps-sets", title="Частоты, HashMap/HashSet и множества", priority="A", total=10,
         acmp=[ACMP(82, "Пересечение множеств"), ACMP(816, "Система пересекающихся множеств")],
         preferred=["1703B", "1760C", "1722C", "519B", "1520D", "1955B", "4C", "1213B"],
         lc=[("1", "Two Sum", "two-sum"), ("49", "Group Anagrams", "group-anagrams")]),
    dict(key="05-linear-ds", title="Стек, очередь, дек и приоритетная очередь", priority="A", total=10,
         acmp=[ACMP(899, "Баланс скобок"), ACMP(946, "Полка")],
         preferred=["26B", "343B", "450A", "545D", "797C", "1092D1", "1907B", "5C"],
         lc=[("20", "Valid Parentheses", "valid-parentheses"), ("239", "Sliding Window Maximum", "sliding-window-maximum")]),
    dict(key="06-prefix-sweep", title="Префиксные суммы, разности, 2D-префиксы и sweep line", priority="A", total=10,
         acmp=[], preferred=["363B", "433B", "313B", "276C", "816B", "466C", "1795C", "1807D", "1703F", "1000C"],
         lc=[("303", "Range Sum Query — Immutable", "range-sum-query-immutable"), ("304", "Range Sum Query 2D — Immutable", "range-sum-query-2d-immutable")]),
    dict(key="07-two-pointers", title="Два указателя и скользящее окно", priority="A", total=10,
         acmp=[ACMP(245, "Сплоченная команда"), ACMP(649, "Защищенный пароль")], preferred=[],
         lc=[("3", "Longest Substring Without Repeating Characters", "longest-substring-without-repeating-characters"), ("11", "Container With Most Water", "container-with-most-water")]),
    dict(key="08-search", title="Бинарный/тернарный поиск и поиск по ответу", priority="A", total=10,
         acmp=[ACMP(267, "Ксерокопии"), ACMP(523, "Роман в томах")],
         preferred=["706B", "230B", "279B", "1352C", "474B", "1873E", "1742E", "1490C"],
         lc=[("704", "Binary Search", "binary-search"), ("875", "Koko Eating Bananas", "koko-eating-bananas")]),
    dict(key="09-greedy", title="Жадные алгоритмы, инварианты и обменный аргумент", priority="A", total=10,
         acmp=[ACMP(39, "Волосатый бизнес"), ACMP(228, "Валютные махинации")], preferred=[],
         lc=[("55", "Jump Game", "jump-game"), ("435", "Non-overlapping Intervals", "non-overlapping-intervals")]),
    dict(key="10-bitmasks", title="Биты, маски, подмаски и булева алгебра", priority="A", total=10,
         acmp=[ACMP(542, "Бит-реверс"), ACMP(563, "Задача про XOR")], preferred=[],
         lc=[("78", "Subsets", "subsets"), ("1310", "XOR Queries of a Subarray", "xor-queries-of-a-subarray")]),
    dict(key="11-number-theory", title="Теория чисел: gcd, простые, факторизация, решето", priority="A", total=10,
         acmp=[ACMP(14, "НОК"), ACMP(170, "Разложение числа")], preferred=[],
         lc=[("204", "Count Primes", "count-primes"), ("1979", "Find Greatest Common Divisor of Array", "find-greatest-common-divisor-of-array")]),
    dict(key="12-combinatorics", title="Модульная арифметика и комбинаторика", priority="A", total=10,
         acmp=[ACMP(158, "Великий комбинатор"), ACMP(629, "Сочетания")], preferred=[],
         lc=[("62", "Unique Paths", "unique-paths"), ("1641", "Count Sorted Vowel Strings", "count-sorted-vowel-strings")]),
    dict(key="13-strings-basic", title="Строки: префикс-функция, Z-функция и хеширование", priority="A", total=10,
         acmp=[ACMP(202, "Поиск подстроки"), ACMP(204, "Циклическая строка")],
         preferred=["96A", "208A", "43A", "126B", "471D", "535D", "1200E", "7D"],
         lc=[("28", "Find the Index of the First Occurrence", "find-the-index-of-the-first-occurrence-in-a-string"), ("214", "Shortest Palindrome", "shortest-palindrome")]),
    dict(key="14-graph-basic", title="Обходы графа, компоненты, циклы и двудольность", priority="A", total=10,
         acmp=[ACMP(15, "Дороги"), ACMP(99, "Лабиринт")],
         preferred=["500A", "1829E", "445A", "1433D", "893C", "1702E", "377A", "1365D"],
         lc=[("200", "Number of Islands", "number-of-islands"), ("785", "Is Graph Bipartite?", "is-graph-bipartite")]),
    dict(key="15-shortest-paths", title="Кратчайшие пути: BFS, 0–1 BFS, Дейкстра, Флойд, Беллман—Форд", priority="A", total=10,
         acmp=[ACMP(132, "Алгоритм Дейкстры"), ACMP(135, "Алгоритм Флойда")],
         preferred=["3A", "520B", "1661B", "1418C", "295B", "242C", "20C", "449B"],
         lc=[("743", "Network Delay Time", "network-delay-time"), ("787", "Cheapest Flights Within K Stops", "cheapest-flights-within-k-stops")]),
    dict(key="16-tree-basic", title="Деревья: Эйлеров обход, двоичные подъёмы и LCA", priority="A", total=10,
         acmp=[ACMP(141, "Дерево")],
         preferred=["115A", "580C", "1843D", "862B", "1676G", "1328E", "1304E", "519E", "1037D"],
         lc=[("236", "Lowest Common Ancestor of a Binary Tree", "lowest-common-ancestor-of-a-binary-tree"), ("863", "All Nodes Distance K in Binary Tree", "all-nodes-distance-k-in-binary-tree")]),
    dict(key="17-dp-basic", title="Базовое DP: пути, рюкзак, LIS и восстановление ответа", priority="A", total=10,
         acmp=[ACMP(11, "Зайчик"), ACMP(121, "Гвоздики")],
         preferred=["580A", "189A", "455A", "327A", "1195C", "698A", "474D", "706C"],
         lc=[("322", "Coin Change", "coin-change"), ("300", "Longest Increasing Subsequence", "longest-increasing-subsequence")]),
    dict(key="18-range-structures", title="Fenwick, segment tree, lazy propagation и sparse table", priority="A", total=10,
         acmp=[ACMP(112, "Армия"), ACMP(418, "Редактор")],
         preferred=["339D", "61E", "380C", "52C", "474F", "242E", "438D", "459D"],
         lc=[("307", "Range Sum Query — Mutable", "range-sum-query-mutable"), ("715", "Range Module", "range-module")]),
    dict(key="19-geometry", title="Вычислительная геометрия", priority="B", total=7,
         acmp=[ACMP(348, "Пересечение отрезков")], preferred=["766B", "507B", "514B", "1486B", "1730B", "1552C"],
         lc=[("973", "K Closest Points to Origin", "k-closest-points-to-origin"), ("149", "Max Points on a Line", "max-points-on-a-line")]),
    dict(key="20-graph-structure", title="DAG, топосортировка, SCC, мосты и точки сочленения", priority="B", total=7,
         acmp=[ACMP(124, "Светофорчики")], preferred=["510C", "427C", "977E", "687A", "118E", "1000E"],
         lc=[("1192", "Critical Connections in a Network", "critical-connections-in-a-network"), ("802", "Find Eventual Safe States", "find-eventual-safe-states")]),
    dict(key="21-dsu-mst", title="DSU, MST и офлайн-связность", priority="B", total=7,
         acmp=[ACMP(142, "Минимальный каркас")], preferred=["277A", "1167C", "25D", "1249B2", "160D", "609E"],
         lc=[("1584", "Min Cost to Connect All Points", "min-cost-to-connect-all-points"), ("721", "Accounts Merge", "accounts-merge")]),
    dict(key="22-structural-dp", title="DP по отрезкам, решёткам, графам и деревьям", priority="B", total=7,
         acmp=[ACMP(123, "Восстановление скобок")],
         preferred=["1249E", "1528A", "607B", "1114D", "161D", "1363E"],
         lc=[("312", "Burst Balloons", "burst-balloons"), ("337", "House Robber III", "house-robber-iii")]),
    dict(key="23-state-dp", title="DP по подмножествам, цифрам и профилю", priority="B", total=7,
         acmp=[ACMP(29, "Компьютерная игра")],
         preferred=["580D", "577B", "1288D", "165E", "628D", "55D"],
         lc=[("464", "Can I Win", "can-i-win"), ("902", "Numbers At Most N Given Digit Set", "numbers-at-most-n-given-digit-set")]),
    dict(key="24-ordered-structures", title="Декартово дерево, treap и порядковые структуры", priority="B", total=7,
         acmp=[ACMP(505, "Забор")],
         preferred=["1354D", "706D", "915E", "558E", "1748E", "702F"],
         lc=[("315", "Count of Smaller Numbers After Self", "count-of-smaller-numbers-after-self"), ("327", "Count of Range Sum", "count-of-range-sum")]),
    dict(key="25-flow-matching", title="Потоки и паросочетания", priority="B", total=7,
         acmp=[ACMP(151, "Банкет")], preferred=["1530D", "1525D", "1437C", "1426E", "546E", "468B"],
         lc=[("1820", "Maximum Number of Accepted Invitations", "maximum-number-of-accepted-invitations"), ("1066", "Campus Bikes II", "campus-bikes-ii")]),
    dict(key="26-strings-advanced", title="Ахо—Корасик, Манакер, suffix array/automaton", priority="B", total=7,
         acmp=[ACMP(70, "Степень строки")],
         preferred=["271D", "432D", "559B", "1326D2", "710F", "873F"],
         lc=[("1044", "Longest Duplicate Substring", "longest-duplicate-substring"), ("336", "Palindrome Pairs", "palindrome-pairs")]),
    dict(key="27-trees-advanced", title="HLD, центроидная декомпозиция, small-to-large и rerooting", priority="B", total=7,
         acmp=[ACMP(116, "Фермер - 2")], preferred=["191C", "383C", "321C", "342E", "600E", "375D"],
         lc=[("834", "Sum of Distances in Tree", "sum-of-distances-in-tree"), ("1483", "Kth Ancestor of a Tree Node", "kth-ancestor-of-a-tree-node")]),
    dict(key="28-games", title="Теория игр: выигрыш/проигрыш, Nim и Sprague—Grundy", priority="B", total=7,
         acmp=[ACMP(4, "Игра")], preferred=["1527B1", "1747C", "276B", "1472D", "1370C", "1363C"],
         lc=[("292", "Nim Game", "nim-game"), ("486", "Predict the Winner", "predict-the-winner")]),
    dict(key="29-mitm", title="Meet-in-the-middle и разбиение пространства поиска", priority="B", total=7,
         acmp=[], preferred=["769D", "888E", "552C", "1006F", "525E", "1105E", "1257F"],
         lc=[("1755", "Closest Subsequence Sum", "closest-subsequence-sum")]),
    dict(key="30-sqrt-mo", title="Корневая декомпозиция, Mo и офлайн-запросы", priority="C", total=5,
         acmp=[], preferred=["13E", "86D", "220B", "617E", "455D"],
         lc=[("493", "Reverse Pairs", "reverse-pairs")]),
    dict(key="31-rollback-persistent", title="Rollback, персистентность и динамическая связность", priority="C", total=5,
         acmp=[], preferred=["292D", "707D", "813E", "891C", "484E"],
         lc=[("1146", "Snapshot Array", "snapshot-array")]),
    dict(key="32-dp-optimization", title="Оптимизации DP: CHT/Li Chao, divide-and-conquer, Knuth", priority="C", total=5,
         acmp=[], preferred=["319C", "868F", "321E", "1083E", "932F"],
         lc=[("410", "Split Array Largest Sum", "split-array-largest-sum")]),
    dict(key="33-algebra-fft", title="Матрицы, линейная алгебра, FFT/NTT", priority="C", total=5,
         acmp=[], preferred=["1557C", "1117D", "222E", "718C", "528D"],
         lc=[("509", "Fibonacci Number", "fibonacci-number"), ("43", "Multiply Strings", "multiply-strings")]),
    dict(key="34-random-interactive", title="Вероятность, рандомизация, interactive и output-only", priority="C", total=5,
         acmp=[], preferred=["453A", "839C", "1407C", "1479A", "148D"],
         lc=[("528", "Random Pick with Weight", "random-pick-with-weight")]),
]


CUSTOM_CF = {
    "26B": ("Regular Bracket Sequence", 1400), "343B": ("Alternating Current", 1600),
    "450A": ("Jzzhu and Children", 1000), "545D": ("Queue", 1300),
    "797C": ("Minimal string", 1700), "1092D1": ("Great Vova Wall (Version 1)", 2200),
    "363B": ("Fence", 1100), "433B": ("Kuriyama Mirai's Stones", 1200),
    "313B": ("Ilya and Queries", 1100), "380C": ("Sereja and Brackets", 2000),
    "52C": ("Circular RMQ", 2200), "474F": ("Ant colony", 2100),
    "242E": ("XOR on Segment", 2000), "438D": ("The Child and Sequence", 2300),
    "459D": ("Pashmak and Parmida's problem", 1800), "118E": ("Bertown roads", 2000),
    "1000E": ("We Need More Bosses", 2100), "160D": ("Edges in MST", 2300),
    "13E": ("Holes", 2700), "220B": ("Little Elephant and Array", 1800),
    "617E": ("XOR and Favorite Number", 2200), "455D": ("Serega and Fun", 2700),
    "292D": ("Connected Components", 1900), "707D": ("Persistent Bookcase", 2200),
    "813E": ("Army Creation", 2200), "891C": ("Envy", 2300),
    "484E": ("Sign on Fence", 2500), "319C": ("Kalila and Dimna in the Logging Industry", 2100),
    "321E": ("Ciel and Gondolas", 2600), "1083E": ("The Fair Nut and Rectangles", 2400),
    "932F": ("Escape Through Leaf", 2700), "148D": ("Bag of mice", 1800),
    "222E": ("Decoding Genome", 1900),
    "1304E": ("1-Trees and Queries", 2000),
    "1195C": ("Basketball Exercise", 1400), "698A": ("Vacations", 1400),
    "474D": ("Flowers", 1700), "706C": ("Hard problem", 1600),
    "1249E": ("By Elevator or Stairs?", 1700), "607B": ("Zuma", 1900),
    "1114D": ("Flood Fill", 1900), "628D": ("Magic Numbers", 2200),
    "55D": ("Beautiful numbers", 2500), "1354D": ("Multiset", 1900),
    "915E": ("Physical Education Lessons", 2300), "558E": ("A Simple Task", 2300),
    "1748E": ("Yet Another Array Counting Problem", 2300), "702F": ("T-Shirts", 2800),
    "710F": ("String Set Queries", 2400), "873F": ("Forbidden Indices", 2400),
    "1000C": ("Covered Points Count", 1700), "1200E": ("Compress Words", 2000),
    "471D": ("MUH and Cube Walls", 1800), "535D": ("Tavas and Malekas", 1900),
    "7D": ("Palindrome Degree", 2200),
}


ROLE_PATTERNS = {
    "A": ["D", "L", "L", "L", "R", "R", "R", "H", "F", "X"],
    "B": ["D", "L", "L", "R", "H", "F", "X"],
    "C": ["L", "R", "H", "F", "X"],
}


def flatten_candidates(raw: dict) -> tuple[dict[str, dict], dict[str, list[dict]]]:
    by_id: dict[str, dict] = {}
    for values in raw.values():
        for item in values:
            by_id.setdefault(item["id"], item)
    return by_id, raw


def select_tasks(topic: dict, by_id: dict[str, dict], raw: dict, globally_used: set[str]) -> list[tuple]:
    selected: list[tuple] = list(topic["acmp"])
    need_cf = topic["total"] - len(selected)
    chosen_cf: list[tuple] = []

    for task_id in topic["preferred"]:
        key = "CF:" + task_id
        if key in globally_used:
            continue
        item = by_id.get(task_id)
        if item:
            chosen_cf.append(("CF", task_id, item["name"], item.get("rating")))
        elif task_id in CUSTOM_CF:
            name, rating = CUSTOM_CF[task_id]
            chosen_cf.append(("CF", task_id, name, rating))
        else:
            raise RuntimeError(f"Missing metadata for Codeforces {task_id}")
        globally_used.add(key)
        if len(chosen_cf) == need_cf:
            break

    if len(chosen_cf) < need_cf:
        # The browser-side research snapshot is deliberately interleaved by
        # rating bands; preserve that order so a topic does not collapse into
        # ten nearly identical easy tasks.
        for item in raw[topic["key"]]:
            key = "CF:" + item["id"]
            if key in globally_used:
                continue
            chosen_cf.append(("CF", item["id"], item["name"], item.get("rating")))
            globally_used.add(key)
            if len(chosen_cf) == need_cf:
                break

    if len(chosen_cf) != need_cf:
        raise RuntimeError(f"Not enough unique tasks for {topic['key']}: {len(chosen_cf)}/{need_cf}")

    selected.extend(sorted(chosen_cf, key=lambda x: x[3] or 0))
    if len(selected) != topic["total"]:
        raise AssertionError(topic["key"])
    return selected


def task_link(platform: str, task_id: str, name: str) -> str:
    if platform == "CF":
        contest = task_id[:-1]
        index = task_id[-1]
        # Indices such as D1/D2 have two trailing characters.
        if task_id[-2:].startswith(("A", "B", "C", "D", "E", "F", "G", "H")) and task_id[-1].isdigit():
            contest, index = task_id[:-2], task_id[-2:]
        return f"[CF {task_id} — {name}](https://codeforces.com/problemset/problem/{contest}/{index})"
    return f"[ACMP {task_id} — {name}](https://acmp.ru/index.asp?main=task&id_task={task_id})"


def main() -> None:
    raw = json.loads(CF_DATA.read_text(encoding="utf-8"))
    by_id, pools = flatten_candidates(raw)
    used: set[str] = set()
    sections: list[str] = []
    totals = {"A": 0, "B": 0, "C": 0}
    required = 0

    for number, topic in enumerate(TOPICS, start=1):
        tasks = select_tasks(topic, by_id, pools, used)
        roles = ROLE_PATTERNS[topic["priority"]]
        totals[topic["priority"]] += len(tasks)
        required += sum(role not in {"H", "X"} for role in roles)

        lines = [
            f"## {number}. {topic['title']}",
            "",
            f"Приоритет **{topic['priority']}**. Задач: **{len(tasks)}**. "
            f"Связь с этапом и признаки распознавания: [ROADMAP.md — тема {number}](ROADMAP.md#тема-{number}).",
            "",
        ]
        if topic["lc"]:
            lc_links = [f"[LC {num} — {name}](https://leetcode.com/problems/{slug}/)" for num, name, slug in topic["lc"]]
            lines.extend(["База LeetCode, не входит в лимит: " + "; ".join(lc_links) + ".", ""])

        lines.extend(["| № | Задача | Рейтинг CF | Роль |", "|---:|---|---:|:---:|"])
        for idx, ((platform, task_id, name, rating), role) in enumerate(zip(tasks, roles), start=1):
            rating_text = str(rating) if rating else "—"
            lines.append(f"| {idx} | {task_link(platform, task_id, name)} | {rating_text} | `{role}` |")
        sections.append("\n".join(lines))

    grand_total = sum(totals.values())
    if grand_total != 282:
        raise AssertionError(f"Expected 282 tasks, got {grand_total}")

    intro = f"""# Банк задач

Этот каталог построен под календарь «лето → отборы в октябре–ноябре → финалы в марте–апреле». Он не требует решить все задачи подряд.

## Объём и маршрут

- приоритет A: **{totals['A']}** задач — фундамент и наиболее вероятные темы отборов;
- приоритет B: **{totals['B']}** задач — усиление после прохождения отбора;
- приоритет C: **{totals['C']}** задач — финальный и выборочный продвинутый слой;
- полный каталог: **{grand_total}** задач Codeforces/ACMP;
- основной маршрут без `H` и `X`: **{required}** задач;
- LeetCode вынесен отдельно и в эти числа не входит.

Роли: `D` — диагностика; `L` — изучение приёма; `R` — закрепление; `H` — трудная/stretch-задача; `F` — контрольная задача без подсказок; `X` — задача на сочетание тем. Для быстрого маршрута решать `D/L/R/F`; `H/X` переносить на финальный цикл или брать по слабым местам.

## Правила работы

1. До начала темы решить `D` за ограниченное время. Если идея не найдена, изучить теорию и перейти к `L`.
2. После каждой задачи записать не пересказ решения, а три пункта: признак темы, ключевой инвариант, ошибка реализации.
3. `F` решать как мини-контест: без подсказок, с полным тестированием и разбором после сдачи.
4. ACMP используется как русскоязычный вход и тренировка реализации; Codeforces — как основная шкала сложности.
5. Рейтинг Codeforces — ориентир, а не строгий порядок: редкая знакомая тема может оказаться легче незнакомой задачи с меньшим рейтингом.

"""
    OUTPUT.write_text(intro + "\n\n".join(sections) + "\n", encoding="utf-8")
    print(f"wrote {OUTPUT}: {grand_total} tasks, {required} on the core route")


if __name__ == "__main__":
    main()
