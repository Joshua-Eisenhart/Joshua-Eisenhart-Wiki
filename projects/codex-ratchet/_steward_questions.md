# Codex-Ratchet Steward Questions

## Q1 — qutip + cirq capability FAILs (resolved)

**Context:** Tier A initially hit runner FAILs on `tool_capability_qutip.py` and `tool_capability_cirq.py`.

**Resolution:** later Tier A repairs landed, reruns succeeded, and `tier_a.md` now records both probes as repaired and runner-DONE.

**Current status:** resolved; retained here only as audit history, not as pending L3 judgment.

## Q2 — orphan canonical results downgrade (resolved in part)

**Context:** `tier_a_t3_audit.json` initially listed 80 canonical results with no `system_v4/probes/*.py` source match.

**OVERNIGHT.md §1 default:** downgrade to `classification: "classical_baseline"` with reason `"orphan_no_source_2026-04-17"`.

**Current status:** `tier_a.md` says the orphan downgrade was applied, and repo commit `abf0ffac` also landed a broader systematic downgrade of 71 SIM_TEMPLATE-violation probes. This item is no longer a pending L3 question, though the exact overlap between the 80 orphan set and the 71 systematic-violation set may still deserve later audit.

---

Historical note from the 2026-04-17 steward pass: no non-META blockers were pending in that pass. Use `STATUS.md` and the spec mirrors for current blocker state.

## META blocker 2026-04-17T01:32:25-07:00
- critical canonical-label abuse: {'result_json': '/Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_ito_calculus_constraint_results.json', 'missing': 'load_bearing ladder tool'}
- critical canonical-label abuse: {'result_json': '/Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_quantum_error_correction_constraint_results.json', 'missing': 'load_bearing ladder tool'}
- critical canonical-label abuse: {'result_json': '/Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_banach_fixed_point_constraint_results.json', 'missing': 'load_bearing ladder tool'}
- critical canonical-label abuse: {'result_json': '/Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_geometry_toric_variety_fan_constraint_canonical_results.json', 'missing': 'load_bearing ladder tool'}
- critical canonical-label abuse: {'result_json': '/Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_renormalization_group_constraint_results.json', 'missing': 'load_bearing ladder tool'}
- critical canonical-label abuse: {'result_json': '/Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/torch_t_gate_results.json', 'missing': 'TOOL_INTEGRATION_DEPTH'}
- critical canonical-label abuse: {'result_json': '/Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_fiber_bundle_triviality_results.json', 'missing': 'load_bearing ladder tool'}
- critical canonical-label abuse: {'result_json': '/Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_geometry_pure_motive_chow_group_constraint_canonical_results.json', 'missing': 'load_bearing ladder tool'}
- critical canonical-label abuse: {'result_json': '/Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_e6_root_system_constraint_results.json', 'missing': 'load_bearing ladder tool'}
- critical canonical-label abuse: {'result_json': '/Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_intersection_cohomology_constraint_results.json', 'missing': 'load_bearing ladder tool'}
- critical canonical-label abuse: {'result_json': '/Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/low_rank_psd_approximation_results.json', 'missing': 'load_bearing ladder tool'}
- critical canonical-label abuse: {'result_json': '/Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/entanglement_entropy_results.json', 'missing': 'load_bearing ladder tool'}
- critical canonical-label abuse: {'result_json': '/Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/qit_szilard_record_ordering_refinement_translation_lane_results.json', 'missing': 'load_bearing ladder tool'}
- critical canonical-label abuse: {'result_json': '/Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_univalence_axiom_constraint_results.json', 'missing': 'load_bearing ladder tool'}
- critical canonical-label abuse: {'result_json': '/Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_fisher_information_constraint_results.json', 'missing': 'load_bearing ladder tool'}
- critical canonical-label abuse: {'result_json': '/Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_geometry_heegaard_floer_homology_constraint_canonical_results.json', 'missing': 'load_bearing ladder tool'}
- critical canonical-label abuse: {'result_json': '/Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/branch_weight_results.json', 'missing': 'load_bearing ladder tool'}
- critical canonical-label abuse: {'result_json': '/Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_subdifferential_constraint_canonical_results.json', 'missing': 'load_bearing ladder tool'}
- critical canonical-label abuse: {'result_json': '/Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_induced_representation_constraint_results.json', 'missing': 'load_bearing ladder tool'}
- critical canonical-label abuse: {'result_json': '/Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_algebraic_effect_handler_constraint_results.json', 'missing': 'load_bearing ladder tool'}

## META blocker 2026-04-17T08:48:22Z
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/gtower_order_so_to_u_then_su_vs_reverse_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/geom_noncomm_so3_u1_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_zorns_lemma_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_endoscopy_transfer_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_enriched_category_hom_object_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_toric_moment_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_geometric_langlands_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/leviathan_centralization_destroys_admissibility_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_jet_bundle_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_system_f_rank_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_de_rham_crystalline_comparison_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_cohft_axioms_splitting_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/z3_negative_quasiprob_exclusion_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_sobolev_embedding_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_compound_z3_clifford_pyg_so3_admissibility_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_derived_stack_mapping_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/tool_integration_sympy_pyg_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/L8_chiral_density_bookkeeping_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_open_mapping_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_geometry_donaldson_uhlenbeck_yau_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_geometry_characteristic_variety_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_autograd_deep_implicit_function_theorem_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_neron_model_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/c2_topology_remaining_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_cobordism_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/f01n01_couple_indistinguishable_saturates_probe_capacity_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_applicative_functor_laws_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_nahodge_3_reduction_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/geom_noncomm_hopf_weyl_proj_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_operator_product_expansion_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_infinity_category_nerve_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/hopf_fiber_equivalence_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/layer_stacking_nonprefix_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_braided_monoidal_hexagon_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cl3_bivector_entropy_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/torch_re_coherence_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_geometry_reductive_group_root_datum_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/torsion_curvature_splitting_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_cubical_type_theory_path_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_gap_associative_3algebra_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_conformal_bootstrap_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/rustworkx_petersen_iso_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_discrete_log_hardness_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/geom_noncomm_bch_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_arrow_calculus_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/tri_science_method_x_igt_x_leviathan_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/lego_08_equiv_class_cardinality_2q_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_elliptic_regularity_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/geom_layer_8_9_10_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_derived_geom_4_admissibility_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/werner_manifold_scan_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/qit_weyl_geometry_repair_comparison_surface_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_information_complexity_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_lawvere_theory_model_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_rustworkx_deep_cayley_s4_admissibility_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_halting_problem_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_geometry_delzant_polytope_torus_action_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_ramsey_theorem_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/bridge_fe_relay_sweep_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_perfectoid_space_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/e3nn_capability_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_uniqueness_type_alias_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_gap_derived_stack_cotangent_complex_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_holo_mera_clifford_triple_coexistence_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_a_infinity_algebra_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/conditional_entropy_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_abstract_interpretation_lattice_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/f01n01_couple_probe_refinement_bounded_by_log_N_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/tri_science_method_x_fep_x_igt_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/holodeck_atom_6_chirality_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/cl3_deep_rotor_conjugation_preserves_grade_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_u1_gauge_fixing_residual_mode_shell_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_lattice_distributive_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/f01_fail_07_zero_quantum_infinite_regress_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_compound_torus_spinor_admissibility_cvc5_parity_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/spectral_triple_gtower_reduction_spectrum_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/f01_cross_11_pytorch_autograd_distinguishability_loss_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/gerbe_reduction_coboundary_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/torch_channel_taxonomy_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/covariance_operator_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_u1_link_variable_exactness_shell_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_motivic_cohomology_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_clifford_deep_cl3_rotor_double_cover_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_fep_pair_free_energy_x_engine_coupling_cvc5_parity_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_limit_universal_cone_constraint.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_duality_gap_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_negative_k_theory_bass_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/bridge_entropy_inequality_guardrails_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_mechanism_design_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/integrated_dependency_chain_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_symmetric_monoidal_coherence_maclanethm_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/negative_xi_winner_disqualifiers_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_jones_polynomial_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/teleportation_fidelity_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/wilczek_zee_holonomy_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_geometry_calibrated_submanifold_comass_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/qit_repair_comparison_surface_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_quantum_teleportation_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/contact_symplectic_kahler_coexistence_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/phase7_divergence_analysis_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_n01_compose_refinement_monotone_in_probe_set_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_min_plus_algebra_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/trace_distance_geometry_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_geometry_mixed_hodge_structure_weight_filtration_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/operator_low_rank_factorization_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_pi_type_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_gtower_reduction_chain_composition_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_arthur_packet_multiplicity_formula_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_compact_operator_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_whitehead_theorem_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/fep_pair_active_inference_x_markov_blanket_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_identity_type_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/gerbe_structure_b_field_cochain_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_poisson_process_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_L17_signed_unsigned_entropy_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/cl3_deep_rotor_order_rx_ry_vs_ry_rx_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_geometry_cheeger_inequality_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/qit_weyl_geometry_carrier_translation_lane_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_completeness_theorem_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/conformal_structure_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/fep_pair_surprise_x_precision_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_ads_cft_bulk_boundary_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_weakest_precondition_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_chromatic_convergence_theorem_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_no_cloning_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/tool_integration_manim_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_fredholm_index_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_field_extension_degree_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_gap_formal_moduli_problem_schlessinger_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_geometry_open_book_decomposition_contact_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_natural_gradient_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/tri_holodeck_x_science_method_x_leviathan_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_axiom_f01_quotient_well_defined_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_modular_form_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_quasi_isometry_invariant_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_descent_data_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/weyl_geometry_ladder_audit_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_gerbe_pairwise_holonomy_coupling_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_infinity_topos_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_networkx_deep_expander_gap_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_assoc_bundle_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/lego_07_abc_vs_acb_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/contact_symplectic_coupling_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/lego_su2_representations_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/tensor_network_spinor_torus_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/groebner_basis_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/qit_carnot_closure_translation_lane_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_perfect_complex_amplitude_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_a1_homotopy_6_chirality_coupling_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/torus_seat_entropy_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_gromov_witten_genus_virtual_dimension_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_geometry_dolbeault_cohomology_hodge_numbers_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cotangent_complex_obstruction_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/cross_holodeck_x_igt_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_gerbe_derived_stack_cohomology_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_exact_sequence_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_index_theorem_torch_foundation_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/holodeck_deep_coupling_to_fep_markov_blanket_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_bezout_theorem_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_geometry_p_adic_hodge_cst_functor_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_feigenbaum_constant_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/f01_deep_03_information_bound_shannon_log_N_max_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_noncommutative_torus_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_modal_mu_calculus_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_geometry_thom_transversality_stratification_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cl6_even_subalgebra_closure_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_density_matrix_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_ricci_flow_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_homological_mirror_symmetry_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_matroid_intersection_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_gtower_gudhi_persistence_reduction_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_geometry_castelnuovo_mumford_regularity_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_fep_pair_surprise_x_precision_cvc5_parity_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_galois_correspondence_subgroup_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_motivic_filtration_tc_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_gtower_u1_hopf_fiber_reduction_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_arith_geom_1_carrier_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_crystalline_cohomology_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/fep_atom_6_chirality_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_presentable_infinity_category_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/cl3_deep_pseudoscalar_inversion_vs_reflection_order_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_geometry_lagrangian_floer_index_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/fep_joint_smt_free_energy_and_markov_blanket_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_brown_representability_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_torch_clifford_ga_bridge_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_geometry_etale_cohomology_ladic_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/f01_deep_02_finiteness_forces_discrete_spectrum_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_schur_weyl_duality_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_quad_holodeck_igt_sci_method_fep_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_local_global_principle_hasse_minkowski_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_string_diagram_composition_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/toponetx_constraint_shells_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_geometry_floer_homology_maslov_index_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_derived_geom_6_chirality_coupling_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_sobolev_embedding_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/pure_lego_qfi_wy_qgt_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_algebraic_cycles_hodge_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/spectral_triple_connes_distance_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_subtyping_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_chern_simons_gauge_invariance_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/circuit_unitary_canonicalization_z3_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_intersection_theory_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sympy_gaussian_integral_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/stable_stems_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/pauli_algebra_relations_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_connection_form_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_heterotic_string_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_gap_homotopy_hypothesis_grothendieck_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_geometry_height_function_weil_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sympy_jacobi_su2_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_cartesian_closed_category_exponential_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_integration_evotorch_autograd_constraint_search_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/fep_pair_markov_blanket_x_precision_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_dirichlet_lfunction_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_pymoo_nsga2_pareto_admissibility_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_contact_manifold_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/leviathan_atom_7_coupling_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_geometry_quantum_cohomology_frobenius_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cobordism_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/holodeck_atom_1_carrier_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/xgi_capability_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_fep_pair_markov_blanket_x_precision_cvc5_parity_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/assoc_bundle_weyl_spinor_as_section_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_gtower_su_to_sp_symplectic_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/foundation_equivariant_graph_backprop_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_L19_dynamics_on_entropy_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/axis_couple_1_5_curvature_x_torus_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_results/geom_symplectic_kahler_contact_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_results/lego_toric_code_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_results/geom_2qubit_s7_cp3_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_results/lego_info_geometry_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T09:13:35Z
- timestamp: 2026-04-17T09:13:35Z
- class: canonical-label abuse
- why critical: 43 new canonical results in the audit window lacked TOOL_INTEGRATION_DEPTH or a load_bearing ladder tool, so the public canonical label outran the harness gate.
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/L8_chiral_density_bookkeeping_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/autograd_matrix_exp_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/axis6_e3nn_fe_bridge_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/axis7_12_gs_residual_axes_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/bridge_phi0_proof_integration_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/bridge_z3_kernel_ordering_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/c2_topology_remaining_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/channel_space_geometry_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/chiral_density_bookkeeping_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/cross_shell_coupling_cp1_bures_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/density_hopf_geometry_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/fep_atom_2_structure_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/frame_bundle_structure_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/rustworkx_petersen_iso_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_algebraic_k_theory_quillen_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_assume_guarantee_composition_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_gromov_witten_genus_virtual_dimension_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_intersection_type_meet_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_limit_universal_cone_constraint.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_flux_stokes_cell_shell_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_geometry_dolbeault_cohomology_hodge_numbers_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_geometry_height_function_weil_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_geometry_pss_isomorphism_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_gerbestack_weyl_hopf_dirac_mera_toric_clifford_spinor_riemannian_connection_holonomy_fiber_assoc_moment_14shell_coupling_canonical_results.json — canonical result lacks load_bearing ladder tool
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_gerbestack_weyl_hopf_dirac_mera_toric_clifford_spinor_riemannian_connection_holonomy_fiber_assoc_moment_derivedcategory_15shell_coupling_canonical_results.json — canonical result lacks load_bearing ladder tool
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_gerbestack_weyl_hopf_dirac_mera_toric_clifford_spinor_riemannian_connection_holonomy_fiber_assoc_moment_derivedcategory_crystallinecoho_16shell_coupling_canonical_results.json — canonical result lacks load_bearing ladder tool
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_gerbestack_weyl_hopf_dirac_mera_toric_clifford_spinor_riemannian_connection_holonomy_fiber_assoc_moment_derivedcategory_etalecoho_16shell_coupling_canonical_results.json — canonical result lacks load_bearing ladder tool
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_gerbestack_weyl_hopf_dirac_mera_toric_clifford_spinor_riemannian_connection_holonomy_fiber_assoc_moment_derivedcategory_etalecoho_adsboundary_17shell_coupling_canonical_results.json — canonical result lacks load_bearing ladder tool
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_gerbestack_weyl_hopf_dirac_mera_toric_clifford_spinor_riemannian_connection_holonomy_fiber_assoc_moment_derivedcategory_etalecoho_bpsmass_17shell_coupling_canonical_results.json — canonical result lacks load_bearing ladder tool
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_gerbestack_weyl_hopf_dirac_mera_toric_clifford_spinor_riemannian_connection_holonomy_fiber_assoc_moment_derivedcategory_etalecoho_instantonnumber_17shell_coupling_canonical_results.json — canonical result lacks load_bearing ladder tool
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_gerbestack_weyl_hopf_dirac_mera_toric_clifford_spinor_riemannian_connection_holonomy_fiber_assoc_moment_derivedcategory_etalecoho_tqftpartition_17shell_coupling_canonical_results.json — canonical result lacks load_bearing ladder tool
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_hopf_fibration_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_integration_optuna_sympy_invariant_search_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_lagrangian_duality_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_lego_entropy_relative_js_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_lego_entropy_shell_history_weighted_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_negative_bridge_cut_counterfeits_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_negative_global_shell_bridge_counterfeits_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_quillen_model_category_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_riemannian_connection_holonomy_fiber_assoc_moment_index_chern_8shell_coupling_canonical_results.json — canonical result lacks load_bearing ladder tool
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_symmetric_monoidal_coherence_maclanethm_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/torch_gnn_directional_gate_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/weyl_geometry_ladder_audit_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T09:44:46Z
- class: canonical-label abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/assoc_bundle_parallel_transport_admissibility_results.json
- why critical: new committed result is labeled canonical but lacks TOOL_INTEGRATION_DEPTH, so canonical-by-process support is not present in the artifact.

## BLOCKER 2026-04-17T10:07:48Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/cl3_deep_pseudoscalar_inversion_vs_reflection_order_results.json (cd1c9a4d7b024edba79a65f8332b18e611061e57)
- why_critical: classification is canonical while TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool is missing, so canonical-by-process was not earned under the stated detector contract.

## BLOCKER 2026-04-17T10:07:48Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/cl3_deep_rotor_conjugation_preserves_grade_results.json (cd1c9a4d7b024edba79a65f8332b18e611061e57)
- why_critical: classification is canonical while TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool is missing, so canonical-by-process was not earned under the stated detector contract.

## BLOCKER 2026-04-17T10:07:48Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/cl3_deep_rotor_order_rx_ry_vs_ry_rx_results.json (cd1c9a4d7b024edba79a65f8332b18e611061e57)
- why_critical: classification is canonical while TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool is missing, so canonical-by-process was not earned under the stated detector contract.

## BLOCKER 2026-04-17T10:07:48Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/lego_entropy_holevo_quantity_results.json (cd1c9a4d7b024edba79a65f8332b18e611061e57)
- why_critical: classification is canonical while TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool is missing, so canonical-by-process was not earned under the stated detector contract.

## BLOCKER 2026-04-17T10:07:48Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/lego_entropy_inequalities_results.json (cd1c9a4d7b024edba79a65f8332b18e611061e57)
- why_critical: classification is canonical while TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool is missing, so canonical-by-process was not earned under the stated detector contract.

## BLOCKER 2026-04-17T10:07:48Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/channel_space_geometry_results.json (38805f0c9e9c419544481191768b5afa4facf80d)
- why_critical: classification is canonical while TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool is missing, so canonical-by-process was not earned under the stated detector contract.

## BLOCKER 2026-04-17T10:07:48Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/cirq_matrix_state_bridge_results.json (992a6245cbae2eea40923649c55ad011c2aae239)
- why_critical: classification is canonical while TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool is missing, so canonical-by-process was not earned under the stated detector contract.

