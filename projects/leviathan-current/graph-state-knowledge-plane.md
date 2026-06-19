---
title: Graph / Context Graph State Knowledge Plane
created: 2026-06-17
updated: 2026-06-19
type: runtime-plane-map
status: current-source-correction
source_repo: lev-os/leviathan
source_snapshot: b7bca2cdbed5862743395f7c0330e7d640132764
claim_ceiling: source/package map for the state and knowledge plane; not full adapter test proof; not runtime health proof
sources:
  - https://raw.githubusercontent.com/lev-os/leviathan/b7bca2cdbed5862743395f7c0330e7d640132764/docs/ARCHITECTURE.md
  - https://raw.githubusercontent.com/lev-os/leviathan/b7bca2cdbed5862743395f7c0330e7d640132764/core/context-graph/package.json
---

# Graph / Context Graph State Knowledge Plane

## Current Correction

Older wiki pages described the implementation package as `core/graph/**` / `@lev-os/graph`. A fresh source read on 2026-06-19 found:

```text
core/graph/package.json: missing
core/context-graph/package.json: present
package name: @lev-os/context-graph
```

Use "Graph" for the architecture plane and `core/context-graph/**` for current implementation path claims.

## Boundary Summary

The Graph / Context Graph plane owns state and knowledge behavior:

- entity memory and lifecycle observation;
- traversal, lineage, and projections;
- context graph compositor behavior;
- adapters, schemas, validators, views, pairing, dashboard, handlers, and MCP-facing surfaces exposed by `@lev-os/context-graph`;
- graph-to-event relationships where lifecycle changes must be mirrored into the event/proof trail.

It does not own worker scheduling, retry logic, or process dispatch. Those remain Orchestration and Daemon concerns.

## Current Package Surface

Observed from `core/context-graph/package.json` at `b7bca2cd`:

- `@lev-os/context-graph`
- exports `.`
- exports `./views`
- exports `./adapters`
- exports `./events`
- exports `./schemas`
- exports `./validators`
- exports `./pairing`
- exports `./dashboard`
- exports `./handlers`
- exports `./surfaces/mcp`

Dependencies include `@lev-os/config`, `@lev-os/domain`, `@lev-os/graph-algorithms`, `@lev-os/lifecycle`, and `@lev-os/uri`.

## Cross-Plane Relationships

| To | Relationship |
|---|---|
| FlowMind | Supplies context and graph-shaped targets, while FlowMind owns control/policy. |
| Orchestration | Provides state and projections to execution strategy; does not schedule itself. |
| Event Bus | Mirrors lifecycle-significant changes into canonical event/receipt trails. |
| Poly/MCP | Exposes selected context-graph surfaces, including MCP-facing exports. |

## Open Verification

This page did not run `@lev-os/context-graph` tests, adapter tests, build, typecheck, or MCP smoke. Treat package exports as observed source/package existence, not runtime proof.
