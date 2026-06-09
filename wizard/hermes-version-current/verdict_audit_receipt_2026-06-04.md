# Codex2 Verdict Audit Receipt

Generated: 2026-06-04
Repo: `/Users/joshuaeisenhart/Desktop/Codex Ratchet`

This is a fresh controller-side audit of the 9 pending codex2 verdicts. I read the
`/tmp/cx_*.out` outputs, inspected the current Julia source files, inspected the
result JSONs that exist, and reran every genuine candidate with an actual Julia
source path under `julia --project=system_v5/julia_carrier` using a 120s
sleep/kill hard cap.

Live-process preflight was attempted before reruns, but this sandbox could not
read the process table:

- `ps -axo ...` -> `operation not permitted`
- `pgrep -af ...` -> `Cannot get process list`

No CTMRG/PEPS3D contraction was used in any rerun. Where PEPS3D is mentioned in
the audited artifacts, it is explicitly a blocked/non-admitted anchor or boundary,
not the carrier used for the rerun.

## Classification Table

| Verdict | cx output | Result JSON audited | Source audited | Classification |
|---|---|---|---|---|
| order-null `survives` | `/tmp/cx_defl_ordernull.out` | `system_v5/julia_carrier/layers/deflation_order_null_results.json` | `system_v5/julia_carrier/layers/deflation_order_null.jl` | `AUDIT-CONFIRMED` |
| ratchet-survivor `deflated` | `/tmp/cx_defl_ratchet.out` | `layers/deflation_ratchet_survivor_results.json`; table path `system_v5/julia_carrier/layers/ratchet_survivor_reach_killtest_results.json` is the parent mixed kill-test, not the deflation result | `layers/deflation_ratchet_survivor.jl` | `AUDIT-CONFIRMED` |
| Hopfield-basin `deflated` | `/tmp/cx_defl_hopfield.out` | `system_v5/julia_carrier/hopfield/deflation_hopfield_basin_results.json`; not missing | `system_v5/julia_carrier/hopfield/deflation_hopfield_basin.jl` | `AUDIT-CONFIRMED` |
| substrate-band `survives` | `/tmp/cx_defl_substrate.out` | `system_v5/julia_carrier/layers/deflation_substrate_band_results.json` | `system_v5/julia_carrier/layers/deflation_substrate_band.jl` | `AUDIT-CONFIRMED` |
| cocycle 3rd-section `reproduces` | `/tmp/cx_third_section.out` | `system_v5/julia_carrier/layers/cocycle_third_section_results.json`; not missing | `system_v5/julia_carrier/layers/cocycle_third_section.jl` | `AUDIT-CONFIRMED` |
| N=64 carrier `reached` | `/tmp/cx_n64_carrier.out` | `layers/carrier_n64_attack_results.json`; not missing | `layers/carrier_n64_attack.jl` | `AUDIT-CONFIRMED` |
| curvature-frame `unifies` | `/tmp/cx_curvature_frame.out` | `layers/curvature_unified_frame_results.json`; actual verdict is `per_layer_needed` | `layers/curvature_unified_frame.jl` | `FABRICATED` |
| cocycle full-eta monopole `present` | `/tmp/cx_full_monopole.out` | `system_v5/julia_carrier/layers/cocycle_full_monopole_results.json` | `system_v5/julia_carrier/layers/cocycle_full_monopole.jl` | `AUDIT-CONFIRMED` |
| neural-on-manifold `nonflat_changes_network` | `/tmp/cx_neural_manifold.out` | `system_v5/julia_carrier/hopfield/neural_on_manifold_results.json`; not missing | `system_v5/julia_carrier/hopfield/neural_on_manifold.jl` | `AUDIT-CONFIRMED` |

## Per-Verdict Evidence

### 1. order-null `survives`

