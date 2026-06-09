---
title: Sim Run Catalogue and Result Family Router
created: 2026-05-18
updated: 2026-05-21
type: concept
tags: [simulation, results, catalogue, routing, evidence]
sources:
  - /tmp/wiki_sim_catalogue_path_scan_20260518.json
  - /tmp/wiki_sim_catalogue_scan_20260518.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/ops/formal_scouts/results
spec_mirrors:
  - /Users/joshuaeisenhart/wiki/specs/codex-ratchet/formal-scout-readiness-status.md
  - /Users/joshuaeisenhart/wiki/specs/codex-ratchet/sim-estate-integration-status.md
  - /Users/joshuaeisenhart/wiki/specs/codex-ratchet/tool-function-receipt-status.md
framing: historical_catalogue_snapshot
---

# Sim Run Catalogue and Result Family Router

## Purpose
This page is a catalogue router for things already run or artifacted in the repo. It is not about currently running sims.

It exists because the wiki was processing prior sim/result families while also enriching the broader harness, research, and tool-use surfaces. The right unit here is not one live process; it is a result family, probe packet, or catalogue layer that future agents can route into the wiki without rerunning everything first.

## Evidence boundary
The scan behind this page is filesystem/path-first over existing result JSON estates. It does not rerun sims, does not validate every JSON contract, and does not promote any result. It gives the wiki a catalogue map so later tranches can choose bounded families.

Current repo status is not maintained here. For generated counts, readiness, tool-role gate state, and promotion blockers, use [[specs/codex-ratchet/formal-scout-readiness-status|formal-scout-readiness-status]], [[specs/codex-ratchet/sim-estate-integration-status|sim-estate-integration-status]], and [[specs/codex-ratchet/tool-function-receipt-status|tool-function-receipt-status]].

Scan artifacts:
- `/tmp/wiki_sim_catalogue_path_scan_20260518.json`
- `/tmp/wiki_sim_catalogue_scan_20260518.json`

These `/tmp` scan artifacts are ephemeral inputs, not durable authority.

Observed result JSON estates in the dated catalogue pass:
- `system_v4/probes/a2_state/sim_results`: 6804 JSONs
- `system_v4/probes/results`: 10 JSONs
- `system_v5/ops/formal_scouts/results`: dated notes in this page recorded 294 raw JSONs on 2026-05-20 and 208 in the original 2026-05-18 scan. Do not use those as live counts.
- `system_v5/legos/results`: 13 JSONs
- `system_v5/evidence`: 10 JSONs
- dated total across those listed estates: 7131 JSONs on 2026-05-20. The original 2026-05-18 scan total was 7043.

Count boundary: the representative samples and family counts below come from the 2026-05-18 catalogue scan and later hand notes through 2026-05-20. They are routing signals, not live status. For current status, use the spec mirrors above.

## Catalogue family counts
These counts are routing signals from filenames/paths, not proof counts.

| Family | Count | Role |
|---|---:|---|
| survivor / gap micro-sims | 6146 | large prior micro-sim estate; good for extracting repeated constraint-survivor grammar |
| graph / topology / persistence | 2518 | graph, topology, GUDHI/TopoNetX/XGI/rustworkx/PyG evidence surfaces |
| Clifford / Pauli / spinor / chirality | 2045 | algebra/chirality/spinor routing family |
| Hopf / Weyl / torus | 1836 | nested Hopf/Weyl geometry routing family |
| density / QIT / entropy | 710 | tensor/density/coherent-information and entropy readout family |
| formal scouts | dated notes superseded by the spec mirror | v5 formal-scout result estate, mostly noncanonical formal_scout surfaces; use the formal-scout spec mirror for current counts |
| indices / ledgers / audits | 121 | catalogue surfaces that summarize other result families |
| tool capability / integration | 91 | tool-role/capability/function receipt surfaces |
| legos | 41 | explicit lego result surfaces |
| attractor / basin / policy / FEP | 39 | basin/anti-teleology/future-option support surfaces |

## Representative samples

### Survivor / gap micro-sims
- `system_v4/probes/a2_state/sim_results/sim_hopf_projection_relative_phase_pi_over_669_numpy_global_phase_gap_survivor_classes_results.json` — classification `tool_lego_fit_probe`
- `system_v4/probes/a2_state/sim_results/sim_spinor_s3_exact_coordinate_ratio_42_sympy_density_trace_gap_survivor_classes_results.json` — classification `tool_lego_fit_probe`
- `system_v4/probes/a2_state/sim_results/sim_composition_order_permutation_bound_44_cvc5_noncommuting_rank_gap_survivor_classes_results.json` — classification `tool_lego_fit_probe`
- `system_v4/probes/a2_state/sim_results/sim_clifford_pauli_weighted_generator_73_square_scalar_gap_survivor_classes_results.json` — classification `tool_lego_fit_probe`
- `system_v4/probes/a2_state/sim_results/sim_nested_torus_polygon_width_106_toponetx_cell_incidence_gap_survivor_classes_results.json` — classification `tool_lego_fit_probe`
- `system_v4/probes/a2_state/sim_results/sim_clifford_pauli_to_composition_order_weight_312_clifford_anticommutator_gap_survivor_classes_results.json` — classification `tool_lego_fit_probe`

