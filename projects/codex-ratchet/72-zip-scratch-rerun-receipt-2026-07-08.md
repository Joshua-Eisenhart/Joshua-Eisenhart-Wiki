# 72.zip scratch rerun receipt

Date: 2026-07-08

Artifact: `/Users/joshuaeisenhart/Desktop/72.zip`

SHA256: `cdc1d188b5ff11c8ba502dbafda0c8ca78e38190ef6e1ede7f766d0246964267`

Scratch extract: `/tmp/codex_72.2jxbhp`

Claim ceiling: scratch bundle rerun only. This is not live Codex-Ratchet admission, not Lev mesh mutation, and not canon. The bundle states `synced-not-canon`; scientific result files continue to use `scratch_diagnostic` and `promotion_allowed=false`.

## Command Run

```bash
/Users/joshuaeisenhart/.local/share/sim-stack/bin/python3 run_all.py
```

## Result

```text
111 pass / 0 fail / 0 skip -> GREEN
```

The engines lane passed:

```text
1q: oracle vs jax+torch+julia GREEN
3q: oracle vs jax+torch+julia GREEN (63-dim Pauli, C^8)
```

## Delta From 68.zip

New Python sims present in `72.zip` relative to the prior scratch extraction of `68.zip`:

- `downstream_dominance_window_discriminator_sim.py`
- `substage_architecture_discriminator_sim.py`
- `qit_epistemic_active_inference_sim.py`

All three passed in the full harness.

## New Signals

- `downstream_dominance_window_discriminator_sim_results.json`: `classification=scratch_diagnostic`, `promotion_allowed=false`. Re-identification does not discriminate the candidate readings, but object formation does: canonical-equivalent object count only holds on an interior alpha window `[0.10, 0.30]`, while too-weak and too-strong subordinate operators diverge. This makes object formation a downstream discriminator, not a rubber stamp.
- `substage_architecture_discriminator_sim_results.json`: `classification=scratch_diagnostic`, `promotion_allowed=false`. Candidate A and C behave like engine cycles under the closing-plus-oriented-work test; candidate B fails oriented work. Position uniqueness over 64 remains explicitly open.
- `qit_epistemic_active_inference_sim_results.json`: `classification=scratch_diagnostic`, `promotion_allowed=false`. Epistemic policy resolves all 8 hidden terrains, mean `8.875` ticks to certainty, beats random `10.833`, and an uninformative-probe control leaves uncertainty unresolved.

## Continued Object And Teeth Signals

- `perception_object_binding_sim_results.json`: object binding across novel perspectives passes, degeneracy refusal passes, and binding requires the distinct-kind interior.
- `engine_reidentification_objective_sim_results.json`: `real_reidentification_rate_novel_probes=1.0`, `n_stages_reidentified=16`, `chance_rate=0.0625`, control flip true.
- `perception_scorecard_eval_admission_sim_results.json`: missing eval-admission fields are measured: recall ratio, anti-key penalty, attention leak, and cross-node mesh convergence.
- `objective_gate_integrity_sweep_sim_results.json`: perception, scorecard, and reidentification gates are real, not rubber stamps.
- `stage_necessity_ablation_sim_results.json`: every nondegenerate stage scramble/duplicate induces error; expected degenerate nulls stay lower; all stages do unique work under the bundle's criterion.
- `sixteen_intelligences_substages_terrain_ratchet_sim_results.json`: sixteen distinct kinds, four ordered substages per stage, eight terrains ratcheted into two signed types, engine interior built.
- `lev_qit_evidence_envelope_emitter_results.json`: emitter ran, source-fidelity status says it packages linted source-faithful sims, dynamic claim status is none, host boundary conforms, promoting-twin control rejected.

## Honest Reading

`72.zip` is stronger than `68.zip` as a scratch executable bundle: it reruns fully green under the proper interpreter, adds three passed sims, and adds a better downstream discriminator for object formation plus an explicit epistemic active-inference lane.

It still does not prove live mesh admission. The next live step remains narrow: consume only the admissible evidence envelope/consumer surfaces in the real Codex-Ratchet and Lev gate path, preserving `scratch_diagnostic` and `promotion_allowed=false` until live repo gates consume them.
