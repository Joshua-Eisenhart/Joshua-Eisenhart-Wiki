"""
Metamorphic self-tests for the L-proof encodings.

Harness surface encoded: 30_z3_harness_formalization.md (scope-limits section) +
29_harness_edit_protocol.md (L-meta) — audit-response Phase 4 (2026-04-18).

Two independent invariance tests are run per encoding, over the full boolean cube:

  M1 — tactic-variance invariance (z3 vs z3)
        Run the same predicate under two different z3 tactics and require identical
        verdicts on every cube point. If the solver's tactic choice can change the
        verdict, the encoding has a correctness-affecting implementation dependency
        and should be refused.

  M2 — complete-negation dual invariance
        For every cube point P with verdict V, the all-flipped cube point ~P must have
        verdict V' consistent with the predicate's semantic dual where a dual exists.
        Concretely: for the three predicates whose admissibility is a conjunction of
        positively-polarized flags (bounded-work, closeout), the all-false record MUST
        be UNSAT under every role/shape. This is a weak invariant — strong enough to
        catch an accidentally-flipped flag, not strong enough to be a substantive proof.

Both tests run over the same full boolean cube as `cvc5_cross_check.py` so coverage
is symmetric.

Run:
    /Users/joshuaeisenhart/.local/share/codex-ratchet/envs/main/bin/python3 \
        ~/wiki/wizard/harness-consolidated/probes/z3_metamorphic_self_test.py
"""

import itertools
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from z3 import (
    Bool, Int, Solver, Then, And, Or, Not, Implies, sat, unsat, RealVal,
)

import z3_status_ladder_admissibility as SL
import z3_pre_emit_six_axis as PE
import z3_bounded_work_unit as BW
import z3_coupling_gate_ordering as CG
import z3_closeout_completeness as CO


# ----- M1: tactic-variance invariance ---------------------------------------
#
# We run each admissibility check twice, once with the default z3 Solver and once
# with a composed tactic. If the two verdicts ever differ on any cube point, M1
# fails. This is a sanity check, not a correctness proof — two z3 tactics could
# share the same bug — but drift between tactics surfaces encoding issues.


def status_ladder_tactic(claim_value, evidence):
    s = Then("simplify", "propagate-values", "solve-eqs", "smt").solver()
    claim = Int("claim"); s.add(claim == claim_value)
    e_exists = Bool("e_exists"); s.add(e_exists == evidence["exists"])
    e_runs = Bool("e_runs"); s.add(e_runs == evidence["runs"])
    e_passes = Bool("e_passes"); s.add(e_passes == evidence["passes"])
    e_canon = Bool("e_canonical"); s.add(e_canon == evidence["canonical"])
    s.add(SL.admissibility_predicate(claim, e_exists, e_runs, e_passes, e_canon))
    return s.check()


def pre_emit_tactic(record):
    s = Then("simplify", "propagate-values", "smt").solver()
    keys = [
        "has_identity_claim", "asserts_existence", "collapses_set",
        "probe_cited", "constraint_cited", "quotient_named",
        "status_labeled", "divergence_preserved", "banned_construction_absent",
    ]
    flags = {k: Bool(k) for k in keys}
    for k in keys:
        s.add(flags[k] == record[k])
    s.add(PE.pre_emit_predicate(**flags))
    return s.check()


def bounded_work_tactic(record):
    s = Then("simplify", "propagate-values", "smt").solver()
    keys = [
        "scope_declared", "scope_is_singular",
        "action_in_scope", "action_in_out_of_scope",
        "bound_exit_cited", "out_of_scope_enumerated",
    ]
    flags = {k: Bool(k) for k in keys}
    for k in keys:
        s.add(flags[k] == record[k])
    s.add(BW.work_unit_predicate(**flags))
    return s.check()


def gate_tactic(claim_value, evidence):
    s = Then("simplify", "propagate-values", "smt").solver()
    claim = Int("claim"); s.add(claim == claim_value)
    flags = {f"evidence_step{i}": Bool(f"evidence_step{i}") for i in range(1, 7)}
    for i in range(1, 7):
        s.add(flags[f"evidence_step{i}"] == evidence[f"step{i}"])
    s.add(CG.gate_ordering_predicate(
        claim,
        *(flags[f"evidence_step{i}"] for i in range(1, 7)),
    ))
    return s.check()


def closeout_tactic(role, record):
    s = Then("simplify", "propagate-values", "smt").solver()
    required = CO.ROLE_FIELDS[role]
    flags = {f: Bool(f) for f in required}
    forward_plan = Bool("forward_plan_present")
    for f in required:
        s.add(flags[f] == record.get(f, False))
    s.add(forward_plan == record.get("forward_plan_present", False))
    s.add(CO.closeout_predicate(role, flags, forward_plan))
    return s.check()


# ----- cube enumerators ------------------------------------------------------

def all_bool_records(keys):
    for bits in itertools.product([False, True], repeat=len(keys)):
        yield dict(zip(keys, bits))


# ----- M1 drivers ------------------------------------------------------------