### Graph / topology / persistence
- `system_v4/probes/a2_state/sim_results/sim_nested_torus_polygon_width_106_toponetx_cell_incidence_gap_survivor_classes_results.json` — classification `tool_lego_fit_probe`
- `system_v4/probes/a2_state/sim_results/sim_nested_torus_cycle_edges_215_gudhi_first_betti_gap_survivor_classes_results.json` — classification `tool_lego_fit_probe`
- `system_v4/probes/a2_state/sim_results/sim_fiber_base_loop_directed_path_nodes_76_rustworkx_endpoint_reachability_gap_survivor_classes_results.json` — classification `tool_lego_fit_probe`
- `system_v4/probes/a2_state/sim_results/sim_nested_torus_shared_hyperedge_width_345_xgi_incidence_degree_gap_survivor_classes_results.json` — classification `tool_lego_fit_probe`
- `system_v4/probes/a2_state/sim_results/sim_nested_torus_cycle_edges_50_gudhi_first_betti_gap_survivor_classes_results.json` — classification `tool_lego_fit_probe`
- `system_v4/probes/a2_state/sim_results/sim_rustworkx_deep_cycle_basis_generator_results.json` — classification `canonical`

### Clifford / Pauli / spinor / chirality
- `system_v4/probes/a2_state/sim_results/sim_spinor_s3_exact_coordinate_ratio_42_sympy_density_trace_gap_survivor_classes_results.json` — classification `tool_lego_fit_probe`
- `system_v4/probes/a2_state/sim_results/sim_clifford_pauli_weighted_generator_73_square_scalar_gap_survivor_classes_results.json` — classification `tool_lego_fit_probe`
- `system_v4/probes/a2_state/sim_results/sim_clifford_pauli_to_composition_order_weight_312_clifford_anticommutator_gap_survivor_classes_results.json` — classification `tool_lego_fit_probe`
- `system_v4/probes/a2_state/sim_results/sim_clifford_pauli_weighted_generator_144_square_scalar_gap_survivor_classes_results.json` — classification `tool_lego_fit_probe`
- `system_v4/probes/a2_state/sim_results/sim_spinor_s3_exact_coordinate_ratio_56_sympy_density_trace_gap_survivor_classes_results.json` — classification `tool_lego_fit_probe`
- `system_v4/probes/a2_state/sim_results/sim_spinor_s3_exact_coordinate_pi_over_520_sympy_hidden_coordinate_gap_survivor_classes_results.json` — classification `tool_lego_fit_probe`

### Hopf / Weyl / torus
- `system_v4/probes/a2_state/sim_results/sim_hopf_projection_relative_phase_pi_over_669_numpy_global_phase_gap_survivor_classes_results.json` — classification `tool_lego_fit_probe`
- `system_v4/probes/a2_state/sim_results/sim_nested_torus_polygon_width_106_toponetx_cell_incidence_gap_survivor_classes_results.json` — classification `tool_lego_fit_probe`
- `system_v4/probes/a2_state/sim_results/L0_hopf_manifold_results.json` — classification `classical_baseline`
- `system_v4/probes/a2_state/sim_results/sim_nested_torus_cycle_edges_215_gudhi_first_betti_gap_survivor_classes_results.json` — classification `tool_lego_fit_probe`
- `system_v4/probes/a2_state/sim_results/sim_nested_torus_shared_hyperedge_width_345_xgi_incidence_degree_gap_survivor_classes_results.json` — classification `tool_lego_fit_probe`
- `system_v4/probes/a2_state/sim_results/sim_nested_torus_cycle_edges_50_gudhi_first_betti_gap_survivor_classes_results.json` — classification `tool_lego_fit_probe`

### Density / QIT / entropy
- `system_v4/probes/a2_state/sim_results/sim_spinor_s3_exact_coordinate_ratio_42_sympy_density_trace_gap_survivor_classes_results.json` — classification `tool_lego_fit_probe`
- `system_v4/probes/a2_state/sim_results/sim_spinor_s3_exact_coordinate_ratio_56_sympy_density_trace_gap_survivor_classes_results.json` — classification `tool_lego_fit_probe`
- `system_v4/probes/a2_state/sim_results/sim_density_state_partial_trace_marginal_gap_survivor_classes_results.json` — classification `tool_lego_fit_probe`
- `system_v4/probes/a2_state/sim_results/sim_hopf_projection_relative_phase_pi_over_153_sympy_density_distance_gap_survivor_classes_results.json` — classification `tool_lego_fit_probe`
- `system_v4/probes/a2_state/sim_results/sim_hopf_projection_relative_phase_pi_over_118_qiskit_density_distance_gap_survivor_classes_results.json` — classification `tool_lego_fit_probe`
- `system_v4/probes/a2_state/sim_results/sim_hopf_projection_statevector_phase_pi_over_86_qiskit_density_distance_gap_survivor_classes_results.json` — classification `tool_lego_fit_probe`

