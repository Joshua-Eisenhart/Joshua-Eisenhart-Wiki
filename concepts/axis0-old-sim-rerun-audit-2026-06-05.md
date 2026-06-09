---
title: Axis0 Old Sim Rerun Audit 2026-06-05
created: 2026-06-05
updated: 2026-06-05
type: concept
tags: [concept, axis0, sims, audit, formal-scout, entropy, jk-fuzz]
sources:
  - /tmp/ax0_julia_results.json
  - /tmp/cfc_chirality_results.json
  - /tmp/qubit_scaling_sweep_f01n01_structure_results.json
  - /tmp/old_sim_rerun_20260605/
  - /Users/joshuaeisenhart/Codex-Ratchet/system_v5/julia_carrier/axis0_entropy_monotone.jl
  - /Users/joshuaeisenhart/Codex-Ratchet/system_v5/julia_carrier/nonchiral_carrier_f01n01_negative_control.jl
  - /Users/joshuaeisenhart/Codex-Ratchet/system_v5/julia_carrier/qubit_scaling_sweep_f01n01_structure_object.jl
  - /Users/joshuaeisenhart/Codex-Ratchet/system_v5/ops/formal_scouts/sim_xi_phi0_path_weighted_cut_candidate_probe.py
  - /Users/joshuaeisenhart/Codex-Ratchet/system_v5/ops/formal_scouts/sim_xi_phi0_boundary_capacity_cut_candidate_probe.py
claim_ceiling: rerun audit and result-status router only; no source edits, no script edits, no proof, no final Axis0, no admitted gravity/dark-energy/ToE claim
---

# Axis0 Old Sim Rerun Audit 2026-06-05

## Claim ceiling

This page records a bounded Hermes-controlled rerun/audit of old Axis0-adjacent sim surfaces. It is a result-status router, not a theorem.

It does not admit final `Axis0`, final `Xi`, final `Phi0`, gravity, dark energy, holography, ER=EPR, a universal clock, or a ToE. The reruns below only show which old scripts still run under a no-source-edit gate and what their own result ceilings say.

## Controller boundary

- Repo source state was dirty before the rerun tranche, so no source edits were allowed.
- Codex2 did the heavy read-only audit. It could not write its requested `/tmp` audit artifact because the read-only sandbox blocked the write, but it returned a receipt.
- Hermes reran only scripts that were either already `/tmp`-writing or copied into a fresh `/tmp` directory before execution.
- No old sim script was edited.
- No repo result file was intentionally written by the rerun tranche.

## Codex2 heavy-audit receipt

Codex2 audited 16 script families and 25 result/index surfaces, plus 30 embedded Axis0 index rows. Its key result was conservative:

- `formal_scout_readiness_index.json` reports a large indexed estate, but the live `system_v5/ops/formal_scouts/results/` checkout had only three direct JSON results at the time of audit.
- The index is therefore a map, not admission evidence, until missing result artifacts are restored or freshly rerun.
- The strongest directly observed blocker is the old flat-`S2`/Popper-Reidemeister style control pressure against promoting linking-number-as-mass or scratch mass claims.
- The strongest positive in the audit was index-only, not a live direct result artifact: `holographic_boundary_path_ensemble_axis0_fep_selection`.

## Verified rerun table

| Script/result family | Rerun mode | Exit | Result artifact | Local finding | Claim ceiling |
|---|---:|---:|---|---|---|
| `axis0_entropy_monotone.jl` | direct Julia, writes `/tmp` | 0 | `/tmp/ax0_julia_results.json` | `f01_finite=true`, `n01_sensitive=true`, `axis0_split_real=true`; `n01_comm_norm=0.2214721729`; outer `MI_LR=0.1732867951`; outer `CI_LR=-0.5198603854` | candidate only; `promotion_allowed=false` |
| `nonchiral_carrier_f01n01_negative_control.jl` | direct Julia, writes `/tmp` | 0 | `/tmp/cfc_chirality_results.json` | Non-chiral and chiral finite carriers can both satisfy the minimal F01+N01 witness pair; chirality is admitted as a chosen/extra structural principle, not forced by F01+N01 alone | `diagnostic_only_negative_control`; no geometry/bridge/physics admission |
| `qubit_scaling_sweep_f01n01_structure_object.jl` | direct Julia, writes `/tmp` | 0 | stdout plus malformed/minimal JSON at `/tmp/qubit_scaling_sweep_f01n01_structure_results.json` | stdout says q=1 fails nested-shell distinguishability; q=2/q=3/q=4 pass this A-F battery; the expected “2 qubits fail, 3 succeeds” observation is not reproduced under this criterion set | stdout diagnostic only; JSON broken/minimal; `promotion_allowed=false` by stdout |
| `sim_xi_phi0_path_weighted_cut_candidate_probe.py` | copied to fresh `/tmp` dir before running | 0 | `/tmp/old_sim_rerun_20260605/formal_scouts_temp_1780701246/results/xi_phi0_path_weighted_cut_candidate_probe_results.json` | `all_pass=true`, but the candidate is explicitly killed: it does not beat the zero-phase coherent-information control | formal scout only; final `Xi/Phi0/Axis0` blocked |
| `sim_xi_phi0_boundary_capacity_cut_candidate_probe.py` | copied to fresh `/tmp` dir before running | 0 | `/tmp/old_sim_rerun_20260605/formal_scouts_temp_1780701246/results/xi_phi0_boundary_capacity_cut_candidate_probe_results.json` | `all_pass=true`, but the candidate is explicitly killed: zero/uniform/random capacity controls beat the candidate | formal scout only; final `Xi/Phi0/Axis0`, holography, and physics blocked |

