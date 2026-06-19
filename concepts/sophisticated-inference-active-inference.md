---
title: Sophisticated Inference and Belief-State Planning
created: 2026-06-19
updated: 2026-06-19
type: concept
framing: current
status: external_support_reference
claim_ceiling: external reference and analogy for active inference / belief-state planning only; not Codex Ratchet proof, not Leviathan implementation proof, not QIT-engine or manifold admission
tags: [active-inference, fep, world-model, prediction-first, belief-state-planning, research, external-reference]
sources:
  - https://arxiv.org/abs/2006.04120
  - /Users/joshuaeisenhart/.codex/attachments/ff934da4-149e-496b-b1af-13251241798a/pasted-text.txt
  - /Users/joshuaeisenhart/.codex/attachments/863b6071-0cfa-4637-b223-eb5d5695ebfc/pasted-text.txt
  - /Users/joshuaeisenhart/Codex-Ratchet/system_v5/docs/CONSTRAINT_SURFACE_AND_PROCESS.md
  - /Users/joshuaeisenhart/Codex-Ratchet/system_v5/docs/LLM_CONTROLLER_CONTRACT.md
---

# Sophisticated Inference and Belief-State Planning

## Status

External reference / analogy. This page adds Friston, Da Costa, Hafner, Hesp, and Parr's arXiv paper "Sophisticated Inference" as a support source for active inference, expected free energy, recursive belief-state planning, epistemic affordance, and finite planning-horizon caveats.

It must not be used as proof of Codex Ratchet ontology, QIT engines, Axis0, bridge/physics claims, manifold admission, or Leviathan runtime correctness.

Atlas route: [[fep-research-atlas-and-crosswalk]] is now the hub for FEP/active-inference routing; use [[belief-state-tree-search-and-finite-horizons]], [[expected-free-energy-policy-selection]], and [[active-inference-benchmark-fixtures]] for the finite-horizon planning leaves.

## Source card

- Paper: "Sophisticated Inference"
- Authors: Karl Friston, Lancelot Da Costa, Danijar Hafner, Casper Hesp, Thomas Parr
- Source: https://arxiv.org/abs/2006.04120
- Submitted: 2020-06-07
- Categories: q-bio.NC; cs.AI
- Durable role in this wiki: external support for [[fep-and-active-inference-reference]], [[prediction-first-memory-vs-llm-memory]], and [[holodeck-qit-fep-leviathan-integration]]

## Core usable distinction

The paper distinguishes ordinary counterfactual action planning from recursive belief-state planning. The useful wiki translation is:

```text
ordinary planning: what might happen if this action is taken?
sophisticated inference: what would the agent later believe would happen if this action is taken?
```

The important object is not just a future world state. It is the possible future belief distribution after action, observation, and belief update. This supports the wiki's prediction-first and world-model cluster without collapsing Codex Ratchet into active inference.

## Why it fits the wiki

- [[fep-and-active-inference-reference]] already carries variational free energy, expected free energy, Markov blankets, policy selection, and critique boundaries. This page adds the recursive/sophisticated planning source.
- [[prediction-first-memory-vs-llm-memory]] needs a clean external support point for model-first update loops that are more than transcript retrieval.
- [[holodeck-qit-fep-leviathan-integration]] can cite this page for belief-state planning over an internal world-model, while preserving that QIT and Leviathan claims require their own evidence.
- [[leviathan-world-engine-memo]] can use it only as an FEP-compatible planning reference, not as a repo implementation claim.
- [[wiki-as-harness-architecture]] can use it as a formal neighbor for planning under uncertainty while still requiring finite witness paths and claim ceilings.

## Safe claims

- Active inference can value actions for the belief updates and information gain they enable, not only for immediate reward.
- Sophisticated inference treats planning as recursive evaluation of expected free energy over future belief states.
- Epistemic actions can be valuable because they reduce ambiguity or uncertainty before later exploitation.
- Belief-state tree search is a useful analogy for prediction-first memory, counterfactual world-modeling, and finite exploration under uncertainty.
- Scaling remains a caveat: the source examples are small, and practical use depends on factorization, sparsity, temporal hierarchy, and tractable state/action models.

