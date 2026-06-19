---
title: Active Inference Benchmark Fixtures
created: 2026-06-19
updated: 2026-06-19
type: benchmark-fixtures
framing: future_fixture_router
status: proposal_only
claim_ceiling: future fixture ideas only; no listed benchmark is Codex Ratchet evidence until implemented, run, and admitted under the repo sim/lego contract
tags: [active-inference, benchmark, fep, fixtures, sim-ideas, epistemic-action]
sources:
  - https://arxiv.org/abs/2006.04120
  - https://arxiv.org/abs/2009.08111
  - /Users/joshuaeisenhart/.codex/attachments/f86e4a29-48ca-4984-bcea-7943521c2303/pasted-text.txt
---

# Active Inference Benchmark Fixtures

These are future fixture ideas only. They are not Codex Ratchet evidence until built under the live sim/lego contract.

## Fixture list

| Fixture | What it tests | Useful signal | Required negative |
|---|---|---|---|
| T-maze epistemic cue | information-gathering before direct reward | agent seeks cue when uncertainty matters | cue ignored when uninformative |
| Costly cue | short-term cost for later uncertainty reduction | policy pays cost only when later value justifies it | no cost paid when cue has no value |
| Hidden-state navigation | route choice under latent map uncertainty | belief-state planning differs from greedy route | greedy baseline fails or differs |
| Novelty-driven map learning | exploration to improve model | novelty chosen when it changes future belief | novelty not chosen when redundant |
| Ambiguity trap | local horizon failure | shallow horizon gets stuck | deeper horizon escapes only under specified conditions |
| Boundary discovery probe | action to identify a hidden boundary | better partition after probe | fake boundary control rejected |

## Required sim discipline

Any future Codex Ratchet fixture must name:

- state space;
- observation model;
- action/probe set;
- finite horizon;
- policy objective;
- baseline/control;
- positive, negative, and boundary cases;
- artifact path;
- allowed and blocked claims.

## Claim ceiling

Even a passing active-inference fixture would show only that a toy model captures a bounded active-inference behavior. It would not prove Codex Ratchet, QIT engines, Leviathan runtime, Axis0, bridge, physics, gravity, or consciousness.

## Read next

- [[expected-free-energy-policy-selection]]
- [[belief-state-tree-search-and-finite-horizons]]
- [[lego-sim-contract]]
- [[fep-critique-and-assumption-ledger]]
