"""
Negative fuzzing + contract suite over all 5 L-proof encodings.

Harness surface encoded: 30_z3_harness_formalization.md (Phase 2 deliverable).

Contract guarantees fuzzed per encoding:

  C1 (non-triviality)      — SAT-set and UNSAT-set are both non-empty over the input cube.
  C2 (monotone evidence)   — for status-ladder + gate-ordering: adding evidence never turns
                             SAT into UNSAT (evidence is monotone in admissibility).
  C3 (bad-flag sensitivity)— for each "bad-state" input flag in each encoding, flipping
                             that flag alone must flip at least one admissible record
                             into UNSAT.
  C4 (universal inflation) — status-ladder: any claim L with zero lower-ladder evidence is
                             UNSAT except at L=exists.

All checks run against the production predicates imported from their encoding modules, so
this file is a black-box contract test, not a re-implementation.

Run:
    /Users/joshuaeisenhart/.local/share/codex-ratchet/envs/main/bin/python3 \
        ~/wiki/wizard/harness-consolidated/probes/z3_fuzz_contract.py
"""

import itertools
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from z3 import sat, unsat

import z3_status_ladder_admissibility as SL
import z3_pre_emit_six_axis as PE
import z3_bounded_work_unit as BW
import z3_coupling_gate_ordering as CG
import z3_closeout_completeness as CO


# ----- helpers ---------------------------------------------------------------

def all_bool_records(keys):
    for bits in itertools.product([False, True], repeat=len(keys)):
        yield dict(zip(keys, bits))


def partition(encoding_name, check_fn, inputs, bad_flags=None):
    sat_set, unsat_set = [], []
    for rec in inputs:
        r = check_fn(rec)
        if r == sat:
            sat_set.append(rec)
        elif r == unsat:
            unsat_set.append(rec)
        else:
            raise RuntimeError(f"{encoding_name} unknown result {r} for {rec}")
    return sat_set, unsat_set


# ----- contract checks per encoding -----------------------------------------

def fuzz_status_ladder():
    errors = []
    evidence_keys = ["exists", "runs", "passes", "canonical"]
    all_evidence = list(all_bool_records(evidence_keys))

    sat_claims_by_label = {}
    unsat_claims_by_label = {}
    for label_v in (SL.L_EXISTS, SL.L_RUNS, SL.L_PASSES, SL.L_CANONICAL):
        sat_recs, unsat_recs = [], []
        for ev in all_evidence:
            r = SL.run_admissibility_check(label_v, ev)
            (sat_recs if r == sat else unsat_recs).append(ev)
        sat_claims_by_label[label_v] = sat_recs
        unsat_claims_by_label[label_v] = unsat_recs

    for lbl, recs in sat_claims_by_label.items():
        if not recs:
            errors.append(f"status-ladder C1 fail: no SAT evidence set for label {lbl}")
    for lbl, recs in unsat_claims_by_label.items():
        if not recs and lbl != SL.L_EXISTS:
            errors.append(f"status-ladder C1 fail: no UNSAT evidence set for label {lbl}")

    for lbl in (SL.L_RUNS, SL.L_PASSES, SL.L_CANONICAL):
        no_lower = {"exists": False, "runs": False, "passes": False, "canonical": False}
        if SL.run_admissibility_check(lbl, no_lower) != unsat:
            errors.append(f"status-ladder C4 fail: claim {lbl} with zero evidence not UNSAT")

    for lbl in (SL.L_EXISTS, SL.L_RUNS, SL.L_PASSES, SL.L_CANONICAL):
        for ev in all_evidence:
            if SL.run_admissibility_check(lbl, ev) == sat:
                for k in evidence_keys:
                    if not ev[k]:
                        ev_plus = dict(ev)
                        ev_plus[k] = True
                        if SL.run_admissibility_check(lbl, ev_plus) != sat:
                            errors.append(
                                f"status-ladder C2 fail: adding evidence {k} flipped SAT→UNSAT "
                                f"for lbl={lbl} ev={ev}"
                            )
    return errors


