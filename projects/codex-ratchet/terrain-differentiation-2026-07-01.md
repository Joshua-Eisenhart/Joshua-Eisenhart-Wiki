---
title: Maximal Differentiation of the Eight Terrains
created: 2026-07-01
updated: 2026-07-01
type: project-result
status: synced-not-canon
claim_ceiling: scratch_diagnostic; promotion_allowed=false. Exact source-locked GKSL generators; 14-feature fingerprint; all 8 distinct. Pure structural indices (t0..t7); names in rosetta_layer.json.
framing: codex-ratchet
sources:
  - concepts/igt-pattern-explicit-math-reference.md (exact terrain Bloch maps, lines 486-497)
provenance: Claude Science session 2026-07-01. Synced for review, NOT canon.
---

# Maximal Differentiation of the Eight Terrains

> **SYNC STATUS: not canon.** scratch_diagnostic. Strong per-terrain sim on the geometric constraint
> manifold, structural indices only.

## Setup

Each terrain (t0..t7) is its EXACT source-locked GKSL generator on C^2 (scratch Bloch maps,
igt-pattern lines 486-497). Goal: maximal differentiation — every terrain provably distinct in
information processing. No labels in the math; rosetta names below.

## A single fixed point is not enough

From maximally-mixed start, the 4 dissipative terrains pin to their exact z* poles (t0->+0.78,
t2->-0.91, t4->-0.78, t6->+0.91). The 4 unitary-dominant terrains all collapse to r=0 (degenerate).
Differentiation needs a rich dynamical fingerprint.

## The 14-feature fingerprint

Fixed-point Bloch (3) + radius + fixed-point entropy + Liouvillian decay rates (2) + oscillation +
total dissipativity + signed drift + trajectory arclen + signed chirality + trajectory handedness +
signed swept area (eps-odd geometric-phase proxy). The last three see the sheet sign eps, which
scalar invariants cannot (unitary terrains are mirror trajectories with identical spectra).

## Result

All 8 terrains DISTINCT. Standardized pairwise distances: mean 5.5, max 6.9, min 0.35.
Degeneracies break in order: fixed point (6) -> Liouvillian spectrum -> chirality (t1!=t5) ->
handedness + swept area (t3<->t7: 0.28 -> 0.35).

The bottleneck pair t3-t7 (Hill/Citadel, the two projective Si terrains) is a GENUINE structural
fact: their generator is nearly SHEET-SYMMETRIC, so only eps-odd geometric features distinguish them.
Every other pair is 3-7 apart.

## Use

When the real Julia/JAX/PyTorch engines run, this fingerprint is the natural per-terrain validation
target: each engine stage must reproduce its terrain's fingerprint row.

## Rosetta names

t0=Funnel(Se-in), t1=Vortex(Ne-in), t2=Pit(Ni-in), t3=Hill(Si-in), t4=Cannon(Se-out),
t5=Spiral(Ne-out), t6=Source(Ni-out), t7=Citadel(Si-out). Bottleneck = Hill/Citadel (both Si).

## Artifacts

`terrain_differentiation.png`, `terrain_fingerprints.json`, `terrain_differentiation_sim.py`.
Spec S7p: `constraint-core-formal-spec-2026-07-01.md`. Rosetta: `rosetta_layer.json`.
