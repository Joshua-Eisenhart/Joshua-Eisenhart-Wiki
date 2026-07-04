#!/usr/bin/env python3
"""cand_canonical_v2 -- G2/SU(3) octonion-derivation reduction, BLIND + SHARP.

Structurally derived from SIM_TEMPLATE.py. Math reused (honestly) from the source
scout system_v5/ops/formal_scouts/foundation_foundation_r5_g2_su3_reduction_jax.py:
  - Cayley-Dickson octonion structure constants (exact integer table)
  - derivation constraint matrix  D(e_a e_b) = D(e_a) e_b + e_a D(e_b)
  - Der(O) = g2 has dim 14; stabiliser of one imaginary unit e1 is su(3), dim 8.

Harness framing (nominalist constraint-admissibility):
  This is a probe, not a proof of ontology. It tests which derivation operators
  survive under constraint set C (derivation identity + unit-fixing) and probe
  family M (the explicit row probes). Survivors remain candidates. Exclusion
  (z3/cvc5 UNSAT) is the primary signal.

  Status ladder: exists < runs < passes local rerun < canonical by process.

TWO FIXES over the source scout (both load-bearing, both auditable in code):

  FIX 1 -- BLIND DERIVATION.
    The source passed expected_dim=8 into the SMT and the harness compared the
    RREF free-coordinate count to the literal 8. Here NO target dimension is fed
    to the solver or the verdict. The dimension is *decided by the solvers*:
      (a) k_lower = largest k for which z3+cvc5 find k linearly independent
          kernel vectors  -> a sequence of SAT checks, no literal target.
      (b) k_upper = smallest k+1 for which z3+cvc5 prove NO k+1 linearly
          independent kernel vectors exist -> UNSAT.
    The reported stabiliser dimension is k where SAT(k) and UNSAT(k+1) both hold.
    RREF is used ONLY to mint candidate independent vectors (a witness source);
    the dimension number that the sim reports comes off the SMT SAT/UNSAT ladder,
    cross-checked against RREF rank. See blind_dimension_via_smt().

  FIX 2 -- SHARP VALUE-COUPLED NEGATIVE CONTROL.
    A second, independently-known subalgebra: fixing TWO independent imaginary
    units (e1,e2) collapses the stabiliser to su(2)+center, dim 3 (computed here
    by the SAME blind SMT ladder, not asserted). The control predicts the
    SPECIFIC integer 3. We then run a value-coupled SMT:
      - assert the two-unit fixing rows AND "exists kernel vector outside the
        3-dim span"  -> UNSAT  (the dim is exactly 3, sharp).
      - DROP one of the two unit-fixing constraints (revert to single-unit
        fixing) and re-run the same "outside 3-dim span" query -> SAT
        (an su(3) vector outside the 3-dim su(2)+center span now exists).
    Dropping the control constraint FLIPS the verdict unsat<->sat, and the
    flip is tied to the independently computed integer 3. See sharp_value_control().
"""

from __future__ import annotations

# Module-level classification (read by lint_sim_contract._module_level_assignments).
# Honest ceiling: this is pre-admission tool-lego fit evidence only. Promotion to
# canonical is OWNER-GATED and conditional on the blind+sharp properties holding at
# runtime; see build_result() promotion_allowed and the result-summary claim ceiling.
classification = "tool_lego_fit_probe"

from fractions import Fraction
import hashlib
import json
import os
from typing import Any

import numpy as np  # baseline numeric layer only (control cross-check); not load-bearing

# =====================================================================
# TOOL MANIFEST -- which tools were tried; non-empty reason for each
# =====================================================================

TOOL_MANIFEST = {
    "z3": {
        "tried": False,
        "used": False,
        "reason": "",
    },
    "cvc5": {
        "tried": False,
        "used": False,
        "reason": "",
    },
    "sympy": {
        "tried": False,
        "used": False,
        "reason": "",
    },
    "numpy": {
        "tried": True,
        "used": True,
        "reason": "baseline float rank cross-check on the constraint matrix; NOT load-bearing (exact answer comes from Fraction RREF and SMT)",
    },
    "python_stdlib": {
        "tried": True,
        "used": True,
        "reason": "supportive exact rational (fractions) RREF, hashing, JSON receipt serialization",
    },
}

TOOL_INTEGRATION_DEPTH = {
    "z3": None,
    "cvc5": None,
    "sympy": None,
    "numpy": "supportive",
    "python_stdlib": "supportive",
}

try:
    import z3
    TOOL_MANIFEST["z3"]["tried"] = True
except ImportError:
    TOOL_MANIFEST["z3"]["reason"] = "not installed"

try:
    import cvc5
    from cvc5 import Kind
    TOOL_MANIFEST["cvc5"]["tried"] = True
