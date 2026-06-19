---
title: Variational Free Energy Core
created: 2026-06-19
updated: 2026-06-19
type: concept
framing: external_support_reference
status: current
claim_ceiling: formal FEP reference only; does not prove Codex Ratchet, Leviathan, QIT-engine, Axis0, manifold, physics, or consciousness claims
tags: [fep, variational-free-energy, bayesian-inference, prediction-first, external-reference]
sources:
  - https://arxiv.org/abs/1906.10184
  - https://arxiv.org/abs/2201.06387
  - /Users/joshuaeisenhart/.codex/attachments/f86e4a29-48ca-4984-bcea-7943521c2303/pasted-text.txt
---

# Variational Free Energy Core

This page isolates the formal FEP core so [[fep-and-active-inference-reference]] does not have to carry every downstream analogy.

## Core expression

```text
F = E_q[-ln P(y,x)] - H[q(x)]
```

`F` is variational free energy for current inference. It is not the same object as expected free energy `G`, which is used for future policy evaluation in active inference.

## Two standard decompositions

| Decomposition | Meaning | Wiki guardrail |
|---|---|---|
| `F = D_KL[q(x) || P(x|y)] - ln P(y)` | free energy bounds surprise because KL divergence is nonnegative | requires probabilistic assumptions; not a generic "constraint" proof |
| `F = D_KL[q(x) || P(x)] - E_q[ln P(y|x)]` | complexity minus accuracy | useful neighbor for parsimony, but not identical to F01 finitude |

## Object map

| FEP object | Plain role | Codex Ratchet crosswalk | Guardrail |
|---|---|---|---|
| `q(x)` | approximate posterior / recognition density | candidate internal readout over hidden state | do not call it truth |
| `P(y,x)` | generative density over observations and hidden causes | model side of prediction-first pages | not automatically `M(C)` |
| `y` | observation / sensory state | probe output or readout analogy | not raw reality |
| `x` | hidden state variable | latent cause analogy | not primitive ontology |
| `H[q]` | entropy of recognition density | uncertainty language | not standalone viability |
| `D_KL` | mismatch between distributions | distinguishability support language | not QIT admission by itself |

## Safe wiki use

- Support prediction-first processing language.
- Distinguish current perception/update `F` from future policy/search `G`.
- Explain why surprise means self-information, not colloquial surprise.
- Provide external vocabulary for model evidence and approximate inference.

## Blocked use

- Do not infer F01 or N01 from the formula.
- Do not treat complexity-accuracy as the same as the ratchet's weakest-survivor doctrine.
- Do not treat `q(x)` as a literal holodeck state without a local model.
- Do not treat this page as sim evidence.

## Read next

- [[expected-free-energy-policy-selection]]
- [[belief-state-tree-search-and-finite-horizons]]
- [[fep-critique-and-assumption-ledger]]
- [[fep-research-atlas-and-crosswalk]]