def m1_status_ladder():
    disagreements = 0; count = 0
    for claim in (SL.L_EXISTS, SL.L_RUNS, SL.L_PASSES, SL.L_CANONICAL):
        for ev in all_bool_records(["exists", "runs", "passes", "canonical"]):
            count += 1
            a = SL.run_admissibility_check(claim, ev)
            b = status_ladder_tactic(claim, ev)
            if a != b:
                disagreements += 1
    return count, disagreements


def m1_pre_emit():
    disagreements = 0; count = 0
    keys = [
        "has_identity_claim", "asserts_existence", "collapses_set",
        "probe_cited", "constraint_cited", "quotient_named",
        "status_labeled", "divergence_preserved", "banned_construction_absent",
    ]
    for rec in all_bool_records(keys):
        count += 1
        a = PE.check(rec); b = pre_emit_tactic(rec)
        if a != b:
            disagreements += 1
    return count, disagreements


def m1_bounded_work():
    disagreements = 0; count = 0
    keys = [
        "scope_declared", "scope_is_singular",
        "action_in_scope", "action_in_out_of_scope",
        "bound_exit_cited", "out_of_scope_enumerated",
    ]
    for rec in all_bool_records(keys):
        count += 1
        a = BW.check(rec); b = bounded_work_tactic(rec)
        if a != b:
            disagreements += 1
    return count, disagreements


def m1_gate():
    disagreements = 0; count = 0
    step_keys = [f"step{i}" for i in range(1, 7)]
    for claim in range(1, 7):
        for ev in all_bool_records(step_keys):
            count += 1
            a = CG.check(claim, ev); b = gate_tactic(claim, ev)
            if a != b:
                disagreements += 1
    return count, disagreements


def m1_closeout():
    disagreements = 0; count = 0
    for role, fields in CO.ROLE_FIELDS.items():
        keys = fields + ["forward_plan_present"]
        for rec in all_bool_records(keys):
            count += 1
            a = CO.check(role, rec); b = closeout_tactic(role, rec)
            if a != b:
                disagreements += 1
    return count, disagreements


# ----- M2: complete-negation dual invariance --------------------------------
#
# For bounded-work and closeout the admissibility predicate is a positive
# conjunction of flags. Setting every flag to False must be UNSAT by construction.
# For status-ladder and gate-ordering, the predicate is claim-dependent; the
# simpler universal invariant we can state is: at claim=L_CANONICAL / claim=6,
# the all-false evidence cube must UNSAT (already implied by C4 in the fuzzer, but
# restated here as an independent metamorphic check).


def m2_bounded_work_all_false():
    all_false = {k: False for k in [
        "scope_declared", "scope_is_singular",
        "action_in_scope", "action_in_out_of_scope",
        "bound_exit_cited", "out_of_scope_enumerated",
    ]}
    return BW.check(all_false) == unsat


def m2_closeout_all_false_each_role():
    results = []
    for role, fields in CO.ROLE_FIELDS.items():
        all_false = {f: False for f in fields}
        all_false["forward_plan_present"] = False
        results.append((role, CO.check(role, all_false) == unsat))
    return results


def m2_status_ladder_canonical_all_false():
    ev = {"exists": False, "runs": False, "passes": False, "canonical": False}
    return SL.run_admissibility_check(SL.L_CANONICAL, ev) == unsat


def m2_gate_step6_all_false():
    ev = {f"step{i}": False for i in range(1, 7)}
    return CG.check(6, ev) == unsat


# ----- driver ---------------------------------------------------------------

def main():
    m1_results = []
    for name, fn in [
        ("status-ladder", m1_status_ladder),
        ("pre-emit", m1_pre_emit),
        ("bounded-work", m1_bounded_work),
        ("gate", m1_gate),
        ("closeout", m1_closeout),
    ]:
        count, dis = fn()
        m1_results.append((name, count, dis))
        print(f"[{'OK' if dis == 0 else 'FAIL'}] M1 tactic-variance {name:<15} {count} cube pts, {dis} disagreements")

    bw_ok = m2_bounded_work_all_false()
    print(f"[{'OK' if bw_ok else 'FAIL'}] M2 bounded-work all-false → UNSAT required")

    co_results = m2_closeout_all_false_each_role()
    for role, ok in co_results:
        print(f"[{'OK' if ok else 'FAIL'}] M2 closeout[{role}] all-false → UNSAT required")

    sl_ok = m2_status_ladder_canonical_all_false()
    print(f"[{'OK' if sl_ok else 'FAIL'}] M2 status-ladder canonical all-false → UNSAT required")

    g_ok = m2_gate_step6_all_false()
    print(f"[{'OK' if g_ok else 'FAIL'}] M2 gate claim=6 all-false → UNSAT required")

    all_ok = (
        all(d == 0 for _, _, d in m1_results)
        and bw_ok and sl_ok and g_ok
        and all(ok for _, ok in co_results)
    )
    print()
    print("all metamorphic invariants hold" if all_ok else "metamorphic invariant violated")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
