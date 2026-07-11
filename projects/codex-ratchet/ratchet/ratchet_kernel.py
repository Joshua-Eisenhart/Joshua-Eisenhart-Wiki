#!/usr/bin/env python3
"""Structural validator for provisional-MSS Ratchet receipts.

This validates process invariants only. It never promotes a scientific claim and
does not test the truth of a candidate's mathematics.
"""

from __future__ import annotations

import argparse
import copy
import json
import math
import sys
from pathlib import Path
from typing import Any


ROOT_PRIMITIVE = "constrained_distinguishability"
SCHEMA_VERSION = "ratchet-run/0.3"
REQUIRED_CONTROL_FAMILIES = {
    "root_smuggling",
    "lower_structure",
    "label_metadata_erasure",
    "anti_by_construction",
    "probe_quotient",
    "order_commutation",
    "history_memory",
    "resolution",
    "carrier_family",
    "topology_locality",
    "entropy_geometry_split",
    "field_vs_token",
    "lineage_freshness",
    "held_out_contact",
    "gradient_freeze",
    "gradient_closure",
    "gradient_injection",
    "gradient_obligation_coupling",
}
PROVISIONAL_STATUS = "PROVISIONAL_MSS"
CLIMB_DECISION = "CLIMB"
HOLD_DECISIONS = {
    "HOLD_NO_GRADIENT",
    "HOLD_UNLICENSED_GRADIENT",
    "HOLD_EXTRINSIC_DRIVE",
    "HOLD_UNCOUPLED_GRADIENT",
}


def _as_dict(value: Any, where: str, errors: list[str]) -> dict[str, Any]:
    if not isinstance(value, dict):
        errors.append(f"{where} must be an object")
        return {}
    return value


def _as_list(value: Any, where: str, errors: list[str]) -> list[Any]:
    if not isinstance(value, list):
        errors.append(f"{where} must be an array")
        return []
    return value


def _nonempty_text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _finite_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def _cycle_exists(nodes: set[str], adjacency: dict[str, set[str]]) -> bool:
    temporary: set[str] = set()
    permanent: set[str] = set()

    def visit(node: str) -> bool:
        if node in permanent:
            return False
        if node in temporary:
            return True
        temporary.add(node)
        for nxt in adjacency.get(node, set()):
            if visit(nxt):
                return True
        temporary.remove(node)
        permanent.add(node)
        return False

    return any(visit(node) for node in nodes if node not in permanent)


def _reaches(start: str, target: str, adjacency: dict[str, set[str]]) -> bool:
    todo = list(adjacency.get(start, set()))
    seen: set[str] = set()
    while todo:
        node = todo.pop()
        if node == target:
            return True
        if node in seen:
            continue
        seen.add(node)
        todo.extend(adjacency.get(node, set()) - seen)
    return False


