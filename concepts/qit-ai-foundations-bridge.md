---
title: QIT AI Foundations Bridge
created: 2026-04-10
updated: 2026-04-12
type: concept
tags: [reference, research, ai, alignment, simulation]
sources:
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/qit_predictive_world_model_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/qit_szilard_landauer_cycle_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/qit_strong_coupling_landauer_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/qit_moloch_coordination_trap_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/a2_state/sim_results/qit_graph_engine_alignment_probe_results.json
framing: current
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# QIT AI Foundations Bridge

## Overview
This page keeps the AI bridge narrow. The goal is not to declare that QIT engines already solve intelligence or alignment. The goal is to track where finite density-state and channel language gives a real bridge into AI foundations, world models, and alignment research. Public parent terms should stay in front: operationalism, distinguishability, quantum channels, measurement and feedback control, shared-resource coordination, and bounded predictive world models.

## What is actually earned
- Predictive world-model behavior: `sim_qit_predictive_world_model.py` shows that an internal density-state model updated from a noncommuting probe set can reduce prediction error and re-adapt after an environment shift.
- Information-thermodynamic bookkeeping: `sim_qit_szilard_landauer_cycle.py` and `sim_qit_strong_coupling_landauer.py` show that measurement, feedback, erasure, and strong-coupling corrections can be handled in finite operator language.
- Coordination failure: `sim_qit_moloch_coordination_trap.py` shows a bounded shared-resource trap where greedy local extraction depletes a common resource faster than scheduled repair preserves it.
- Structural engine/runtime alignment: `qit_graph_engine_alignment_probe.py` is currently a drift signal, not a success anchor. Its result surface reports `KILL` and says the owner graph has drifted from the live runtime topology.

## What this maps to in AI research
### Predictive world models
The clean bridge is finite predictive-state estimation. Internal state updates can be represented as density-state changes under admissible probe updates. This is closest to predictive processing, state estimation, and bounded world-model adaptation.

### Active inference and free-energy language
The useful overlap is narrow: prediction error minimization, belief update, and bounded adaptation. The repo does not yet earn a full active-inference action-policy theorem, Markov-blanket theorem, or a claim that the whole stack is literally FEP.

For the routed support version, read [[fep-research-atlas-and-crosswalk]], especially [[fep-information-geometry-and-gradient-flow]], [[fep-distinguishability-and-operational-identity]], and [[fep-critique-and-assumption-ledger]].

### Information bottleneck and representation compression
Density-matrix language is already a good fit for kernel structure, spectral truncation, and certain bottleneck-style descriptions. This bridge is strongest in representation geometry and weakest when people try to turn every neural computation into a literal CPTP channel.

### Alignment and failure modes
The current bridge is not “AI alignment solved.” The stronger current overlap is failure analysis:
- reward hacking and deceptive behavior belong with harness / admission / fail-closed process design
- shared-resource traps belong with bounded Moloch-style coordination rows
- measurement and observability limits belong with predictive-model mismatch

### Multi-agent and world-engine language
The repo can now support a bounded shared-resource coordination story and a bounded predictive-world-model story. It still does not earn a full world-engine doctrine, universal social model, or general AI agency theorem.

It is now also useful to distinguish two levels clearly:
- source/doctrine level: the legacy and synthesis materials are converging on a broader recursive engine pattern spanning science method, prediction-first perception, memory, emotion/personality state grammar, and social coordination
- earned live-repo level: only bounded predictive-world-model and coordination slices are currently supported directly by result files

That distinction should remain explicit.

## Live repo status
- Owner rows: `sim_qit_predictive_world_model.py`, `sim_qit_szilard_landauer_cycle.py`, `sim_qit_strong_coupling_landauer.py`, `sim_qit_moloch_coordination_trap.py`
- Supporting sidecars: `world_model_sim.py`, `alignment_sim.py`, `demon_fixed_sim.py`, `qit_graph_engine_alignment_probe.py`
- Current caution: the graph/engine alignment probe is presently a mismatch signal rather than a passing alignment proof, so this page should not use it as evidence that owner graph doctrine and live runtime topology still coincide.
- Research support pages: [[ai-ml-density-matrix-connections]], [[fep-and-active-inference-reference]], [[llm-bias-and-failure-modes-reference]], [[moloch-trap-reference]]

## Not earned
- general AGI theory
- universal alignment theorem
- consciousness admission
- full FEP identity between the stack and the world
- a claim that every AI object is naturally a density matrix or channel

## Recommended use
Use this page when the question is: which AI/foundational claims are actually supported by the live QIT rows, and which are still only research overlays.

## Related pages
- [[fep-research-atlas-and-crosswalk]]
- [[fep-information-geometry-and-gradient-flow]]
- [[fep-distinguishability-and-operational-identity]]
- [[current-research-overlays]]
- [[current-docs-vs-legacy-framing]]
- [[qit-engine-dev-framing]]
- [[codex-ratchet-cs-bounded-system-framing]]
- [[qit-vocabulary-discipline-reference]]
- [[operationalism-and-measurement-reference]]
- [[distinguishability-formal-reference]]
- [[stochastic-thermodynamics-reference]]
- [[ai-ml-density-matrix-connections]]
- [[fep-and-active-inference-reference]]
- [[llm-bias-and-failure-modes-reference]]
- [[moloch-trap-reference]]
- [[qit-engine-proto-ratchet-and-sim-plan]]
- [[probe-doc-result-map]]
- [[topic-map]]
