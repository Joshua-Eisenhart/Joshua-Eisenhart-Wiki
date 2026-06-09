---
title: Aligned Sim Backlog And Build Order
created: 2026-04-07
updated: 2026-04-08
type: summary
framing: current
tags: [reference, research, planning]
sources:
  - raw/articles/new-docs/08_aligned_sim_backlog_and_build_order.md
---

# Aligned Sim Backlog and Build Order

## Overview
Next-step bridge from the newly tested L0 building blocks to the rest of the system. Not a theory doc — a build-order doc for what should be simulated next, in the right alignment.

## What the L0 Work Established

- state representations at L0 compared directly (purification ranked highest, coherence vector best d=4 bridge, eigenvalues weak)
- geometry families at L0 compared directly (trace distance, Bures, Fubini-Study, QFI, QGT survived; HS-alone too flat; relative entropy not metric)
- 161-family math inventory catalogued

## L0 Collapse Classes

| Class | Members |
|---|---|
| State representation | density matrix, Bloch/coherence vector, purification, eigenvalue/spectrum, Stokes |
| Geometry/metric | trace distance, Bures, Fubini-Study, QFI/QGT, Berry/holonomy |
| Correlation/entropy | MI, conditional entropy, coherent information, vN, Rényi/Tsallis/min/max, concurrence/negativity |
| Algebra/dynamics | Pauli, Clifford, CPTP maps, channels, commutators, left/right action asymmetry |
| Decomposition/compression | SVD, Schmidt, principal-subspace truncation, low-rank approximation |

## Build Order After L0

| Layer | What to test |
|---|---|
| L1 | carrier and probe admissibility |
| L2 | geometry survivability on same carrier |
| L3 | operator family discrimination |
| L4 | bipartite structure and correlation |
| L5 | entropy family sweep |
| L6 | axis tests only after admission |

## Negative Controls That Must Stay in Every Batch

- carrier flattening
- spectrum-only blindness
- commutative collapse
- real-only collapse
- flat-geometry-only collapse
- entropy assumption lock-in
- diagnostic-only substitution for real evidence

## Promotion Rule

A family is canon only if it survives: base carrier, geometry layer, operator layer, negative suite, and remains distinct under probe changes when it should.

## How it connects
This build order follows [[07-model-math-geometry-sim-plan]] and feeds into [[falsification-sim-designs]]. See [[research-inventory-and-foundations]] for the evidence base.

## Open questions
- Whether L1-L6 should be run sequentially or some layers can be parallelized.
