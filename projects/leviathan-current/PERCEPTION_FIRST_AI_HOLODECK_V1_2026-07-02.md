---
title: Perception-First AI Holodeck V1
created: 2026-07-02
updated: 2026-07-03
type: doctrine-and-build-spec
status: v1 buildable spec
claim_ceiling: scratch_diagnostic; promotion_allowed=false; no learning result, benchmark result, consciousness claim, or gate-admission claim is made by this page
tags: [lev, codex-ratchet, holodeck, perception, qit-engine, gates, learning]
sources:
  - ./WIZARD_QIT_ENGINE_MAP_2026-07-02.md
  - ./KERNEL_UPGRADES_LEVIATHAN_2026-07-02.md
  - ./GATE_DOCTRINE_ADMISSIBILITY_NOT_QUALITY.md
  - ../constraint-core/RATCHET_STATE_BY_TIER_2026-07-02.md
---

# Perception-First AI Holodeck V1 - 2026-07-02

## Doctrine

Owner doctrine, verbatim-faithful:

```text
I am making AI perception, not AI reasoning. From a Hume perspective this is how to make better reasoning by creating its proper foundations in perception.
```

The holodeck model is the engineering extension of the QIT engines into empirical reality. It is not an extra metaphor on top of the engines. It is the place where engine state meets measured event streams, surprise, prediction error, memory, and update receipts.

Cross-links:

- [Wizard QIT Engine Map](./WIZARD_QIT_ENGINE_MAP_2026-07-02.md) for QIT terrain/operator scheduling, surprise boundaries, inter-wave register state, and the G3 port.
- [Kernel Upgrades Leviathan](./KERNEL_UPGRADES_LEVIATHAN_2026-07-02.md) for the surprise bridge, EFE action edge, and engine-as-channel gate design.
- [Gate Doctrine: Admissibility, Not Quality](./GATE_DOCTRINE_ADMISSIBILITY_NOT_QUALITY.md) for the rule that code admits shaped evidence and LLMs do not self-grade.

## Humean Argument

LLMs are ideas without impressions. They can recombine, analogize, narrate, and reason over linguistic traces, but the reasoning surface is not grounded by its own sensory contact. Reasoning cannot ground itself because the thing that decides whether a distinction matters is not another idea; it is an impression channel with recurrence, error, surprise, memory, and correction.

The engine supplies the missing impression faculties as measured gated quantities:

| Faculty | Engineering quantity |
|---|---|
| Impression | Event-stream observation with source address, timestamp, and schema |
| Surprise | `surprise_bits` or prediction-error residual over expected event pattern |
| Belief state | Finite register state over predicted context/event patterns |
| Attention | Resource allocation toward high-surprise or high-expected-value stream regions |
| Memory | Bounded k-slot register with source hashes, decay/no-decay policy, and update receipts |
| Learning | Umegaki relative-entropy prediction/update step with controls and parity witnesses |

The controller thesis follows from that Humean frame: weak models lack perception, not knowledge. A weaker model wrapped in a perception engine can gain useful control because the harness supplies impressions, error signals, memory registers, attention allocation, and executable correction pressure. A stronger raw model without that substrate still has to reason from ideas whose grounding is implicit, lossy, and not receipt-bound.

## Perception Lane Contract

The perception lane is a trainable engine lane, not a prose evaluator.

| Engine | Role |
|---|---|
| PyTorch | Native trainable engine for the perception module: tensor state, autograd, graph/network machinery where applicable, and update execution. |
| Julia | Canon/parity witness for exact or algebraic reference checks when the carrier/update formula requires it. |
| JAX | Batched parity witness for high-volume event-pattern sweeps, capacity sweeps, and learning-curve agreement. |

Every learning update must be a computed Umegaki relative-entropy step:

```text
D(rho_observed || rho_predicted) = Tr[rho_observed (log rho_observed - log rho_predicted)]
```

The receipt must record the prior state, observed event batch, predicted distribution or density state, update rule, error value, post-update state, control state, source hashes, engine versions, and parity deltas. Gradients may optimize the update, but opaque gradients are not claims. A training curve is admissible only as a receipt series: epoch by epoch, update by update, with controls attached.

Training loops are gated per epoch:

| Gate | Required receipt |
|---|---|
| Shape | Input event rows, register state, update packet, and output prediction all validate. |
| Source | Event stream address, qit surprise address, and code hash are recorded. |
| Error | Umegaki error or declared prediction-error value is recomputed and stored. |
| Control | Frozen-prior, label-erased, capacity-edge, shuffled-stream, and cross-engine parity controls are evaluated at the epoch boundary. |
| Claim language | The epoch cannot claim learning unless the shuffled-stream control stays dead and the real stream improves under the declared metric. |

## Holodeck V1 Spec

Status: `scratch_diagnostic`, `promotion_allowed=false`.

### Substrate

Empirical reality for V1 is Lev event history:

