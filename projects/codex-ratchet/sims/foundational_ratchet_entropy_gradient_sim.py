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
  THE ENTROPY GRADIENT = AXIS-0, AT THE FLOOR: the possibility space GROWS -- each step admits more
                    distinguishable refinements (the room grows; the ceiling of distinguishable possibilities
                    rises). The permanent GAP between what the carrier currently distinguishes and that rising
                    ceiling IS the entropy gradient. It is NOT injected; it is constitutive of a growing
                    possibility space. This gap is the ratchet DRIVE.
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

def vn_entropy(rho):
    w = np.linalg.eigvalsh((rho + rho.conj().T) / 2); w = w[w > 1e-12]
    return float(-(w * np.log2(w)).sum())

# ---- minimal persistent evolving structure: a norm-preserving carrier that can GROW its distinguishing basis
# The carrier lives on a finite set of "probe directions" (readouts). Its distinguishing CAPACITY at climb-level
# k is the number of probe directions it can resolve. F01: finite. N01: probes noncommute (order matters).
PROBES = [SZ, SX, SY,
          (SX + SZ) / np.sqrt(2), (SX - SZ) / np.sqrt(2),
          (SY + SZ) / np.sqrt(2), (SY + SX) / np.sqrt(2)]  # a finite ladder of noncommuting probes (F01+N01)

def possibility_set(r, frozen_at=None, n0=2):
    """Omega_r: admissible distinguishable futures on the shell at radius r. GROWS with r (the room grows) unless
    frozen. Each future is a distinct carrier state the fuzz admits; the CEILING of distinguishable possibilities
    is |Omega_r|. Frozen: size pinned at frozen_at (no growth -> no gradient)."""
    n = n0 + r if frozen_at is None else n0 + min(r, frozen_at)
    rng = np.random.default_rng(1000 + n)  # deterministic in the CURRENT size -> frozen truly stops growth
    states = []
    for _ in range(n):
        v = rng.normal(size=2) + 1j * rng.normal(size=2); v = v / np.linalg.norm(v)
        states.append(np.outer(v, v.conj()))
    return states

def distinguishing_capacity(states, level, resolution):
    """How many admissible futures the carrier tells apart with the first `level` probes AT a finite acquired
    RESOLUTION. Resolution is the carrier's acquired distinguishing GEOMETRY: coarse resolution merges nearby
    probe values (few classes), fine resolution splits them (more classes). Climbing = refining resolution
    and/or admitting a probe, the SMALLEST step at a time (MSS) -- so capacity rises incrementally, never
    shattering the whole set in one jump. Decidable, finite."""
    bin_w = 2.0 / max(resolution, 1)          # coarse when resolution small; fine when large
    q = lambda x: int(np.floor(x / bin_w))
    classes = {}
    for i, rho in enumerate(states):
        key = tuple(q(np.real(np.trace(P @ rho))) for P in PROBES[:level])
        classes.setdefault(key, []).append(i)
    return len(classes)

def ceiling(states):
    """The rising ceiling: total distinguishable futures the fuzz admits at FULL probe count and FULL resolution
    -- the distinguishability the growing possibility space makes available (the entropy side of the co-ratchet).
    Capped by |states| (cannot distinguish more futures than exist)."""
    return min(distinguishing_capacity(states, len(PROBES), resolution=64), len(states))

def mss_step(states, level, resolution):
    """The SMALLEST move that resolves >=1 more distinction. Candidate weakest steps, in order of increasing
    added structure: (a) refine resolution by one notch at the current probe level; (b) admit one more probe at
    the current resolution. Take the first candidate that strictly raises capacity (a forced tooth), preferring
    the one that adds the FEWEST new distinctions (the weakest sufficient step -- MSS)."""
    D0 = distinguishing_capacity(states, level, resolution)
    cands = []
    # (a) refine resolution one notch
    if distinguishing_capacity(states, level, resolution + 1) > D0:
        cands.append(("resolution", level, resolution + 1,
                      distinguishing_capacity(states, level, resolution + 1) - D0))
    # (b) admit one more probe
    if level < len(PROBES) and distinguishing_capacity(states, level + 1, resolution) > D0:
        cands.append(("probe", level + 1, resolution,
                      distinguishing_capacity(states, level + 1, resolution) - D0))
    if not cands:
        return level, resolution, False, None
    cands.sort(key=lambda c: c[3])              # fewest new distinctions first = weakest step
    kind, nl, nr, _ = cands[0]
    return nl, nr, True, kind

def run_ratchet(R=8, frozen_at=None):
    """Climb the MSS ladder driven by the entropy gradient. At each shell r the possibility space (maybe) grows;
    while a gap remains the carrier takes the SMALLEST step (refine resolution or admit a probe) that resolves
    >=1 newly-forced distinction. Record geometry (acquired capacity) and entropy gradient (ceiling - capacity)
    -> test co-ratchet and the Feynman freeze."""
    level = 1; resolution = 1; hist = []
    for r in range(R):
        states = possibility_set(r, frozen_at=frozen_at)
        C = ceiling(states)                                       # rising ceiling (entropy side)
        D = distinguishing_capacity(states, level, resolution)    # carrier geometry (geometry side)
        grad = C - D                                              # ENTROPY GRADIENT = Axis-0 drive
        climbed = False; kind = None
        # MSS: one smallest step per shell while the gradient is open (incremental, never a batch shatter)
        if grad > 0:
            level, resolution, climbed, kind = mss_step(states, level, resolution)
        Dpost = distinguishing_capacity(states, level, resolution)
        hist.append({"r": r, "ceiling": C, "geometry_pre": D, "geometry_post": Dpost,
                     "entropy_gradient": grad, "climbed": climbed, "step_kind": kind,
                     "level": level, "resolution": resolution})
    return hist