except ImportError:
    TOOL_MANIFEST["cvc5"]["reason"] = "not installed"

try:
    import sympy as sp  # noqa: F401
    TOOL_MANIFEST["sympy"]["tried"] = True
    TOOL_MANIFEST["sympy"]["used"] = True
    TOOL_MANIFEST["sympy"]["reason"] = "supportive Matrix.nullspace cross-check on the constraint matrix dimension"
    TOOL_INTEGRATION_DEPTH["sympy"] = "supportive"
except ImportError:
    TOOL_MANIFEST["sympy"]["reason"] = "not installed"
    sp = None


# =====================================================================
# OCTONION ALGEBRA -- exact integer Cayley-Dickson structure constants
# (genuine math reused from the source scout, reimplemented in pure Python
#  exact integers so the math core needs no float runtime).
# =====================================================================

def cd_conj(x: list[int]) -> list[int]:
    return [x[0]] + [-v for v in x[1:]]


def multiply(table: list[list[list[int]]], x: list[int], y: list[int]) -> list[int]:
    dim = len(x)
    out = [0] * dim
    for c in range(dim):
        s = 0
        tc = table[c]
        for a in range(dim):
            xa = x[a]
            if xa == 0:
                continue
            tca = tc[a]
            for b in range(dim):
                yb = y[b]
                if yb and tca[b]:
                    s += tca[b] * xa * yb
        out[c] = s
    return out


def cd_pair_multiply(parent: list[list[list[int]]], x: list[int], y: list[int]) -> list[int]:
    n = len(parent)
    a, b = x[:n], x[n:]
    c, d = y[:n], y[n:]
    first = [u - v for u, v in zip(multiply(parent, a, c), multiply(parent, cd_conj(d), b))]
    second = [u + v for u, v in zip(multiply(parent, d, a), multiply(parent, b, cd_conj(c)))]
    return first + second


def cd_double(parent: list[list[list[int]]]) -> list[list[list[int]]]:
    n = len(parent)
    dim = 2 * n
    table = [[[0] * dim for _ in range(dim)] for _ in range(dim)]
    eye = [[1 if i == j else 0 for j in range(dim)] for i in range(dim)]
    for i in range(dim):
        for j in range(dim):
            prod = cd_pair_multiply(parent, eye[i], eye[j])
            for c in range(dim):
                table[c][i][j] = prod[c]
    return table


def build_octonion_table() -> list[list[list[int]]]:
    real = [[[1]]]
    complex_t = cd_double(real)
    quaternion = cd_double(complex_t)
    octonion = cd_double(quaternion)
    return octonion


def derivation_constraint_rows(table: list[list[list[int]]]) -> list[list[int]]:
    """Rows of the linear system for a derivation D (flattened d[row,col])."""
    dim = len(table)

    def varidx(row: int, col: int) -> int:
        return row + col * dim

    rows: list[list[int]] = []
    for a in range(dim):
        for b in range(dim):
            for c in range(dim):
                row = [0] * (dim * dim)
                for k in range(dim):
                    row[varidx(c, k)] += table[k][a][b]
                    row[varidx(k, a)] += -table[c][k][b]
                    row[varidx(k, b)] += -table[c][a][k]
                rows.append(row)
    return rows


def fixing_constraint_rows(dim: int, vectors: list[list[int]]) -> list[list[int]]:
    rows: list[list[int]] = []
    for vec in vectors:
        for out_idx in range(dim):
            row = [0] * (dim * dim)
            for col, coeff in enumerate(vec):
                if coeff:
                    row[out_idx + col * dim] += int(coeff)
            rows.append(row)
    return rows


# =====================================================================
# EXACT RATIONAL RREF + NULLSPACE  (witness source only)
# =====================================================================

def rref_fraction(rows_in: list[list[int]], ncols: int) -> tuple[list[int], list[list[Fraction]]]:
    rows = [[Fraction(x) for x in row] for row in rows_in if any(row)]
    pivot_cols: list[int] = []
    r = 0
    for c in range(ncols):
        pivot = None
        for i in range(r, len(rows)):
            if rows[i][c] != 0:
                pivot = i
                break
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        pv = rows[r][c]
        rows[r] = [x / pv for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c] != 0:
                factor = rows[i][c]
                rows[i] = [rows[i][j] - factor * rows[r][j] for j in range(ncols)]
        pivot_cols.append(c)
        r += 1
        if r == len(rows):
            break
    return pivot_cols, rows[: len(pivot_cols)]