## BLOCKER 2026-04-17T10:07:48Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/assoc_bundle_parallel_transport_admissibility_results.json (d72f13e21911dcb054e3ac237dce85ed4ad13787)
- why_critical: classification is canonical while TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool is missing, so canonical-by-process was not earned under the stated detector contract.

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/3q_ambiguity_expansion_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/3qubit_full_cascade_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/4qubit_cascade_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/adiabatic_berry_dynamics_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/adversarial_ratchet_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/axis6_e3nn_fe_bridge_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/bridge_cut_perturbation_stability_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/bridge_entropy_inequality_guardrails_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/bridge_finite_blocklength_cut_states_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/bridge_phi0_proof_integration_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/c2_topology_remaining_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/channel_space_geometry_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/chiral_density_bookkeeping_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/chsh_tsirelson_canonical_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/cl3_deep_pseudoscalar_inversion_vs_reflection_order_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/cl3_deep_rotor_conjugation_preserves_grade_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/cl3_deep_rotor_order_rx_ry_vs_ry_rx_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/coherent_information_measure_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/conditional_entropy_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/contact_structure_s3_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/contact_symplectic_coupling_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/contact_symplectic_kahler_coexistence_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/cvc5_capability_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/cvc5_cross_check_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/e3nn_capability_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/e3nn_equivariant_qubits_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/engine_16_placements_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/engine_8_terrains_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/fiber_loop_law_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/foundation_channel_constraints_hardway_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/foundation_equivariant_graph_backprop_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/full_ratchet_cascade_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/geodesic_deviation_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/geodesic_exponential_map_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/geom_cp1_u1_projective_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/geom_layer_1_2_3_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/geom_layer_4_5_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/geom_layer_6_7_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/geom_layer_8_9_10_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/geom_su2_so3_quaternions_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/geom_topology_layers_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/geomstats_frechet_mean_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/geomstats_shell_metrics_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/graph_geometry_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/gudhi_bridge_persistence_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/gudhi_cascade_persistence_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/gudhi_wasserstein_significance_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/hopf_contact_symplectic_bridge_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/information_geometry_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/integrated_dependency_chain_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/layer_coupling_matrix_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/layer_coupling_matrix_v2_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/layer_coupling_matrix_v3_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/layered_foundation_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/lego_coherent_info_advanced_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/lego_entanglement_distillation_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/lego_entropy_bipartite_cut_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/lego_entropy_extremal_density_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/lego_entropy_finite_blocklength_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/lego_entropy_holevo_quantity_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/lego_entropy_inequalities_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/lego_entropy_inequalities_stability_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/lego_entropy_multipartite_cuts_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/lego_entropy_smooth_one_shot_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/lego_entropy_spectral_families_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/lego_graph_cluster_states_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/lego_nested_hopf_tori_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/lego_su2_representations_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/lego_uhlmann_phase_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/lego_weyl_wigner_phase_space_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/lego_zeno_speed_limits_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/local_operator_action_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/lorentzian_geometry_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/negative_phi0_candidate_disqualifiers_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/negative_xi_winner_disqualifiers_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/phase7_divergence_analysis_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/phase_transition_sweep_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/phi0_ic_vs_mi_regime_map_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/phi0_integrated_bakeoff_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/phi0_matched_packet_head_to_head_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/phi0_packet_robustness_audit_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/phi0_shell_global_ablation_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/pure_lego_hypothesis_testing_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/pure_lego_ic_shell_boundary_continuity_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/qfi_killpoint_divergence_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/qit_szilard_record_translation_lane_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/ratchet_optimizer_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/riemannian_curvature_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/rustworkx_cascade_dag_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/rustworkx_family_dag_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sa10_wilczek_zee_curvature_boundary_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_fep_pair_free_energy_x_engine_coupling_cvc5_parity_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_geometry_etale_cohomology_ladic_constraint_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_gerbe_pairwise_holonomy_coupling_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_lego_entropy_relative_js_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_lego_entropy_shell_history_weighted_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_negative_bridge_cut_counterfeits_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_negative_global_shell_bridge_counterfeits_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/spectral_triple_contact_gerbe_bridge_claims_canonical_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/stinespring_dilation_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/su2_killing_form_exhaustion_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/wilczek_zee_curvature_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:32:53Z canonical_abuse
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/wilczek_zee_holonomy_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T10:57:07Z
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/adams_spectral_sequence_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/circuit_unitary_canonicalization_z3_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/cvc5_proof_complexity_size_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/cvc5_resolution_proof_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/density_hopf_geometry_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/geomstats_capability_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/leviathan_gudhi_stability_persistence_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_geometry_k_theory_localization_sequence_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/stable_stems_constraint_canonical_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/temporal_cascade_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/tensor_network_spinor_torus_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/topology_entropy_dynamics_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/toponetx_constraint_shells_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/torch_bit_phase_flip_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/torch_cartan_kak_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/torch_channel_taxonomy_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/torch_chiral_overlap_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/torch_cnot_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/torch_constraint_shells_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/torch_cz_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/torch_density_matrix_pilot_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/torch_hadamard_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/torch_husimi_q_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/torch_iswap_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/torch_lindblad_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/torch_mutual_info_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/torch_phase_flip_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/torch_re_coherence_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/torch_swap_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/torch_t_gate_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/torch_unitary_rotation_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/torch_wigner_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/torch_x_dephasing_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/torch_z_measurement_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/twilight_zone_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/variational_quantum_bridge_pytorch_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/von_neumann_entropy_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/weyl_geometry_ladder_audit_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/weyl_nested_shell_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/xgi_l7_marginal_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/xgi_shell_hypergraph_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T11:18:26Z
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/cvc5_shells_crosscheck_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/density_hopf_geometry_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T11:41:10Z
- critical canonical_abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/density_hopf_geometry_results.json — canonical classification lacks TOOL_INTEGRATION_DEPTH


## META blocker 2026-04-17T12:05:17Z
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/SA12_wilczek_zee_curvature_sympy_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/cvc5_frege_system_constraint_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/density_hopf_geometry_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/fiber_loop_law_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/hopf_fiber_equivalence_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/lego_entropy_spectral_families_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
## META blocker 2026-04-17T12:27:37Z canonical_abuse /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/lego_entropy_smooth_one_shot_results.json
- timestamp: 2026-04-17T12:27:37Z
- class: canonical_abuse
- commit: 439a8906e14e465f17954cc8b537790db47b3138
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/lego_entropy_smooth_one_shot_results.json
- why_critical: classification is canonical but TOOL_INTEGRATION_DEPTH is absent, so canonical by process is not admitted under Tier META rules.

## META blocker 2026-04-17T12:27:37Z canonical_abuse /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_shimura_variety_canonical_model_results.json
- timestamp: 2026-04-17T12:27:37Z
- class: canonical_abuse
- commit: 439a8906e14e465f17954cc8b537790db47b3138
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_shimura_variety_canonical_model_results.json
- why_critical: classification is canonical but TOOL_INTEGRATION_DEPTH is absent, so canonical by process is not admitted under Tier META rules.

## META blocker 2026-04-17T12:27:37Z canonical_abuse /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/L8_chiral_density_bookkeeping_results.json
- timestamp: 2026-04-17T12:27:37Z
- class: canonical_abuse
- commit: e207553273de6a54e0b3b02a7647dd935a044aa9
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/L8_chiral_density_bookkeeping_results.json
- why_critical: classification is canonical but TOOL_INTEGRATION_DEPTH is absent, so canonical by process is not admitted under Tier META rules.

## META blocker 2026-04-17T12:27:37Z canonical_abuse /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/heat_equation_constraint_canonical_results.json
- timestamp: 2026-04-17T12:27:37Z
- class: canonical_abuse
- commit: e207553273de6a54e0b3b02a7647dd935a044aa9
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/heat_equation_constraint_canonical_results.json
- why_critical: classification is canonical but TOOL_INTEGRATION_DEPTH is absent, so canonical by process is not admitted under Tier META rules.

## META blocker 2026-04-17T12:27:37Z canonical_abuse /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/lego_entropy_extremal_density_results.json
- timestamp: 2026-04-17T12:27:37Z
- class: canonical_abuse
- commit: e207553273de6a54e0b3b02a7647dd935a044aa9
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/lego_entropy_extremal_density_results.json
- why_critical: classification is canonical but TOOL_INTEGRATION_DEPTH is absent, so canonical by process is not admitted under Tier META rules.

## META blocker 2026-04-17T12:27:37Z canonical_abuse /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/leviathan_authority_entropy_operator_results.json
- timestamp: 2026-04-17T12:27:37Z
- class: canonical_abuse
- commit: e207553273de6a54e0b3b02a7647dd935a044aa9
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/leviathan_authority_entropy_operator_results.json
- why_critical: classification is canonical but TOOL_INTEGRATION_DEPTH is absent, so canonical by process is not admitted under Tier META rules.

## META blocker 2026-04-17T12:27:37Z canonical_abuse /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/spinor_harmonics_constraint_results.json
- timestamp: 2026-04-17T12:27:37Z
- class: canonical_abuse
- commit: e207553273de6a54e0b3b02a7647dd935a044aa9
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/spinor_harmonics_constraint_results.json
- why_critical: classification is canonical but TOOL_INTEGRATION_DEPTH is absent, so canonical by process is not admitted under Tier META rules.

## META blocker 2026-04-17T12:27:37Z canonical_abuse /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/clifford_so_homomorphism_results.json
- timestamp: 2026-04-17T12:27:37Z
- class: canonical_abuse
- commit: 9443639e34ba0470c8f64142aa0b76d88b88c783
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/clifford_so_homomorphism_results.json
- why_critical: classification is canonical but TOOL_INTEGRATION_DEPTH is absent, so canonical by process is not admitted under Tier META rules.

## META blocker 2026-04-17T12:27:37Z canonical_abuse /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/groebner_basis_constraint_canonical_results.json
- timestamp: 2026-04-17T12:27:37Z
- class: canonical_abuse
- commit: 9443639e34ba0470c8f64142aa0b76d88b88c783
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/groebner_basis_constraint_canonical_results.json
- why_critical: classification is canonical but TOOL_INTEGRATION_DEPTH is absent, so canonical by process is not admitted under Tier META rules.

## META blocker 2026-04-17T12:27:37Z canonical_abuse /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sa10_wilczek_zee_curvature_boundary_results.json
- timestamp: 2026-04-17T12:27:37Z
- class: canonical_abuse
- commit: 9443639e34ba0470c8f64142aa0b76d88b88c783
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sa10_wilczek_zee_curvature_boundary_results.json
- why_critical: classification is canonical but TOOL_INTEGRATION_DEPTH is absent, so canonical by process is not admitted under Tier META rules.

## META blocker 2026-04-17T12:27:37Z canonical_abuse /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/tropical_geometry_constraint_canonical_results.json
- timestamp: 2026-04-17T12:27:37Z
- class: canonical_abuse
- commit: 1a585fa6a08cdeb1959a35a5094b7745f08fac0e
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/tropical_geometry_constraint_canonical_results.json
- why_critical: classification is canonical but TOOL_INTEGRATION_DEPTH is absent, so canonical by process is not admitted under Tier META rules.


## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_shimura_reciprocity_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_k1_group_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_toric_moment_constraint_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_geometric_langlands_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_jet_bundle_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_branching_rules_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_sobolev_embedding_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_fiber_bundle_triviality_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/quillen_adjunction_derived_functor_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_temporal_logic_ltl_constraint_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_clifford_chirality_admissible_generators_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_rectifiable_current_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_mixing_property_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cauchy_theorem_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_simply_typed_lambda_constraint_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_e6_root_system_constraint_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_kahler_positivity_constraint_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_sigma_algebra_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_infinity_category_nerve_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cl3_bivector_entropy_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_poisson_bracket_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_connection_torch_foundation_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_nim_strategy_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_assoc_bundle_torch_foundation_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/qit_weyl_geometry_repair_comparison_surface_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_weyl_character_formula_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_spin_foam_vertex_amplitude_constraint_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_sheaf_condition_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_spin7_holonomy_constraint_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cheeger_inequality_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_elliptic_regularity_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_integration_ribs_z3_constraint_archive_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_universal_q_cross_program_invariant_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_yang_mills_energy_constraint_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_hamiltonian_flow_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_induced_representation_constraint_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_mixing_rate_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/qit_strong_coupling_landauer_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_reflexive_banach_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_hecke_correspondence_shimura_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/lego_nested_hopf_tori_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/bridge_entropy_inequality_guardrails_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_cubical_path_constraint_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_newton_polygon_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_chow_group_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/negative_xi_winner_disqualifiers_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_marchenko_pastur_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_torelli_theorem_constraint_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_cohomology_ring_constraint_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cl6_clifford_algebra_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_module_over_ring_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_hopf_symplectic_contact_torch_canonical_results.json
- why_critical: classification=canonical with missing load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_p_adic_comparison_crystalline_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_type_inference_hindley_milner_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_covariant_derivative_torch_foundation_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_identity_type_constraint_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_fredholm_operator_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_lego_cl6_tool_integration_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_sylow_theorem_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/clifford_weyl_transport_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_kantorovich_duality_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_epistemic_logic_constraint_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_poisson_process_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_completeness_theorem_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_church_turing_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/e3nn_equivariant_qubits_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_entropy_map_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_ads_cft_bulk_boundary_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_weakest_precondition_constraint_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_monte_carlo_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cofibration_lifting_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_no_cloning_constraint_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_lego_entropy_family_crosscheck_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_proximal_gradient_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/negative_phi0_candidate_disqualifiers_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_e7_root_system_constraint_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_fluctuation_dissipation_constraint_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/gudhi_3qubit_bridge_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_symplectic_form_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/kahler_geometry_constraint_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_continuity_equation_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_sprague_grundy_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_plateau_problem_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_geometry_stable_maps_gromov_witten_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_symmetric_function_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/homotopy_limit_colimit_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cantor_theorem_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/hardy_littlewood_maximal_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_newtons_method_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_lyapunov_stability_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_martingale_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_newton_method_convergence_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_hopf_connection_curvature_operators_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_connection_curvature_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_geometry_tautological_ring_moduli_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_index_theorem_torch_foundation_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_g2_exceptional_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_geometry_shimura_variety_reciprocity_constraint_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_hensel_lemma_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_z3_pytorch_cross_check_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_condition_number_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/newton_polytope_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_dirichlet_principle_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_ergodic_theorem_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_crystalline_cohomology_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_moment_map_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_infinity_stack_descent_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_nullstellensatz_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_zermelo_wellordering_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/gerbe_derived_stack_pairwise_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_grothendieck_topos_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_contact_torch_foundation_results.json
- why_critical: classification=canonical with missing load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_darboux_theorem_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_graph_coloring_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_hoare_logic_constraint_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_spectral_unbounded_operator_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_z3_deep_no_classical_stochastic_under_dephasing_weyl_commute_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_g2_manifold_constraint_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_horn_conjecture_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_holographic_entropy_bound_constraint_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_gerbe_contact_clifford_torch_canonical_results.json
- why_critical: classification=canonical with missing load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_lego_assoc_bundle_load_bearing_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_radon_nikodym_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/foundation_pauli_bloch_backprop_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_connection_form_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_holonomy_torch_foundation_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/z3_dephasing_symmetry_guard_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_schauder_basis_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_integration_evotorch_autograd_constraint_search_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_mera_entropy_bound_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_weyl_clifford_spectral_triple_coupling_canonical_results.json
- why_critical: classification=canonical with missing load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_p_adic_ultrametric_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_fano_variety_constraint_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/xgi_capability_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_motivic_cohomology_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_quantum_circuit_depth_constraint_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_cvc5_curry_howard_constraint_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T06:19:59-0700 canonical_abuse
- timestamp: 2026-04-17T06:19:59-0700
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_courant_fischer_constraint_canonical_results.json
- why_critical: classification=canonical with missing TOOL_INTEGRATION_DEPTH,load_bearing_ladder_tool

## META blocker 2026-04-17T13:47:51Z canonical_abuse
- timestamp: 2026-04-17T13:47:51Z
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/c2_topology_expansion_results.json
- why_critical: committed result is labeled canonical but lacks TOOL_INTEGRATION_DEPTH.

## META blocker 2026-04-17T13:47:51Z canonical_abuse
- timestamp: 2026-04-17T13:47:51Z
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/chiral_density_bookkeeping_results.json
- why_critical: committed result is labeled canonical but lacks TOOL_INTEGRATION_DEPTH.

## META blocker 2026-04-17T13:47:51Z canonical_abuse
- timestamp: 2026-04-17T13:47:51Z
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/geomstats_ratchet_trajectory_results.json
- why_critical: committed result is labeled canonical but lacks TOOL_INTEGRATION_DEPTH.

## META blocker 2026-04-17T13:47:51Z canonical_abuse
- timestamp: 2026-04-17T13:47:51Z
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/xgi_l7_marginal_results.json
- why_critical: committed result is labeled canonical but lacks TOOL_INTEGRATION_DEPTH, load_bearing ladder tool.

## META blocker 2026-04-17T13:47:51Z canonical_abuse
- timestamp: 2026-04-17T13:47:51Z
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/riemannian_curvature_results.json
- why_critical: committed result is labeled canonical but lacks TOOL_INTEGRATION_DEPTH.

## META blocker 2026-04-17T13:47:51Z canonical_abuse
- timestamp: 2026-04-17T13:47:51Z
- class: canonical_abuse
- path: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/e3nn_equivariant_qubits_results.json
- why_critical: committed result is labeled canonical but lacks TOOL_INTEGRATION_DEPTH, load_bearing ladder tool.

## META blocker 2026-04-17T14:11:08Z
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/berry_phase_u1_abelian_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/lego_uhlmann_phase_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing ladder tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/bridge_chain_integration_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/pure_lego_ic_shell_boundary_continuity_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/xgi_shell_hypergraph_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/c2_topology_remaining_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/cvc5_cross_check_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing ladder tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/lego_entropy_inequalities_stability_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH, load_bearing ladder tool
- critical canonical-label abuse: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sa5_curvature_commutator_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T14:57:10Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/berry_curvature_stokes_results.json
- why_critical: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T14:57:10Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/bridge_cvc5_crosscheck_results.json
- why_critical: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T14:57:10Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/bridge_kernel_z3_proof_results.json
- why_critical: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T14:57:10Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/cross_shell_coupling_cp1_bures_results.json
- why_critical: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T14:57:10Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/e3nn_hopf_spinor_equivariance_results.json
- why_critical: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T14:57:10Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/e3nn_relay_equivariance_results.json
- why_critical: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T14:57:10Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/e3nn_tensor_product_results.json
- why_critical: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T14:57:10Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/foundation_channel_constraints_hardway_results.json
- why_critical: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T14:57:10Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/gauss_bonnet_cp1_results.json
- why_critical: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T14:57:10Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/lego_weyl_wigner_phase_space_results.json
- why_critical: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T14:57:10Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/ratchet_optimizer_results.json
- why_critical: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T14:57:10Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/torch_channel_composition_results.json
- why_critical: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T14:57:10Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/torch_phase_damping_results.json
- why_critical: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T14:57:10Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/weyl_hopf_tori_results.json
- why_critical: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## BLOCKER 2026-04-17T08:18:58-07:00 canonical_abuse system_v4/probes/a2_state/sim_results/adversarial_ratchet_results.json
- timestamp: 2026-04-17T08:18:58-07:00
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/adversarial_ratchet_results.json
- why_critical: classification is canonical but TOOL_INTEGRATION_DEPTH is absent and no load-bearing ladder tool is named.

## BLOCKER 2026-04-17T08:18:58-07:00 canonical_abuse system_v4/probes/a2_state/sim_results/bridge_extended_proofs_results.json
- timestamp: 2026-04-17T08:18:58-07:00
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/bridge_extended_proofs_results.json
- why_critical: classification is canonical but TOOL_INTEGRATION_DEPTH is absent and no load-bearing ladder tool is named.

## BLOCKER 2026-04-17T08:18:58-07:00 canonical_abuse system_v4/probes/a2_state/sim_results/lego_lindblad_dissipator_results.json
- timestamp: 2026-04-17T08:18:58-07:00
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/lego_lindblad_dissipator_results.json
- why_critical: classification is canonical but TOOL_INTEGRATION_DEPTH is absent and no load-bearing ladder tool is named.

