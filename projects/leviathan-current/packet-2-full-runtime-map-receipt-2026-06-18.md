---
title: Packet 2 Full Runtime Map Receipt — 2026-06-18
created: 2026-06-18
updated: 2026-06-18
type: receipt
packet: 2-full-pass
status: complete
claim_ceiling: historical receipt for damaged local-checkout runtime map; not current upstream source truth; not runtime proof
repo_snapshot:
  path: /Users/joshuaeisenhart/GitHub/leviathan
  head: a661ecbf410469becd7b89c3bfc5ee215721ae34
wiki_probe:
  output: /tmp/leviathan-packet2-full-runtime-map-wiki-probe.json
  missing_pages: 0
  broken_links: 0
  orphans: 0
---

# Packet 2 Full Runtime Map Receipt — 2026-06-18

> Supersession note, 2026-06-18: this receipt preserves a full runtime-map pass over the deleted damaged local checkout at `a661ecbf...`. It remains useful as process evidence, but current upstream truth now begins at [[projects/leviathan-current/deep-audit-current-snapshot-2026-06-18]].

## Scope completed

Created two new wiki-only runtime map pages under `/Users/joshuaeisenhart/wiki/projects/leviathan-current`:

- `runtime-module-map-full-2026-06-18.md`
- `runtime-build-test-surface-map-2026-06-18.md`

This receipt records evidence, caveats, and validation for the Packet 2 full implementation/runtime map pass.

## Files created / modified

Created:

- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/runtime-module-map-full-2026-06-18.md`
- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/runtime-build-test-surface-map-2026-06-18.md`
- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/packet-2-full-runtime-map-receipt-2026-06-18.md`

No files under `/Users/joshuaeisenhart/GitHub/leviathan` were modified. The repo was treated as read-only.

## Existing wiki context read

- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/read-first.md`
- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/README.md`
- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/bounded-ingestion-plan.md`
- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/model-pressure/fusion-glm-wiki-direction-2026-06-18.md`
- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/runtime-module-map-start.md`
- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/flowmind-control-plane.md`
- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/graph-state-knowledge-plane.md`
- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/event-bus-causality-plane.md`
- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/orchestration-execution-plane.md`
- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/exec-poly-daemon-boundary.md`
- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/plugin-ownership-map.md`
- `/Users/joshuaeisenhart/wiki/projects/leviathan-current/packet-2-runtime-map-receipt-2026-06-17.md`

Fusion/GLM pressure was used only as advisory direction for breadth/claim discipline, not as implementation evidence.

## Repo paths read

Docs/workspace/build/test:

- `/Users/joshuaeisenhart/GitHub/leviathan/docs/README.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/ARCHITECTURE.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/docs/ROADMAP.md`
- `/Users/joshuaeisenhart/GitHub/leviathan/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/pnpm-workspace.yaml`
- `/Users/joshuaeisenhart/GitHub/leviathan/turbo.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/vitest.config.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/vitest.config.e2e.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/tests/e2e/real/vitest.config.real.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/tests/e2e/pipeline/vitest.config.pipeline.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/.github/workflows/validate-packages.yml`
- `/Users/joshuaeisenhart/GitHub/leviathan/.github/workflows/schema-drift.yml`
- `/Users/joshuaeisenhart/GitHub/leviathan/.github/workflows/proto-breaking.yml`
- `/Users/joshuaeisenhart/GitHub/leviathan/.github/workflows/evolve-memory-stress.yml`
- `/Users/joshuaeisenhart/GitHub/leviathan/.github/workflows/critical-path-sentinel.yml`
- `/Users/joshuaeisenhart/GitHub/leviathan/.github/workflows/audit.yml`
- `/Users/joshuaeisenhart/GitHub/leviathan/.gitmodules`

Runtime core:

- `/Users/joshuaeisenhart/GitHub/leviathan/core/domain/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/session.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/src/kernel/system-flowmind-loader.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/orchestration/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/orchestration/src/loop/iterative-runner.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/orchestration/src/graph/scheduler.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/graph/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/graph/src/compositor.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/src/index.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/src/events/event-bus.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/exec/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/exec/src/index.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/poly/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/poly/src/sdk/index.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/daemon/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/daemon/src/core.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/build/src/commands/skills.ts`

Rust/crates:

- `/Users/joshuaeisenhart/GitHub/leviathan/crates/Cargo.toml`
- `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-kernel/Cargo.toml`
- `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-kernel/src/lib.rs`
- `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-kernel/src/ratchet.rs`
- `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-domain/Cargo.toml`
- `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-events/Cargo.toml`
- `/Users/joshuaeisenhart/GitHub/leviathan/crates/levd/Cargo.toml`
- `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-tui-theme/src/lib.rs`
- `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-tui-widgets/src/attention_kanban.rs`