def nullspace_basis(pivot_cols: list[int], rref_rows: list[list[Fraction]], ncols: int) -> list[list[Fraction]]:
    pivot_set = set(pivot_cols)
    free_cols = [idx for idx in range(ncols) if idx not in pivot_set]
    basis: list[list[Fraction]] = []
    for free in free_cols:
        vec = [Fraction(0) for _ in range(ncols)]
        vec[free] = Fraction(1)
        for row_idx, pivot_col in enumerate(pivot_cols):
            vec[pivot_col] = -rref_rows[row_idx][free]
        basis.append(vec)
    return basis


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def vectors_sha(vectors: list[list[Fraction]]) -> str:
    payload = "|".join(",".join(fraction_text(x) for x in row) for row in vectors)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def matrix_rank_fraction(rows: list[list[Fraction]], ncols: int) -> int:
    """Exact rational rank of a row set (number of pivots in RREF)."""
    M = [row[:] for row in rows]
    nr = len(M)
    rank = 0
    for c in range(ncols):
        pivot = None
        for i in range(rank, nr):
            if M[i][c] != 0:
                pivot = i
                break
        if pivot is None:
            continue
        M[rank], M[pivot] = M[pivot], M[rank]
        pv = M[rank][c]
        M[rank] = [x / pv for x in M[rank]]
        for i in range(nr):
            if i != rank and M[i][c] != 0:
                f = M[i][c]
                M[i] = [M[i][j] - f * M[rank][j] for j in range(ncols)]
        rank += 1
        if rank == nr:
            break
    return rank


# =====================================================================
# INDEPENDENT PREDICTION ROUTE -- orbit-stabiliser, NOT assumed
#
# This route never sees a target dimension. It computes the predicted
# stabiliser dimension purely from STRUCTURE:
#
#   dim(stabiliser of unit u in Der(O))
#       = dim(Der(O))  -  rank( image of the action D -> D(u) on Der(O) )
#
# Derivation: Der(O) acts on the imaginary octonions; the stabiliser of u
# is the kernel of the linear map  phi_u : D -> D(u)  restricted to Der(O).
# rank-nullity on phi_u gives the identity above, where the "image" is the
# tangent space to the orbit of u (orbit-stabiliser).
#
#   - dim(Der(O)) is the exact-rational nullspace dim of the derivation
#     constraint matrix (the g2 carrier), computed here, not asserted.
#   - rank(image) is the exact-rational rank of { D_i(u) } over a basis
#     {D_i} of Der(O), computed here, not asserted.
#
# The integer 8 is NEVER fed in. For a genuine imaginary unit the orbit has
# rank 6 (the S^6 orbit) so the prediction lands at 14 - 6; for the zero
# vector the orbit collapses to rank 0 and the prediction is the full 14
# (a vacuous fixing -- caught by the non-trivial-orbit requirement below).
# The blind SMT ladder dimension must AGREE with this prediction.
# =====================================================================

def derivation_algebra_basis(table: list[list[list[int]]]) -> tuple[int, list[list[Fraction]]]:
    """Exact basis of Der(O) (= g2 carrier). Returns (dim, basis vectors)."""
    dim = len(table)
    ncols = dim * dim
    der_rows = derivation_constraint_rows(table)
    pivot_cols, rref_rows = rref_fraction(der_rows, ncols)
    basis = nullspace_basis(pivot_cols, rref_rows, ncols)
    return len(basis), basis


def apply_derivation(dvec: list[Fraction], unit: list[int], dim: int) -> list[Fraction]:
    """(D u)_row = sum_col d[row, col] u[col], with d flattened as row + col*dim."""
    out = [Fraction(0)] * dim
    for row in range(dim):
        s = Fraction(0)
        for col in range(dim):
            coeff = unit[col]
            if coeff:
                s += dvec[row + col * dim] * coeff
        out[row] = s
    return out


def orbit_stabiliser_prediction(table: list[list[list[int]]], unit: list[int]) -> dict[str, Any]:
    """Predict stabiliser dim of `unit` from structure: g2_dim - orbit_rank.

    No target dimension is used. Both terms are computed exactly from the
    derivation algebra and the chosen unit."""
    dim = len(table)
    g2_dim, g2_basis = derivation_algebra_basis(table)
    image_rows = [apply_derivation(b, unit, dim) for b in g2_basis]
    orbit_rank = matrix_rank_fraction([row[:] for row in image_rows], dim)
    return {
        "g2_dim_from_kernel": g2_dim,
        "orbit_rank_of_unit": orbit_rank,
        "predicted_stabiliser_dim": g2_dim - orbit_rank,
        "orbit_is_nontrivial": orbit_rank > 0,
        "note": "predicted = dim(Der(O)) - rank(D->D(u)); no target integer fed in",
    }


# =====================================================================
# SMT HELPERS
# =====================================================================

