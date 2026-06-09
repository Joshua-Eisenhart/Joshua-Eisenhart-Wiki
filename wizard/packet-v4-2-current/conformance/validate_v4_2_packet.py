#!/usr/bin/env python3
"""Validate Wizard v4.2 packet shape and embedded runtime invariants."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = Path("/Users/joshuaeisenhart/Desktop/Codex Ratchet")
BASELINE_MMM_ROOT = Path.home() / "wiki/wizard/packet-v4-1-current/mmm"

REQUIRED_FILES = [
    "PACKET_MANIFEST_v4_2.md",
    "README.md",
    "WIZARD_v4_2.md",
    "mmm/FULL_MMM_v4_2.md",
    "mmm/COMPACT_MMM_v4_2.md",
    "mmm/mini/MEMBER_MINI_MMM_REGISTRY_v4_2.md",
    "skills/SKILLS_MANIFEST_v4_2.md",
    "skills/premortem/SKILL.md",
    "skills/claude-bridge/SKILL.md",
    "skills/council-members/loophole-auditor/SKILL.md",
    "skills/council-members/factory-handoff/SKILL.md",
    "skills/council-members/follow-up-selector/SKILL.md",
    "skills/council-members/strategy-loop/SKILL.md",
    "skills/council-members/systems-strategy/SKILL.md",
]

REMOVED_DOC_PATHS = [
    "WIZARD_FULL_v4_2.md",
    "WIZARD_COMPACT_v4_2.md",
    "topology/ROUTE_GRAPH_v4_2.yaml",
    "schemas/RECEIPT_SCHEMA_v4_2.md",
    "schemas/OUTPUT_SCHEMA_v4_2.md",
    "taskcards/TASK_CARD_SCHEMA_v4_2.md",
    "docs/EXTERNAL_CHECK_PROTOCOL_v4_2.md",
    "adapters/CODEX_ADAPTER_v4_2.md",
]

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


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


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


def check_static(errors: list[str]) -> None:
    for item in REQUIRED_FILES:
        path = ROOT / item
        if not path.exists():
            errors.append(f"missing required file: {item}")
            continue
        if "authority_status:" not in path.read_text(encoding="utf-8"):
            errors.append(f"missing authority_status: {item}")

    for item in REMOVED_DOC_PATHS:
        if (ROOT / item).exists():
            errors.append(f"doc sprawl path should not exist: {item}")

    for junk in list(ROOT.rglob(".DS_Store")) + list(ROOT.rglob("__pycache__")) + list(ROOT.rglob("*.pyc")):
        errors.append(f"generated/junk file in packet: {rel(junk)}")

    mmm_thresholds = {
        "mmm/FULL_MMM_v4_2.md": 30000,
        "mmm/COMPACT_MMM_v4_2.md": 3000,
        "mmm/mini/MEMBER_MINI_MMM_REGISTRY_v4_2.md": 500,
    }
    for path, minimum in mmm_thresholds.items():
        actual = line_count(path)
        if actual < minimum:
            errors.append(f"MMM appears collapsed/truncated: {path} has {actual} lines, expected at least {minimum}")

    baseline_pairs = [
        ("mmm/FULL_MMM_v4_2.md", BASELINE_MMM_ROOT / "FULL_MMM_v4_1.md", 0.95),
        ("mmm/COMPACT_MMM_v4_2.md", BASELINE_MMM_ROOT / "COMPACT_MMM_v4_1.md", 0.95),
    ]
    for current_rel, baseline_path, threshold in baseline_pairs:
        if not baseline_path.exists():
            errors.append(f"missing v4.1 MMM baseline for content check: {baseline_path}")
            continue
        overlap = token_overlap(read(current_rel), baseline_path.read_text(encoding="utf-8", errors="replace"))
        if overlap < threshold:
            errors.append(f"MMM semantic baseline overlap too low: {current_rel} overlap={overlap:.3f}, expected >= {threshold}")

    mini_md = sorted((ROOT / "mmm/mini").rglob("*.md"))
    if len(mini_md) < 40:
        errors.append(f"mini-MMM reservoir appears incomplete: found {len(mini_md)} markdown files, expected at least 40")
    for path in mini_md:
        mini_text = path.read_text(encoding="utf-8", errors="replace")
        lines = mini_text.splitlines()
        rel_path = rel(path)
        if "authority_status: canonical-runtime" not in mini_text[:1000]:
            errors.append(f"mini-MMM missing v4.2 authority overlay: {rel_path}")
        if "v4_2_overlay:" not in mini_text[:1000]:
            errors.append(f"mini-MMM missing v4.2 runtime overlay: {rel_path}")
        if len(lines) < 100 and "ALL_OF_THE_ABOVE" not in path.name:
            errors.append(f"mini-MMM appears collapsed/truncated: {rel_path} has {len(lines)} lines")
        if path.name == "MEMBER_MINI_MMM_REGISTRY_v4_2.md":
            baseline_path = BASELINE_MMM_ROOT / "mini/MEMBER_MINI_MMM_REGISTRY_v4_1.md"
        else:
            baseline_path = BASELINE_MMM_ROOT / path.relative_to(ROOT / "mmm")
        if not baseline_path.exists():
            errors.append(f"missing v4.1 mini-MMM baseline for content check: {rel_path}")
            continue
        overlap = token_overlap(mini_text, baseline_path.read_text(encoding="utf-8", errors="replace"))
        if overlap < 0.85:
            errors.append(f"mini-MMM semantic baseline overlap too low: {rel_path} overlap={overlap:.3f}, expected >= 0.85")

    wizard = read("WIZARD_v4_2.md")
    for phrase in [
        "Council sequence:",
        "decision.context_strategy",
        "failure.premortem",
        "follow_up.compile_gate",
        "Management parents:",
        "voice receipts cannot satisfy parent route completion",
        "Child receipt fields:",
        "compact_mmm_loaded",
        "required_mini_mmms_loaded",
        "optional_mini_mmms_loaded",
        "source_language_overlay_loaded",
        "which_loaded_slice_changed_output",
        "function-fit mini-MMM slices",
        "Allowed management intervention verbs:",
        "Premortem and Opus audit are separate steps",
        "Reject log-shaped output",
        "Preserve this shape",
        "## ✨ Answer",
        "## 🧭 Context + Strategy",
        "prompt-and-context engineering system",
        "larger context it belongs to",
        "strategy/state that must carry forward",
        "local-overoptimization risk",
        "Follow-up options are generated from the prompt plus the larger context plus strategy state",
        "## 🧠 What We Learned",
        "### ✅ Solid",
        "### ⚠️ Still Weak",
        "## ✅ Compiled Move",
        "## 🧭 Follow-Up Options",
        "## 🧙 Footer",
        "🧙 Time/value:",
        "⚠️ Honest status:",
    ]:
        if phrase not in wizard:
            errors.append(f"WIZARD_v4_2 missing embedded runtime phrase: {phrase}")

    for route in PARENT_ROUTES:
        if wizard.count(route) < 2:
            errors.append(f"parent route not fully embedded: {route}")
    for manager in MANAGERS:
        if manager not in wizard:
            errors.append(f"manager missing from Wizard doc: {manager}")

    referenced_mini_mmms = sorted(set(re.findall(r"`(mmm/mini/[^`]+\.md)`", wizard)))
    if len(referenced_mini_mmms) < 9:
        errors.append(f"embedded child definitions reference too few mini-MMMs: {len(referenced_mini_mmms)}")
    for path in referenced_mini_mmms:
        if not (ROOT / path).exists():
            errors.append(f"embedded child definition references missing mini-MMM: {path}")

    if any(token in wizard for token in ["decision.voices_council", "decision.six_hats_council", "decision.experts_council"]):
        errors.append("legacy voice/expert parent route leaked into v4.2")

    premortem = read("skills/premortem/SKILL.md")
    for phrase in ["Do not create documents", "Do not create HTML", "novel_findings_count", "deep_dives"]:
        if phrase not in premortem:
            errors.append(f"premortem skill missing no-doc/no-web receipt phrase: {phrase}")

    all_md = "\n".join(path.read_text(encoding="utf-8", errors="replace") for path in ROOT.rglob("*.md"))
    if re.search(r"children:\s*50/50", all_md):
        errors.append("topology-specific 50/50 count leaked into docs")
    for stale in [
        "WIZARD_FULL_v4_2.md",
        "WIZARD_COMPACT_v4_2.md",
        "schemas/RECEIPT_SCHEMA_v4_2.md",
        "schemas/OUTPUT_SCHEMA_v4_2.md",
        "adapters/CODEX_ADAPTER_v4_2.md",
        "topology/ROUTE_GRAPH_v4_2.yaml",
        "taskcards/TASK_CARD_SCHEMA_v4_2.md",
        "docs/EXTERNAL_CHECK_PROTOCOL_v4_2.md",
        "Supporting YAML mirrors",
    ]:
        if stale in all_md:
            errors.append(f"stale/deleted doc reference remains: {stale}")

    for skill in ROOT.glob("skills/**/*.md"):
        if skill.name == "SKILLS_MANIFEST_v4_2.md":
            continue
        lines = skill.read_text(encoding="utf-8").splitlines()
        if len(lines) < 25:
            errors.append(f"skill doc too thin: {rel(skill)} has {len(lines)} lines")
        for phrase in ["Return Fields", "authority_status:"]:
            if phrase not in "\n".join(lines):
                errors.append(f"skill doc missing {phrase}: {rel(skill)}")

    claude_skill = read("skills/claude-bridge/SKILL.md")
    if "skills/claude-bridge/scripts/" in claude_skill:
        for script in ["claude_bridge.py", "claude_child_fanout.py", "fanout_receipt_summary.py"]:
            if not (ROOT / "skills/claude-bridge/scripts" / script).exists():
                errors.append(f"claude bridge skill references missing packet-local script: {script}")


def run_smoke() -> tuple[bool, str]:
    cmd = [
        sys.executable,
        str(REPO_ROOT / "scripts/wizard_child_matrix.py"),
        "--route",
        "decision.context_strategy",
        "--only-children",
        "voice.strategy",
        "--prompt",
        "Wizard v4.2 conformance smoke. Return compact YAML with id, status, distinct_delta, evidence_boundary, conclusion, outcome_delta, killed_or_changed, followup_patch.",
        "--followup-prompt",
        "If smoke fails, name only missing fields.",
        "--payoff",
        "Prove v4.2 route and voice child can run.",
        "--use-when",
        "v4.2 conformance smoke.",
        "--stop-if",
        "Stop if formal child is missing.",
        "--boundary",
        "No repo edits. /tmp receipts only.",
        "--out-dir",
        "/tmp/wizard_v4_2_conformance_smoke",
        "--run-id",
        "wizard-v4-2-conformance-smoke",
        "--sonnet-timeout-sec",
        "160",
        "--opus-timeout-sec",
        "220",
        "--haiku-timeout-sec",
        "100",
        "--sonnet-budget",
        "0.35",
        "--opus-budget",
        "0.55",
        "--haiku-budget",
        "0.2",
        "--global-max-active",
        "3",
        "--max-concurrency",
        "1",
    ]
    proc = subprocess.run(cmd, cwd=str(REPO_ROOT), text=True, capture_output=True, timeout=360)
    if proc.returncode != 0:
        return False, proc.stdout[-2000:] + proc.stderr[-1000:]
    try:
        receipt = json.loads(proc.stdout)
    except Exception:
        return False, "smoke did not return JSON"
    if receipt.get("status") != "accepted":
        return False, f"smoke status={receipt.get('status')}"
    if "voice.strategy" not in receipt.get("formal_children_completed", []):
        return False, "voice.strategy not completed"
    return True, receipt.get("receipt_path", "")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true", help="Run one live v4.2 child-matrix smoke.")
    args = parser.parse_args()

    errors: list[str] = []
    check_static(errors)

    smoke_result = ""
    if args.smoke and not errors:
        ok, smoke_result = run_smoke()
        if not ok:
            errors.append("smoke failed: " + smoke_result)

    if errors:
        print("v4.2 packet conformance: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("v4.2 packet conformance: PASS")
    print(f"runtime_doc=WIZARD_v4_2.md sha256:{digest(ROOT / 'WIZARD_v4_2.md')}")
    print(f"council_parents={len(PARENT_ROUTES)}")
    print(f"management_parents={len(MANAGERS)}")
    if args.smoke:
        print(f"smoke=accepted {smoke_result}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
