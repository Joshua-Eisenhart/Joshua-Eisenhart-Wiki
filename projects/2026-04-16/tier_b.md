# Tier B — geometry shell-local canonical coverage

Date: 2026-04-17
Status: gate pass
Scope: shell-local coverage only (no pairwise/coexistence/bridge promotion)

Read order used
- `/Users/joshuaeisenhart/Desktop/Codex Ratchet/CLAUDE.md`
- project memory: `project_g_tower_math_backlog.md`
- project memory: `feedback_constraint_manifold_simultaneous.md`

Operating fence
- shell-local only
- at least one load-bearing tool per canonical sim
- no cross-layer judging-function language below Axis 4
- standard math/object naming only

## Gate result

All 5 Tier B layer families now have canonical shell-local coverage documented below.

## B1 — G-stack / G-tower shell-local coverage

New canonical shell-local sims added and rerun-backed:
- `system_v4/probes/sim_gstack_associated_bundle_shell_local.py`
  - `system_v4/probes/a2_state/sim_results/sim_gstack_associated_bundle_shell_local_results.json`
- `system_v4/probes/sim_gstack_spectral_triple_shell_local.py`
  - `system_v4/probes/a2_state/sim_results/sim_gstack_spectral_triple_shell_local_results.json`
- `system_v4/probes/sim_gstack_gerbe_shell_local.py`
  - `system_v4/probes/a2_state/sim_results/sim_gstack_gerbe_shell_local_results.json`
- `system_v4/probes/sim_gstack_floer_complex_shell_local.py`
  - `system_v4/probes/a2_state/sim_results/sim_gstack_floer_complex_shell_local_results.json`
- `system_v4/probes/sim_gstack_twistor_line_shell_local.py`
  - `system_v4/probes/a2_state/sim_results/sim_gstack_twistor_line_shell_local_results.json`
- `system_v4/probes/sim_gstack_stable_bundle_shell_local.py`
  - `system_v4/probes/a2_state/sim_results/sim_gstack_stable_bundle_shell_local_results.json`
- `system_v4/probes/sim_gstack_higgs_bundle_shell_local.py`
  - `system_v4/probes/a2_state/sim_results/sim_gstack_higgs_bundle_shell_local_results.json`
- `system_v4/probes/sim_gstack_harmonic_bundle_shell_local.py`
  - `system_v4/probes/a2_state/sim_results/sim_gstack_harmonic_bundle_shell_local_results.json`
- `system_v4/probes/sim_gstack_hitchin_fibration_shell_local.py`
  - `system_v4/probes/a2_state/sim_results/sim_gstack_hitchin_fibration_shell_local_results.json`
- `system_v4/probes/sim_gstack_arithmetic_curve_shell_local.py`
  - `system_v4/probes/a2_state/sim_results/sim_gstack_arithmetic_curve_shell_local_results.json`
- `system_v4/probes/sim_gstack_nonabelian_hodge_shell_local.py`
  - `system_v4/probes/a2_state/sim_results/sim_gstack_nonabelian_hodge_shell_local_results.json`

Verification
- fresh reruns completed under Makefile interpreter
- direct py_compile completed on helper + new sims

## B2 — Hopf shell-local coverage

Shell-local owner packets rerun-backed in scope:
- `system_v4/probes/sim_hopf_fibration_constraint_canonical.py`
  - `system_v4/probes/a2_state/sim_results/sim_hopf_fibration_constraint_canonical_results.json`
  - overall_pass: true
- `system_v4/probes/sim_cvc5_hopf_fiber_constraint.py`
  - `system_v4/probes/a2_state/sim_results/sim_cvc5_hopf_fiber_constraint_results.json`
  - overall_pass: true
- `system_v4/probes/sim_hopf_fiber_equivalence.py`
  - `system_v4/probes/a2_state/sim_results/hopf_fiber_equivalence_results.json`
  - all_pass: true
- `system_v4/probes/sim_hopf_foliation_structure.py`
  - `system_v4/probes/a2_state/sim_results/hopf_foliation_structure_results.json`
  - all_pass: true

Note
- `sim_pure_geometry_hopf_tori.py` was kept honest as classical baseline and not promoted.
- shell-local Hopf coverage is carried by the packets above.

## B3 — Weyl shell-local coverage

Touched and rerun-backed owner packets:
- `system_v4/probes/sim_weyl_group_a2_root_system.py`
  - `system_v4/probes/a2_state/sim_results/sim_weyl_group_a2_root_system_results.json`
  - classification: canonical
  - overall_pass: true
- `system_v4/probes/sim_weyl_group_bc2_root_system.py`
  - `system_v4/probes/a2_state/sim_results/sim_weyl_group_bc2_root_system_results.json`
  - classification: canonical
  - overall_pass: true
