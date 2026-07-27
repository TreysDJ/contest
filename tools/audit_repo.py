#!/usr/bin/env python3
"""Cheap, deterministic repository checks for the research deliverables."""

from __future__ import annotations

import argparse
import html
import re
import sys
import unicodedata
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote, unquote, urldefrag, urlsplit
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
LINK_PATTERN = re.compile(r"!?\[[^\]]*]\(([^)]+)\)")
HEADING_PATTERN = re.compile(r"^(#{1,6})[ \t]+(.+?)(?:[ \t]+#+[ \t]*)?$")
EXPLICIT_ANCHOR_PATTERN = re.compile(
    r"""<a\b[^>]*\b(?:id|name)\s*=\s*["']([^"']+)["']""",
    re.IGNORECASE,
)
FENCE_PATTERN = re.compile(r"^\s*(`{3,}|~{3,})")
EXTERNAL_TIMEOUT_SECONDS = 10
EXTERNAL_WORKERS = 12
URL_SAFE_CHARACTERS = ":/?&=%#@+;,[]!$'()*"


def require(condition: bool, message: str) -> None:
    if not condition:
        ERRORS.append(message)


def link_target(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and target.endswith(">"):
        return target[1:-1]
    return target.split(maxsplit=1)[0]


def strip_heading_markup(heading: str) -> str:
    heading = re.sub(r"!\[([^\]]*)]\([^)]*\)", r"\1", heading)
    heading = re.sub(r"\[([^\]]+)]\([^)]*\)", r"\1", heading)
    heading = re.sub(r"<[^>]+>", "", heading)
    heading = html.unescape(heading)
    return heading.replace("`", "").replace("*", "").replace("~", "")


def github_heading_anchor(heading: str) -> str:
    """Apply GitHub's documented section-link rules to headings used here."""
    result: list[str] = []
    for character in strip_heading_markup(heading).strip().lower():
        if character == " ":
            result.append("-")
        elif character in {"-", "_"}:
            result.append(character)
        elif character.isalnum() or unicodedata.category(character).startswith("M"):
            result.append(character)
    return "".join(result)


def markdown_anchors(markdown: Path) -> set[str]:
    anchors: set[str] = set()
    heading_counts: dict[str, int] = {}
    fence: tuple[str, int] | None = None

    for line in markdown.read_text(encoding="utf-8").splitlines():
        fence_match = FENCE_PATTERN.match(line)
        if fence_match:
            marker = fence_match.group(1)
            if fence is None:
                fence = (marker[0], len(marker))
            elif marker[0] == fence[0] and len(marker) >= fence[1]:
                fence = None
            continue
        if fence is not None:
            continue

        anchors.update(EXPLICIT_ANCHOR_PATTERN.findall(line))
        heading_match = HEADING_PATTERN.match(line)
        if not heading_match:
            continue

        base = github_heading_anchor(heading_match.group(2))
        duplicate_index = heading_counts.get(base, 0)
        heading_counts[base] = duplicate_index + 1
        anchors.add(base if duplicate_index == 0 else f"{base}-{duplicate_index}")

    return anchors


def check_links() -> dict[str, tuple[Path, int]]:
    external_links: dict[str, tuple[Path, int]] = {}
    anchor_cache: dict[Path, set[str]] = {}

    for markdown in sorted(ROOT.rglob("*.md")):
        text = markdown.read_text(encoding="utf-8")
        for match in LINK_PATTERN.finditer(text):
            target = html.unescape(link_target(match.group(1)))
            line_number = text.count("\n", 0, match.start()) + 1

            if target.startswith(("http://", "https://")):
                request_url = urldefrag(target).url
                external_links.setdefault(request_url, (markdown, line_number))
                continue
            if target.startswith("mailto:"):
                continue

            path_part, fragment = urldefrag(target)
            resolved = (
                (markdown.parent / unquote(path_part)).resolve()
                if path_part
                else markdown.resolve()
            )
            location = f"{markdown.relative_to(ROOT)}:{line_number}"
            if not resolved.exists():
                require(False, f"broken local link in {location}: {target}")
                continue

            if fragment and resolved.suffix.lower() in {".md", ".markdown"}:
                anchors = anchor_cache.setdefault(resolved, markdown_anchors(resolved))
                decoded_fragment = unquote(fragment)
                require(
                    decoded_fragment in anchors,
                    f"broken local anchor in {location}: {target}",
                )

    return external_links


def probe_external_link(url: str) -> tuple[str, str]:
    encoded_url = quote(url, safe=URL_SAFE_CHARACTERS)
    request = Request(
        encoded_url,
        headers={
            "Accept": "*/*",
            "Accept-Encoding": "identity",
            "Connection": "close",
            "User-Agent": "contest-repository-link-check/1.0",
        },
        method="GET",
    )
    try:
        with urlopen(request, timeout=EXTERNAL_TIMEOUT_SECONDS) as response:
            status = response.getcode()
    except HTTPError as error:
        status = error.code
    except (URLError, TimeoutError, OSError, ValueError, UnicodeError) as error:
        return "unverified", str(error)

    if 200 <= status < 400:
        return "ok", f"HTTP {status}"
    if status in {404, 410}:
        return "broken", f"HTTP {status}"
    return "unverified", f"HTTP {status}"


def check_external_links(links: dict[str, tuple[Path, int]]) -> None:
    results: list[tuple[str, str, str]] = []
    with ThreadPoolExecutor(max_workers=EXTERNAL_WORKERS) as executor:
        futures = {
            executor.submit(probe_external_link, url): url
            for url in sorted(links)
        }
        for future in as_completed(futures):
            url = futures[future]
            status, detail = future.result()
            results.append((status, url, detail))

    counts = {"ok": 0, "broken": 0, "unverified": 0}
    unverified_groups: Counter[tuple[str, str]] = Counter()
    for status, url, detail in sorted(results):
        counts[status] += 1
        markdown, line_number = links[url]
        location = f"{markdown.relative_to(ROOT)}:{line_number}"
        if status == "broken":
            require(False, f"broken external link in {location}: {url} ({detail})")
        elif status == "unverified":
            unverified_groups[(urlsplit(url).netloc, detail)] += 1

    for (domain, detail), count in sorted(unverified_groups.items()):
        print(
            f"External links unverified: {count} on {domain} ({detail})",
            file=sys.stderr,
        )

    print(
        "External links: "
        f"{counts['ok']} OK, {counts['broken']} broken, "
        f"{counts['unverified']} unverified"
    )


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


def check_template_cross_references() -> None:
    readme_path = ROOT / "templates" / "java" / "README.md"
    readme = readme_path.read_text(encoding="utf-8")
    roadmap = (ROOT / "ROADMAP.md").read_text(encoding="utf-8")

    require(
        not re.search(r"https?://", readme),
        "templates/java/README.md duplicates external theory links; keep them in ROADMAP.md",
    )

    topic_matches = list(re.finditer(r'<a id="тема-(\d+)"></a>', roadmap))
    topic_sections: dict[int, str] = {}
    for index, match in enumerate(topic_matches):
        end = topic_matches[index + 1].start() if index + 1 < len(topic_matches) else len(roadmap)
        topic_sections[int(match.group(1))] = roadmap[match.start():end]

    anchor_matches = list(re.finditer(r'<a id="(template-[^"]+)"></a>', readme))
    require(anchor_matches, "template README has no stable template anchors")

    documented_files: set[str] = set()
    anchors: set[str] = set()
    for index, match in enumerate(anchor_matches):
        anchor = match.group(1)
        anchors.add(anchor)
        end = anchor_matches[index + 1].start() if index + 1 < len(anchor_matches) else len(readme)
        section = readme[match.start():end]

        java_files = [
            Path(target).name
            for target in re.findall(r"\[[^\]]*]\(([^)#]+\.java)\)", section)
        ]
        topics = {
            int(number)
            for number in re.findall(r"\.\./\.\./ROADMAP\.md#тема-(\d+)", section)
        }
        require(java_files, f"template section #{anchor} has no Java file")
        require(topics, f"template section #{anchor} has no ROADMAP topic")
        if java_files:
            primary_file = java_files[0]
            require(
                primary_file not in documented_files,
                f"Java file {primary_file} is primary in more than one template section",
            )
            documented_files.add(primary_file)

        backlink = f"templates/java/README.md#{anchor}"
        for topic in topics:
            require(topic in topic_sections, f"template section #{anchor} links missing topic {topic}")
            if topic in topic_sections:
                require(
                    backlink in topic_sections[topic],
                    f"ROADMAP topic {topic} has no backlink to #{anchor}",
                )

    actual_files = {path.name for path in (ROOT / "templates" / "java").glob("*.java")}
    require(
        documented_files == actual_files,
        "template README inventory differs from Java files: "
        f"missing={sorted(actual_files - documented_files)}, "
        f"extra={sorted(documented_files - actual_files)}",
    )

    roadmap_anchors = set(
        re.findall(r"templates/java/README\.md#(template-[^)]+)", roadmap)
    )
    require(
        roadmap_anchors == anchors,
        "ROADMAP/template anchor inventory differs: "
        f"missing in ROADMAP={sorted(anchors - roadmap_anchors)}, "
        f"unknown in ROADMAP={sorted(roadmap_anchors - anchors)}",
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--external-links",
        action="store_true",
        help="also check external HTTP(S) links",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    for filename in [
        "research.md", "ROADMAP.md", "PRACTICE.md", "PROGRESS.md",
        "CONTEST_STRATEGY.md", "contests/MANIFEST.md", "templates/java/README.md",
    ]:
        require((ROOT / filename).is_file(), f"missing deliverable: {filename}")
    external_links = check_links()
    check_contests()
    check_template_cross_references()
    if args.external_links:
        check_external_links(external_links)
    if ERRORS:
        print("Audit failed:")
        for error in ERRORS:
            print("-", error)
        return 1
    print("Repository audit: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
