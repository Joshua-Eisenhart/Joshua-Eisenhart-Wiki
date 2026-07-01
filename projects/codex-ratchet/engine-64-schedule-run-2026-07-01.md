---
title: Engine 64 Schedule Run — Unique Processing Under N01
created: 2026-07-01
updated: 2026-07-01
type: project-status
status: synced-not-canon
claim_ceiling: finite enumeration with an order-sensitive observable; scratch_diagnostic; promotion_allowed=false; formal_admission_allowed=false. Earns 'unique processing under N01' and 'closed-form layer precision' only — NOT full 64-state runtime-visitation closure, NOT Axis0/flux/bridge admission.
framing: codex-ratchet
sources:
  - system_v5/READ ONLY Reference Docs/ENGINE_64_SCHEDULE_ATLAS.md
  - system_v5/ops/QIT_ENGINE_FOUR_OPERATOR_SIGNED_MATH_20260522.md
  - concepts/engine-64-schedule-atlas.md
  - concepts/igt-axes-terrain-source-extraction-2026-06-04.md (eng_64 degeneracy: 64 stages, 16 distinct)
provenance: Claude Science formalization session 2026-07-01; synced for review, NOT admitted as canon.
---

# Engine 64 Schedule Run — Unique Processing Under N01

> **SYNC STATUS: not canon.** `scratch_diagnostic`, `promotion_allowed=false`.

## The runtime object

`64 = 2 engines (L/R) x 8 terrains (4 topology x 2 flux) x 4 judging operators`.

The four judging operators are exact quantum channels on `M_2(C)`, verified CPTP with correct fixed algebra:

- `Ti` = z-basis pinching (cond. expectation onto `A_z=span(I,sigma_z)`) — unital CPTP dephasing.
- `Te` = x-basis pinching (onto `A_x`) — unital CPTP dephasing.
- `Fi` = inner automorphism by `sigma_x` (SU(2) x-rotation) — reversible unitary, purity-preserving.
- `Fe` = inner automorphism by `sigma_z` (SU(2) z-rotation) — reversible unitary, purity-preserving.

`up` = operator-first `Phi_JP = T_P o J`; `down` = terrain-first `Phi_PJ = J o T_P` (the Axis-6 / N01 precedence).
`SiTe` = `Te^down` = gradient descent; `Te^up` = gradient ascent.

## Result: unique processing is an N01 property of the observable

| Readout | Distinct microsteps / 64 |
|---|---|
| order-blind, coarse (single seed, symmetrized up/down) | **11 / 64** — reproduces documented eng_64 collapse |
| N01 order-sensitive (terrain-first, multi-seed) | **64 / 64** — full uniqueness |

All 64 microsteps carry a real up != down order gap (mean 0.544). Uniqueness comes
from reading an **order-sensitive** observable, NOT from adding terrains/operators. This is why prior
order-blind sims collapsed 64 -> 16.

## Deep-ratchet layer precision

Deepest geometric layer (L4 transport/holonomy) locked to closed form `-2*pi*cos(2*eta)`:
independent recomputation `-4.442882938`, residual ~3e-10, converged at 256 steps.

## Artifacts (Claude Science session 2026-07-01)

- `engine_64_schedule.png`, `engine_64_schedule_results.json`, `engine_64_schedule_sim.py`
- Full spec: `constraint-core-formal-spec-2026-07-01.md` §7g (this), §7a-7f (manifold/build/co-ratchet/3-qubit/FEP/atlas).

## Next (gated)

- Full 64-state runtime-visitation dynamics (does an actual engine run visit every slot?), still open per source.
- Lock Se/Ne/Si dissipators so terrain flows have source-locked content on the 3-qubit carrier (Axis-0 blocker).
