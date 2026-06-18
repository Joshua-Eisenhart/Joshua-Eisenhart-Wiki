---
title: Leviathan Clean Clone Proof Audit Roadmap Vs MVP
created: 2026-06-18
updated: 2026-06-18
type: proof-audit
status: active
source_snapshot: c90ec8499c83db3d17f6132ec734698a8de2dbce
claim_ceiling: clean-clone command receipt audit; not full release readiness; not maintainer acceptance
---

# Leviathan Clean Clone Proof Audit Roadmap Vs MVP

## Bottom Line

The `docs/ROADMAP.md` vs `mvp.md` conflict is now a split verdict, not a vibe check.

The clean proof run shows real green surfaces:

- dependency install completed in a disposable clone;
- `pnpm run build:poly` completed;
- high-severity audit passed, though low/moderate vulnerabilities remain;
- `@lev-os/daemon-pentagon` exists and its package tests pass;
- the named `pentagon-sdk-poly-binding` run and gate pass after the required package builds;
- `lev events --help` and `lev triggers --help` expose the manual event/trigger CLI surfaces.

The same proof run also shows real red or blocked surfaces:

- `@lev-os/testing test` fails before assertions in this clean proof packet because Vitest cannot resolve `@lev-os/utils` built output consistently;
- default `lev pentagon run --project .` and `lev pentagon gate --project .` fail after builds with 42 `DAEMON_CODING_AGENT_MCP_ARTIFACT_MISSING` diagnostics;
- targeted `core/event-dispatch` tests fail before assertions because workspace/package imports are unresolved in this run;
- child-process `process.env` pass-through sites still exist in source and need severity classification;
- `docs/ROADMAP.md` appears stale for the exact `new Function` gate-executor claim, because the source scout did not find literal `new Function` in the current executor file.

Safe current verdict:

```text
Leviathan has real source-backed and proof-backed runtime surfaces, but the default daemon/Pentagon proof path and testing package are not green in this clean proof packet. MVP is right about the named SDK/Poly gate; ROADMAP is right that default daemon/testing proof remains blocked or red.
```

## Source Setup

| Surface | Path / value | Evidence ceiling |
|---|---|---|
| Clean source clone | `/tmp/leviathan-wiki-src-20260618` | Source audit only; kept clean. |
| Disposable proof clone | `/tmp/leviathan-proof-src-20260618` | Command proof surface; allowed to create `node_modules` and `.lev` proof state. |
| Remote | `https://github.com/lev-os/leviathan.git` | Current upstream source. |
| Commit | `c90ec8499c83db3d17f6132ec734698a8de2dbce` | Snapshot for this packet. |
| Command receipts | `/tmp/leviathan-proof-audit-command-receipts-20260618/` | Raw logs for this audit. |

The proof clone is intentionally disposable. The persistent damaged checkout at `/Users/joshuaeisenhart/GitHub/leviathan` was not reused.

## Command Results