## BLOCKER 2026-04-17T08:18:58-07:00 canonical_abuse system_v4/probes/a2_state/sim_results/lego_su2_representations_results.json
- timestamp: 2026-04-17T08:18:58-07:00
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/lego_su2_representations_results.json
- why_critical: classification is canonical but TOOL_INTEGRATION_DEPTH is absent and no load-bearing ladder tool is named.

## BLOCKER 2026-04-17T08:18:58-07:00 canonical_abuse system_v4/probes/a2_state/sim_results/stinespring_dilation_results.json
- timestamp: 2026-04-17T08:18:58-07:00
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/stinespring_dilation_results.json
- why_critical: classification is canonical but TOOL_INTEGRATION_DEPTH is absent and no load-bearing ladder tool is named.

## BLOCKER 2026-04-17T08:18:58-07:00 canonical_abuse system_v4/probes/a2_state/sim_results/density_hopf_geometry_results.json
- timestamp: 2026-04-17T08:18:58-07:00
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/density_hopf_geometry_results.json
- why_critical: classification is canonical but TOOL_INTEGRATION_DEPTH is absent and no load-bearing ladder tool is named.

## BLOCKER 2026-04-17T08:18:58-07:00 canonical_abuse system_v4/probes/a2_state/sim_results/hopf_tori_base_results.json
- timestamp: 2026-04-17T08:18:58-07:00
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/hopf_tori_base_results.json
- why_critical: classification is canonical but TOOL_INTEGRATION_DEPTH is absent and no load-bearing ladder tool is named.

## BLOCKER 2026-04-17T08:18:58-07:00 canonical_abuse system_v4/probes/a2_state/sim_results/lego_entanglement_distillation_results.json
- timestamp: 2026-04-17T08:18:58-07:00
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/lego_entanglement_distillation_results.json
- why_critical: classification is canonical but TOOL_INTEGRATION_DEPTH is absent and no load-bearing ladder tool is named.

## BLOCKER 2026-04-17T08:18:58-07:00 canonical_abuse system_v4/probes/a2_state/sim_results/pairwise_shell_coupling_cp1_results.json
- timestamp: 2026-04-17T08:18:58-07:00
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/pairwise_shell_coupling_cp1_results.json
- why_critical: classification is canonical but TOOL_INTEGRATION_DEPTH is absent and no load-bearing ladder tool is named.

## BLOCKER 2026-04-17T08:18:58-07:00 canonical_abuse system_v4/probes/a2_state/sim_results/phi0_shell_global_ablation_results.json
- timestamp: 2026-04-17T08:18:58-07:00
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/phi0_shell_global_ablation_results.json
- why_critical: classification is canonical but TOOL_INTEGRATION_DEPTH is absent and no load-bearing ladder tool is named.

## BLOCKER 2026-04-17T08:18:58-07:00 canonical_abuse system_v4/probes/a2_state/sim_results/wilczek_zee_curvature_results.json
- timestamp: 2026-04-17T08:18:58-07:00
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/wilczek_zee_curvature_results.json
- why_critical: classification is canonical but TOOL_INTEGRATION_DEPTH is absent and no load-bearing ladder tool is named.

## BLOCKER 2026-04-17T08:18:58-07:00 canonical_abuse system_v4/probes/a2_state/sim_results/foundation_equivariant_graph_backprop_results.json
- timestamp: 2026-04-17T08:18:58-07:00
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/foundation_equivariant_graph_backprop_results.json
- why_critical: classification is canonical but TOOL_INTEGRATION_DEPTH is absent and no load-bearing ladder tool is named.

## BLOCKER 2026-04-17T08:18:58-07:00 canonical_abuse system_v4/probes/a2_state/sim_results/layer_stacking_nonprefix_results.json
- timestamp: 2026-04-17T08:18:58-07:00
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/layer_stacking_nonprefix_results.json
- why_critical: classification is canonical but TOOL_INTEGRATION_DEPTH is absent and no load-bearing ladder tool is named.

## BLOCKER 2026-04-17T08:18:58-07:00 canonical_abuse system_v4/probes/a2_state/sim_results/lego_choi_state_duality_results.json
- timestamp: 2026-04-17T08:18:58-07:00
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/lego_choi_state_duality_results.json
- why_critical: classification is canonical but TOOL_INTEGRATION_DEPTH is absent and no load-bearing ladder tool is named.

## BLOCKER 2026-04-17T08:18:58-07:00 canonical_abuse system_v4/probes/a2_state/sim_results/lego_clifford_hierarchy_results.json
- timestamp: 2026-04-17T08:18:58-07:00
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/lego_clifford_hierarchy_results.json
- why_critical: classification is canonical but TOOL_INTEGRATION_DEPTH is absent and no load-bearing ladder tool is named.

## BLOCKER 2026-04-17T08:18:58-07:00 canonical_abuse system_v4/probes/a2_state/sim_results/phase_transition_sweep_results.json
- timestamp: 2026-04-17T08:18:58-07:00
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/phase_transition_sweep_results.json
- why_critical: classification is canonical but TOOL_INTEGRATION_DEPTH is absent and no load-bearing ladder tool is named.

## BLOCKER 2026-04-17T08:18:58-07:00 canonical_abuse system_v4/probes/a2_state/sim_results/3q_ambiguity_expansion_results.json
- timestamp: 2026-04-17T08:18:58-07:00
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/3q_ambiguity_expansion_results.json
- why_critical: classification is canonical but TOOL_INTEGRATION_DEPTH is absent and no load-bearing ladder tool is named.

## BLOCKER 2026-04-17T08:18:58-07:00 canonical_abuse system_v4/probes/a2_state/sim_results/geomstats_shell_metrics_results.json
- timestamp: 2026-04-17T08:18:58-07:00
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/geomstats_shell_metrics_results.json
- why_critical: classification is canonical but TOOL_INTEGRATION_DEPTH is absent and no load-bearing ladder tool is named.

## BLOCKER 2026-04-17T08:18:58-07:00 canonical_abuse system_v4/probes/a2_state/sim_results/hopf_contact_symplectic_bridge_results.json
- timestamp: 2026-04-17T08:18:58-07:00
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/hopf_contact_symplectic_bridge_results.json
- why_critical: classification is canonical but TOOL_INTEGRATION_DEPTH is absent and no load-bearing ladder tool is named.

## BLOCKER 2026-04-17T08:18:58-07:00 canonical_abuse system_v4/probes/a2_state/sim_results/temporal_cascade_results.json
- timestamp: 2026-04-17T08:18:58-07:00
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/temporal_cascade_results.json
- why_critical: classification is canonical but TOOL_INTEGRATION_DEPTH is absent and no load-bearing ladder tool is named.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/3q_ambiguity_expansion_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/3q_ambiguity_expansion_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH, load_bearing ladder tool is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/3qubit_dag_formal_ordering_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/3qubit_dag_formal_ordering_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/3qubit_full_cascade_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/3qubit_full_cascade_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH, load_bearing ladder tool is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/4qubit_cascade_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/4qubit_cascade_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH, load_bearing ladder tool is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/adversarial_ratchet_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/adversarial_ratchet_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH, load_bearing ladder tool is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/axis6_canonical_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/axis6_canonical_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/axis6_e3nn_fe_bridge_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/axis6_e3nn_fe_bridge_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/axis7_12_gs_residual_axes_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/axis7_12_gs_residual_axes_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/axis7_12_orthogonal_closure_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/axis7_12_orthogonal_closure_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/bridge_cut_perturbation_stability_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/bridge_cut_perturbation_stability_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH, load_bearing ladder tool is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/bridge_extended_proofs_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/bridge_extended_proofs_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/bridge_phi0_proof_integration_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/bridge_phi0_proof_integration_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/contact_symplectic_coupling_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/contact_symplectic_coupling_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/contact_symplectic_kahler_coexistence_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/contact_symplectic_kahler_coexistence_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/cvc5_shells_crosscheck_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/cvc5_shells_crosscheck_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/density_hopf_geometry_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/density_hopf_geometry_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/e3nn_ic_invariance_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/e3nn_ic_invariance_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/engine_16_placements_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/engine_16_placements_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/engine_8_terrains_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/engine_8_terrains_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH, load_bearing ladder tool is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/engine_lab_matrix_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/engine_lab_matrix_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH, load_bearing ladder tool is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/foundation_equivariant_graph_backprop_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/foundation_equivariant_graph_backprop_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH, load_bearing ladder tool is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/frozen_kernel_classification_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/frozen_kernel_classification_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/full_ratchet_cascade_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/full_ratchet_cascade_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH, load_bearing ladder tool is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/geomstats_shell_metrics_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/geomstats_shell_metrics_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH, load_bearing ladder tool is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/gnn_cascade_integrated_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/gnn_cascade_integrated_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/hopf_contact_symplectic_bridge_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/hopf_contact_symplectic_bridge_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/hopf_foliation_structure_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/hopf_foliation_structure_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/hopf_tori_base_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/hopf_tori_base_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/information_geometry_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/information_geometry_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH, load_bearing ladder tool is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/layer_coupling_matrix_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/layer_coupling_matrix_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/layer_coupling_matrix_v2_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/layer_coupling_matrix_v2_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/layer_coupling_matrix_v3_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/layer_coupling_matrix_v3_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/layer_stacking_coexistence_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/layer_stacking_coexistence_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/layer_stacking_nonprefix_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/layer_stacking_nonprefix_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/layer_triple_catalog_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/layer_triple_catalog_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/layered_foundation_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/layered_foundation_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH, load_bearing ladder tool is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/lego_choi_state_duality_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/lego_choi_state_duality_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/lego_clifford_hierarchy_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/lego_clifford_hierarchy_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH, load_bearing ladder tool is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/lego_coherent_info_advanced_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/lego_coherent_info_advanced_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH, load_bearing ladder tool is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/lego_entanglement_distillation_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/lego_entanglement_distillation_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH, load_bearing ladder tool is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/lego_lindblad_dissipator_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/lego_lindblad_dissipator_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/lego_povm_measurement_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/lego_povm_measurement_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/lego_su2_representations_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/lego_su2_representations_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH, load_bearing ladder tool is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/lorentzian_geometry_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/lorentzian_geometry_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH, load_bearing ladder tool is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/pairwise_shell_coupling_cp1_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/pairwise_shell_coupling_cp1_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/phase7_baseline_validation_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/phase7_baseline_validation_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/phase7_divergence_analysis_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/phase7_divergence_analysis_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH, load_bearing ladder tool is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/phase_damping_fixed_point_geometry_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/phase_damping_fixed_point_geometry_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/phase_transition_sweep_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/phase_transition_sweep_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH, load_bearing ladder tool is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/phi0_packet_robustness_audit_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/phi0_packet_robustness_audit_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH, load_bearing ladder tool is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/phi0_shell_global_ablation_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/phi0_shell_global_ablation_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH, load_bearing ladder tool is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/pyg_dynamic_edge_werner_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/pyg_dynamic_edge_werner_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/qit_engine_companion_array_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/qit_engine_companion_array_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH, load_bearing ladder tool is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/stinespring_dilation_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/stinespring_dilation_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/temporal_cascade_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/temporal_cascade_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH, load_bearing ladder tool is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/tools_load_bearing_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/tools_load_bearing_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/torch_constraint_shells_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/torch_constraint_shells_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH, load_bearing ladder tool is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/torch_constraint_shells_v2_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/torch_constraint_shells_v2_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/torch_gnn_directional_gate_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/torch_gnn_directional_gate_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/torch_ratchet_gnn_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/torch_ratchet_gnn_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/torch_shells_gradient_flow_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/torch_shells_gradient_flow_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/twilight_zone_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/twilight_zone_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH, load_bearing ladder tool is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/werner_manifold_scan_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/werner_manifold_scan_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/weyl_spinor_hopf_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/weyl_spinor_hopf_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/weyl_two_model_crosscheck_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/weyl_two_model_crosscheck_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/wilczek_zee_curvature_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/wilczek_zee_curvature_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/wilczek_zee_holonomy_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/wilczek_zee_holonomy_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/z3_channel_boundary_theorem_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/z3_channel_boundary_theorem_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/z3_channel_composition_boundary_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/z3_channel_composition_boundary_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## Blocker 2026-04-17T16:07:36Z canonical_abuse system_v4/probes/a2_state/sim_results/z3_quantum_capacity_bound_results.json
- timestamp: 2026-04-17T16:07:36Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/z3_quantum_capacity_bound_results.json
- why_critical: classification canonical is present but TOOL_INTEGRATION_DEPTH is absent under the Tier META contract.

## META blocker 2026-04-17T16:31:44Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/sim_lego_entropy_relative_js_results.json
- why_critical: classification canonical without TOOL_INTEGRATION_DEPTH and without a load-bearing ladder tool

## META blocker 2026-04-17T16:31:44Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/sim_lego_entropy_shell_history_weighted_results.json
- why_critical: classification canonical without TOOL_INTEGRATION_DEPTH and without a load-bearing ladder tool

## META blocker 2026-04-17T16:31:44Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/sim_negative_bridge_cut_counterfeits_results.json
- why_critical: classification canonical without TOOL_INTEGRATION_DEPTH and without a load-bearing ladder tool

## META blocker 2026-04-17T16:31:44Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/sim_negative_global_shell_bridge_counterfeits_results.json
- why_critical: classification canonical without TOOL_INTEGRATION_DEPTH and without a load-bearing ladder tool

## BLOCKER 2026-04-17T17:45:39Z canonical_abuse
- class: critical
- path: system_v4/probes/a2_state/sim_results/channel_space_geometry_results.json
- why: classification is canonical but the uppercase TOOL_INTEGRATION_DEPTH contract is absent and no ladder tool is load_bearing.

## BLOCKER 2026-04-17T17:45:39Z canonical_abuse
- class: critical
- path: system_v4/probes/a2_state/sim_results/cirq_matrix_state_bridge_results.json
- why: classification is canonical but the uppercase TOOL_INTEGRATION_DEPTH contract is absent and no named ladder tool is load_bearing.

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/adiabatic_berry_dynamics_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/adiabatic_berry_dynamics_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/contact_structure_s3_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/contact_structure_s3_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/contact_symplectic_coupling_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/contact_symplectic_coupling_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/contact_symplectic_kahler_coexistence_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/contact_symplectic_kahler_coexistence_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/geodesic_deviation_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/geodesic_deviation_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/hopf_contact_symplectic_bridge_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/hopf_contact_symplectic_bridge_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/information_geometry_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/information_geometry_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/layer_coupling_matrix_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/layer_coupling_matrix_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/layer_coupling_matrix_v2_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/layer_coupling_matrix_v2_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/layer_coupling_matrix_v3_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/layer_coupling_matrix_v3_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/layered_foundation_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/layered_foundation_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/lego_coherent_info_advanced_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/lego_coherent_info_advanced_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/lego_entanglement_distillation_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/lego_entanglement_distillation_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/lego_entropy_bipartite_cut_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/lego_entropy_bipartite_cut_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/lego_entropy_extremal_density_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/lego_entropy_extremal_density_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/lego_entropy_inequalities_stability_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/lego_entropy_inequalities_stability_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/lego_entropy_multipartite_cuts_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/lego_entropy_multipartite_cuts_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/lego_entropy_smooth_one_shot_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/lego_entropy_smooth_one_shot_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/lego_entropy_spectral_families_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/lego_entropy_spectral_families_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/lego_su2_representations_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/lego_su2_representations_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/lego_uhlmann_phase_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/lego_uhlmann_phase_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/lego_weyl_wigner_phase_space_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/lego_weyl_wigner_phase_space_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/lego_zeno_speed_limits_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/lego_zeno_speed_limits_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/local_operator_action_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/local_operator_action_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/lorentzian_geometry_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/lorentzian_geometry_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/phase7_divergence_analysis_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/phase7_divergence_analysis_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/phase_transition_sweep_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/phase_transition_sweep_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/phi0_packet_robustness_audit_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/phi0_packet_robustness_audit_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/phi0_shell_global_ablation_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/phi0_shell_global_ablation_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/pure_lego_hypothesis_testing_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/pure_lego_hypothesis_testing_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/pure_lego_ic_shell_boundary_continuity_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/pure_lego_ic_shell_boundary_continuity_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/qfi_killpoint_divergence_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/qfi_killpoint_divergence_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/ratchet_optimizer_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/ratchet_optimizer_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/riemannian_curvature_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/riemannian_curvature_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/sa10_wilczek_zee_curvature_boundary_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/sa10_wilczek_zee_curvature_boundary_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/sim_lego_entropy_relative_js_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/sim_lego_entropy_relative_js_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/sim_lego_entropy_shell_history_weighted_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/sim_lego_entropy_shell_history_weighted_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/sim_negative_bridge_cut_counterfeits_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/sim_negative_bridge_cut_counterfeits_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/sim_negative_global_shell_bridge_counterfeits_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/sim_negative_global_shell_bridge_counterfeits_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/stinespring_dilation_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/stinespring_dilation_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/wilczek_zee_curvature_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/wilczek_zee_curvature_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/wilczek_zee_holonomy_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/wilczek_zee_holonomy_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/3q_ambiguity_expansion_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/3q_ambiguity_expansion_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/3qubit_full_cascade_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/3qubit_full_cascade_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/4qubit_cascade_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/4qubit_cascade_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/adversarial_ratchet_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/adversarial_ratchet_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/axis6_e3nn_fe_bridge_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/axis6_e3nn_fe_bridge_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/bridge_cut_perturbation_stability_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/bridge_cut_perturbation_stability_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/bridge_entropy_inequality_guardrails_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/bridge_entropy_inequality_guardrails_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/bridge_phi0_proof_integration_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/bridge_phi0_proof_integration_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/c2_topology_remaining_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/c2_topology_remaining_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/channel_space_geometry_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/channel_space_geometry_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/chiral_density_bookkeeping_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/chiral_density_bookkeeping_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/coherent_information_measure_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/coherent_information_measure_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/conditional_entropy_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/conditional_entropy_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/cvc5_cross_check_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/cvc5_cross_check_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/e3nn_equivariant_qubits_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/e3nn_equivariant_qubits_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/engine_16_placements_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/engine_16_placements_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/engine_8_terrains_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/engine_8_terrains_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/fiber_loop_law_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/fiber_loop_law_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/foundation_channel_constraints_hardway_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/foundation_channel_constraints_hardway_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/foundation_equivariant_graph_backprop_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/foundation_equivariant_graph_backprop_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/full_ratchet_cascade_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/full_ratchet_cascade_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/geomstats_frechet_mean_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/geomstats_frechet_mean_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/graph_geometry_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/graph_geometry_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## Blocker 2026-04-17T18:09:57Z canonical_abuse system_v4/probes/a2_state/sim_results/classical_maxwell_demon_information_accounting_results.json
- timestamp: 2026-04-17T18:09:57Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/classical_maxwell_demon_information_accounting_results.json
- why_critical: classification canonical in new result commit but missing TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool

## META blocker 2026-04-17T18:33:19Z canonical_abuse
- timestamp: 2026-04-17T18:33:19Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/clifford_so_homomorphism_results.json
- why_critical: critical because classification canonical lacks TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T18:33:19Z canonical_abuse
- timestamp: 2026-04-17T18:33:19Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/lego_entropy_extremal_density_results.json
- why_critical: critical because classification canonical lacks TOOL_INTEGRATION_DEPTH and lacks a load-bearing ladder tool