def z3_real(value: Fraction | int) -> "z3.ArithRef":
    if isinstance(value, Fraction):
        return z3.RealVal(fraction_text(value))
    return z3.RealVal(value)


def z3_linear(coeffs, variables) -> "z3.ArithRef":
    terms = [z3_real(c) * v for c, v in zip(coeffs, variables) if c != 0]
    return z3.Sum(terms) if terms else z3.RealVal(0)


def cvc5_real(solver, value: Fraction | int):
    return solver.mkReal(fraction_text(value)) if isinstance(value, Fraction) else solver.mkReal(str(value))


def cvc5_join(solver, terms, kind, empty_value: bool):
    if not terms:
        return solver.mkBoolean(empty_value)
    if len(terms) == 1:
        return terms[0]
    return solver.mkTerm(kind, *terms)


def cvc5_linear(solver, coeffs, variables):
    terms = []
    for c, v in zip(coeffs, variables):
        if c == 0:
            continue
        if c == 1:
            terms.append(v)
        else:
            terms.append(solver.mkTerm(Kind.MULT, cvc5_real(solver, c), v))
    return cvc5_join(solver, terms, Kind.ADD, True) if terms else cvc5_real(solver, 0)


# =====================================================================
# FIX 1 -- BLIND DIMENSION VIA SMT
#
# kernel K = { d in R^ncols : A d = 0 } for constraint matrix A (rows).
# We decide dim(K) without telling any solver a target.
#
#   SAT(k): there exist scalars and k vectors v_1..v_k each in K, with the
#           k x k Gram-style independence witnessed by requiring a specific
#           coordinate pattern to be nonzero. We instead use the cleaner,
#           solver-honest formulation:
#             "is there a kernel vector NOT in span(W)?"  for a growing W.
#   We grow W one independent kernel vector at a time. At each step the SMT
#   asks: exists d with A d = 0 AND d not in span(W). SAT -> add the next minted
#   (exact-RREF) independent witness -> repeat. The first k where the query is
#   UNSAT means span(W) = K, so dim = |W| = k.
#
# The number k is produced by counting SMT SAT answers until an SMT UNSAT.
# RREF only MINTS candidate vectors; the dimension is read off SMT verdicts.
# No target dimension is ever asserted to any solver or to the verdict.
# =====================================================================

def _z3_exists_kernel_outside_span(name, rows, ncols, span):
    """z3: exists d (Real^ncols) with  A d = 0,  d _|_ span(W),  d != 0.

    Purely existential QF_LRA, exact. Linear-algebra fact: K=ker(A) is a
    subspace; K intersect W^perp is nonzero iff span(W) does NOT cover K.
      SAT  -> a kernel vector orthogonal to span(W) and nonzero exists
              -> dim(K) > |W|.
      UNSAT-> the only kernel vector orthogonal to span(W) is 0
              -> span(W) covers K -> dim(K) == |W|.
    The verdict (sat/unsat) is what the ladder counts; no target dim asserted."""
    solver = z3.Solver()
    d = [z3.Real(f"{name}_d_{i}") for i in range(ncols)]
    for row in rows:
        if any(row):
            solver.add(z3_linear(row, d) == 0)
    for w in span:
        solver.add(z3.Sum([z3_real(w[i]) * d[i] for i in range(ncols) if w[i] != 0]) == 0)
    solver.add(z3.Or([d[i] != 0 for i in range(ncols)]))
    status = solver.check()
    return "sat" if status == z3.sat else ("unsat" if status == z3.unsat else str(status))


def _cvc5_exists_kernel_outside_span(name, rows, ncols, span):
    # pylint no-member is a false positive: cvc5.Solver lives in a C-extension
    # that pylint cannot introspect statically. It exists at runtime (used below).
    solver = cvc5.Solver()  # pylint: disable=no-member
    solver.setLogic("QF_LRA")
    rs = solver.getRealSort()
    d = [solver.mkConst(rs, f"{name}_d_{i}") for i in range(ncols)]
    zero = cvc5_real(solver, 0)
    for row in rows:
        if any(row):
            solver.assertFormula(solver.mkTerm(Kind.EQUAL, cvc5_linear(solver, row, d), zero))
    for w in span:
        solver.assertFormula(solver.mkTerm(Kind.EQUAL, cvc5_linear(solver, w, d), zero))
    nz = [solver.mkTerm(Kind.NOT, solver.mkTerm(Kind.EQUAL, d[i], zero)) for i in range(ncols)]
    solver.assertFormula(cvc5_join(solver, nz, Kind.OR, False))
    res = solver.checkSat()
    if res.isSat():
        return "sat"
    if res.isUnsat():
        return "unsat"
    return str(res)


