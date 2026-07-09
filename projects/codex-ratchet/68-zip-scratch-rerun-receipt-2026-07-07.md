# 68.zip scratch rerun receipt

Date: 2026-07-07

Artifact: `/Users/joshuaeisenhart/Desktop/68.zip`

SHA256: `0476e9e75a8f6331ba2ce38e4d3dca67fc1c6c027fbb5cea082f5b4533863eab`

Scratch extract: `/tmp/codex_68.me92wW`

Claim ceiling: scratch bundle rerun only. This is not live Codex-Ratchet admission, not Lev mesh mutation, and not canon. The bundle itself states `synced-not-canon`, `scratch_diagnostic`, and `promotion_allowed=false`.

## Commands Run

```bash
python3 run_all.py
/Users/joshuaeisenhart/.local/share/sim-stack/bin/python3 run_all.py
```

## Results

Default Homebrew Python result:

```text
103 pass / 1 fail / 4 skip -> RED
```

Cause: `engine_dynamics_id_arbiter_sim.py` failed because `pysindy` was not installed in the default interpreter. JAX and qutip lanes skipped in that interpreter.

Sim-stack interpreter result:

```text
108 pass / 0 fail / 0 skip -> GREEN
```

The sim-stack run exercised JAX, qutip, PySINDy, Torch, z3, cvc5, and Julia. The engines lane passed:

```text
1q: oracle vs jax+torch+julia GREEN
3q: oracle vs jax+torch+julia GREEN (63-dim Pauli, C^8)
```

## Object And Teeth Signals

- `perception_object_binding_sim_results.json`: `classification=scratch_diagnostic`, `promotion_allowed=false`; policy eval says object binding across novel perspectives passed, degeneracy refusal passed, and binding requires the distinct-kind interior.
- `engine_reidentification_objective_sim_results.json`: `real_reidentification_rate_novel_probes=1.0`, `n_stages_reidentified=16`, `chance_rate=0.0625`, control flip true.
- `engine_object_formation_scorecard_sim_results.json`: convergence and handling controls both flip.
- `objective_gate_integrity_sweep_sim_results.json`: perception, scorecard, and reidentification gates are real, not rubber stamps.
- `stage_necessity_ablation_sim_results.json`: every nondegenerate stage scramble/duplicate induces error; expected degenerate nulls stay lower; all stages do unique work under the bundle's criterion.
- `sixteen_intelligences_substages_terrain_ratchet_sim_results.json`: sixteen distinct kinds, four ordered substages per stage, eight terrains ratcheted into two signed types, engine interior built.
- `lev_qit_evidence_envelope_emitter_results.json`: emitter ran, source-fidelity status says it packages linted source-faithful sims, dynamic claim status is none, host boundary conforms, promoting-twin control rejected.

## Honest Reading

This is the strongest local runnable artifact in the numbered Desktop bundle family so far: it has a full scratch rerun green under the proper sim-stack interpreter and includes object/perception/teeth checks that directly match the current QIT/Lev questions.

It still does not prove live mesh admission. The next live step is to migrate only the admissible evidence envelope/consumer surfaces into the real Codex-Ratchet and Lev gate path, preserving `scratch_diagnostic` and `promotion_allowed=false` until the live repo gates consume them.