def validate_receipt(receipt: Any) -> list[str]:
    errors: list[str] = []
    data = _as_dict(receipt, "receipt", errors)
    if not data:
        return errors

    if data.get("schema_version") != SCHEMA_VERSION:
        errors.append(f"schema_version must be {SCHEMA_VERSION!r}")

    receipt_meta = _as_dict(data.get("receipt"), "receipt", errors)
    for field in ("id", "generated_at"):
        if not _nonempty_text(receipt_meta.get(field)):
            errors.append(f"receipt.{field} must be non-empty text")
    if receipt_meta.get("append_only") is not True:
        errors.append("receipt.append_only must be true")
    if receipt_meta.get("self_adjudicating") is not False:
        errors.append("receipt.self_adjudicating must be false")

    lineage = _as_dict(data.get("lineage"), "lineage", errors)
    predecessor_receipts = lineage.get("predecessor_receipts")
    if not isinstance(predecessor_receipts, list) or any(not _nonempty_text(x) for x in predecessor_receipts):
        errors.append("lineage.predecessor_receipts must be an array of non-empty receipt ids")
    elif len(set(predecessor_receipts)) != len(predecessor_receipts):
        errors.append("lineage.predecessor_receipts must be unique")
    for field in ("constraint_hash", "obligation_hash", "code_hash", "data_hash", "test_battery_hash"):
        if not _nonempty_text(lineage.get(field)):
            errors.append(f"lineage.{field} must be non-empty text")
    independent_audit = _as_dict(lineage.get("independent_audit"), "lineage.independent_audit", errors)
    if not isinstance(independent_audit.get("performed"), bool):
        errors.append("lineage.independent_audit.performed must be boolean")
    if not isinstance(independent_audit.get("auditor"), str):
        errors.append("lineage.independent_audit.auditor must be text")
    if independent_audit.get("performed") is True and not _nonempty_text(independent_audit.get("auditor")):
        errors.append("a performed independent audit requires an auditor identity")
    if not _nonempty_text(independent_audit.get("freshness")):
        errors.append("lineage.independent_audit.freshness must be non-empty text")

    claim = _as_dict(data.get("claim"), "claim", errors)
    for field in ("id", "text", "obligation", "claim_ceiling"):
        if not _nonempty_text(claim.get(field)):
            errors.append(f"claim.{field} must be non-empty text")

    root = _as_dict(data.get("root"), "root", errors)
    if root.get("primitive") != ROOT_PRIMITIVE:
        errors.append("root.primitive must be constrained_distinguishability")
    for field in ("presumes_objects", "presumes_equivalence", "relation_total"):
        if root.get(field) is not False:
            errors.append(f"root.{field} must be false")

    scope = _as_dict(data.get("finite_scope"), "finite_scope", errors)
    for field, minimum in (
        ("candidate_limit", 1),
        ("test_limit", 1),
        ("history_limit", 0),
        ("resolution_limit", 1),
    ):
        value = scope.get(field)
        if not isinstance(value, int) or isinstance(value, bool) or value < minimum:
            errors.append(f"finite_scope.{field} must be an integer >= {minimum}")
    if not _nonempty_text(scope.get("budget_label")):
        errors.append("finite_scope.budget_label must be non-empty text")

    candidate_grammar = _as_dict(data.get("candidate_grammar"), "candidate_grammar", errors)
    weakening_grammar = _as_dict(data.get("weakening_grammar"), "weakening_grammar", errors)
    for name, grammar in (("candidate_grammar", candidate_grammar), ("weakening_grammar", weakening_grammar)):
        if grammar.get("globally_complete") is not False:
            errors.append(f"{name}.globally_complete must be false")
        for field in ("id", "hash"):
            if not _nonempty_text(grammar.get(field)):
                errors.append(f"{name}.{field} must be non-empty text")

    families = _as_list(candidate_grammar.get("families"), "candidate_grammar.families", errors)
    operators = _as_list(weakening_grammar.get("operators"), "weakening_grammar.operators", errors)
    family_set = {x for x in families if _nonempty_text(x)}
    operator_set = {x for x in operators if _nonempty_text(x)}
    if not family_set:
        errors.append("candidate_grammar.families must contain at least one family")
    if not operator_set:
        errors.append("weakening_grammar.operators must contain at least one operator")

    candidates = _as_list(data.get("candidates"), "candidates", errors)
    candidate_by_id: dict[str, dict[str, Any]] = {}
    for index, raw in enumerate(candidates):
        candidate = _as_dict(raw, f"candidates[{index}]", errors)
        cid = candidate.get("id")
        if not _nonempty_text(cid):
            errors.append(f"candidates[{index}].id must be non-empty text")
            continue
        if cid in candidate_by_id:
            errors.append(f"duplicate candidate id {cid!r}")
            continue
        candidate_by_id[cid] = candidate
        if candidate.get("family") not in family_set:
            errors.append(f"candidate {cid!r} uses an undeclared family")
        if not isinstance(candidate.get("survived"), bool):
            errors.append(f"candidate {cid!r}.survived must be boolean")
        assumptions = candidate.get("assumptions")
        if not isinstance(assumptions, list) or any(not _nonempty_text(x) for x in assumptions):
            errors.append(f"candidate {cid!r}.assumptions must be an array of non-empty strings")

    if not candidates:
        errors.append("candidates must not be empty")
    if isinstance(scope.get("candidate_limit"), int) and len(candidates) > scope["candidate_limit"]:
        errors.append("candidate population exceeds finite_scope.candidate_limit")

    edges = _as_list(data.get("weakness_edges"), "weakness_edges", errors)
    adjacency: dict[str, set[str]] = {cid: set() for cid in candidate_by_id}
    seen_edges: set[tuple[str, str]] = set()
    for index, raw in enumerate(edges):
        edge = _as_dict(raw, f"weakness_edges[{index}]", errors)
        weaker, stronger = edge.get("weaker"), edge.get("stronger")
        if weaker not in candidate_by_id or stronger not in candidate_by_id:
            errors.append(f"weakness_edges[{index}] references an unknown candidate")
            continue
        if weaker == stronger:
            errors.append(f"weakness_edges[{index}] is reflexive; strict edges must not be")
            continue
        pair = (weaker, stronger)
        if pair in seen_edges:
            errors.append(f"duplicate weakness edge {weaker!r} -> {stronger!r}")
        seen_edges.add(pair)
        adjacency[weaker].add(stronger)
        if edge.get("operator") not in operator_set:
            errors.append(f"weakness_edges[{index}] uses an undeclared weakening operator")
        if not _nonempty_text(edge.get("witness")):
            errors.append(f"weakness_edges[{index}].witness must be non-empty")
        if edge.get("preserves_obligation") is not True:
            errors.append(f"weakness_edges[{index}] must preserve the frozen obligation")

    if _cycle_exists(set(candidate_by_id), adjacency):
        errors.append("strict weakness graph contains a cycle")

    coverage = _as_list(data.get("weakening_coverage"), "weakening_coverage", errors)
    covered_operators: set[str] = set()
    coverage_has_open = False
    for index, raw in enumerate(coverage):
        row = _as_dict(raw, f"weakening_coverage[{index}]", errors)
        candidate = row.get("candidate")
        operator = row.get("operator")
        status_value = row.get("status")
        if candidate not in candidate_by_id:
            errors.append(f"weakening_coverage[{index}] references an unknown candidate")
        if operator not in operator_set:
            errors.append(f"weakening_coverage[{index}] uses an undeclared weakening operator")
        else:
            covered_operators.add(operator)
        if status_value not in {"tested_survivor", "tested_killed", "undefined", "open"}:
            errors.append(f"weakening_coverage[{index}] has an invalid status")
        if status_value == "open":
            coverage_has_open = True
        if not _nonempty_text(row.get("detail")):
            errors.append(f"weakening_coverage[{index}].detail must be non-empty")
    missing_coverage = operator_set - covered_operators
    if missing_coverage:
        errors.append(f"registered weakening operators lack coverage: {sorted(missing_coverage)}")

    declared_survivors = _as_list(data.get("survivors"), "survivors", errors)
    survivor_set = {x for x in declared_survivors if isinstance(x, str)}
    if len(survivor_set) != len(declared_survivors):
        errors.append("survivors must contain unique candidate ids")
    unknown_survivors = survivor_set - set(candidate_by_id)
    if unknown_survivors:
        errors.append(f"survivors reference unknown candidates: {sorted(unknown_survivors)}")
    measured_survivors = {cid for cid, candidate in candidate_by_id.items() if candidate.get("survived") is True}
    if survivor_set != measured_survivors:
        errors.append(
            "survivors must equal candidates whose survived flag is true "
            f"(declared={sorted(survivor_set)}, measured={sorted(measured_survivors)})"
        )

    computed_frontier = {
        candidate
        for candidate in survivor_set
        if not any(
            weaker != candidate and _reaches(weaker, candidate, adjacency)
            for weaker in survivor_set
        )
    }
    declared_frontier_raw = _as_list(data.get("declared_frontier"), "declared_frontier", errors)
    declared_frontier = {x for x in declared_frontier_raw if isinstance(x, str)}
    if len(declared_frontier) != len(declared_frontier_raw):
        errors.append("declared_frontier must contain unique candidate ids")
    if declared_frontier != computed_frontier:
        errors.append(
            "declared_frontier does not equal minimal tested survivors "
            f"(declared={sorted(declared_frontier)}, computed={sorted(computed_frontier)})"
        )

    tests = _as_list(data.get("tests"), "tests", errors)
    controls = _as_list(data.get("controls"), "controls", errors)
    if not tests:
        errors.append("tests must not be empty")
    if isinstance(scope.get("test_limit"), int) and len(tests) + len(controls) > scope["test_limit"]:
        errors.append("tests plus controls exceed finite_scope.test_limit")

    control_by_family: dict[str, dict[str, Any]] = {}
    for index, raw in enumerate(controls):
        control = _as_dict(raw, f"controls[{index}]", errors)
        family = control.get("family")
        if not _nonempty_text(family):
            errors.append(f"controls[{index}].family must be non-empty")
            continue
        if family in control_by_family:
            errors.append(f"duplicate control family {family!r}")
        control_by_family[family] = control
        result = control.get("result")
        if result not in {"pass", "fail", "not_applicable"}:
            errors.append(f"control {family!r} has invalid result")
        if not _nonempty_text(control.get("expected_effect")):
            errors.append(f"control {family!r} must declare expected_effect")
        if not _nonempty_text(control.get("observed_effect")):
            errors.append(f"control {family!r} must declare observed_effect")
        if result == "pass" and control.get("fired") is not True:
            errors.append(f"passing control {family!r} did not fire")
        if result == "not_applicable" and not _nonempty_text(control.get("justification")):
            errors.append(f"not-applicable control {family!r} needs a justification")

    missing_controls = REQUIRED_CONTROL_FAMILIES - set(control_by_family)
    if missing_controls:
        errors.append(f"missing required control families: {sorted(missing_controls)}")

    drive = _as_dict(data.get("drive"), "drive", errors)
    if drive.get("kind") not in {"distinction_gradient", "typed_entropy_gradient"}:
        errors.append("drive.kind must be distinction_gradient or typed_entropy_gradient")
    for field in ("entropy_type", "functional", "orientation", "witness"):
        if not _nonempty_text(drive.get(field)):
            errors.append(f"drive.{field} must be non-empty text")
    for field in ("licensed", "gradient_witnessed", "intrinsic", "obligation_coupled"):
        if not isinstance(drive.get(field), bool):
            errors.append(f"drive.{field} must be boolean")
    for field in ("potential_before", "potential_after", "magnitude", "tolerance"):
        if not _finite_number(drive.get(field)):
            errors.append(f"drive.{field} must be a finite number")
    magnitude = drive.get("magnitude")
    tolerance = drive.get("tolerance")
    before = drive.get("potential_before")
    after = drive.get("potential_after")
    if _finite_number(magnitude) and magnitude < 0:
        errors.append("drive.magnitude must be non-negative")
    if _finite_number(tolerance) and tolerance < 0:
        errors.append("drive.tolerance must be non-negative")
    if all(_finite_number(value) for value in (before, after, magnitude, tolerance)):
        numerical_slack = max(float(tolerance), 1e-12)
        if not math.isclose(float(magnitude), abs(float(before) - float(after)), abs_tol=numerical_slack):
            errors.append("drive.magnitude must equal |potential_before - potential_after| within tolerance")
        expected_witness = float(magnitude) > float(tolerance)
        if drive.get("gradient_witnessed") is not expected_witness:
            errors.append("drive.gradient_witnessed must equal (magnitude > tolerance)")

    response_rows = _as_list(drive.get("candidate_responses"), "drive.candidate_responses", errors)
    if not response_rows:
        errors.append("drive.candidate_responses must not be empty")
    coupled_responses: set[str] = set()
    for index, raw in enumerate(response_rows):
        row = _as_dict(raw, f"drive.candidate_responses[{index}]", errors)
        candidate = row.get("candidate")
        if candidate not in candidate_by_id:
            errors.append(f"drive.candidate_responses[{index}] references an unknown candidate")
        if not _finite_number(row.get("delta")):
            errors.append(f"drive.candidate_responses[{index}].delta must be a finite number")
        if not isinstance(row.get("coupled"), bool):
            errors.append(f"drive.candidate_responses[{index}].coupled must be boolean")
        if row.get("coupled") is True and _finite_number(row.get("delta")):
            if not _finite_number(tolerance) or abs(float(row["delta"])) > float(tolerance):
                coupled_responses.add(candidate)

    open_world = _as_dict(data.get("open_world"), "open_world", errors)
    if open_world.get("global_minimum_claimed") is not False:
        errors.append("open_world.global_minimum_claimed must be false")
    defeated_weaker = open_world.get("defeated_weaker_candidates")
    if not isinstance(defeated_weaker, list) or any(not _nonempty_text(x) for x in defeated_weaker):
        errors.append("open_world.defeated_weaker_candidates must be a string array")
    open_attacks = open_world.get("open_weaker_attacks")
    if not isinstance(open_attacks, list) or not open_attacks or any(not _nonempty_text(x) for x in open_attacks):
        errors.append("open_world.open_weaker_attacks must be a non-empty string array")

    entropy_geometry = _as_dict(data.get("entropy_geometry"), "entropy_geometry", errors)
    for field in ("independent_entropy_state", "independent_geometry_state"):
        if entropy_geometry.get(field) is not False:
            errors.append(f"entropy_geometry.{field} must be false")
    if entropy_geometry.get("applicable") is True and entropy_geometry.get("single_surface") is not True:
        errors.append("applicable entropy/geometry claims must use a single distinction surface")
    if drive.get("kind") == "typed_entropy_gradient":
        if entropy_geometry.get("applicable") is not True:
            errors.append("typed_entropy_gradient requires entropy_geometry.applicable true")
        if drive.get("entropy_type") == "untyped_root_precursor":
            errors.append("typed_entropy_gradient requires an earned named entropy_type")

    transition = _as_dict(data.get("transition"), "transition", errors)
    decision = transition.get("decision")
    if decision not in {CLIMB_DECISION, *HOLD_DECISIONS, "REOPEN"}:
        errors.append("transition.decision is not a recognized Ratchet decision")
    if not _nonempty_text(transition.get("reason")):
        errors.append("transition.reason must be non-empty text")
    selected_raw = _as_list(
        transition.get("selected_frontier_members"),
        "transition.selected_frontier_members",
        errors,
    )
    selected = {x for x in selected_raw if isinstance(x, str)}
    if len(selected) != len(selected_raw):
        errors.append("transition.selected_frontier_members must contain unique candidate ids")
    if selected - declared_frontier:
        errors.append("transition.selected_frontier_members must be a subset of declared_frontier")
    if not isinstance(transition.get("evidence_tooth_recorded"), bool):
        errors.append("transition.evidence_tooth_recorded must be boolean")

    if decision == CLIMB_DECISION:
        for field in ("licensed", "gradient_witnessed", "intrinsic", "obligation_coupled"):
            if drive.get(field) is not True:
                errors.append(f"CLIMB requires drive.{field} true")
        if not coupled_responses:
            errors.append("CLIMB requires a nonzero obligation-coupled candidate response")
        if not selected:
            errors.append("CLIMB requires at least one selected frontier member")
        if transition.get("evidence_tooth_recorded") is not True:
            errors.append("CLIMB requires evidence_tooth_recorded true")
        for family in (
            "gradient_freeze",
            "gradient_closure",
            "gradient_injection",
            "gradient_obligation_coupling",
        ):
            control = control_by_family.get(family, {})
            if control.get("result") != "pass" or control.get("fired") is not True:
                errors.append(f"CLIMB requires passing, fired {family!r} control")
    elif decision in HOLD_DECISIONS:
        if selected:
            errors.append(f"{decision} must not select frontier members")
        if transition.get("evidence_tooth_recorded") is not False:
            errors.append(f"{decision} must not record a Ratchet tooth")
        if decision == "HOLD_NO_GRADIENT" and drive.get("gradient_witnessed") is not False:
            errors.append("HOLD_NO_GRADIENT requires drive.gradient_witnessed false")
        if decision == "HOLD_UNLICENSED_GRADIENT" and drive.get("licensed") is not False:
            errors.append("HOLD_UNLICENSED_GRADIENT requires drive.licensed false")
        if decision == "HOLD_EXTRINSIC_DRIVE" and drive.get("intrinsic") is not False:
            errors.append("HOLD_EXTRINSIC_DRIVE requires drive.intrinsic false")
        if decision == "HOLD_UNCOUPLED_GRADIENT" and drive.get("obligation_coupled") is not False:
            errors.append("HOLD_UNCOUPLED_GRADIENT requires drive.obligation_coupled false")

    status = _as_dict(data.get("status"), "status", errors)
    if status.get("self_promotes") is not False:
        errors.append("status.self_promotes must be false")
    if status.get("claim_ceiling") != claim.get("claim_ceiling"):
        errors.append("status.claim_ceiling must match claim.claim_ceiling")
    if status.get("claim_ceiling") == "ratchet_earned_provisional" and independent_audit.get("performed") is not True:
        errors.append("ratchet_earned_provisional requires a performed independent audit")
    if status.get("lifecycle_status") == PROVISIONAL_STATUS:
        if decision != CLIMB_DECISION:
            errors.append("PROVISIONAL_MSS requires transition.decision CLIMB")
        if not declared_frontier:
            errors.append("PROVISIONAL_MSS requires a non-empty frontier")
        failed_controls = [
            family
            for family, control in control_by_family.items()
            if control.get("result") != "pass"
        ]
        if failed_controls:
            errors.append(f"PROVISIONAL_MSS has controls not passing: {sorted(failed_controls)}")
        if len(family_set) < 2:
            errors.append("PROVISIONAL_MSS requires at least two declared candidate families")
        if coverage_has_open:
            errors.append("PROVISIONAL_MSS cannot leave a registered one-step weakening open")
    if decision in HOLD_DECISIONS:
        if status.get("lifecycle_status") != decision:
            errors.append(f"{decision} requires matching status.lifecycle_status")
        if status.get("claim_ceiling") == "ratchet_earned_provisional":
            errors.append(f"{decision} cannot have ratchet_earned_provisional claim ceiling")

    next_rung = data.get("next_rung")
    if next_rung is not None:
        if decision != CLIMB_DECISION:
            errors.append("next_rung requires transition.decision CLIMB")
        next_obj = _as_dict(next_rung, "next_rung", errors)
        if not _nonempty_text(next_obj.get("demanded_distinction")):
            errors.append("next_rung.demanded_distinction must be non-empty")
        if not _nonempty_text(next_obj.get("predecessor_projection")):
            errors.append("next_rung.predecessor_projection must be non-empty")

    reopen_triggers = data.get("reopen_triggers")
    if not isinstance(reopen_triggers, list) or not reopen_triggers or any(not _nonempty_text(x) for x in reopen_triggers):
        errors.append("reopen_triggers must be a non-empty string array")

    return errors


