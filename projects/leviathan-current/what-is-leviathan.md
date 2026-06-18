---
title: What Is Leviathan
created: 2026-06-17
updated: 2026-06-17
type: explanatory-wiki-page
status: packet-1 current-authority synthesis
claim_ceiling: current repo docs plus cheap code/package checks; not maintainer acceptance, not full implementation proof
sources:
  - /Users/joshuaeisenhart/GitHub/leviathan/README.md
  - /Users/joshuaeisenhart/GitHub/leviathan/docs/README.md
  - /Users/joshuaeisenhart/GitHub/leviathan/docs/NORTH_STAR.md
  - /Users/joshuaeisenhart/GitHub/leviathan/docs/ROADMAP.md
  - /Users/joshuaeisenhart/GitHub/leviathan/docs/ARCHITECTURE.md
---

# What Is Leviathan?

## Plain answer

Leviathan / Lev is an open runtime for agent-human systems.

It is not just a prompt wrapper and not just a chat UI. The current docs frame it as a runtime where agents can act through real surfaces, under explicit policy, with graph/memory context, event receipts, execution boundaries, and human approval loops.

Short version:

```text
Leviathan tries to move agents from "talking in chat" to "acting through governed runtime surfaces".
```

## What the runtime is trying to hold together

The current authority docs describe these pieces as one runtime:

| Piece | Plain role | Support |
|---|---|---|
| **FlowMind** | Control and policy declarations; the place where constraints and intent are expressed. | `README.md`, `NORTH_STAR.md`, `ARCHITECTURE.md` |
| **Orchestration** | Scheduling, worker coordination, execution strategy, queues, loops. | `ARCHITECTURE.md`, specs/code-package scout |
| **Graph** | State, knowledge, memory, lineage, context projection. | `README.md`, `ARCHITECTURE.md`, specs/code-package scout |
| **Event Bus** | Canonical event spine, replay, audit, cross-plane lifecycle events. | `README.md`, `ARCHITECTURE.md`, specs/code-package scout |
| **Exec / Poly / Daemon** | Execution SDK, protocol/CLI bindings, process/runtime supervision. | `ARCHITECTURE.md`, package/code scout |
| **AgentPing** | Default human-loop surface and interaction layer. | `docs/README.md`, `NORTH_STAR.md`, AgentPing specs |
| **AgentLease** | Scoped trust / permission / accountability concept. | `NORTH_STAR.md`; implementation status still needs a deeper packet |

The cleanest current mental model is:

```text
Human intent enters through a surface.
FlowMind constrains and routes it.
Orchestration schedules the work.
Exec/Poly/Daemon run or expose it.
Graph stores state and context.
Event Bus records lifecycle-significant changes.
AgentPing/AgentLease keep humans and permissions in the loop.
```

## What makes it different from ordinary agent frameworks

The docs position Lev as a runtime substrate rather than a model wrapper. Its distinctive bet is that durable value moves from prompts into runtime structure:

- context assembly instead of chat-history stuffing;
- graph state instead of stateless conversation;
- explicit policy instead of implicit assistant behavior;
- scoped leases instead of ambient permission;
- event receipts instead of vibes;
- surfaces instead of chat-only interaction;
- provider/runtime breadth instead of one-vendor lock-in.

## What exists now, at this support level

Observed from current docs and cheap package/code checks:

- Root package exposes `lev` at `core/poly/bin/lev`.
- Packages exist for `core/flowmind`, `core/orchestration`, `core/graph`, `core/event-bus`, `core/exec`, `core/poly`, `core/daemon`, `core/domain`, `core/memory`, `core/ui`, and related modules.
- `core/flowmind/system/constraint-manifold.flow.yaml` exists and names the kernel constraint manifold.
- `core/flowmind/src/kernel/constraint-manifold.ts` exists and names C1/C2 root validators.
- `crates/lev-kernel/` exists with Rust surfaces for the constraint manifold / ratchet admission kernel.
- Specs index claims 61 specs total.
- Roadmap claims 1,031 test files, 60+ CLI commands, 4 CI workflows, and a real foundation still needing hardening.

This page did not run install/build/test. Treat package/code existence as `observed file/path/package`, not as proof that the full runtime works end-to-end.

## What Leviathan is not, yet

The current docs themselves block overclaiming:

- universal context graph is not fully landed;
- enterprise readiness is not complete;
- architecture is ahead of some implementation areas;
- MCP server story is not complete;
- security hardening remains open;
- AgentLease and enterprise governance need implementation-status separation;
- docs-to-code ratio and DX are named risks.

So the honest status is:

```text
The architecture is serious and partly implemented. The full product/runtime promise is not yet closed.
```

## Relationship to Josh / Codex Ratchet

Leviathan is not Codex Ratchet. It is also not separate from Josh's root frame.

The current repo explicitly says Josh identified the unification of two constraint systems: ontological constraints such as ratchet, finitude, and non-commutation, and operational constraints such as ABAC, leases, and containment. Current code/docs also contain a constraint manifold with C1 Finitude and C2 Non-Commutation as root kernel constraints.

Safe bridge:

```text
Codex Ratchet works on the mathematical/proof/admissibility kernel.
Leviathan applies related constraint structure as an agent-human runtime.
```

The exact contribution map still needs Packet 4 provenance work. This page only says the current docs/code contain strong contribution signals.