def blind_dimension_via_smt(name: str, rows: list[list[int]], ncols: int) -> dict[str, Any]:
    """Decide dim(kernel) by an SMT SAT/UNSAT ladder. No target dim fed in.

    Witness source: exact RREF nullspace vectors (small, exact). RREF only MINTS
    candidate independent kernel vectors; the DIMENSION is decided by the solvers:
    we grow the span one minted vector at a time and at each step ask both z3 and
    cvc5 whether a kernel vector outside the current span exists.
      step k (span size k): SAT  -> dim > k, add the next minted vector.
                            UNSAT -> dim == k, stop.
    The reported blind_dim is the span size at the first SMT UNSAT. Counting
    SMT verdicts gives the dimension; no integer target is asserted anywhere."""
    pivot_cols, rref_rows = rref_fraction(rows, ncols)
    minted = nullspace_basis(pivot_cols, rref_rows, ncols)  # candidate independent kernel vectors

    span: list[list[Fraction]] = []
    sat_steps: list[dict[str, Any]] = []
    blind_dim = 0
    for step in range(len(minted) + 1):
        z3_status = _z3_exists_kernel_outside_span(f"{name}_blind_{step}", rows, ncols, span)
        cvc5_status = _cvc5_exists_kernel_outside_span(f"{name}_blind_{step}", rows, ncols, span)
        sat_steps.append({"step": step, "span_size": len(span), "z3": z3_status,
                          "cvc5": cvc5_status, "agree": z3_status == cvc5_status})
        if z3_status == "unsat" and cvc5_status == "unsat":
            blind_dim = len(span)
            break
        if z3_status == "sat" and cvc5_status == "sat":
            if step < len(minted):
                span.append(minted[step])
                blind_dim = len(span)
                continue
            # solvers say more vectors exist but we ran out of minted ones
            blind_dim = len(span)
            break
        # disagreement or unknown -> stop and report honestly
        blind_dim = len(span)
        break
    return {
        "blind_dim": blind_dim,
        "steps": sat_steps,
        "both_solvers_agreed_every_step": all(s["agree"] for s in sat_steps),
        "terminated_on_unsat": sat_steps[-1]["z3"] == "unsat" and sat_steps[-1]["cvc5"] == "unsat",
        "witness_span": span,
    }


# =====================================================================
# FIX 2 -- SHARP VALUE-COUPLED NEGATIVE CONTROL
#
# Two-unit fixing (e1,e2) gives stabiliser dim = D2 (computed blind here).
# Value-coupled query: "exists a kernel vector OUTSIDE the D2-dim witness span?"
#   - with BOTH unit-fixing constraints present:  UNSAT (dim is exactly D2)
#   - DROP one unit-fixing constraint:            SAT  (single-unit stabiliser
#                                                  has dim 8 > D2, so a vector
#                                                  outside the D2 span exists)
# The flip unsat<->sat is tied to the specific integer D2 (computed, not fed).
# =====================================================================

def sharp_value_control(table, e1, e2) -> dict[str, Any]:
    dim = len(table)
    ncols = dim * dim
    der_rows = derivation_constraint_rows(table)

    two_unit_rows = der_rows + fixing_constraint_rows(dim, [e1, e2])
    one_unit_rows = der_rows + fixing_constraint_rows(dim, [e1])

    # Independently compute the two-unit stabiliser dim, blind, via SMT.
    two_blind = blind_dimension_via_smt("two_unit_ctrl", two_unit_rows, ncols)
    d2 = two_blind["blind_dim"]
    d2_span = two_blind["witness_span"]  # d2 independent kernel vectors

    # Value-coupled query A: with BOTH fixing rows, is there a kernel vector
    # outside the d2-dim span?  Expect UNSAT (sharp: dim is exactly d2).
    z3_both = _z3_exists_kernel_outside_span("sharp_both", two_unit_rows, ncols, d2_span)
    cvc5_both = _cvc5_exists_kernel_outside_span("sharp_both", two_unit_rows, ncols, d2_span)

    # Value-coupled query B: DROP one fixing constraint (single-unit). Same
    # d2-dim span. Expect SAT (su(3) is dim 8 > d2, vector outside span exists).
    z3_dropped = _z3_exists_kernel_outside_span("sharp_dropped", one_unit_rows, ncols, d2_span)
    cvc5_dropped = _cvc5_exists_kernel_outside_span("sharp_dropped", one_unit_rows, ncols, d2_span)

    flip = (z3_both == "unsat" and z3_dropped == "sat"
            and cvc5_both == "unsat" and cvc5_dropped == "sat")

    return {
        "independently_computed_control_dim": d2,
        "control_dim_span_sha256": vectors_sha(d2_span),
        "query_both_fixing_outside_span_z3": z3_both,
        "query_both_fixing_outside_span_cvc5": cvc5_both,
        "query_dropped_fixing_outside_span_z3": z3_dropped,
        "query_dropped_fixing_outside_span_cvc5": cvc5_dropped,
        "drop_control_flips_unsat_to_sat": flip,
        "value_coupled": True,
        "note": "the flip is tied to the SPECIFIC integer d2 computed blind; the d2-dim span is the value the control predicts",
    }