- cx output: builder created and ran `deflation_order_null.jl`, reporting `VERDICT: order_null_survives`.
- Code actually runs the claimed test: it builds density operators and compares genuine multi-channel order words against a single fixed-base lift-only deflation arm.
- Negative controls: present and collapsing. `controls_flat=true`; flat same-lift word has zero order gap and zero order-discriminating irreversibility. A forbidden nonbase-axis control is reported but explicitly not used for the verdict.
- Carrier: exact small dense Julia density-operator algebra. No Bloch readout, no NumPy, no CTMRG, no PEPS3D.
- Result JSON matches output: `verdict.overall=order_null_survives`; Z3 gap/irreversibility reproduction are `unsat`, flat control is `sat`, `load_bearing_flip=true`.
- Contraction-error certificate: not applicable; no tensor-network contraction is used.

Rerun:

- Command shape: `julia --project=system_v5/julia_carrier system_v5/julia_carrier/layers/deflation_order_null.jl`
- Hard cap: 120s
- Result: `rc=0`, elapsed `7s`, log `/tmp/verdict_rerun_order_null.log`
- Rerun verdict: `order_null_survives`

### 2. ratchet-survivor `deflated`

- cx output: builder created and ran `layers/deflation_ratchet_survivor.jl`, reporting `VERDICT: ratchet_deflated`.
- Path caveat: the user table's `system_v5/julia_carrier/layers/ratchet_survivor_reach_killtest_results.json` is the parent kill-test and says parent verdict `mixed`; the deflation result is `layers/deflation_ratchet_survivor_results.json`.
- Code actually runs the claimed deflation: genuine order survivor spread is compared against commuting control, central U1 invisible control, and single-base connection-lift candidates.
- Negative controls: present and collapsing. `commuting_control_same_survivor=true`, `central_u1_density_invisible_control_same_survivor=true`, and invalid nonconverged channels are explicitly excluded.
- Carrier: exact small dense Julia density-channel algebra. No NumPy, no Bloch, no CTMRG, no PEPS3D.
- Result JSON matches output: `verdict.classification=ratchet_deflated`, with `genuine_max=0.44370390106554813`, `best_valid_singlebase_connection_max=0.9162456945817075`, ratio `2.0649935517388003`, Z3 zero-law genuine `unsat` vs controls `sat`, deflation threshold `sat`.
- Contraction-error certificate: not applicable; no tensor-network contraction is used.

Rerun:

- Command shape: `julia --project=system_v5/julia_carrier layers/deflation_ratchet_survivor.jl`
- Hard cap: 120s
- Result: `rc=0`, elapsed `8s`, log `/tmp/verdict_rerun_ratchet_survivor.log`
- Rerun verdict: `ratchet_deflated`

### 3. Hopfield-basin `deflated`

- cx output: builder created and ran `system_v5/julia_carrier/hopfield/deflation_hopfield_basin.jl`; the result was not missing, just outside the table's `layers/` path.
- Code actually runs the claimed test: it reproduces the parent Clifford-Hopfield order-dependent basin control, then tests single fixed `W0` plus spin/connection lift variation and pure-lift pullback controls.
- Negative controls: present. The commuting complex-subalgebra arm collapses to floor, erased metric control is zero, and the result reports pure-gauge short-horizon vs converged pullback behavior honestly.
- Carrier: explicit Julia quaternion/SU(2) dense carrier over Float64. No CTMRG, no PEPS3D. `peps3d_embedding` is explicitly `not_present`.
- Result JSON matches output: `verdict=hopfield_basin_deflated`; full quaternion max order basin distance `1.27217045409484`; commuting control max `1.0931390796396078e-8`; `load_bearing_flip=true`.
- Contraction-error certificate: not applicable; no tensor-network contraction is used.

Rerun:

- Command shape: `julia --project=system_v5/julia_carrier system_v5/julia_carrier/hopfield/deflation_hopfield_basin.jl`
- Hard cap: 120s
- Result: `rc=0`, elapsed `6s`, log `/tmp/verdict_rerun_hopfield_basin.log`
- Rerun verdict: `hopfield_basin_deflated`

### 4. substrate-band `survives`

