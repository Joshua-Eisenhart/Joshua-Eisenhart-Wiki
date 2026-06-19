---
title: What Is Leviathan
created: 2026-06-17
updated: 2026-06-19
type: explanatory-wiki-page
status: current-source-reader
source_repo: lev-os/leviathan
source_snapshot: b7bca2cdbed5862743395f7c0330e7d640132764
claim_ceiling: current source-doc and package-surface orientation; not build proof; not maintainer acceptance; not release certification
sources:
  - https://github.com/lev-os/leviathan
  - https://raw.githubusercontent.com/lev-os/leviathan/b7bca2cdbed5862743395f7c0330e7d640132764/README.md
  - https://raw.githubusercontent.com/lev-os/leviathan/b7bca2cdbed5862743395f7c0330e7d640132764/docs/README.md
  - https://raw.githubusercontent.com/lev-os/leviathan/b7bca2cdbed5862743395f7c0330e7d640132764/docs/ARCHITECTURE.md
  - https://raw.githubusercontent.com/lev-os/leviathan/b7bca2cdbed5862743395f7c0330e7d640132764/docs/ROADMAP.md
  - https://raw.githubusercontent.com/lev-os/leviathan/b7bca2cdbed5862743395f7c0330e7d640132764/mvp.md
---

# What Is Leviathan?

Leviathan / Lev is an open runtime for agent-human systems.

It is not only a chat UI, not only a prompt wrapper, and not only a docs stack. The current repo frames Lev as a runtime where agents act through explicit surfaces, under policy, with context/state, event receipts, execution boundaries, and human-loop product surfaces.

Plain version:

```text
Lev tries to move agents from "talking in chat" to "acting through governed runtime surfaces."
```

## Canonical Runtime Shape

Use the four-plane technical model for wiki pages:

| Plane | Role | Current source basis |
|---|---|---|
| FlowMind | Control and policy plane: declarations, constraints, compilation, runtime policy. | `docs/ARCHITECTURE.md`, `core/flowmind/package.json` |
| Orchestration | Execution strategy plane: DAG scheduling, worker coordination, loops, queues. | `docs/ARCHITECTURE.md`, `core/orchestration/package.json` |
| Graph / Context Graph | State and knowledge plane: entity memory, traversal, lineage, projections. | `docs/ARCHITECTURE.md`, `core/context-graph/package.json` |
| Event Bus | Causality spine: canonical `LevEvent` transport, replay, recovery, receipt trail. | `docs/ARCHITECTURE.md`, `core/event-bus/package.json` |

The root README still introduces a simplified three-plane view: FlowMind, Graph, Event Bus. Treat that as public shorthand. For technical ownership, use the four-plane boundary in [[projects/leviathan-current/architecture-planes-and-ownership]].

## Adjacent Runtime Owners

- Exec owns the execution SDK and provider dispatch boundary.
- Poly owns registry/binder/control-surface projection such as CLI, MCP, HTTP, gRPC, and SDK surfaces.
- Daemon owns long-running process supervision and worker/process lifecycle.
- AgentPing is the default human-loop surface direction, not the runtime kernel itself.
- AgentLease is a scoped-authority and accountability concept whose product/runtime proof still needs exact source and test separation.

## Current Status In One Sentence

Lev is a pre-release, source-visible agent-human runtime with real architecture and many implemented surfaces, but its proof state must be treated as split until current commands reconcile `docs/ROADMAP.md`, `mvp.md`, and fresh test results.

## What Makes It Different

Lev's distinctive bet is that durable agent work belongs in runtime structure, not only in prompts:

- context graph instead of chat-history stuffing;
- policy and leases instead of ambient permission;
- event receipts instead of vibes;
- explicit execution surfaces instead of chat-only interaction;
- human-loop surfaces instead of invisible automation;
- provider/runtime breadth instead of one-vendor lock-in.

## What This Page Does Not Prove

This page did not run `pnpm install`, build, typecheck, package tests, Pentagon gates, or security scans. It reports a current source read at `b7bca2cdbed5862743395f7c0330e7d640132764` plus earlier wiki proof packets. Use [[projects/leviathan-current/proof-backed-status-dashboard]] for current proof routing.
