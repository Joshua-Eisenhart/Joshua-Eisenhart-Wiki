---
title: Leviathan Current Concept Map Start
created: 2026-06-17
updated: 2026-06-17
type: concept-map
status: starter map / needs packet expansion
claim_ceiling: synthesis from first authority-doc pass; not full repo understanding
sources:
  - /Users/joshuaeisenhart/GitHub/leviathan/README.md
  - /Users/joshuaeisenhart/GitHub/leviathan/docs/NORTH_STAR.md
  - /Users/joshuaeisenhart/GitHub/leviathan/docs/ROADMAP.md
  - /Users/joshuaeisenhart/GitHub/leviathan/docs/ARCHITECTURE.md
  - /Users/joshuaeisenhart/wiki/wizard/harness-consolidated/14_leviathan_os_constraint_map.md
---

# Leviathan Current Concept Map — Start

## Plain core

Leviathan is a runtime for agent-human systems.

It tries to move agents out of pure chat and into real, governed action surfaces: browser buttons, dashboards, voice, notifications, CLIs, MCP, worker execution, approvals, receipts, and graph memory.

## The four-plane runtime

Current architecture names a four-plane boundary:

| Plane | Plain role | Current path anchor |
|---|---|---|
| FlowMind | control / policy declarations | `core/flowmind/**` |
| Orchestration | scheduling and execution strategy | `core/orchestration/**` |
| Graph | state, knowledge, memory, lineage | `core/graph/**` |
| Event Bus | event spine, replay, audit | `core/event-bus/**` |

Important non-collapse rule from `ARCHITECTURE.md`:

- FlowMind does not dispatch workers.
- Orchestration does not mutate policy.
- Graph does not schedule.
- Event Bus connects lifecycle-significant boundaries through canonical `LevEvent`.

## Execution and surfaces

Current docs also name:

- `core/exec/**` — execution SDK.
- `core/poly/**` — binder/router/control-surface generation.
- `core/daemon/**` — daemon/process runtime.
- `core/ui/**` — UI renderers / abstract UI layer.
- `AgentPing` — default human-loop surface system.
- `AgentLease` — scoped permission/accountability concept; needs implementation-status packet before stronger claims.

## Kernel constraints

Repo docs list five kernel constraints:

| Lev constraint | Safe current meaning |
|---|---|
| C1 Finitude | Plans and runs are bounded; no infinite exploration. |
| C2 Non-commutation | Order matters; dependencies and execution order are explicit. |
| C3 Nominalized Reality | Only named and validated artifacts are real to the runtime. |
| C4 Ratchet | State transitions tighten; rollback needs explicit compensation. |
| C5 Locality | Scope is explicit; no ambient authority. |

Wiki bridge maps C1/C2 to Josh's root constraints F01/N01 and treats C3–C5 as derived consequences unless a current repo source says otherwise.

## What exists now — first-pass support only

Observed from current docs:

- FlowMind compiler and execution surfaces exist.
- `@lev-os/exec` exists as execution SDK.
- Docs claim 60+ CLI commands across multiple modules.
- Root package exposes `lev` at `core/poly/bin/lev`.
- Workspace includes `core/*`, `packages/*`, `plugins/*`, `tooling/*`, `apps/*`, and selected `context/schema` packages.
- Current docs admit gaps: universal context graph not fully landed, enterprise readiness not reached, architecture ahead of some implementation.

This page has not yet verified all tests or command counts. Treat these as doc-observed claims until Packet 2/implementation reads verify them.

## What Leviathan could become

From North Star / roadmap language, the intended direction is:

- universal context graph;
- conversational dispatcher rather than direct executor;
- context engineering instead of chat-history stuffing;
- agents that earn autonomy through leases and successful execution;
- surfaces that match decision weight;
- memory that decays, strengthens, and prunes;
- constraints as declarations evaluated by the system itself;
- open-source runtime with enterprise governance layer.

## Open questions that matter

1. Which of the five kernel constraints are actually enforced in current code, versus described in docs?
2. Which AgentLease / permission concepts are implemented, partial, planned, or only product language?
3. What is the current status of FlowMind system declarations as kernel-level programs?
4. How much of the universal graph is live code versus roadmap/design?
5. Which chat/transcript claims reflect Josh's root contribution, JP's architecture intent, or assistant elaboration?
6. Where does Leviathan's runtime boundary differ from Hermes/Wizard and Codex Ratchet?

## Working answer for Josh

At this early pass, the most honest answer is:

```text
Leviathan is a governed agent runtime that tries to turn human intent into constrained, auditable, multi-surface action. It borrows your root constraint logic most visibly in finitude, non-commutation, nominalized reality, ratchet behavior, and locality/scope. It is not finished; the docs say the foundation is real while graph, enterprise readiness, protocol coverage, and hardening are still open.
```