- cx output: builder created and ran `deflation_substrate_band.jl`, reporting `VERDICT: substrate_survives`.
- Code actually runs the claimed test: for `d={2,4,8}`, it compares genuine Hopf rotor substrate suppression against a single fixed-base spin-lift family and a scale-swept matched random band.
- Negative controls: present. Required negatives are `flat_frame_U_eq_I_each_d`, `scale_swept_commutator_matched_random_band_brackets_c`, and `Z3_flat_implies_zero_separation_flip`.
- Carrier: exact dense Julia density-operator / Clifford matrix algebra. No NumPy, no Bloch, no CTMRG, no PEPS3D.
- Result JSON matches output: `verdict.overall=substrate_survives`; genuine high-d suppression true at d4/d8; deflated high-d reproduction false at d4/d8; Z3 genuine d8 flip true and best-deflated d8 flip false.
- Contraction-error certificate: not applicable; no tensor-network contraction is used.

Rerun:

- Command shape: `julia --project=system_v5/julia_carrier system_v5/julia_carrier/layers/deflation_substrate_band.jl`
- Hard cap: 120s
- Result: `rc=0`, elapsed `78s`, log `/tmp/verdict_rerun_substrate_band.log`
- Rerun verdict: `substrate_survives`

### 5. cocycle 3rd-section `reproduces`

- cx output: builder created and ran `system_v5/julia_carrier/layers/cocycle_third_section.jl`; the result was not missing.
- Code actually runs the claimed test: it builds a finite eta/torus plaquette cocycle from gamma5 L/R lifts and compares against glued, eta-decoupled, erased-chirality, global-phase-only, and diagonal-cycle controls.
- Negative controls: present and collapsing except the intentionally same-sign erased-chirality control. Checks include `glued_product_control_collapses=true`, `eta_decoupled_control_collapses=true`, `global_phase_only_control_collapses=true`, `diagonal_cycle_control_collapses=true`, and `erased_chirality_same_sign=true`.
- Carrier: exact finite ComplexF64 spinor/FHS plaquette computation. No CTMRG, no PEPS3D contraction. PEPS3D mention is a non-promotion compatibility anchor only.
- Result JSON matches output: `verdict=third_section_reproduces`; base `w_L=0.24549502543491758`, `w_R=-0.2454950254349176`; controls near zero; band dependence reproduced.
- Contraction-error certificate: not applicable; no tensor-network contraction is used.

Rerun:

- Command shape: `julia --project=system_v5/julia_carrier system_v5/julia_carrier/layers/cocycle_third_section.jl`
- Hard cap: 120s
- Result: `rc=0`, elapsed `4s`, log `/tmp/verdict_rerun_third_section.log`
- Rerun verdict: `third_section_reproduces`

### 6. N=64 carrier `reached`

- cx output: builder created and ran `layers/carrier_n64_attack.jl`; the result was not missing, just under top-level `layers/`.
- Code actually runs the claimed test: it builds N=64 finite ITensors/ITensorMPS carriers for V2 chain reproduction, radial parallel eta bonds, and a coarser deeper shell ladder.
- Negative controls: present. Flat/product controls are at floor for reliable variants, with equal maxdim/cutoff for genuine and control paths.
- Carrier: ITensors/ITensorMPS finite MPS. No CTMRG, no dense full-state closure, no NumPy, no PEPS3D contraction.
- Result JSON matches output, but the verdict is under `classification_summary.verdict`, not top-level `verdict`: `n64_reached`; best variant `radial_parallel_eta_bonds`; best min inter-shell entropy `0.04274390813365116`; reached variants `["radial_parallel_eta_bonds"]`.
- Contraction-error certificate: present as per-variant fields, not as a top-level `contraction_error_certificate`: `cap_clear_no_observed_truncation=true`, equal maxdim/cutoff, discarded weights logged `0.0`, controls at floor, and `error_bounded_effect_gt_error=true`.

Rerun:

- Command shape: `julia --project=system_v5/julia_carrier layers/carrier_n64_attack.jl`
- Hard cap: 120s
- Result: `rc=0`, elapsed `37s`, log `/tmp/verdict_rerun_n64_carrier.log`
- Rerun verdict: `n64_reached`

