---
title: Axis 0 1 2 QIT Packet
created: 2026-04-07
updated: 2026-04-08
type: concept
framing: source_snapshot
tags: [simulation, validation, system, architecture]
sources:
  - raw/articles/system-v5-reference-docs/AXIS_0_1_2_QIT_MATH.md
  - raw/articles/new-docs/CONSTRAINT_ON_DISTINGUISHABILITY_FULL_MATH.md
  - raw/articles/new-docs/AXIS_AND_ENTROPY_REFERENCE.md
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Axis 0 1 2 QIT Packet

## Current boundary
This is a source-packet snapshot, not a live v5 status card. Use current repo receipts and the spec mirrors before treating any axis, bridge, or carrier statement here as promoted.

## Overview
This packet records the working lock for Axes 0–2: the shared carrier objects, the geometry spine, and the source-locked split between direct and conjugated kernel forms.

## Geometry spine
The build order is: constraints -> M(C) (admissible configuration space) -> geometry on M(C) (coordinate-free compatibility structure) -> axis slices A_i: M(C) -> V_i. The concrete realization uses H = C^2 with left/right Weyl sheets on S^3, paired carrier-density objects, and a realization map from the concrete geometry into the canon constraint manifold. The carrier geometry is source-tight in the packet: Hopf chart, torus strata, Hopf connection, fiber/base loop split, and horizontal condition are cited as executable by `sim_L0_s3_valid.py`.

## Axis 0 requires a cut-state bridge
Axis 0 cannot be evaluated on a single isolated spinor; it needs a bipartite cut-state rho_AB. The bridge family Xi maps geometry or history windows into rho_AB. The source packet names three bridge surfaces: pointwise pullback (x -> rho(x) -> Phi_0(rho(x))), shell-cut pullback (weighted sum of coherent information over shell cuts), and history-window pullback (time-averaged integral over trajectory). The strongest simple kernel candidate is Phi_0(rho_AB) = -S(A|B)_rho = I_c(A>B)_rho (coherent information). The pointwise product pullback remains MI-trivial in the cited Hopf probe, while richer direct-cut variants and history-window constructions were being separated in source-reported Axis-0 bridge bakeoffs; current status must be checked in the spec mirrors and live repo receipts.

## Axis 1 and Axis 2
Axis 1 is the unitary-vs-CPTP split (coherent vs dissipative dynamics). Axis 2 is the direct-vs-conjugated representation split (expansion vs compression). These are source-locked at the semantic class-split level, though the reduced Axis 1 x Axis 2 terrain join is still being tightened.

## Discrete Axis 0 projection
The discrete projection of Axis 0 maps {Ne, Ni} -> N/white and {Se, Si} -> S/black, corresponding to the N/S polarity in the terrain address lattice.

## Executable evidence
The geometry spine is not just diagrammatic in the source packet: `sim_L0_s3_valid.py` is cited for S^3, SU(2), Hopf map, fiber preservation, Berry phase, torus coordinates, and Bloch round-trip numerics. `test_engine_dual_loop_grammar.py` is cited for engine state carrying explicit psi_L, psi_R, named nested-torus coordinates, and 32-step cycle execution. `axis0_xi_strict_bakeoff_sim.py` is the strongest cited bridge discriminator in this packet; current v5 status still comes from the live spec/receipt mirrors.

## Source
Extracted from `raw/articles/system-v5-reference-docs/AXIS_0_1_2_QIT_MATH.md`. See [[formal-constraints-and-geometry]] for the constraint layer, [[qit-engine-geometry-entropy-bridge]] for the master table, and [[axis-and-entropy-reference]] for the full axis stack.
