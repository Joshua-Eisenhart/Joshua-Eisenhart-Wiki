---
title: The Eight-of-Sixteen Access Law (Engine Type as Weyl Chirality)
created: 2026-07-01
updated: 2026-07-01
type: project-result
status: synced-not-canon
claim_ceiling: scratch_diagnostic; promotion_allowed=false. 8/8 partition exact + pole-mirrored; engine type = global sign of loop geometric phase; access violation flips 8/8. Structural indices only; rosetta names in rosetta_layer.json.
framing: codex-ratchet
provenance: Claude Science session 2026-07-01. Synced for review, NOT canon.
---

# The Eight-of-Sixteen Access Law

> **SYNC STATUS: not canon.** scratch_diagnostic. Built on 7r (16 stages). Grounds the owner's
> "each person accesses only 8 of 16 stages" as a dynamical theorem, not a stipulation.

## Grounding

engine-math-reference.md line 55: Type-1 (Left Weyl) = in-terrains {Funnel,Vortex,Pit,Hill} = t0-t3;
Type-2 (Right Weyl) = out-terrains {Cannon,Spiral,Source,Citadel} = t4-t7. Engine types are the two
Weyl chiralities eps=+/-1, sheet Hamiltonians H_L=+H0 and H_R=-H0.

## Three tests (all structural, pure indices)

1. PARTITION EXACT + POLE-MIRRORED. Left accesses t0-t3, Right t4-t7; overlap 0, union all 8.
   Dissipative fixed points pole-mirror: t0 z*=+1 vs t4 z*=-1; t2 z*=-1 vs t6 z*=+1 (each sums 0).
   Out-terrains are pole-flipped images of in-terrains = opposite Weyl handedness (rdot=+/-2 n x r).

2. ENGINE TYPE = GLOBAL SIGN OF LOOP GEOMETRIC PHASE. Signed swept Bloch area (eps-odd geometric
   phase) of each stage's drive loop: all 8 Left stages POSITIVE, all 8 Right stages NEGATIVE. The
   engine type is a single global sign carried by Weyl chirality -- the same handedness as the 720
   spinor sign (7l) and the gauge-breaking readout (7o).

3. ACCESS VIOLATION FLIPS 8/8. Forcing a Left stage onto the Right sheet reverses its geometric-phase
   sign (8 of 8). A stage on the wrong chirality is the MIRROR stage, not the same stage. A person
   locked to one chirality genuinely cannot run the other engine's 8 stages. Within each engine the 8
   stages stay distinct (min 0.15/0.20, mean 2.7).

## Reading

The eight-of-sixteen access law is a structural theorem: engine type is a global geometric-phase sign
(Weyl chirality), the two 8-sets are pole-mirror pairs, cross-engine access flips handedness 8/8. This
closes the stage/engine layer -- the manifold now carries the full 16 = 2 engines x 8 stages structure
with the split earned dynamically. Validation target for the real engines: a Left-engine run gives all
positive loop areas, a Right-engine run all negative.

## Artifacts

`engine_type_access.png`, `engine_type_access.json`, `engine_type_access_sim.py`.
Spec S7s: `constraint-core-formal-spec-2026-07-01.md`. Rosetta: `rosetta_layer.json`.
