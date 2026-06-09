---
title: Geometry Ingredient Map
created: 2026-04-09
updated: 2026-05-21
type: concept
tags: [geometry, reference, system, topology]
sources:
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/07_model_math_geometry_sim_plan.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/08_aligned_sim_backlog_and_build_order.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/16_lego_build_catalog.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/17_actual_lego_registry.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/plans/plans/sim_backlog_matrix.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/plans/plans/sim_truth_audit.md
framing: geometry_inventory_snapshot
spec_mirrors:
  - specs/codex-ratchet/process-contract-mirror-index
  - specs/codex-ratchet/llm-controller-contract-current
  - specs/codex-ratchet/enforcement-process-rules-current
  - specs/codex-ratchet/lego-sim-contract-current
  - specs/codex-ratchet/formal-scout-readiness-status
  - specs/codex-ratchet/sim-estate-integration-status
  - specs/codex-ratchet/tool-function-receipt-status
---

# Geometry Ingredient Map

The actual geometric ingredients that appear in the system's sims and constraint structure. Not a textbook survey — this is a dated working inventory of what was routed through the repo's geometry-manifold lane in the cited sources.

Planning note: this page mixes admitted/current/partial/open ingredients for navigation. It is not itself a public truth-label surface or repo-canonical status page. Use [[geometry-manifold-parity-audit]], [[current-geometry-spine-status]], and the spec mirrors when you need queue/truth-aligned status language.

## Carrier Geometry

| Ingredient | Role | Wiki page | Key results |
|---|---|---|---|
| Density matrices | Primary admissible objects | [[density-matrix-mathematics]] | pure_lego_density_matrices, phase7_baseline_validation |
| Bloch / Pauli / Stokes | Parameterization of single-qubit states | [[density-matrix-mathematics]] | stokes_parameterization_results (sim only) |
| Weyl spinors | Chiral carriers on Hopf tori | [[clifford-algebra-qit]], [[hopf-fibration-mathematics]] | weyl_hopf_tori, weyl_spinor_hopf, dual_weyl |
| Clifford algebra Cl(3)/Cl(6) | Geometric product, rotation, spinor transport | [[clifford-algebra-qit]] | pure_lego_clifford_algebra, clifford_generator_basis, q2_clifford_structure |
| Hopf fibration S³→S² | Fiber bundle behind qubit carrier | [[hopf-fibration-mathematics]], [[fiber-bundles-and-spin-geometry]] | hopf_torus_lego, density_hopf_geometry, pure_geometry_hopf_tori |
| Nested/Clifford/Hopf tori | Compound carrier geometry | [[hopf-fibration-mathematics]] | nested_torus_geometry (sim), full_torus_spinor_dynamics |
| Fubini-Study / Bures / QFI | Metrics on state space | [[quantum-geometry-fubini-study]], [[distance-metrics-state-space]], [[quantum-fisher-information-geometry]] | fubini_study_geometry, bures_geometry, pure_lego_qfi_wy_qgt |
| Contact / symplectic / Kähler | Phase space and geometric structure | [[contact-structure-s3]], [[g-structure-tower]], [[sasakian-s3-prequantum-bundle]] | contact_structure_s3 (result), pure_lego_symplectic_kahler_weyl |
| Wigner / Husimi | Quasiprobability representations | [[quantum-computing-applications]] (partial) | lego_weyl_wigner_phase_space, husimi_phase_space_representation |
| Channels / Kraus / Choi | CPTP maps on carrier | [[cptp-maps-and-channels]] | pure_lego_channels_choi_lindblad |

## Constraint Geometry

| Ingredient | Role | Wiki page |
|---|---|---|
| Root constraints F01 + N01 | Finitude + noncommutation | [[constraint-surface-and-process]] |
| Nested shells S0⊃S1⊃... | Simultaneous constraint surfaces | [[pytorch-ratchet-build-plan]] |
| M(C) constraint manifold | Admissible state space | [[constraint-surface-and-process]], [[axes-0-6-and-constraint-manifold-explicit-atlas]] |
| L0-L7 cascade | Progressive constraint application | [[pytorch-ratchet-build-plan]], [[migration-registry]] |
| Kill points (L4, L6) | Structural elimination | [[pytorch-ratchet-build-plan]] |

## Bridge Geometry

| Ingredient | Role | Wiki page | Status |
|---|---|---|---|
| rho_AB (bipartite) | Composite system state | [[entanglement-theory]] | OPEN |
| Xi (bridge object) | Chiral bridge between shells | [[qit-engine-geometry-entropy-bridge]] | OPEN |
| Phi0 (seam quantity) | Cut-state transition | [[qit-engine-geometry-entropy-bridge]] | OPEN (embargoed) |
| Axis 0 (gradient field) | ∇_η I_c on shell parameters | [[pytorch-ratchet-build-plan]] | OPEN |

## Missing Current-Doc Pages (geometry frontier)

These ingredients appear in sims/results but lack dedicated wiki pages:

- **Levi-Civita connection** — affine connection on state space (result: riemannian_curvature_results)
- **Riemannian curvature** — Riemann tensor on carrier (result: riemannian_curvature_results)
- **Geodesic exp/log** — exponential map on shell geometry
- **Geodesic deviation** — Jacobi fields, tidal forces on state space
- **Gauss-Bonnet on CP¹** — topological invariant of qubit carrier
- **Contact structure S³** — contact form on Hopf total space (result: contact_structure_s3_results)
- **Hopf/contact/symplectic bridge** — relation between three structures on S³
- **QFI kill-point behavior** — where QFI diverges at cascade transitions (result: qfi_killpoint_divergence_results)

## Queue pressure now

The cited backlog snapshot still puts the main geometry pressure on:
- explicit Hopf-map audit
- fiber-equivalence / loop-law audit
- connection / holonomy / transport consolidation
- nested-torus separation from generic torus geometry
- Weyl/chiral bookkeeping
- explicit Pauli-on-Weyl packet
- stronger cell-complex and persistence packet

So this page should not be read as saying the geometry lane is complete just because the ingredient list is rich.

## Related Pages

- [[pytorch-ratchet-build-plan]] — build plan these ingredients feed
- [[qit-engine-geometry-entropy-bridge]] — bridge geometry
- [[density-matrix-mathematics]] — primary carrier object
- [[hopf-fibration-mathematics]] — fiber bundle carrier
- [[clifford-algebra-qit]] — geometric algebra
- [[quantum-geometry-fubini-study]] — state space metrics
- [[probe-doc-result-map]] — mapping this to actual sims/results
- [[current-geometry-spine-status]] — current queue-facing geometry summary
- [[geometry-manifold-parity-audit]] — parity check between wiki geometry summaries and repo authority surfaces
