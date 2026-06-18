---
title: Runtime Build/Test Surface Map — 2026-06-18
created: 2026-06-18
updated: 2026-06-18
type: build-test-surface-map
packet: 2-full-pass
status: current snapshot with tests not run
claim_ceiling: command/manifests/config/workflow map only; no package health claims
repo_snapshot:
  path: /Users/joshuaeisenhart/GitHub/leviathan
  head: a661ecbf410469becd7b89c3bfc5ee215721ae34
---

# Runtime Build/Test Surface Map — 2026-06-18

> Supersession note, 2026-06-18: this page preserves build/test surfaces and local-incident evidence from the deleted damaged checkout. Its conflict-marker findings are not current upstream truth after the clean snapshot audit at `c90ec8499c83db3d17f6132ec734698a8de2dbce`; see [[projects/leviathan-current/deep-audit-current-snapshot-2026-06-18]]. Keep the build/test command inventory, but do not treat the listed conflict markers as current blockers unless a fresh scan re-finds them. The current source also changes some package/path details, so use [[projects/leviathan-current/repo-current-vs-wiki-drift-audit-2026-06-18]] before citing this page.

## Claim discipline

This page maps build/test/runtime-health surfaces. It does **not** claim that any package builds, typechecks, or passes tests. No `pnpm test`, `pnpm build`, `turbo`, `vitest`, `bun test`, or `cargo test` command was run in this wiki pass. **[tests not run]**

Support labels:

- **[observed file]** — read in a manifest/config/workflow/source file.
- **[command output]** — observed from a command run during this pass.
- **[broken/conflict marker]** — source contains unresolved conflict markers or a command failed.
- **[tests not run]** — test/build/typecheck command exists or test files exist, but was not executed here.
- **[open gap]** — needs follow-up verification.

## Commands run in this pass

### Repo state

Command:

```bash
git rev-parse HEAD && git remote get-url origin && git status --short && git submodule status
```

Output summary:

```text
a661ecbf410469becd7b89c3bfc5ee215721ae34
https://github.com/lev-os/leviathan.git
 m apps/nanoclaw
 m community/agentguard
 m community/agentping
 m community/lev-content
 D docs/vernacular.md
 M plugins/prompt-stack/vendors/jeffreysprompts.com
...
fatal: no submodule mapping found in .gitmodules for path 'community/clawstore-pre-reset'
```

Exit code: `128`. **[command output] / [broken/conflict marker]**

Interpretation: current repo is dirty and submodule inventory is blocked by a `.gitmodules`/submodule-state mismatch. Do not use this state as a clean release/runtime-health baseline. **[open gap]**

### Tool availability

Command:

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

Interpretation: Node, pnpm, Cargo, and rustc are present on this host; `bun` is not present. Because several package scripts use `bun test`, those scripts cannot be assumed runnable on this host without installing Bun or changing command route. **[command output]**

### Conflict-marker scan

A Python read-only scan over `/Users/joshuaeisenhart/GitHub/leviathan`, excluding `.git`, `node_modules`, `target`, `dist`, `.turbo`, and `.next`, observed `56` files containing lines starting `<<<<<<<`, `=======`, or `>>>>>>>`. Active runtime/build blockers include Event Bus, Build skills, and Rust TUI files listed below. **[command output] / [broken/conflict marker]**

## Sources read

Build/test/workspace sources read:

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
- `/Users/joshuaeisenhart/GitHub/leviathan/crates/Cargo.toml`
- `/Users/joshuaeisenhart/GitHub/leviathan/.gitmodules`

Core manifests read:

- `/Users/joshuaeisenhart/GitHub/leviathan/core/domain/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/flowmind/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/orchestration/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/graph/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/exec/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/poly/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/daemon/package.json`

Selected plugin manifests/configs read:

