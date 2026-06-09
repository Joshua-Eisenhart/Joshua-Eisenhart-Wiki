---
title: Three-Engine QIT CPTP Dephasing Pinned-Rho Scratch Scout 2026-06-07
created: 2026-06-07
type: project-result-router
status: active-scratch-diagnostic-receipt
claim_ceiling: validated local scratch_diagnostic envelope only; no canonical, formal admission, bridge, manifold, axis, M(C), QIT-engine, or full-system claim
framing: codex-ratchet
---

# Three-Engine QIT CPTP Dephasing Pinned-Rho Scratch Scout 2026-06-07

## Bottom line

This is the next bounded run after the pinned-rho entropy packet. It applies one named CPTP channel to the same pinned finite state and validates a three-engine scratch envelope.

Safe phrase:

```text
three-engine QIT CPTP dephasing scratch scout validated at the scratch_diagnostic ceiling
```

Unsafe phrases:

```text
QIT engine admitted
canonical channel result
formal admission
M(C) / bridge / manifold / axis evidence
full system works
```

## Pinned finite object and channel

Input state:

```text
rho(p) = (1-p)|GHZ><GHZ| + p*I/8
p = 0.3
n_qubits = 3
hilbert_dimension = 8
entropy_base = natural_log
```

Channel:

```text
computational-basis dephasing
E_gamma(rho) = (1-gamma)rho + gamma*diag(rho)
gamma = 0.4
post-channel exact spectrum = {239/400, 71/400, 15/400 x 6}
```

## Current repo artifacts

Hermes created a new non-overlapping packet:

```text
/Users/joshuaeisenhart/Codex-Ratchet/system_v5/julia_carrier/qit_cptp_dephasing_pinned_rho_julia.jl
/Users/joshuaeisenhart/Codex-Ratchet/system_v5/julia_carrier/qit_cptp_dephasing_pinned_rho_julia_results.json
/Users/joshuaeisenhart/Codex-Ratchet/system_v5/ops/formal_scouts/sim_qit_cptp_dephasing_pinned_rho_jax_leg.py
/Users/joshuaeisenhart/Codex-Ratchet/system_v5/ops/formal_scouts/results/qit_cptp_dephasing_pinned_rho_jax_leg_results.json
/Users/joshuaeisenhart/Codex-Ratchet/system_v5/ops/formal_scouts/sim_qit_cptp_dephasing_pinned_rho_pytorch_leg.py
/Users/joshuaeisenhart/Codex-Ratchet/system_v5/ops/formal_scouts/results/qit_cptp_dephasing_pinned_rho_pytorch_leg_results.json
/Users/joshuaeisenhart/Codex-Ratchet/system_v5/ops/formal_scouts/sim_three_engine_qit_cptp_dephasing_pinned_rho_envelope.py
/Users/joshuaeisenhart/Codex-Ratchet/system_v5/ops/formal_scouts/results/three_engine_qit_cptp_dephasing_pinned_rho_envelope_results.json
```

## Observed values

| Engine | Load-bearing path | entropy before | entropy after | Extra observable |
|---|---:|---:|---:|---|
| Julia | QuantumOptics | 1.0864570440180348 | 1.3533406014060736 | entropy change 0.2668835573880388 |
| JAX | qutip + z3/cvc5 | 1.0864570440180346 | 1.3533406014060736 | qutip entropy after 1.353340601406074; z3/cvc5 spectrum certificate passed |
| PyTorch | torch.func | 1.0864570440180348 | 1.3533406014060738 | dS/dgamma = 0.42482428621156787; grad/jacrev/analytic agree |

Envelope readback:

```text
all_pass = true
same_spec = true
max_divergence = 2.220446049250313e-16
entropy_change_max_divergence = 2.220446049250313e-16
engine reads_peer_result = false, false, false
classification = scratch_diagnostic
promotion_allowed = false
formal_admission_allowed = false
```

Crossover proof status:

```text
z3 verdict = sat
z3 negative_control_verdict = unsat
cvc5 verdict = sat
cvc5 negative_control_verdict = unsat
claim = exact post-dephasing spectrum {239/400, 71/400, 15/400 x 6} is a nonnegative probability simplex
```

## Commands that passed

Hermes direct real-test run passed:

```text
/opt/homebrew/bin/julia --startup-file=no system_v5/julia_carrier/qit_cptp_dephasing_pinned_rho_julia.jl
/Users/joshuaeisenhart/.local/share/codex-ratchet/envs/main/bin/python3 system_v5/ops/formal_scouts/sim_qit_cptp_dephasing_pinned_rho_jax_leg.py
/Users/joshuaeisenhart/.local/share/codex-ratchet/envs/main/bin/python3 system_v5/ops/formal_scouts/sim_qit_cptp_dephasing_pinned_rho_pytorch_leg.py
/Users/joshuaeisenhart/.local/share/codex-ratchet/envs/main/bin/python3 system_v5/ops/formal_scouts/sim_three_engine_qit_cptp_dephasing_pinned_rho_envelope.py
/Users/joshuaeisenhart/.local/share/codex-ratchet/envs/main/bin/python3 scripts/lint_sim_contract.py [three CPTP dephasing Python scripts]
/Users/joshuaeisenhart/.local/share/codex-ratchet/envs/main/bin/python3 scripts/validate_three_engine_sim_result.py --require-pytorch system_v5/ops/formal_scouts/results/three_engine_qit_cptp_dephasing_pinned_rho_envelope_results.json
```

Observed validator output:

```text
lint_sim_contract: checked=3, violation_total=0
validate_three_engine_sim_result: ok=true
```

## Status ladder

Earned:

```text
runs
passes local rerun
shape-validator ok:true
proper three-engine scratch_diagnostic packet over one pinned finite state and one named CPTP channel
```

Not earned:

```text
canonical
formal_scout admission
formal admission
M(C) admission
QIT engine admission
bridge / manifold / basin / axis evidence
full-system or all-tools claim
```

## Current caveats

- This is current-worktree evidence; the new packet files are untracked.
- Formal-scout result JSONs under `system_v5/ops/formal_scouts/results/*.json` are gitignored.
- The validator is a shape/contract gate, not a standalone proof of the mathematics.
- Fresh-context audit is still required before stronger wording.

## Next bounded run packet

The next step should not widen to full-system execution. It should extend the same pin-first pattern to one more bounded finite object or channel, for example:

```text
- a second named CPTP channel with a different exact spectrum/control;
- coherent information / mutual information readout on a pinned bipartite state;
- a small finite constraint object that begins pressuring M(C) without naming it admitted.
```