### Formal scouts
- `system_v5/ops/formal_scouts/results/source_native_multicarrier_subdense_environment_contraction_probe_results.json` — classification `formal_scout`
- `system_v5/ops/formal_scouts/results/axis0_holographic_boundary_branch_closure_probe_results.json` — classification `formal_scout`
- `system_v5/ops/formal_scouts/results/long_horizon_source_multicarrier_holonomy_boundary_entropy_probe_results.json` — classification `formal_scout`
- `system_v5/ops/formal_scouts/results/hopf_shell_chirality_asymmetric_cptp_entropy_coupling_probe_results.json` — classification `formal_scout`
- `system_v5/ops/formal_scouts/results/gamma5_chirality_asymmetric_cptp_arbitrary_kraus_equivalence_kill_probe_results.json` — classification `formal_scout`
- `system_v5/ops/formal_scouts/results/fe_asymmetry_pauli_generator_algebra_z3_derivation_probe_results.json` — classification `formal_scout`

### Tool capability / integration
- `system_v4/probes/a2_state/sim_results/sim_geomstats_capability_results.json` — classification `canonical`
- `system_v4/probes/a2_state/sim_results/pytorch_capability_results.json` — classification `canonical`
- `system_v4/probes/a2_state/sim_results/sim_capability_rustworkx_isolated_results.json` — classification `classical_baseline`
- `system_v4/probes/a2_state/sim_results/tool_integration_sympy_pyg_results.json` — classification `canonical`
- `system_v4/probes/a2_state/sim_results/tool_capability_torch_results.json` — classification `canonical`
- `system_v4/probes/a2_state/sim_results/sim_capability_optuna_isolated_results.json` — classification `classical_baseline`

### Attractor / basin / policy / FEP
- `system_v4/probes/a2_state/sim_results/qit_carnot_hold_policy_companion_results.json` — classification `classical_baseline`
- `system_v4/probes/a2_state/sim_results/viability_vs_attractor_results.json` — classification `canonical`
- `system_v5/ops/formal_scouts/results/stage_record_true_perturbation_depth_probe_results.json` — classification `formal_scout`
- `system_v5/ops/formal_scouts/results/high_n_mps_engine_boundary_path_fep_transport_probe_results.json` — classification `formal_scout`
- `system_v5/ops/formal_scouts/results/operational_manifold_assembly_true_perturbation_depth_probe_results.json` — classification `formal_scout`
- `system_v5/ops/formal_scouts/results/attractor_basin_tmp_engine_v2_execution_aggregate_probe_results.json` — classification `formal_scout`

## How to process this catalogue into the wiki
Use this order for future bounded tranches:

1. Pick one family, not the whole estate.
2. Sample representative result JSONs and read their `classification`, `all_pass`/`pass`, tool manifest, tool integration depth, and claim ceiling.
3. Patch or create one family router/ledger page.
4. Link the family to broader research/support pages only as support, not proof.
5. Run `tools/wiki_probe.py` after each tranche.

## Existing processed lanes
- [[sim-session-index]] — older session-scoped catalogue of sampled sim findings.
- [[sim-math-geometry-result-surface-router]] — high-signal math/geometry surface router.
- [[attractor-basin-result-surface-ledger]] and [[attractor-basin-row-level-evidence-ledger]] — basin/result row ledgers.
- [[multi-tool-constraint-manifold-packet-router]] and [[max-stack-probe-variants-status-router]] — max-stack/multi-tool probe packet routing.
- [[formal-scout-readiness-index-router]] and [[sim-estate-integration-index-router]] — v5 formal-scout and manifold-estate index routers.
- [[specs/codex-ratchet/formal-scout-readiness-status]] and [[specs/codex-ratchet/sim-estate-integration-status]] — current wiki-side status mirrors.

## Overclaim fences
Do not read this catalogue as:
- a current rerun;
- proof that all JSONs satisfy the latest contract;
- proof that a family is canonical;
- proof that path keywords equal load-bearing use;
- permission to collapse many distinct result families into one story.

Safer language:
- artifacted result family;
- existing result estate;
- catalogue/router status;
- candidate family for bounded wiki processing;
- needs receipt-level reading before promotion.

## Related pages
- [[sim-math-geometry-result-surface-router]]
- [[repo-tool-use-router]]
- [[tool-function-receipt-matrix-router]]
- [[formal-scout-readiness-index-router]]
- [[sim-estate-integration-index-router]]
- [[specs/codex-ratchet/formal-scout-readiness-status]]
- [[specs/codex-ratchet/sim-estate-integration-status]]
- [[specs/codex-ratchet/tool-function-receipt-status]]
- [[negative-sims-and-kill-tests-support]]
- [[mass-sim-generator-wide-exploration-support]]
- [[basin-stability-and-viability-support]]