Plugins:

- `/Users/joshuaeisenhart/GitHub/leviathan/plugins/genui-exec-daemon/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/plugins/genui-exec-daemon/config.yaml`
- `/Users/joshuaeisenhart/GitHub/leviathan/plugins/voice/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/plugins/voice/config.yaml`
- `/Users/joshuaeisenhart/GitHub/leviathan/plugins/core-sdlc/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/plugins/core-sdlc/config.yaml`
- `/Users/joshuaeisenhart/GitHub/leviathan/plugins/graph-adapters/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/plugins/evolve-memory/package.json`

## Commands and outputs captured

### Git/repo state

Command run from `/Users/joshuaeisenhart/GitHub/leviathan`:

```bash
git rev-parse HEAD && git remote get-url origin && git status --short && git submodule status
```

Result: exit code `128` after printing HEAD/remote/dirty status and failing submodule status:

```text
a661ecbf410469becd7b89c3bfc5ee215721ae34
https://github.com/lev-os/leviathan.git
 m apps/nanoclaw
 m community/agentguard
 m community/agentping
 m community/lev-content
 D docs/vernacular.md
 M plugins/prompt-stack/vendors/jeffreysprompts.com
fatal: no submodule mapping found in .gitmodules for path 'community/clawstore-pre-reset'
```

### Toolchain availability

Command run from `/Users/joshuaeisenhart/GitHub/leviathan`:

```bash
node --version && pnpm --version && bun --version || true && cargo --version && rustc --version
```

Output:

```text
v22.22.3
10.28.2
/bin/bash: line 2: bun: command not found
cargo 1.88.0 (Homebrew)
rustc 1.88.0 (6b00bc388 2025-06-23) (Homebrew)
```

### Wiki validation

Command run:

```bash
python3 /Users/joshuaeisenhart/wiki/tools/wiki_probe.py --wiki-root /Users/joshuaeisenhart/wiki --output /tmp/leviathan-packet2-full-runtime-map-wiki-probe.json
```

Output file read from `/tmp/leviathan-packet2-full-runtime-map-wiki-probe.json`:

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

## Key findings recorded in new pages

1. **Runtime surface exists across FlowMind, Orchestration, Graph, Event Bus, Exec, Poly, Daemon, plugins, and Rust crates.** Each plane has concrete package/source files and a mapped ownership boundary.
2. **Event Bus is the main runtime-health blocker.** `core/event-bus/src/index.ts` contains unresolved conflict markers; event bus implementation file `events/event-bus.ts` exists, but package-level import health is not claimable.
3. **Build/skills and Rust TUI also contain conflict markers.** `core/build/src/commands/skills.ts`, `crates/lev-tui-theme/src/lib.rs`, and `crates/lev-tui-widgets/src/attention_kanban.rs` were read with markers present.
4. **Repo state is dirty and submodule status fails.** Git output showed modified/deleted paths and a fatal missing `.gitmodules` mapping for `community/clawstore-pre-reset`.
5. **Bun is not installed on this host.** Some packages use `bun test`; no Bun-backed test health can be assumed.
6. **CI mismatch found.** `.github/workflows/evolve-memory-stress.yml` invokes `pnpm --filter @lev-os/evolve-memory run test:stress`, while `plugins/evolve-memory/package.json` read in this pass exposes only `test` and `test:e2e`.
7. **No package health was claimed.** The build/test surface page explicitly marks every command surface as not run.

## Tests/builds not run

Explicitly not run:

- `pnpm install`
- `pnpm run build`
- `pnpm run test`
- `pnpm run typecheck`
- `pnpm run lint`
- `turbo run ...`
- `vitest`
- `bun test`
- `cargo check`
- `cargo build`
- `cargo test`
- plugin start/smoke commands
- daemon/FlowMind/Graph/Event Bus/Exec/Poly cross-plane smoke

## Acceptance checklist

- [x] Wiki-only edits.
- [x] No edits to `/Users/joshuaeisenhart/GitHub/leviathan`.
- [x] Exact repo paths read cited in pages/receipt.
- [x] FlowMind, Orchestration, Graph, Event Bus, Exec/Poly/Daemon, plugins, and test/build surfaces covered.
- [x] Observed implementation vs docs/contract intent distinguished.
- [x] Broken/conflict markers documented as blockers, not truth.
- [x] Tests/builds not run explicitly stated.
- [x] Open gaps listed.
- [x] Fusion/GLM pressure mentioned only as advisory.
- [x] Wiki probe passed with no missing pages, broken links, or orphans.
