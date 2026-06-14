#!/usr/bin/env python3
"""Validate Wizard v4.3 packet SHAPE and structure conformance only.

CEILING: this validator checks shape, structure, and volume — NOT runtime
correctness or semantic proof. A padded shell with correct file layout will
pass. A token-overlap counterfeit scored at 1.0 overlap will pass. Passing
this validator does NOT mean the packet is correct, complete, or safe to run.
It means the packet has the required files, volume thresholds, route names,
and version labels. Runtime semantic proof requires independent execution
and audit in a fresh context.

check_class: shape_conformance_not_runtime_proof
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASELINE_V42 = Path.home() / "wiki/wizard/packet-v4-2-current"

REQUIRED_FILES = [
    "PACKET_MANIFEST_v4_3.md",
    "README.md",
    "WIZARD_v4_3.md",
    "mmm/README.md",
    "mmm/FULL_MMM_v4_3.md",
    "mmm/COMPACT_MMM_v4_3.md",
    "mmm/mini/MEMBER_MINI_MMM_REGISTRY_v4_3.md",
    "skills/SKILLS_MANIFEST_v4_3.md",
    "skills/premortem/SKILL.md",
    "skills/claude-bridge/SKILL.md",
    "skills/claude-bridge/scripts/claude_bridge.py",
    "skills/claude-bridge/scripts/claude_child_fanout.py",
    "skills/claude-bridge/scripts/fanout_receipt_summary.py",
    "skills/council-members/loophole-auditor/SKILL.md",
    "skills/council-members/factory-handoff/SKILL.md",
    "skills/council-members/follow-up-selector/SKILL.md",
    "skills/council-members/strategy-loop/SKILL.md",
    "skills/council-members/systems-strategy/SKILL.md",
    "agents/AGENTS_MANIFEST_v4_3.md",
    "agents/README.md",
    "agents/templates/AGENT_SPEC_v4_3.md",
    "agents/wizard-loop/route-truth-agent.md",
    "agents/wizard-loop/evidence-mapper.md",
    "agents/wizard-loop/falsifier-agent.md",
    "agents/wizard-loop/premortem-agent.md",
    "agents/wizard-loop/scout-runner.md",
    "agents/wizard-loop/selector-compiler.md",
    "agents/wizard-loop/prompt-packetizer.md",
    "agents/wizard-loop/route-sequencer.md",
    "agents/wizard-loop/scope-keeper.md",
    "agents/voices/voice-hume.md",
    "agents/voices/voice-zhuangzi.md",
    "agents/voices/voice-feynman.md",
    "agents/voices/voice-orwell.md",
    "agents/voices/voice-popper.md",
    "agents/voices/voice-pushback.md",
    "agents/voices/voice-factory.md",
    "agents/voices/voice-strategy.md",
    "agents/voices/voice-systems.md",
    "agents/auditors/council-collapse-auditor.md",
    "taskcards/TASKCARDS_MANIFEST_v4_3.md",
    "taskcards/PARENT_ROUTE_TASK_CARD_SCHEMA_v4_3.md",
    "taskcards/CHILD_TASK_CARD_SCHEMA_v4_3.md",
    "taskcards/SUBAGENT_BOOT_RULES_v4_3.md",
    "taskcards/SUBSUBAGENT_BOOT_RULES_v4_3.md",
    "taskcards/templates/SUBAGENT_TASK_CARD_v4_3.md",
    "taskcards/templates/PARENT_ROUTE_TASK_CARD_v4_3.md",
]

FORBIDDEN_JUNK_NAMES = {".DS_Store"}
FORBIDDEN_SUFFIXES = {".pyc"}

PARENT_ROUTES = [
    "decision.context_strategy",
    "decision.move_selection",
    "decision.evidence_boundary",
    "failure.premortem",
    "failure.falsifier",
    "failure.loophole_auditor",
    "follow_up.next_move_selector",
    "follow_up.lane_builder",
    "follow_up.compile_gate",
]

MANAGERS = [
    "manager.run_controller",
    "manager.child_health",
    "manager.route_truth",
    "manager.output_compiler",
    "manager.strategy_memory",
]


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def read(path: str | Path) -> str:
    p = ROOT / path if isinstance(path, str) else path
    return p.read_text(encoding="utf-8", errors="replace")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


def line_count(path: str) -> int:
    return len(read(path).splitlines())


def token_overlap(left: str, right: str) -> float:
    left_tokens = set(re.findall(r"[A-Za-z0-9_./:-]+", left.lower()))
    right_tokens = set(re.findall(r"[A-Za-z0-9_./:-]+", right.lower()))
    if not left_tokens or not right_tokens:
        return 0.0
    return len(left_tokens & right_tokens) / len(right_tokens)


def check_required(errors: list[str]) -> None:
    for item in REQUIRED_FILES:
        path = ROOT / item
        if not path.exists():
            errors.append(f"missing required file: {item}")
            continue
        if path.suffix == ".md" and "authority_status:" not in path.read_text(encoding="utf-8", errors="replace")[:2000]:
            errors.append(f"missing authority_status in runtime-bearing file: {item}")


def check_no_junk(errors: list[str]) -> None:
    for path in ROOT.rglob("*"):
        if path.name in FORBIDDEN_JUNK_NAMES or path.suffix in FORBIDDEN_SUFFIXES or path.name == "__pycache__":
            errors.append(f"generated/junk file in packet: {rel(path)}")


def check_mmm(errors: list[str]) -> None:
    thresholds = {
        "mmm/FULL_MMM_v4_3.md": 30000,
        "mmm/COMPACT_MMM_v4_3.md": 3000,
        "mmm/mini/MEMBER_MINI_MMM_REGISTRY_v4_3.md": 500,
    }
    for path, minimum in thresholds.items():
        actual = line_count(path)
        if actual < minimum:
            errors.append(f"MMM appears collapsed/truncated: {path} has {actual} lines, expected at least {minimum}")

    mini_md = sorted((ROOT / "mmm/mini").rglob("*.md"))
    if len(mini_md) < 40:
        errors.append(f"mini-MMM reservoir appears incomplete: found {len(mini_md)} markdown files, expected at least 40")

    # Main v4.3 MMMs should be seeded from the v4.2 runtime reservoir, not summaries.
    baseline_pairs = [
        ("mmm/FULL_MMM_v4_3.md", BASELINE_V42 / "mmm/FULL_MMM_v4_2.md", 0.90),
        ("mmm/COMPACT_MMM_v4_3.md", BASELINE_V42 / "mmm/COMPACT_MMM_v4_2.md", 0.90),
    ]
    for current_rel, baseline_path, threshold in baseline_pairs:
        if not baseline_path.exists():
            errors.append(f"missing v4.2 MMM baseline for content check: {baseline_path}")
            continue
        overlap = token_overlap(read(current_rel), baseline_path.read_text(encoding="utf-8", errors="replace"))
        if overlap < threshold:
            errors.append(f"MMM baseline overlap too low: {current_rel} overlap={overlap:.3f}, expected >= {threshold}")


def check_runtime(errors: list[str]) -> None:
    wizard = read("WIZARD_v4_3.md")
    if line_count("WIZARD_v4_3.md") < 250:
        errors.append(f"WIZARD_v4_3.md appears collapsed/truncated: {line_count('WIZARD_v4_3.md')} lines")
    for phrase in [
        "Council sequence:",
        "decision.context_strategy",
        "failure.premortem",
        "follow_up.compile_gate",
        "Management parents:",
        "action_class",
        "execution_claim_state",
        "proof_depth",
        "premortem",
        "loophole",
        "not_run",
        "blocked",
    ]:
        if phrase not in wizard:
            errors.append(f"WIZARD_v4_3.md missing runtime phrase: {phrase}")
    for route in PARENT_ROUTES + MANAGERS:
        if route not in wizard:
            errors.append(f"WIZARD_v4_3.md missing route: {route}")


def check_skills(errors: list[str]) -> None:
    manifest = read("skills/SKILLS_MANIFEST_v4_3.md")
    for phrase in ["premortem", "claude-bridge", "loophole-auditor", "factory-handoff", "follow-up-selector", "strategy-loop", "systems-strategy"]:
        if phrase not in manifest:
            errors.append(f"skills manifest missing skill entry: {phrase}")
    for py in sorted((ROOT / "skills").rglob("*.py")):
        try:
            ast.parse(py.read_text(encoding="utf-8", errors="replace"))
        except SyntaxError as exc:
            errors.append(f"python syntax error in {rel(py)}: {exc}")


def check_v43_names(errors: list[str]) -> None:
    active_files = [
        "README.md", "PACKET_MANIFEST_v4_3.md", "00_READ_FIRST.md", "WIZARD_v4_3.md",
        "skills/SKILLS_MANIFEST_v4_3.md",
        "agents/AGENTS_MANIFEST_v4_3.md", "taskcards/TASKCARDS_MANIFEST_v4_3.md",
        # Registry included: it is an active runtime file and must not contain v4.2 framing.
        "mmm/mini/MEMBER_MINI_MMM_REGISTRY_v4_3.md",
    ]
    # Hard name tokens: file/artifact names that must not appear in active v4.3 files.
    forbidden_name_tokens = [
        "PACKET_MANIFEST_v4_2", "WIZARD_v4_2", "SKILLS_MANIFEST_v4_2",
        "FULL_MMM_v4_2", "COMPACT_MMM_v4_2", "MEMBER_MINI_MMM_REGISTRY_v4_2",
    ]
    # Prose phrases: version framing that incorrectly labels this packet as v4.2.
    forbidden_prose_phrases = [
        "this v4.2 packet",
        "Wizard v4.2 and repo authority control runtime",
        "v4.2 packet.",
    ]
    for relp in active_files:
        text = read(relp)
        for forbidden in forbidden_name_tokens:
            if forbidden in text:
                errors.append(f"active v4.3 file still routes through {forbidden}: {relp}")
        for phrase in forbidden_prose_phrases:
            if phrase in text:
                errors.append(f"active v4.3 file contains v4.2 prose framing ({phrase!r}): {relp}")



def check_agents_taskcards(errors: list[str]) -> None:
    agents = ROOT / "agents"
    taskcards = ROOT / "taskcards"
    if not agents.exists():
        errors.append("missing agents directory")
        return
    if not taskcards.exists():
        errors.append("missing taskcards directory")
        return

    parent_specs = sorted((agents / "parents").glob("*.md"))
    manager_specs = sorted((agents / "managers").glob("*.md"))
    wizard_loop_specs = sorted((agents / "wizard-loop").glob("*.md"))
    voice_specs = sorted((agents / "voices").glob("*.md"))
    auditor_specs = sorted((agents / "auditors").glob("*.md"))
    if len(parent_specs) < 9:
        errors.append(f"parent agent specs incomplete: found {len(parent_specs)}, expected >= 9")
    if len(manager_specs) < 5:
        errors.append(f"manager agent specs incomplete: found {len(manager_specs)}, expected >= 5")
    if len(wizard_loop_specs) < 9:
        errors.append(f"wizard-loop agent specs incomplete: found {len(wizard_loop_specs)}, expected >= 9")
    if len(voice_specs) < 9:
        errors.append(f"voice agent specs incomplete: found {len(voice_specs)}, expected >= 9")
    if len(auditor_specs) < 1:
        errors.append("auditor agent specs incomplete: missing collapse auditor")

    manifest = read("agents/AGENTS_MANIFEST_v4_3.md")
    for route in PARENT_ROUTES + MANAGERS:
        if route not in manifest and f"{route}.md" not in manifest:
            errors.append(f"agents manifest missing route/spec: {route}")
    for voice in ["voice-hume", "voice-zhuangzi", "voice-feynman", "voice-orwell", "voice-popper", "voice-pushback", "voice-factory", "voice-strategy", "voice-systems"]:
        path = agents / "voices" / f"{voice}.md"
        if not path.exists():
            errors.append(f"missing voice agent spec: {voice}")
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if "packet-v4-2-current" in text or "WIZARD_v4_2" in text:
            errors.append(f"voice agent still points at old runtime: {rel(path)}")
        if "slices_loaded" not in text:
            errors.append(f"voice agent missing slices_loaded receipt field: {rel(path)}")

    for relp in [
        "taskcards/SUBAGENT_BOOT_RULES_v4_3.md",
        "taskcards/SUBSUBAGENT_BOOT_RULES_v4_3.md",
        "taskcards/CHILD_TASK_CARD_SCHEMA_v4_3.md",
        "taskcards/PARENT_ROUTE_TASK_CARD_SCHEMA_v4_3.md",
    ]:
        text = read(relp)
        for phrase in ["agent_spec", "task_card", "proof_depth"]:
            if phrase not in text:
                errors.append(f"taskcard surface missing {phrase}: {relp}")


def build_report() -> dict:
    files = [p for p in ROOT.rglob("*") if p.is_file()]
    return {
        "check_class": "shape_conformance_not_runtime_proof",
        "packet": str(ROOT),
        "file_count": len(files),
        "wizard_lines": line_count("WIZARD_v4_3.md") if (ROOT / "WIZARD_v4_3.md").exists() else 0,
        "mmm_markdown_count": len(list((ROOT / "mmm").rglob("*.md"))) if (ROOT / "mmm").exists() else 0,
        "agent_spec_count": len(list((ROOT / "agents").rglob("*.md"))) if (ROOT / "agents").exists() else 0,
        "taskcard_file_count": len(list((ROOT / "taskcards").rglob("*.md"))) if (ROOT / "taskcards").exists() else 0,
        "digests": {item: digest(ROOT / item) for item in REQUIRED_FILES if (ROOT / item).exists()},
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    errors: list[str] = []
    for check in [check_required, check_no_junk, check_mmm, check_runtime, check_skills, check_agents_taskcards, check_v43_names]:
        check(errors)
    report = build_report()
    report["ok"] = not errors
    report["errors"] = errors
    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print("check_class=" + report["check_class"])
        print("ok=" + str(report["ok"]).lower())
        for error in errors:
            print("ERROR:", error)
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