## Blocked claims

- Do not say Codex Ratchet is active inference.
- Do not use this paper to prove F01/N01, `M(C)`, QIT engines, Axis0, bridge, physics, gravity, consciousness, or final manifold claims.
- Do not cite this paper as Leviathan OS implementation evidence.
- Do not convert expected free energy into reward optimization language without preserving the belief-distribution object and epistemic/pragmatic split.
- Do not use a story about active inference to bypass repo gates, result artifacts, or sim contracts.

## Codex Ratchet analogy boundary

The analogy is useful but narrow:

| Sophisticated inference | Codex Ratchet support analogy | Boundary |
|---|---|---|
| Beliefs about future beliefs | Candidate surfaces can be re-entered after finite checks change what is admissible | Not a formal derivation of `M(C)` |
| Expected free energy | Future uncertainty / ambiguity / preference structure can guide inquiry | Codex Ratchet filters by constraint survival, not agent preference |
| Epistemic action | A weird probe can be valuable because it changes the boundary map | The probe still needs a result artifact and claim ceiling |
| Belief-state tree search | Finite exploration over possible future model states | F01 forbids pretending the whole tree was searched |
| Horizon depth | Local minima and shallow planning are real failure modes | Not a license for broad ungated downstream work |

## Benchmark fixtures to mine later

These are source-inspired fixture ideas only. They are not Codex Ratchet evidence until implemented under the sim contract.

| Fixture | What it would test | Current status |
|---|---|---|
| T-maze epistemic cue | whether information-gathering is chosen before direct reward | future benchmark idea |
| Costly cue variant | whether short-term cost is tolerated for later uncertainty reduction | future benchmark idea |
| Navigation with hidden state | whether planning follows non-obvious routes through a belief map | future benchmark idea |
| Novelty-driven map learning | whether unknown regions are explored for model improvement | future benchmark idea |

Any such sim must obey [[lego-sim-contract]] and the current Codex Ratchet process docs before it can count as a real lego.

## Glossary additions

- **Sophisticated inference:** active-inference planning with beliefs about future beliefs.
- **Belief-state tree search:** search over possible future belief distributions rather than only objective world states.
- **Epistemic affordance:** an action's value for reducing uncertainty or improving future model state.
- **Expected free energy:** active-inference objective that combines pragmatic and epistemic value in policy selection.
- **Planning to learn:** choosing an action because it changes what the agent can learn next.
- **Local horizon trap:** failure mode where shallow planning depth leaves the agent in a local minimum.
- **Novelty term:** exploration pressure from uncertainty about the model or likelihood mapping.

## Bounded intake pack

```yaml
purpose: Add arXiv:2006.04120 as an external active-inference support source.
role: wiki_router
frame: External reference / analogy for belief-state planning and prediction-first agency.
read_order:
  - concepts/fep-and-active-inference-reference.md
  - concepts/prediction-first-memory-vs-llm-memory.md
  - concepts/holodeck-qit-fep-leviathan-integration.md
  - system_v5/docs/CONSTRAINT_SURFACE_AND_PROCESS.md
do_not_read:
  - as Leviathan-origin source
  - as Codex Ratchet origin source
  - as sim evidence or implementation proof
questions:
  - What future belief state does an action make available?
  - What uncertainty does a probe reduce?
  - What horizon-depth caveat blocks the analogy?
required_output: A bounded source card plus crosslinks, not raw paper import.
promotion_rule: analogy/support only until a local sim or proof artifact names variables, states, policies, update rules, controls, and result paths.
target_codex_surface: wiki concept support layer; no repo code or sim status change.
minimal_test: wiki_probe must remain clean after insertion.
```

## Read next

- [[fep-and-active-inference-reference]]
- [[prediction-first-memory-vs-llm-memory]]
- [[holodeck-qit-fep-leviathan-integration]]
- [[leviathan-world-engine-memo]]
- [[wiki-as-harness-architecture]]