| Check | Receipt | Exit | Verdict |
|---|---:|---:|---|
| `pnpm install --frozen-lockfile --ignore-scripts` | `01b-pnpm-install-ignore-scripts-rerun.log` | 0 | Install completed. Warnings include cyclic workspace deps and missing dist bins due `--ignore-scripts`. |
| `pnpm run build:poly` | `02-build-poly.log` | 0 | Poly registry build completed; 15 modules and 5 registry roots discovered. |
| `pnpm run audit` | `03-pnpm-run-audit.log` | 0 | High audit passed, but 8 low/moderate vulnerabilities remain. |
| `pnpm --filter @lev-os/testing test` before package builds | `04-testing-package-test.log` | 1 | Failed before tests; `@lev-os/utils` entry unresolved. |
| `pnpm --filter @lev-os/utils build` | `04a-utils-build.log` | 0 | Built `core/utils/dist`. |
| `pnpm --filter @lev-os/testing test` after utils build | `04b-testing-package-test-after-utils-build.log` | 1 | Failed before tests; Vitest/import resolution around `./case-bridge.js`. |
| `pnpm --filter @lev-os/daemon-pentagon test` | `05-daemon-pentagon-test.log` | 0 | 5 test files, 31 tests passed. |
| `pnpm exec lev pentagon --help` | `06-lev-pentagon-help.log` | 0 | CLI exposes `pentagon-sdk-poly-binding`, `daemon-run-fabric-implemented-surfaces-v1`, and `daemon-run-fabric-real-world-usage-v1`. |
| Default `lev pentagon run --project . --json` before testing build | `07-lev-pentagon-run-default.log` | 1 | Failed because `@lev-os/testing/dist/pentagon.js` was missing. |
| `pnpm --filter @lev-os/testing build` | `07a-testing-package-build.log` | 0 | Built `core/testing/dist`. |
| `pnpm --filter @lev-os/testing test` after testing build | `07b-testing-package-test-after-build.log` | 1 | Still failed before assertions on `@lev-os/utils` built-dist import resolution. |
| Default `lev pentagon run --project . --json` after builds | `08-lev-pentagon-run-default-after-testing-build.log` | 1 | Executed but failed with missing mini-app `receiptPath` / `gateProofPath` artifacts. |
| Default `lev pentagon gate --project . --json` after builds | `09-lev-pentagon-gate-default-after-testing-build.log` | 1 | `PENTAGON_GATE_FAILED`, 42 diagnostics, all grouped as `DAEMON_CODING_AGENT_MCP_ARTIFACT_MISSING`. |
| Named `lev pentagon run --suite pentagon-sdk-poly-binding --json` | `10-lev-pentagon-run-sdk-poly.log` | 0 | Named SDK/Poly run passed. |
| Named `lev pentagon gate --suite pentagon-sdk-poly-binding --json` | `11-lev-pentagon-gate-sdk-poly.log` | 0 | Named SDK/Poly gate passed with 8 required logs and 0 diagnostics. |
| Targeted `core/event-dispatch` tests | `12-event-dispatch-targeted-tests.log` | 1 | Failed before tests; unresolved `@lev-os/daemon` and `@lev-os/config/xdg-paths` imports. |
| `pnpm exec lev events --help` | `13-lev-events-help.log` | 0 | Shows `lev events tail [--source <events.jsonl>] [--limit <n>] [--json]`. |
| `pnpm exec lev triggers --help` | `14-lev-triggers-help.log` | 0 | Shows `project` and `dispatch` trigger commands with dry-run / exec-dry-run flags. |

Do not count `04c-testing-vitest-force-after-utils-build.log` as useful proof. It failed because Vitest v4.1.5 does not support the attempted `--force` flag.

## Settled Claims

| Claim | Previous conflict | Clean proof verdict |
|---|---|---|
| High audit | `ROADMAP.md` says high audit red; `mvp.md` says scoped gate green. | High audit exits 0 in this proof run. Low/moderate vulnerabilities remain, so do not claim all security debt is gone. |
| Literal `new Function` in FlowMind gate executor | `ROADMAP.md` names it as open. | Source scout did not find literal `new Function` in current `core/flowmind/src/kernel/validation-gate-executor.ts`; roadmap wording is likely stale for that exact item. |
| Ambient child env pass-through | `ROADMAP.md` says open; `mvp.md` implies scoped security cleanup. | Source hits remain in daemon/app-runner/universal-preview paths. Severity is unclassified here. |
| `@lev-os/daemon-pentagon` package | `ROADMAP.md` says missing package / next fix. | Package exists and its tests pass in this proof run. That does not prove default daemon gate. |
| `@lev-os/testing` package health | `ROADMAP.md` says red; `mvp.md` says green. | Test command fails before assertions in clean proof run. Package can build, but test health is not green. |
| Named S5 SDK/Poly provider proof | `mvp.md` says green; `ROADMAP.md` is more pessimistic. | Named `pentagon-sdk-poly-binding` run and gate pass after builds. |
| Default daemon Run Fabric/Pentagon gate | `mvp.md` says green; `ROADMAP.md` says red/blocked. | Default run/gate fail after builds with 42 mini-app artifact diagnostics. Packet 8 narrowed the representative cause to stale absolute artifact paths from another checkout while clone-local artifacts exist. |
| Manual events CLI surface | Roadmap says manual mode works; daemon automation remains open. | Help commands expose `events` and `triggers` surfaces. Runtime tests did not run successfully; Packet 8 narrowed the hosted-daemon blocker to unresolved `@lev-os/daemon` and `@lev-os/config/xdg-paths` import/build resolution. |

## Pentagon Split

The Pentagon evidence must stay split:

```text
@lev-os/daemon-pentagon package tests: green in this packet.
pentagon-sdk-poly-binding named run/gate: green in this packet.
default daemon Run Fabric/Pentagon run/gate: red in this packet.
```

