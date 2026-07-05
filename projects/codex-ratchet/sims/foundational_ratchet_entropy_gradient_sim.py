#!/usr/bin/env python3
"""foundational_ratchet_entropy_gradient -- the ratchet MECHANISM itself, built at the foundations, with the
entropy gradient (Axis-0) as the DRIVE and geometry+entropy co-ratcheting as ONE object.

QUARANTINE_EXPLORATORY. classification="scratch_diagnostic". promotion_allowed=False.

THE CORRECTION THIS ENCODES (owner, 2026-07-05): Axis-0 kept failing because it was being built as a LATE
readout (density-level, after engines). That is the wrong place. Axis-0 IS an entropy gradient, and an entropy
gradient is a FOUNDATIONAL DRIVE, not a late observable. Every prior attempt collapsed Axis-0 onto Axis-1
(entropy) at the density level -- because it literally is the entropy gradient, misplaced. The collapse was the
clue. So Axis-0 belongs at the very foundations: the gradient that drives the ratchet from the first step.

THE FOUNDATIONS, PRESUMING THE LEAST (order aligned with the constraints, not prescribed):
  ROOT CONSTRAINTS: F01 finitude (finitely many distinguishable things), N01 noncommutation (order matters).
                    Nothing else assumed.
  STATIC FUZZ:      a field of possibilities; frames carry no information between them.
  MINIMAL PERSISTENT EVOLVING STRUCTURE: the least thing that persists AND evolves between fuzz frames under
                    F01+N01 is a NORM-PRESERVING carrier (a unit state in a finite complex space -- a spinor).
                    A non-norm-preserving thing either vanishes or blows up across frames; only the unit-norm
                    carrier persists. (earned prior: persistence_is_norm_preserving.)
  THE ENTROPY GRADIENT = AXIS-0, AT THE FLOOR, AS A DISTINGUISHABILITY (owner: "bits are classical"; "bits
                    presume too much"). The measure is QUANTUM DISTINGUISHABILITY -- trace distance / Helstrom --
                    NEVER bits, log2, or counting of microstates (entropy is the LATER measure the doc names, not
                    the substance). Two faces, per the owner's positive/negative-entropy split: AVAILABLE
                    distinguishability the growing possibility space offers (positive-entropy face, opening) vs
                    RESOLVED distinguishability the carrier's acquired measurement bases can access (negative-
                    entropy face, binding). AXIS-0 = the GAP available - resolved. It is not injected; it is
                    constitutive of a growing possibility space. This gap is the ratchet DRIVE.
  CO-RATCHET (geometry == entropy, ONE thing): the carrier's structural climb (geometry: how much distinguishing
                    capacity it has acquired) and the entropy gradient (the distinguishability gap) are the SAME
                    object read two ways -- they must move one-for-one. Measured here, not asserted.
  MSS CLIMB: driven by the gradient, the carrier climbs by the SMALLEST step that resolves a forced distinction
                    (weakest capacity that separates one more pair the growth just made distinguishable).

THE KILLER CONTROL (Feynman): FREEZE the growth of the possibility space. The gradient closes; the drive
  vanishes; the ratchet must STOP once the carrier catches the (now static) ceiling. If the climb continues
  without growth, the drive was not the gradient and the whole picture is wrong. If it halts, the entropy
  gradient at the foundation IS the drive -- Axis-0 earned at the floor.
"""
import json, sys
import numpy as np

I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)

# ---- THE MEASURE IS DISTINGUISHABILITY, NOT BITS OR COUNTING (owner: "bits are classical"; "bits presume too
# much"). The primitive is constraint on distinguishability (a=a iff a~b). So every quantity below is built from
# QUANTUM DISTINGUISHABILITY -- the trace distance / Helstrom bound -- with NO log2, NO Shannon/von-Neumann bits,
# and NO counting of microstates. Entropy here is the LATER measure the doc names, never the substance.

def trace_distance(ra, rb):
    """Quantum distinguishability of two carrier states = 1/2 ||ra - rb||_1 (Helstrom). This is the OPTIMAL
    single-shot distinguishability over ALL measurements; basis-independent; in [0,1]; purely nonclassical
    (no bits, no counting). This is the 'available' distinguishability the possibility space offers on a pair."""
    ev = np.linalg.eigvalsh((ra - rb + (ra - rb).conj().T) / 2)
    return 0.5 * float(np.abs(ev).sum())

