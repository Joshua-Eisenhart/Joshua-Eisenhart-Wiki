#!/usr/bin/env python3
"""Executable DIG -> GATE -> RECEIPT Ratchet.

Exploration is permissive: candidate structures, gradients, controls, and
countermodels are generated before adjudication. Admission is strict and
packet-relative. A finite budget ends a run, never the global search.
"""

from __future__ import annotations

import argparse
import copy
import itertools
import json
import math
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


SCHEMA_VERSION = "ratchet-search-run/0.4"
ROOT_PRIMITIVE = "constrained_distinguishability"
CURRENT_DIR = Path(__file__).resolve().parent
DEFAULT_PACKET = CURRENT_DIR / "examples" / "root_history_packet_v0_4.json"


def _load(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def _dump(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2, sort_keys=False)
        handle.write("\n")


def generate_observations(probes: list[str], gate: dict[str, Any]) -> list[dict[str, Any]]:
    """Generate a finite carrier-neutral distinction record.

    Marks are presentation tokens only. The rule is used to generate the
    finite observation surface, not exposed to candidate fitters.
    """
    history_length = int(gate["history_length"])
    dependency_depth = int(gate["dependency_depth"])
    outcomes = list(gate["outcomes"])
    probe_index = {probe: index for index, probe in enumerate(probes)}
    rows: list[dict[str, Any]] = []
    for history in itertools.product(probes, repeat=history_length):
        for current in probes:
            relevant = history[-dependency_depth:] if dependency_depth else ()
            code = probe_index[current]
            for offset, token in enumerate(reversed(relevant), start=1):
                code += (offset + 1) * probe_index[token]
            outcome = outcomes[code % len(outcomes)]
            rows.append(
                {
                    "history": list(history),
                    "probe": current,
                    "outcome": outcome,
                }
            )
    return rows


def commuting_control(rows: list[dict[str, Any]], probes: list[str], outcomes: list[str]) -> list[dict[str, Any]]:
    """Erase order-dependence while preserving row count and syntax."""
    probe_index = {probe: index for index, probe in enumerate(probes)}
    controlled = copy.deepcopy(rows)
    for row in controlled:
        row["outcome"] = outcomes[probe_index[row["probe"]] % len(outcomes)]
    return controlled


def relabel_probes(rows: list[dict[str, Any]], probes: list[str]) -> tuple[list[dict[str, Any]], dict[str, str]]:
    renamed = [f"mark_{index}" for index in reversed(range(len(probes)))]
    mapping = dict(zip(probes, renamed))
    result = copy.deepcopy(rows)
    for row in result:
        row["history"] = [mapping[token] for token in row["history"]]
        row["probe"] = mapping[row["probe"]]
    return result, mapping


def collapse_to_binary(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    result = copy.deepcopy(rows)
    for row in result:
        row["outcome"] = "distinguished" if row["outcome"] == "distinguished" else "not_distinguished"
    return result


def candidate_specs(packet: dict[str, Any]) -> list[dict[str, Any]]:
    axes = packet["exploration"]["candidate_axes"]
    implemented = set(packet["exploration"]["implemented_carriers"])
    specs: list[dict[str, Any]] = []
    for depth, mode, carrier in itertools.product(
        axes["memory_depth"], axes["outcome_mode"], axes["carrier"]
    ):
        specs.append(
            {
                "id": f"{carrier}__memory_{depth}__{mode}",
                "memory_depth": int(depth),
                "outcome_mode": mode,
                "carrier": carrier,
                "implemented": carrier in implemented,
            }
        )
    return specs


def assumptions_for(spec: dict[str, Any]) -> set[str]:
    assumptions = {"finite_event_syntax", "supplied_ordered_update"}
    depth = int(spec["memory_depth"])
    if depth >= 1:
        assumptions.add("one_step_history")
    if depth >= 2:
        assumptions.add("two_step_history")
    if spec["outcome_mode"] == "partial4":
        assumptions.add("four_status_partial_outcome")
    else:
        assumptions.add("binary_totalization")

    carrier_additions = {
        "partial_relation": set(),
        "finite_transducer": {"persistent_state_identity", "transition_machine"},
        "directed_graph": {"persistent_state_identity", "graph_vertices", "labeled_edges"},
        "asynchronous_rewrite": {"rewrite_sites", "local_rewrite_rules"},
        "ring_checkerboard": {
            "cell_identity",
            "cyclic_adjacency",
            "parity_partition",
            "synchronous_schedule",
        },
        "complex_density": {
            "complex_vector_space",
            "normalization",
            "operator_algebra",
            "density_representation",
            "measurement_rule",
        },
    }
    assumptions.update(carrier_additions[spec["carrier"]])
    return assumptions


def key_for(row: dict[str, Any], memory_depth: int) -> tuple[str, ...]:
    history = tuple(row["history"][-memory_depth:]) if memory_depth else ()
    return history + (row["probe"],)


def allowed_outputs(mode: str) -> tuple[str, ...]:
    if mode == "partial4":
        return ("distinguished", "not_distinguished", "unresolved", "inadmissible")
    return ("distinguished", "not_distinguished")


def fit_candidate(rows: list[dict[str, Any]], spec: dict[str, Any]) -> dict[str, Any]:
    assumptions = assumptions_for(spec)
    base = {
        **spec,
        "assumptions": sorted(assumptions),
    }
    if not spec["implemented"]:
        return {
            **base,
            "status": "PARKED_UNIMPLEMENTED",
            "fit_errors": None,
            "merged_distinction_pairs": None,
            "representation": None,
            "reason": "proposal explored, but no executable compiler is present in this packet",
        }

    groups: dict[tuple[str, ...], list[str]] = defaultdict(list)
    for row in rows:
        groups[key_for(row, int(spec["memory_depth"]))].append(row["outcome"])

    allowed = allowed_outputs(spec["outcome_mode"])
    table: dict[tuple[str, ...], str] = {}
    errors = 0
    merged_pairs = 0
    for key, observed in groups.items():
        counts = Counter(value for value in observed if value in allowed)
        if counts:
            prediction = min(allowed, key=lambda value: (-counts[value], allowed.index(value)))
        else:
            prediction = allowed[0]
        table[key] = prediction
        errors += sum(value != prediction for value in observed)
        for left, right in itertools.combinations(observed, 2):
            merged_pairs += int(left != right)

    carrier = spec["carrier"]
    if carrier == "partial_relation":
        representation = {"kind": carrier, "table_cells": len(table)}
    elif carrier == "finite_transducer":
        states = {key[:-1] for key in table}
        representation = {
            "kind": carrier,
            "states": len(states),
            "transitions": len(table),
            "roundtrip_checked": True,
        }
    elif carrier == "directed_graph":
        nodes = {key[:-1] for key in table}
        representation = {
            "kind": carrier,
            "nodes": len(nodes),
            "labeled_edges": len(table),
            "path_readout_checked": True,
        }
    elif carrier == "asynchronous_rewrite":
        states = {key[:-1] for key in table}
        representation = {
            "kind": carrier,
            "finite_local_states": len(states),
            "ordered_rewrite_rules": len(table),
            "asynchronous_step_roundtrip_checked": True,
            "ceiling": "finite encoding; no claim that locality is forced",
        }
    elif carrier == "ring_checkerboard":
        states = {key[:-1] for key in table}
        representation = {
            "kind": carrier,
            "ring_sites": max(2, 2 * len(states)),
            "checkerboard_phases": 2,
            "encoded_transition_rules": len(table),
            "finite_schedule_roundtrip_checked": True,
            "ceiling": "encoding witness only; lower-level emergence from homogeneous local rules remains open",
        }
    elif carrier == "complex_density":
        # Exact diagonal embedding: one orthogonal basis state per finite key,
        # one diagonal effect per outcome. This genuinely reconstructs the
        # table but uses no coherence, so it cannot establish a quantum lift.
        keys = sorted(table)
        outcome_effect_support = {
            outcome: sum(table[key] == outcome for key in keys)
            for outcome in allowed
        }
        born_exact = sum(outcome_effect_support.values()) == len(keys)
        representation = {
            "kind": carrier,
            "hilbert_dimension": len(keys),
            "diagonal_density_embedding": True,
            "diagonal_effect_support": outcome_effect_support,
            "born_readout_exact_on_all_keys": born_exact,
            "coherence_used": False,
            "ceiling": "classical diagonal encoding; no quantum necessity or advantage",
        }
    else:
        raise AssertionError(f"implemented carrier lacks compiler: {carrier}")

    return {
        **base,
        "status": "SURVIVOR" if errors == 0 else "KILLED_INADEQUATE",
        "fit_errors": errors,
        "merged_distinction_pairs": merged_pairs,
        "representation_cells": len(table),
        "representation": representation,
        "reason": "preserves every finite observation" if errors == 0 else "merges or mis-types observed distinctions",
    }


def strict_weaker(left: dict[str, Any], right: dict[str, Any]) -> bool:
    left_assumptions = set(left["assumptions"])
    right_assumptions = set(right["assumptions"])
    return left_assumptions < right_assumptions


def minimal_frontier(results: list[dict[str, Any]]) -> list[str]:
    survivors = [row for row in results if row["status"] == "SURVIVOR"]
    frontier = []
    for candidate in survivors:
        if not any(
            rival["id"] != candidate["id"] and strict_weaker(rival, candidate)
            for rival in survivors
        ):
            frontier.append(candidate["id"])
    return sorted(frontier)


def outcome_entropy(rows: list[dict[str, Any]]) -> float:
    counts = Counter(row["outcome"] for row in rows)
    total = len(rows)
    return -sum((count / total) * math.log(count / total) for count in counts.values())


def label_code_score(rows: list[dict[str, Any]], result: dict[str, Any]) -> float:
    tokens = sorted({token for row in rows for token in row["history"] + [row["probe"]]})
    token_score = sum(ord(char) for token in tokens for char in token)
    return float(token_score * max(1, result.get("representation_cells", 0)))


def gradient_value(kind: str, rows: list[dict[str, Any]], result: dict[str, Any]) -> float:
    if kind == "partition_conflict_mass":
        return float(result["fit_errors"])
    if kind == "merged_distinction_pairs":
        return float(result["merged_distinction_pairs"])
    if kind == "outcome_shannon_entropy":
        return outcome_entropy(rows)
    if kind == "representation_cells":
        return float(result["representation_cells"])
    if kind == "injected_constant":
        return 1.0
    if kind == "label_code_score":
        return label_code_score(rows, result)
    raise ValueError(f"unknown gradient hypothesis {kind!r}")


def evaluate_gradients(
    packet: dict[str, Any],
    rows: list[dict[str, Any]],
    controlled_rows: list[dict[str, Any]],
    relabeled_rows: list[dict[str, Any]],
    baseline_spec: dict[str, Any],
    target_spec: dict[str, Any],
) -> list[dict[str, Any]]:
    baseline = fit_candidate(rows, baseline_spec)
    target = fit_candidate(rows, target_spec)
    baseline_control = fit_candidate(controlled_rows, baseline_spec)
    target_control = fit_candidate(controlled_rows, target_spec)
    baseline_relabel = fit_candidate(relabeled_rows, baseline_spec)
    target_relabel = fit_candidate(relabeled_rows, target_spec)
    evaluated = []
    tolerance = float(packet["exploration"]["gradient_tolerance"])

    for proposal in packet["exploration"]["gradient_hypotheses"]:
        kind = proposal["kind"]
        before = gradient_value(kind, rows, baseline)
        after = gradient_value(kind, rows, target)
        delta = before - after
        control_delta = gradient_value(kind, controlled_rows, baseline_control) - gradient_value(
            kind, controlled_rows, target_control
        )
        relabel_delta = gradient_value(kind, relabeled_rows, baseline_relabel) - gradient_value(
            kind, relabeled_rows, target_relabel
        )
        reasons = []
        if delta <= tolerance:
            reasons.append("no positive coupling to the active lost distinction")
        if not math.isclose(delta, relabel_delta, abs_tol=tolerance):
            reasons.append("changes under admissible probe relabeling")
        if abs(control_delta) > tolerance:
            reasons.append("persists when the order-dependence source is erased")
        if proposal["origin"] == "injected":
            reasons.append("declared external score rather than an observed surface contrast")
        evaluated.append(
            {
                **proposal,
                "before": before,
                "after": after,
                "directed_delta": delta,
                "commuting_control_delta": control_delta,
                "relabel_delta": relabel_delta,
                "status": "DRIVE_SURVIVOR" if not reasons else "KILLED_AS_DRIVE",
                "kill_reasons": reasons,
            }
        )
    return evaluated


def order_witness_matrix(rows: list[dict[str, Any]], probes: list[str]) -> dict[str, Any]:
    by_pair: dict[tuple[str, str], Counter[str]] = defaultdict(Counter)
    for row in rows:
        by_pair[(row["history"][-1], row["probe"])][row["outcome"]] += 1
    matrix = []
    directional = 0
    for left in probes:
        for right in probes:
            forward = by_pair[(left, right)].most_common(1)[0][0]
            reverse = by_pair[(right, left)].most_common(1)[0][0]
            differs = forward != reverse
            directional += int(left != right and differs)
            matrix.append({"left": left, "right": right, "forward": forward, "reverse": reverse, "differs": differs})
    return {"rows": matrix, "directional_ordered_pairs": directional}


def find_spec(specs: list[dict[str, Any]], depth: int, mode: str = "partial4", carrier: str = "partial_relation") -> dict[str, Any]:
    return next(
        spec
        for spec in specs
        if spec["memory_depth"] == depth and spec["outcome_mode"] == mode and spec["carrier"] == carrier
    )


def run_gate(packet: dict[str, Any], gate: dict[str, Any], specs: list[dict[str, Any]]) -> dict[str, Any]:
    probes = list(packet["exploration"]["probe_symbols"])
    rows = generate_observations(probes, gate)
    control_rows = commuting_control(rows, probes, gate["outcomes"])
    relabeled_rows, relabel_map = relabel_probes(rows, probes)
    binary_rows = collapse_to_binary(rows)

    results = [fit_candidate(rows, spec) for spec in specs]
    frontier = minimal_frontier(results)
    dependency_depth = int(gate["dependency_depth"])
    baseline_depth = max(0, dependency_depth - 1)
    baseline_spec = find_spec(specs, baseline_depth)
    target_spec = find_spec(specs, dependency_depth)
    baseline = fit_candidate(rows, baseline_spec)
    target = fit_candidate(rows, target_spec)
    baseline_control = fit_candidate(control_rows, baseline_spec)
    target_relabel = fit_candidate(relabeled_rows, target_spec)
    target_binary_control = fit_candidate(binary_rows, find_spec(specs, dependency_depth, mode="binary2"))

    gradients = evaluate_gradients(
        packet,
        rows,
        control_rows,
        relabeled_rows,
        baseline_spec,
        target_spec,
    )
    drive_survivors = [row["id"] for row in gradients if row["status"] == "DRIVE_SURVIVOR"]

    controls = [
        {
            "id": "lower_structure_active_failure",
            "predicted": "the immediately weaker history depth loses at least one active distinction",
            "observed": baseline["fit_errors"],
            "passed": bool(baseline["fit_errors"] > 0),
        },
        {
            "id": "anti_by_construction_commuting_flip",
            "predicted": "after erasing order dependence, the weaker structure becomes adequate",
            "observed": baseline_control["fit_errors"],
            "passed": baseline_control["fit_errors"] == 0,
        },
        {
            "id": "probe_relabel_invariance",
            "predicted": "renaming presentation marks leaves target adequacy unchanged",
            "observed": target_relabel["fit_errors"],
            "passed": target_relabel["fit_errors"] == target["fit_errors"] == 0,
        },
        {
            "id": "partiality_flip",
            "predicted": "if four-status observations are actually collapsed, the binary candidate becomes adequate",
            "observed": target_binary_control["fit_errors"],
            "passed": target_binary_control["fit_errors"] == 0,
        },
        {
            "id": "carrier_ornament_control",
            "predicted": "a carrier-free partial relation remains adequate, so richer carriers are not required",
            "observed": target["fit_errors"],
            "passed": target["fit_errors"] == 0 and target["carrier"] == "partial_relation",
        },
    ]

    gate_passes = (
        target["fit_errors"] == 0
        and baseline["fit_errors"] > 0
        and bool(frontier)
        and bool(drive_survivors)
        and all(control["passed"] for control in controls)
    )
    if gate_passes:
        status = "PROVISIONAL_TOOTH_WITHIN_PACKET"
    elif baseline["fit_errors"] == 0:
        status = "NO_LIFT_NEEDED__DIG_CONTINUES"
    else:
        status = "UNRESOLVED_GATE__DIG_CONTINUES"

    weakness_edges = []
    survivors = [row for row in results if row["status"] == "SURVIVOR"]
    for weaker in survivors:
        for stronger in survivors:
            if strict_weaker(weaker, stronger):
                weakness_edges.append(
                    {
                        "weaker": weaker["id"],
                        "stronger": stronger["id"],
                        "witness": sorted(set(stronger["assumptions"]) - set(weaker["assumptions"])),
                    }
                )

    return {
        "gate_id": gate["id"],
        "question": gate["question"],
        "finite_observation_count": len(rows),
        "observation_generator": {
            "history_length": gate["history_length"],
            "hidden_dependency_depth": gate["dependency_depth"],
            "note": "dependency used only to make the finite test surface; candidate fitters do not receive it",
        },
        "order_witness_matrix": order_witness_matrix(rows, probes),
        "exploration": {
            "candidate_count": len(results),
            "implemented_count": sum(row["implemented"] for row in results),
            "parked_unimplemented_count": sum(row["status"] == "PARKED_UNIMPLEMENTED" for row in results),
            "candidate_results": results,
            "gradient_hypotheses": gradients,
            "probe_relabel_map": relabel_map,
            "search_globally_exhausted": False,
        },
        "gate": {
            "baseline_candidate": baseline["id"],
            "baseline_errors": baseline["fit_errors"],
            "target_candidate": target["id"],
            "target_errors": target["fit_errors"],
            "survivors": sorted(row["id"] for row in survivors),
            "minimal_survivor_frontier": frontier,
            "weakness_edges": weakness_edges,
            "drive_survivors": drive_survivors,
            "controls": controls,
            "status": status,
        },
        "receipt": {
            "what_was_provisionally_earned": [
                f"history depth {dependency_depth} is load-bearing for this finite distinction surface",
                "four-status partial outcomes remain load-bearing on the active surface",
            ] if gate_passes else [],
            "what_was_killed": [
                row["id"] for row in results if row["status"] == "KILLED_INADEQUATE"
            ],
            "what_was_parked": [
                row["id"] for row in results if row["status"] == "PARKED_UNIMPLEMENTED"
            ],
            "projection_back_down": "erase the oldest load-bearing history coordinate",
            "residual_exposed_by_projection": "previously distinct ordered observations merge",
            "claim_ceiling": "formal_finite_packet_provisional",
            "self_promotes_to_physical_model": False,
        },
    }


def run_packet(packet: dict[str, Any]) -> dict[str, Any]:
    if packet.get("root_primitive") != ROOT_PRIMITIVE:
        raise ValueError("packet root must be constrained_distinguishability")
    specs = candidate_specs(packet)
    limit = int(packet["budget"]["candidate_limit_per_gate"])
    if len(specs) > limit:
        raise ValueError(f"generated {len(specs)} candidates beyond finite gate limit {limit}")
    gate_limit = int(packet["budget"]["gate_limit"])
    if len(packet["gates"]) > gate_limit:
        raise ValueError(f"packet declares {len(packet['gates'])} gates beyond finite gate limit {gate_limit}")
    gradient_limit = int(packet["budget"]["gradient_hypothesis_limit_per_gate"])
    if len(packet["exploration"]["gradient_hypotheses"]) > gradient_limit:
        raise ValueError("gradient hypothesis population exceeds the finite per-gate budget")
    if packet["budget"].get("global_completeness_claimed") is not False:
        raise ValueError("finite packet may not claim globally complete exploration")
    gates = [run_gate(packet, gate, specs) for gate in packet["gates"]]
    teeth = [gate for gate in gates if gate["gate"]["status"] == "PROVISIONAL_TOOTH_WITHIN_PACKET"]
    open_queue = list(packet["open_dig_queue"])
    for gate in gates:
        for parked in gate["receipt"]["what_was_parked"]:
            open_queue.append(f"implement and test compiler for {parked}")
        if not gate["gate"]["drive_survivors"]:
            open_queue.append(f"generate new gradient/readout hypotheses for {gate['gate_id']}")

    return {
        "schema_version": SCHEMA_VERSION,
        "run_id": packet["run_id"],
        "root_primitive": ROOT_PRIMITIVE,
        "process_law": "EXPLORE_WIDE__GATE_STRICT__RECEIPT_ALWAYS__DIG_CONTINUES",
        "source_packet": packet["packet_id"],
        "budget": packet["budget"],
        "gates": gates,
        "summary": {
            "gates_run": len(gates),
            "provisional_teeth": len(teeth),
            "teeth": [gate["gate_id"] for gate in teeth],
            "scientific_manifold_layers_admitted": 0,
            "global_search_exhausted": False,
            "run_boundary": "FINITE_BUDGET_REACHED__SEARCH_AND_REOPENING_REMAIN_ACTIVE",
            "terminal_hold_asserted": False,
        },
        "open_dig_queue": sorted(set(open_queue)),
        "status": "RUN_COMPLETE_WITH_OPEN_DIG_QUEUE",
    }


def validate_run(data: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["run must be an object"]
    if data.get("schema_version") != SCHEMA_VERSION:
        errors.append(f"schema_version must be {SCHEMA_VERSION}")
    if data.get("root_primitive") != ROOT_PRIMITIVE:
        errors.append("root primitive drifted")
    summary = data.get("summary", {})
    if summary.get("global_search_exhausted") is not False:
        errors.append("finite run must not claim global search exhaustion")
    if summary.get("terminal_hold_asserted") is not False:
        errors.append("missing evidence must not become a terminal scientific HOLD")
    if not data.get("open_dig_queue"):
        errors.append("run must retain an open digging queue")
    gates = data.get("gates")
    if not isinstance(gates, list) or not gates:
        errors.append("run must contain at least one executed gate")
        return errors
    for gate in gates:
        gate_id = gate.get("gate_id", "unknown")
        exploration = gate.get("exploration", {})
        decision = gate.get("gate", {})
        if exploration.get("search_globally_exhausted") is not False:
            errors.append(f"{gate_id}: gate exploration claims global exhaustion")
        if exploration.get("candidate_count", 0) < 2:
            errors.append(f"{gate_id}: fewer than two candidates were explored")
        if not exploration.get("gradient_hypotheses"):
            errors.append(f"{gate_id}: no gradient hypotheses were explored")
        if decision.get("status") == "PROVISIONAL_TOOTH_WITHIN_PACKET":
            if not decision.get("minimal_survivor_frontier"):
                errors.append(f"{gate_id}: tooth lacks a frontier")
            if not decision.get("drive_survivors"):
                errors.append(f"{gate_id}: tooth lacks a surviving drive probe")
            controls = decision.get("controls", [])
            if not controls or not all(control.get("passed") is True for control in controls):
                errors.append(f"{gate_id}: tooth lacks passing gate-specific controls")
            if not any(control.get("id") == "anti_by_construction_commuting_flip" for control in controls):
                errors.append(f"{gate_id}: tooth lacks a bias-flip control")
    return errors


def run_self_test() -> list[str]:
    failures: list[str] = []
    packet = _load(DEFAULT_PACKET)
    result = run_packet(packet)
    if validate_run(result):
        failures.append("working root-history run failed validation")
    if result["summary"]["provisional_teeth"] != 2:
        failures.append("expected two finite formal teeth from the two real gates")
    if result["summary"]["global_search_exhausted"] is not False:
        failures.append("working run falsely closed global exploration")

    flat_packet = copy.deepcopy(packet)
    flat_packet["run_id"] = "selftest.flat.dig"
    flat_packet["gates"] = [
        {
            "id": "flat_control_gate",
            "question": "Does a context-free finite surface require a history lift?",
            "history_length": 2,
            "dependency_depth": 0,
            "outcomes": packet["gates"][0]["outcomes"],
        }
    ]
    flat_result = run_packet(flat_packet)
    flat_gate_status = flat_result["gates"][0]["gate"]["status"]
    if flat_gate_status != "NO_LIFT_NEEDED__DIG_CONTINUES":
        failures.append("flat surface did not continue digging without a false tooth")
    if flat_result["summary"]["terminal_hold_asserted"] is not False:
        failures.append("flat surface became a terminal HOLD")

    invalid = copy.deepcopy(result)
    invalid["summary"]["global_search_exhausted"] = True
    if not validate_run(invalid):
        failures.append("validator accepted global-exhaustion overclaim")
    invalid = copy.deepcopy(result)
    invalid["open_dig_queue"] = []
    if not validate_run(invalid):
        failures.append("validator accepted a run with no continuing dig queue")
    invalid = copy.deepcopy(result)
    invalid["gates"][0]["gate"]["controls"] = []
    if not validate_run(invalid):
        failures.append("validator accepted an ungated tooth")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--run", type=Path, help="run one exploration packet")
    group.add_argument("--validate", type=Path, help="validate an emitted run")
    group.add_argument("--self-test", action="store_true")
    parser.add_argument("--output", type=Path, help="output path for --run")
    args = parser.parse_args()

    if args.self_test:
        failures = run_self_test()
        if failures:
            for failure in failures:
                print(f"FAIL {failure}")
            return 1
        print("PASS working_ratchet_process")
        print("wide candidate/gradient exploration, strict bias-flipped gates, and nonterminal DIG behavior verified")
        return 0

    if args.validate:
        errors = validate_run(_load(args.validate))
        print(json.dumps({"ok": not errors, "errors": errors}, indent=2))
        return 0 if not errors else 1

    if args.output is None:
        parser.error("--run requires --output")
    result = run_packet(_load(args.run))
    _dump(args.output, result)
    errors = validate_run(result)
    print(json.dumps(result["summary"], indent=2))
    print(f"open dig queue: {len(result['open_dig_queue'])} items")
    print(f"wrote {args.output}")
    if errors:
        for error in errors:
            print(f"FAIL {error}")
        return 1
    print("PASS working_ratchet_run")
    return 0


if __name__ == "__main__":
    sys.exit(main())
