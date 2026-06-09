last_updated: 2026-04-17T08:40:07Z

# Tier B — Clifford / Pauli (B5)

Historical Tier B B5 compile/source inventory. `canonical` labels are
source/result self-classification or filenames, not current `canonical by
process`; the new probes were `exists` only here.

Historical source-inventory status: written
Historical gate at write time: pending runner
Worker: B5
Scope: `sim_clifford*.py`, `sim_pauli*.py`, `classical_baseline_*pauli*.py`, `ops/queue_tier_b.txt`, `~/wiki/projects/codex-ratchet/tier_b_clifford_pauli.md`

Method
- Read order followed from the B5 brief and Tier B spawn plan.
- Inventory is compile-only plus source/result scan.
- No sims were executed in this pass.
- Step-1 shell-local gaps only; no coupling, coexistence, topology-variant, emergence, or bridge work added.

## Existing inventory before B5 writes

### Shell-local direct-prefix files
Source/result self-classification: canonical at write time
- `sim_clifford_capability.py`
- `sim_clifford_chirality_admissible_generators.py`
- `sim_clifford_deep_cl3_rotor_double_cover.py`
- `sim_clifford_generator_basis.py`
- `sim_clifford_so_homomorphism.py`
- `sim_clifford_torch_foundation.py`
- `sim_pauli_generator_basis.py`
- `sim_pauli_algebra_relations.py`

Classical baseline
- `classical_baseline_cl3_rotor_pauli_rep.py`
- `classical_baseline_cl6_kron_pauli_rep.py`

Broken
- none found in the shell-local direct-prefix bucket

### Direct-prefix later-lane files present but not gap candidates for Step 1
Source/result self-classification: canonical at write time
- `sim_clifford_holo_dirac_bridge_claims_canonical.py`
- `sim_clifford_holo_dirac_pairwise_coupling.py`

Classical baseline
- `sim_clifford_contact_kahler_riemannian_spectral_triple_fiber_holonomy_7shell_coupling_canonical.py`
- `sim_clifford_fiber_assoc_symplectic_coupling_canonical.py`
- `sim_clifford_gerbe_symplectic_bridge_claims_canonical.py`
- `sim_clifford_gerbe_symplectic_emergence_quantities.py`
- `sim_clifford_gerbe_symplectic_pairwise_coupling.py`
- `sim_clifford_gerbe_symplectic_topology_variants.py`
- `sim_clifford_gerbe_symplectic_triple_coexistence.py`
- `sim_clifford_spinor_contact_kahler_riemannian_spectral_triple_6shell_coupling_canonical.py`
- `sim_clifford_spinor_riemannian_connection_holonomy_fiber_assoc_moment_index_chern_10shell_coupling_canonical.py`
- `sim_clifford_weyl_contact_bridge_claims_canonical.py`
- `sim_clifford_weyl_contact_emergence_quantities.py`
- `sim_clifford_weyl_contact_pairwise_coupling.py`
- `sim_clifford_weyl_contact_topology_variants.py`
- `sim_clifford_weyl_contact_triple_coexistence.py`
- `sim_clifford_weyl_pairwise_coupling.py`

Broken
- `sim_clifford_holo_dirac_emergence_quantities.py`
- `sim_clifford_holo_dirac_topology_variants.py`
- `sim_clifford_holo_dirac_triple_coexistence.py`

## Shell-local gaps identified before writing
- No direct shell-local row isolated the Clifford even/odd grade partition with an UNSAT gate excluding nonzero mixed parity collapse.
- No direct shell-local row isolated rotor-plane invariance in Cl(3): plane bivector stability, transverse-axis stability, and 2π / 4π rotor boundary behavior.
- No direct shell-local row isolated Pauli projector reconstruction from Bloch-axis data.
- No direct shell-local row isolated the Z-centralizer constraint inside the Pauli span with an UNSAT gate excluding nonzero X/Y commuting witnesses.

Residual shell-local gaps still open after this pass
- Pauli probe-response / expectation-value local packet is still separate work if needed.
- Clifford local bivector commutator / stabilizer packet beyond the rotor-plane row is still separate work if needed.

## New probes written in this pass
All four new files are `exists` only in this report. They were not executed here.

1. `sim_clifford_even_odd_grade_partition.py`
- commit: `7c4736e8162cf5050e29870d65dc0bbf5d6a290a`
- queue: `sim_clifford_even_odd_grade_partition`
- shell-local focus: even/odd grade split in Cl(3)
- load-bearing tools: `clifford`, `z3`

2. `sim_clifford_rotor_plane_invariance.py`
- commit: `9ba253ac0f48d9677ada4003c053083ddf8b8dd0`
- queue: `sim_clifford_rotor_plane_invariance`
- shell-local focus: e12-plane rotor action, bivector stability, 2π / 4π boundary
- load-bearing tools: `clifford`

3. `sim_pauli_projector_reconstruction.py`
- commit: `8a5f84a66ff977d3e72ff93ca211fc7699cb9ea2`
- queue: `sim_pauli_projector_reconstruction`
- shell-local focus: `rho(n) = (I + n·sigma)/2` projector recovery on Bloch axes
- load-bearing tools: `sympy`

4. `sim_pauli_centralizer_constraint.py`
- commit: `0640b77553f09d9af2b4bbe0e6bd649213489830`
- queue: `sim_pauli_centralizer_constraint`
- shell-local focus: Z-centralizer inside `aI + bX + cY + dZ`
- load-bearing tools: `z3`, `sympy`

## Queue + steward audit lines appended
Queue lines appended to `ops/queue_tier_b.txt`
- `sim_clifford_even_odd_grade_partition`
- `sim_clifford_rotor_plane_invariance`
- `sim_pauli_projector_reconstruction`
- `sim_pauli_centralizer_constraint`

Steward log lines appended in canonical format to `~/wiki/projects/codex-ratchet/_steward_log.md`
- `2026-04-17T08:38:23Z hermes-b5 B5 probe=sim_clifford_even_odd_grade_partition commit=7c4736e8162cf5050e29870d65dc0bbf5d6a290a enqueued=ops/queue_tier_b.txt`
- `2026-04-17T08:38:57Z hermes-b5 B5 probe=sim_clifford_rotor_plane_invariance commit=9ba253ac0f48d9677ada4003c053083ddf8b8dd0 enqueued=ops/queue_tier_b.txt`
- `2026-04-17T08:39:16Z hermes-b5 B5 probe=sim_pauli_projector_reconstruction commit=8a5f84a66ff977d3e72ff93ca211fc7699cb9ea2 enqueued=ops/queue_tier_b.txt`
- `2026-04-17T08:39:37Z hermes-b5 B5 probe=sim_pauli_centralizer_constraint commit=0640b77553f09d9af2b4bbe0e6bd649213489830 enqueued=ops/queue_tier_b.txt`

## Note on shared-index carryover
- The first B5 commit also captured a pre-staged out-of-scope file already sitting in the shared git index: `system_v4/probes/sim_u1_charge_sector_selection_shell_canonical.py`.
- The B5 probe listed above is still present and queued correctly.
- Subsequent B5 commits used `git commit --only` to keep the remaining probe commits scope-tight.