- `/Users/joshuaeisenhart/GitHub/leviathan/plugins/genui-exec-daemon/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/plugins/genui-exec-daemon/config.yaml`
- `/Users/joshuaeisenhart/GitHub/leviathan/plugins/voice/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/plugins/voice/config.yaml`
- `/Users/joshuaeisenhart/GitHub/leviathan/plugins/core-sdlc/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/plugins/core-sdlc/config.yaml`
- `/Users/joshuaeisenhart/GitHub/leviathan/plugins/graph-adapters/package.json`
- `/Users/joshuaeisenhart/GitHub/leviathan/plugins/evolve-memory/package.json`

Conflict-marker files read:

- `/Users/joshuaeisenhart/GitHub/leviathan/core/event-bus/src/index.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/build/src/commands/skills.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-tui-theme/src/lib.rs`
- `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-tui-widgets/src/attention_kanban.rs`

## Workspace and package manager surfaces

### Root package

`/Users/joshuaeisenhart/GitHub/leviathan/package.json` defines private root package `@lev-os/root`, `type: module`, root binary `lev -> ./core/poly/bin/lev`, workspaces `core/*`, `packages/*`, `plugins/*`, `tooling/*`, Node engine `>=18.0.0`, pnpm engine `>=8.0.0`, and package manager `pnpm@10.28.2`. **[observed file]**

Root high-level scripts include:

| Script | Command surface | Notes |
|---|---|---|
| `build` | `pnpm run build:turbo && pnpm run build:binaries` | Full build aggregator. **Not run.** |
| `build:turbo` | `pnpm run build:poly && pnpm -r build` | Runs registry build then recursive workspace builds. **Not run.** |
| `build:poly` | `cd core/poly && pnpm run build:registry` | Poly registry generation. **Not run.** |
| `test` | `pnpm run test:all` | Full test aggregator. **Not run.** |
| `test:all` | guard legacy paths → guard FlowMind scheduler → guard runtime routing → plugins → vitest → exec integration → prompt-stack → CLI surface → e2e | Broad test chain. **Not run.** |
| `typecheck` | `turbo run typecheck` | Turbo typecheck. **Not run.** |
| `lint` | `turbo run lint` | Turbo lint. **Not run.** |
| `validate` | `turbo run validate` | Turbo validation. **Not run.** |
| `audit` | `pnpm audit --audit-level=high` | Security audit command. **Not run.** |

### pnpm workspace

`/Users/joshuaeisenhart/GitHub/leviathan/pnpm-workspace.yaml` includes `core/*`, `packages/*`, `apps/*`, `apps/*/web`, desktop internal packages, `tooling/*`, `plugins/*`, and `context/schema`; excludes selected problematic/archive/non-package paths including `apps/universal-preview`, `apps/agentping/packages/*`, `apps/max`, archive dirs, `core/cli`, `core/schemas`, and `tooling/agentctl`. **[observed file]**

### Turbo

`/Users/joshuaeisenhart/GitHub/leviathan/turbo.json` defines tasks for `build`, `dev`, `format`, `lint`, `typecheck`, `validate`, docs tasks, and clean/push/studio/UI tasks. Build/typecheck outputs target `.cache/tsbuildinfo.json` and `dist/**`; `dev` and `studio` are persistent/non-cache. **[observed file]**

No `turbo` command was run. **[tests not run]**

## Core package scripts

Read from manifests and/or Python manifest inventory. No script below was executed during this pass. **[tests not run]**

| Package | Path | Scripts observed | Build/test caveat |
|---|---|---|---|
| `@lev-os/domain` | `core/domain/package.json` | `test: npx tsx --test tests/*.test.js && vitest run`, `typecheck: tsc --noEmit` | Not run. |
| `@lev-os/flowmind` | `core/flowmind/package.json` | `build: tsc`, `test: vitest run`, `lint: eslint src`, `typecheck: tsc --noEmit` | Not run. |
| `@lev-os/orchestration` | `core/orchestration/package.json` | `build: tsc`, `test: vitest run`, `typecheck: tsc --noEmit` | Not run. |
| `@lev-os/graph` | `core/graph/package.json` | `build: tsc`, `test: bun test`, `typecheck: tsc --noEmit` | Host command output says `bun: command not found`; graph test script is not runnable on this host without Bun. |
| `@lev-os/event-bus` | `core/event-bus/package.json` | `build: tsc`, `test: vitest`, `test:coverage: vitest --coverage`, `lint: eslint src`, `typecheck: tsc --noEmit` | Not run; package barrel has conflict markers. |
| `@lev-os/exec` | `core/exec/package.json` | `build: tsc`, `test: vitest run`, `typecheck: tsc --noEmit` | Not run; imports Event Bus event subpath. |
| `@lev-os/poly` | `core/poly/package.json` | `build: npm run build:tsc && npm run build:registry`, `build:registry`, `build:manifest`, `typecheck`, `test: node tests/registry-builder.test.js`, `test:gates: vitest run src/__tests__/gates/` | Not run. |
| `@lev-os/daemon` | `core/daemon/package.json` | `build: tsc`, `test: vitest run`, `typecheck: tsc --noEmit` | Not run; depends on Event Bus. |

