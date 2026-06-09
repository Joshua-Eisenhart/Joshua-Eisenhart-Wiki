---
title: Engine 64 Schedule Atlas
created: 2026-04-07
updated: 2026-04-08
type: concept
tags: [system, planning, validation, architecture]
sources:
  - raw/articles/system-v5-reference-docs/ENGINE_64_SCHEDULE_ATLAS.md
  - raw/articles/new-docs/15_stack_authority_and_capability_index.md
  - raw/articles/new-docs/07_model_math_geometry_sim_plan.md
framing: mixed
---

# Engine 64 Schedule Atlas

## Overview
This atlas preserves the schedule-layer claim that the four topology classes, two loop families, and chirality/flux tags combine into a 64-slot control atlas.

## Grammar layer ownership
The governing split keeps three systems separate: IGT owns stage results (WIN/LOSE/win/lose), mixed vs same-sign patterns, and first/second strategy. Jung owns operator pairings (NeTi, FeSi, etc.), loop families (FeTi vs TeFi), and composition order (UP vs DOWN). I Ching owns the 64-schedule slot identity and hexagram-to-microstep mapping. They do not overlap or redefine each other.

## Topology4 and Terrain8
The owner math locks four real topology classes: Se (dissipative radial expansion), Ne (Hamiltonian tangential circulation), Ni (dissipative contraction), Si (commuting Hamiltonian plus invariant subspaces). Terrain8 = Topology4 x Flux2 is a candidate overlay that pairs each topology with an IN/OUT flux orientation. The atlas's eight terrains (Se-in, Ne-in, Ni-in, Si-in, Se-out, Ne-out, Ni-out, Si-out) are chart correlations, not closed theorems.

## 64-layer split
Three interpretations of the 64 slots coexist: (1) live runtime 64 = 2 engines x 8 terrains x 4 operator slots (the executable scaffold); (2) chart atlas 64 = 8 terrains x 8 signed operators (the schedule-index surface); (3) hexagram layer 64 = optional secondary tag family. The chart atlas assigns 16 macro-stage occupancies (starred cells) across the 8x8 grid, with 48 non-starred cells as schedule slots, not runtime claims.

## Invariants
Per engine: 4 terrains, 8 macro-stages (4 outer + 4 inner), 32 microsteps, 2 WIN, 2 LOSE, 2 win, 2 lose, 8 signed operators. Total: 64 microsteps across both engines. Chart-locked macro-stages: 16. Terrain families shared between engines: 4. Chart terrain IDs shared: 0 (Se-in != Se-out).

## Hard non-claims
Type is not flow is not chirality is not precedence. Ax3 is not closed by this atlas. I Ching labels are not ontology. Correlations are not proof. The 8 chart terrains are not a closed Weyl geometry theorem. Runtime step IDs are not schedule-slot IDs. This document is not proof of full 64-state closure.

## Source
Extracted from `raw/articles/system-v5-reference-docs/ENGINE_64_SCHEDULE_ATLAS.md`. See [[terrain-laws-and-loop-geometry]] for the terrain law math, [[formal-constraints-and-geometry]] for the constraint chain, and [[qit-engine-geometry-entropy-bridge]] for the master-table separation.
