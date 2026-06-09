last_updated: 2026-04-17T08:45:36Z

# Tier B Weyl

April 2026 source-inventory snapshot. `canonical` below is source/result self-classification for Tier B shell-local work, not current maturity, promotion, or live formal readiness.

Status: write_complete
Worker: B3
Scope: `sim_weyl_*`, `~/wiki/projects/codex-ratchet/tier_b_weyl.md`, `ops/queue_tier_b.txt`
Execution note: this worker did not execute sims. Inventory labels below come from source self-classification plus `python3 -m py_compile`, not from reruns.

## Inventory

Overall `sim_weyl_*.py` inventory seen in this snapshot:
- total files: 85
- canonical: 27
- classical_baseline: 58
- broken: 0

Step-1 shell-local subset retained for this worker:
- shell-local files: 46
- shell-local canonical: 22
- shell-local classical_baseline: 24
- shell-local broken: 0

Non-shell-local / deferred from this worker:
- 39 files are pairwise/triple/topology/emergence/bridge or visibly cross-layer (`hopf`, `dirac`, `mera`, `gerbe`, `contact`, `symplectic`, `toric`, composed-stack surfaces)
- explicit cross-layer examples that were not treated as Step-1 shell-local: `sim_weyl_spinor_hopf.py`, `sim_weyl_hopf_tori.py`, `sim_weyl_hopf_couple_chirality_x_fiber_winding.py`, all `*_pairwise_coupling.py`, `*_triple_coexistence.py`, `*_topology_variants.py`, `*_emergence_quantities.py`, and `*_bridge_claims_canonical.py`

Existing shell-local canonical anchors before this batch:
- `sim_weyl_nested_shell.py`
- `sim_weyl_geometry_rescaling_shell.py`
- `sim_weyl_group_a2_root_system.py`
- `sim_weyl_group_bc2_root_system.py`
- `sim_weyl_group_g2_shell_local.py`
- `sim_weyl_torch_foundation.py`
- `sim_weyl_two_model_crosscheck.py`
- `sim_weyl_character_formula_constraint_canonical.py`
- `sim_weyl_deep_chirality_flip_requires_even_rotor_count.py`
- `sim_weyl_deep_cross_cl3_vs_sympy_pauli_decomp.py`
- `sim_weyl_deep_left_right_projector_unsat_mix.py`
- `sim_weyl_deep_pauli_joint_commute_unsat.py`
- audit-like canonicals already present but not used as the main gap-fill targets: `sim_weyl_geometry_alignment_overlay.py`, `sim_weyl_geometry_ladder_audit.py`, `sim_weyl_geometry_translation_targets.py`

Shell-local classical_baseline / repair-helper surfaces still present:
- chirality / local bookkeeping baselines: `sim_weyl_chirality_bipartite.py`, `sim_weyl_chirality_g_reduction_noncomm.py`, `sim_weyl_delta_packet.py`, `sim_weyl_dof_analysis.py`
- geometry / repair / audit baselines: `sim_weyl_ambient_vs_engine_overlay.py`, `sim_weyl_geometry_alignment_overlay_v2.py`, `sim_weyl_geometry_carrier_array.py`, `sim_weyl_geometry_carrier_compare_refinement.py`, `sim_weyl_geometry_constraint_audit.py`, `sim_weyl_geometry_family_expansion.py`, `sim_weyl_geometry_graph_proof_alignment.py`, `sim_weyl_geometry_lab_matrix.py`, `sim_weyl_geometry_lego_registry_supplement.py`, `sim_weyl_geometry_multifamily_expansion.py`, `sim_weyl_geometry_proof_pressure.py`, `sim_weyl_geometry_repair_priority.py`, `sim_weyl_geometry_repair_priority_v2.py`
- hypergraph / helper / mixed local surfaces: `sim_weyl_hypergraph_admission_helper.py`, `sim_weyl_hypergraph_follow_on.py`, `sim_weyl_hypergraph_geometry_bridge.py`, `sim_weyl_relay_gradient_sweep.py`
- mis-scoped-for-Step-1 but still source-self-classified classical baselines in the `sim_weyl_*` namespace: `sim_weyl_g2_exceptional_emergence.py`, `sim_weyl_triple_a2_bc2_g2_coexistence.py`, plus coupling-named files outside this shell-local list

## Shell-local gaps identified

The Step-1 gaps that were still open inside the Weyl namespace were:
1. finite higher-rank simply-laced packet beyond A2
2. finite exceptional non-simply-laced packet beyond G2
3. affine alcove packets for local Weyl-wall admissibility
4. chamber adjacency / wall-local open-sector packet
5. fundamental-weight / dominant-cone local packet
6. keep all of the above shell-local only; anything touching Hopf, Dirac, MERA, Pauli composition, or bridge surfaces is deferred

Deferred-but-still-local future gaps after this batch:
- affine G2 alcove packet
- B3/C3 higher-rank finite packets
- denominator / rho-shift local packet if kept strictly shell-local
- more exact dominant-order packets beyond the A2 fundamental-weight base case

## New probes written in this batch

Each new probe is `SIM_TEMPLATE`-style, `classification = "canonical"`, includes positive + negative + boundary sections, and uses Tier-A-capable tools load-bearing in-source.

1. `sim_weyl_group_d4_triality_shell_local.py`
   - commit: `1fe5f3a5d5a83150a19c5bee1eacff531d222aac`
   - local gap filled: higher-rank simply-laced finite Weyl packet (D4), even sign-parity exclusion, triality-arm Dynkin local structure
2. `sim_weyl_group_f4_shell_local.py`
   - commit: `7c183cf09e1bf70a157ca660c5656f8468b15913`
   - local gap filled: exceptional finite Weyl packet (F4), mixed long/short root local structure, local simple-reflection closure
3. `sim_weyl_affine_a2_alcove_shell_local.py`
   - commit: `ca3f38a5a667545c1369da5d7b901d643b2f147e`
   - local gap filled: affine A2 fundamental alcove inequalities and wall packet
4. `sim_weyl_affine_c2_alcove_shell_local.py`
   - commit: `2a8e037fe3f8fe9332ab6ec8d78bc411ee87ecb7`
   - local gap filled: affine C2 fundamental alcove inequalities and highest-root coefficients
5. `sim_weyl_chamber_adjacency_a2_shell_local.py`
   - commit: `4be5581de05897ea8b9bf4e15bee5efa179fd1a3`
   - local gap filled: open-chamber adjacency / wall-sector packet for A2
6. `sim_weyl_fundamental_weights_a2_shell_local.py`
   - commit: `c9679a2ec4e2b0d76293e44818a052107d4fd9a6`
   - local gap filled: inverse-Cartan / fundamental-weight / dominant-cone local packet for A2

## Queue + steward-log updates completed

Appended to `ops/queue_tier_b.txt`:
- `sim_weyl_group_d4_triality_shell_local`
- `sim_weyl_group_f4_shell_local`
- `sim_weyl_affine_a2_alcove_shell_local`
- `sim_weyl_affine_c2_alcove_shell_local`
- `sim_weyl_chamber_adjacency_a2_shell_local`
- `sim_weyl_fundamental_weights_a2_shell_local`

Appended canonical steward log lines to `~/wiki/projects/codex-ratchet/_steward_log.md` for each of the six commits.

## Stop-rule check

- no sims executed here
- no coupling / coexistence / topology-variant / emergence / bridge authoring added
- no non-Weyl probe source was modified
- work stopped after writing, committing, enqueueing, and updating this layer report
