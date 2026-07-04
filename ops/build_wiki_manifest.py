#!/usr/bin/env python3
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "ops" / "wiki_manifest_20260702.jsonl"
SUMMARY = ROOT / "ops" / "wiki_manifest_20260702_summary.json"
MISSING_FRONTMATTER = ROOT / "ops" / "missing_frontmatter_20260702.txt"

EXTENSIONS = {".md", ".txt"}
STALE_BEFORE = (2026, 5)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read_text(path: Path) -> str:
    data = path.read_bytes()
    return data.decode("utf-8", errors="replace")


def split_frontmatter(text: str):
    if not text.startswith("---\n"):
        return False, None, text, None, None
    end = text.find("\n---", 4)
    if end == -1:
        return False, None, text, None, None
    close_end = text.find("\n", end + 1)
    if close_end == -1:
        close_end = len(text)
    frontmatter = text[4:end]
    body = text[close_end + 1 :] if close_end < len(text) else ""
    return True, frontmatter, body, 0, close_end + 1


def frontmatter_status(frontmatter: str | None):
    if not frontmatter:
        return None
    match = re.search(r"(?mi)^\s*status\s*:\s*(.*?)\s*$", frontmatter)
    if not match:
        return None
    value = match.group(1).strip()
    return value.strip("'\"") if value else ""


def first_title_or_line(text: str, body: str) -> str | None:
    for line in body.splitlines():
        stripped = line.strip()
        if stripped:
            return stripped.lstrip("#").strip() or stripped
    for line in text.splitlines():
        stripped = line.strip()
        if stripped and stripped != "---":
            return stripped.lstrip("#").strip() or stripped
    return None


def old_date_found(surface: str) -> bool:
    for year, month, _day in re.findall(r"\b(20\d{2})[-_/](\d{1,2})[-_/](\d{1,2})\b", surface):
        y = int(year)
        m = int(month)
        if (y, m) < STALE_BEFORE:
            return True
    for year, month, _day in re.findall(r"\b(20\d{2})(\d{2})(\d{2})\b", surface):
        y = int(year)
        m = int(month)
        if (y, m) < STALE_BEFORE:
            return True
    return False


def stale_reason(path: Path, frontmatter: str | None, title: str | None):
    surface = "\n".join(part for part in [rel(path), frontmatter or "", title or ""] if part)
    lower = surface.lower()
    checks = [
        (r"\bclaimgate\b", "references claimgate branch"),
        (r"\bpatch\b|\bwaverun\b|\bwave-run\b|\bwave run\b", "references patch/waverun artifact"),
        (r"\bold wizard\b", "references old wizard"),
        (r"\bsuperseded\b|\bdeprecated\b|\bobsolete\b|\bretired\b", "explicit superseded/deprecated wording"),
    ]
    for pattern, reason in checks:
        if re.search(pattern, lower):
            return reason
    if old_date_found(surface):
        return "dated before 2026-05"
    if re.search(r"\bdraft\b", lower) and old_date_found(surface):
        return "draft predates 2026-05 superseder window"
    return None


def superseded_by_for(reason: str) -> str:
    if "claimgate" in reason:
        return "current canon-gated branch state"
    if "patch/waverun" in reason:
        return "current wave/canon receipts"
    if "old wizard" in reason:
        return "current Wizard v4.3 materials"
    if "2026-05" in reason:
        return "post-2026-05 current wiki canon"
    if "superseded/deprecated" in reason:
        return "current replacement document"
    return "current wiki canon"


def yaml_quote(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def add_superseded_status(path: Path, reason: str):
    text = read_text(path)
    has_fm, frontmatter, _body, _start, body_start = split_frontmatter(text)
    if not has_fm or frontmatter_status(frontmatter) is not None:
        return False
    insert = (
        f"status: superseded\n"
        f"superseded_by: {yaml_quote(superseded_by_for(reason))}\n"
        f"reason: {yaml_quote(reason)}\n"
    )
    new_text = text[: body_start - 4] + insert + text[body_start - 4 :]
    path.write_text(new_text, encoding="utf-8")
    return True


def iter_docs():
    for path in sorted(ROOT.rglob("*")):
        if ".git" in path.parts:
            continue
        if not path.is_file():
            continue
        if path.suffix.lower() not in EXTENSIONS:
            continue
        yield path


def build():
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    records = []
    stale_candidates = []
    missing_frontmatter = []

    for path in iter_docs():
        stat = path.stat()
        text = read_text(path)
        has_fm, frontmatter, body, _start, _body_start = split_frontmatter(text)
        title = first_title_or_line(text, body)
        status = frontmatter_status(frontmatter) if has_fm else None
        reason = stale_reason(path, frontmatter, title)
        record = {
            "path": rel(path),
            "bytes": stat.st_size,
            "mtime_iso": datetime.fromtimestamp(stat.st_mtime, timezone.utc).isoformat(),
            "has_frontmatter": has_fm,
            "status_field": status,
            "title_or_head": title,
            "stale_signal": reason is not None,
        }
        records.append(record)
        if reason is not None:
            stale_candidates.append((path, record, reason))
        if not has_fm:
            missing_frontmatter.append(rel(path))

    with MANIFEST.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, sort_keys=True) + "\n")

    stale_marked = 0
    for path, record, reason in stale_candidates:
        if record["has_frontmatter"] and record["status_field"] is None:
            if add_superseded_status(path, reason):
                stale_marked += 1

    MISSING_FRONTMATTER.write_text(
        "\n".join(missing_frontmatter) + ("\n" if missing_frontmatter else ""),
        encoding="utf-8",
    )

    summary = {
        "total": len(records),
        "stale_signal": len(stale_candidates),
        "stale_marked": stale_marked,
        "no_frontmatter": len(missing_frontmatter),
        "manifest": rel(MANIFEST),
        "missing_frontmatter": rel(MISSING_FRONTMATTER),
    }
    SUMMARY.write_text(json.dumps(summary, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    build()