## Test file inventory command output

Python inventory counted test-like files by package area. This is file existence only, not pass/fail. **[command output]**

| Area | Test-like files counted | Notes |
|---|---:|---|
| `core/flowmind` | 39 | `*.test.ts` only in count. |
| `core/orchestration` | 32 | `*.test.ts` only in count. |
| `core/graph` | 9 | `*.test.ts`; package script uses `bun test`. |
| `core/event-bus` | 19 | `*.test.ts`; package barrel conflict blocks health claims. |
| `core/exec` | 6 | `*.test.ts`. |
| `core/poly` | 70 | 61 `*.test.ts` + 9 `*.test.js`. |
| `core/daemon` | 28 | `*.test.ts`. |
| `plugins` | 84 | 79 `*.test.ts` + 5 `*.test.js`. |
| `tests` | 56 | 39 `*.test.ts`, 7 `*.test.js`, 6 `*.spec.ts`, 4 `*.test.sh`. |
| `crates` | 9 | TypeScript test files under crate-related SDK/examples; Rust `#[test]` functions not counted here. |

Additional file searches observed examples of test surfaces under:

- `/Users/joshuaeisenhart/GitHub/leviathan/core/poly/src/__tests__/...`
- `/Users/joshuaeisenhart/GitHub/leviathan/core/orchestration/src/__tests__/...`
- `/Users/joshuaeisenhart/GitHub/leviathan/plugins/core-platforms/tests/adapters/...`
- `/Users/joshuaeisenhart/GitHub/leviathan/tests/e2e/real/...`
- `/Users/joshuaeisenhart/GitHub/leviathan/tests/e2e/pipeline/...`

No test result is implied by these counts. **[tests not run]**

## Vitest surfaces

Read root and e2e configs:

- `/Users/joshuaeisenhart/GitHub/leviathan/vitest.config.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/vitest.config.e2e.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/tests/e2e/real/vitest.config.real.ts`
- `/Users/joshuaeisenhart/GitHub/leviathan/tests/e2e/pipeline/vitest.config.pipeline.ts`

Observed:

- Root vitest includes `tests/**/*.test.ts`, aliases `@lev-os/event-bus` to `core/event-bus/src/index.ts`, and aliases `@lev-os/event-bus/events` to `core/event-bus/src/events/index.ts`. Because `core/event-bus/src/index.ts` has conflict markers, root tests importing the package alias are blocked until conflicts resolve. **[observed file] / [broken/conflict marker]**
- E2E hooks config includes `tests/e2e/hooks/**/*.test.ts` and `tests/e2e/hooks/**/*.e2e.test.ts`, with sequential execution and `30s` test timeout. **[observed file]**
- Real E2E config includes `tests/e2e/real/**/*.test.ts`, aliases core packages, sets `120s` timeout, sequential execution, and JUnit output at `reports/e2e/real-junit.xml`. **[observed file]**
- Pipeline E2E config includes `tests/e2e/pipeline/**/*.test.ts`, aliases core packages including Event Bus, Exec, Daemon, Poly adapters, UI renderers, sets `60s` timeout, sequential execution, and JUnit output at `reports/e2e/pipeline-junit.xml`. **[observed file]**