## META blocker 2026-04-17T18:33:19Z canonical_abuse
- timestamp: 2026-04-17T18:33:19Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/lego_entropy_smooth_one_shot_results.json
- why_critical: critical because classification canonical lacks TOOL_INTEGRATION_DEPTH and lacks a load-bearing ladder tool

## META blocker 2026-04-17T18:33:19Z canonical_abuse
- timestamp: 2026-04-17T18:33:19Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/sa10_wilczek_zee_curvature_boundary_results.json
- why_critical: critical because classification canonical lacks TOOL_INTEGRATION_DEPTH and lacks a load-bearing ladder tool

## META blocker 2026-04-17T18:33:19Z canonical_abuse
- timestamp: 2026-04-17T18:33:19Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/SA12_wilczek_zee_curvature_sympy_results.json
- why_critical: critical because classification canonical lacks TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T18:33:19Z canonical_abuse
- timestamp: 2026-04-17T18:33:19Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/fiber_loop_law_results.json
- why_critical: critical because classification canonical lacks TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T18:33:19Z canonical_abuse
- timestamp: 2026-04-17T18:33:19Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/hopf_fiber_equivalence_results.json
- why_critical: critical because classification canonical lacks TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T18:33:19Z canonical_abuse
- timestamp: 2026-04-17T18:33:19Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/lego_entropy_spectral_families_results.json
- why_critical: critical because classification canonical lacks TOOL_INTEGRATION_DEPTH and lacks a load-bearing ladder tool

## META blocker 2026-04-17T18:33:19Z canonical_abuse
- timestamp: 2026-04-17T18:33:19Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/weyl_geometry_ladder_audit_results.json
- why_critical: critical because classification canonical lacks TOOL_INTEGRATION_DEPTH and lacks a load-bearing ladder tool

## META blocker 2026-04-17T18:33:19Z canonical_abuse
- timestamp: 2026-04-17T18:33:19Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/circuit_unitary_canonicalization_z3_results.json
- why_critical: critical because classification canonical lacks TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T18:33:19Z canonical_abuse
- timestamp: 2026-04-17T18:33:19Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/variational_quantum_bridge_pytorch_results.json
- why_critical: critical because classification canonical lacks TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T18:33:19Z canonical_abuse
- timestamp: 2026-04-17T18:33:19Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/temporal_cascade_results.json
- why_critical: critical because classification canonical lacks TOOL_INTEGRATION_DEPTH and lacks a load-bearing ladder tool

## META blocker 2026-04-17T18:33:19Z canonical_abuse
- timestamp: 2026-04-17T18:33:19Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/tensor_network_spinor_torus_results.json
- why_critical: critical because classification canonical lacks TOOL_INTEGRATION_DEPTH and lacks a load-bearing ladder tool

## META blocker 2026-04-17T18:58:55Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/c2_topology_expansion_results.json
- why_critical: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T18:58:55Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/chiral_density_bookkeeping_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T18:58:55Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/geomstats_ratchet_trajectory_results.json
- why_critical: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T18:58:55Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/xgi_l7_marginal_results.json
- why_critical: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T18:58:55Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/e3nn_equivariant_qubits_results.json
- why_critical: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T18:58:55Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/riemannian_curvature_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T18:58:55Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/bridge_entropy_inequality_guardrails_results.json
- why_critical: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T18:58:55Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/clifford_weyl_transport_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T18:58:55Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/z3_dephasing_symmetry_guard_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T18:58:55Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/lego_entropy_bipartite_cut_results.json
- why_critical: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T18:58:55Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/rustworkx_capability_results.json
- why_critical: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T18:58:55Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/bridge_to_rhoab_construction_results.json
- why_critical: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T18:58:55Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/frame_bundle_structure_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T18:58:55Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/torsion_curvature_splitting_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T19:20:03Z
- critical canonical-label abuse: system_v4/probes/a2_state/sim_results/bridge_z3_kernel_ordering_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: system_v4/probes/a2_state/sim_results/lego_entropy_multipartite_cuts_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH|load_bearing_ladder_tool
- critical canonical-label abuse: system_v4/probes/a2_state/sim_results/adiabatic_berry_dynamics_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH|load_bearing_ladder_tool
- critical canonical-label abuse: system_v4/probes/a2_state/sim_results/gudhi_bridge_persistence_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: system_v4/probes/a2_state/sim_results/qfi_killpoint_divergence_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: system_v4/probes/a2_state/sim_results/toponetx_state_class_binding_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: system_v4/probes/a2_state/sim_results/z3_dpi_proof_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: system_v4/probes/a2_state/sim_results/berry_phase_u1_abelian_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: system_v4/probes/a2_state/sim_results/bridge_chain_integration_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: system_v4/probes/a2_state/sim_results/lego_uhlmann_phase_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH|load_bearing_ladder_tool
- critical canonical-label abuse: system_v4/probes/a2_state/sim_results/pure_lego_ic_shell_boundary_continuity_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: system_v4/probes/a2_state/sim_results/c2_topology_remaining_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH|load_bearing_ladder_tool
- critical canonical-label abuse: system_v4/probes/a2_state/sim_results/cvc5_cross_check_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH|load_bearing_ladder_tool
- critical canonical-label abuse: system_v4/probes/a2_state/sim_results/lego_entropy_inequalities_stability_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH|load_bearing_ladder_tool
- critical canonical-label abuse: system_v4/probes/a2_state/sim_results/sa5_curvature_commutator_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH
- critical canonical-label abuse: system_v4/probes/a2_state/sim_results/weyl_geometry_translation_targets_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH|load_bearing_ladder_tool
- critical canonical-label abuse: system_v4/probes/a2_state/sim_results/xgi_shell_hypergraph_results.json — canonical result lacks TOOL_INTEGRATION_DEPTH|load_bearing_ladder_tool

## META blocker 2026-04-17T19:20:03Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/bridge_z3_kernel_ordering_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T19:20:03Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/lego_entropy_multipartite_cuts_results.json
- why_critical: TOOL_INTEGRATION_DEPTH|load_bearing_ladder_tool

## META blocker 2026-04-17T19:20:03Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/adiabatic_berry_dynamics_results.json
- why_critical: TOOL_INTEGRATION_DEPTH|load_bearing_ladder_tool

## META blocker 2026-04-17T19:20:03Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/gudhi_bridge_persistence_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T19:20:03Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/qfi_killpoint_divergence_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T19:20:03Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/toponetx_state_class_binding_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T19:20:03Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/z3_dpi_proof_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T19:20:03Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/berry_phase_u1_abelian_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T19:20:03Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/bridge_chain_integration_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T19:20:03Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/lego_uhlmann_phase_results.json
- why_critical: TOOL_INTEGRATION_DEPTH|load_bearing_ladder_tool

## META blocker 2026-04-17T19:20:03Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/pure_lego_ic_shell_boundary_continuity_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T19:20:03Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/c2_topology_remaining_results.json
- why_critical: TOOL_INTEGRATION_DEPTH|load_bearing_ladder_tool

## META blocker 2026-04-17T19:20:03Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/cvc5_cross_check_results.json
- why_critical: TOOL_INTEGRATION_DEPTH|load_bearing_ladder_tool

## META blocker 2026-04-17T19:20:03Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/lego_entropy_inequalities_stability_results.json
- why_critical: TOOL_INTEGRATION_DEPTH|load_bearing_ladder_tool

## META blocker 2026-04-17T19:20:03Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/sa5_curvature_commutator_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T19:20:03Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/weyl_geometry_translation_targets_results.json
- why_critical: TOOL_INTEGRATION_DEPTH|load_bearing_ladder_tool

## META blocker 2026-04-17T19:20:03Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/xgi_shell_hypergraph_results.json
- why_critical: TOOL_INTEGRATION_DEPTH|load_bearing_ladder_tool

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/a2_state/sim_results/3q_ambiguity_expansion_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/3q_ambiguity_expansion_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/a2_state/sim_results/berry_curvature_stokes_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/berry_curvature_stokes_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/a2_state/sim_results/bridge_cvc5_crosscheck_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/bridge_cvc5_crosscheck_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/a2_state/sim_results/bridge_kernel_z3_proof_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/bridge_kernel_z3_proof_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/a2_state/sim_results/bridge_z3_kernel_ordering_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/bridge_z3_kernel_ordering_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/a2_state/sim_results/cross_shell_coupling_cp1_bures_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/cross_shell_coupling_cp1_bures_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/a2_state/sim_results/cvc5_amplitude_damping_boundary_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/cvc5_amplitude_damping_boundary_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/a2_state/sim_results/e3nn_hopf_spinor_equivariance_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/e3nn_hopf_spinor_equivariance_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/a2_state/sim_results/e3nn_relay_equivariance_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/e3nn_relay_equivariance_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/a2_state/sim_results/e3nn_tensor_product_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/e3nn_tensor_product_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/a2_state/sim_results/foundation_channel_constraints_hardway_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/foundation_channel_constraints_hardway_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/a2_state/sim_results/foundation_equivariant_graph_backprop_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/foundation_equivariant_graph_backprop_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/a2_state/sim_results/gauss_bonnet_cp1_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/gauss_bonnet_cp1_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/a2_state/sim_results/geodesic_deviation_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/geodesic_deviation_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/a2_state/sim_results/geomstats_frechet_mean_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/geomstats_frechet_mean_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/a2_state/sim_results/geomstats_shell_metrics_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/geomstats_shell_metrics_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/a2_state/sim_results/hopf_contact_symplectic_bridge_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/hopf_contact_symplectic_bridge_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/a2_state/sim_results/lego_choi_state_duality_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/lego_choi_state_duality_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/a2_state/sim_results/lego_entropy_multipartite_cuts_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/lego_entropy_multipartite_cuts_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/a2_state/sim_results/lego_weyl_wigner_phase_space_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/lego_weyl_wigner_phase_space_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/a2_state/sim_results/lego_zeno_speed_limits_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/lego_zeno_speed_limits_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/a2_state/sim_results/pure_lego_hypothesis_testing_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/pure_lego_hypothesis_testing_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/a2_state/sim_results/ratchet_optimizer_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/ratchet_optimizer_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/a2_state/sim_results/temporal_cascade_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/temporal_cascade_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/a2_state/sim_results/tensor_network_spinor_torus_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/tensor_network_spinor_torus_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/a2_state/sim_results/torch_hopf_connection_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/torch_hopf_connection_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/sim_results/engine_4_operators_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/sim_results/engine_4_operators_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/sim_results/engine_terrain_couplings_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/sim_results/engine_terrain_couplings_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/sim_results/geom_2qubit_s7_cp3_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/sim_results/geom_2qubit_s7_cp3_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/sim_results/geom_metric_layers_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/sim_results/geom_metric_layers_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/sim_results/geom_symplectic_kahler_contact_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/sim_results/geom_symplectic_kahler_contact_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/sim_results/lego_adiabatic_theorem_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/sim_results/lego_adiabatic_theorem_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/sim_results/lego_dirac_gamma_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/sim_results/lego_dirac_gamma_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/sim_results/lego_dynamical_decoupling_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/sim_results/lego_dynamical_decoupling_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/sim_results/lego_fiber_bundles_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/sim_results/lego_fiber_bundles_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/sim_results/lego_flux_candidates_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/sim_results/lego_flux_candidates_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/sim_results/lego_gksl_kossakowski_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/sim_results/lego_gksl_kossakowski_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/sim_results/lego_info_geometry_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/sim_results/lego_info_geometry_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/sim_results/lego_lindblad_spectral_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/sim_results/lego_lindblad_spectral_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/sim_results/lego_pauli_algebra_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/sim_results/lego_pauli_algebra_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/sim_results/lego_positive_maps_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/sim_results/lego_positive_maps_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/sim_results/lego_qit_batch_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/sim_results/lego_qit_batch_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/sim_results/lego_quantum_capacities_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/sim_results/lego_quantum_capacities_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/sim_results/lego_quantum_thermo_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/sim_results/lego_quantum_thermo_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/sim_results/lego_quantum_trajectories_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/sim_results/lego_quantum_trajectories_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/sim_results/lego_stagewise_deltas_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/sim_results/lego_stagewise_deltas_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/sim_results/lego_stinespring_complementary_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/sim_results/lego_stinespring_complementary_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/sim_results/lego_toric_code_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/sim_results/lego_toric_code_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/sim_results/lego_unitary_generators_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/sim_results/lego_unitary_generators_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/sim_results/lego_wilczek_zee_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/sim_results/lego_wilczek_zee_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/sim_results/meta_learning_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/sim_results/meta_learning_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/sim_results/qec_ratchet_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/sim_results/qec_ratchet_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/sim_results/temporal_cascade_flipped_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/sim_results/temporal_cascade_flipped_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool.

## Blocker 2026-04-17T19:43:42Z — canonical_abuse — system_v4/probes/sim_results/vqe_ratchet_results.json
- timestamp: 2026-04-17T19:43:42Z
- class: canonical_abuse
- path/commit: system_v4/probes/sim_results/vqe_ratchet_results.json
- why_critical: classification canonical without required TOOL_INTEGRATION_DEPTH contract and/or without a load-bearing ladder tool. Missing: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool.

## META blocker 2026-04-17T20:11:10Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/3qubit_dag_formal_ordering_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T20:11:10Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/bridge_cut_perturbation_stability_results.json
- why_critical: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T20:11:10Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/density_hopf_geometry_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T20:11:10Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/layered_foundation_results.json
- why_critical: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T20:11:10Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/lorentzian_geometry_results.json
- why_critical: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T20:11:10Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/twilight_zone_results.json
- why_critical: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T20:11:10Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/weyl_spinor_hopf_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T20:11:10Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/axis7_12_gs_residual_axes_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T20:11:10Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/axis7_12_orthogonal_closure_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T20:11:10Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/engine_16_placements_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T20:11:10Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/phi0_packet_robustness_audit_results.json
- why_critical: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T20:11:10Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/weyl_nested_shell_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T20:11:10Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/z3_channel_boundary_theorem_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T20:11:10Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/axis6_e3nn_fe_bridge_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T20:11:10Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/contact_symplectic_coupling_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T20:11:10Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/cvc5_shells_crosscheck_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T20:11:10Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/weyl_two_model_crosscheck_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T20:11:10Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/wilczek_zee_holonomy_results.json
- why_critical: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T20:11:10Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/z3_quantum_capacity_bound_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T20:11:10Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/adversarial_ratchet_results.json
- why_critical: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T20:11:10Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/sim_results/lego_qit_batch_results.json
- why_critical: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T20:11:10Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/sim_results/meta_learning_results.json
- why_critical: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T20:11:10Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/bridge_extended_proofs_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T20:11:10Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/hopf_tori_base_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T20:11:10Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/lego_entanglement_distillation_results.json
- why_critical: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T20:11:10Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/lego_lindblad_dissipator_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T20:11:10Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/lego_su2_representations_results.json
- why_critical: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T20:11:10Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/pairwise_shell_coupling_cp1_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T20:11:10Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/phi0_shell_global_ablation_results.json
- why_critical: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T20:11:10Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/stinespring_dilation_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T20:11:10Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/wilczek_zee_curvature_results.json
- why_critical: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T20:11:10Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/sim_results/geom_metric_layers_results.json
- why_critical: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T20:11:10Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/sim_results/lego_quantum_capacities_results.json
- why_critical: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T20:11:10Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/sim_results/lego_quantum_trajectories_results.json
- why_critical: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T20:11:10Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/sim_results/lego_unitary_generators_results.json
- why_critical: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T20:11:10Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/sim_results/temporal_cascade_flipped_results.json
- why_critical: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T20:11:10Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/foundation_equivariant_graph_backprop_results.json
- why_critical: TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T20:11:10Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/hopf_contact_symplectic_bridge_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T20:11:10Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/lego_choi_state_duality_results.json
- why_critical: TOOL_INTEGRATION_DEPTH