def validate_ledger(ledger: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(ledger, list) or not ledger:
        return ["ledger must be a non-empty array of Ratchet receipts"]

    by_id: dict[str, dict[str, Any]] = {}
    for index, raw in enumerate(ledger):
        receipt_errors = validate_receipt(raw)
        errors.extend(f"ledger[{index}]: {error}" for error in receipt_errors)
        if not isinstance(raw, dict):
            continue
        receipt_meta = raw.get("receipt")
        rid = receipt_meta.get("id") if isinstance(receipt_meta, dict) else None
        if not _nonempty_text(rid):
            continue
        if rid in by_id:
            errors.append(f"duplicate ledger receipt id {rid!r}")
        else:
            by_id[rid] = raw

    adjacency: dict[str, set[str]] = {rid: set() for rid in by_id}
    for rid, receipt in by_id.items():
        lineage = receipt.get("lineage", {})
        predecessors = lineage.get("predecessor_receipts", []) if isinstance(lineage, dict) else []
        if not isinstance(predecessors, list):
            continue
        for predecessor in predecessors:
            if predecessor not in by_id:
                errors.append(f"receipt {rid!r} references missing predecessor {predecessor!r}")
                continue
            adjacency[predecessor].add(rid)
            predecessor_status = by_id[predecessor].get("status", {})
            child_status = receipt.get("status", {})
            pred_lifecycle = predecessor_status.get("lifecycle_status") if isinstance(predecessor_status, dict) else None
            child_lifecycle = child_status.get("lifecycle_status") if isinstance(child_status, dict) else None
            if pred_lifecycle in {"REOPENED", "DEMOTED"} and child_lifecycle == PROVISIONAL_STATUS:
                errors.append(
                    f"receipt {rid!r} remains PROVISIONAL_MSS while predecessor {predecessor!r} is {pred_lifecycle}"
                )

    if _cycle_exists(set(by_id), adjacency):
        errors.append("receipt dependency graph contains a cycle")
    return errors


def _load(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def run_self_test() -> list[str]:
    fixture_path = Path(__file__).resolve().parent / "examples" / "process_fixture.json"
    hold_fixture_path = Path(__file__).resolve().parent / "examples" / "no_gradient_hold_fixture.json"
    fixture = _load(fixture_path)
    hold_fixture = _load(hold_fixture_path)
    failures: list[str] = []

    if validate_receipt(fixture):
        failures.append("valid fixture was rejected")
    if validate_receipt(hold_fixture):
        failures.append("valid no-gradient HOLD fixture was rejected")

    mutations: list[tuple[str, Any]] = []

    root_smuggle = copy.deepcopy(fixture)
    root_smuggle["root"]["presumes_objects"] = True
    mutations.append(("root object smuggling", root_smuggle))

    global_minimum = copy.deepcopy(fixture)
    global_minimum["open_world"]["global_minimum_claimed"] = True
    mutations.append(("global minimum overclaim", global_minimum))

    wrong_frontier = copy.deepcopy(fixture)
    wrong_frontier["declared_frontier"] = ["equivalence_quotient"]
    mutations.append(("wrong frontier", wrong_frontier))

    split_surface = copy.deepcopy(fixture)
    split_surface["entropy_geometry"]["independent_entropy_state"] = True
    mutations.append(("independent entropy state", split_surface))

    missing_control = copy.deepcopy(fixture)
    missing_control["controls"] = missing_control["controls"][1:]
    mutations.append(("missing hostile control", missing_control))

    cyclic = copy.deepcopy(fixture)
    cyclic["weakness_edges"].append(
        {
            "weaker": "metric_state_space",
            "stronger": "partial_distinction_table",
            "operator": "forget_structure",
            "witness": "Synthetic invalid reverse edge for the self-test.",
            "preserves_obligation": True,
        }
    )
    mutations.append(("cyclic strict weakness", cyclic))

    missing_lineage = copy.deepcopy(fixture)
    missing_lineage.pop("lineage")
    mutations.append(("missing receipt lineage", missing_lineage))

    open_registered_weakening = copy.deepcopy(fixture)
    open_registered_weakening["weakening_coverage"][0]["status"] = "open"
    mutations.append(("open registered weakening at provisional frontier", open_registered_weakening))

    unaudited_admission = copy.deepcopy(fixture)
    unaudited_admission["claim"]["claim_ceiling"] = "ratchet_earned_provisional"
    unaudited_admission["status"]["claim_ceiling"] = "ratchet_earned_provisional"
    mutations.append(("unaudited Ratchet admission", unaudited_admission))

    zero_gradient_climb = copy.deepcopy(fixture)
    zero_gradient_climb["drive"]["potential_after"] = zero_gradient_climb["drive"]["potential_before"]
    zero_gradient_climb["drive"]["magnitude"] = 0.0
    zero_gradient_climb["drive"]["gradient_witnessed"] = False
    mutations.append(("zero-gradient climb", zero_gradient_climb))

    extrinsic_climb = copy.deepcopy(fixture)
    extrinsic_climb["drive"]["intrinsic"] = False
    mutations.append(("extrinsic drive climb", extrinsic_climb))

    uncoupled_climb = copy.deepcopy(fixture)
    uncoupled_climb["drive"]["obligation_coupled"] = False
    for row in uncoupled_climb["drive"]["candidate_responses"]:
        row["coupled"] = False
    mutations.append(("uncoupled gradient climb", uncoupled_climb))

    missing_drive = copy.deepcopy(fixture)
    missing_drive.pop("drive")
    mutations.append(("missing drive record", missing_drive))

    false_magnitude = copy.deepcopy(fixture)
    false_magnitude["drive"]["magnitude"] = 99.0
    mutations.append(("false gradient magnitude", false_magnitude))

    hold_with_tooth = copy.deepcopy(hold_fixture)
    hold_with_tooth["transition"]["evidence_tooth_recorded"] = True
    mutations.append(("no-gradient hold records tooth", hold_with_tooth))

    hold_with_next_rung = copy.deepcopy(hold_fixture)
    hold_with_next_rung["next_rung"] = {
        "demanded_distinction": "Synthetic forbidden next rung.",
        "predecessor_projection": "Synthetic forbidden projection.",
    }
    mutations.append(("no-gradient hold advances rung", hold_with_next_rung))

    for label, mutated in mutations:
        if not validate_receipt(mutated):
            failures.append(f"invalid mutation was accepted: {label}")

    if validate_ledger([fixture]):
        failures.append("valid one-receipt ledger was rejected")

    unknown_predecessor = copy.deepcopy(fixture)
    unknown_predecessor["lineage"]["predecessor_receipts"] = ["missing.receipt"]
    if not validate_ledger([unknown_predecessor]):
        failures.append("ledger with unknown predecessor was accepted")

    cycle_a = copy.deepcopy(fixture)
    cycle_b = copy.deepcopy(fixture)
    cycle_a["receipt"]["id"] = "synthetic.cycle.a"
    cycle_b["receipt"]["id"] = "synthetic.cycle.b"
    cycle_a["claim"]["id"] = "synthetic.cycle.claim.a"
    cycle_b["claim"]["id"] = "synthetic.cycle.claim.b"
    cycle_a["lineage"]["predecessor_receipts"] = ["synthetic.cycle.b"]
    cycle_b["lineage"]["predecessor_receipts"] = ["synthetic.cycle.a"]
    if not validate_ledger([cycle_a, cycle_b]):
        failures.append("cyclic receipt ledger was accepted")

    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--validate", type=Path, help="validate one JSON receipt")
    group.add_argument("--validate-ledger", type=Path, help="validate a JSON array of linked receipts")
    group.add_argument("--self-test", action="store_true", help="run valid and invalid fixture tests")
    args = parser.parse_args()

    if args.self_test:
        failures = run_self_test()
        if failures:
            for failure in failures:
                print(f"FAIL {failure}")
            return 1
        print("PASS ratchet_process_integrity")
        print("valid CLIMB/HOLD fixtures and ledger accepted; anti-drift receipt and dependency mutations rejected")
        return 0

    try:
        target = _load(args.validate or args.validate_ledger)
    except (OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"ok": False, "errors": [str(exc)]}, indent=2))
        return 1

    errors = validate_ledger(target) if args.validate_ledger else validate_receipt(target)
    print(json.dumps({"ok": not errors, "errors": errors}, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
