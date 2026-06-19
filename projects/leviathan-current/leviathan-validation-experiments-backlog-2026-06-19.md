---
title: Leviathan Validation Experiments Backlog
created: 2026-06-19
updated: 2026-06-19
type: validation-backlog
status: proposal-only
claim_ceiling: validation backlog only; none of these experiments has run or certified Leviathan runtime behavior
tags: [leviathan, validation, experiments, fep, event-bus, world-model, policy]
sources:
  - /Users/joshuaeisenhart/.codex/attachments/9d7bccf2-41e3-4c04-9659-2e2acb2d01da/pasted-text.txt
  - projects/leviathan-current/packet-13-pasted-fep-runtime-boundary-audit-intake-2026-06-19.md
  - projects/leviathan-current/world-model-reconciler-fep-support-2026-06-19.md
---

# Leviathan Validation Experiments Backlog

These experiments are backlog pressure only. They are not proof that the current runtime passes.

## Experiment Cards

| Experiment | What it tests | Evidence required | Current status |
|---|---|---|---|
| Belief-state planner benchmark | hidden-state planning beats reactive/state-only baselines | clean fixture, baseline, result receipt | not run |
| Event-bus completeness and replay | actions emit auditable events and replay cleanly | event IDs, correlation IDs, state deltas, replay result | not run |
| Context reconciliation drill | contradictory context is merged or surfaced | contradiction packet, reconciler output, no silent corruption | not run |
| Policy/gating separation test | policy blocks unsafe actions without code edits | allowed/disallowed actions, false allow/deny counts | not run |
| Human-loop escalation trial | risky actions route to human approval | approval-required action logs and execution block proof | not run |
| Receipt-vs-claim discipline audit | outputs distinguish execution from synthesis | claim-to-receipt table | not run |

## Why These Matter

They test Leviathan's strongest runtime virtues:

- policy boundaries;
- auditable events;
- context/state handling;
- world-model/reconciler behavior;
- human-loop control;
- receipt discipline.

## Promotion Rule

No experiment becomes a wiki proof claim until it records:

- source SHA or raw source snapshot;
- clean status;
- command or runner;
- result artifact;
- negative/control case;
- allowed and blocked claims.

## Read Next

- [[projects/leviathan-current/proof-backed-status-dashboard]]
- [[projects/leviathan-current/packet-14-pasted-fep-atlas-and-leviathan-boundary-intake-2026-06-19]]
- [[projects/leviathan-current/leviathan-claim-ceilings-2026-06-19]]
- [[projects/leviathan-current/world-model-reconciler-fep-support-2026-06-19]]
- [[projects/leviathan-current/security-gate-stack-v4-2026-06-19]]
- [[active-inference-benchmark-fixtures]]