## BLOCKER 2026-04-17T20:38:11Z canonical_abuse system_v4/probes/a2_state/sim_results/sim_lego_entropy_relative_js_results.json
- timestamp: 2026-04-17T20:38:11Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/sim_lego_entropy_relative_js_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T20:38:11Z canonical_abuse system_v4/probes/a2_state/sim_results/sim_lego_entropy_shell_history_weighted_results.json
- timestamp: 2026-04-17T20:38:11Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/sim_lego_entropy_shell_history_weighted_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T20:38:11Z canonical_abuse system_v4/probes/a2_state/sim_results/sim_negative_bridge_cut_counterfeits_results.json
- timestamp: 2026-04-17T20:38:11Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/sim_negative_bridge_cut_counterfeits_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T20:38:11Z canonical_abuse system_v4/probes/a2_state/sim_results/sim_negative_global_shell_bridge_counterfeits_results.json
- timestamp: 2026-04-17T20:38:11Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/sim_negative_global_shell_bridge_counterfeits_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T20:38:11Z canonical_abuse system_v4/probes/sim_results/engine_terrain_couplings_results.json
- timestamp: 2026-04-17T20:38:11Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/sim_results/engine_terrain_couplings_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T20:38:11Z canonical_abuse system_v4/probes/sim_results/lego_dynamical_decoupling_results.json
- timestamp: 2026-04-17T20:38:11Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/sim_results/lego_dynamical_decoupling_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T20:38:11Z canonical_abuse system_v4/probes/sim_results/lego_gksl_kossakowski_results.json
- timestamp: 2026-04-17T20:38:11Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/sim_results/lego_gksl_kossakowski_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T20:38:11Z canonical_abuse system_v4/probes/sim_results/lego_lindblad_spectral_results.json
- timestamp: 2026-04-17T20:38:11Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/sim_results/lego_lindblad_spectral_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T20:38:11Z canonical_abuse system_v4/probes/sim_results/lego_pauli_algebra_results.json
- timestamp: 2026-04-17T20:38:11Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/sim_results/lego_pauli_algebra_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T20:38:11Z canonical_abuse system_v4/probes/sim_results/lego_quantum_thermo_results.json
- timestamp: 2026-04-17T20:38:11Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/sim_results/lego_quantum_thermo_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T20:38:11Z canonical_abuse system_v4/probes/sim_results/lego_stinespring_complementary_results.json
- timestamp: 2026-04-17T20:38:11Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/sim_results/lego_stinespring_complementary_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T20:38:11Z canonical_abuse system_v4/probes/sim_results/lego_toric_code_results.json
- timestamp: 2026-04-17T20:38:11Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/sim_results/lego_toric_code_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T20:38:11Z canonical_abuse system_v4/probes/sim_results/qec_ratchet_results.json
- timestamp: 2026-04-17T20:38:11Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/sim_results/qec_ratchet_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T20:38:11Z canonical_abuse system_v4/probes/a2_state/sim_results/3qubit_full_cascade_results.json
- timestamp: 2026-04-17T20:38:11Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/3qubit_full_cascade_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T20:38:11Z canonical_abuse system_v4/probes/a2_state/sim_results/4qubit_cascade_results.json
- timestamp: 2026-04-17T20:38:11Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/4qubit_cascade_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T20:38:11Z canonical_abuse system_v4/probes/a2_state/sim_results/axis6_canonical_results.json
- timestamp: 2026-04-17T20:38:11Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/axis6_canonical_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T20:38:11Z canonical_abuse system_v4/probes/a2_state/sim_results/bridge_phi0_proof_integration_results.json
- timestamp: 2026-04-17T20:38:11Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/bridge_phi0_proof_integration_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T20:38:11Z canonical_abuse system_v4/probes/a2_state/sim_results/full_ratchet_cascade_results.json
- timestamp: 2026-04-17T20:38:11Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/full_ratchet_cascade_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T20:38:11Z canonical_abuse system_v4/probes/a2_state/sim_results/information_geometry_results.json
- timestamp: 2026-04-17T20:38:11Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/information_geometry_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T20:38:11Z canonical_abuse system_v4/probes/a2_state/sim_results/layer_coupling_matrix_results.json
- timestamp: 2026-04-17T20:38:11Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/layer_coupling_matrix_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T20:38:11Z canonical_abuse system_v4/probes/a2_state/sim_results/layer_coupling_matrix_v2_results.json
- timestamp: 2026-04-17T20:38:11Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/layer_coupling_matrix_v2_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T20:38:11Z canonical_abuse system_v4/probes/a2_state/sim_results/layer_coupling_matrix_v3_results.json
- timestamp: 2026-04-17T20:38:11Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/layer_coupling_matrix_v3_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T20:38:11Z canonical_abuse system_v4/probes/a2_state/sim_results/layer_triple_catalog_results.json
- timestamp: 2026-04-17T20:38:11Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/layer_triple_catalog_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T20:38:11Z canonical_abuse system_v4/probes/a2_state/sim_results/phase7_baseline_validation_results.json
- timestamp: 2026-04-17T20:38:11Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/phase7_baseline_validation_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T20:38:11Z canonical_abuse system_v4/probes/a2_state/sim_results/tools_load_bearing_results.json
- timestamp: 2026-04-17T20:38:11Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/tools_load_bearing_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T20:38:11Z canonical_abuse system_v4/probes/a2_state/sim_results/torch_constraint_shells_results.json
- timestamp: 2026-04-17T20:38:11Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/torch_constraint_shells_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T20:38:11Z canonical_abuse system_v4/probes/a2_state/sim_results/torch_constraint_shells_v2_results.json
- timestamp: 2026-04-17T20:38:11Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/torch_constraint_shells_v2_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T20:38:11Z canonical_abuse system_v4/probes/a2_state/sim_results/z3_channel_composition_boundary_results.json
- timestamp: 2026-04-17T20:38:11Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/z3_channel_composition_boundary_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T20:38:11Z canonical_abuse system_v4/probes/a2_state/sim_results/contact_symplectic_kahler_coexistence_results.json
- timestamp: 2026-04-17T20:38:11Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/contact_symplectic_kahler_coexistence_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T20:38:11Z canonical_abuse system_v4/probes/a2_state/sim_results/e3nn_ic_invariance_results.json
- timestamp: 2026-04-17T20:38:11Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/e3nn_ic_invariance_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T20:38:11Z canonical_abuse system_v4/probes/a2_state/sim_results/engine_8_terrains_results.json
- timestamp: 2026-04-17T20:38:11Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/engine_8_terrains_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T20:38:11Z canonical_abuse system_v4/probes/a2_state/sim_results/frozen_kernel_classification_results.json
- timestamp: 2026-04-17T20:38:11Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/frozen_kernel_classification_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T20:38:11Z canonical_abuse system_v4/probes/a2_state/sim_results/hopf_foliation_structure_results.json
- timestamp: 2026-04-17T20:38:11Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/hopf_foliation_structure_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T20:38:11Z canonical_abuse system_v4/probes/a2_state/sim_results/lego_coherent_info_advanced_results.json
- timestamp: 2026-04-17T20:38:11Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/lego_coherent_info_advanced_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T20:38:11Z canonical_abuse system_v4/probes/a2_state/sim_results/lego_povm_measurement_results.json
- timestamp: 2026-04-17T20:38:11Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/lego_povm_measurement_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T20:38:11Z canonical_abuse system_v4/probes/a2_state/sim_results/phase7_divergence_analysis_results.json
- timestamp: 2026-04-17T20:38:11Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/phase7_divergence_analysis_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T20:38:11Z canonical_abuse system_v4/probes/a2_state/sim_results/phase_damping_fixed_point_geometry_results.json
- timestamp: 2026-04-17T20:38:11Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/phase_damping_fixed_point_geometry_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T20:38:11Z canonical_abuse system_v4/probes/a2_state/sim_results/torch_ratchet_gnn_results.json
- timestamp: 2026-04-17T20:38:11Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/torch_ratchet_gnn_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T20:38:11Z canonical_abuse system_v4/probes/a2_state/sim_results/torch_shells_gradient_flow_results.json
- timestamp: 2026-04-17T20:38:11Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/torch_shells_gradient_flow_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T20:38:11Z canonical_abuse system_v4/probes/a2_state/sim_results/gnn_cascade_integrated_results.json
- timestamp: 2026-04-17T20:38:11Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/gnn_cascade_integrated_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z banned_verbs /Users/joshuaeisenhart/wiki/harness/agent-spawn-template.md:9
- timestamp: 2026-04-17T21:06:08Z
- class: banned_verbs
- path_or_commit: /Users/joshuaeisenhart/wiki/harness/agent-spawn-template.md:9
- why_critical: harness narrative prose used prohibited wording in live harness prose.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/assoc_bundle_hopf_frame_bundle_carrier_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/assoc_bundle_hopf_frame_bundle_carrier_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/autograd_implicit_diff_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/autograd_implicit_diff_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/autograd_kraus_purity_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/autograd_kraus_purity_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/autograd_ntk_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/autograd_ntk_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/autograd_svd_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/autograd_svd_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/axis_couple_0_4_entropy_x_loop_ordering_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/axis_couple_0_4_entropy_x_loop_ordering_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/axis_couple_0_6_entropy_gradient_x_action_orientation_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/axis_couple_0_6_entropy_gradient_x_action_orientation_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/axis_couple_6_1_action_x_curvature_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/axis_couple_6_1_action_x_curvature_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/boundary_flux_to_pauli_admissibility_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/boundary_flux_to_pauli_admissibility_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/boundary_hopf_to_weyl_admissibility_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/boundary_hopf_to_weyl_admissibility_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/boundary_weyl_to_flux_admissibility_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/boundary_weyl_to_flux_admissibility_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/branch_weight_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/branch_weight_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/bridge_carnot_admissibility_fence_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/bridge_carnot_admissibility_fence_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/bridge_hopf_u1_equivariance_e3nn_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/bridge_hopf_u1_equivariance_e3nn_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/bridge_jarzynski_probe_relative_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/bridge_jarzynski_probe_relative_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/bridge_ladder_L11_placement_z3_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/bridge_ladder_L11_placement_z3_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/bridge_szilard_landauer_floor_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/bridge_szilard_landauer_floor_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/bridge_weyl_cl3_rotor_chirality_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/bridge_weyl_cl3_rotor_chirality_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/cirq_capability_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/cirq_capability_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/commutative_geometry_collapse_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/commutative_geometry_collapse_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/cross_fep_x_igt_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/cross_fep_x_igt_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/cross_fep_x_science_method_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/cross_fep_x_science_method_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/cross_holodeck_x_igt_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/cross_holodeck_x_igt_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/cross_science_method_x_leviathan_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/cross_science_method_x_leviathan_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/discrete_axis0_field_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/discrete_axis0_field_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/f01_cross_09_z3_cvc5_parity_probe_bound_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/f01_cross_09_z3_cvc5_parity_probe_bound_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/f01n01_couple_indistinguishable_saturates_probe_capacity_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/f01n01_couple_indistinguishable_saturates_probe_capacity_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/fep_atom_1_carrier_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/fep_atom_1_carrier_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/fep_atom_4_admissibility_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/fep_atom_4_admissibility_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/fep_atom_5_distinguishability_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/fep_atom_5_distinguishability_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/fep_atom_7_coupling_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/fep_atom_7_coupling_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/fep_deep_active_inference_gradient_flow_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/fep_deep_active_inference_gradient_flow_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/fep_pair_active_inference_x_markov_blanket_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/fep_pair_active_inference_x_markov_blanket_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/fep_pair_fep_minimization_x_g_reduction_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/fep_pair_fep_minimization_x_g_reduction_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/fep_pair_free_energy_x_engine_coupling_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/fep_pair_free_energy_x_engine_coupling_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/fep_pair_markov_blanket_x_precision_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/fep_pair_markov_blanket_x_precision_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/geom_noncomm_z3_unsat_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/geom_noncomm_z3_unsat_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/gerbe_admissibility_dixmier_douady_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/gerbe_admissibility_dixmier_douady_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/gerbe_carrier_cell_complex_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/gerbe_carrier_cell_complex_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/gerbe_coupling_nested_hopf_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/gerbe_coupling_nested_hopf_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/gerbe_distinguishability_holonomy_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/gerbe_distinguishability_holonomy_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/gerbe_reduction_coboundary_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/gerbe_reduction_coboundary_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/gerbe_structure_b_field_cochain_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/gerbe_structure_b_field_cochain_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/ghz_mermin_inequality_canonical_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/ghz_mermin_inequality_canonical_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/gudhi_torus_betti_canonical_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/gudhi_torus_betti_canonical_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/history_window_support_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/history_window_support_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/holodeck_atom_5_distinguishability_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/holodeck_atom_5_distinguishability_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/holodeck_atom_6_chirality_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/holodeck_atom_6_chirality_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/holodeck_deep_coupling_to_fep_markov_blanket_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/holodeck_deep_coupling_to_fep_markov_blanket_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/holodeck_deep_probe_relative_indistinguishability_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/holodeck_deep_probe_relative_indistinguishability_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/igt_deep_nested_win_lose_irreducibility_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/igt_deep_nested_win_lose_irreducibility_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/igt_deep_ring_topology_chirality_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/igt_deep_ring_topology_chirality_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/lego_01_rank_distinguishability_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/lego_01_rank_distinguishability_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/leviathan_ai_starvation_under_monoculture_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/leviathan_ai_starvation_under_monoculture_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/leviathan_as_civilizational_shell_on_manifold_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/leviathan_as_civilizational_shell_on_manifold_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/leviathan_atom_2_structure_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/leviathan_atom_2_structure_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/leviathan_atom_3_reduction_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/leviathan_atom_3_reduction_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/leviathan_atom_4_admissibility_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/leviathan_atom_4_admissibility_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/leviathan_atom_5_distinguishability_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/leviathan_atom_5_distinguishability_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/leviathan_atom_7_coupling_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/leviathan_atom_7_coupling_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/leviathan_centralization_destroys_admissibility_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/leviathan_centralization_destroys_admissibility_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/leviathan_deep_authority_gradient_monotone_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/leviathan_deep_authority_gradient_monotone_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/leviathan_deep_coalition_minimum_coverage_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/leviathan_deep_coalition_minimum_coverage_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/leviathan_legacy_durability_under_civilizational_reset_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/leviathan_legacy_durability_under_civilizational_reset_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/leviathan_zero_sum_authoritarian_attractor_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/leviathan_zero_sum_authoritarian_attractor_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/loop_order_family_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/loop_order_family_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/mutual_information_measure_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/mutual_information_measure_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/no_cloning_theorem_canonical_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/no_cloning_theorem_canonical_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/numpy_capability_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/numpy_capability_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/operator_ordered_entropy_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/operator_ordered_entropy_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/pauli_algebra_relations_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/pauli_algebra_relations_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/pennylane_capability_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/pennylane_capability_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/positivity_constraint_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/positivity_constraint_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/qutip_capability_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/qutip_capability_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/representation_violation_check_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/representation_violation_check_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/rustworkx_apsp_constraint_skeleton_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/rustworkx_apsp_constraint_skeleton_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/rustworkx_scc_admissibility_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/rustworkx_scc_admissibility_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/schmidt_mode_truncation_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/schmidt_mode_truncation_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/sci_method_deep_probe_set_determines_falsifiability_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/sci_method_deep_probe_set_determines_falsifiability_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/scipy_capability_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/scipy_capability_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/spectral_triple_admissibility_first_order_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/spectral_triple_admissibility_first_order_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/spectral_triple_carrier_algebra_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/spectral_triple_carrier_algebra_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/spectral_triple_chirality_gamma_grading_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/spectral_triple_chirality_gamma_grading_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/spectral_triple_dirac_spectrum_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/spectral_triple_dirac_spectrum_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/spectral_triple_distinguishability_heat_trace_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/spectral_triple_distinguishability_heat_trace_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/spectral_triple_reduction_connes_distance_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/spectral_triple_reduction_connes_distance_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH and load_bearing_ladder_tool.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/sympy_campbell_pauli_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/sympy_campbell_pauli_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/sympy_charpoly_eigvals_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/sympy_charpoly_eigvals_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/sympy_det_product_4x4_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/sympy_det_product_4x4_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/sympy_gaussian_integral_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/sympy_gaussian_integral_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/sympy_jacobi_su2_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/sympy_jacobi_su2_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/sympy_partial_fraction_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/sympy_partial_fraction_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/sympy_schur_complement_psd_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/sympy_schur_complement_psd_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.

## BLOCKER 2026-04-17T21:06:08Z canonical_abuse system_v4/probes/a2_state/sim_results/torch_ga_capability_results.json
- timestamp: 2026-04-17T21:06:08Z
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/torch_ga_capability_results.json
- why_critical: classification canonical lacks TOOL_INTEGRATION_DEPTH.
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/gtower_order_so_to_u_then_su_vs_reverse_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/autograd_vfe_descent_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/reduced_state_object_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/classical_szilard_one_bit_measurement_work_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/autograd_grad_Ic_axis0_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/tri_fep_x_igt_x_leviathan_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/z3_negative_quasiprob_exclusion_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/history_window_entropy_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/channel_capacity_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/gtower_order_full_chain_unique_path_admissibility_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/toponetx_gudhi_hodge_betti_cross_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/pauli_generator_basis_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/rustworkx_cayley_s4_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/qit_szilard_record_reconciled_translation_lane_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/holevo_quantity_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/qit_szilard_substep_ordering_push_translation_lane_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/autograd_matrix_exp_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/low_rank_psd_approximation_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/z3_chsh_no_lhv_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/entanglement_entropy_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/commutator_algebra_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/qit_szilard_substep_balanced_translation_lane_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/qit_szilard_record_ordering_refinement_translation_lane_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/unsigned_entropy_family_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/rustworkx_petersen_iso_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/tri_science_method_x_igt_x_leviathan_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/svd_factorization_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/triangle_holodeck_fep_science_method_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/fep_atom_3_reduction_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/sci_method_atom_2_structure_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/mermin_peres_magic_square_canonical_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/holodeck_atom_7_coupling_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/characteristic_representation_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/conditional_entropy_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/shell_weighted_entropy_field_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/tri_science_method_x_fep_x_igt_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/covariance_operator_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/gauge_group_correspondence_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/pyg_expander_spectral_mixing_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/tri_holodeck_x_igt_x_leviathan_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/graph_geometry_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/sci_method_atom_5_distinguishability_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/cross_fep_x_leviathan_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/persistence_geometry_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/holodeck_atom_2_structure_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/geometry_preserving_basis_change_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/sci_method_atom_6_chirality_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/assoc_bundle_associated_vector_bundle_construction_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/probe_identity_preservation_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/fubini_study_geometry_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/trace_distance_geometry_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/qit_szilard_record_ordering_translation_lane_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/operator_low_rank_factorization_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/qit_szilard_substep_refinement_translation_lane_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/spectral_triple_hopf_dirac_spectrum_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/gudhi_persistence_stability_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/correlation_tensor_principal_directions_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/autograd_eigh_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/state_class_binding_geometry_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/coherence_measure_canonical_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/cirq_matrix_state_bridge_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/correlation_tensor_object_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/shell_window_support_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/fep_pair_free_energy_x_markov_blanket_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/local_operator_action_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/sci_method_atom_7_coupling_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/fep_pair_surprise_x_precision_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/holodeck_deep_carrier_shell_u1_gauge_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/gtower_order_z3_unsat_invalid_reduction_order_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/sympy_bch_4th_order_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/viability_vs_attractor_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/operator_coordinate_representation_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/tri_holodeck_x_science_method_x_leviathan_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/spectral_triple_chirality_grading_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/real_only_geometry_rejection_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/sci_method_atom_3_reduction_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/entanglement_witness_family_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/dual_hypergraph_geometry_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/relative_entropy_js_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/shannon_entropy_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/von_neumann_entropy_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/leviathan_atom_1_carrier_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/qit_szilard_substep_promotion_translation_lane_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/gtower_order_u1_gauge_then_chirality_vs_reverse_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/relative_entropy_nonmetric_boundary_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/qit_carnot_closure_translation_lane_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/gtower_order_o_to_so_then_u_vs_reverse_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/cross_holodeck_x_fep_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/geom_noncomm_ptrace_rotor_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/rustworkx_max_clique_carriers_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/bures_geometry_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/leviathan_atom_6_chirality_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/sci_method_atom_1_carrier_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/engine_lab_alignment_overlay_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/base_loop_law_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/z3_kcbs_contextuality_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/gtower_order_gl_to_o_then_so_vs_reverse_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/spectral_truncation_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/measurement_instrument_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/qit_szilard_substep_structural_translation_lane_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/assoc_bundle_associated_bundle_coupling_to_g_tower_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/schmidt_decomposition_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/qit_szilard_record_hard_reset_translation_lane_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/holodeck_atom_3_reduction_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/eigenvalue_spectrum_view_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/sympy_capability_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/nested_torus_geometry_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/fep_atom_6_chirality_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/concurrence_measure_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/graph_shell_geometry_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/stokes_parameterization_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/engine_lab_translation_targets_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/cross_holodeck_x_leviathan_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/helstrom_guess_bound_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/cross_holodeck_x_science_method_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/holonomy_shell_classifier_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/negativity_measure_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/assoc_bundle_canonical_connection_from_hopf_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/transport_weighted_entropy_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/clifford_generator_basis_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/spectral_triple_noncomm_order_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/spectral_triple_connes_distance_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/hypergraph_geometry_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/coherent_information_measure_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/sphere_geometry_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/fep_atom_2_structure_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/assoc_bundle_parallel_transport_admissibility_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/joint_operator_action_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/entanglement_breaking_ppt_witness_canonical_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/coarse_grained_operator_algebra_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/holodeck_atom_1_carrier_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/sci_method_atom_4_admissibility_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/qit_carnot_hold_translation_lane_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/assoc_bundle_weyl_spinor_as_section_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/carrier_probe_support_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/hilbert_schmidt_flatness_rejection_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/joint_density_matrix_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/holodeck_atom_4_admissibility_results.json
- why_critical: missing uppercase TOOL_INTEGRATION_DEPTH
## Meta blocker 2026-04-17T21:41:51Z — lane_skip
- class: lane_skip
- path_or_commit: 32227f769415
- why_critical: sim_clifford_holo_dirac_bridge_claims_canonical.py references uncovered layer tokens ['dirac', 'holo']
## Meta blocker 2026-04-17T21:41:51Z — lane_skip
- class: lane_skip
- path_or_commit: 32227f769415
- why_critical: sim_hopf_weyl_torus_triple_coexistence.py references uncovered layer tokens ['torus']
## Meta blocker 2026-04-17T21:41:51Z — lane_skip
- class: lane_skip
- path_or_commit: 32227f769415
- why_critical: sim_mera_weyl_hopf_emergence_quantities.py references uncovered layer tokens ['mera']

