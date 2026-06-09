---
title: Battery Index
created: 2026-04-08
updated: 2026-05-21
type: concept
tags: [simulation, validation, audit, system]
sources:
  - raw/articles/new-docs/BATTERY_INDEX.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/BATTERY_INDEX.md
spec_mirrors:
  - /Users/joshuaeisenhart/wiki/specs/codex-ratchet/enforcement-process-rules-current.md
  - /Users/joshuaeisenhart/wiki/specs/codex-ratchet/lego-sim-contract-current.md
  - /Users/joshuaeisenhart/wiki/specs/codex-ratchet/sim-estate-integration-status.md
  - /Users/joshuaeisenhart/wiki/specs/codex-ratchet/formal-scout-readiness-status.md
framing: historical_battery_snapshot
---

# Battery Index

Historical index of the April negative-battery surface. The source page reported 38 batteries covering 2152+ distinct failure-mode evaluations across L0-L7.

Status boundary: this page preserves an April battery catalogue. It is not live validator authority and does not promote any sim or result. For current process/status, use [[specs/codex-ratchet/enforcement-process-rules-current|enforcement-process-rules-current]], [[specs/codex-ratchet/lego-sim-contract-current|lego-sim-contract-current]], [[specs/codex-ratchet/sim-estate-integration-status|sim-estate-integration-status]], and [[specs/codex-ratchet/formal-scout-readiness-status|formal-scout-readiness-status]].

## Battery Categories

| Category | Count | Tests |
|----------|-------|-------|
| Graveyard (engine kill) | 5 | 46 |
| Pure math (no engine) | 10 | 107 |
| Cascade / cross-layer | 3 | 143 |
| Engine axiom kills (neg\_\*) | 8 | ~40 |
| Geometry negatives (sim\_neg\_\*) | 6 | ~12 |
| Stage matrix negatives | 5 | ~1,792+ |
| Original engine battery | 1 | 12 |

## Graveyard Batteries

Engine-level kill tests that run the engine with deliberately broken constraints:

1. **Information Graveyard** — 8/8 killed. Classical-only, no-feedback, deterministic, max-mixed, identical-op, proj-only, frozen-basis, anti-ratchet.
2. **Deep Graveyard** — 8/8 killed. CPTP violation, chirality swap, no measurement, no unitary, no spectral projection, force identity, compound locks.
3. **Extended Graveyard** — 6/6 killed. Entropy ordering, triple lock, dual-loop+chirality, scrambled sequence, symmetric ops, maximal decoherence.
4. **Thermodynamic Graveyard** — 8/8 killed. No-cloning, zero H, infinite coupling, pure lock, d=1, no bath, zero temp, reversed entropy.
5. **Entropy Form Negative** — 16 comparisons across 6 entropy alternatives. Confirms von Neumann remains best default.

## Pure Math Batteries

Test failure modes of quantum-information primitives directly, independent of the engine:

- Negative Geometry (10 tests), Density Matrix (12), Topology Graphs (10), Channels (10), Entanglement (10), Compound Failures (10), Entropy Boundaries (10), Boundary Sweep (10), MEGA Boundaries (15), Advanced Legos (10).

## Constraint Cascade Batteries

- **Constraint Cascade** — breaks one constraint at a time, measures propagation through L0-L7.
- **Cross-Layer Propagation** — 13 breaks across L2-L12, maps inter-layer dependencies.
- **Z3 Fence Exhaustive** — 120 tests (15 single + 105 pair removal), proves every fence is necessary.

## Stage Matrix Negatives

Per-stage structural properties across all 64 engine stages using `stage_matrix_neg_lib.py`:
- Missing operator (1024 tests), native-only (256), type flatten (256), Axis 6 shared (896), missing Fe (256).

## Layer Coverage

| Layer | Batteries Touching |
|-------|-------------------|
| L0 | 1-5, 6-7, 9-10, 12-13, 16, 18, 19-22 |
| L1 | 2-5, 9, 11-12, 15, 18 |
| L2 | 1-2, 6, 8, 17 |
| L3 | 2-4, 10, 13, 16, 23-26, 33-35, 37-38 |
| L4 | 2-3, 17, 25-26, 28, 32, 35-36 |
| L5 | 8, 11, 14-15, 17, 29-32 |
| L6 | 27, 36, 38 |
| L7 | 16-17, 27 |

## Related Pages

- [[enforcement-and-process-rules]] — negative testing is mandatory (Rule 6)
- [[specs/codex-ratchet/enforcement-process-rules-current]]
- [[specs/codex-ratchet/lego-sim-contract-current]]
- [[migration-registry]] — per-family negative battery status
- [[falsification-sim-designs]] — falsification protocol design
- [[pytorch-ratchet-build-plan]] — build plan referencing battery coverage
