"""
cvc5 cross-check of all 5 L-proof encodings — full boolean-cube replay.

Harness surface encoded: 30_z3_harness_formalization.md (Phase 3 deliverable) +
07_z3_unsat_primacy.md (dual-solver practice: every UNSAT claim deserves two
independent solver witnesses).

For each encoding, an independent cvc5 implementation of the predicate is run on
**every point of the input boolean cube** (not a curated sample). If z3 and cvc5
disagree on any cube point, the contract fails.

Cube sizes per encoding:
    status-ladder : 4 claims × 2^4 evidence = 64 cases
    pre-emit      : 2^9 = 512 cases
    bounded-work  : 2^6 = 64 cases
    gate-ordering : 6 claims × 2^6 evidence = 384 cases
    closeout      : Σ_role 2^(|fields_role|+1) = 2^10 + 2^8 + 2^8 + 2^8 = 1792 cases

Total ~= 2816 cube points. Full agreement on the cube is a strictly stronger
contract than agreement on hand-authored test lists.

Run:
    /Users/joshuaeisenhart/.local/share/codex-ratchet/envs/main/bin/python3 \
        ~/wiki/wizard/harness-consolidated/probes/cvc5_cross_check.py
"""

import itertools
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import cvc5
from cvc5 import Kind
from z3 import sat as z3_sat, unsat as z3_unsat

import z3_status_ladder_admissibility as SL
import z3_pre_emit_six_axis as PE
import z3_bounded_work_unit as BW
import z3_coupling_gate_ordering as CG
import z3_closeout_completeness as CO


def new_solver():
    s = cvc5.Solver()
    s.setLogic("QF_LIA")
    return s


def cvc5_verdict(s, formula):
    s.assertFormula(formula)
    r = s.checkSat()
    if r.isSat():
        return z3_sat
    if r.isUnsat():
        return z3_unsat
    raise RuntimeError(f"cvc5 unknown result: {r}")


def cvc5_bool(s, name, value):
    v = s.mkConst(s.getBooleanSort(), name)
    s.assertFormula(s.mkTerm(Kind.EQUAL, v, s.mkBoolean(value)))
    return v


def cvc5_int(s, name, value):
    v = s.mkConst(s.getIntegerSort(), name)
    s.assertFormula(s.mkTerm(Kind.EQUAL, v, s.mkInteger(value)))
    return v


def AND(s, *args):
    return args[0] if len(args) == 1 else s.mkTerm(Kind.AND, *args)


def OR(s, *args):
    return s.mkTerm(Kind.OR, *args)


def NOT(s, x):
    return s.mkTerm(Kind.NOT, x)


def IMPLIES(s, a, b):
    return s.mkTerm(Kind.IMPLIES, a, b)


def EQ(s, a, b):
    return s.mkTerm(Kind.EQUAL, a, b)


# ----- cvc5 re-encodings (identical math, independent solver) ----------------

def cvc5_status_ladder(claim_value, evidence):
    s = new_solver()
    claim = cvc5_int(s, "claim", claim_value)
    e_exists = cvc5_bool(s, "e_exists", evidence["exists"])
    e_runs = cvc5_bool(s, "e_runs", evidence["runs"])
    e_passes = cvc5_bool(s, "e_passes", evidence["passes"])
    e_canon = cvc5_bool(s, "e_canonical", evidence["canonical"])
    i0 = s.mkInteger(SL.L_EXISTS); i1 = s.mkInteger(SL.L_RUNS)
    i2 = s.mkInteger(SL.L_PASSES); i3 = s.mkInteger(SL.L_CANONICAL)
    pred = OR(s,
        AND(s, EQ(s, claim, i0), e_exists),
        AND(s, EQ(s, claim, i1), e_runs, e_exists),
        AND(s, EQ(s, claim, i2), e_passes, e_runs, e_exists),
        AND(s, EQ(s, claim, i3), e_canon, e_passes, e_runs, e_exists),
    )
    return cvc5_verdict(s, pred)


def cvc5_pre_emit(record):
    s = new_solver()
    keys = [
        "has_identity_claim", "asserts_existence", "collapses_set",
        "probe_cited", "constraint_cited", "quotient_named",
        "status_labeled", "divergence_preserved", "banned_construction_absent",
    ]
    f = {k: cvc5_bool(s, k, record[k]) for k in keys}
    axis1 = IMPLIES(s, f["has_identity_claim"], f["probe_cited"])
    axis2 = IMPLIES(s, f["asserts_existence"], f["constraint_cited"])
    axis3 = IMPLIES(s, f["collapses_set"], f["quotient_named"])
    pred = AND(s, axis1, axis2, axis3,
               f["status_labeled"], f["divergence_preserved"], f["banned_construction_absent"])
    return cvc5_verdict(s, pred)


