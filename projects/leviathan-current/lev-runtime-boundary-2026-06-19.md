---
title: Lev Runtime Boundary
created: 2026-06-19
updated: 2026-06-19
type: architecture-boundary
status: current-source-synthesis
claim_ceiling: runtime boundary map only; not proof that every package, surface, or daemon path works
tags: [leviathan, lev, runtime-boundary, architecture, policy, event-bus]
sources:
  - /Users/joshuaeisenhart/.codex/attachments/9d7bccf2-41e3-4c04-9659-2e2acb2d01da/pasted-text.txt
  - projects/leviathan-current/architecture-planes-and-ownership.md
  - projects/leviathan-current/proof-backed-status-dashboard.md
  - projects/leviathan-current/exec-poly-daemon-package-posture-v4-2026-06-19.md
---

# Lev Runtime Boundary

Leviathan should not be summarized as a generic graph stack. The safer current wiki shape is:

```text
agent-human runtime
  = policy/control boundary
  + orchestration/execution boundary
  + graph/context/memory boundary
  + event/audit boundary
  + package/surface boundary
  + human-loop/accountability boundary
```

## Boundary Map

| Boundary | What it owns | Safe claim | Proof question |
|---|---|---|---|
| FlowMind | policy, declarations, workflow/control intent | contract/control surface | which rules are runtime-enforced now? |
| Orchestration | scheduling, worker coordination, execution strategy | execution-plane design and code surface | which default workflows pass in a clean clone? |
| Graph/context/memory | state, context, lineage, recall, reconciliation | source-backed state/memory direction | which backend or flow is proof-backed? |
| Event Bus | `LevEvent`, audit, replay, trace semantics | audit/event spine | do state-changing actions emit replayable events? |
| Exec | SDK-first execution contract | central execution package | which named SDK commands pass? |
| Poly | registry, CLI/binder/surface projection | surface projection layer | which bindings are current and tested? |
| Daemon | process lifecycle, health, supervision | lifecycle package surface | is default daemon proof green now? |
| AgentPing / AgentLease / AgentGuard | human loop, authority, permission/accountability | product/security lanes | which flows are implemented and enforced? |

## Main Correction

FlowMind, Graph, Event Bus, Exec, Poly, and Daemon are not interchangeable. A page that says "the graph does everything" or "FlowMind proves runtime health" is collapsing boundaries.

## Safe Summary

Leviathan is strongest as a runtime-boundary discipline: explicit policy, explicit state, explicit events, explicit execution surfaces, and explicit human/permission boundaries. Runtime health still has to be proved row by row.

## Read Next

- [[projects/leviathan-current/leviathan-fep-runtime-boundary-2026-06-19]]
- [[projects/leviathan-current/packet-14-pasted-fep-atlas-and-leviathan-boundary-intake-2026-06-19]]
- [[projects/leviathan-current/proof-backed-status-dashboard]]
- [[projects/leviathan-current/leviathan-claim-ceilings-2026-06-19]]
- [[projects/leviathan-current/provenance-status-guardrails-2026-06-19]]
- [[projects/leviathan-current/exec-poly-daemon-package-posture-v4-2026-06-19]]
- [[projects/leviathan-current/release-readiness-ladder-v4-2026-06-19]]