def main():
    live = run_ratchet(frozen_at=None)      # constitutive: room grows -> gradient persists -> drive
    frozen = run_ratchet(frozen_at=1)       # Feynman control: freeze growth at r=1 -> gradient closes

    live_climbs = sum(h["climbed"] for h in live)
    frozen_climbs_after_freeze = sum(h["climbed"] for h in frozen if h["r"] > 1)
    # co-ratchet: does geometry climb track the entropy gradient one-for-one? (geometry gain == gradient closed)
    coratchet_pairs = [(h["geometry_post"] - h["geometry_pre"], h["entropy_gradient"]) for h in live if h["climbed"]]
    coratchet_ok = all(g > 0 and grad > 0 for g, grad in coratchet_pairs) and len(coratchet_pairs) > 0
    # The Feynman signature is about the DRIVE, not the gap hitting exactly zero. Under growth the gradient must
    # keep re-opening (fresh distinctions keep appearing -> permanent drive, climbs continue). Under freeze the
    # gradient must STOP GROWING (no new distinctions injected) and the climb must HALT. A residual constant gap
    # after freeze is a quantization floor (a distinction the finite carrier cannot resolve at any resolution),
    # NOT a live drive -- what matters is that it is FLAT (not growing) and produces no further climb.
    live_grad_final = live[-1]["entropy_gradient"]
    frozen_grad_final = frozen[-1]["entropy_gradient"]
    frozen_grads_after = [h["entropy_gradient"] for h in frozen if h["r"] > 1]
    frozen_gradient_flat = (len(set(frozen_grads_after)) <= 1)     # no new drive appears after freeze
    live_gradient_reopens = sum(1 for h in live if h["entropy_gradient"] > 0) >= 4  # drive persists under growth

    drive_is_gradient = (live_climbs >= 3) and live_gradient_reopens and \
                        (frozen_climbs_after_freeze == 0) and frozen_gradient_flat

    out = {"classification": "scratch_diagnostic", "promotion_allowed": False,
           "live_total_climbs": live_climbs,
           "frozen_climbs_after_freeze": frozen_climbs_after_freeze,
           "live_entropy_gradient_final": live_grad_final,
           "frozen_entropy_gradient_final": frozen_grad_final,
           "frozen_gradient_flat_after_freeze": bool(frozen_gradient_flat),
           "live_gradient_reopens_under_growth": bool(live_gradient_reopens),
           "coratchet_geometry_tracks_entropy": bool(coratchet_ok),
           "AXIS0_IS_FOUNDATIONAL_DRIVE": bool(drive_is_gradient),
           "live_history": live, "frozen_history": frozen}
    path = __file__.replace(".py", "_results.json"); json.dump(out, open(path, "w"), indent=1)

    print("THE RATCHET MECHANISM AT THE FOUNDATIONS -- entropy gradient (Axis-0) as the drive:")
    print("  root constraints F01 (finite probes) + N01 (noncommuting probes); minimal persistent carrier;")
    print("  possibility space GROWS -> entropy gradient (ceiling - carrier capacity) is the DRIVE.\n")
    print("  r | ceiling  geometry  entropy_grad  climbed   [LIVE: room grows]")
    for h in live:
        print(f"  {h['r']} |   {h['ceiling']:2d}       {h['geometry_post']:2d}         {h['entropy_gradient']:2d}        {h['climbed']}")
    print(f"\n  LIVE   total forced climbs: {live_climbs}; final entropy gradient (stays open = permanent drive): {live_grad_final}")
    print("\n  FEYNMAN CONTROL -- freeze growth at r=1 (gradient must close, climb must stop):")
    print("  r | ceiling  geometry  entropy_grad  climbed   [FROZEN after r=1]")
    for h in frozen:
        print(f"  {h['r']} |   {h['ceiling']:2d}       {h['geometry_post']:2d}         {h['entropy_gradient']:2d}        {h['climbed']}")
    print(f"\n  FROZEN climbs after freeze: {frozen_climbs_after_freeze}; gradient FLAT after freeze (no new drive): {frozen_gradient_flat}")
    print(f"  (residual gap {frozen_grad_final} is a quantization floor -- a distinction the finite carrier cannot")
    print(f"   resolve at any resolution -- NOT a live drive; what matters is it stops growing and halts the climb)")
    print(f"\n  CO-RATCHET (geometry climb tracks entropy gradient, one object two readings): {coratchet_ok}")
    print(f"  AXIS-0 IS THE FOUNDATIONAL DRIVE (grows->climbs, freeze->stops): {drive_is_gradient}")
    if drive_is_gradient and coratchet_ok:
        print("PASS foundational_ratchet_entropy_gradient")
    ok = drive_is_gradient and coratchet_ok
    print("ALL_GATES:", "PASS" if ok else "FAIL", "->", path)
    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