### 7. curvature-frame `unifies`

- cx output and source show the builder implemented a curvature-frame POC, but the actual result does not support the claimed `unifies` verdict.
- Code writes `curvature_unifies ? "curvature_unifies" : "per_layer_needed"`.
- Result JSON says `verdict=per_layer_needed`, `break_layer=G_nested_hopf_tori`.
- Negative controls: present for constant spinor flat control and Weyl trivial mass control; nested fixed-leaf flatness and Clifford boundary break are explicitly reported.
- Carrier: exact finite ComplexF64 spinor/LinearAlgebra curvature/holonomy POC. No CTMRG, no PEPS3D admission.
- Contraction-error certificate: not applicable; no tensor-network contraction is used.

Classification: `FABRICATED` for the pending claim `curvature-frame unifies`, because the actual source/result contradict it. I did not rerun this row as a genuine candidate.

### 8. cocycle full-eta monopole `present`

- cx output: builder created and ran `system_v5/julia_carrier/layers/cocycle_full_monopole.jl`, eventually fixing the Z3 API issue and reporting `full_monopole_present`.
- Code actually runs the claimed test: full eta range `[0, pi]` x torus cycle `[0, 2pi]` mixed Wilson curvature, with glued, eta-decoupled, erased-chirality, and grid-convergence controls.
- Negative controls: present. Glued and eta-decoupled controls collapse to zero; erased chirality keeps integer magnitude but kills opposite sign; Z3 gate flips genuine SAT vs glued/erased UNSAT.
- Carrier: exact finite ComplexF64 spinor/FHS plaquette computation. No NumPy, no CTMRG, no PEPS3D contraction.
- Result JSON matches output: `verdict=full_monopole_present`; full eta `w_L=0.9999999999999378`, `w_R=-0.9999999999999359`; Z3 `flip_pass=true`.
- Contraction-error certificate: not applicable; no tensor-network contraction is used.

Rerun:

- Command shape: `julia --project=system_v5/julia_carrier system_v5/julia_carrier/layers/cocycle_full_monopole.jl`
- Hard cap: 120s
- Result: `rc=0`, elapsed `7s`, log `/tmp/verdict_rerun_full_monopole.log`
- Rerun verdict: `full_monopole_present`

### 9. neural-on-manifold `nonflat_changes_network`

- cx output: builder created and ran `system_v5/julia_carrier/hopfield/neural_on_manifold.jl`; the result was not missing.
- Code actually runs the claimed test: finite quaternionic Hopf/Clifford neurons are compared against flat unconstrained Euclidean, externally projected flat, commuting scalar, flat scalar AB=BA, and erased B:=A controls.
- Negative controls: present. Commuting real-scalar quaternion control max distance `1.1144443718950155e-8`; flat scalar max `2.1507973566264877e-9`; erased controls near floor.
- Carrier: explicit Julia Float64 quaternion/SU(2) dense carrier. No CTMRG/PEPS3D contraction. The result includes a finite PEPS3D site/bond anchor, but it explicitly says no PEPS contraction or bond-tensor admission is claimed.
- Result JSON matches output: `verdict=nonflat_changes_network`; verdict components all true; basin mismatch fraction `0.6`; nonflat max order basin distance `1.1895269646869522`; flat norm growth ratio is enormous while nonflat S3 norm deviation is machine precision.
- Contraction-error certificate: not applicable; no tensor-network contraction is used.

Rerun:

- Command shape: `julia --project=system_v5/julia_carrier system_v5/julia_carrier/hopfield/neural_on_manifold.jl`
- Hard cap: 120s
- Result: `rc=0`, elapsed `5s`, log `/tmp/verdict_rerun_neural_manifold.log`
- Rerun verdict: `nonflat_changes_network`

## Honest Deflation Map

Genuine or surviving after audit:

