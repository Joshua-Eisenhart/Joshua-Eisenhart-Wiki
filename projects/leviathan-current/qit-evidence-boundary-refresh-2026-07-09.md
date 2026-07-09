# QIT Evidence Boundary Refresh - 2026-07-09

## Status

Local worktree and contract audit. This page corrects any reading that the July 7 evidence importer already makes the current QIT packets live mesh state.

## Local Repo Topology At Audit

Common repository:

`/Users/joshuaeisenhart/GitHub/lev`

Relevant worktrees:

| Worktree | Branch | Head before sync | Relevant state |
|---|---|---|---|
| `/Users/joshuaeisenhart/GitHub/lev` | `patch/waverun-engine-gates-20260630` | `e9a4ba7717dbc35e478b3db737a4d5b752ba8252` | contains pending QIT evidence-consumer and handler files plus orchestration changes |
| `/Users/joshuaeisenhart/lev-main` | `fable/cr-sim-eval-pack` | `77cf36c9d44c13fe4a3eeecfce87c3a52acd3d63` | contains one proof-bundle wording edit and local ratchet-policy receipts |

These are different branches and evidence families. A passing consumer in one worktree is not automatically integrated into the other or into upstream `main`.

## What Exists

The July 7 consumer receipt records a useful evidence-only shape:

```text
truth_state: proposed
evidence_kind: measurement
decision_ceiling: accepted_as_evidence_only
graph_mutation_allowed: false
compositor_apply_allowed: false
mesh_projection_allowed: false
```

It also records focused tests, typecheck, a broader orchestration test run, and a local k-of-n evidence quorum over the then-current QIT envelopes.

That is real host-boundary work. It is not current mesh admission.

## What The July 9 Audit Found Missing

For the 86/v84/92 evidence family and the new object/geometry receipts, the current path still needs:

- a current adapter into the active `RunEvidence` contract;
- `ProofBundle` binding over source hashes, trace, gates, claims, and blocked consumers;
- a durable idempotency identity;
- replay and double-consume tests;
- explicit `promotion_allowed=false` enforcement;
- a no-state-mutation integration test;
- proof that failed quorum cannot project;
- proof that host policy, not external evidence, authorizes projection.

The v84 adapter can be structurally parsed as non-authoritative evidence input, but structural parsing is not the same as a current proof-bound consumer.

## Current Safe Claim

```text
Codex Ratchet can emit bounded evidence envelopes.
Lev has a demonstrated evidence-only consumer shape and local quorum design.
The current multi-branch repo does not yet provide one synchronized,
ProofBundle-bound, idempotent path from the new QIT object receipts to
host-authorized mesh projection.
```

No graph, ontology, MMM, or mesh state mutation is earned by the July 9 packet audit.

## Required Integration Sequence

1. Synchronize and reconcile the relevant Lev branches without treating local receipts as upstream admission.
2. Port the QIT consumer onto the current proof contracts.
3. Bind a frozen Codex Ratchet object receipt.
4. Run focused tests, typecheck, and integration replay.
5. Double-consume the same receipt and prove one durable identity.
6. Tamper with a source hash, gate, and blocked-consumer field; all must fail.
7. Run k-of-n quorum with pass and fail populations.
8. Keep mesh projection disabled.
9. Add one explicit host policy and test that only it can authorize a projection.
10. Run a two-node partition/rejoin trial before any production claim.

## Related

- [[projects/leviathan-current/qit-evidence-consumer-receipt-2026-07-07]]
- [[projects/codex-ratchet/external-86-v84-92-foundations-engine-audit-receipt-2026-07-09]]
- [[projects/codex-ratchet/qit-lev-operationalization-plan-2026-07-09]]
- [[projects/codex-ratchet/current-research-frontier-2026-07-09]]