## META blocker 2026-04-17T22:24:32Z #1
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/L7_weyl_extraction_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #2
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/L8_chiral_density_bookkeeping_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #3
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/SA12_wilczek_zee_curvature_sympy_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #4
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/adams_spectral_sequence_constraint_canonical_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #5
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/blackwell_style_comparison_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #6
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/blp_non_markovianity_canonical_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #7
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/bridge_landauer_erasure_bit_distinguishability_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #8
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/bridge_maxwell_demon_distinguishability_cost_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #9
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/cell_complex_geometry_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #10
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/channel_space_geometry_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T22:24:32Z #11
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/chromatic_homotopy_constraint_canonical_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #12
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/chsh_tsirelson_canonical_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #13
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/circuit_unitary_canonicalization_z3_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #14
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/cl3_deep_double_reflection_equals_rotation_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #15
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/cl3_deep_pseudoscalar_inversion_vs_reflection_order_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #16
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/cl3_deep_rotor_commutator_is_bivector_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #17
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/cl3_deep_rotor_composition_bch_second_order_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #18
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/cl3_deep_rotor_conjugation_preserves_grade_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #19
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/cl3_deep_rotor_order_rx_ry_vs_ry_rx_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #20
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/cl3_deep_stack_three_rotors_order_sensitive_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #21
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/cl6_deep_bivector_decomposition_into_orthogonal_planes_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #22
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/classical_landauer_erasure_cost_curve_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T22:24:32Z #23
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/classical_maxwell_demon_information_accounting_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T22:24:32Z #24
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/clifford_capability_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #25
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/clifford_even_odd_grade_partition_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #26
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/clifford_rotor_plane_invariance_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #27
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/clifford_so_homomorphism_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #28
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/coherent_info_erasure_canonical_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #29
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/conformal_structure_constraint_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #30
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/cvc5_capability_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #31
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/cvc5_frege_system_constraint_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #32
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/cvc5_proof_complexity_size_constraint_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #33
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/cvc5_resolution_proof_constraint_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #34
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/distinguishability_relation_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #35
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/e3nn_capability_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #36
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/elliptic_pde_constraint_canonical_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #37
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/engine_protocol_dag_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #38
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/entanglement_spectrum_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T22:24:32Z #39
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/fep_joint_smt_free_energy_and_markov_blanket_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #40
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/fiber_loop_law_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #41
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/foundation_hopf_torus_geomstats_clifford_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T22:24:32Z #42
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/fourier_uncertainty_constraint_canonical_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #43
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/geomstats_capability_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T22:24:32Z #44
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/groebner_basis_constraint_canonical_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #45
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/gtower_order_su_to_sp_then_so_vs_reverse_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #46
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/gtower_order_three_step_gl_o_so_permutations_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #47
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/gudhi_capability_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #48
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/heat_equation_constraint_canonical_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #49
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/holevo_bound_canonical_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #50
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/hopf_base_section_phase_recovery_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #51
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/hopf_connection_gauge_transition_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #52
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/hopf_fiber_equivalence_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #53
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/hopf_higher_fibration_winding_index_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #54
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/hopf_horizontal_lift_closure_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #55
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/hopf_horizontal_projector_constraint_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #56
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/hopf_s15_connection_parallel_transport_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #57
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/hopf_s7_local_section_fiber_bundle_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #58
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/hopf_section_overlap_transition_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #59
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/hopf_torus_rank_stratification_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #60
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/hopf_vertical_horizontal_response_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #61
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/husimi_phase_space_representation_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T22:24:32Z #62
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/kazhdan_lusztig_polynomial_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #63
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/kochen_specker_18ray_canonical_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #64
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/leggett_garg_k3_canonical_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #65
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/leggett_garg_k3_clifford_canonical_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #66
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/lego_entropy_extremal_density_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T22:24:32Z #67
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/lego_entropy_finite_blocklength_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T22:24:32Z #68
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/lego_entropy_holevo_quantity_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T22:24:32Z #69
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/lego_entropy_inequalities_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T22:24:32Z #70
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/lego_entropy_smooth_one_shot_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #71
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/lego_entropy_spectral_families_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #72
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/lego_weyl_hopf_spinor_bridge_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #73
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/lego_weyl_hypergraph_local_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #74
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/lego_weyl_pauli_transport_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T22:24:32Z #75
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/leviathan_authority_entropy_operator_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #76
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/leviathan_gudhi_stability_persistence_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #77
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/leviathan_xgi_coalition_hypergraph_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #78
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/logarithmic_negativity_werner_canonical_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #79
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/networkx_capability_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T22:24:32Z #80
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/pauli_centralizer_constraint_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #81
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/pauli_projector_reconstruction_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #82
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/plancherel_theorem_constraint_canonical_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #83
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/plethysm_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #84
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/probe_object_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #85
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/pyg_capability_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #86
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/pyg_toponetx_higher_order_mp_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #87
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/pytorch_capability_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #88
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/qfi_squeezed_canonical_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #89
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/qit_attractor_basin_recovery_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T22:24:32Z #90
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/qit_carnot_irreversibility_translation_lane_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T22:24:32Z #91
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/qit_entropy_companion_array_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T22:24:32Z #92
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/qit_moloch_coordination_trap_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T22:24:32Z #93
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/qit_predictive_world_model_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T22:24:32Z #94
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/qit_szilard_record_repair_translation_lane_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T22:24:32Z #95
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/qit_szilard_record_translation_lane_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T22:24:32Z #96
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/qit_szilard_reverse_recovery_companion_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T22:24:32Z #97
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/qit_szilard_reverse_translation_lane_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T22:24:32Z #98
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/qit_szilard_substep_translation_lane_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T22:24:32Z #99
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/qit_weyl_carnot_bridge_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #100
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/qit_weyl_geometry_carrier_translation_lane_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T22:24:32Z #101
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/qit_weyl_geometry_compare_translation_lane_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T22:24:32Z #102
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/qit_weyl_geometry_translation_lane_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T22:24:32Z #103
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/qit_weyl_hypergraph_companion_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #104
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/qit_weyl_hypergraph_translation_lane_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #105
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/qit_weyl_szilard_geometry_bridge_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #106
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/qpca_spectral_extraction_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T22:24:32Z #107
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/quantum_discord_canonical_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #108
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/quantum_mutual_info_superadditivity_canonical_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #109
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/qutip_classical_bridge_density_roundtrip_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T22:24:32Z #110
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/relative_entropy_of_entanglement_canonical_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #111
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/robertson_uncertainty_canonical_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #112
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/rsk_correspondence_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #113
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/sa10_wilczek_zee_curvature_boundary_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #114
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/sim_cstar_algebra_constraint_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #115
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/sim_geometry_algebraic_cycle_hodge_class_constraint_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #116
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/sim_geometry_algebraic_k_theory_quillen_constraint_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #117
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/sim_geometry_automorphic_form_cuspidality_constraint_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #118
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/sim_geometry_deligne_cohomology_regulator_constraint_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #119
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/sim_geometry_etale_cohomology_ladic_constraint_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #120
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/sim_geometry_griffiths_group_non_torsion_constraint_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #121
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/sim_geometry_k_theory_localization_sequence_constraint_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #122
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/sim_geometry_p_adic_valuation_ultrametric_constraint_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #123
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/sim_geometry_topological_k_theory_bott_periodicity_constraint_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #124
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/sim_geometry_weil_conjectures_zeta_function_constraint_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #125
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/sim_ktheory_cstar_constraint_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #126
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/sim_shimura_variety_canonical_model_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #127
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/sim_von_neumann_algebra_constraint_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #128
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/spectral_triple_gtower_reduction_spectrum_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #129
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/spectral_triple_weyl_hopf_coupling_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #130
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/spinor_harmonics_constraint_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #131
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/stable_stems_constraint_canonical_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #132
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/stinespring_isometric_equivalence_canonical_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #133
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/superdense_coding_capacity_canonical_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #134
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/teleportation_fidelity_canonical_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #135
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/tetra_holodeck_fep_science_method_axis0_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #136
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/torch_eigendecomp_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #137
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/torch_husimi_q_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T22:24:32Z #138
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/torch_l1_coherence_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #139
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/torch_mutual_info_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T22:24:32Z #140
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/torch_quantum_discord_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #141
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/torch_re_coherence_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T22:24:32Z #142
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/torch_wigner_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T22:24:32Z #143
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/torch_z_measurement_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T22:24:32Z #144
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/tri_holodeck_x_fep_x_leviathan_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #145
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/tropical_geometry_constraint_canonical_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #146
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/variational_quantum_bridge_pytorch_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #147
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/wave_equation_constraint_canonical_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #148
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/werner_entanglement_witness_canonical_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #149
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/weyl_geometry_alignment_overlay_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T22:24:32Z #150
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/weyl_geometry_ladder_audit_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #151
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/z3_capability_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #152
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/z3_pauli_joint_commute_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:24:32Z #153
- timestamp: 2026-04-17T22:24:32Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/z3_ppt_rank_constraints_results.json
- why_critical: classification canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:49:49Z — canonical_abuse — system_v4/probes/a2_state/sim_results/residue_theorem_constraint_canonical_results.json
- timestamp: 2026-04-17T22:49:49Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/residue_theorem_constraint_canonical_results.json
- why_critical: classification "canonical" lacks TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:49:49Z — canonical_abuse — system_v4/probes/a2_state/sim_results/contact_symplectic_mera_bridge_claims_canonical_results.json
- timestamp: 2026-04-17T22:49:49Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/contact_symplectic_mera_bridge_claims_canonical_results.json
- why_critical: classification "canonical" lacks TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:49:49Z — canonical_abuse — system_v4/probes/a2_state/sim_results/qit_carnot_two_bath_cycle_results.json
- timestamp: 2026-04-17T22:49:49Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/qit_carnot_two_bath_cycle_results.json
- why_critical: classification "canonical" lacks TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:49:49Z — canonical_abuse — system_v4/probes/a2_state/sim_results/qit_carnot_closure_companion_results.json
- timestamp: 2026-04-17T22:49:49Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/qit_carnot_closure_companion_results.json
- why_critical: classification "canonical" lacks TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:49:49Z — canonical_abuse — system_v4/probes/a2_state/sim_results/weyl_contact_dirac_bridge_claims_canonical_results.json
- timestamp: 2026-04-17T22:49:49Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/weyl_contact_dirac_bridge_claims_canonical_results.json
- why_critical: classification "canonical" lacks TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:49:49Z — canonical_abuse — system_v4/probes/a2_state/sim_results/symplectic_spectral_triple_mera_bridge_claims_canonical_results.json
- timestamp: 2026-04-17T22:49:49Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/symplectic_spectral_triple_mera_bridge_claims_canonical_results.json
- why_critical: classification "canonical" lacks TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:49:49Z — canonical_abuse — system_v4/probes/a2_state/sim_results/c2_c4_independence_crosscheck_results.json
- timestamp: 2026-04-17T22:49:49Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/c2_c4_independence_crosscheck_results.json
- why_critical: classification "canonical" lacks TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:49:49Z — canonical_abuse — system_v4/probes/a2_state/sim_results/sim_geometry_langlands_functoriality_constraint_results.json
- timestamp: 2026-04-17T22:49:49Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/sim_geometry_langlands_functoriality_constraint_results.json
- why_critical: classification "canonical" lacks TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:49:49Z — canonical_abuse — system_v4/probes/a2_state/sim_results/riemann_mapping_theorem_constraint_canonical_results.json
- timestamp: 2026-04-17T22:49:49Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/riemann_mapping_theorem_constraint_canonical_results.json
- why_critical: classification "canonical" lacks TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:49:49Z — canonical_abuse — system_v4/probes/a2_state/sim_results/holo_contact_symplectic_bridge_claims_canonical_results.json
- timestamp: 2026-04-17T22:49:49Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/holo_contact_symplectic_bridge_claims_canonical_results.json
- why_critical: classification "canonical" lacks TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:49:49Z — canonical_abuse — system_v4/probes/a2_state/sim_results/toponetx_capability_results.json
- timestamp: 2026-04-17T22:49:49Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/toponetx_capability_results.json
- why_critical: classification "canonical" lacks TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:49:49Z — canonical_abuse — system_v4/probes/a2_state/sim_results/model_category_quillen_axioms_results.json
- timestamp: 2026-04-17T22:49:49Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/model_category_quillen_axioms_results.json
- why_critical: classification "canonical" lacks TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:49:49Z — canonical_abuse — system_v4/probes/a2_state/sim_results/qit_weyl_geometry_companion_results.json
- timestamp: 2026-04-17T22:49:49Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/qit_weyl_geometry_companion_results.json
- why_critical: classification "canonical" lacks TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:49:49Z — canonical_abuse — system_v4/probes/a2_state/sim_results/gudhi_concurrence_filtration_results.json
- timestamp: 2026-04-17T22:49:49Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/gudhi_concurrence_filtration_results.json
- why_critical: classification "canonical" lacks TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:49:49Z — canonical_abuse — system_v4/probes/a2_state/sim_results/toponetx_hopf_crosscheck_results.json
- timestamp: 2026-04-17T22:49:49Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/toponetx_hopf_crosscheck_results.json
- why_critical: classification "canonical" lacks TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:49:49Z — canonical_abuse — system_v4/probes/a2_state/sim_results/rustworkx_dag_reduction_results.json
- timestamp: 2026-04-17T22:49:49Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/rustworkx_dag_reduction_results.json
- why_critical: classification "canonical" lacks TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:49:49Z — canonical_abuse — system_v4/probes/a2_state/sim_results/gudhi_bloch_sphere_2d_results.json
- timestamp: 2026-04-17T22:49:49Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/gudhi_bloch_sphere_2d_results.json
- why_critical: classification "canonical" lacks TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:49:49Z — canonical_abuse — system_v4/probes/a2_state/sim_results/torch_purification_results.json
- timestamp: 2026-04-17T22:49:49Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/torch_purification_results.json
- why_critical: classification "canonical" lacks TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:49:49Z — canonical_abuse — system_v4/probes/a2_state/sim_results/gtower_triple_su2_u1_spin_ordering_results.json
- timestamp: 2026-04-17T22:49:49Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/gtower_triple_su2_u1_spin_ordering_results.json
- why_critical: classification "canonical" lacks TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:49:49Z — canonical_abuse — system_v4/probes/a2_state/sim_results/dirac_symplectic_weyl_bridge_claims_canonical_results.json
- timestamp: 2026-04-17T22:49:49Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/dirac_symplectic_weyl_bridge_claims_canonical_results.json
- why_critical: classification "canonical" lacks TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:49:49Z — canonical_abuse — system_v4/probes/a2_state/sim_results/contact_clifford_mera_bridge_claims_canonical_results.json
- timestamp: 2026-04-17T22:49:49Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/contact_clifford_mera_bridge_claims_canonical_results.json
- why_critical: classification "canonical" lacks TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:49:49Z — canonical_abuse — system_v4/probes/a2_state/sim_results/phi0_matched_packet_head_to_head_results.json
- timestamp: 2026-04-17T22:49:49Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/phi0_matched_packet_head_to_head_results.json
- why_critical: classification "canonical" lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T22:49:49Z — canonical_abuse — system_v4/probes/a2_state/sim_results/torch_t_gate_results.json
- timestamp: 2026-04-17T22:49:49Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/torch_t_gate_results.json
- why_critical: classification "canonical" lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T22:49:49Z — canonical_abuse — system_v4/probes/a2_state/sim_results/phi0_integrated_bakeoff_results.json
- timestamp: 2026-04-17T22:49:49Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/phi0_integrated_bakeoff_results.json
- why_critical: classification "canonical" lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T22:49:49Z — canonical_abuse — system_v4/probes/a2_state/sim_results/torch_chiral_overlap_results.json
- timestamp: 2026-04-17T22:49:49Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/torch_chiral_overlap_results.json
- why_critical: classification "canonical" lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T22:49:49Z — canonical_abuse — system_v4/probes/a2_state/sim_results/torch_swap_results.json
- timestamp: 2026-04-17T22:49:49Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/torch_swap_results.json
- why_critical: classification "canonical" lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T22:49:49Z — canonical_abuse — system_v4/probes/a2_state/sim_results/bridge_finite_blocklength_cut_states_results.json
- timestamp: 2026-04-17T22:49:49Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/bridge_finite_blocklength_cut_states_results.json
- why_critical: classification "canonical" lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T22:49:49Z — canonical_abuse — system_v4/probes/a2_state/sim_results/rustworkx_cascade_dag_results.json
- timestamp: 2026-04-17T22:49:49Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/rustworkx_cascade_dag_results.json
- why_critical: classification "canonical" lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T22:49:49Z — canonical_abuse — system_v4/probes/a2_state/sim_results/phi0_ic_vs_mi_regime_map_results.json
- timestamp: 2026-04-17T22:49:49Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/phi0_ic_vs_mi_regime_map_results.json
- why_critical: classification "canonical" lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T22:49:49Z — canonical_abuse — system_v4/probes/a2_state/sim_results/spectral_triple_contact_gerbe_bridge_claims_canonical_results.json
- timestamp: 2026-04-17T22:49:49Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/spectral_triple_contact_gerbe_bridge_claims_canonical_results.json
- why_critical: classification "canonical" lacks TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-17T22:49:49Z — canonical_abuse — system_v4/probes/a2_state/sim_results/torch_hadamard_results.json
- timestamp: 2026-04-17T22:49:49Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/torch_hadamard_results.json
- why_critical: classification "canonical" lacks TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-17T23:22:51Z canonical_abuse system_v4/probes/a2_state/sim_results/adiabatic_berry_dynamics_results.json
- timestamp: 2026-04-17T23:22:51Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/adiabatic_berry_dynamics_results.json
- why_critical: classification canonical is present while TOOL_INTEGRATION_DEPTH is absent; critical contract is not satisfied.

## META blocker 2026-04-17T23:22:51Z canonical_abuse system_v4/probes/a2_state/sim_results/c2_topology_remaining_results.json
- timestamp: 2026-04-17T23:22:51Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/c2_topology_remaining_results.json
- why_critical: classification canonical is present while TOOL_INTEGRATION_DEPTH is absent; critical contract is not satisfied.

## META blocker 2026-04-17T23:22:51Z canonical_abuse system_v4/probes/a2_state/sim_results/cauchy_riemann_constraint_canonical_results.json
- timestamp: 2026-04-17T23:22:51Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/cauchy_riemann_constraint_canonical_results.json
- why_critical: classification canonical is present while TOOL_INTEGRATION_DEPTH is absent; critical contract is not satisfied.

## META blocker 2026-04-17T23:22:51Z canonical_abuse system_v4/probes/a2_state/sim_results/e3nn_hopf_spinor_equivariance_results.json
- timestamp: 2026-04-17T23:22:51Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/e3nn_hopf_spinor_equivariance_results.json
- why_critical: classification canonical is present while TOOL_INTEGRATION_DEPTH is absent; critical contract is not satisfied.

## META blocker 2026-04-17T23:22:51Z canonical_abuse system_v4/probes/a2_state/sim_results/gudhi_cascade_persistence_results.json
- timestamp: 2026-04-17T23:22:51Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/gudhi_cascade_persistence_results.json
- why_critical: classification canonical is present while TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool is absent; critical contract is not satisfied.

## META blocker 2026-04-17T23:22:51Z canonical_abuse system_v4/probes/a2_state/sim_results/gudhi_phase_sensitive_kernel_results.json
- timestamp: 2026-04-17T23:22:51Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/gudhi_phase_sensitive_kernel_results.json
- why_critical: classification canonical is present while TOOL_INTEGRATION_DEPTH is absent; critical contract is not satisfied.

## META blocker 2026-04-17T23:22:51Z canonical_abuse system_v4/probes/a2_state/sim_results/gudhi_wasserstein_significance_results.json
- timestamp: 2026-04-17T23:22:51Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/gudhi_wasserstein_significance_results.json
- why_critical: classification canonical is present while TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool is absent; critical contract is not satisfied.

## META blocker 2026-04-17T23:22:51Z canonical_abuse system_v4/probes/a2_state/sim_results/integrated_dependency_chain_results.json
- timestamp: 2026-04-17T23:22:51Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/integrated_dependency_chain_results.json
- why_critical: classification canonical is present while TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool is absent; critical contract is not satisfied.

## META blocker 2026-04-17T23:22:51Z canonical_abuse system_v4/probes/a2_state/sim_results/qit_carnot_closure_companion_results.json
- timestamp: 2026-04-17T23:22:51Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/qit_carnot_closure_companion_results.json
- why_critical: classification canonical is present while TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool is absent; critical contract is not satisfied.

