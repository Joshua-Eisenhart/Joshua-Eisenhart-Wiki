# Rosetta/Xi Adversarial Hardening Audit

Date: 2026-06-06

This is a controller-side hardening audit over the two formal scouts from the
Rosetta/Xi-gradient operational-theory tranche. It records demotion, not
promotion.

## Repo Result

Source:

```text
/Users/joshuaeisenhart/Codex-Ratchet/system_v5/ops/formal_scouts/sim_rosetta_xi_adversarial_hardening_audit_probe.py
```

Result:

```text
/Users/joshuaeisenhart/Codex-Ratchet/system_v5/ops/formal_scouts/results/rosetta_xi_adversarial_hardening_audit_probe_results.json
```

Validation:

```text
py_compile: pass
direct run: pass
validate_formal_scout_results.py --fresh-rerun: pass
```

## Verdicts

```text
classification: formal_scout
all_pass: true
promotion_allowed: false
formal_admission_allowed: false
```

```text
rosetta_table_consistency_survived: true
rosetta_independent_invariant_not_admitted: true
xi_lambda_schedule_explains_gradient: true
xi_shell_geometry_specific_reading_killed: true
xi_cut_specificity_reading_killed: true
```

## Rosetta

The 4-element Rosetta scout survives only as a bounded table-consistency scout.

The row-atomic controls keep the natural map unique:

```text
full_best_nonnatural_ratio: 0.7142857142857143
core_best_nonnatural_ratio: 0.75
```

But the 224 exact-stage denominator is not independent evidence. Several single
features uniquely bind row order:

```text
perception
ordered_token
realization
dynamics_family
rate
```

So the correct ceiling is:

```text
Rosetta table consistency survived.
Independent IGT/QIT invariant not admitted.
```

## Xi

The Xi-shell coherent-information gradient scout is demoted harder.

The lambda-only fixed-basis control reuses the candidate `lambda_k` sequence, but
removes shell spinor/twistor/incidence geometry, boundary variation, and phase.
It reproduces the candidate gradient to numerical precision:

```text
candidate_score: 0.9953412943548703
lambda_only_score_gap: 2.220446049250313e-16
lambda_only_gradient_profile_l2_gap: 2.085365630873008e-15
```

The cut-specific reading also fails: all tested 2/2 cuts and both coherent
information directions produced the same score.

The pure-state readout collapses the claimed coherent-information object to
subsystem entropy:

```text
S_AB ~= 0
S_A ~= S_B
I_c(A->B) ~= S_B
```

So the correct ceiling is:

```text
The current Xi-gradient result is carried by the monotone lambda entanglement
schedule. The shell-geometry/cut-specific Xi bridge reading is killed.
```

## Independent Wizard/codex2 Xi adversarial audit

A later Hermes Wizard full/auto attempt plus codex2 direct-build produced an
independent reimplementation audit:

```text
/Users/joshuaeisenhart/Codex-Ratchet/system_v5/ops/formal_scouts/sim_xi_shell_coherent_information_gradient_adversarial_audit_probe.py
```

Result:

```text
/Users/joshuaeisenhart/Codex-Ratchet/system_v5/ops/formal_scouts/results/xi_shell_coherent_information_gradient_adversarial_audit_probe_results.json
```

Controller receipt:

```text
wizard-full-loop-xi-adversarial-audit-2026-06-06.hermes-verification.json
```

This result is deliberately stricter and records:

```text
all_pass: false
xi_shell_gradient_candidate_survived_adversarial_audit: false
strongest_falsifier: entanglement_angle_only_countermodel
profile_l2_gap: 5.887846720064157e-16
candidate_score: 0.9934389788815682
cut_swap_wrong_cut_control: false
phase_twist_randomization_control: false
no_chirality_symmetrized_orientation_control: false
no_signal_control: true
promotion_allowed: false
formal_admission_allowed: false
```

Interpretation: the original positive gradient profile exists, but the stronger
shell-geometry / cut-specific / phase-twist / chirality reading does not survive.
A same entanglement-angle schedule on a fixed computational basis reproduces the
profile to numerical precision.

Claim ceiling: this kills the current bridge reading; it does not kill every
possible future Xi construction. A future Xi packet must define a finite object
whose gradient cannot be reproduced by the lambda/entanglement-angle-only
countermodel and must pass the wrong-cut, phase/twist, no-chirality, product,
no-boundary, no-signal, and scalar-only controls.

## Fisher/Bures Follow-On

Source:

```text
/Users/joshuaeisenhart/Codex-Ratchet/system_v5/ops/formal_scouts/sim_xi_shell_bures_metric_audit_probe.py
```

