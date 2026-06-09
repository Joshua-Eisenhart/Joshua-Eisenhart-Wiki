#!/usr/bin/env python3
"""Validate Wizard v4.1 loop-contract fixture binding.

This validator writes no files and opens no browser. It is intentionally small:
the goal is to prove that the fixture index is consumed by executable checks
instead of being decorative packet prose.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path


REQUIRED_FAMILIES = ("codex_native", "opus", "sonnet", "haiku", "gemini")
PASSING_FAMILY_STATUSES = {"completed", "accepted", "useful", "accepted_smaller_retry", "accepted_degraded_alt"}
EXTERNAL_RUNTIMES = {
    "codex",
    "codex_native",
    "claude_bridge",
    "claude_code_builtin",
    "opus",
    "sonnet",
    "haiku",
    "gemini",
    "omx_tmux",
}
COMPLETION_SYNONYMS = {
    "done",
    "closed",
    "complete",
    "completed",
    "finished",
    "green",
    "shipped",
    "ratcheted",
    "ready",
    "resolved",
    "clean",
}
BOILERPLATE_DELTA_WORDS = {
    "wording",
    "updated",
    "update",
    "refined",
    "refine",
    "clarify",
    "clarified",
    "clarity",
    "intent",
    "text",
    "prose",
    "renamed",
    "phrasing",
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def quote_hash(path: Path, line_start: int, line_end: int) -> tuple[str, str]:
    lines = path.read_text().splitlines()
    quote = "\n".join(lines[line_start - 1 : line_end])
    return sha256_bytes(quote.encode("utf-8")), quote


def has_structural_divergence(a: dict, b: dict) -> bool:
    axes = (
        "model_family",
        "runtime",
        "prompt_seed_or_digest",
        "receipt_bundle_digest",
        "adversarial_task_card_id",
    )
    for axis in axes:
        av = a.get(axis)
        bv = b.get(axis)
        if av and bv and av != bv:
            if axis == "prompt_seed_or_digest" and not (
                re.fullmatch(r"[0-9a-f]{32,64}", str(av)) and re.fullmatch(r"[0-9a-f]{32,64}", str(bv))
            ):
                continue
            if axis == "receipt_bundle_digest" and not (
                re.fullmatch(r"[0-9a-f]{64}", str(av)) and re.fullmatch(r"[0-9a-f]{64}", str(bv))
            ):
                continue
            return True
    return False


def validate_skill_digest(receipt: dict, root: Path) -> bool:
    ref = receipt.get("skill_body_read_ref", [])
    digest = receipt.get("skill_body_source_digest", "")
    if not re.fullmatch(r"[0-9a-f]{64}", digest):
        return False
    if not ref:
        return False
    path = Path(ref[0])
    if not path.is_absolute():
        path = root / path
    if not path.exists():
        return False
    return sha256_file(path) == digest


def validate_quote_anchor(anchor: dict, root: Path) -> bool:
    path = Path(anchor.get("source_path", ""))
    if not path.is_absolute():
        path = root / path
    if not path.exists():
        return False
    try:
        expected, _ = quote_hash(path, int(anchor["line_start"]), int(anchor["line_end"]))
    except Exception:
        return False
    if expected != anchor.get("quote_sha256"):
        return False
    text = anchor.get("quote_text", "")
    return "This packet-local skill is embedded in Wizard" in text and "open a browser" in text


def ref_exists(root: Path, ref: str) -> bool:
    path_text, _, needle = ref.partition("#")
    path = root / path_text
    if not path.exists():
        return False
    return not needle or needle in path.read_text()


def material_delta(delta: str) -> bool:
    tokens = re.findall(r"[a-z0-9_]+", delta.lower())
    substantive = [token for token in tokens if token not in BOILERPLATE_DELTA_WORDS and len(token) > 2]
    return len(substantive) >= 4


def cross_loop_delta_ok(case: dict, root: Path) -> bool:
    loop_kind = case.get("loop_kind", "edit")
    disposition = case.get("disposition", "")
    old_digest = case.get("old_digest")
    new_digest = case.get("new_digest")
    delta = case.get("delta_summary", "")
    if loop_kind in {"read_only", "audit_only"} and disposition == "unchanged":
        return old_digest == new_digest and ref_exists(root, case.get("artifact_or_clause_ref", ""))
    if disposition in {"extends", "resolved", "supersedes"}:
        return old_digest != new_digest and material_delta(delta)
    return disposition == "unchanged"


def is_substantive_codex_adapter(receipts: list[dict]) -> bool:
    for receipt in receipts:
        if not receipt.get("accepted", True):
            continue
        runtime = str(receipt.get("runtime", "")).lower()
        family = str(receipt.get("family", "")).lower()
        if runtime in EXTERNAL_RUNTIMES or family in EXTERNAL_RUNTIMES:
            return True
    return False


def family_statuses_allow_full(statuses: dict, substantive: bool) -> bool:
    if not substantive:
        return True
    return all(statuses.get(family) in PASSING_FAMILY_STATUSES for family in REQUIRED_FAMILIES)


def prose_status_ok(prose_status_claims: list[str], terminal_status: str, prose_body: str = "") -> bool:
    canonical = f"done_status:{terminal_status}"
    if any(claim != canonical for claim in prose_status_claims):
        return False
    if terminal_status != "done":
        body_tokens = set(re.findall(r"[a-z]+", prose_body.lower()))
        if body_tokens & COMPLETION_SYNONYMS:
            return False
    return True


def done_gate_ok(done_predicate: dict) -> bool:
    return (
        done_predicate.get("terminal_status") == "done"
        and
        done_predicate.get("consecutive_empty_new_finding_loops_observed", 0)
        >= done_predicate.get("consecutive_empty_new_finding_loops_required", 2)
        and done_predicate.get("unresolved_load_bearing_findings_count", 1) == 0
        and done_predicate.get("validator_or_audit_findings_count", 0) == 0
        and done_predicate.get("audit_chain_fixed_point") is True
        and len(done_predicate.get("audit_receipt_ids", [])) >= 2
    )


def cross_loop_coverage_ok(prior_open_ids: list[str], dispositions: list[dict]) -> bool:
    prior = set(prior_open_ids)
    seen: list[str] = []
    for disposition in dispositions:
        finding_id = disposition.get("prior_finding_id")
        if finding_id:
            seen.append(finding_id)
        if not disposition.get("rationale"):
            return False
        if not disposition.get("artifact_or_clause_ref"):
            return False
        if disposition.get("disposition") not in {"supersedes", "kills", "extends", "resolved", "unchanged"}:
            return False
    return set(seen) == prior and len(seen) == len(prior)


def confidence_boundary_ok(audit: dict) -> bool:
    if audit.get("confidence_status") != "sufficient":
        return False
    if audit.get("literal_certainty_claimed") is True:
        return False
    if not audit.get("evidence_standard"):
        return False
    return int(audit.get("unresolved_known_loopholes_count", 1)) == 0


def autoresearch_launch_ok(packet: dict) -> bool:
    if packet.get("mode") == "exec":
        return bool(packet.get("fully_configured"))
    return bool(packet.get("approval_received") and packet.get("run_mode") in {"foreground", "background"})


def management_started_ok(loop_state: dict) -> bool:
    management = loop_state.get("manager", {})
    pressure = management.get("resource_pressure", {})
    statuses = pressure.get("model_family_statuses", {})
    return bool(loop_state.get("management_started_before_voting_parents") and all(family in statuses for family in REQUIRED_FAMILIES))


def premortem_novelty_ok(receipt: dict) -> bool:
    if int(receipt.get("novel_findings_count", 0)) <= 0:
        return False
    if not receipt.get("novel_failure_reasons"):
        return False
    for dive in receipt.get("deep_dives", []):
        required = ("failure_story", "hidden_assumption", "early_warning_signs", "prevention", "novelty")
        if any(not dive.get(field) for field in required):
            return False
    return any(dive.get("novelty") in {"derived_extension", "novel"} for dive in receipt.get("deep_dives", []))


def current_topology_run_id_ok(rows: list[dict]) -> bool:
    required = {
        "decision.voices_council",
        "decision.six_hats_council",
        "decision.experts_council",
        "failure.premortem_council",
        "failure.falsifier_council",
        "failure.loophole_auditor_council",
        "follow_up.prompt_voice_council",
        "follow_up.lane_council",
        "follow_up.compile_gate_council",
    }
    routes = [row.get("route") for row in rows]
    if set(routes) != required or len(routes) != len(required):
        return False
    if any(row.get("status") != "accepted" for row in rows):
        return False
    if any(not isinstance(row.get("run_id"), str) or not row.get("run_id").strip() or row.get("run_id") != row.get("run_id").strip() for row in rows):
        return False
    run_ids = {row.get("run_id") for row in rows}
    if len(run_ids) != 1 or None in run_ids or "" in run_ids:
        return False
    return True


def output_gate_ok(text: str) -> bool:
    if "FULL" in text and "🧙 Wizard v4.1 | FULL | waves:" not in text:
        return False
    if "🧙 Wizard v4.1 | FULL |" in text:
        required = ("parents:9/9", "## ✨ Answer", "## 🏛️ Council Results", "## ✅ Compiled Move", "## 🧭 Follow-Up Options", "## 🧙 Footer")
        return all(item in text for item in required)
    return True


def coverage_matrix_ok(matrix: dict) -> bool:
    routes = {
        "decision.voices_council",
        "decision.six_hats_council",
        "decision.experts_council",
        "failure.premortem_council",
        "failure.falsifier_council",
        "failure.loophole_auditor_council",
        "follow_up.prompt_voice_council",
        "follow_up.lane_council",
        "follow_up.compile_gate_council",
    }
    failure_modes = {"missing_run_id", "mixed_run_id", "wrong_member_count", "obsolete_route", "nonaccepted_row", "unregistered_route"}
    covered = {(item.get("route"), item.get("failure_mode")) for item in matrix.get("cells", [])}
    return all((route, mode) in covered for route in routes for mode in failure_modes)


def assert_packet_identity(root: Path) -> bool:
    manifest = root / "PACKET_MANIFEST_v4_1.md"
    premortem = root / "skills/premortem/SKILL.md"
    return manifest.exists() and premortem.exists() and "packet: v4.1" in manifest.read_text()


def stale_skill_mirror_detected(root: Path) -> bool:
    source = root / "skills/premortem/SKILL.md"
    mirror = root / "conformance/fixtures/stale_mirror/premortem/SKILL.md"
    if not source.exists() or not mirror.exists():
        return False
    return sha256_file(source) != sha256_file(mirror)


def fixture_cases_are_bound(fixtures: list[dict], case_names: set[str]) -> bool:
    return all(fixture.get("validator_case") in case_names for fixture in fixtures)


def dispositions_ref_summary_ok(root: Path) -> bool:
    path = root / "conformance/fixtures/sample_cross_loop_ledger_v4_1.json"
    data = json.loads(path.read_text())
    summary = data["disposition_summary"]
    dispositions = data["dispositions"]
    return summary["dispositions_count"] == len(dispositions) and summary["prior_open_count"] == len({d["prior_finding_id"] for d in dispositions})


CASE_NAMES = {
    "audit_prose_only_divergence",
    "audit_structural_divergence",
    "cross_loop_boilerplate_delta",
    "cross_loop_fresh_delta",
    "missing_model_family_key",
    "prose_yaml_contradiction",
    "bogus_skill_digest",
    "stale_skill_mirror",
    "meta_clause_fixture_mapping",
    "index_without_validator",
    "recomputed_skill_digest",
    "author_asserted_structural_axis",
    "read_only_loop_unchanged_digest",
    "receipt_derived_substantive_classifier",
    "completion_synonym_prose",
    "skill_body_quote_anchor",
    "dispositions_ref_summary",
    "hypothesis_not_load_bearing",
    "cross_loop_missing_prior_id",
    "cross_loop_exact_coverage",
    "confidence_boundary_literal_certainty",
    "confidence_boundary_sufficient",
    "autoresearch_missing_launch_approval",
    "autoresearch_launch_approved",
    "management_late_start",
    "management_started_before_routes",
    "premortem_repeats_user_only",
    "premortem_has_novel_failure",
    "mixed_run_id_rejected",
    "single_run_id_current_topology",
    "missing_run_id_rejected",
    "wrong_member_count_rejected",
    "obsolete_route_rejected",
    "nonaccepted_row_rejected",
    "unregistered_route_rejected",
    "coverage_matrix_complete",
    "coverage_matrix_missing_cell",
    "output_gate_rejects_near_full",
    "output_gate_accepts_canonical_full",
}


def run_case(name: str, root: Path, validator_exists: bool, fixtures: list[dict]) -> bool:
    if name == "audit_prose_only_divergence":
        a = {"model_family": "opus", "runtime": "claude", "prompt_seed_or_digest": "seed-2026050701", "receipt_bundle_digest": "aaa"}
        b = {"model_family": "opus", "runtime": "claude", "prompt_seed_or_digest": "seed-2026050702", "receipt_bundle_digest": "aaa"}
        return has_structural_divergence(a, b)
    if name == "audit_structural_divergence":
        a = {"model_family": "opus", "runtime": "claude", "prompt_seed_or_digest": "seed-a", "receipt_bundle_digest": "aaa"}
        b = {"model_family": "sonnet", "runtime": "claude", "prompt_seed_or_digest": "seed-a", "receipt_bundle_digest": "aaa"}
        return has_structural_divergence(a, b)
    if name == "cross_loop_boilerplate_delta":
        return cross_loop_delta_ok({"loop_kind": "edit", "disposition": "extends", "old_digest": "aaa", "new_digest": "bbb", "delta_summary": "Updated wording for clarity and intent"}, root)
    if name == "cross_loop_fresh_delta":
        return cross_loop_delta_ok({"loop_kind": "edit", "disposition": "extends", "old_digest": "aaa", "new_digest": "bbb", "delta_summary": "validator recomputes digest from cited packet local bytes"}, root)
    if name == "missing_model_family_key":
        return family_statuses_allow_full({"opus": "completed", "sonnet": "completed"}, substantive=True)
    if name == "prose_yaml_contradiction":
        return prose_status_ok(["done_status:continue"], "continue", "The run is green across the board.")
    if name == "bogus_skill_digest":
        return validate_skill_digest({"skill_body_read_ref": ["skills/premortem/SKILL.md"], "skill_body_source_digest": "not-a-digest"}, root)
    if name == "stale_skill_mirror":
        return not stale_skill_mirror_detected(root)
    if name == "meta_clause_fixture_mapping":
        return validator_exists and fixture_cases_are_bound(fixtures, CASE_NAMES)
    if name == "index_without_validator":
        return fixture_cases_are_bound([{"validator_case": "missing_case"}], CASE_NAMES)
    if name == "recomputed_skill_digest":
        path = root / "skills/premortem/SKILL.md"
        return validate_skill_digest({"skill_body_read_ref": [str(path)], "skill_body_source_digest": sha256_file(path)}, root)
    if name == "author_asserted_structural_axis":
        a = {"model_family": "opus", "runtime": "claude", "prompt_seed_or_digest": "seed-a", "receipt_bundle_digest": "aaa", "structural_axis_verified": True}
        b = {"model_family": "opus", "runtime": "claude", "prompt_seed_or_digest": "seed-a", "receipt_bundle_digest": "aaa", "structural_axis_verified": True}
        return has_structural_divergence(a, b)
    if name == "read_only_loop_unchanged_digest":
        return cross_loop_delta_ok({"loop_kind": "read_only", "disposition": "unchanged", "old_digest": "aaa", "new_digest": "aaa", "artifact_or_clause_ref": "schemas/COMPILE_GATE_SCHEMA_v4_1.md#`loop_kind` controls digest freshness"}, root)
    if name == "receipt_derived_substantive_classifier":
        receipts = [{"kind": "parent", "runtime": "claude_bridge", "accepted": True}]
        return is_substantive_codex_adapter(receipts)
    if name == "completion_synonym_prose":
        return prose_status_ok(["done_status:continue"], "continue", "This is green and shipped.")
    if name == "skill_body_quote_anchor":
        path = root / "skills/premortem/SKILL.md"
        digest, quote = quote_hash(path, 17, 22)
        return validate_quote_anchor({"source_path": str(path), "line_start": 17, "line_end": 22, "quote_sha256": digest, "quote_text": quote}, root)
    if name == "dispositions_ref_summary":
        return dispositions_ref_summary_ok(root)
    if name == "hypothesis_not_load_bearing":
        return done_gate_ok({
            "terminal_status": "done",
            "consecutive_empty_new_finding_loops_required": 2,
            "consecutive_empty_new_finding_loops_observed": 2,
            "unresolved_load_bearing_findings_count": 0,
            "premortem_hypotheses_count": 9,
            "validator_or_audit_findings_count": 0,
            "audit_chain_fixed_point": True,
            "audit_receipt_ids": ["audit-1", "audit-2"],
        })
    if name == "cross_loop_missing_prior_id":
        return cross_loop_coverage_ok(
            ["F-1", "F-2"],
            [{"prior_finding_id": "F-1", "disposition": "resolved", "rationale": "fixed by clause", "artifact_or_clause_ref": "05_RUN_PROTOCOL_AND_RETRY.md#Loop mode repeats"}],
        )
    if name == "cross_loop_exact_coverage":
        return cross_loop_coverage_ok(
            ["F-1", "F-2"],
            [
                {"prior_finding_id": "F-1", "disposition": "resolved", "rationale": "fixed by clause", "artifact_or_clause_ref": "05_RUN_PROTOCOL_AND_RETRY.md#Loop mode repeats"},
                {"prior_finding_id": "F-2", "disposition": "unchanged", "rationale": "still load-bearing", "artifact_or_clause_ref": "schemas/COMPILE_GATE_SCHEMA_v4_1.md#For `loop_iteration > 1`"},
            ],
        )
    if name == "confidence_boundary_literal_certainty":
        return confidence_boundary_ok({"confidence_status": "sufficient", "literal_certainty_claimed": True, "evidence_standard": "declared", "unresolved_known_loopholes_count": 0})
    if name == "confidence_boundary_sufficient":
        return confidence_boundary_ok({"confidence_status": "sufficient", "literal_certainty_claimed": False, "evidence_standard": "declared", "unresolved_known_loopholes_count": 0})
    if name == "autoresearch_missing_launch_approval":
        return autoresearch_launch_ok({"mode": "background", "approval_received": False, "run_mode": "background"})
    if name == "autoresearch_launch_approved":
        return autoresearch_launch_ok({"mode": "background", "approval_received": True, "run_mode": "background"})
    if name == "management_late_start":
        return management_started_ok({"management_started_before_voting_parents": False, "manager": {"resource_pressure": {"model_family_statuses": {family: "completed" for family in REQUIRED_FAMILIES}}}})
    if name == "management_started_before_routes":
        return management_started_ok({"management_started_before_voting_parents": True, "manager": {"resource_pressure": {"model_family_statuses": {family: "completed" for family in REQUIRED_FAMILIES}}}})
    if name == "premortem_repeats_user_only":
        return premortem_novelty_ok({
            "novel_findings_count": 0,
            "user_named_issues": [{"id": "U-1", "issue": "members did not run"}],
            "novel_failure_reasons": [],
            "deep_dives": [
                {
                    "failure_story": "The run repeats missing members.",
                    "hidden_assumption": "The known complaint is enough.",
                    "early_warning_signs": "No new issue appears.",
                    "prevention": "Require novelty.",
                    "novelty": "user_named",
                }
            ],
        })
    if name == "premortem_has_novel_failure":
        return premortem_novelty_ok({
            "novel_findings_count": 1,
            "user_named_issues": [{"id": "U-1", "issue": "members did not run"}],
            "novel_failure_reasons": [{"id": "N-1", "reason": "Renderer can mix old and new topology receipts into a false green table."}],
            "deep_dives": [
                {
                    "failure_story": "The run looks green because stale obsolete receipts are accepted beside new receipts.",
                    "hidden_assumption": "Latest-by-route is enough without topology generation separation.",
                    "early_warning_signs": "Obsolete route rows appear in member status output.",
                    "prevention": "Fail on obsolete route rows and require a clean current topology root.",
                    "novelty": "novel",
                }
            ],
        })
    if name == "mixed_run_id_rejected":
        return current_topology_run_id_ok([
            {"route": "decision.voices_council", "status": "accepted", "run_id": "A"},
            {"route": "decision.six_hats_council", "status": "accepted", "run_id": "A"},
            {"route": "decision.experts_council", "status": "accepted", "run_id": "A"},
            {"route": "failure.premortem_council", "status": "accepted", "run_id": "B"},
            {"route": "failure.falsifier_council", "status": "accepted", "run_id": "A"},
            {"route": "failure.loophole_auditor_council", "status": "accepted", "run_id": "A"},
            {"route": "follow_up.prompt_voice_council", "status": "accepted", "run_id": "A"},
            {"route": "follow_up.lane_council", "status": "accepted", "run_id": "A"},
            {"route": "follow_up.compile_gate_council", "status": "accepted", "run_id": "A"},
        ])
    if name == "single_run_id_current_topology":
        return current_topology_run_id_ok([
            {"route": "decision.voices_council", "status": "accepted", "run_id": "R"},
            {"route": "decision.six_hats_council", "status": "accepted", "run_id": "R"},
            {"route": "decision.experts_council", "status": "accepted", "run_id": "R"},
            {"route": "failure.premortem_council", "status": "accepted", "run_id": "R"},
            {"route": "failure.falsifier_council", "status": "accepted", "run_id": "R"},
            {"route": "failure.loophole_auditor_council", "status": "accepted", "run_id": "R"},
            {"route": "follow_up.prompt_voice_council", "status": "accepted", "run_id": "R"},
            {"route": "follow_up.lane_council", "status": "accepted", "run_id": "R"},
            {"route": "follow_up.compile_gate_council", "status": "accepted", "run_id": "R"},
        ])
    if name == "missing_run_id_rejected":
        return current_topology_run_id_ok([
            {"route": route, "status": "accepted", "run_id": "" if i == 0 else "R"}
            for i, route in enumerate(sorted({
                "decision.voices_council", "decision.six_hats_council", "decision.experts_council",
                "failure.premortem_council", "failure.falsifier_council", "failure.loophole_auditor_council",
                "follow_up.prompt_voice_council", "follow_up.lane_council", "follow_up.compile_gate_council",
            }))
        ])
    if name == "wrong_member_count_rejected":
        return current_topology_run_id_ok([
            {"route": "decision.voices_council", "status": "accepted", "run_id": "R"},
            {"route": "decision.six_hats_council", "status": "accepted", "run_id": "R"},
        ])
    if name == "obsolete_route_rejected":
        rows = [
            {"route": "decision.voices_council", "status": "accepted", "run_id": "R"},
            {"route": "decision.six_hats_council", "status": "accepted", "run_id": "R"},
            {"route": "decision.experts_council", "status": "accepted", "run_id": "R"},
            {"route": "failure.premortem_council", "status": "accepted", "run_id": "R"},
            {"route": "failure.falsifier_council", "status": "accepted", "run_id": "R"},
            {"route": "failure.six_hats_risk_council", "status": "accepted", "run_id": "R"},
            {"route": "follow_up.prompt_voice_council", "status": "accepted", "run_id": "R"},
            {"route": "follow_up.lane_council", "status": "accepted", "run_id": "R"},
            {"route": "follow_up.compile_gate_council", "status": "accepted", "run_id": "R"},
        ]
        return current_topology_run_id_ok(rows)
    if name == "nonaccepted_row_rejected":
        rows = [
            {"route": "decision.voices_council", "status": "partial", "run_id": "R"},
            {"route": "decision.six_hats_council", "status": "accepted", "run_id": "R"},
            {"route": "decision.experts_council", "status": "accepted", "run_id": "R"},
            {"route": "failure.premortem_council", "status": "accepted", "run_id": "R"},
            {"route": "failure.falsifier_council", "status": "accepted", "run_id": "R"},
            {"route": "failure.loophole_auditor_council", "status": "accepted", "run_id": "R"},
            {"route": "follow_up.prompt_voice_council", "status": "accepted", "run_id": "R"},
            {"route": "follow_up.lane_council", "status": "accepted", "run_id": "R"},
            {"route": "follow_up.compile_gate_council", "status": "accepted", "run_id": "R"},
        ]
        return current_topology_run_id_ok(rows)
    if name == "unregistered_route_rejected":
        return "failure.six_hats_risk_council" in {
            "decision.voices_council",
            "decision.six_hats_council",
            "decision.experts_council",
            "failure.premortem_council",
            "failure.falsifier_council",
            "failure.loophole_auditor_council",
            "follow_up.prompt_voice_council",
            "follow_up.lane_council",
            "follow_up.compile_gate_council",
        }
    if name == "coverage_matrix_complete":
        routes = [
            "decision.voices_council",
            "decision.six_hats_council",
            "decision.experts_council",
            "failure.premortem_council",
            "failure.falsifier_council",
            "failure.loophole_auditor_council",
            "follow_up.prompt_voice_council",
            "follow_up.lane_council",
            "follow_up.compile_gate_council",
        ]
        modes = ["missing_run_id", "mixed_run_id", "wrong_member_count", "obsolete_route", "nonaccepted_row", "unregistered_route"]
        return coverage_matrix_ok({"cells": [{"route": route, "failure_mode": mode} for route in routes for mode in modes]})
    if name == "coverage_matrix_missing_cell":
        return coverage_matrix_ok({"cells": [{"route": "decision.voices_council", "failure_mode": "missing_run_id"}]})
    if name == "output_gate_rejects_near_full":
        return output_gate_ok("Wizard v4.1 FULL enough; parents 9/9; children done.")
    if name == "output_gate_accepts_canonical_full":
        return output_gate_ok(
            "🧙 Wizard v4.1 | FULL | waves:3/3 | parents:9/9 | children:49/49 | score:90 | runtimes:codex\n"
            "## ✨ Answer\nx\n## 🏛️ Council Results\nx\n## ✅ Compiled Move\nx\n## 🧭 Follow-Up Options\nx\n## 🧙 Footer\n🧙 Time/value:\n"
        )
    raise KeyError(name)


def clause_ref_exists(root: Path, clause_ref: str) -> bool:
    path_text, _, needle = clause_ref.partition("#")
    path = root / path_text
    if not path.exists():
        return False
    if not needle:
        return True
    return path.read_text().count(needle) == 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--packet-root", default=str(Path(__file__).resolve().parents[1]))
    args = parser.parse_args()
    root = Path(args.packet_root).resolve()
    if not assert_packet_identity(root):
        print("loop_contract_fixtures: fail")
        print(f"- invalid packet root: {root}")
        return 1
    index_path = root / "conformance/fixtures/loop_contract_fixtures_v4_1.json"
    data = json.loads(index_path.read_text())
    fixtures = data.get("fixtures", [])
    validator_path = root / data.get("validator", "")
    validator_exists = validator_path.exists()

    ids = [fixture["id"] for fixture in fixtures]
    errors: list[str] = []
    if len(ids) != len(set(ids)):
        errors.append("duplicate fixture id")
    if not validator_exists:
        errors.append(f"validator missing: {validator_path}")

    for fixture in fixtures:
        if not fixture.get("covers"):
            errors.append(f"{fixture['id']}: missing covers")
        if not fixture.get("clause_refs"):
            errors.append(f"{fixture['id']}: missing clause_refs")
        for clause_ref in fixture.get("clause_refs", []):
            if not clause_ref_exists(root, clause_ref):
                errors.append(f"{fixture['id']}: stale clause_ref {clause_ref}")

    for fixture in fixtures:
        case_name = fixture["validator_case"]
        observed_pass = run_case(case_name, root, validator_exists, fixtures)
        expected_pass = fixture["expected"] == "pass"
        if observed_pass != expected_pass:
            errors.append(f"{fixture['id']}: expected {fixture['expected']} observed {'pass' if observed_pass else 'fail'}")

    if errors:
        print("loop_contract_fixtures: fail")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"loop_contract_fixtures: pass ({len(fixtures)} fixtures)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
