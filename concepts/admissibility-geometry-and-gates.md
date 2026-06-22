---
title: Admissibility Geometry and Gates
created: 2026-06-21
updated: 2026-06-21
type: concept
status: proposal_design_current
claim_ceiling: architecture concept; not standalone proof system
---

# Admissibility Geometry and Gates

## Core idea

A gate is not merely a yes/no filter. In Research Ratchet, a gate is an operator over project state.

```text
GateOperator: State x Evidence -> StateTransition | Block | Error
```

The system is therefore a geometry of admissible transitions.

## Gate classes

```text
source gate       binds source intent and content hash
scope gate        checks object, claim ceiling, and allowed surface
owner gate        verifies owner approval / trust root when required
host gate         verifies host request + host receipt
act gate          requires real ACT before proof
proof gate        checks eval measurements / GateProof / ProofBundle
basin gate        checks deepen/leak/split/kill classification
frontier gate     controls whether a branch may update accepted state
collapse gate     detects overclaim, fixture authority, docs-green, stale proof
```

## Relation to ClaimGate

ClaimGate supplies the authority chain:

```text
proposal -> owner approval -> host request -> host receipt
```

v39 tightened the chain with unified admission logic, expiry, replay detection, approval decision checks, and request-hash binding.

v40 wired trust-root verification through consume, but left enforcement opt-in.

v41 closes the enforcement boundary: enforcing gates require trust-root verified owner and host authority, and persistent approval replay protection is present for enforcement-grade approvals.

## Relation to Leviathan

Leviathan supplies the effect/eval proof loop:

```text
INGEST -> OBSERVE -> PROPOSE -> ADMISSION_GATE -> ACT -> VERIFY_GATE -> ADAPT -> DECIDE/APPLY -> UPDATE -> EMIT
```

Effect answers what was attempted and what happened.

Eval answers whether the evidence satisfies the obligation.

Semantic Control turns scored evidence into the next tick plan.

## Relation to Spinor Memory

Spinor Memory records the ordered operator trace:

```text
source_bind -> owner_approve -> host_request -> host_consume -> observe_effect -> eval_measure -> seal_receipt -> promote_frontier
```

The operator trace is part of identity. Same claim text with a different trace is a different project state.

## Failure classes

```text
fake proof
measurement missing
stale facts
effect absent
projection green
LLM verdict
fixture authority overclaim
untrusted key for enforcement
replay attempt
source drift
basin leakage
```

Each failure class should have a named graveyard/collapse entry and an eval/probe when possible.