# =====================================================================
# ADMISSION TESTS
# Probe family M: explicit derivation row probes + unit-fixing row probes.
# Constraint set C: D is an octonion derivation AND D(e1)=0.
# =====================================================================

def run_positive_tests(table) -> dict[str, Any]:
    dim = len(table)
    ncols = dim * dim
    fixed_unit = [0, 1, 0, 0, 0, 0, 0, 0]
    der_rows = derivation_constraint_rows(table)
    unit_rows = der_rows + fixing_constraint_rows(dim, [fixed_unit])

    # Blind: solvers decide the stabiliser dimension of Der(O) fixing the unit.
    blind = blind_dimension_via_smt("fix_e1", unit_rows, ncols)

    # INDEPENDENT prediction (orbit-stabiliser, no target dim): g2_dim - orbit_rank.
    # Computed from the SAME `fixed_unit`, by a route that never touches the SMT
    # ladder. Correctness lives here: blind dim must AGREE with this prediction.
    prediction = orbit_stabiliser_prediction(table, fixed_unit)

    # Supportive cross-checks (NOT load-bearing): RREF rank and sympy nullspace.
    pivot_cols, _rref_rows = rref_fraction(unit_rows, ncols)
    rref_null_dim = ncols - len(pivot_cols)
    sympy_null_dim = None
    if sp is not None:
        M = sp.Matrix([row for row in unit_rows if any(row)])
        sympy_null_dim = len(M.nullspace())

    return {
        "candidate": "Der(O) with D(e1)=0 (su(3) candidate)",
        "blind_smt_stabilizer_dim": blind["blind_dim"],
        "blind_smt_both_solvers_agreed": blind["both_solvers_agreed_every_step"],
        "blind_smt_terminated_on_unsat": blind["terminated_on_unsat"],
        "independent_prediction": prediction,
        "blind_matches_independent_prediction":
            blind["blind_dim"] == prediction["predicted_stabiliser_dim"],
        "fixing_is_nontrivial": prediction["orbit_is_nontrivial"],
        "rref_nullspace_dim_crosscheck": rref_null_dim,
        "sympy_nullspace_dim_crosscheck": sympy_null_dim,
        "blind_matches_rref": blind["blind_dim"] == rref_null_dim,
        "blind_matches_sympy": (sympy_null_dim is None) or (blind["blind_dim"] == sympy_null_dim),
        "admissibility": "candidate su(3) stabiliser survived the blind SMT dimension ladder",
        "_blind_detail": blind,
    }


def run_negative_tests(table) -> dict[str, Any]:
    e1 = [0, 1, 0, 0, 0, 0, 0, 0]
    e2 = [0, 0, 1, 0, 0, 0, 0, 0]
    sharp = sharp_value_control(table, e1, e2)
    return {
        "exclusion_form": "sharp value-coupled SMT flip (unsat<->sat) tied to an independently computed dimension",
        "sharp_control": sharp,
    }


def run_boundary_tests(table) -> dict[str, Any]:
    """Boundary: full Der(O) with NO unit fixing. The probe family M (unit-fixing
    rows) is absent, so M cannot distinguish the su(3) class from g2. The blind
    dimension here should be 14 (g2). This is where C becomes thin: removing the
    fixing rows removes the distinguishing probe."""
    dim = len(table)
    ncols = dim * dim
    der_rows = derivation_constraint_rows(table)
    blind = blind_dimension_via_smt("no_fix_boundary", der_rows, ncols)
    pivot_cols, _ = rref_fraction(der_rows, ncols)
    # Independent: the same g2_dim the orbit-stabiliser route derives from the
    # derivation algebra kernel. No literal 14 anywhere.
    g2_dim_independent, _ = derivation_algebra_basis(table)
    return {
        "configuration": "Der(O) with no unit-fixing probe (g2 candidate)",
        "blind_smt_dim": blind["blind_dim"],
        "rref_dim_crosscheck": ncols - len(pivot_cols),
        "g2_dim_independent_crosscheck": g2_dim_independent,
        "blind_matches_independent": blind["blind_dim"] == g2_dim_independent,
        "boundary_type": "sharp (formal): without the fixing probe, M cannot resolve su(3) inside g2",
        "blind_matches_rref": blind["blind_dim"] == (ncols - len(pivot_cols)),
    }


