#!/usr/bin/env python3
"""Strict-but-open L5 manifold gate over the bundle's actual L5/L7/L8 evidence.

This asks whether nested-shell geometry is the MSS needed to preserve the L5
stratum/flux distinctions, while providing an oriented-path counter-surface on
which a stronger connection really does become load-bearing.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import sys
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parent.parent
L5_PATH = ROOT / "sims_and_scripts" / "manifold_L5_nested_shells_schmidt_strata_sim_results.json"
L7_PATH = ROOT / "sims_and_scripts" / "manifold_L7_shell_connection_holonomy_sim_results.json"
L8_PATH = ROOT / "sims_and_scripts" / "manifold_L8_global_bundle_chern_quantization_sim_results.json"
DEFAULT_OUTPUT = Path(__file__).resolve().parent / "runs" / "manifold_L5_reaudit_v0_4.json"


def load(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def binary_entropy(probability: float) -> float:
    p = min(1.0, max(0.0, probability))
    if p in {0.0, 1.0}:
        return 0.0
    return -p * math.log2(p) - (1.0 - p) * math.log2(1.0 - p)


def entropy_to_radius(entropy_bits: float) -> float:
    """Invert h2((1+r)/2) on r in [0,1] by finite bisection."""
    lo, hi = 0.0, 1.0
    for _ in range(100):
        mid = (lo + hi) / 2.0
        value = binary_entropy((1.0 + mid) / 2.0)
        if value > entropy_bits:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def truth(angle: float) -> dict[str, float]:
    radius = abs(math.cos(2.0 * angle))
    negativity = 0.5 * abs(math.sin(2.0 * angle))
    purity = 0.5 * (1.0 + radius * radius)
    entropy = binary_entropy((1.0 + radius) / 2.0)
    return {
        "angle": angle,
        "radius": radius,
        "negativity": negativity,
        "purity": purity,
        "entropy_bits": entropy,
    }


def rmse(values: list[float]) -> float:
    return math.sqrt(sum(value * value for value in values) / len(values)) if values else 0.0


def candidate_definitions(train: list[dict[str, float]]) -> list[dict[str, Any]]:
    entangled_mean = sum(row["radius"] for row in train if row["negativity"] > 1e-12) / sum(
        row["negativity"] > 1e-12 for row in train
    )

    def nearest_lookup(row: dict[str, float]) -> float:
        nearest = min(train, key=lambda item: abs(item["angle"] - row["angle"]))
        return nearest["radius"]

    return [
        {
            "id": "binary_product_entangled",
            "assumptions": ["binary_product_flag"],
            "predict": lambda row: 1.0 if row["negativity"] <= 1e-12 else entangled_mean,
            "structure": "one binary class plus a fitted representative",
        },
        {
            "id": "finite_nearest_lookup",
            "assumptions": ["finite_training_table", "nearest_angle_rule"],
            "predict": nearest_lookup,
            "structure": "finite table without a stratum law",
        },
        {
            "id": "schmidt_radius_scalar",
            "assumptions": ["one_real_stratum_coordinate", "pure_two_qubit_branch"],
            "predict": lambda row: abs(math.cos(2.0 * row["angle"])),
            "structure": "one scalar coordinate",
        },
        {
            "id": "negativity_scalar",
            "assumptions": ["one_real_stratum_coordinate", "pure_two_qubit_branch", "negativity_readout"],
            "predict": lambda row: math.sqrt(max(0.0, 1.0 - 4.0 * row["negativity"] ** 2)),
            "structure": "one scalar, exactly invertible to radius on this branch",
        },
        {
            "id": "purity_scalar",
            "assumptions": ["one_real_stratum_coordinate", "pure_two_qubit_branch", "purity_readout"],
            "predict": lambda row: math.sqrt(max(0.0, 2.0 * row["purity"] - 1.0)),
            "structure": "one scalar, exactly invertible to radius on this branch",
        },
        {
            "id": "entropy_scalar",
            "assumptions": [
                "one_real_stratum_coordinate",
                "pure_two_qubit_branch",
                "binary_entropy_readout",
                "finite_numeric_inversion",
            ],
            "predict": lambda row: entropy_to_radius(row["entropy_bits"]),
            "structure": "one scalar entropy coordinate, invertible on this branch",
        },
        {
            "id": "full_schmidt_spectrum",
            "assumptions": [
                "one_real_stratum_coordinate",
                "pure_two_qubit_branch",
                "two_component_spectrum",
                "normalization_constraint",
            ],
            "predict": lambda row: abs(math.cos(2.0 * row["angle"])),
            "structure": "normalized two-component spectrum",
        },
        {
            "id": "nested_shell_geometry",
            "assumptions": [
                "one_real_stratum_coordinate",
                "pure_two_qubit_branch",
                "nested_shell_topology",
                "geometric_embedding",
                "cross_shell_flux_readout",
            ],
            "predict": lambda row: abs(math.cos(2.0 * row["angle"])),
            "structure": "the claimed L5 nested-shell presentation",
        },
    ]


def evaluate_candidate(
    candidate: dict[str, Any],
    heldout: list[dict[str, float]],
    berry_normalization: float,
) -> dict[str, Any]:
    predictor: Callable[[dict[str, float]], float] = candidate["predict"]
    predicted = [predictor(row) for row in heldout]
    radius_errors = [prediction - row["radius"] for prediction, row in zip(predicted, heldout)]
    flux_errors = []
    for left, right in itertools.combinations(range(len(heldout)), 2):
        predicted_flux = berry_normalization * (predicted[left] - predicted[right])
        true_flux = berry_normalization * (heldout[left]["radius"] - heldout[right]["radius"])
        flux_errors.append(predicted_flux - true_flux)
    radius_rmse = rmse(radius_errors)
    flux_rmse = rmse(flux_errors)
    passed = radius_rmse < 1e-9 and flux_rmse < 1e-9
    return {
        "id": candidate["id"],
        "assumptions": candidate["assumptions"],
        "structure": candidate["structure"],
        "heldout_radius_rmse": radius_rmse,
        "heldout_cross_shell_flux_rmse": flux_rmse,
        "status": "SURVIVOR" if passed else "KILLED_HELDOUT_FAILURE",
    }


def build_run() -> dict[str, Any]:
    l5, l7, l8 = load(L5_PATH), load(L7_PATH), load(L8_PATH)
    source_sweep = l5["dual_ratchet_sweep"]
    train = [truth(float(row["a"])) for row in source_sweep[::2]]
    source_angles = [float(row["a"]) for row in source_sweep]
    heldout_angles = [(left + right) / 2.0 for left, right in zip(source_angles[:-1], source_angles[1:])]
    heldout = [truth(angle) for angle in heldout_angles]

    # The audited L7 normalization is -pi * (r_i-r_j). The earlier L5
    # bookkeeping used 2pi; both are functions of the same one-dimensional
    # scalar and therefore cannot by themselves force shell geometry.
    berry_normalization = -math.pi
    candidates = candidate_definitions(train)
    evaluated = [evaluate_candidate(candidate, heldout, berry_normalization) for candidate in candidates]
    survivors = [row for row in evaluated if row["status"] == "SURVIVOR"]

    scalar_members = [
        row["id"]
        for row in survivors
        if row["id"] in {"schmidt_radius_scalar", "negativity_scalar", "purity_scalar", "entropy_scalar"}
    ]
    scalar_exact_translation = all(
        max(
            abs(truth(angle)["radius"] - entropy_to_radius(truth(angle)["entropy_bits"])),
            abs(truth(angle)["radius"] - math.sqrt(max(0.0, 1.0 - 4.0 * truth(angle)["negativity"] ** 2))),
            abs(truth(angle)["radius"] - math.sqrt(max(0.0, 2.0 * truth(angle)["purity"] - 1.0))),
        ) < 1e-9
        for angle in heldout_angles
    )

    baseline = next(row for row in evaluated if row["id"] == "binary_product_entangled")
    scalar = next(row for row in evaluated if row["id"] == "schmidt_radius_scalar")
    gradient_hypotheses = [
        {
            "id": "heldout_radius_residual",
            "before": baseline["heldout_radius_rmse"],
            "after": scalar["heldout_radius_rmse"],
            "status": "DRIVE_SURVIVOR",
        },
        {
            "id": "heldout_flux_residual",
            "before": baseline["heldout_cross_shell_flux_rmse"],
            "after": scalar["heldout_cross_shell_flux_rmse"],
            "status": "DRIVE_SURVIVOR",
        },
        {
            "id": "raw_stratum_outcome_entropy",
            "before": binary_entropy(0.5),
            "after": binary_entropy(0.5),
            "status": "KILLED_AS_DRIVE",
            "reason": "unchanged across the repair",
        },
        {
            "id": "representation_size",
            "before": 1,
            "after": 1,
            "status": "KILLED_AS_DRIVE",
            "reason": "does not measure the lost held-out distinction",
        },
    ]

    # Bias-flip/counter-surface from actual L8 orientation evidence: same
    # scalar shell coordinate, opposite oriented winding. Scalar strata merge
    # it; an oriented connection/bundle readout separates it.
    plus = float(l8["fact2_chern_sign_is_chirality"]["chern_plus_orientation"])
    minus = float(l8["fact2_chern_sign_is_chirality"]["chern_reversed_orientation"])
    orientation_counter = {
        "same_shell_scalar": True,
        "scalar_stratum_distinguishes": False,
        "oriented_connection_distinguishes": plus * minus < 0,
        "plus_orientation": plus,
        "minus_orientation": minus,
        "gate_flips_for_path_orientation_obligation": plus * minus < 0,
    }

    controls = [
        {
            "id": "heldout_midpoint_prediction",
            "passed": scalar["heldout_radius_rmse"] < 1e-9 and baseline["heldout_radius_rmse"] > 1e-3,
        },
        {
            "id": "erase_nesting",
            "passed": l5["erase_nesting_control"]["pass"] is True
            and abs(float(l5["erase_nesting_control"]["erased_flux"])) < 1e-12,
        },
        {
            "id": "audited_berry_normalization",
            "passed": l7["fact1_flux_is_berry_holonomy"]["flux_matches_ledger"] is True,
        },
        {
            "id": "anti_by_construction_orientation_flip",
            "passed": orientation_counter["gate_flips_for_path_orientation_obligation"],
        },
        {
            "id": "scalar_translation_crosscheck",
            "passed": scalar_exact_translation,
        },
    ]

    gate_pass = bool(scalar_members) and scalar_exact_translation and all(control["passed"] for control in controls)
    return {
        "schema_version": "ratchet-manifold-gate/0.4",
        "run_id": "manifold-L5-reaudit-v0.4",
        "root_process": "constrained_distinguishability",
        "source_evidence": {
            "L5": str(L5_PATH.relative_to(ROOT)),
            "L7": str(L7_PATH.relative_to(ROOT)),
            "L8": str(L8_PATH.relative_to(ROOT)),
            "all_source_rows_scratch_diagnostic": True,
        },
        "question": "Does the actual L5 evidence force nested-shell geometry, or does a weaker stratum presentation carry it?",
        "exploration": {
            "candidate_count": len(evaluated),
            "candidate_results": evaluated,
            "heldout_angles": heldout_angles,
            "gradient_hypotheses": gradient_hypotheses,
            "global_search_exhausted": False,
        },
        "gate": {
            "tested_survivors": [row["id"] for row in survivors],
            "provisional_mss_frontier": {
                "id": "one_dimensional_scalar_stratum_equivalence_class",
                "members": scalar_members,
                "mutually_translatable_on_tested_branch": scalar_exact_translation,
            },
            "nested_shell_geometry_status": "SURVIVES_BUT_NONMINIMAL",
            "controls": controls,
            "orientation_counter_surface": orientation_counter,
            "status": "L5_GEOMETRY_DEMOTED__SCALAR_STRATUM_PROVISIONAL",
        },
        "receipt": {
            "provisionally_earned": "one-dimensional scalar stratum equivalence class on the installed pure two-qubit branch",
            "killed": [row["id"] for row in evaluated if row["status"].startswith("KILLED")],
            "demoted": ["nested_shell_geometry as L5 MSS"],
            "preserved": [
                "L5 numerical sweep",
                "L7 Berry holonomy mathematics",
                "L8 Chern orientation mathematics",
            ],
            "downstream_admission_effect": "L6-L8 scientific admission reopens; their local mathematics is not erased",
            "claim_ceiling": "installed_QIT_branch_formal_provisional",
            "scientific_manifold_layer_admitted": False,
        },
        "open_dig_queue": [
            "find an empirical or lower-level distinction requiring a continuous stratum rather than finite lookup",
            "test multi-parameter mixed-state families where scalar stratum readouts cease to be mutually invertible",
            "run the oriented-path counter-surface as the next connection/holonomy gate",
            "compare BKM, QFI, classical Fisher, Euclidean, and finite graph metrics without presuming BKM uniqueness",
            "challenge assumption inclusion with compiler-based weakness maps",
        ],
        "status": "RUN_COMPLETE_WITH_OPEN_DIG_QUEUE" if gate_pass else "UNRESOLVED_GATE__DIG_CONTINUES",
    }


def validate(run: Any) -> list[str]:
    errors = []
    if not isinstance(run, dict) or run.get("schema_version") != "ratchet-manifold-gate/0.4":
        return ["invalid manifold-gate schema"]
    if run.get("status") not in {"RUN_COMPLETE_WITH_OPEN_DIG_QUEUE", "UNRESOLVED_GATE__DIG_CONTINUES"}:
        errors.append("invalid nonterminal status")
    if not run.get("open_dig_queue"):
        errors.append("manifold gate lacks continuing dig queue")
    if run.get("exploration", {}).get("global_search_exhausted") is not False:
        errors.append("finite manifold gate claims global exhaustion")
    gate = run.get("gate", {})
    if gate.get("status") == "L5_GEOMETRY_DEMOTED__SCALAR_STRATUM_PROVISIONAL":
        if not all(control.get("passed") is True for control in gate.get("controls", [])):
            errors.append("L5 adjudication lacks passing controls")
        if not gate.get("orientation_counter_surface", {}).get("gate_flips_for_path_orientation_obligation"):
            errors.append("L5 gate lacks a stronger-structure flip surface")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--validate", type=Path)
    args = parser.parse_args()
    if args.validate:
        errors = validate(load(args.validate))
        print(json.dumps({"ok": not errors, "errors": errors}, indent=2))
        return 0 if not errors else 1
    run = build_run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as handle:
        json.dump(run, handle, indent=2)
        handle.write("\n")
    errors = validate(run)
    print(json.dumps({
        "status": run["gate"]["status"],
        "frontier": run["gate"]["provisional_mss_frontier"],
        "nested_shell_geometry": run["gate"]["nested_shell_geometry_status"],
        "open_dig_queue": len(run["open_dig_queue"]),
    }, indent=2))
    print(f"wrote {args.output}")
    if errors:
        for error in errors:
            print(f"FAIL {error}")
        return 1
    print("PASS manifold_L5_working_ratchet_gate")
    return 0


if __name__ == "__main__":
    sys.exit(main())