def fuzz_pre_emit():
    errors = []
    keys = [
        "has_identity_claim", "asserts_existence", "collapses_set",
        "probe_cited", "constraint_cited", "quotient_named",
        "status_labeled", "divergence_preserved", "banned_construction_absent",
    ]
    inputs = list(all_bool_records(keys))
    sat_set, unsat_set = partition("pre-emit", PE.check, inputs)
    if not sat_set:
        errors.append("pre-emit C1 fail: SAT set empty")
    if not unsat_set:
        errors.append("pre-emit C1 fail: UNSAT set empty")

    for bad in ("status_labeled", "divergence_preserved", "banned_construction_absent"):
        flips_found = False
        for rec in sat_set:
            rec2 = dict(rec)
            rec2[bad] = False
            if PE.check(rec2) == unsat:
                flips_found = True
                break
        if not flips_found:
            errors.append(f"pre-emit C3 fail: flipping {bad} never produces UNSAT")

    return errors


def fuzz_bounded_work():
    errors = []
    keys = [
        "scope_declared", "scope_is_singular",
        "action_in_scope", "action_in_out_of_scope",
        "bound_exit_cited", "out_of_scope_enumerated",
    ]
    inputs = list(all_bool_records(keys))
    sat_set, unsat_set = partition("bounded-work", BW.check, inputs)
    if not sat_set:
        errors.append("bounded-work C1 fail: SAT set empty")
    if not unsat_set:
        errors.append("bounded-work C1 fail: UNSAT set empty")

    all_good = {k: True for k in keys}
    all_good["action_in_out_of_scope"] = False
    if BW.check(all_good) != sat:
        errors.append("bounded-work C3 fail: canonical good record not SAT")
    for k in keys:
        rec2 = dict(all_good)
        rec2[k] = not rec2[k]
        if BW.check(rec2) != unsat:
            errors.append(f"bounded-work C3 fail: flipping {k} away from good value did not yield UNSAT")

    return errors


def fuzz_coupling_gate():
    errors = []
    step_keys = [f"step{i}" for i in range(1, 7)]

    for claim in range(1, 7):
        sat_recs, unsat_recs = [], []
        for bits in itertools.product([False, True], repeat=6):
            ev = dict(zip(step_keys, bits))
            r = CG.check(claim, ev)
            (sat_recs if r == sat else unsat_recs).append(ev)
        if not sat_recs:
            errors.append(f"gate C1 fail: no SAT evidence set for claim={claim}")
        if not unsat_recs:
            errors.append(f"gate C1 fail: no UNSAT evidence set for claim={claim}")

        for ev in sat_recs:
            for k in step_keys:
                if not ev[k]:
                    ev2 = dict(ev)
                    ev2[k] = True
                    if CG.check(claim, ev2) != sat:
                        errors.append(
                            f"gate C2 fail: adding evidence {k} flipped SAT→UNSAT "
                            f"for claim={claim} ev={ev}"
                        )

    for claim in (2, 3, 4, 5, 6):
        ev = {k: False for k in step_keys}
        ev[f"step{claim}"] = True
        if CG.check(claim, ev) != unsat:
            errors.append(f"gate C3 fail: claim={claim} with only step{claim} evidence not UNSAT")

    return errors


def fuzz_closeout():
    errors = []
    for role in CO.ROLE_FIELDS:
        field_keys = CO.ROLE_FIELDS[role]
        all_true = {k: True for k in field_keys}
        rec_good = dict(all_true)
        rec_good["forward_plan_present"] = False
        if CO.check(role, rec_good) != sat:
            errors.append(f"closeout[{role}] C3 fail: all-required + no-forward-plan not SAT")

        rec_fp = dict(rec_good)
        rec_fp["forward_plan_present"] = True
        if CO.check(role, rec_fp) != unsat:
            errors.append(f"closeout[{role}] C3 fail: forward_plan_present not UNSAT")

        for f in field_keys:
            rec_missing = dict(rec_good)
            rec_missing[f] = False
            if CO.check(role, rec_missing) != unsat:
                errors.append(f"closeout[{role}] C3 fail: missing field {f} not UNSAT")

    return errors


# ----- driver ----------------------------------------------------------------

def main():
    suites = [
        ("status-ladder", fuzz_status_ladder),
        ("pre-emit six-axis", fuzz_pre_emit),
        ("bounded-work", fuzz_bounded_work),
        ("coupling-gate ordering", fuzz_coupling_gate),
        ("closeout completeness", fuzz_closeout),
    ]

    all_errors = []
    for name, fn in suites:
        errs = fn()
        status = "OK" if not errs else "FAIL"
        print(f"[{status}] contract fuzz: {name}  ({len(errs)} violations)")
        for e in errs:
            print(f"        - {e}")
        all_errors.extend(errs)

    print()
    print(f"total contract violations: {len(all_errors)}")
    print("all contracts hold" if not all_errors else "contract violations detected")
    return 0 if not all_errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
