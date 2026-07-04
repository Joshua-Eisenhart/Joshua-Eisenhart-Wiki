---
title: Gate doctrine - admissibility, not quality
created: 2026-07-02
type: doctrine-reference
status: distilled owner-approved doctrine
claim_ceiling: wiki doctrine reference distilled from owner-approved JP-facing source notes; describes gate semantics and integration seams, not new empirical proof
tags: [lev, codex-ratchet, gates, admissibility, engines]
---

# Gate Doctrine: Admissibility, Not Quality - 2026-07-02

## Bottom line

The inversion: code determines admissibility and survival, never quality.

Code does not say "this is good." Code says "this survived every declared check we currently know how to run, receipts attached." LLMs propose candidates, invent attacks, repair probes, and red-team the system. Code remembers each discovered failure mode as a permanent gate and re-runs it forever.

Status ladder:

```text
exists < runs < passes fresh local rerun < mutation-proven load-bearing < admitted by declared gate < canonical by process
```

## Related

- [Lev / CR Integration State](./LEV_CR_INTEGRATION_STATE_2026-07-02.md)
- [Relevant Docs Index](./RELEVANT_DOCS_INDEX_2026-07-02.md)
- [LINEAGE_AND_VERDICTS](../constraint-core/LINEAGE_AND_VERDICTS_2026-07-02.md)
- [RATCHET_STATE_BY_TIER](../constraint-core/RATCHET_STATE_BY_TIER_2026-07-02.md)

## Nine gate types

| Gate | What it admits | Lev example | CR example |
|---|---|---|---|
| Existence / shape | The artifact exists and matches declared schema. | `provider_evidence.v1` validates before a sim-eval sensor runs. | `codex_ratchet.engine_leg_result.v1` requires fields such as `written_at` and shaped `negative_tests`. |
| Execution | The artifact runs and exits cleanly. | core/eval tests pass and typecheck is clean before pack landing. | `probe_quotient` jax leg exits 0 in the shared venv. |
| Independent recomputation / parity | Two independent paths agree on the same observable. | Evaluator pack compares separately authored evidence lanes instead of trusting a payload number. | Julia and JAX compute the same named quantity, exact for integers or within float tolerance. |
| Polarity / mutation | The check flips when the claim breaks. | Sensor hardening verified "mutation-proven load-bearing"; neutralized guard must fail. | SMT control flips `unsat` to `sat`, or erased control changes the numeric observable. |
| Provenance / anti-self-grading | Producers cannot assert their own verdicts as gate observables. | `cr-result-adapter.ts` bans `all_pass`, `promotion_allowed`, and `formal_admission_allowed`. | Sim evidence carrying verdict-shaped fields is structurally rejected. |
| Conservation / invariants | Declared invariants survive changes. | Boundary rule: core ships the judge, plugins ship witnesses. | Content-addresses, source hashes, and promoted evidence references must remain stable and resolvable. |
| Claim-language | Words cannot outrun receipts. | ClaimGate/status language blocks promotion wording unless the receipt chain resolves. | Claim ceilings prevent `draft_unaudited` legs from being described as earned/admitted. |
| Freshness | Stale evidence is rerun or demoted. | Fresh source newer than result blocks admission until rerun. | Sparse single-engine drafts must be freshly rerun into full v1 legs before battery eligibility. |
| Basin / builder convergence | Independent blind builders converge on behavior, or divergence measures a missing constraint. | k-builder convergence can become a code witness. | Self-grading ban, Julia-leg fix, and eval-builder/sim-contract convergence were basin events. |

## Three-engine role contract

The engines are not three copies of the same check.

| Engine | Role | Contract |
|---|---|---|
| Julia | exact / judge | Algebraic, symbolic, exact checks; carries Z3-style formal lanes where applicable. |
| JAX | scale / throughput | `vmap` / `jit` style batched sweeps and high-volume recomputation. |
| PyTorch | gradient / steerable | Autograd lane that can answer which direction improves a metric, not only pass/fail. |

One engine is testimony. Two independent engines are parity. Three role-separated engines are parity plus scale plus gradient.

## Four integration seams

| Seam | Meaning |
|---|---|
| Evaluators | Engine lanes upgrade what admission can check: evidence carries independent recomputation, and the sensor gates on agreement. This is the live cr packs plus adapter seam. |
| Graph + world model, outbound and inbound | Outbound: engine results become world-model measurements and graph nodes with hash-chained provenance. Inbound: graph digest lanes point engines at the graph itself, so drift becomes a measured quantity. |
| Flows / control | Engine tick stream emits `belief`, `surprise_bits`, and `fe_gradient`; surprise routes novelty/urgency into scheduling. The reverse edge is expected-free-energy action selection over Lev's world/action model. |
| Trust spine | Every engine lane ships an executable falsifier. Receipts become re-derivable: rerun the lane and watch the negative control flip. |

## LLM scoring as measurement

LLM-as-sensor-input is allowed. LLM-as-admission-decision is banned.

Rules for LLM scoring lanes:

- N-judge parity: independent judges must converge before the judgment becomes a measurement.
- Paraphrase and label-permutation invariance: the same verdict should survive wording and label erasure.
- Adversarial refuter: a prompted attack lane must try to break the candidate or expose overclaiming.

One LLM opinion is testimony. Multiple independent opinions surviving permutation and refutation can become a measurement consumed by a deterministic gate.

## Sim to vibe-code mapping

| Sim method | Vibe-code counterpart |
|---|---|
| engine legs | independent verification lanes on a change: tests, property spec, second implementation, shadow run |
| negative controls | mutation testing: neutralize the claimed fix and require the suite to go red |
| fresh rerun | no cached greens |
| tool manifests | declared dependencies and permissions with reasons |
| claim ceilings | PR, commit, and doc language cannot exceed receipts |
| registry | graph tracks what has earned each status rung |
| stage gate | merge train: draft -> reviewed -> mutation-proven -> canary -> main |

The method is not physics-specific. A sim is any bounded claim with declared observables and executed falsifiers.

## Ratchet property

Every discovered failure mode becomes a permanent gate: fabricated receipt, rounding hole, self-graded pass, decorative test, stale rerun, sparse leg, overclaiming language. The survivor set is quality under a monotonically growing constraint family.

This is the ratchet:

```text
LLMs explore and attack; code remembers and enforces
```

## Honest gap

Evidence and claims are gated end to end today. The unified diff-admission pipeline remains composition work: existence -> runs -> tests -> mutation-proven -> parity where possible -> claim-language checked. The pieces exist across Lev and CR, but the single standing harness for arbitrary code diffs is not yet the settled path.

## World / game-engine framing

An admission system plus a world model plus a tick is a game engine.

| Game-engine term | Lev / CR term |
|---|---|
| state kernel | measurement -> world model -> graph node seam |
| tick | surprise stream |
| action edge | EFE loop |
| candidate law layer | constraint core |

The swarm generates high-variance candidates. Gates decide admission. The world persists what survived.

## Claim ceiling

This page is doctrine reference, not new proof. It may be used to design or review gates, adapters, and integration seams. It may not be used to promote any result above the receipt rung earned by its executable evidence.
