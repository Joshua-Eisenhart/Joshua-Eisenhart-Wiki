---
title: Markov Blankets, Boundaries, and Ratchet Cuts
created: 2026-06-19
updated: 2026-06-19
type: concept
framing: external_support_reference
status: current
claim_ceiling: boundary/blanket crosswalk only; a Markov blanket is not automatically an Axis0 cut, QIT cut, or Codex Ratchet quotient boundary
tags: [fep, markov-blanket, boundary, ratchet-cut, axis0, distinguishability]
sources:
  - https://arxiv.org/abs/1906.10184
  - https://arxiv.org/abs/2201.06387
  - https://arxiv.org/abs/2001.06408
  - https://arxiv.org/abs/2105.11203
  - /Users/joshuaeisenhart/.codex/attachments/f86e4a29-48ca-4984-bcea-7943521c2303/pasted-text.txt
---

# Markov Blankets, Boundaries, and Ratchet Cuts

This page keeps boundary language precise. FEP Markov blankets are useful, but they do not automatically become Codex Ratchet cuts.

## FEP partition

The standard FEP partition separates:

- external states;
- sensory states;
- active states;
- internal states.

The blanket is the sensory-plus-active boundary that mediates conditional independence between internal and external states under the relevant model assumptions.

## Crosswalk

| Boundary object | Role | Safe Codex Ratchet relation | Blocked collapse |
|---|---|---|---|
| Markov blanket | statistical conditional-independence boundary | support language for mediation and thingness | `Markov blanket = Axis0 cut` |
| sensory state | state affected by external states | possible probe/readout surface | not raw truth |
| active state | state affecting external states | possible intervention/control surface | not ratchet action by default |
| ratchet cut | local boundary where candidates are admitted, killed, or quotiented | must be finite/probe-relative and receipt-backed | not guaranteed by FEP |
| Axis0 cut | open bridge object in the owner system | requires its own evidence packet | not imported from blanket theory |

## Cut checklist

A local ratchet cut needs:

- finite carrier or finite readout;
- probe equivalence or blocked equivalence;
- operation/control surface;
- negative or contrast condition;
- artifact path or blocked-reason receipt;
- explicit downstream claim ceiling.

## Critique pressure

The critique literature matters here. Blanket definitions vary, and some FEP derivations depend on additional assumptions. If a page uses blanket language, it should name whether the claim is statistical, dynamical, physical, or analogy-only.

## Safe use

- Use Markov blankets as external support for bounded boundary vocabulary.
- Use them to ask better cut/candidate questions.
- Preserve the internal/external/active/sensory distinction when relevant.

## Blocked use

- Do not identify blankets with Axis0.
- Do not treat conditional independence as a physical boundary without extra evidence.
- Do not use blanket language to promote bridge, gravity, QIT-engine, or consciousness claims.

## Read next

- [[fep-particular-physics-and-ness]]
- [[fep-distinguishability-and-operational-identity]]
- [[fep-to-axis0-bridge-claim-ceilings]]
- [[fep-critique-and-assumption-ledger]]