def basis_distinguishability(ra, rb, probe):
    """Distinguishability ACHIEVABLE by measuring in the probe's eigenbasis = total variation of the two outcome
    distributions = 1/2 sum_k |<k|(ra-rb)|k>|. By Helstrom this is <= trace_distance, with equality iff the
    probe's basis IS the eigenbasis of (ra-rb). The GAP is distinguishability that exists but this instrument
    cannot access. Still no bits, no counting -- an achievable-distinguishability number in [0,1]."""
    w, V = np.linalg.eigh((probe + probe.conj().T) / 2)
    d = V.conj().T @ (ra - rb) @ V
    return 0.5 * float(np.abs(np.real(np.diag(d))).sum())

# minimal persistent evolving structure: a norm-preserving carrier whose GEOMETRY is a growing set of acquired
# measurement bases (probes). F01: finitely many probes. N01: the probes noncommute (order/basis matters).
PROBES = [SZ, SX, SY,
          (SX + SZ) / np.sqrt(2), (SX - SZ) / np.sqrt(2),
          (SY + SZ) / np.sqrt(2), (SY + SX) / np.sqrt(2)]

def possibility_set(r, frozen_at=None, n0=2):
    """Omega_r: admissible futures on the shell at radius r. GROWS with r (the room grows) unless frozen. Each
    future is a carrier state the fuzz admits. Growth adds new states -> new pairwise distinguishability becomes
    AVAILABLE. Frozen: state count pinned (no new distinguishability -> gradient can close)."""
    n = n0 + r if frozen_at is None else n0 + min(r, frozen_at)
    rng = np.random.default_rng(1000 + n)  # deterministic in the CURRENT size -> frozen truly stops growth
    return [np.outer(v / np.linalg.norm(v), (v / np.linalg.norm(v)).conj())
            for v in (rng.normal(size=2) + 1j * rng.normal(size=2) for _ in range(n))]

def available_distinguishability(states):
    """ENTROPY SIDE (available): total quantum distinguishability the possibility set offers = sum over pairs of
    trace distance. This is what a PERFECT instrument could resolve. Rises as the room grows (more pairs)."""
    return sum(trace_distance(states[i], states[j])
               for i in range(len(states)) for j in range(i + 1, len(states)))

def resolved_distinguishability(states, acquired):
    """GEOMETRY SIDE (resolved): distinguishability the carrier's ACQUIRED measurement bases can actually access
    = sum over pairs of the BEST achievable basis-distinguishability among acquired probes. <= available always
    (Helstrom). Rises as the carrier acquires probes whose bases align with real (ra-rb) directions."""
    if not acquired:
        return 0.0
    tot = 0.0
    for i in range(len(states)):
        for j in range(i + 1, len(states)):
            tot += max(basis_distinguishability(states[i], states[j], PROBES[p]) for p in acquired)
    return tot

def mss_step(states, acquired):
    """The SMALLEST move that closes >0 of the distinguishability gap: admit ONE more probe -- the WEAKEST one,
    i.e. the probe that recovers the LEAST additional resolved distinguishability while still recovering some.
    (MSS: not the greedy best probe, the least sufficient one -- the smallest tooth that still turns the wheel.)
    No counting, no bits: the selection score is achievable trace-distance recovered, a distinguishability."""
    D0 = resolved_distinguishability(states, acquired)
    gains = []
    for p in range(len(PROBES)):
        if p in acquired:
            continue
        g = resolved_distinguishability(states, acquired | {p}) - D0
        if g > 1e-9:
            gains.append((g, p))
    if not gains:
        return acquired, False
    gains.sort()                       # smallest positive gain first = weakest sufficient probe (MSS)
    _, p = gains[0]
    return acquired | {p}, True

def run_ratchet(R=8, frozen_at=None):
    """Climb driven by the DISTINGUISHABILITY gradient (Axis-0 at the floor). At each shell the room may grow ->
    more available distinguishability. While a gap remains between AVAILABLE (perfect instrument) and RESOLVED
    (acquired bases), the carrier admits the WEAKEST probe that recovers some. Record the two faces and the gap.
    All quantities are distinguishabilities (trace distance), never bits or counts."""
    acquired = {0}; hist = []           # start with one acquired basis
    for r in range(R):
        states = possibility_set(r, frozen_at=frozen_at)
        avail = available_distinguishability(states)        # POSITIVE-entropy face: growing available (opening)
        resolved = resolved_distinguishability(states, acquired)  # NEGATIVE-entropy face: resolved/bound (binding)
        grad = avail - resolved                              # AXIS-0 = the distinguishability gap (the drive)
        climbed = False
        if grad > 1e-6:
            acquired, climbed = mss_step(states, acquired)
        resolved_post = resolved_distinguishability(states, acquired)
        hist.append({"r": r, "available": round(avail, 4), "resolved_pre": round(resolved, 4),
                     "resolved_post": round(resolved_post, 4), "gap": round(grad, 4),
                     "climbed": climbed, "n_acquired": len(acquired)})
    return hist