Result:

```text
/Users/joshuaeisenhart/Codex-Ratchet/system_v5/ops/formal_scouts/results/xi_shell_bures_metric_audit_probe_results.json
```

Validation:

```text
py_compile: pass
direct run: pass
validate_formal_scout_results.py --fresh-rerun: pass
```

Verdict:

```text
classification: formal_scout
all_pass: true
promotion_allowed: false
formal_admission_allowed: false
bures_metric_route_pressure_survived: true
bures_lambda_only_does_not_explain_metric_profile: true
bures_metric_does_not_promote_xi_bridge: true
coherent_information_geometry_reading_remains_killed: true
```

The Bures-distance profile sees carrier-frame/phase motion not reproduced by
the fixed-basis lambda-only control:

```text
candidate_vs_lambda_zero_phase_global_l2: 0.04401856738316161
candidate_vs_lambda_phase_global_l2: 0.04285063647438024
```

But this does not restore the Xi bridge. The productized-cut control has
same-order metric motion:

```text
candidate_vs_product_global_l2: 0.039805827550330734
product_mean_ratio_to_candidate: 1.1874399238226088
```

So the correct ceiling is:

```text
Bures metric route pressure survived as a formal scout. The current
coherent-information bridge reading remains killed, and no Xi/Phi0/Axis0/
gravity/physics/QIT-engine promotion is allowed.
```

## Channel/Resource Metric Follow-On

Source:

```text
/Users/joshuaeisenhart/Codex-Ratchet/system_v5/ops/formal_scouts/sim_xi_shell_channel_resource_metric_audit_probe.py
```

Result:

```text
/Users/joshuaeisenhart/Codex-Ratchet/system_v5/ops/formal_scouts/results/xi_shell_channel_resource_metric_audit_probe_results.json
```

Validation:

```text
py_compile: pass
direct run: pass
validate_formal_scout_results.py --fresh-rerun: pass
numpy/np compute grep: clean
```

Verdict:

```text
classification: formal_scout
all_pass: true
promotion_allowed: false
formal_admission_allowed: false
channel_resource_metric_pressure_survived: true
bures_contractivity_controls_pass: true
common_unitary_invariance_pass: true
coherence_and_discard_controls_reduce_residual: true
does_not_promote_xi_bridge: true
```

This follow-on keeps the same Xi-shell density family and tests the Bures
profile under finite channel/resource-style controls: common unitary,
global depolarizing noise, B-local depolarizing noise, dephasing,
discard/replace channels, and partial-trace cuts.

Key observed metric effects:

```text
base candidate_vs_lambda_zero_l2: 0.04401858984945489
dephasing_p065 candidate_vs_lambda_zero_l2: 0.0076065981379939635
discard_replace_B candidate_vs_lambda_zero_l2: 0.008136375801666183
global_depolarizing_p100 profile mean: 0.0
common_unitary mean_ratio_to_identity: 0.9999986417899676
B_local_depolarizing_p100 candidate_vs_lambda_zero_l2: 0.008136393239699464
```

The result supports a narrow resource/distinguishability reading: finite CPTP
controls contract the Bures profile as expected, while coherence-destroying and
discard channels remove most of the non-lambda residual. That makes the metric
residual correlation/coherence-sensitive.

It still does not admit a channel-box construction, resource monotone, Xi/Phi0
bridge, Axis0, gravity, physics, or QIT-engine claim. It is a route-pressure
scout saying that the next admissible resource-theory packet should use actual
channel boxes, superchannel/data-processing controls, and a chosen
divergence/min-relative-entropy readout.

## Blocked Consumers

The audit does not admit:

```text
QIT engine
final IGT
final Xi
final Phi0
Axis0
gravity
physics
bridge promotion
consciousness
perception
FTL
formal admission
```

## Next Admissible Tests

1. Rosetta: add a row-atomic marginal-preserving null that preserves per-group
   token/result/sign/terrain marginals while breaking natural stage binding.
2. Xi: redesign the shell family so geometry, cut, or boundary variation is
   load-bearing after the lambda schedule is held fixed or neutralized.
3. Fisher/Bures: independently reimplement the landed metric scout and add
   channelized/resource-distinguishability controls. The first channel/resource
   follow-on now passes bounded Bures contractivity controls, but remains below
   channel-box, bridge, Axis0, gravity, physics, and QIT-engine promotion.
4. Resource theory: build an actual channel-box scout with two tiny channels,
   one selected divergence/min-relative-entropy readout, and superchannel
   data-processing controls.