## CI/workflow surfaces

Read workflows:

| Workflow | Path | Observed behavior | Caveat |
|---|---|---|---|
| Package Schema Validation | `.github/workflows/validate-packages.yml` | On PR/push path filters for core/plugin package manifests and validator; installs `@lev-os/package-validator...`; runs `pnpm run validate:packages --report validation-report.json`. | Not run locally. |
| Schema Drift Detection | `.github/workflows/schema-drift.yml` | Watches Rust domain/reactive/TUI and TS event/domain paths; initializes `crates/lev-agentfs`; runs `cargo test -p lev-domain -p lev-tui-core`; runs `make check-schema`. | Not run locally; Rust TUI conflict markers exist in current tree. |
| Proto Breaking Change Detection | `.github/workflows/proto-breaking.yml` | Runs `buf lint`, PR breaking check, `buf generate`, then checks generated stubs for uncommitted changes. | Not run locally. |
| Evolve Memory Stress | `.github/workflows/evolve-memory-stress.yml` | On evolve-memory/orchestration/exec/flowmind changes, installs pnpm and runs `pnpm --filter @lev-os/evolve-memory run test:stress`. | Read `plugins/evolve-memory/package.json` exposes `test` and `test:e2e`, not `test:stress`; workflow/package mismatch is an open CI issue. |
| Critical Path Sentinel | `.github/workflows/critical-path-sentinel.yml` | Manual dispatch. Blocking architecture sync via `node tooling/scripts/check-architecture-sync.js`; non-blocking sentinel report; blocking regression check. | Not run locally. |
| Dependency Audit | `.github/workflows/audit.yml` | Push/PR/schedule; installs pnpm, runs `bash tooling/scripts/audit-check.sh`, generates SBOM. | Not run locally. |

## Rust/Cargo build and test surface

`/Users/joshuaeisenhart/GitHub/leviathan/crates/Cargo.toml` defines a Rust workspace with many members, including runtime/kernel/event/UI/daemon crates. **[observed file]**

Selected Rust manifests read:

- `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-kernel/Cargo.toml` — library crate, optional NAPI feature, depends on `lev-core`, `lev-policy`, `lev-declaration`, `lev-events`, `lev-audit`, serde, chrono, sha2, tokio. **[observed file]**
- `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-domain/Cargo.toml` — canonical domain types and schema generation binary. **[observed file]**
- `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-events/Cargo.toml` — event spine/schema/bus/JSONL persistence crate. **[observed file]**
- `/Users/joshuaeisenhart/GitHub/leviathan/crates/levd/Cargo.toml` — daemon binary crate. **[observed file]**

Command output confirms `cargo 1.88.0` and `rustc 1.88.0` are installed. **[command output]**

No `cargo check`, `cargo test`, `cargo build`, or Rust workspace command was run. **[tests not run]**

Rust blockers read:

- `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-tui-theme/src/lib.rs` contains conflict markers around `AttentionColors` derive. **[broken/conflict marker]**
- `/Users/joshuaeisenhart/GitHub/leviathan/crates/lev-tui-widgets/src/attention_kanban.rs` contains conflict markers in widget methods and `buf.set_string` calls. **[broken/conflict marker]**

Because `crates/Cargo.toml` includes `lev-tui-theme` and `lev-tui-widgets`, Rust workspace health cannot be claimed until conflicts resolve or a scoped command proves unaffected packages. **[open gap]**

## Lockfile/package-surface inventory

Python inventory observed these relevant root/active lockfiles:

- `/Users/joshuaeisenhart/GitHub/leviathan/pnpm-lock.yaml`
- `/Users/joshuaeisenhart/GitHub/leviathan/crates/Cargo.lock`
- Additional package-local lockfiles under `tooling/doc-validator`, apps, workshop, `crates/lev-agentfs`, `core/poly/sdk/*`, `core/poly/tests/cross-language`, `tests/e2e/real/01-crosslang-grpc/rust`, `packages/poly-test-rs`, and others.

This is an inventory only; lockfile freshness was not verified. **[command output] / [tests not run]**