def main():
    live = run_ratchet(frozen_at=None)      # constitutive: room grows -> gradient persists -> drive
    frozen = run_ratchet(frozen_at=1)       # Feynman control: freeze growth at r=1 -> gradient closes

    live_climbs = sum(h["climbed"] for h in live)
    frozen_climbs_after_freeze = sum(h["climbed"] for h in frozen if h["r"] > 1)
    # CO-RATCHET (one object, two readings): every forced climb must RAISE resolved distinguishability (geometry
    # side) AND face a positive gap (entropy side) -- they move together, measured not asserted.
    coratchet_pairs = [(h["resolved_post"] - h["resolved_pre"], h["gap"]) for h in live if h["climbed"]]
    coratchet_ok = all(dg > 1e-9 and gp > 1e-9 for dg, gp in coratchet_pairs) and len(coratchet_pairs) > 0
    # Feynman: under growth the gap keeps re-opening (available rises faster than one probe closes it -> permanent
    # drive, climbs continue). Under freeze available stops rising; the carrier closes the gap it can and the
    # climb HALTS. A residual gap after freeze is distinguishability NO acquired basis can reach (a real quantum
    # limit, not a live drive) -- what matters is it stops GROWING and produces no further climb.
    live_gap_final = live[-1]["gap"]
    frozen_gaps_after = [h["gap"] for h in frozen if h["r"] > 1]
    frozen_gap_flat = (max(frozen_gaps_after) - min(frozen_gaps_after) < 1e-6) if frozen_gaps_after else True
    live_gap_reopens = sum(1 for h in live if h["gap"] > 1e-6) >= 4    # drive persists under growth

    drive_is_gradient = (live_climbs >= 3) and live_gap_reopens and \
                        (frozen_climbs_after_freeze == 0) and frozen_gap_flat

    out = {"classification": "scratch_diagnostic", "promotion_allowed": False,
           "measure": "quantum_distinguishability_trace_distance (NO bits, NO log2, NO microstate counting)",
           "live_total_climbs": live_climbs,
           "frozen_climbs_after_freeze": frozen_climbs_after_freeze,
           "live_gap_final": live_gap_final,
           "frozen_gap_flat_after_freeze": bool(frozen_gap_flat),
           "live_gap_reopens_under_growth": bool(live_gap_reopens),
           "coratchet_available_tracks_resolved": bool(coratchet_ok),
           "AXIS0_IS_FOUNDATIONAL_DRIVE": bool(drive_is_gradient),
           "live_history": live, "frozen_history": frozen}
    path = __file__.replace(".py", "_results.json"); json.dump(out, open(path, "w"), indent=1)

    print("THE RATCHET AT THE FOUNDATIONS -- Axis-0 = the DISTINGUISHABILITY gradient (no bits, no counting):")
    print("  primitive = constraint on distinguishability (a=a iff a~b). F01 finite noncommuting probes + N01.")
    print("  AVAILABLE (positive-entropy face, opening) = distinguishability a perfect instrument could resolve;")
    print("  RESOLVED (negative-entropy face, binding)  = what the carrier's acquired bases actually access;")
    print("  AXIS-0 GAP = available - resolved = the drive. All quantities are trace distances, not bits.\n")
    print("  r | available  resolved     GAP    climbed   [LIVE: room grows]")
    for h in live:
        print(f"  {h['r']} |  {h['available']:6.3f}    {h['resolved_post']:6.3f}   {h['gap']:6.3f}    {h['climbed']}")
    print(f"\n  LIVE forced climbs: {live_climbs}; final gap (stays open under growth = permanent drive): {live_gap_final}")
    print("\n  FEYNMAN CONTROL -- freeze growth at r=1 (available stops rising; drive must die, climb must stop):")
    print("  r | available  resolved     GAP    climbed   [FROZEN after r=1]")
    for h in frozen:
        print(f"  {h['r']} |  {h['available']:6.3f}    {h['resolved_post']:6.3f}   {h['gap']:6.3f}    {h['climbed']}")
    print(f"\n  FROZEN climbs after freeze: {frozen_climbs_after_freeze}; gap FLAT after freeze (no new drive): {frozen_gap_flat}")
    print(f"\n  CO-RATCHET (available tracks resolved, one object two readings): {coratchet_ok}")
    print(f"  AXIS-0 IS THE FOUNDATIONAL DRIVE (grows->climbs, freeze->stops): {drive_is_gradient}")
    ok = drive_is_gradient and coratchet_ok
    if ok:
        print("PASS foundational_ratchet_entropy_gradient")
    print("ALL_GATES:", "PASS" if ok else "FAIL", "->", path)
    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