- `order_null_survives`: genuine multi-channel order DOF candidate survives this single-base deflation control.
- `substrate_survives`: matched-band substrate suppression survives this single-base spin-lift deflation control for d4/d8.
- `third_section_reproduces`: independent third-section presence-bar cocycle reproduces the partial-band opposite-sign signal with collapsing controls.
- `n64_reached`: at least one reliable ITensors-MPS N=64 carrier variant remains above the pre-registered inter-shell entropy floor.
- `full_monopole_present`: full-eta mixed cocycle integrates to opposite-sign integer charge with collapsing zero controls.
- `nonflat_changes_network`: the finite quaternionic/Clifford Hopfield network changes finitude, commutation, basins, and capacity relative to flat controls.

Deflated:

- `ratchet_survivor` deflates under the single-base connection-lift control.
- `Hopfield-basin` deflates under the single fixed-weight/lift variation control, with an important caveat: the result also reports lift/roundoff-sensitive converged attractor behavior rather than a clean promoted geometric order witness.

Fabricated as stated:

- `curvature-frame unifies`: actual result is `per_layer_needed`, not `curvature_unifies`.

## Contradictions And Caveats

- The table's "missing" result labels are stale for Hopfield-basin, third-section, N=64, and neural-on-manifold. Their result JSONs exist, but some are outside `system_v5/julia_carrier/layers/`.
- The ratchet-survivor table path points to the parent `ratchet_survivor_reach_killtest_results.json`, whose verdict is `mixed`; the deflation verdict lives at `layers/deflation_ratchet_survivor_results.json`.
- Substrate-band survives this matched-band deflation control even though earlier holonomy-law/substrate-law work deflated under a single-base lift reading. The honest map is split: holonomy law deflates, matched-band substrate suppression survives here.
- Curvature-frame does not unify the audited layer stack. It recovers some curvature/Chern-style invariants, but breaks on nested Hopf and Clifford/algebraic/MPS structures; the actual result says per-layer observables are still needed.
- N=64 `reached` is carrier/topology-sensitive. The V2 chain reproduction still decays below the floor, while the radial parallel eta-bond carrier reaches; this must not be silently substituted into the V2 claim.
- All confirmed results remain `promotion_allowed=false` POCs or controls. None admits layer completion, full manifold admission, Axis0/FEP/flux/physics progress, or a PEPS3D claim.

## Rerun Summary

| Label | File | rc | Elapsed | Rerun verdict | Log |
|---|---:|---:|---:|---|---|
| order_null | `system_v5/julia_carrier/layers/deflation_order_null.jl` | 0 | 7s | `order_null_survives` | `/tmp/verdict_rerun_order_null.log` |
| ratchet_survivor | `layers/deflation_ratchet_survivor.jl` | 0 | 8s | `ratchet_deflated` | `/tmp/verdict_rerun_ratchet_survivor.log` |
| hopfield_basin | `system_v5/julia_carrier/hopfield/deflation_hopfield_basin.jl` | 0 | 6s | `hopfield_basin_deflated` | `/tmp/verdict_rerun_hopfield_basin.log` |
| substrate_band | `system_v5/julia_carrier/layers/deflation_substrate_band.jl` | 0 | 78s | `substrate_survives` | `/tmp/verdict_rerun_substrate_band.log` |
| third_section | `system_v5/julia_carrier/layers/cocycle_third_section.jl` | 0 | 4s | `third_section_reproduces` | `/tmp/verdict_rerun_third_section.log` |
| n64_carrier | `layers/carrier_n64_attack.jl` | 0 | 37s | `n64_reached` | `/tmp/verdict_rerun_n64_carrier.log` |
| full_monopole | `system_v5/julia_carrier/layers/cocycle_full_monopole.jl` | 0 | 7s | `full_monopole_present` | `/tmp/verdict_rerun_full_monopole.log` |
| neural_manifold | `system_v5/julia_carrier/hopfield/neural_on_manifold.jl` | 0 | 5s | `nonflat_changes_network` | `/tmp/verdict_rerun_neural_manifold.log` |

