---
title: Expected Free Energy Policy Selection
created: 2026-06-19
updated: 2026-06-19
type: concept
framing: external_support_reference
status: current
claim_ceiling: active-inference policy-selection support only; expected free energy is not the Codex Ratchet objective and not a Leviathan implementation claim
tags: [fep, active-inference, expected-free-energy, policy-selection, epistemic-action]
sources:
  - https://arxiv.org/abs/2006.04120
  - https://arxiv.org/abs/2009.08111
  - /Users/joshuaeisenhart/.codex/attachments/f86e4a29-48ca-4984-bcea-7943521c2303/pasted-text.txt
---

# Expected Free Energy Policy Selection

Expected free energy belongs to future/counterfactual policy evaluation. Keep it separate from [[variational-free-energy-core]], which handles current inference/update.

## F versus G

```text
F = current inference / perception update
G = future policy evaluation / counterfactual planning
```

In active inference, policy selection evaluates expected free energy across possible actions and observations. This can combine epistemic value and pragmatic value.

## Two pressures

| Pressure | Active-inference role | Wiki crosswalk | Guardrail |
|---|---|---|---|
| Epistemic value | information gain, ambiguity reduction, exploration | a weird probe can be valuable because it changes the boundary map | not evidence unless the probe has an artifact |
| Pragmatic value | prior preference satisfaction / exploitation | useful contrast with goals, viability, and survival | not the ratchet objective |

## Popper pressure analogy

The safe analogy is:

```text
epistemic action in FEP
  ~ falsifiable probe in Codex Ratchet

information gain
  ~ better boundary map of M(C)

policy horizon
  ~ finite probe sequence with no claim of exhaustive search
```

The unsafe collapse is:

```text
expected free energy = ratchet objective
```

Codex Ratchet filters by constraint survival and admission gates. It does not simply optimize prior preferences.

## Da Costa et al. caveat

The discrete active-inference reward source is useful because it states conditions under which active inference relates to Bellman-optimal action over finite horizons. This supports benchmark design and horizon caveats. It does not make active inference a universal implementation proof.

## Safe use

- Explain why information-gathering action can be rational before exploitation.
- Design future toy fixtures around epistemic versus pragmatic pressure.
- Compare policy horizons to finite probe paths.

## Blocked use

- Do not promote Codex Ratchet, QIT-engine, Axis0, bridge, or manifold claims from this page.
- Do not say Leviathan implements active inference unless current Leviathan repo evidence shows it.
- Do not turn active inference into a teleological doctrine for the ratchet.

## Read next

- [[belief-state-tree-search-and-finite-horizons]]
- [[active-inference-benchmark-fixtures]]
- [[fep-critique-and-assumption-ledger]]
- [[fep-research-atlas-and-crosswalk]]
