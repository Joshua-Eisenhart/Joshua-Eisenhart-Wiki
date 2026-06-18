#!/usr/bin/env python3
"""Hermes-native controller harness v0.

This is intentionally not a Claude/Codex clone. It imports lessons from those
systems as constraints, then emits Hermes route-truth receipts for bounded work.

Inputs are JSON scenarios. Outputs are JSON receipts. No network, no model call,
no repo mutation beyond the chosen receipt path.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

ALLOWED_ACTION_CLASSES = {
    "controller_local",
    "tool_run",
    "spawn_worker",
    "spawn_subagent",
    "enqueue_runner",
    "blocked",
    "deferred",
    "not_run",
    "superseded",
}

ALLOWED_EXECUTION_STATES = {
    "future_choice",
    "prechecked",
    "completed",
    "partial",
    "blocked",
    "deferred",
    "not_run",
    "superseded",
}

ALLOWED_PROOF_DEPTHS = {
    "controller_local",
    "parent_reported",
    "controller_visible",
    "artifact_verified",
    "test_passed",
}

CODEX_STATUS_LABELS = {
    "exists",
    "runs",
    "passes local rerun",
    "canonical by process",
}

REQUIRED_COUNCILS = ["decision", "failure", "follow_up"]
REQUIRED_ROUTE_FIELDS = [
    "route_id",
    "council",
    "action_class",
    "execution_claim_state",
    "proof_depth",
    "receipt",
    "evidence_boundary",
]

REFERENCE_LESSONS = {
    "codex": [
        "Do not collapse exists/runs/passes/canonical.",
        "Broad claims require claim/evidence/verification rows.",
        "Worker reports are receipts to audit, not truth by themselves.",
    ],
    "claude": [
        "Policy text is insufficient if async/background completions render as raw logs.",
        "Measurement datasets need comparable schemas and claim parity before promotion.",
        "Full scaffold must regenerate after background completions, not just initial turns.",
    ],
    "hermes": [
        "Use Hermes route fields and proof-depth ceilings.",
        "Use profile-scoped memory/skills/wiki surfaces rather than another runtime's files.",
        "Keep Wizard v4.3 scaffold compact and non-log-shaped while preserving route truth.",
    ],
}


@dataclass
class Finding:
    severity: str
    code: str
    message: str


def _now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def load_json(path: Path) -> Dict[str, Any]:
    try:
        return json.loads(path.read_text())
    except Exception as exc:  # pragma: no cover - defensive CLI path
        raise SystemExit(f"failed to load JSON {path}: {exc}") from exc


def sha256_json(obj: Any) -> str:
    payload = json.dumps(obj, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def check_paths(paths: Iterable[str]) -> Tuple[List[str], List[str]]:
    present, missing = [], []
    for raw in paths:
        p = Path(raw).expanduser()
        if p.exists():
            present.append(str(p))
        else:
            missing.append(str(p))
    return present, missing


def validate_route(route: Dict[str, Any]) -> List[Finding]:
    findings: List[Finding] = []
    for field in REQUIRED_ROUTE_FIELDS:
        if field not in route or route.get(field) in (None, ""):
            findings.append(Finding("error", "missing_route_field", f"route missing {field}: {route!r}"))

    action = route.get("action_class")
    if action and action not in ALLOWED_ACTION_CLASSES:
        findings.append(Finding("error", "bad_action_class", f"{route.get('route_id')} action_class={action!r}"))

    state = route.get("execution_claim_state")
    if state and state not in ALLOWED_EXECUTION_STATES:
        findings.append(Finding("error", "bad_execution_state", f"{route.get('route_id')} execution_claim_state={state!r}"))

    proof = route.get("proof_depth")
    if proof and proof not in ALLOWED_PROOF_DEPTHS:
        findings.append(Finding("error", "bad_proof_depth", f"{route.get('route_id')} proof_depth={proof!r}"))

    # Hermes-specific route truth: completed must have at least controller-visible proof.
    if state == "completed" and proof in {"controller_local", "parent_reported"}:
        findings.append(
            Finding(
                "error",
                "completed_without_visible_artifact",
                f"{route.get('route_id')} says completed with insufficient proof_depth={proof!r}",
            )
        )

    # Completed routes need a real local receipt path unless the caller explicitly marks
    # a non-file receipt scheme. v0 accepts file paths only; model prose is not enough.
    receipt = route.get("receipt")
    if state == "completed" and isinstance(receipt, str):
        if not Path(receipt).expanduser().exists():
            findings.append(
                Finding(
                    "error",
                    "completed_receipt_missing",
                    f"{route.get('route_id')} completed receipt path not found: {receipt!r}",
                )
            )

    # Proposed/skipped work must not masquerade as done.
    if action in {"not_run", "deferred", "blocked"} and state == "completed":
        findings.append(
            Finding(
                "error",
                "skipped_route_marked_completed",
                f"{route.get('route_id')} action={action!r} cannot be completed",
            )
        )

    return findings


def validate_claim(claim: Dict[str, Any]) -> List[Finding]:
    findings: List[Finding] = []
    for field in ["claim", "source", "criteria", "status_label"]:
        if not claim.get(field):
            findings.append(Finding("error", "missing_claim_field", f"claim row missing {field}: {claim!r}"))
    label = claim.get("status_label")
    if label and label not in CODEX_STATUS_LABELS:
        findings.append(Finding("error", "bad_status_label", f"claim uses non-Codex status label {label!r}: {claim.get('claim')}"))
    if label in {"runs", "passes local rerun", "canonical by process"} and not claim.get("result_path"):
        findings.append(Finding("error", "runtime_claim_without_result", f"{label!r} requires result_path: {claim.get('claim')}"))
    if label == "canonical by process" and "template" not in " ".join(claim.get("criteria", [])).lower():
        findings.append(Finding("error", "canonical_without_template_criterion", f"canonical claim lacks template criterion: {claim.get('claim')}"))
    return findings


def validate_scenario(scenario: Dict[str, Any]) -> Dict[str, Any]:
    findings: List[Finding] = []

    for field in ["scenario_id", "objective", "routes", "claim_table"]:
        if field not in scenario:
            findings.append(Finding("error", "missing_scenario_field", f"scenario missing {field}"))

    source_paths = scenario.get("source_paths", [])
    present, missing = check_paths(source_paths)
    for p in missing:
        findings.append(Finding("warning", "missing_source_path", p))

    routes = scenario.get("routes", [])
    councils_seen = {r.get("council") for r in routes}
    for council in REQUIRED_COUNCILS:
        if council not in councils_seen:
            findings.append(Finding("error", "missing_council", f"missing council route: {council}"))
    for route in routes:
        findings.extend(validate_route(route))

    for claim in scenario.get("claim_table", []):
        findings.extend(validate_claim(claim))

    has_errors = any(f.severity == "error" for f in findings)
    completed_routes = [r for r in routes if r.get("execution_claim_state") == "completed"]
    blocked_routes = [r for r in routes if r.get("execution_claim_state") == "blocked"]

    if has_errors:
        verdict = "fail"
    elif blocked_routes:
        verdict = "pass_with_blockers"
    else:
        verdict = "pass"

    return {
        "harness": "hermes_controller_harness_v0",
        "created_at": _now(),
        "scenario_id": scenario.get("scenario_id"),
        "scenario_sha256": sha256_json(scenario),
        "verdict": verdict,
        "route_counts": {
            "total": len(routes),
            "completed": len(completed_routes),
            "blocked": len(blocked_routes),
            "deferred": sum(1 for r in routes if r.get("execution_claim_state") == "deferred"),
            "not_run": sum(1 for r in routes if r.get("execution_claim_state") == "not_run"),
        },
        "source_path_check": {"present": present, "missing": missing},
        "reference_lessons_imported_not_cloned": REFERENCE_LESSONS,
        "findings": [f.__dict__ for f in findings],
        "claim_table": scenario.get("claim_table", []),
        "routes": routes,
        "evidence_boundary": scenario.get(
            "evidence_boundary",
            "Harness validates route/claim discipline. It does not execute model workers or prove domain runtime behavior.",
        ),
    }


def selftest() -> Dict[str, Any]:
    good = {
        "scenario_id": "selftest_good",
        "objective": "prove a valid minimal packet can pass",
        "source_paths": [__file__],
        "routes": [
            {
                "route_id": "decision.local",
                "council": "decision",
                "action_class": "controller_local",
                "execution_claim_state": "completed",
                "proof_depth": "artifact_verified",
                "receipt": __file__,
                "evidence_boundary": "file exists and scenario shape validates",
            },
            {
                "route_id": "failure.falsifier",
                "council": "failure",
                "action_class": "controller_local",
                "execution_claim_state": "completed",
                "proof_depth": "artifact_verified",
                "receipt": __file__,
                "evidence_boundary": "local validation only",
            },
            {
                "route_id": "follow_up.menu",
                "council": "follow_up",
                "action_class": "controller_local",
                "execution_claim_state": "completed",
                "proof_depth": "artifact_verified",
                "receipt": __file__,
                "evidence_boundary": "route menu constructed locally",
            },
        ],
        "claim_table": [
            {
                "claim": "harness file exists",
                "source": __file__,
                "result_path": "",
                "criteria": ["path existence checked"],
                "status_label": "exists",
            }
        ],
    }
    bad = {
        "scenario_id": "selftest_bad",
        "objective": "prove overclaims fail",
        "source_paths": [],
        "routes": [
            {
                "route_id": "decision.bad",
                "council": "decision",
                "action_class": "not_run",
                "execution_claim_state": "completed",
                "proof_depth": "parent_reported",
                "receipt": "none",
                "evidence_boundary": "bad by design",
            }
        ],
        "claim_table": [
            {
                "claim": "bad claim",
                "source": "none",
                "result_path": "",
                "criteria": ["none"],
                "status_label": "verified",
            }
        ],
    }
    good_receipt = validate_scenario(good)
    bad_receipt = validate_scenario(bad)
    ok = good_receipt["verdict"] == "pass" and bad_receipt["verdict"] == "fail"
    return {
        "harness": "hermes_controller_harness_v0_selftest",
        "created_at": _now(),
        "ok": ok,
        "good_verdict": good_receipt["verdict"],
        "bad_verdict": bad_receipt["verdict"],
        "bad_error_codes": [f["code"] for f in bad_receipt["findings"] if f["severity"] == "error"],
    }


def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scenario", type=Path, help="JSON scenario to validate/run")
    parser.add_argument("--out", type=Path, help="Receipt path to write")
    parser.add_argument("--selftest", action="store_true", help="Run built-in selftest")
    args = parser.parse_args(argv)

    if args.selftest:
        receipt = selftest()
    elif args.scenario:
        receipt = validate_scenario(load_json(args.scenario))
    else:
        parser.error("provide --selftest or --scenario")

    text = json.dumps(receipt, indent=2, sort_keys=True)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text + "\n")
    print(text)
    return 0 if receipt.get("ok", receipt.get("verdict") in {"pass", "pass_with_blockers"}) else 1


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main(sys.argv[1:]))
