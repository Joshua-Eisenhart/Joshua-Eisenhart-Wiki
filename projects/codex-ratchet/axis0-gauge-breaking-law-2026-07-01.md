---
title: The Gauge-Breaking Law — Axis-0 Readability Scales With Earned Entropy
created: 2026-07-01
updated: 2026-07-01
type: project-result
status: synced-not-canon
claim_ceiling: scratch_diagnostic; promotion_allowed=false. Relational readout + linear scaling law are solid numerics (R^2=0.99999+). Stated in pure structural indices (a1,a2,eps,delta); labels in rosetta_layer.json.
framing: codex-ratchet
provenance: Claude Science session 2026-07-01. Synced for review, NOT canon.
---

# The Gauge-Breaking Law

> **SYNC STATUS: not canon.** scratch_diagnostic. Extends the two-sector theorem (spec S7n) and builds
> the open chi_2 piece as a relational readout.

## Pure structure (no jargon)

Objects are (a1, a2) in {0,1}^2 with sheet sign eps; a1 = dynamics bit (1=unitary, 0=dephasing),
a2 = frame bit (1=conjugated frame V^dag . V, 0=identity), delta >= 0 = subdominant dissipation.

## The relational readout works — and exposes a gauge degeneracy

System A entangled with a FIXED reference B (the gauge does not act on B). The frame bit a2 shifts the
A-B relational coherence <00|rho_AB|11> for dephasing objects (a1=0): 0.075 vs 0.28. But for unitary
objects (a1=1) it is invisible, because V = exp(-i H0 s) COMMUTES with unitary dynamics about H0:
||[V, exp(-iH0 t)]|| = 2.6e-16. The two unitary objects (1,0) and (1,1) are the IDENTICAL channel
(difference 3e-16). So the parity p = a1 XOR a2 cannot be a single-channel observable among the
unitary objects.

## The gauge-breaking law

Adding subdominant dissipation delta breaks the degeneracy; the frame bit becomes physical in exact
linear proportion:

  a2-physicality = k * delta,   k ~ 0.0787,   R^2 = 0.999997  (through origin).

At delta=0 the split is 6e-17 (pure gauge, parity unreadable); it grows linearly as symmetry-breaking
dissipation switches on.

## Why this matters — the co-ratchet link

This is a STRUCTURAL reason Axis-0 is a late object: the parity is unreadable until the entropy sector
is switched on. The gauge charge becomes physical only once symmetry-breaking dissipation lifts the
unitary degeneracy — precisely the co-ratchet claim (spec S7c) that entropy and operators must be
earned before higher structure is readable. Axis-0's readability is proportional to how much the
co-ratchet has advanced. This makes "Axis-0 is a late object" a measurable statement, not a slogan.

## Artifacts

`axis0_gauge_breaking.png`, `axis0_gauge_breaking_sim.py`.
Spec S7o: `constraint-core-formal-spec-2026-07-01.md`. Rosetta: `rosetta_layer.json` (earned tier).