# =====================================================================
# MAIN
# =====================================================================

def build_result() -> dict[str, Any]:
    table = build_octonion_table()

    positive = run_positive_tests(table)
    negative = run_negative_tests(table)
    boundary = run_boundary_tests(table)

    # Honest tool-depth: z3 and cvc5 are load-bearing iff both ran and the
    # blind ladder + sharp flip actually used them.
    z3_ran = TOOL_MANIFEST["z3"]["tried"]
    cvc5_ran = TOOL_MANIFEST["cvc5"]["tried"]
    if z3_ran:
        TOOL_MANIFEST["z3"]["used"] = True
        TOOL_MANIFEST["z3"]["reason"] = "load-bearing: blind dimension SAT/UNSAT ladder and value-coupled sharp control flip"
        TOOL_INTEGRATION_DEPTH["z3"] = "load_bearing"
    if cvc5_ran:
        TOOL_MANIFEST["cvc5"]["used"] = True
        TOOL_MANIFEST["cvc5"]["reason"] = "load-bearing: independent SMT confirmation of every blind-ladder step and the sharp flip"
        TOOL_INTEGRATION_DEPTH["cvc5"] = "load_bearing"

    # numpy supportive float-rank cross-check (not load-bearing)
    ncols = len(table) * len(table)
    der_rows = derivation_constraint_rows(table)
    A = np.array([r for r in der_rows if any(r)], dtype=float)
    numpy_g2_dim = ncols - int(np.linalg.matrix_rank(A))

    # ----- BLIND PROPERTY CHECK (no target dim anywhere in the decision) -----
    # Correctness is STRUCTURAL: the blind SMT ladder dimension must AGREE with
    # the independent orbit-stabiliser prediction (g2_dim - orbit_rank), and the
    # fixing must be non-trivial (orbit_rank > 0, otherwise the fixing constrains
    # nothing and the "reduction" is vacuous). No integer target appears here.
    blind_ok = (
        positive["blind_smt_both_solvers_agreed"]
        and positive["blind_smt_terminated_on_unsat"]
        and positive["blind_matches_independent_prediction"]
        and positive["fixing_is_nontrivial"]
        and positive["blind_matches_rref"]
        and positive["blind_matches_sympy"]
    )

    # ----- SHARP PROPERTY CHECK (flip tied to computed dim) -----
    sharp = negative["sharp_control"]
    sharp_ok = (
        sharp["drop_control_flips_unsat_to_sat"]
        and sharp["independently_computed_control_dim"] >= 1
    )

    # ----- BOUNDARY (g2) STRUCTURAL CHECK -----
    # The no-fixing blind dim must agree with the independently derived g2 dim.
    boundary_ok = bool(boundary["blind_matches_independent"])

    # Independent prediction figures (decided by structure, never asserted):
    structural = {
        "su3_blind_dim": positive["blind_smt_stabilizer_dim"],
        "su3_independent_predicted_dim": positive["independent_prediction"]["predicted_stabiliser_dim"],
        "su3_orbit_rank": positive["independent_prediction"]["orbit_rank_of_unit"],
        "g2_blind_dim": boundary["blind_smt_dim"],
        "g2_independent_dim": boundary["g2_dim_independent_crosscheck"],
        "two_unit_blind_dim": sharp["independently_computed_control_dim"],
        "numpy_g2_dim_crosscheck": numpy_g2_dim,
    }

    # all_pass: true only if solvers ran AND every dimension is decided by
    # STRUCTURAL AGREEMENT (blind SMT == independent route) plus the sharp flip.
    # The integers 8/14/3 do NOT appear in this decision; they live only in
    # reproduction_report below for human comparison.
    all_pass = bool(
        z3_ran and cvc5_ran
        and blind_ok
        and sharp_ok
        and boundary_ok
    )

    # Reproduction report: the literature values, kept OUT of the gate. These are
    # for a human to eyeball the known G2/SU(3) reduction; they are not consulted
    # by all_pass / blind_ok / sharp_ok / boundary_ok above.
    reproduction_report = {
        "expected_g2_dim_literature": 14,
        "expected_su3_dim_literature": 8,
        "expected_two_unit_dim_literature": 3,
        "g2_blind_dim_observed": structural["g2_blind_dim"],
        "su3_blind_dim_observed": structural["su3_blind_dim"],
        "two_unit_blind_dim_observed": structural["two_unit_blind_dim"],
        "matches_literature": (
            structural["g2_blind_dim"] == 14
            and structural["su3_blind_dim"] == 8
            and structural["two_unit_blind_dim"] == 3
        ),
        "note": "literature comparison only; NOT used by the gate",
    }

    # Classification stays HONEST: not hardcoded to canonical. We reuse the
    # module-level value; we only assert the blind+sharp properties and promotion
    # is owner-gated.
    result_classification = classification

    result = {
        "name": "cand_canonical_v2 -- G2/SU(3) octonion derivation reduction (blind+sharp)",
        "probe_family": "M_unit_fixing_derivation_row_probe",
        "constraint_set": "C_octonion_derivation_AND_unit_fixing",
        "tool_manifest": TOOL_MANIFEST,
        "tool_integration_depth": TOOL_INTEGRATION_DEPTH,
        "source_math_provenance": {
            "source_scout": "system_v5/ops/formal_scouts/foundation_foundation_r5_g2_su3_reduction_jax.py",
            "reused": "Cayley-Dickson octonion structure constants; derivation constraint matrix; unit-fixing rows; Der(O)=g2 dim 14; stabilizer of e1 = su(3) dim 8",
        },
        "blind_property": {
            "where_in_code": "blind_dimension_via_smt() ladder, agreement checked against orbit_stabiliser_prediction()",
            "claim": "stabiliser dimension decided by z3/cvc5 SAT(k)->UNSAT(k+1) ladder; correctness is the AGREEMENT between that blind dim and the independent orbit-stabiliser prediction (g2_dim - orbit_rank); no target integer is fed to any solver or to the verdict",
            "no_dim_literal_fed_to_solver": True,
            "independent_prediction": positive["independent_prediction"],
            "blind_matches_independent_prediction": positive["blind_matches_independent_prediction"],
            "fixing_is_nontrivial": positive["fixing_is_nontrivial"],
            "holds": blind_ok,
            "detail": positive["_blind_detail"],
        },
        "sharp_property": {
            "where_in_code": "sharp_value_control()",
            "claim": "value-coupled control predicts the SPECIFIC blind-computed integer d2; both-fixing -> UNSAT (outside d2-span), drop-one-fixing -> SAT; flip is tied to d2",
            "holds": sharp_ok,
            "detail": sharp,
        },
        "structural_dimensions": structural,
        "reproduction_report": reproduction_report,
        "positive": positive,
        "negative": negative,
        "boundary": boundary,
        "classification": result_classification,
        "surviving_alternatives": [
            "su(3) stabiliser of a single imaginary unit (dim 8) -- the candidate",
            "g2 = Der(O) (dim 14) when no fixing probe is active -- boundary class",
        ],
        "claim_ceiling": "tool_lego_fit_probe; blind+sharp SMT properties demonstrated; NOT canonical/bridge/axis admission by itself",
        "promotion_allowed": False,
        "formal_admission_allowed": False,
        "next_lego_target": "none",
        "promotion_condition": "owner-gated: promote only after a separate reconciled queue row + fresh blind audit of the blind/sharp properties",
        "blocked_until": "owner confirms blind+sharp audit in fresh context and reconciles a queue row",
        "demotion_condition": "demote if blind_ok or sharp_ok is False, or if any named criterion below fails",
        "out_of_scope": [
            "no lego promotion from this probe alone",
            "no bridge, axis, engine, emergence, Tier D, or coupling claim",
        ],
        "all_pass": all_pass,
        "criteria_checked": [
            "C1 z3 ran",
            "C2 cvc5 ran",
            "C3 blind ladder: both solvers agreed every step and terminated on UNSAT",
            "C4 blind su(3) dim AGREES with the independent orbit-stabiliser prediction (g2_dim - orbit_rank); this is the load-bearing structural correctness check",
            "C5 fixing is non-trivial (orbit_rank > 0): the unit-fixing actually reduces the dimension; rules out vacuous-fixing attacks",
            "C6 boundary g2 blind dim AGREES with the independently derived Der(O) dimension",
            "C7 sharp value-coupled control flips unsat->sat on dropping one fixing constraint",
            "C8 (report only, NOT gating) literature reproduction g2=14, su3=8, two-unit=3 in reproduction_report",
        ],
    }
    return result


if __name__ == "__main__":
    results = build_result()
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "a2_state", "sim_results")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "cand_canonical_v2_results.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"Results written to {out_path}")
    print(
        "CAND_CANONICAL_V2_DONE "
        f"all_pass={str(results['all_pass']).lower()} "
        f"blind_ok={str(results['blind_property']['holds']).lower()} "
        f"sharp_ok={str(results['sharp_property']['holds']).lower()} "
        f"g2={results['structural_dimensions']['g2_blind_dim']} "
        f"su3={results['structural_dimensions']['su3_blind_dim']} "
        f"two_unit={results['structural_dimensions']['two_unit_blind_dim']}"
    )
    raise SystemExit(0 if results["all_pass"] else 1)
