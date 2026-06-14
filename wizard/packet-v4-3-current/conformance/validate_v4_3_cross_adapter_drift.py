#!/usr/bin/env python3
"""Validate current Wizard v4.3 cross-adapter drift on Josh's local Hermes/Claude/Codex surfaces.

authority_status: conformance
packet_version: v4.3

This validator is intentionally concrete and local. It checks the drift class found
in the 2026-06-13 full audit: active Hermes/Claude/Codex surfaces saying v4.3
while still loading v4.2/v4.1 paths or metadata.

It does not prove that a live model route executed. It proves the checked adapter
source surfaces no longer contain the known stale current-route strings and that
Codex v4.3 skill frontmatter parses as YAML when PyYAML is available.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover - PyYAML may be absent on minimal systems
    yaml = None

HOME = Path("/Users/joshuaeisenhart")

PATHS = {
    "hermes_profile": HOME / ".hermes/HERMES.md",
    "mmm_index": HOME / ".hermes/task-cards/MMM_RESERVOIR_CONTENT_INDEX.json",
    "hermes_manifest": HOME / "wiki/wizard/hermes-version-current/MANIFEST.md",
    "legacy_codex_adapter": HOME / "wiki/wizard/10-codex-three-council-adapter.md",
    "claude_wizard_council": HOME / "Codex-Ratchet/.claude/skills/wizard-council/SKILL.md",
}

CODEX_SKILL_ROOTS = [
    HOME / ".codex/skills/three-council-wizard-v4-3",
    HOME / ".codex-second/skills/three-council-wizard-v4-3",
    HOME / "Codex-Ratchet/system_v5/codex_skills/three-council-wizard-v4-3",
]

VOICE_DIR = HOME / "Codex-Ratchet/.claude/agents"
VOICE_FILES = [
    "voice-hume.md",
    "voice-zhuangzi.md",
    "voice-feynman.md",
    "voice-orwell.md",
    "voice-popper.md",
    "voice-pushback.md",
    "voice-factory.md",
    "voice-strategy.md",
    "voice-systems.md",
]

HERMES_SKILL_DRIFT_CHECKS = [
    (
        HOME / ".hermes/skills/software-development/hermes-wizard-v4-3-object-preservation/SKILL.md",
        "hermes_v43_object_skill_v42_mmm",
        [r"FULL_MMM_v4_2", r"COMPACT_MMM_v4_2", r"MEMBER_MINI_MMM_REGISTRY_v4_2"],
    ),
    (
        HOME / ".hermes/skills/note-taking/wiki-maintenance-and-harness/SKILL.md",
        "wiki_maintenance_skill_current_v42",
        [r"active Wizard v4\.2 MMM packet surfaces", r"wizard/packet-v4-2-current/mmm", r"For the current Wizard stack, v4\.2 is current", r"FULL_MMM_v4_2", r"COMPACT_MMM_v4_2"],
    ),
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def add_hit(findings: list[dict[str, Any]], code: str, path: Path, detail: str, line: int | None = None) -> None:
    findings.append({"code": code, "path": str(path), "line": line, "detail": detail})


def scan_for_patterns(findings: list[dict[str, Any]], path: Path, code: str, patterns: list[str]) -> None:
    if not path.exists():
        add_hit(findings, "missing_file", path, f"required file missing for {code}")
        return
    rx = re.compile("|".join(patterns))
    for i, line in enumerate(read(path).splitlines(), 1):
        if rx.search(line):
            add_hit(findings, code, path, line.strip(), i)


def check_json_index(findings: list[dict[str, Any]]) -> None:
    path = PATHS["mmm_index"]
    if not path.exists():
        add_hit(findings, "missing_mmm_index", path, "MMM index missing")
        return
    try:
        data = json.loads(read(path))
    except Exception as e:
        add_hit(findings, "mmm_index_json_parse", path, repr(e))
        return
    root = data.get("root")
    if root != "/Users/joshuaeisenhart/wiki/wizard/packet-v4-3-current/mmm/mini":
        add_hit(findings, "mmm_index_wrong_root", path, f"root={root!r}")
    missing = []
    stale = []
    for item in data.get("items", []):
        p = str(item.get("path", ""))
        if "packet-v4-2-current" in p or "MEMBER_MINI_MMM_REGISTRY_v4_2" in p:
            stale.append(p)
        if p and not Path(p).exists():
            missing.append(p)
    if stale:
        add_hit(findings, "mmm_index_stale_paths", path, f"{len(stale)} stale paths; first={stale[0]}")
    if missing:
        add_hit(findings, "mmm_index_missing_paths", path, f"{len(missing)} missing paths; first={missing[0]}")


def check_codex_skill(findings: list[dict[str, Any]], root: Path) -> None:
    skill = root / "SKILL.md"
    agent = root / "agents/openai.yaml"
    route_cards = root / "references/codex_v43_route_cards.md"
    for path in [skill, agent, route_cards]:
        if not path.exists():
            add_hit(findings, "missing_codex_v43_surface", path, "missing Codex v4.3 surface")
    if skill.exists():
        text = read(skill)
        if "description: Run or develop Wizard v4.3 as the current Wizard route:" in text:
            add_hit(findings, "codex_skill_unquoted_description", skill, "description still uses colon-rich plain scalar")
        if yaml is not None:
            try:
                fm = text.split("---", 2)[1]
                yaml.safe_load(fm)
            except Exception as e:
                add_hit(findings, "codex_skill_yaml_parse", skill, repr(e))
    if agent.exists():
        scan_for_patterns(findings, agent, "codex_agent_v42_current_route", [r"over Wizard v4\.2", r"before Wizard v4\.2"])
    if route_cards.exists():
        scan_for_patterns(
            findings,
            route_cards,
            "codex_route_cards_v42_mmm",
            [r"FULL_MMM_v4_2", r"COMPACT_MMM_v4_2", r"MEMBER_MINI_MMM_REGISTRY_v4_2"],
        )


def check_claude_voices(findings: list[dict[str, Any]]) -> None:
    scan_for_patterns(
        findings,
        PATHS["claude_wizard_council"],
        "claude_wizard_council_stale_packet",
        [r"packet-v4-2-current", r"packet-v4-1-current", r"SKILLS_MANIFEST_v4_2", r"COMPACT_MMM_v4_2"],
    )
    for name in VOICE_FILES:
        path = VOICE_DIR / name
        if not path.exists():
            add_hit(findings, "missing_voice_agent", path, "voice agent missing")
            continue
        text = read(path)
        if "packet-v4-2-current" in text or "packet-v4-1-current" in text:
            add_hit(findings, "voice_stale_packet_path", path, "voice still names old packet path")
        if "_v4_1" in text and "inherited filename provenance, not v4.1 routing" not in text:
            add_hit(findings, "voice_v41_suffix_unqualified", path, "voice mentions _v4_1 without provenance/non-routing qualification")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true", help="emit JSON")
    args = ap.parse_args()
    findings: list[dict[str, Any]] = []

    scan_for_patterns(findings, PATHS["hermes_profile"], "hermes_profile_v42_mmm_loader", [r"COMPACT_MMM_v4_2", r"FULL_MMM_v4_2"])
    check_json_index(findings)
    scan_for_patterns(findings, PATHS["hermes_manifest"], "hermes_manifest_current_v42", [r"current Wizard v4\.2 loop work", r"preflight over v4\.2 councils"])
    if PATHS["legacy_codex_adapter"].exists():
        text = read(PATHS["legacy_codex_adapter"])
        if re.search(r"^framing:\s*current\s*$", text, re.M):
            add_hit(findings, "legacy_codex_adapter_current", PATHS["legacy_codex_adapter"], "legacy adapter still framed current")

    for root in CODEX_SKILL_ROOTS:
        check_codex_skill(findings, root)
    check_claude_voices(findings)
    for path, code, patterns in HERMES_SKILL_DRIFT_CHECKS:
        scan_for_patterns(findings, path, code, patterns)

    result = {
        "ok": not findings,
        "findings": findings,
        "checked": {
            "codex_skill_roots": [str(p) for p in CODEX_SKILL_ROOTS],
            "voice_files": [str(VOICE_DIR / name) for name in VOICE_FILES],
            "hermes_profile": str(PATHS["hermes_profile"]),
            "mmm_index": str(PATHS["mmm_index"]),
        },
        "evidence_boundary": "source-surface drift check only; does not prove live model route execution",
    }
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        if result["ok"]:
            print("PASS")
        else:
            print("FAIL")
            for f in findings:
                loc = f.get("path", "") + ((":" + str(f.get("line"))) if f.get("line") else "")
                print(f"- {f['code']} {loc}: {f['detail']}")
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
