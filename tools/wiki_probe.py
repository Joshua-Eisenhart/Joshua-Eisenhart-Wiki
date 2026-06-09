#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path
from typing import Iterable

WIKILINK_RE = re.compile(r"\[\[([^\|]+?)(?:\|[^\|]*?)?\]\]")
HEADER_COUNT_RE = re.compile(r"Total(?:\s+(?:published|concept))?\s+pages:\s*(\d+)", re.IGNORECASE)
SPECIAL_NON_INDEXED = {"index", "log"}
SKIP_DIRS = {"raw", ".obsidian", ".git", "_archive", "_meta"}
PUBLISHED_ROOTS = {"entities", "concepts", "comparisons", "queries"}
MALFORMED_PATTERNS = {
    "triple_bracket": re.compile(r"\[\[\[[^\|]*\]\]\]"),
    "empty_wikilink": re.compile(r"\[\[\s*\]\]"),
}
STALE_NAMESPACE_TARGET_RE = re.compile(r"^(?:\.\./)*current/", re.IGNORECASE)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
INLINE_HTML_COMMENT_RE = re.compile(r"<!--.*?-->")

def extract_wikilinks(text: str) -> list[str]:
    links: list[str] = []
    for match in WIKILINK_RE.findall(text):
        target = match.split("|", 1)[0].split("#", 1)[0].strip()
        target = target.replace("\\", "/")
        target = target[:-3] if target.endswith(".md") else target
        target = Path(target).name
        links.append(target)
    return links

def iter_markdown_files(wiki_root: Path, roots: Iterable[str]) -> Iterable[Path]:
    for dirname in sorted(roots):
        root_dir = wiki_root / dirname
        if not root_dir.exists():
            continue
        for root, dirs, files in os.walk(root_dir):
            dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS and not d.startswith("."))
            for filename in sorted(files):
                if filename.startswith(".") or not filename.endswith(".md"):
                    continue
                yield Path(root) / filename

def iter_active_markdown_files(wiki_root: Path) -> Iterable[Path]:
    # Scan all non-raw, non-archive markdown surfaces that can participate in
    # active routing. Published-page counts remain limited to PUBLISHED_ROOTS.
    all_roots = [d for d in os.listdir(wiki_root) if os.path.isdir(wiki_root / d) and d not in SKIP_DIRS]
    yield from iter_markdown_files(wiki_root, all_roots)

def get_pages(wiki_root: Path) -> dict[str, str]:
    # Index EVERYTHING (including current, projects) for link resolution
    pages: dict[str, str] = {}
    for path in iter_active_markdown_files(wiki_root):
        rel = path.relative_to(wiki_root).as_posix()
        pages[path.stem] = rel
    return pages

def find_malformed_wikilinks(text: str) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    for pattern_name, pattern in MALFORMED_PATTERNS.items():
        for match in pattern.finditer(text):
            findings.append({"pattern": pattern_name, "snippet": match.group(0)})
    return findings


def iter_routing_markdown_lines(text: str) -> Iterable[tuple[int, str]]:
    """Yield lines whose wikilinks should count as active routing text.

    This deliberately skips fenced code blocks, inline code spans, and HTML
    comments so examples in docs/logs do not become hygiene findings.
    """
    in_fence = False
    in_html_comment = False
    for line_no, line in enumerate(text.splitlines(), start=1):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        work = line
        if in_html_comment:
            if "-->" in work:
                work = work.split("-->", 1)[1]
                in_html_comment = False
            else:
                continue
        while "<!--" in work:
            before, after = work.split("<!--", 1)
            if "-->" in after:
                work = before + after.split("-->", 1)[1]
            else:
                work = before
                in_html_comment = True
                break
        work = INLINE_HTML_COMMENT_RE.sub("", work)
        work = INLINE_CODE_RE.sub("", work)
        yield line_no, work


def find_stale_namespace_wikilinks(text: str) -> list[dict[str, str | int]]:
    findings: list[dict[str, str | int]] = []
    for line_no, line in iter_routing_markdown_lines(text):
        for match in WIKILINK_RE.finditer(line):
            target = match.group(1).split("#", 1)[0].strip().replace("\\", "/")
            target = target[:-3] if target.endswith(".md") else target
            if STALE_NAMESPACE_TARGET_RE.match(target):
                findings.append({
                    "line": line_no,
                    "target": target,
                    "reason": "retired current/ namespace; prefer hermes-current/ for Hermes front-door links",
                })
    return findings

def probe_wiki(wiki_root: Path | str, output_path: Path | str | None = None) -> dict:
    wiki_root = Path(wiki_root)
    all_pages = get_pages(wiki_root)

    # Count only public page roots. Raw notes and maintenance dirs may still
    # resolve links, but they are not published page count.
    published_pages_stems = set()
    published_pages_count = 0
    for path in iter_markdown_files(wiki_root, PUBLISHED_ROOTS):
        published_pages_count += 1
        published_pages_stems.add(path.stem)

    index_path = wiki_root / "index.md"
    index_text = index_path.read_text(encoding="utf-8")
    index_links = extract_wikilinks(index_text)
    indexed_targets = set(index_links)

    broken_links = []
    malformed = []
    stale_namespace_wikilinks = []

    for stem, rel_path in all_pages.items():
        text = (wiki_root / rel_path).read_text(encoding="utf-8")
        for finding in find_malformed_wikilinks(text):
            malformed.append({"source": rel_path, **finding})
        for target in extract_wikilinks(text):
            if target not in all_pages and target not in {"index", "log"}:
                broken_links.append({"source": rel_path, "target": target})

    for path in [index_path, *iter_active_markdown_files(wiki_root)]:
        rel_path = path.relative_to(wiki_root).as_posix()
        text = path.read_text(encoding="utf-8")
        for finding in find_stale_namespace_wikilinks(text):
            stale_namespace_wikilinks.append({"source": rel_path, **finding})

    stubs = [
        rel
        for stem, rel in all_pages.items()
        if stem in published_pages_stems and (wiki_root / rel).read_text(encoding="utf-8").count("\n") < 10
    ]

    header_count = 0
    match = HEADER_COUNT_RE.search(index_text)
    if match:
        header_count = int(match.group(1))

    missing_pages = sorted(
        target
        for target in indexed_targets
        if target not in all_pages and target not in SPECIAL_NON_INDEXED
    )

    payload = {
        "page_count": published_pages_count,
        "index_header_count": header_count,
        "indexed_link_count": len(indexed_targets),
        "missing_pages": missing_pages,
        "orphans": [s for s in published_pages_stems if s not in indexed_targets and s not in SPECIAL_NON_INDEXED],
        "broken_links": broken_links,
        "stubs": stubs,
        "malformed_wikilinks": malformed,
        "stale_namespace_wikilinks": stale_namespace_wikilinks,
    }

    if output_path is not None:
        Path(output_path).write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    return payload


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--wiki-root", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    probe_wiki(args.wiki_root, output_path=args.output)

if __name__ == "__main__":
    main()
