#!/usr/bin/env python3
"""
wiki_consistency_continuous.py -- nightly wiki consistency auditor.

Runs three passes over /Users/joshuaeisenhart/wiki:
  1. Page count reconciliation (filesystem .md count vs index.md claim)
  2. Dead wikilink audit ([[target]] tokens that don't resolve to a file)
  3. Archive/active name collisions (same slug in concepts/ and concepts/_archive/)

Writes a timestamped punch list to /Users/joshuaeisenhart/wiki/audits/
and a rolling latest.md. Intended for cron. Read-only against the wiki.
"""

import datetime as dt
import pathlib
import re

WIKI = pathlib.Path("/Users/joshuaeisenhart/wiki")
CONCEPTS = WIKI / "concepts"
ARCHIVE = CONCEPTS / "_archive"
INDEX = WIKI / "index.md"
AUDITS = WIKI / "audits"

WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
INDEX_PAGE_CLAIM = re.compile(r"(\d{2,4})\s*(?:pages|concepts)", re.IGNORECASE)


def md_files(root):
    return [p for p in root.rglob("*.md") if p.is_file()]


def reconcile_page_count():
    fs_all = md_files(WIKI)
    fs_concepts = [p for p in md_files(CONCEPTS) if ARCHIVE not in p.parents]
    fs_archive = md_files(ARCHIVE) if ARCHIVE.exists() else []
    claim_nums = []
    if INDEX.exists():
        claim_nums = [int(m.group(1)) for m in INDEX_PAGE_CLAIM.finditer(INDEX.read_text())]
    return {
        "fs_total_md": len(fs_all),
        "fs_concepts_active": len(fs_concepts),
        "fs_concepts_archived": len(fs_archive),
        "index_page_claims": claim_nums,
    }


def resolve_slug(slug, slug_index):
    key = slug.strip().lower().replace(" ", "-")
    return slug_index.get(key)


def dead_wikilinks():
    slug_index = {}
    for p in md_files(WIKI):
        slug_index[p.stem.lower()] = p
    dead = []
    for p in md_files(WIKI):
        try:
            text = p.read_text()
        except Exception:
            continue
        for m in WIKILINK.finditer(text):
            target = m.group(1)
            if not resolve_slug(target, slug_index):
                dead.append({"file": str(p.relative_to(WIKI)), "target": target})
    return dead


def archive_collisions():
    if not ARCHIVE.exists():
        return []
    active = {p.stem for p in md_files(CONCEPTS) if ARCHIVE not in p.parents}
    archived = {p.stem for p in md_files(ARCHIVE)}
    return sorted(active & archived)


def render(report):
    lines = [f"# Wiki Consistency Audit -- {report['timestamp']}", ""]
    pc = report["page_count"]
    lines += [
        "## Page counts",
        f"- filesystem total .md: {pc['fs_total_md']}",
        f"- concepts/ active: {pc['fs_concepts_active']}",
        f"- concepts/_archive: {pc['fs_concepts_archived']}",
        f"- index.md claims: {pc['index_page_claims']}",
        "",
        f"## Dead wikilinks ({len(report['dead_links'])})",
    ]
    for d in report["dead_links"][:200]:
        lines.append(f"- `{d['file']}` -> [[{d['target']}]]")
    if len(report["dead_links"]) > 200:
        lines.append(f"- ... {len(report['dead_links']) - 200} more")
    lines += ["", f"## Archive/active slug collisions ({len(report['collisions'])})"]
    for s in report["collisions"]:
        lines.append(f"- {s}")
    return "\n".join(lines) + "\n"


def main():
    AUDITS.mkdir(parents=True, exist_ok=True)
    report = {
        "timestamp": dt.datetime.now().isoformat(timespec="seconds"),
        "page_count": reconcile_page_count(),
        "dead_links": dead_wikilinks(),
        "collisions": archive_collisions(),
    }
    md = render(report)
    stamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    (AUDITS / f"consistency_{stamp}.md").write_text(md)
    (AUDITS / "latest.md").write_text(md)
    print(f"wrote audits/consistency_{stamp}.md")
    print(f"dead_links={len(report['dead_links'])} collisions={len(report['collisions'])}")


if __name__ == "__main__":
    main()
