---
title: Packet 2 Runtime Map Receipt
date: 2026-06-17
packet: 2
status: receipt
claim_ceiling: historical Packet 2 receipt for local-checkout runtime map; not current upstream source truth; not runtime proof
owned_by: background-packet-2
---

# Packet 2 Runtime Map Receipt — 2026-06-17

> Supersession note, 2026-06-18: this receipt preserves the original Packet 2 local-checkout pass. Its conflict-marker and dirty-checkout blockers are historical after the clean snapshot audit at `c90ec8499c83db3d17f6132ec734698a8de2dbce`; see [[projects/leviathan-current/deep-audit-current-snapshot-2026-06-18]].

## Work completed

Created the six Packet 2 runtime/module map pages for the Leviathan current wiki:

1. `/Users/joshuaeisenhart/wiki/projects/leviathan-current/flowmind-control-plane.md`
2. `/Users/joshuaeisenhart/wiki/projects/leviathan-current/graph-state-knowledge-plane.md`
3. `/Users/joshuaeisenhart/wiki/projects/leviathan-current/event-bus-causality-plane.md`
4. `/Users/joshuaeisenhart/wiki/projects/leviathan-current/orchestration-execution-plane.md`
5. `/Users/joshuaeisenhart/wiki/projects/leviathan-current/exec-poly-daemon-boundary.md`
6. `/Users/joshuaeisenhart/wiki/projects/leviathan-current/plugin-ownership-map.md`

This receipt was also created:

7. `/Users/joshuaeisenhart/wiki/projects/leviathan-current/packet-2-runtime-map-receipt-2026-06-17.md`

## Source coverage

### Wiki project sources read first

- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/read-first.md`
- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/README.md`
- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/bounded-ingestion-plan.md`
- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/runtime-module-map-start.md`
- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/flowmind-control-plane-start.md`
- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/event-graph-orchestration-start.md`

### Repo authority docs read

- `/Users/joshuaeisenhart/GitHub/leviathan/docs/ARCHITECTURE.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/specs/README.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-flowmind.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-orchestration.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-graph.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-event-architecture.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-event-bus.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-exec.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-poly.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-daemon.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-domain.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/specs/spec-graph-adapters.md`

### Core source files read

FlowMind:

- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/schema.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/compiler.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/executor.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/session.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/run.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/router.policy.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/kernel/index.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/kernel/system-flowmind-loader.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/kernel/system-flowmind-executor.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/kernel/actor-kernel.ts`

Graph:

- `/Users/joshuaeisenhart/GitHub/leviathan/core/graph/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/graph/src/index.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/graph/src/compositor.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/graph/src/bridge/event-adapter.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/graph/src/events/jsonl-store.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/graph/src/context/projector.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/graph/src/adapters/memory.ts`

Event Bus:

- `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/src/index.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/src/events/event-bus.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/src/events/jsonl-persistence.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/src/runtime/queue.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/src/runtime/tool-call-checkpointer.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/src/bridge/event-action-bridge.ts`

Orchestration:

- `/Users/joshuaeisenhart/GitHub/leviathan/core/orchestration/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/orchestration/src/index.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/orchestration/src/types.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/orchestration/src/graph/dag.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/orchestration/src/graph/scheduler.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/orchestration/src/loop/iterative-runner.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/orchestration/src/queue/durable-task-queue.ts`

Exec / Poly / Daemon:

- `/Users/joshuaeisenhart/GitHub/leviathan/core/exec/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/exec/src/index.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/exec/src/types.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/exec/src/client.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/exec/src/adapters/cli.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/exec/src/adapters/mcp.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/exec/src/adapters/poly.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/poly/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/poly/src/sdk/index.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/poly/src/extension-registry.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/poly/src/registry-validator.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/poly/src/surfaces/cli/index.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/poly/src/surfaces/mcp/tools.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/daemon/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/daemon/src/index.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/daemon/src/core.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/daemon/src/supervisor.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/daemon/src/worker-pool.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/daemon/src/plugin-manifest.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/daemon/src/orchestrator-integration.ts`

### Inventory and manifest/config sources

- Enumerated `*.ts` files under:
  - `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src` — 95 observed matches.
  - `/Users/joshuaeisenhart/GitHub/leviathan/core/orchestration/src` — 75 observed matches.
  - `/Users/joshuaeisenhart/GitHub/leviathan/core/graph/src` — 29 observed matches.
  - `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/src` — 50 observed matches.
  - `/Users/joshuaeisenhart/GitHub/leviathan/core/exec/src` — 15 observed matches.
  - `/Users/joshuaeisenhart/GitHub/leviathan/core/daemon/src` — 50 observed matches.
  - `/Users/joshuaeisenhart/GitHub/leviathan/core/poly/src` — 122 observed matches.
- Enumerated 24 plugin `package.json` files and 24 plugin `config.yaml` files under `/Users/joshuaeisenhart/GitHub/leviathan/plugins`.
- Parsed/summarized all 24 plugin manifests/configs for names, namespaces, `ships-with`, `poly`, `flowmind`, `daemon`, activation, and MCP declarations.

## Blockers and cautions preserved

- Unresolved conflict markers were observed in active source, especially:
  - `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/src/index.ts`
  - `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/src/events/scm.ts`
  - `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/src/bridge/index.ts`
  - `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/src/context/pr.ts`
  - plus additional conflict markers in `core/build/**` and Rust TUI crates returned by the scan.
- No runtime health claim is made for Event Bus or any cross-plane path depending on Event Bus.
- No tests, builds, or typechecks were run for the Leviathan repo in this packet.
- The Leviathan repo was not modified.
- Only owned markdown files under `/Users/joshuaeisenhart/wiki/projects/leviathan-current` were written.
- No secrets were copied into the wiki pages. If future reads expose credentials, they should be redacted as `[REDACTED]`.

## Claim-labeling approach

Each Packet 2 page labels major claims with support tags:

- **[observed file]** — directly grounded in a source file read or a file inventory command.
- **[inferred from package/code]** — inferred from package metadata/source boundaries read.
- **[inferred from docs]** — grounded in architecture/spec docs read.
- **[roadmap/design intent]** — design/target-state wording from docs, not asserted as runtime-verified.
- **[open]** — unresolved or requiring follow-up.
- **[not checked]** — deliberately not tested/exhaustively read in this packet.

## Verification performed

After writing, the starts of all seven owned output files were re-read with `read_file`.

Wiki probe command run:

```bash
python3 /Users/joshuaeisenhart/wiki/tools/wiki_probe.py --wiki-root /Users/joshuaeisenhart/wiki --output /tmp/leviathan-packet2-background-wiki-probe.json
```

Probe result read from `/tmp/leviathan-packet2-background-wiki-probe.json`:

```json
{
  "page_count": 440,
  "index_header_count": 440,
  "indexed_link_count": 529,
  "missing_pages": [],
  "orphans": [],
  "broken_links": [],
  "stubs": [],
  "malformed_wikilinks": [],
  "stale_namespace_wikilinks": []
}
```

## Recommended next packet

Packet 3 should resolve or route around the known source-health blockers and validate runtime wiring:

1. Conflict-marker resolution/inventory packet for `core/event-bus/**`, `core/build/**`, and affected crates. Do not claim runtime health until clean.
2. Event Bus contract smoke after cleanup: publish/subscribe, JSONL persistence, replay/checkpoint, bridge export resolution.
3. Cross-plane smoke: FlowMind session -> orchestration iterative runner -> exec/daemon/plugin adapter -> event emission -> graph projection.
4. Plugin registry validation: confirm all 24 plugin manifests/configs are accepted by Poly/Daemon validators and handler paths exist.
