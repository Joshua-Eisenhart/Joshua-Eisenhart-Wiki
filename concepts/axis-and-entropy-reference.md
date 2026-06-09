---
title: Axis And Entropy Reference
created: 2026-04-07
updated: 2026-05-21
type: summary
tags: [reference, research, validation]
sources:
  - raw/articles/new-docs/AXIS_AND_ENTROPY_REFERENCE.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/SIM_ESTATE_INTEGRATION_INDEX.md
framing: mixed
---

# Axis And Entropy Reference

## Overview
Verbatim extraction of the 7-axis stack, terrain table, token partition, loop rules, 64-schedule grid, three-layer entropy architecture, and the Axis 0 working formalization. This is the reference card for what the axes actually do mathematically.

## Current v5 status note
This page is a static mathematical reference, not live status. For current evidence and validator state, read [[specs/codex-ratchet/sim-estate-integration-status]], [[specs/codex-ratchet/formal-scout-readiness-status]], and [[axis0-current-doctrine-state-card]].

Current v5 keeps Axis0 `open_partial`; admitted candidates and blocked candidates are tracked in the sim-estate index, and `promotion_allowed=false` still fences formal-scout rows.

## Honesty Boundary

7 active axes (0-6). Axes 7-12 are planned later mirror layer. Jung, IGT, trigram, hexagram, yin-yang, I-Ching labels are CORRELATION LAYERS, not primary mathematics. Axis 0 is still open at bridge-and-cut level.

## Role in the live wiki cluster
- **Strongest use**: verbatim mathematical reference for the 7-axis stack, terrain table, and entropy definitions.
- **Weakest use**: current operational status (use the Doctrine State Card plus current v5 sim/readiness routers) or reasoning/governance.
- **Authority boundary**: static mathematical reference.

## Recommended reading order
1. [[hermes-current/read-first|read-first]]
2. [[axis-and-entropy-reference]] (this page, for technical definitions)
3. [[axis0-current-doctrine-state-card]]
4. [[qit-engine-doctrine]]

## Global Axis Table

| Axis | Math role | Status |
|---|---|---|
| 0 | entropy drive, cut-state functional | active, open |
| 1 | derived terrain branch split (Se/Ni vs Ne/Si) | active, derived |
| 2 | direct vs conjugated frame | active |
| 3 | fiber vs lifted-base loop | UNRESOLVED |
| 4 | loop-order family (UEUE vs EUEU) | active, derived |
| 5 | operator family (dephasing vs rotation) | active |
| 6 | precedence order (operator-first vs terrain-first) | active, derived |

## Eight Terrain Table

Eight terrains = 4 topologies (Se, Ne, Ni, Si) times 2 loops (fiber, base). Fiber loops are density-stationary (rho constant). Base loops are density-traversing (rho varies). Each terrain has a direct or conjugated frame assignment.

## Signed Judging Variants

Eight variants: Ti up/down, Fe up/down, Te up/down, Fi up/down. "Up" = operator first. "Down" = terrain first. Tokens like TiSe, SeTi, etc. encode the operator-terrain pair and order.

## Three-Layer Entropy Architecture

| Layer | Object | Role |
|---|---|---|
| Runtime engine | S(rho_L), S(rho_R) | per-sheet entropy during operation |
| Torus seat | torus latitude eta to entropy | geometry-level entropy |
| Bipartite Ax0 | S(A|B), I(A:B), I_c(A>B) on rho_AB | the actual Axis 0 family |

Sign structure: S(rho) >= 0 unsigned; I(A:B) >= 0 unsigned; S(A|B) can be negative (signed cut entropy); I_c(A>B) can be negative (signed primitive correlation).

## Axis 0 Working Formalization (NOT CANON)
Eight sections from "Axis 0 rough and drifty": primitive theses (entropic monism, identity not primitive, time not primitive), constraint-first basis, shell/boundary bookkeeping, j/k fuzz as admissible future, Feynman-like path form, entanglement tensor-network shell, ring checkerboard as finite support, entropy field and i-scalar.

## JK fuzz and i-scalar cluster
The wiki had previously under-mapped this cluster. In the Axis-0 document family, `j/k` fuzz and the `i`-scalar are not stray side terms; they are part of the owner Axis-0 packet itself. `JK fuzz` names admissible future/refinement multiplicity and path-history ensemble structure on shell support. The `i`-scalar is the open shell-order / universal-clock candidate on that same support. See [[jk-fuzz-field]] and [[i-scalar-and-axis-0-genealogy]].

2026-06-05 refinement: route `JK fuzz` as a finite, growable entanglement-information support, not as primitive causality. At any witness it must be finite; across refinement it may gain shells, cuts, history windows, or probe resolution. The Axis-0-compatible readout is only available after a bridge builds a cut state such as `rho_AB`, where coherent information `I_c(A>B) = -S(A|B)` or companion entanglement witnesses can be evaluated. This keeps the three-layer entropy architecture intact: runtime sheet entropy, torus-seat entropy, and bipartite Axis-0 cut entropy are related candidates, not one collapsed scalar.

## Entropic Monism Clarification

Entropic monism = doctrine name. Constraint on distinguishability = actual primitive claim. Entropy = a later admissible measure of distinguishability under constraint. Entropic monism does NOT mean "entropy is primitive."

## How it connects
This axis stack feeds into [[constraint-surface-and-process]] at the resolution levels and into [[qit-engine-geometry-entropy-bridge]] at the live-engine layer. See [[entropy-sweep-protocol]] for how each entropy family gets tested and promoted.

## Open questions
- Axis 0 final bridge Xi, final cut A|B, exact shell/hist unification are still open.
- Axis 3 is UNRESOLVED: chirality/flux vs outer/inner, do not close.
- Why the 64-step engine cycle is the right granularity is a pending check.