## Plugin build/test surface

Manifest inventory over `plugins/*/package.json` observed 24 plugin packages with matching `config.yaml` files. Examples and caveats:

| Plugin | Scripts observed | Caveat |
|---|---|---|
| `auth-sniffer` | build/dev/lint/skills compile+emit/test/typecheck | Not run. |
| `beads` | build/clean/test/typecheck | Not run. |
| `browser-cascade` | build/dev/lint/test/typecheck | Not run. |
| `core-bench` | build/test/test:watch/typecheck | Not run. |
| `core-gameai` | build/test/test:watch/typecheck | Not run. |
| `core-platforms` | clean/test/typecheck | Not run. |
| `core-scheduling` | test/typecheck | Not run. |
| `core-sdlc` | build/test/test:watch/typecheck | Not run. |
| `core-workshop` | `dev`, `test: echo 'test framework (plugins/testing) deleted — needs vitest rewrite'` | Script itself says test rewrite needed. |
| `deploy` | build/clean/test/typecheck | Not run. |
| `evolve-memory` | test, test:e2e | Does not expose `test:stress` despite CI workflow referencing it. |
| `genui-exec-daemon` | build/clean/start/test/typecheck | Not run. |
| `graph-adapters` | build/clean/typecheck | No test script observed. |
| `notion` | cargo build/fmt/run/test through `crates/lev-notionctl` | Not run. |
| `vision` | dev, `test: echo 'no tests yet'`, `test:watch: echo 'no tests yet'` | Script says no tests yet. |
| `wiggum-marketer`, `writer` | build/test no-op echo | No health implied. |

No plugin commands were executed. **[tests not run]**

## Active blockers that affect build/test/runtime claims

1. **Conflict markers in package imports/build surfaces.** Root vitest aliases `@lev-os/event-bus` to a conflicted file; Event Bus barrel conflict blocks package-level import/typecheck claims. **[broken/conflict marker]**
2. **Build package conflict markers.** `core/build/src/commands/skills.ts` and related skill-orchestrator/test files contain conflict markers; root scripts depend on `core/build` test runner and build tooling. **[broken/conflict marker]**
3. **Rust TUI conflict markers.** `lev-tui-theme` and `lev-tui-widgets` files contain conflict markers and are members of `crates/Cargo.toml`. **[broken/conflict marker]**
4. **Submodule status failure.** `git submodule status` exited `128` due to missing `.gitmodules` mapping for `community/clawstore-pre-reset`. **[broken/conflict marker]**
5. **Bun unavailable.** Host output says `bun: command not found`, while packages such as `@lev-os/graph`, `@lev-os/config`, and `@lev-os/harness-sdk` use `bun test`. **[command output] / [open gap]**
6. **CI script mismatch.** `evolve-memory-stress.yml` calls `test:stress`; `plugins/evolve-memory/package.json` read in this pass exposes only `test` and `test:e2e`. **[observed file] / [open gap]**

## What would count as verified health later

Do not mark any of these as done until real command output exists in a later receipt:

1. Clean conflict-marker scan over active runtime/build/crate paths.
2. `git status --short` and `git submodule status` without unexpected failure, or documented scope-exclusion.
3. `pnpm install --frozen-lockfile` or equivalent dependency install health.
4. `pnpm run build:poly` and/or scoped `pnpm --filter <pkg> run build` output.
5. `pnpm --filter @lev-os/event-bus run typecheck` after conflict resolution.
6. `pnpm --filter @lev-os/flowmind run test`, `@lev-os/orchestration`, `@lev-os/exec`, `@lev-os/poly`, `@lev-os/daemon` scoped tests.
7. `bun --version` plus scoped `bun test` where package scripts require Bun, or package scripts changed/verified to not require Bun.
8. `cargo test` scoped to non-conflicted crates or workspace after Rust conflicts resolve.
9. Plugin registry validation output proving all plugin manifests/configs and handler paths are accepted.
10. Cross-plane smoke: FlowMind session → Orchestration loop → Exec/Daemon/plugin adapter → Event Bus emit/persist → Graph projection.
