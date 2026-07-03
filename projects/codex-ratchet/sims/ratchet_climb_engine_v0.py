#!/usr/bin/env python3
"""ratchet_climb_engine_v0 -- the ratchet as an ACTUAL climbing process, run.

QUARANTINE_EXPLORATORY. classification="scratch_diagnostic". promotion_allowed=False.

The point this sim proves: the ratchet CLIMBS the weakest-structure ladder one
MINIMAL TOOTH at a time -- L0 -> L1 -> L2 -> L3 -- each rung FORCED by a distinct
measured lost distinction, never a batch jump. (An independent node's first build
jumped L0->L3 in one step and its smallest-step fix was broken Python; this is the
corrected, running version.)

Definition made decidable (all data finite):
  Level strength IS expressible distinction. D_L(items) = partition induced by
  level-L readouts on the finite carrier. L <= L' iff D_L coarsens D_L'
  (refinement on finite partitions -- the weakness order is MEASURED, not chosen).
  A demand = a witness pair (i,j) with provenance that MUST be separated, plus an
  admissibility flag (is there a constraint witness at all?).
  Lift trigger = Lost(L) : the open admissible demands the current level cannot
  separate, found by EXHAUSTIVE enumeration (Minimalist failure is a proof).
  SMALLEST STEP: admit the WEAKEST ladder level above current that strictly refines
  the partition AND resolves >=1 open lost demand; stronger levels that would also
  resolve it are logged REJECTED_UNFORCED (MSS teeth). Lock append-only.
Theorems checked: T1 termination, T2 monotone expressivity (each tooth strictly
  refines), T3 no unforced lift, T4 pawl (level index strictly rises; nothing
  dropped), T5 basin (demand-order-permuted runs converge to the same ladder).
The forcing facts are real: |0> vs |1> needs <Z> (rung L1); |+> vs |-> needs <X>
  (rung L2, invisible to Z); R(2pi)|0> vs |0> has IDENTICAL rho, separable only by
  the spinor lift (rung L3) -- proven by enumeration that no rho-level separates it.
"""
import itertools, json, sys
import numpy as np

EPS = 1e-9
Xg = np.array([[0, 1], [1, 0]], dtype=complex)
Yg = np.array([[0, -1j], [1j, 0]], dtype=complex)
Zg = np.array([[1, 0], [0, -1]], dtype=complex)

def Rz(theta):  # spinor z-rotation: Rz(2pi) = -I on psi, identity on rho
    return np.array([[np.exp(-1j*theta/2), 0], [0, np.exp(1j*theta/2)]], dtype=complex)

def q(v):  # quantize a real to an eps grid for exact hashing
    return int(round(v/EPS))

# ---- finite carrier: named pure/mixed preps with psi (None if mixed) + rho ----
def make_carrier():
    ket0 = np.array([1, 0], dtype=complex)
    ket1 = np.array([0, 1], dtype=complex)
    plus = np.array([1, 1], dtype=complex)/np.sqrt(2)
    minus = np.array([1, -1], dtype=complex)/np.sqrt(2)
    k0_720 = Rz(2*np.pi) @ ket0            # = -|0>, rho identical to |0>
    def it(name, psi):
        return {"name": name, "psi": psi,
                "rho": (np.eye(2, dtype=complex)/2 if psi is None else np.outer(psi, psi.conj()))}
    return [
        it("k0", ket0), it("k1", ket1), it("plus", plus), it("minus", minus),
        it("mix", None), it("k0_720", k0_720), it("k0_copy", ket0.copy()),
    ]

# ---- ladder: each level = the readout that defines its expressible distinctions ----
LADDER = ["L0_trivial", "L1_Z", "L2_Pauli", "L3_Spinor"]

def readout(level, item):
    if level == "L0_trivial":
        return ()
    if level == "L1_Z":
        return (q(np.real(np.trace(Zg @ item["rho"]))),)
    if level == "L2_Pauli":
        return tuple(q(np.real(np.trace(P @ item["rho"]))) for P in (Xg, Yg, Zg))
    if level == "L3_Spinor":  # retains the full lifted vector (global phase/720) that rho erases
        base = tuple(q(np.real(np.trace(P @ item["rho"]))) for P in (Xg, Yg, Zg))
        if item["psi"] is None:
            return base + ("mixed",)
        return base + (q(np.real(item["psi"][0])), q(np.imag(item["psi"][0])),
                       q(np.real(item["psi"][1])), q(np.imag(item["psi"][1])))
    raise KeyError(level)

def partition(level, items):
    cls = {}
    for i, it in enumerate(items):
        cls.setdefault(readout(level, it), []).append(i)
    return sorted(tuple(sorted(v)) for v in cls.values())

def separates(level, items, i, j):
    return readout(level, items[i]) != readout(level, items[j])

def refines(pA, pB):  # pA finer-or-equal to pB
    look = {i: k for k, c in enumerate(pB) for i in c}
    return all(len({look[i] for i in c}) == 1 for c in pA)