## What we have so far

The old sim estate is useful, but the usable statement is narrow:

1. Some finite Axis0-adjacent diagnostic scripts still run cleanly without edits.
2. F01+N01 can be witnessed locally in finite carrier toys.
3. Chirality is not forced by the minimal F01+N01 witness pair alone.
4. Two Xi/Phi0 candidate scouts are executable and tool-using, but both are negative candidates under their own controls.
5. The formal-scout estate needs direct result restoration or fresh reruns before index-level claims can be treated as current evidence.

## Live blockers and falsifiers

- A local `all_pass=true` formal scout is not admission when `promotion_allowed=false` and the result itself says the candidate is killed.
- The qubit-scaling stdout is informative, but its JSON serialization is broken or key-corrupted, so it cannot be promoted as a clean machine-readable result until repaired.
- JAX candidates such as `ax0_jax.py`, `golden_weyl_jax.py`, and `npc2_connection_geometry_jax.py` were not rerun in this Hermes runtime because `jax` was not installed for `python3`.
- V4 bridge/formal-scout scripts that write into repo result directories remain blocked for immediate rerun unless copied into `/tmp` or explicitly authorized to update repo results.
- Linking-number-as-mass and gravity/cosmology identity claims remain blocked by the standing flat-`S2`/control pressure and by lack of a current direct admission surface.

## Relation to the source-teeth map

This audit sharpens [[axis0-physics-source-teeth-map]] without promoting it. The source-teeth page names decisive tests and live routes; this page records that the currently rerun old sims mostly support the **status of the routes**, not the final claims.

Most importantly:

- Shell/cut and `Xi_* -> rho_AB -> Phi0` remain live routes, not solved bridges.
- JK/path weighting remains a candidate probe family, not an admitted physics mechanism.
- Chirality remains structurally important but not forced by the minimal root pair alone.
- Gravity/dark-energy/time readouts still need separate finite witnesses, controls, and direct result surfaces.

## Next honest packet

The next non-editing packet should be one of these:

1. **Result-estate restoration audit** — locate where the missing formal-scout result JSONs went, compare against `formal_scout_readiness_index.json`, and classify which entries are direct artifacts versus index-only references.
2. **Qubit-scaling JSON repair packet** — repair only the JSON serialization path for `qubit_scaling_sweep_f01n01_structure_object.jl`, rerun it, and preserve the stdout caveat that q=2 already passes under the current A-F battery.
3. **Temp-copy Xi/Phi0 expansion** — rerun more Xi/Phi0 candidates from copied `/tmp` scripts only, preserving `promotion_allowed=false` and treating negative candidates as useful kills.
4. **JAX runtime gate** — find or create a Python environment with `jax`, then rerun the three Codex2-shortlisted JAX scripts without editing sources.

Do not use this page to authorize source edits or repo result writes. Use it as a status ledger before deciding which old sim family deserves a bounded repair or rerun packet.

## Related pages

- [[axis0-physics-source-teeth-map]]
- [[field-wide-compression-probe-contract]]
- [[field-wide-compression-packet-template]]
- [[jk-fuzz-field]]
- [[sim-run-catalogue-and-result-family-router]]
- [[formal-scout-readiness-index-router]]
- [[negative-sims-and-kill-tests-support]]
- [[constraint-geometry-axis0-separation]]