## META blocker 2026-04-17T23:22:51Z canonical_abuse system_v4/probes/a2_state/sim_results/qit_carnot_two_bath_cycle_results.json
- timestamp: 2026-04-17T23:22:51Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/qit_carnot_two_bath_cycle_results.json
- why_critical: classification canonical is present while TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool is absent; critical contract is not satisfied.

## META blocker 2026-04-17T23:22:51Z canonical_abuse system_v4/probes/a2_state/sim_results/qit_szilard_substep_companion_results.json
- timestamp: 2026-04-17T23:22:51Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/qit_szilard_substep_companion_results.json
- why_critical: classification canonical is present while TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool is absent; critical contract is not satisfied.

## META blocker 2026-04-17T23:22:51Z canonical_abuse system_v4/probes/a2_state/sim_results/qit_weyl_geometry_companion_array_results.json
- timestamp: 2026-04-17T23:22:51Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/qit_weyl_geometry_companion_array_results.json
- why_critical: classification canonical is present while TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool is absent; critical contract is not satisfied.

## META blocker 2026-04-17T23:22:51Z canonical_abuse system_v4/probes/a2_state/sim_results/rustworkx_bridge_dag_results.json
- timestamp: 2026-04-17T23:22:51Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/rustworkx_bridge_dag_results.json
- why_critical: classification canonical is present while TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool is absent; critical contract is not satisfied.

## META blocker 2026-04-17T23:22:51Z canonical_abuse system_v4/probes/a2_state/sim_results/rustworkx_family_dag_results.json
- timestamp: 2026-04-17T23:22:51Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/rustworkx_family_dag_results.json
- why_critical: classification canonical is present while TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool is absent; critical contract is not satisfied.

## META blocker 2026-04-17T23:22:51Z canonical_abuse system_v4/probes/a2_state/sim_results/sim_cvc5_colimit_cocone_pushout_constraint.json
- timestamp: 2026-04-17T23:22:51Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/sim_cvc5_colimit_cocone_pushout_constraint.json
- why_critical: classification canonical is present while TOOL_INTEGRATION_DEPTH is absent; critical contract is not satisfied.

## META blocker 2026-04-17T23:22:51Z canonical_abuse system_v4/probes/a2_state/sim_results/sim_cvc5_kan_extension_universal_property_constraint.json
- timestamp: 2026-04-17T23:22:51Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/sim_cvc5_kan_extension_universal_property_constraint.json
- why_critical: classification canonical is present while TOOL_INTEGRATION_DEPTH is absent; critical contract is not satisfied.

## META blocker 2026-04-17T23:22:51Z canonical_abuse system_v4/probes/a2_state/sim_results/sim_cvc5_limit_universal_cone_constraint.json
- timestamp: 2026-04-17T23:22:51Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/sim_cvc5_limit_universal_cone_constraint.json
- why_critical: classification canonical is present while TOOL_INTEGRATION_DEPTH is absent; critical contract is not satisfied.

## META blocker 2026-04-17T23:22:51Z canonical_abuse system_v4/probes/a2_state/sim_results/su2_killing_form_exhaustion_results.json
- timestamp: 2026-04-17T23:22:51Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/su2_killing_form_exhaustion_results.json
- why_critical: classification canonical is present while TOOL_INTEGRATION_DEPTH is absent; critical contract is not satisfied.

## META blocker 2026-04-17T23:22:51Z canonical_abuse system_v4/probes/a2_state/sim_results/toponetx_constraint_shells_results.json
- timestamp: 2026-04-17T23:22:51Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/toponetx_constraint_shells_results.json
- why_critical: classification canonical is present while TOOL_INTEGRATION_DEPTH is absent; critical contract is not satisfied.

## META blocker 2026-04-17T23:22:51Z canonical_abuse system_v4/probes/a2_state/sim_results/torch_amplitude_damping_results.json
- timestamp: 2026-04-17T23:22:51Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/torch_amplitude_damping_results.json
- why_critical: classification canonical is present while TOOL_INTEGRATION_DEPTH is absent; critical contract is not satisfied.

## META blocker 2026-04-17T23:22:51Z canonical_abuse system_v4/probes/a2_state/sim_results/torch_bit_flip_results.json
- timestamp: 2026-04-17T23:22:51Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/torch_bit_flip_results.json
- why_critical: classification canonical is present while TOOL_INTEGRATION_DEPTH is absent; critical contract is not satisfied.

## META blocker 2026-04-17T23:22:51Z canonical_abuse system_v4/probes/a2_state/sim_results/torch_cartan_kak_results.json
- timestamp: 2026-04-17T23:22:51Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/torch_cartan_kak_results.json
- why_critical: classification canonical is present while TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool is absent; critical contract is not satisfied.

## META blocker 2026-04-17T23:22:51Z canonical_abuse system_v4/probes/a2_state/sim_results/torch_channel_composition_results.json
- timestamp: 2026-04-17T23:22:51Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/torch_channel_composition_results.json
- why_critical: classification canonical is present while TOOL_INTEGRATION_DEPTH is absent; critical contract is not satisfied.

## META blocker 2026-04-17T23:22:51Z canonical_abuse system_v4/probes/a2_state/sim_results/torch_cz_results.json
- timestamp: 2026-04-17T23:22:51Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/torch_cz_results.json
- why_critical: classification canonical is present while TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool is absent; critical contract is not satisfied.

## META blocker 2026-04-17T23:22:51Z canonical_abuse system_v4/probes/a2_state/sim_results/torch_density_matrix_pilot_results.json
- timestamp: 2026-04-17T23:22:51Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/torch_density_matrix_pilot_results.json
- why_critical: classification canonical is present while TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool is absent; critical contract is not satisfied.

## META blocker 2026-04-17T23:22:51Z canonical_abuse system_v4/probes/a2_state/sim_results/torch_depolarizing_results.json
- timestamp: 2026-04-17T23:22:51Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/torch_depolarizing_results.json
- why_critical: classification canonical is present while TOOL_INTEGRATION_DEPTH is absent; critical contract is not satisfied.

## META blocker 2026-04-17T23:22:51Z canonical_abuse system_v4/probes/a2_state/sim_results/torch_hopf_connection_results.json
- timestamp: 2026-04-17T23:22:51Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/torch_hopf_connection_results.json
- why_critical: classification canonical is present while TOOL_INTEGRATION_DEPTH is absent; critical contract is not satisfied.

## META blocker 2026-04-17T23:22:51Z canonical_abuse system_v4/probes/a2_state/sim_results/torch_iswap_results.json
- timestamp: 2026-04-17T23:22:51Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/torch_iswap_results.json
- why_critical: classification canonical is present while TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool is absent; critical contract is not satisfied.

## META blocker 2026-04-17T23:22:51Z canonical_abuse system_v4/probes/a2_state/sim_results/torch_phase_damping_results.json
- timestamp: 2026-04-17T23:22:51Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/torch_phase_damping_results.json
- why_critical: classification canonical is present while TOOL_INTEGRATION_DEPTH is absent; critical contract is not satisfied.

## META blocker 2026-04-17T23:22:51Z canonical_abuse system_v4/probes/a2_state/sim_results/torch_phase_flip_results.json
- timestamp: 2026-04-17T23:22:51Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/torch_phase_flip_results.json
- why_critical: classification canonical is present while TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool is absent; critical contract is not satisfied.

## META blocker 2026-04-17T23:22:51Z canonical_abuse system_v4/probes/a2_state/sim_results/torch_unitary_rotation_results.json
- timestamp: 2026-04-17T23:22:51Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/torch_unitary_rotation_results.json
- why_critical: classification canonical is present while TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool is absent; critical contract is not satisfied.

## META blocker 2026-04-17T23:22:51Z canonical_abuse system_v4/probes/a2_state/sim_results/torch_x_dephasing_results.json
- timestamp: 2026-04-17T23:22:51Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/torch_x_dephasing_results.json
- why_critical: classification canonical is present while TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool is absent; critical contract is not satisfied.

## META blocker 2026-04-17T23:22:51Z canonical_abuse system_v4/probes/a2_state/sim_results/torch_z_dephasing_results.json
- timestamp: 2026-04-17T23:22:51Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/torch_z_dephasing_results.json
- why_critical: classification canonical is present while TOOL_INTEGRATION_DEPTH is absent; critical contract is not satisfied.

## META blocker 2026-04-17T23:22:51Z canonical_abuse system_v4/probes/a2_state/sim_results/tripartite_mi_bug_fix_results.json
- timestamp: 2026-04-17T23:22:51Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/tripartite_mi_bug_fix_results.json
- why_critical: classification canonical is present while TOOL_INTEGRATION_DEPTH is absent; critical contract is not satisfied.

## META blocker 2026-04-17T23:22:51Z canonical_abuse system_v4/probes/a2_state/sim_results/w_ghz_bipartition_audit_results.json
- timestamp: 2026-04-17T23:22:51Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/w_ghz_bipartition_audit_results.json
- why_critical: classification canonical is present while TOOL_INTEGRATION_DEPTH is absent; critical contract is not satisfied.

## META blocker 2026-04-17T23:22:51Z canonical_abuse system_v4/probes/a2_state/sim_results/xgi_bridge_hyperedges_results.json
- timestamp: 2026-04-17T23:22:51Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/xgi_bridge_hyperedges_results.json
- why_critical: classification canonical is present while TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool is absent; critical contract is not satisfied.

## META blocker 2026-04-17T23:22:51Z canonical_abuse system_v4/probes/a2_state/sim_results/xgi_dual_hypergraph_results.json
- timestamp: 2026-04-17T23:22:51Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/xgi_dual_hypergraph_results.json
- why_critical: classification canonical is present while TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool is absent; critical contract is not satisfied.

## META blocker 2026-04-17T23:52:12Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/xgi_isolate_investigation_results.json
- why_critical: classification canonical is not admitted because TOOL_INTEGRATION_DEPTH is missing

## META blocker 2026-04-17T23:52:12Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/pure_lego_qfi_wy_qgt_results.json
- why_critical: classification canonical is not admitted because TOOL_INTEGRATION_DEPTH is missing

## META blocker 2026-04-17T23:52:12Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/xgi_family_hypergraph_results.json
- why_critical: classification canonical is not admitted because TOOL_INTEGRATION_DEPTH is missing

## META blocker 2026-04-17T23:52:12Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/geom_su2_so3_quaternions_results.json
- why_critical: classification canonical is not admitted because TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool is missing

## META blocker 2026-04-17T23:52:12Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/xgi_indirect_pathway_results.json
- why_critical: classification canonical is not admitted because TOOL_INTEGRATION_DEPTH is missing

## META blocker 2026-04-17T23:52:12Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/dissipative_kraus_shell_compatibility_results.json
- why_critical: classification canonical is not admitted because TOOL_INTEGRATION_DEPTH is missing

## META blocker 2026-04-17T23:52:12Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/geom_layer_4_5_results.json
- why_critical: classification canonical is not admitted because TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool is missing

## META blocker 2026-04-17T23:52:12Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/torch_gnn_loss_regularized_results.json
- why_critical: classification canonical is not admitted because TOOL_INTEGRATION_DEPTH is missing

## META blocker 2026-04-17T23:52:12Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/torch_cnot_results.json
- why_critical: classification canonical is not admitted because TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool is missing

## META blocker 2026-04-17T23:52:12Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/geom_layer_1_2_3_results.json
- why_critical: classification canonical is not admitted because TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool is missing

## META blocker 2026-04-17T23:52:12Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/hopf_torus_lego_results.json
- why_critical: classification canonical is not admitted because TOOL_INTEGRATION_DEPTH is missing

## META blocker 2026-04-17T23:52:12Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/pure_lego_density_matrices_results.json
- why_critical: classification canonical is not admitted because TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool is missing

## META blocker 2026-04-17T23:52:12Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/gudhi_bipartite_entangled_results.json
- why_critical: classification canonical is not admitted because TOOL_INTEGRATION_DEPTH is missing

## META blocker 2026-04-17T23:52:12Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/quantum_discord_depolarizing_c2_results.json
- why_critical: classification canonical is not admitted because TOOL_INTEGRATION_DEPTH is missing

## META blocker 2026-04-17T23:52:12Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/substrate_divergence_resolution_results.json
- why_critical: classification canonical is not admitted because TOOL_INTEGRATION_DEPTH is missing

## META blocker 2026-04-17T23:52:12Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/q2_clifford_structure_results.json
- why_critical: classification canonical is not admitted because TOOL_INTEGRATION_DEPTH is missing

## META blocker 2026-04-17T23:52:12Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/levi_civita_connection_results.json
- why_critical: classification canonical is not admitted because TOOL_INTEGRATION_DEPTH is missing

## META blocker 2026-04-17T23:52:12Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/toponetx_bridge_seam_results.json
- why_critical: classification canonical is not admitted because TOOL_INTEGRATION_DEPTH is missing

## META blocker 2026-04-17T23:52:12Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/topology_entropy_dynamics_results.json
- why_critical: classification canonical is not admitted because TOOL_INTEGRATION_DEPTH is missing

## META blocker 2026-04-17T23:52:12Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/berry_qfi_entangled_path_results.json
- why_critical: classification canonical is not admitted because TOOL_INTEGRATION_DEPTH is missing