- the `.lev/context` JSONL stores as the observable event substrate;
- the QIT surprise stream, especially `qit_surprise_stream_v0` / `surprise_bits`, as the error-bearing tick stream;
- receipt paths, flow outcomes, graph digests, and gate verdicts as structured event families.

This is empirical in the engineering sense: it is the world the agent actually lives in. The substrate is not "the external world" in general. It is the measured stream of events that can be replayed, shuffled, held out, erased, hashed, and routed into gates.

### Model

Use the context-register prediction/update architecture from the bundle holodeck sim, scaled from toy register learning to Lev event-pattern prediction:

```text
input event window
-> k-slot context register
-> predicted next event family / surprise distribution
-> observed event family
-> Umegaki prediction error
-> gated update
-> next register state
```

The known scratch lineage says the k-slot register learns for `k <= 4` and hits a capacity edge at `k = 5` under aliasing. V1 must preserve that as a test condition, not assume unbounded memory.

### Error Signal

The error signal is the surprise stream. For V1, the primary target is not "understand the repo." The primary target is narrower:

```text
Given prior context-register state and recent Lev event history,
predict the next event-pattern family and its surprise profile.
```

Predictions feed the G3 `SurprisePredictor` port as evidence. They do not become port verdicts, gate verdicts, or policy decisions.

### Mandatory Controls

| Control | Pass condition |
|---|---|
| Frozen-prior no-decay | A non-updating or no-decay prior must fail to track real surprise improvement, or the learning claim is suspect. |
| Label-erased structure invariance | Event labels are erased or permuted while structure is preserved; structural observables should remain stable, label stories should not carry the result. |
| Capacity-edge sweep | Sweep register capacity across the expected edge; `k <= 4` and `k = 5` behavior must be measured rather than narrated. |
| Shuffled-stream control | Shuffled events must not learn real temporal or causal structure. If shuffled events improve like the real stream, the model learned a shortcut. |
| Cross-engine parity on learning curves | PyTorch learning curves must be checked against Julia/JAX witnesses for the declared observable, within a named tolerance and with divergence recorded. |

### Deliverable

The V1 deliverable is a perception module:

```text
Lev event stream + QIT surprise stream
-> bounded context-register predictor
-> Umegaki update receipts per epoch
-> controlled prediction curves
-> evidence packet for the G3 SurprisePredictor port
```

Allowed claim: the module emits controlled perception evidence for event-pattern prediction.

Blocked claims: it does not prove consciousness, world understanding, benchmark superiority, IGT truth, QIT canon promotion, or gate admission. It does not decide gates. It sends evidence into gates.

## Run More Of Lev With The Three Engines

The general pattern is to give Lev subsystems engine legs.

Graph-substrate digests already establish the shape: take a live substrate, digest it into engine-readable observations, run independent engine witnesses, emit receipts, and feed shaped evidence back to gates. V1 extends that pattern to:

| Lev subsystem | Engine-leg extension |
|---|---|
| Event streams | Event-pattern digests, prediction targets, holdout splits, shuffled controls, and per-epoch Umegaki receipts. |
| Receipt estate | Receipt-estate statistics: missing fields, stale sources, verdict-shaped payloads, negative-control coverage, and status-label drift. |
| Flow outcomes | Flow-outcome distributions: which routes converge, stall, regress, or trigger surprise boundaries. |
| Graph/world model | Graph digests plus event-stream digests, so world-model drift becomes measured rather than narrated. |
| Gates | Gate outcome prediction as evidence only, with hard separation between prediction and admission. |

The pattern is not "put physics words on Lev." The pattern is: take a Lev substrate, define observables, run torch as the trainable perception engine, run Julia/JAX as witnesses where scoped, attach controls, and preserve claim ceilings.

## Staging And Non-Claims

Stage this as a scratch diagnostic until the receipts exist:

1. Define the event schema and source-address policy for `.lev/context` JSONL and QIT surprise rows.
2. Build the PyTorch context-register predictor with frozen-prior, shuffled-stream, label-erased, and capacity sweeps.
3. Add Julia/JAX parity witnesses for the declared Umegaki/error observable and learning curves.
4. Emit an epoch receipt packet series and an aggregate result envelope.
5. Feed predictions into the G3 port as evidence, with adapter rejection for stale, malformed, or verdict-shaped payloads.
6. Only then evaluate whether a stronger status label is even eligible under gate doctrine.

What this is not:

- No consciousness claim.
- No claim that IGT labels are computation-layer truth; IGT stays rosetta.
- No claim that perception-module outputs are gates. They are evidence into gates, never gates.
- No claim that the holodeck has learned Lev until shuffled-stream controls fail to learn structure and real-stream curves improve under cross-engine parity.
- No claim that parity is proof. Parity is a witness condition and a diagnostic.

Claim ceiling: this page specs Holodeck V1 as perception-first AI infrastructure. It may be used to build the module and design its receipts. It may not be cited as a run result, admission result, or promoted QIT/Lev truth.

{"file":"projects/leviathan-current/PERCEPTION_FIRST_AI_HOLODECK_V1_2026-07-02.md","v1_specced":true,"controls":5}