The default gate failure is not a missing-log issue for the named SDK/Poly surface. Packet 8 narrowed the daemon mini-app artifact issue: a representative report preserved absolute `receiptPath` and `gateProofPath` values rooted at another checkout (`/Users/jean-patricksmith/digital/leviathan/...`), while clone-local mini-app artifacts such as `receipt.jsonl` and `gateproof.json` exist under `/tmp/leviathan-proof-src-20260618/.lev/infra/pentagon/runs/daemon-coding-agent-mcp/...`. The gate validates the report paths with `existsSync`, so stale absolute paths trip `DAEMON_CODING_AGENT_MCP_ARTIFACT_MISSING` with 42 diagnostics.

## Testing Package Blocker

`@lev-os/testing` can build, and direct Node import of `@lev-os/utils` from `core/testing` succeeds. Packet 8 narrowed the test blocker: `core/testing/vitest.config.ts` prefers the `bun` condition; `@lev-os/utils` exports the `bun` condition to `./src/index.ts`; that source entry imports `.js` sibling paths such as `./case-bridge.js` while the source file is `case-bridge.ts`. The package test therefore fails under Vitest before assertions with a source-entry/package-resolution problem around `./case-bridge.js`.

Treat this as a package-resolution/test-harness blocker until a narrower fix proves otherwise. It is not evidence that all testing APIs are absent.

## Event Dispatch Ceiling

The source tree and help output show real event/trigger surfaces:

```text
lev events tail [--source <events.jsonl>] [--limit <n>] [--json]
lev triggers project <events.jsonl> [--dry-run] [--json]
lev triggers dispatch <events.jsonl> [--receipt <receipt.json>] [--exec-dry-run] [--json]
```

The targeted event-dispatch test run did not reach assertions. Packet 8 narrowed the blocker: `core/event-dispatch/src/__tests__/hosted-dispatcher-daemon.test.ts` imports `@lev-os/daemon`, and `core/event-bus/src/events/jsonl-persistence.ts` imports `@lev-os/config/xdg-paths`; the targeted test environment needs those packages built or aliased before hosted-daemon proof can run. Therefore this packet can say the manual CLI surfaces exist and are callable for help, but it cannot say the proof-spine event dispatch path is freshly green.

## Read Implications

Use this page to correct the earlier `contested-doc` posture:

- `mvp.md` is right for the named SDK/Poly provider proof.
- `mvp.md` is too strong for default daemon Run Fabric/Pentagon gate and `@lev-os/testing`.
- `docs/ROADMAP.md` is right that default daemon/testing proof is not green.
- `docs/ROADMAP.md` is stale for `@lev-os/daemon-pentagon` source/package presence and likely stale for the exact `new Function` executor claim.
- Neither document should be treated as current execution truth without this command receipt layer.

## Remaining Blockers

1. Fix or explain the `@lev-os/testing` Vitest/Bun-condition source-entry mismatch around `@lev-os/utils`.
2. Rebase or relativize daemon MCP mini-app `receiptPath` and `gateProofPath` values, then rerun default Pentagon run/gate.
3. Classify child-process env pass-through sites and decide whether a shared safe-env builder is required.
4. Build or alias `@lev-os/daemon` and `@lev-os/config/xdg-paths`, then rerun event-dispatch targeted tests.
5. Patch repo docs only after Josh explicitly asks for source edits; this wiki packet is a proof/read layer, not a Leviathan repo patch.

## Receipt Paths

Raw command logs live under:

```text
/tmp/leviathan-proof-audit-command-receipts-20260618/
```

Important logs:

- `01b-pnpm-install-ignore-scripts-rerun.log`
- `02-build-poly.log`
- `03-pnpm-run-audit.log`
- `04b-testing-package-test-after-utils-build.log`
- `05-daemon-pentagon-test.log`
- `07a-testing-package-build.log`
- `07b-testing-package-test-after-build.log`
- `08-lev-pentagon-run-default-after-testing-build.log`
- `09-lev-pentagon-gate-default-after-testing-build.log`
- `10-lev-pentagon-run-sdk-poly.log`
- `11-lev-pentagon-gate-sdk-poly.log`
- `12-event-dispatch-targeted-tests.log`
- `13-lev-events-help.log`
- `14-lev-triggers-help.log`
