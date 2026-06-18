---
title: AgentLease Scoped Authority
created: 2026-06-18
updated: 2026-06-18
type: product-surface-map
status: candidate/controller-verification-required
claim_ceiling: current-source wiki map; not full AgentLease implementation proof; not enterprise permission readiness
---

# AgentLease Scoped Authority

## Bottom line

AgentLease is the name Lev uses for expiring, scoped authority: agents should receive bounded permission grants rather than open-ended power.

The checked sources support the concept and show some lease-related code, but do not support a claim that a complete AgentLease product is fully landed. The honest wiki status is: **named North Star system + roadmap enterprise target + observed lease primitives in ABAC/GameAI/example policies + some lock artifacts.**

## What current docs say

| Claim | Support | Source |
|---|---|---|
| AgentLease makes interactions accountable. | product vision / repo-doc claim | `/Users/joshuaeisenhart/GitHub/leviathan/docs/NORTH_STAR.md` lines 17-23 |
| AgentLease is one of the three systems: scoped permission grants, step-up auth, lease issuance, expiration-based accountability. | product vision / repo-doc claim | `/Users/joshuaeisenhart/GitHub/leviathan/docs/NORTH_STAR.md` lines 44-66 |
| Sovereignty-by-default includes AgentLease scoped permissions. | product positioning | `/Users/joshuaeisenhart/GitHub/leviathan/docs/NORTH_STAR.md` lines 35-38 |
| Enterprise pillars include ABAC permissions, approval queues/HITL, audit trails, kill switches, resource governors, compliance. | roadmap / intended work | `/Users/joshuaeisenhart/GitHub/leviathan/docs/ROADMAP.md` lines 54-61 |
| Enterprise readiness is not complete. | roadmap / current state | `/Users/joshuaeisenhart/GitHub/leviathan/docs/ROADMAP.md` lines 14-31 |

Safe summary:

```text
AgentLease is Lev's scoped-authority story: grant, monitor, expire, and revoke permissions around agent actions.
```

## Observed implementation-adjacent surfaces

### Rust ABAC lease primitive

Observed file:

- `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-abac/src/lease.rs`

Support level: **observed code file**.

What it contains:

- `LeaseGrant` with subject, resource, permissions, issued/expiry timestamps, optional scope, and revoked flag.
- `is_valid`, `has_permission`, `revoke`, and `remaining` methods.
- `LeaseVerifier::verify` checking revoked, expired, and missing permission cases.

Claim ceiling: this is a lease primitive, not proof of complete AgentLease runtime integration.

### GameAI lease manager

Observed file:

- `/Users/joshuaeisenhart/GitHub/leviathan/plugins/core-gameai/src/leasing/lease-manager.ts`

Support level: **observed code file**.

What it contains:

- A resource-reservation `LeaseManager` with TTL, exclusive/shared leases, holder/resource indexes, wait queue, listeners, event types, and deadlock detection intent.
- Its module comment says it maps to FlowMind's existing `Requirement { type: 'lease' }` contract.

Claim ceiling: useful current lease mechanism, but not full AgentLease product proof.

### Policy examples

Observed files:

- `/Users/joshuaeisenhart/GitHub/leviathan/context/examples/governance/lease-policy.yaml`
- `/Users/joshuaeisenhart/GitHub/leviathan/context/examples/flowmind/lease-policy.yaml`

Support level: **draft examples**.

Both files explicitly say draft/illustration. They are useful for intended policy shape, not runtime proof.

### Agent-lease lock artifacts

Observed file search found:

- `/Users/joshuaeisenhart/GitHub/leviathan/.agent-lease/locks/agent-lease-lev-push-5351e121.lock`
- `/Users/joshuaeisenhart/GitHub/leviathan/.agent-lease/locks/agent-lease-lev-b2b56a0c.lock`

Support level: **observed artifact path**.

Claim ceiling: lock artifacts suggest prior/active lease workflow traces. They do not prove the whole workflow is correct, current, or cleanly integrated.

## Tension to preserve

There are at least three live readings:

1. **Product system name** — AgentLease as one of the three North Star systems.
2. **Runtime primitives** — lease grants/verifiers/managers/policy examples exist in code and examples.
3. **Enterprise readiness gap** — roadmap says enterprise pillars are not enterprise-ready; ABAC/approval queues/compliance are future or partial work.

Do not collapse these into one story. The useful wiki form is a status ladder:

```text
named system < observed lease primitives < integrated runtime enforcement < enterprise-ready authority system
```

The current checked state is between the first two and partly into the third for specific paths, but not the fourth.

## What is open

- No `AgentLease` package/file name was found by filename search in the active repo tree.
- This page did not run ABAC tests, GameAI tests, or FlowMind policy enforcement checks.
- It is still open how `crates/lev-abac`, `plugins/core-gameai`, FlowMind requirements, and `.agent-lease` lock workflows compose into one product surface.
- The roadmap explicitly says enterprise pillars are not fully ready; approval queues/HITL remain roadmap-level until tested.

## Overclaim guard

Safe wording:

```text
AgentLease is Lev's scoped-authority concept. Lease primitives and policy examples exist, but complete product/runtime integration still needs verification.
```

Unsafe wording:

```text
AgentLease is fully implemented, enterprise-ready, or universally enforced across Lev.
```
