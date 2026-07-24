#!/usr/bin/env python3
"""Cheap, deterministic repository checks for the research deliverables."""

from __future__ import annotations

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
    text = (ROOT / "PRACTICE.md").read_text(encoding="utf-8")
    cf_ids = re.findall(r"\[CF ([0-9]+[A-Z][0-9]?) —", text)
    acmp_ids = re.findall(r"\[ACMP ([0-9]+) —", text)
    require(len(cf_ids) + len(acmp_ids) == 282, "practice task count is not 282")
    require(len(cf_ids) == len(set(cf_ids)), "duplicate Codeforces task IDs")
    require(len(acmp_ids) == len(set(acmp_ids)), "duplicate ACMP task IDs")
    require(len(re.findall(r"^## [0-9]+\. ", text, re.MULTILINE)) == 34, "practice topic count is not 34")
    require("приоритет A: **180**" in text, "priority A count missing")
    require("приоритет B: **77**" in text, "priority B count missing")
    require("приоритет C: **25**" in text, "priority C count missing")
    require("основной маршрут без `H` и `X`: **214**" in text, "core route count missing")


def main() -> None:
    for filename in [
        "research.md", "ROADMAP.md", "PRACTICE.md", "PROGRESS.md",
        "CONTEST_STRATEGY.md", "contests/MANIFEST.md", "templates/java/README.md",
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