def cvc5_bounded_work(record):
    s = new_solver()
    keys = [
        "scope_declared", "scope_is_singular",
        "action_in_scope", "action_in_out_of_scope",
        "bound_exit_cited", "out_of_scope_enumerated",
    ]
    f = {k: cvc5_bool(s, k, record[k]) for k in keys}
    pred = AND(s,
        f["scope_declared"], f["scope_is_singular"],
        f["action_in_scope"], NOT(s, f["action_in_out_of_scope"]),
        f["bound_exit_cited"], f["out_of_scope_enumerated"],
    )
    return cvc5_verdict(s, pred)


def cvc5_gate(claim_value, evidence):
    s = new_solver()
    claim = cvc5_int(s, "claim", claim_value)
    ev = {i: cvc5_bool(s, f"step{i}", evidence[f"step{i}"]) for i in range(1, 7)}
    branches = []
    for target in range(1, 7):
        conds = [EQ(s, claim, s.mkInteger(target))]
        conds.extend(ev[i] for i in range(1, target + 1))
        branches.append(AND(s, *conds))
    pred = OR(s, *branches)
    return cvc5_verdict(s, pred)


def cvc5_closeout(role, record):
    s = new_solver()
    required = CO.ROLE_FIELDS[role]
    f = {k: cvc5_bool(s, k, record.get(k, False)) for k in required}
    fp = cvc5_bool(s, "forward_plan_present", record.get("forward_plan_present", False))
    pred = AND(s, *f.values(), NOT(s, fp))
    return cvc5_verdict(s, pred)


# ----- full-cube replay drivers ---------------------------------------------

def all_bool_records(keys):
    for bits in itertools.product([False, True], repeat=len(keys)):
        yield dict(zip(keys, bits))


def cube_status_ladder():
    disagreements = []
    count = 0
    for claim in (SL.L_EXISTS, SL.L_RUNS, SL.L_PASSES, SL.L_CANONICAL):
        for ev in all_bool_records(["exists", "runs", "passes", "canonical"]):
            count += 1
            z = SL.run_admissibility_check(claim, ev)
            c = cvc5_status_ladder(claim, ev)
            if z != c:
                disagreements.append(("status-ladder", claim, ev, z, c))
    return count, disagreements


def cube_pre_emit():
    disagreements = []
    count = 0
    keys = [
        "has_identity_claim", "asserts_existence", "collapses_set",
        "probe_cited", "constraint_cited", "quotient_named",
        "status_labeled", "divergence_preserved", "banned_construction_absent",
    ]
    for rec in all_bool_records(keys):
        count += 1
        z = PE.check(rec)
        c = cvc5_pre_emit(rec)
        if z != c:
            disagreements.append(("pre-emit", None, rec, z, c))
    return count, disagreements


def cube_bounded_work():
    disagreements = []
    count = 0
    keys = [
        "scope_declared", "scope_is_singular",
        "action_in_scope", "action_in_out_of_scope",
        "bound_exit_cited", "out_of_scope_enumerated",
    ]
    for rec in all_bool_records(keys):
        count += 1
        z = BW.check(rec)
        c = cvc5_bounded_work(rec)
        if z != c:
            disagreements.append(("bounded-work", None, rec, z, c))
    return count, disagreements


def cube_gate():
    disagreements = []
    count = 0
    step_keys = [f"step{i}" for i in range(1, 7)]
    for claim in range(1, 7):
        for ev in all_bool_records(step_keys):
            count += 1
            z = CG.check(claim, ev)
            c = cvc5_gate(claim, ev)
            if z != c:
                disagreements.append(("gate", claim, ev, z, c))
    return count, disagreements


def cube_closeout():
    disagreements = []
    count = 0
    for role, fields in CO.ROLE_FIELDS.items():
        keys = fields + ["forward_plan_present"]
        for rec in all_bool_records(keys):
            count += 1
            z = CO.check(role, rec)
            c = cvc5_closeout(role, rec)
            if z != c:
                disagreements.append(("closeout", role, rec, z, c))
    return count, disagreements


# ----- driver ---------------------------------------------------------------

def main():
    suites = [
        ("status-ladder", cube_status_ladder),
        ("pre-emit", cube_pre_emit),
        ("bounded-work", cube_bounded_work),
        ("gate-ordering", cube_gate),
        ("closeout", cube_closeout),
    ]
    all_ok = True
    total_cases = 0
    total_disagreements = 0
    for name, fn in suites:
        count, dis = fn()
        total_cases += count
        total_disagreements += len(dis)
        status = "OK" if not dis else "FAIL"
        print(f"[{status}] cube cross-check: {name:<15}  {count} cube points, {len(dis)} disagreements")
        for enc, claim, rec, z, c in dis[:3]:
            print(f"        - claim={claim} rec={rec}: z3={z} cvc5={c}")
        if dis:
            all_ok = False

    print()
    print(f"total cube points: {total_cases}, disagreements: {total_disagreements}")
    print("z3/cvc5 agree on every cube point" if all_ok else "solver disagreement detected")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