- `system_v4/probes/sim_weyl_group_g2_shell_local.py`
  - `system_v4/probes/a2_state/sim_results/sim_weyl_group_g2_shell_local_results.json`
  - classification: canonical
  - overall_pass: true
- `system_v4/probes/sim_weyl_nested_shell.py`
  - `system_v4/probes/a2_state/sim_results/weyl_nested_shell_results.json`
  - classification: canonical
  - summary: 15 pass / 0 fail / 0 error
- `system_v4/probes/sim_weyl_geometry_rescaling_shell.py`
  - `system_v4/probes/a2_state/sim_results/sim_weyl_geometry_rescaling_shell_results.json`
  - classification: canonical
  - overall_pass: true
- existing owner anchor rerun:
  - `system_v4/probes/sim_weyl_spinor_hopf.py`
  - `system_v4/probes/a2_state/sim_results/weyl_spinor_hopf_results.json`
  - classification: canonical

Note
- optional graph/hypergraph/geomstats cross-checks were hardened so absent optional packages do not crash the shell-local owners.

## B4 — Flux / U(1) shell-local coverage

New canonical shell-local sims added and rerun-backed:
- `system_v4/probes/sim_u1_carrier_phase_shell_canonical.py`
  - `system_v4/probes/a2_state/sim_results/sim_u1_carrier_phase_shell_canonical_results.json`
- `system_v4/probes/sim_u1_structure_matrix_shell_canonical.py`
  - `system_v4/probes/a2_state/sim_results/sim_u1_structure_matrix_shell_canonical_results.json`
- `system_v4/probes/sim_u1_gauge_admissibility_constraint_shell_canonical.py`
  - `system_v4/probes/a2_state/sim_results/sim_u1_gauge_admissibility_constraint_shell_canonical_results.json`
- `system_v4/probes/sim_u1_wilson_loop_distinguishability_shell_canonical.py`
  - `system_v4/probes/a2_state/sim_results/sim_u1_wilson_loop_distinguishability_shell_canonical_results.json`
- `system_v4/probes/sim_u1_orientation_holonomy_shell_canonical.py`
  - `system_v4/probes/a2_state/sim_results/sim_u1_orientation_holonomy_shell_canonical_results.json`
- `system_v4/probes/sim_flux_stokes_cell_shell_canonical.py`
  - `system_v4/probes/a2_state/sim_results/sim_flux_stokes_cell_shell_canonical_results.json`

Verification
- all 6 reran under the Makefile interpreter
- all 6 carry canonical classification and shell-local positive/negative/boundary structure
- all 6 report `passes_local_rerun: true`

Coverage added
- U(1) carrier
- U(1) structure object
- U(1) admissibility constraint
- U(1) distinguishability probe
- U(1) orientation test
- local flux Stokes/cell-shell witness

## B5 — Pauli / Clifford baseline-tag audit

Result
- audited clifford_/pauli_ source/result pairs
- fixed honest tag drift
- reran all touched items
- final mismatch count in scope: 0

Touched files
- `system_v4/probes/sim_axiom_n01_pauli_algebra_closure.py`
- `system_v4/probes/sim_clifford_deep_cl3_rotor_double_cover.py`
- `system_v4/probes/sim_clifford_generator_basis.py`
- `system_v4/probes/sim_contact_clifford_mera_bridge_claims_canonical.py`
- `system_v4/probes/sim_four_topology_pauli_map.py`
- `system_v4/probes/sim_gtower_clifford_spin_double_cover.py`
- `system_v4/probes/sim_holographic_clifford_weyl_bridge_claims_canonical.py`
- `system_v4/probes/sim_lego_clifford_hierarchy.py`
- `system_v4/probes/sim_lego_pauli_algebra.py`
- `system_v4/probes/sim_lego_weyl_pauli_transport.py`
- `system_v4/probes/sim_pauli_algebra_relations.py`
- `system_v4/probes/sim_pauli_generator_basis.py`
- `system_v4/probes/sim_pure_lego_clifford_algebra.py`
- `system_v4/probes/sim_spectral_triple_clifford_z3_coupling.py`

Representative refreshed result paths
- `system_v4/probes/a2_state/sim_results/clifford_generator_basis_results.json`
- `system_v4/probes/a2_state/sim_results/pauli_generator_basis_results.json`
- `system_v4/probes/a2_state/sim_results/pauli_algebra_relations_results.json`
- `system_v4/probes/sim_results/lego_pauli_algebra_results.json`
- `system_v4/probes/a2_state/sim_results/pure_lego_clifford_algebra_results.json`
- `system_v4/probes/a2_state/sim_results/sim_gtower_clifford_spin_double_cover_results.json`

## Controller note

This note records shell-local coverage only. It does not promote pairwise coupling, coexistence, emergence, or Axis-0 manifold completion claims.