def run(order_seed):
    items = make_carrier()
    ix = {it["name"]: k for k, it in enumerate(items)}
    demands = [  # (name, i, j, admissible, forcing-rung-expectation)
        ("sep_0_vs_1",       ix["k0"], ix["k1"],     True),
        ("sep_plus_vs_minus", ix["plus"], ix["minus"], True),
        ("sep_720_process",  ix["k0"], ix["k0_720"], True),
        ("void_identical",   ix["k0"], ix["k0_copy"], False),
    ]
    np.random.default_rng(order_seed).shuffle(demands)   # N01: order varies per run

    level = "L0_trivial"; open_d = list(demands); ledger = []; admitted = [level]
    T = {"T1_termination": True, "T2_monotone_expressivity": True,
         "T3_no_unforced_lift": True, "T4_pawl": True}
    measure_prev = None
    for step in range(1, 12):
        lost = []
        for d in list(open_d):
            name, i, j, adm = d
            if separates(level, items, i, j):
                ledger.append({"step": step, "event": "DEMAND_MET", "demand": name, "level": level}); open_d.remove(d); continue
            if not adm and all(not separates(L, items, i, j) for L in LADDER):
                ledger.append({"step": step, "event": "DEMAND_VOID", "demand": name,
                               "reason": "no level separates; no constraint witness -> trigger refuses"}); open_d.remove(d); continue
            lost.append(d)
        measure = (len(open_d), -LADDER.index(level))
        if not lost:
            ledger.append({"step": step, "event": "NO_LIFT", "level": level, "note": "Minimalist wins: no admissible lost distinction"}); break
        cur = LADDER.index(level); cur_sz = len(partition(level, items))
        # SMALLEST STEP: weakest level above current that strictly refines AND resolves >=1 lost demand
        resolvers = {}
        for d in lost:
            _, i, j, _ = d
            for L in LADDER[cur+1:]:
                if separates(L, items, i, j):
                    resolvers.setdefault(d[0], []).append(L)
        cands = sorted({L for Ls in resolvers.values() for L in Ls
                        if len(partition(L, items)) > cur_sz}, key=LADDER.index)
        if not cands:
            ledger.append({"step": step, "event": "FRONTIER", "unresolvable": [d[0] for d in lost]}); break
        weakest = cands[0]
        this_tooth = [nm for nm, Ls in resolvers.items() if weakest in Ls]
        for L in cands[1:]:
            ledger.append({"step": step, "event": "REJECTED_UNFORCED", "candidate": L,
                           "classes": len(partition(L, items)), "vs_weakest": len(partition(weakest, items))})
        for (nm, i, j, _) in [d for d in lost if d[0] in this_tooth]:
            ledger.append({"step": step, "event": "MINIMALIST_FAILED_PROOF", "demand": nm, "level": level,
                           "readout_i": str(readout(level, items[i])), "readout_j": str(readout(level, items[j]))})
        p_old = partition(level, items); p_new = partition(weakest, items)
        if not (refines(p_new, p_old) and p_new != p_old): T["T2_monotone_expressivity"] = False
        if LADDER.index(weakest) <= cur: T["T4_pawl"] = False
        ledger.append({"step": step, "event": "LIFT_LOCKED", "from": level, "to": weakest,
                       "forced_by": this_tooth, "classes_before": len(p_old), "classes_after": len(p_new)})
        level = weakest; admitted.append(level)
        if measure_prev is not None and not (measure < measure_prev): T["T1_termination"] = False
        measure_prev = measure
    if any(e["event"] == "LIFT_LOCKED" and not e["forced_by"] for e in ledger): T["T3_no_unforced_lift"] = False
    return {"terminal_level": level, "admitted_ladder": admitted,
            "terminal_classes": len(partition(level, items)), "ledger": ledger, "theorems": T}

def main():
    runs = {s: run(s) for s in (11, 23, 47, 101)}
    t5 = len({(r["terminal_level"], r["terminal_classes"], tuple(r["admitted_ladder"])) for r in runs.values()}) == 1
    out = {"classification": "scratch_diagnostic", "promotion_allowed": False,
           "runs": runs, "T5_basin_convergence": t5}
    path = __file__.replace(".py", "_results.json")
    json.dump(out, open(path, "w"), indent=1, default=str)
    r = runs[11]
    print("ladder climbed:", " -> ".join(r["admitted_ladder"]))
    for e in r["ledger"]:
        if e["event"] in ("LIFT_LOCKED", "NO_LIFT", "DEMAND_VOID", "REJECTED_UNFORCED", "FRONTIER"):
            print("  ", e)
    print("theorems:", r["theorems"], " T5_basin(4 orders):", t5)
    ok = all(r["theorems"].values()) and t5 and r["admitted_ladder"] == LADDER
    print("SINGLE-TOOTH CLIMB L0->L1->L2->L3:", r["admitted_ladder"] == LADDER)
    if ok:
        print("PASS ratchet_climb_engine_v0")
    print("ALL_GATES:", "PASS" if ok else "FAIL", "->", path)
    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
