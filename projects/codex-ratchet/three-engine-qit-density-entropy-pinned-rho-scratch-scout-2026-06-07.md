---
title: Three-Engine QIT Density/Entropy Pinned-Rho Scratch Scout 2026-06-07
created: 2026-06-07
type: project-result-router
status: active-scratch-diagnostic-receipt
claim_ceiling: validated local scratch_diagnostic envelope only; no canonical, formal admission, bridge, manifold, axis, or full-system claim
framing: codex-ratchet
---

# Three-Engine QIT Density/Entropy Pinned-Rho Scratch Scout 2026-06-07

## Bottom line

The QIT density/entropy packet is now a **validated three-engine scratch diagnostic over one pinned finite object**.

Safe phrase:

```text
three-engine QIT density/entropy scratch scout validated at the scratch_diagnostic ceiling
```

Unsafe phrases:

```text
full system works
canonical QIT engine
formal admission
bridge/manifold/axis evidence
physics or M(C) admission
```

## Pinned finite object

The shared observable is fixed before engine comparison:

```text
rho(p) = (1-p)|GHZ><GHZ| + p*I/8
p = 0.3
n_qubits = 3
hilbert_dimension = 8
entropy_base = natural_log
dephasing_included = false
exact spectrum = {59/80, 3/80 x 7}
```

This pin matters because the prior unpinned QIT density/entropy legs all ran but computed different states. The earlier entropy spread was a spec artifact, not a substrate result.

## Current repo artifacts

Hermes created non-overlapping Hermes-owned files instead of editing Claude's adjacent QIT artifacts:

```text
/Users/joshuaeisenhart/Codex-Ratchet/system_v5/julia_carrier/qit_density_entropy_pinned_rho_ghz_white_noise_julia.jl
/Users/joshuaeisenhart/Codex-Ratchet/system_v5/julia_carrier/qit_density_entropy_pinned_rho_ghz_white_noise_julia_results.json
/Users/joshuaeisenhart/Codex-Ratchet/system_v5/ops/formal_scouts/sim_qit_density_entropy_pinned_rho_jax_leg.py
/Users/joshuaeisenhart/Codex-Ratchet/system_v5/ops/formal_scouts/results/qit_density_entropy_pinned_rho_jax_leg_results.json
/Users/joshuaeisenhart/Codex-Ratchet/system_v5/ops/formal_scouts/sim_qit_density_entropy_pinned_rho_pytorch_leg.py
/Users/joshuaeisenhart/Codex-Ratchet/system_v5/ops/formal_scouts/results/qit_density_entropy_pinned_rho_pytorch_leg_results.json
/Users/joshuaeisenhart/Codex-Ratchet/system_v5/ops/formal_scouts/sim_three_engine_qit_density_entropy_pinned_rho_envelope.py
/Users/joshuaeisenhart/Codex-Ratchet/system_v5/ops/formal_scouts/results/three_engine_qit_density_entropy_pinned_rho_envelope_results.json
```

## Engine roles and observed values

```text
Julia reference: QuantumOptics
JAX mirror/proof: jax + qutip + z3 + cvc5
PyTorch support/third substrate: torch + torch.func
```

Observed current-run values:

| Engine | Load-bearing package path | vn_entropy | Extra observable |
|---|---:|---:|---|
| Julia | QuantumOptics | 1.0864570440180348 | analytic entropy residual 0.0 |
| JAX | qutip + z3/cvc5 | 1.0864570440180348 | qutip entropy 1.086457044018035; z3/cvc5 spectrum certificate passed |
| PyTorch | torch.func | 1.0864570440180348 | dS/dp = 2.6065595108329083; grad/jacrev/analytic agree |

Envelope readback:

```text
all_pass = true
same_spec = true
entropy_max_divergence = 0.0
spectrum_high_max_divergence = 0.0
spectrum_low_max_divergence = 0.0
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
claim = exact pinned spectrum {59/80, 3/80 x 7} is a nonnegative probability simplex
```

## Commands that passed

Hermes direct real-test run passed:

```text
/opt/homebrew/bin/julia --startup-file=no system_v5/julia_carrier/qit_density_entropy_pinned_rho_ghz_white_noise_julia.jl
/Users/joshuaeisenhart/.local/share/codex-ratchet/envs/main/bin/python3 system_v5/ops/formal_scouts/sim_qit_density_entropy_pinned_rho_jax_leg.py
/Users/joshuaeisenhart/.local/share/codex-ratchet/envs/main/bin/python3 system_v5/ops/formal_scouts/sim_qit_density_entropy_pinned_rho_pytorch_leg.py
/Users/joshuaeisenhart/.local/share/codex-ratchet/envs/main/bin/python3 system_v5/ops/formal_scouts/sim_three_engine_qit_density_entropy_pinned_rho_envelope.py
/Users/joshuaeisenhart/.local/share/codex-ratchet/envs/main/bin/python3 scripts/lint_sim_contract.py [three pinned-rho Python scripts]
/Users/joshuaeisenhart/.local/share/codex-ratchet/envs/main/bin/python3 scripts/validate_three_engine_sim_result.py --require-pytorch system_v5/ops/formal_scouts/results/three_engine_qit_density_entropy_pinned_rho_envelope_results.json
```

Observed validator output:

```text
lint_sim_contract: checked=3, violation_total=0
validate_three_engine_sim_result: ok=true
```

Claude also reported an independent validator rerun with `ok: true` and direct JSON readback of the same pinned values. Treat that as a worker receipt until a fresh Codex/Hermes audit reads the artifacts again.

## Status ladder

Earned:

```text
runs
passes local rerun
shape-validator ok:true
proper three-engine scratch_diagnostic packet over one pinned finite object
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

- The repo artifacts are current-worktree evidence. Several source files are untracked.
- Formal-scout result JSONs under `system_v5/ops/formal_scouts/results/*.json` are gitignored.
- The validator is a shape/contract gate. It does not prove the mathematics by itself.
- A fresh-context audit by a worker that did not build the packet is still the next gate before any stronger wording.

## Next bounded run packet

The next admissible rung should reuse the same pin-first rule:

```text
1. define one exact finite object or channel;
2. compute locally in Julia/JAX/PyTorch before peer comparison;
3. bind result JSONs into an envelope;
4. validate shape with the repo validator or a QIT-specific extension;
5. report divergence as signal;
6. preserve scratch_diagnostic ceiling unless a dedicated stronger gate exists.
```

Best next packet: a pinned CPTP channel over the same `rho(p)` with a named channel, fixed parameter, and entropy/coherent-information readout. This keeps the work adjacent to the validated QIT density/entropy packet without pretending the whole QIT engine is admitted.