## META blocker 2026-04-17T23:52:12Z canonical_abuse
- class: canonical_abuse
- path_or_commit: system_v4/probes/a2_state/sim_results/torch_channel_taxonomy_results.json
- why_critical: classification canonical is not admitted because TOOL_INTEGRATION_DEPTH is missing

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/3qubit_dag_formal_ordering_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/3qubit_dag_formal_ordering_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/3qubit_dag_formal_ordering_v2_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/3qubit_dag_formal_ordering_v2_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/3qubit_full_cascade_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/3qubit_full_cascade_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/4qubit_cascade_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/4qubit_cascade_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/axis6_canonical_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/axis6_canonical_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/axis6_entropy_decomposition_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/axis6_entropy_decomposition_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/axis6_rank_coherence_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/axis6_rank_coherence_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/axis7_12_gs_residual_axes_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/axis7_12_gs_residual_axes_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/axis_couple_0_1_entropy_gradient_x_curvature_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/axis_couple_0_1_entropy_gradient_x_curvature_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/axis_couple_1_4_curvature_x_loop_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/axis_couple_1_4_curvature_x_loop_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/axis_couple_1_5_curvature_x_torus_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/axis_couple_1_5_curvature_x_torus_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/axis_couple_3_0_phase_x_entropy_gradient_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/axis_couple_3_0_phase_x_entropy_gradient_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/axis_couple_3_5_phase_x_torus_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/axis_couple_3_5_phase_x_torus_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/axis_couple_4_5_loop_x_torus_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/axis_couple_4_5_loop_x_torus_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/berry_qfi_shell_paths_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/berry_qfi_shell_paths_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/bridge_cut_perturbation_stability_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/bridge_cut_perturbation_stability_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/bridge_phi0_proof_integration_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/bridge_phi0_proof_integration_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/contact_symplectic_kahler_coexistence_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/contact_symplectic_kahler_coexistence_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/coupling_fep_holodeck_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/coupling_fep_holodeck_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/coupling_fep_sci_method_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/coupling_fep_sci_method_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/coupling_holodeck_igt_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/coupling_holodeck_igt_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/coupling_holodeck_leviathan_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/coupling_holodeck_leviathan_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/coupling_holodeck_sci_method_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/coupling_holodeck_sci_method_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/coupling_igt_sci_method_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/coupling_igt_sci_method_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/coupling_leviathan_sci_method_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/coupling_leviathan_sci_method_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/density_hopf_geometry_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/density_hopf_geometry_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/e3nn_ic_invariance_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/e3nn_ic_invariance_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/e3nn_ic_pipeline_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/e3nn_ic_pipeline_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/engine_16_placements_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/engine_16_placements_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/engine_8_terrains_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/engine_8_terrains_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/engine_lab_matrix_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/engine_lab_matrix_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/f01_compose_12_tensor_product_preserves_finiteness_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/f01_compose_12_tensor_product_preserves_finiteness_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/f01_compose_13_partial_trace_preserves_distinguishability_bound_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/f01_compose_13_partial_trace_preserves_distinguishability_bound_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/f01_compose_14_iterated_measurement_saturates_log_N_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/f01_compose_14_iterated_measurement_saturates_log_N_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/f01_compose_15_quotient_cardinality_le_original_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/f01_compose_15_quotient_cardinality_le_original_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/f01_cross_10_clifford_rotor_distinguishability_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/f01_cross_10_clifford_rotor_distinguishability_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/f01_cross_11_pytorch_autograd_distinguishability_loss_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/f01_cross_11_pytorch_autograd_distinguishability_loss_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/f01_deep_01_probe_size_lower_bound_log2_N_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/f01_deep_01_probe_size_lower_bound_log2_N_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/f01_deep_02_finiteness_forces_discrete_spectrum_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/f01_deep_02_finiteness_forces_discrete_spectrum_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/f01_deep_03_information_bound_shannon_log_N_max_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/f01_deep_03_information_bound_shannon_log_N_max_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/f01_deep_04_distinguishability_quantum_nonzero_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/f01_deep_04_distinguishability_quantum_nonzero_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/f01_deep_05_probe_reuse_compresses_capacity_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/f01_deep_05_probe_reuse_compresses_capacity_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/f01_fail_06_continuum_distinguishability_contradiction_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/f01_fail_06_continuum_distinguishability_contradiction_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/f01_fail_08_no_finite_hilbert_no_trace_class_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/f01_fail_08_no_finite_hilbert_no_trace_class_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/f01n01_couple_clifford_rotor_identity_under_finite_probes_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/f01n01_couple_clifford_rotor_identity_under_finite_probes_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/f01n01_couple_finite_classes_excludes_continuum_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/f01n01_couple_finite_classes_excludes_continuum_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/f01n01_couple_noncommute_requires_distinct_probes_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/f01n01_couple_noncommute_requires_distinct_probes_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/f01n01_couple_probe_refinement_bounded_by_log_N_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/f01n01_couple_probe_refinement_bounded_by_log_N_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/f01n01_couple_quotient_respects_cardinality_bound_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/f01n01_couple_quotient_respects_cardinality_bound_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/four_topology_pauli_map_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/four_topology_pauli_map_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/frozen_kernel_classification_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/frozen_kernel_classification_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/full_ratchet_cascade_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/full_ratchet_cascade_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/geodesic_exponential_map_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/geodesic_exponential_map_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/geom_cp1_u1_projective_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/geom_cp1_u1_projective_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/geom_layer_6_7_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/geom_layer_6_7_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/geom_layer_8_9_10_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/geom_layer_8_9_10_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/geom_noncomm_pauli_xz_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/geom_noncomm_pauli_xz_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/geom_noncomm_so3_u1_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/geom_noncomm_so3_u1_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/geom_noncomm_spin_reflect_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/geom_noncomm_spin_reflect_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/geom_topology_layers_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/geom_topology_layers_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/geometric_constraint_manifold_pyg_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/geometric_constraint_manifold_pyg_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/gnn_cascade_integrated_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/gnn_cascade_integrated_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/gstructure_compatibility_coupling_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/gstructure_compatibility_coupling_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/gudhi_s2_topology_recovery_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/gudhi_s2_topology_recovery_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/hopf_foliation_structure_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/hopf_foliation_structure_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/information_geometry_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/information_geometry_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/layer_coupling_matrix_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/layer_coupling_matrix_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/layer_coupling_matrix_v2_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/layer_coupling_matrix_v2_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/layer_coupling_matrix_v3_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/layer_coupling_matrix_v3_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/layer_stacking_coexistence_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/layer_stacking_coexistence_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/layer_triple_catalog_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/layer_triple_catalog_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/layered_foundation_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/layered_foundation_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/lego_02_noncommutation_propagation_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/lego_02_noncommutation_propagation_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/lego_03_identity_via_indistinguishability_mixed_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/lego_03_identity_via_indistinguishability_mixed_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/lego_04_partial_trace_bounds_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/lego_04_partial_trace_bounds_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/lego_05_cl_rotor_pair_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/lego_05_cl_rotor_pair_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/lego_06_unsat_max_mixed_self_conj_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/lego_06_unsat_max_mixed_self_conj_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/lego_07_abc_vs_acb_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/lego_07_abc_vs_acb_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/lego_08_equiv_class_cardinality_2q_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/lego_08_equiv_class_cardinality_2q_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/lego_09_probe_size_lower_bound_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/lego_09_probe_size_lower_bound_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/lego_10_n01_commutator_zero_equivalence_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/lego_10_n01_commutator_zero_equivalence_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/lego_coherent_info_advanced_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/lego_coherent_info_advanced_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/lego_graph_cluster_states_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/lego_graph_cluster_states_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/lego_povm_measurement_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/lego_povm_measurement_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/leviathan_explore_as_constraint_satisfaction_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/leviathan_explore_as_constraint_satisfaction_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/lorentzian_geometry_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/lorentzian_geometry_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/multiqubit_cp_admissibility_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/multiqubit_cp_admissibility_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/path_entropy_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/path_entropy_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/phase7_baseline_validation_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/phase7_baseline_validation_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/phase7_divergence_analysis_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/phase7_divergence_analysis_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/phase_damping_fixed_point_geometry_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/phase_damping_fixed_point_geometry_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/phi0_packet_robustness_audit_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/phi0_packet_robustness_audit_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/q3_bipartite_analysis_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/q3_bipartite_analysis_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/qit_engine_companion_array_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/qit_engine_companion_array_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/qit_repair_comparison_surface_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/qit_repair_comparison_surface_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/ring_checkerboard_support_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/ring_checkerboard_support_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/sci_method_deep_popper_refutation_unsat_for_tautology_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/sci_method_deep_popper_refutation_unsat_for_tautology_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/shell_fuzz_jk_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/shell_fuzz_jk_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/shell_indexed_tensor_network_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/shell_indexed_tensor_network_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/sim_lego_entropy_relative_js_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/sim_lego_entropy_relative_js_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/sim_lego_entropy_shell_history_weighted_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/sim_lego_entropy_shell_history_weighted_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/sim_negative_bridge_cut_counterfeits_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/sim_negative_bridge_cut_counterfeits_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/sim_negative_global_shell_bridge_counterfeits_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/sim_negative_global_shell_bridge_counterfeits_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/tools_load_bearing_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/tools_load_bearing_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/torch_bit_phase_flip_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/torch_bit_phase_flip_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/torch_constraint_shells_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/torch_constraint_shells_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/torch_constraint_shells_v2_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/torch_constraint_shells_v2_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/torch_gnn_directional_gate_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/torch_gnn_directional_gate_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/torch_gnn_extended_training_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/torch_gnn_extended_training_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/torch_gnn_gradient_ref_ablation_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/torch_gnn_gradient_ref_ablation_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/torch_graph_integrated_pipeline_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/torch_graph_integrated_pipeline_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/torch_lindblad_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/torch_lindblad_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/torch_ratchet_gnn_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/torch_ratchet_gnn_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/torch_ratchet_pipeline_v2_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/torch_ratchet_pipeline_v2_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/torch_shells_gradient_flow_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/torch_shells_gradient_flow_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/torus_seat_entropy_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/torus_seat_entropy_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/twilight_zone_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/twilight_zone_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/w_ghz_analytic_resolution_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/w_ghz_analytic_resolution_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/werner_manifold_scan_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/werner_manifold_scan_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/werner_qwci_gap_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/werner_qwci_gap_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/werner_topology_boundary_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/werner_topology_boundary_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/weyl_nested_shell_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/weyl_nested_shell_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/weyl_spinor_hopf_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/weyl_spinor_hopf_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/z3_channel_composition_boundary_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/z3_channel_composition_boundary_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/a2_state/sim_results/z3_s6_unitary_impossibility_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/z3_s6_unitary_impossibility_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/sim_results/engine_4_operators_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/sim_results/engine_4_operators_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/sim_results/engine_terrain_couplings_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/sim_results/engine_terrain_couplings_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/sim_results/geom_symplectic_kahler_contact_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/sim_results/geom_symplectic_kahler_contact_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/sim_results/lego_dynamical_decoupling_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/sim_results/lego_dynamical_decoupling_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/sim_results/lego_gksl_kossakowski_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/sim_results/lego_gksl_kossakowski_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/sim_results/lego_info_geometry_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/sim_results/lego_info_geometry_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/sim_results/lego_lindblad_spectral_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/sim_results/lego_lindblad_spectral_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/sim_results/lego_positive_maps_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/sim_results/lego_positive_maps_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/sim_results/lego_quantum_thermo_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/sim_results/lego_quantum_thermo_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:19:20Z — canonical_abuse — system_v4/probes/sim_results/lego_toric_code_results.json
- timestamp: 2026-04-18T00:19:20Z
- class: canonical_abuse
- path/commit: system_v4/probes/sim_results/lego_toric_code_results.json
- why_critical: classification=canonical but missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:54:46Z canonical_abuse
- timestamp: 2026-04-18T00:54:46Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/f01_cross_11_pytorch_autograd_distinguishability_loss_results.json
- why critical: missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:54:46Z canonical_abuse
- timestamp: 2026-04-18T00:54:46Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/axis_couple_0_1_entropy_gradient_x_curvature_results.json
- why critical: missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:54:46Z canonical_abuse
- timestamp: 2026-04-18T00:54:46Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/axis_couple_3_0_phase_x_entropy_gradient_results.json
- why critical: missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:54:46Z canonical_abuse
- timestamp: 2026-04-18T00:54:46Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/geom_noncomm_hopf_weyl_proj_results.json
- why critical: missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:54:46Z canonical_abuse
- timestamp: 2026-04-18T00:54:46Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/f01n01_couple_cvc5_parity_on_joint_bound_results.json
- why critical: missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:54:46Z canonical_abuse
- timestamp: 2026-04-18T00:54:46Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/geom_noncomm_bch_results.json
- why critical: missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:54:46Z canonical_abuse
- timestamp: 2026-04-18T00:54:46Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/geom_noncomm_e3nn_results.json
- why critical: missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:54:46Z canonical_abuse
- timestamp: 2026-04-18T00:54:46Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/geom_noncomm_chirality_winding_results.json
- why critical: missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:54:46Z canonical_abuse
- timestamp: 2026-04-18T00:54:46Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/loop_vector_fields_results.json
- why critical: missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool

## META blocker 2026-04-18T00:54:46Z canonical_abuse
- timestamp: 2026-04-18T00:54:46Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/axis_couple_triple_0_3_5_results.json
- why critical: missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:54:46Z canonical_abuse
- timestamp: 2026-04-18T00:54:46Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/spectral_triple_reduction_connes_distance_results.json
- why critical: missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:54:46Z canonical_abuse
- timestamp: 2026-04-18T00:54:46Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/spectral_triple_chirality_gamma_grading_results.json
- why critical: missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:54:46Z canonical_abuse
- timestamp: 2026-04-18T00:54:46Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/spectral_triple_carrier_algebra_results.json
- why critical: missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:54:46Z canonical_abuse
- timestamp: 2026-04-18T00:54:46Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/spectral_triple_dirac_spectrum_results.json
- why critical: missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:54:46Z canonical_abuse
- timestamp: 2026-04-18T00:54:46Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/cross_holodeck_x_igt_results.json
- why critical: missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:54:46Z canonical_abuse
- timestamp: 2026-04-18T00:54:46Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/cross_fep_x_science_method_results.json
- why critical: missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:54:46Z canonical_abuse
- timestamp: 2026-04-18T00:54:46Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/cross_fep_x_igt_results.json
- why critical: missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T00:54:46Z canonical_abuse
- timestamp: 2026-04-18T00:54:46Z
- class: canonical_abuse
- path/commit: system_v4/probes/a2_state/sim_results/cross_science_method_x_leviathan_results.json
- why critical: missing TOOL_INTEGRATION_DEPTH

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/L7_weyl_extraction_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/L8_chiral_density_bookkeeping_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/SA12_wilczek_zee_curvature_sympy_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/bridge_entropy_inequality_guardrails_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/bridge_to_rhoab_construction_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/clifford_so_homomorphism_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/clifford_weyl_transport_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/conformal_structure_constraint_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/cvc5_frege_system_constraint_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/cvc5_proof_complexity_size_constraint_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/elliptic_pde_constraint_canonical_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/fiber_loop_law_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/foundation_hopf_torus_geomstats_clifford_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/foundation_pauli_bloch_backprop_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/fourier_uncertainty_constraint_canonical_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/frame_bundle_structure_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/gerbe_derived_stack_pairwise_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/groebner_basis_constraint_canonical_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/gtower_triple_su2_u1_spin_ordering_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/gudhi_bloch_sphere_2d_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/gudhi_capability_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/gudhi_concurrence_filtration_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/hardy_littlewood_maximal_canonical_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/heat_equation_constraint_canonical_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/hopf_fiber_equivalence_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/kahler_geometry_constraint_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/lego_entropy_bipartite_cut_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/lego_entropy_extremal_density_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/lego_entropy_finite_blocklength_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/lego_entropy_smooth_one_shot_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/lego_entropy_spectral_families_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/lego_weyl_hopf_spinor_bridge_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/lego_weyl_hypergraph_local_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/lego_weyl_pauli_transport_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/leviathan_authority_entropy_operator_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/leviathan_gudhi_stability_persistence_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/leviathan_xgi_coalition_hypergraph_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/negative_phi0_candidate_disqualifiers_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/negative_xi_winner_disqualifiers_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/newton_polytope_constraint_canonical_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/plancherel_theorem_constraint_canonical_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/pyg_capability_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/qit_entropy_companion_array_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/qit_moloch_coordination_trap_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/qit_predictive_world_model_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/qit_strong_coupling_landauer_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/qit_szilard_record_translation_lane_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/qit_szilard_reverse_recovery_companion_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/qit_weyl_carnot_bridge_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/qit_weyl_hypergraph_companion_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/qit_weyl_szilard_geometry_bridge_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/rsk_correspondence_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/rustworkx_capability_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sa10_wilczek_zee_curvature_boundary_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_geometry_algebraic_cycle_hodge_class_constraint_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_geometry_automorphic_form_cuspidality_constraint_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_geometry_deligne_cohomology_regulator_constraint_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_geometry_langlands_functoriality_constraint_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_geometry_shimura_variety_reciprocity_constraint_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_hecke_correspondence_shimura_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/sim_shimura_variety_canonical_model_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/spectral_triple_weyl_hopf_coupling_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/spinor_harmonics_constraint_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/teleportation_fidelity_canonical_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/toponetx_capability_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/torch_eigendecomp_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/torch_husimi_q_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/torch_l1_coherence_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/torch_mutual_info_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/torch_quantum_discord_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/torch_re_coherence_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/torch_wigner_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/torch_z_measurement_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/torsion_curvature_splitting_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/tropical_geometry_constraint_canonical_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/wave_equation_constraint_canonical_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/weyl_geometry_alignment_overlay_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/weyl_geometry_ladder_audit_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/xgi_capability_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:17:53Z canonical_abuse
- timestamp: 2026-04-18T02:17:53Z
- class: canonical_abuse
- path_or_commit: /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/z3_dephasing_symmetry_guard_results.json
- why_critical: canonical result surface lacks required contract fields named by TIER_META.

## META blocker 2026-04-18T02:42:05Z — canonical_abuse — system_v4/probes/a2_state/sim_results/sim_shimura_reciprocity_results.json
- timestamp: 2026-04-18T02:42:05Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/sim_shimura_reciprocity_results.json
- why_critical: classification is canonical while missing TOOL_INTEGRATION_DEPTH; this does not satisfy the Tier META canonical contract.

## META blocker 2026-04-18T02:42:05Z — canonical_abuse — system_v4/probes/a2_state/sim_results/quillen_adjunction_derived_functor_results.json
- timestamp: 2026-04-18T02:42:05Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/quillen_adjunction_derived_functor_results.json
- why_critical: classification is canonical while missing TOOL_INTEGRATION_DEPTH; this does not satisfy the Tier META canonical contract.

## META blocker 2026-04-18T02:42:05Z — canonical_abuse — system_v4/probes/a2_state/sim_results/qit_weyl_geometry_repair_comparison_surface_results.json
- timestamp: 2026-04-18T02:42:05Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/qit_weyl_geometry_repair_comparison_surface_results.json
- why_critical: classification is canonical while missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool; this does not satisfy the Tier META canonical contract.

## META blocker 2026-04-18T02:42:05Z — canonical_abuse — system_v4/probes/a2_state/sim_results/torch_chiral_overlap_results.json
- timestamp: 2026-04-18T02:42:05Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/torch_chiral_overlap_results.json
- why_critical: classification is canonical while missing TOOL_INTEGRATION_DEPTH; this does not satisfy the Tier META canonical contract.

## META blocker 2026-04-18T02:42:05Z — canonical_abuse — system_v4/probes/a2_state/sim_results/lego_nested_hopf_tori_results.json
- timestamp: 2026-04-18T02:42:05Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/lego_nested_hopf_tori_results.json
- why_critical: classification is canonical while missing TOOL_INTEGRATION_DEPTH; this does not satisfy the Tier META canonical contract.

## META blocker 2026-04-18T02:42:05Z — canonical_abuse — system_v4/probes/a2_state/sim_results/gudhi_3qubit_bridge_results.json
- timestamp: 2026-04-18T02:42:05Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/gudhi_3qubit_bridge_results.json
- why_critical: classification is canonical while missing TOOL_INTEGRATION_DEPTH; this does not satisfy the Tier META canonical contract.

## META blocker 2026-04-18T02:42:05Z — canonical_abuse — system_v4/probes/a2_state/sim_results/qit_weyl_geometry_companion_results.json
- timestamp: 2026-04-18T02:42:05Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/qit_weyl_geometry_companion_results.json
- why_critical: classification is canonical while missing TOOL_INTEGRATION_DEPTH, load_bearing_ladder_tool; this does not satisfy the Tier META canonical contract.

## META blocker 2026-04-18T02:42:05Z — canonical_abuse — system_v4/probes/a2_state/sim_results/geomstats_ratchet_trajectory_results.json
- timestamp: 2026-04-18T02:42:05Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/geomstats_ratchet_trajectory_results.json
- why_critical: classification is canonical while missing TOOL_INTEGRATION_DEPTH; this does not satisfy the Tier META canonical contract.

## META blocker 2026-04-18T02:42:05Z — canonical_abuse — system_v4/probes/a2_state/sim_results/homotopy_limit_colimit_results.json
- timestamp: 2026-04-18T02:42:05Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/homotopy_limit_colimit_results.json
- why_critical: classification is canonical while missing TOOL_INTEGRATION_DEPTH; this does not satisfy the Tier META canonical contract.

## META blocker 2026-04-18T02:42:05Z — canonical_abuse — system_v4/probes/a2_state/sim_results/c2_topology_expansion_results.json
- timestamp: 2026-04-18T02:42:05Z
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/c2_topology_expansion_results.json
- why_critical: classification is canonical while missing TOOL_INTEGRATION_DEPTH; this does not satisfy the Tier META canonical contract.

## 2026-04-18T03:23:50Z — META blocker
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/e3nn_relay_equivariance_results.json
- why_critical: top-level classification is canonical while uppercase TOOL_INTEGRATION_DEPTH is absent; canonical by process contract did not survive this check.

## 2026-04-18T03:23:50Z — META blocker
- class: canonical_abuse
- path: system_v4/probes/a2_state/sim_results/e3nn_tensor_product_results.json
- why_critical: top-level classification is canonical while uppercase TOOL_INTEGRATION_DEPTH is absent; canonical by process contract did not survive this check.
## META blocker 2026-04-18T04:29:17Z banned_verb
- timestamp: 2026-04-18T04:29:17Z
- class: banned_verb
- path_or_commit: /Users/joshuaeisenhart/wiki/harness/AUDIT.md
- why_critical: prohibited-construction hit inside harness narrative surface

## META blocker 2026-04-18T04:29:17Z banned_verb
- timestamp: 2026-04-18T04:29:17Z
- class: banned_verb
- path_or_commit: /Users/joshuaeisenhart/wiki/harness/AUDIT.md
- why_critical: prohibited-construction hit inside harness narrative surface

## META blocker 2026-04-18T04:29:17Z banned_verb
- timestamp: 2026-04-18T04:29:17Z
- class: banned_verb
- path_or_commit: /Users/joshuaeisenhart/wiki/harness/AUDIT.md
- why_critical: prohibited-construction hit inside harness narrative surface

## META blocker 2026-04-18T04:29:17Z banned_verb
- timestamp: 2026-04-18T04:29:17Z
- class: banned_verb
- path_or_commit: /Users/joshuaeisenhart/wiki/harness/CORE.md
- why_critical: prohibited-construction hit inside harness narrative surface

## META blocker 2026-04-18T04:29:17Z banned_verb
- timestamp: 2026-04-18T04:29:17Z
- class: banned_verb
- path_or_commit: /Users/joshuaeisenhart/wiki/harness/CORE.md
- why_critical: prohibited-construction hit inside harness narrative surface

## META blocker 2026-04-18T04:29:17Z banned_verb
- timestamp: 2026-04-18T04:29:17Z
- class: banned_verb
- path_or_commit: /Users/joshuaeisenhart/wiki/harness/CORE.md
- why_critical: prohibited-construction hit inside harness narrative surface

## META blocker 2026-04-18T04:29:17Z banned_verb
- timestamp: 2026-04-18T04:29:17Z
- class: banned_verb
- path_or_commit: /Users/joshuaeisenhart/wiki/harness/CORE.md
- why_critical: prohibited-construction hit inside harness narrative surface

## META blocker 2026-04-18T04:29:17Z banned_verb
- timestamp: 2026-04-18T04:29:17Z
- class: banned_verb
- path_or_commit: /Users/joshuaeisenhart/wiki/harness/CORE.md
- why_critical: prohibited-construction hit inside harness narrative surface

## META blocker 2026-04-18T04:29:17Z banned_verb
- timestamp: 2026-04-18T04:29:17Z
- class: banned_verb
- path_or_commit: /Users/joshuaeisenhart/wiki/harness/CORE.md
- why_critical: prohibited-construction hit inside harness narrative surface

## META blocker 2026-04-18T04:29:17Z banned_verb
- timestamp: 2026-04-18T04:29:17Z
- class: banned_verb
- path_or_commit: /Users/joshuaeisenhart/wiki/harness/CORE.md
- why_critical: prohibited-construction hit inside harness narrative surface

## META blocker 2026-04-18T04:29:17Z banned_verb
- timestamp: 2026-04-18T04:29:17Z
- class: banned_verb
- path_or_commit: /Users/joshuaeisenhart/wiki/harness/CORE.md
- why_critical: prohibited-construction hit inside harness narrative surface
## META correction 2026-04-18T04:30:13Z
- supersedes: 2026-04-18T04:29:17Z banned_verb blocker entries for /Users/joshuaeisenhart/wiki/harness/AUDIT.md and /Users/joshuaeisenhart/wiki/harness/CORE.md
- why: the cited text was example, quote, or banned-list context inside harness guidance files rather than newly-authored narrative prose. Those items do not survive the conservative critical threshold.
