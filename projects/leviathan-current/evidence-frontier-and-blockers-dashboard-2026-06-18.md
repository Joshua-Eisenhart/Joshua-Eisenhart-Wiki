---
title: Leviathan Evidence Frontier And Blockers Dashboard
created: 2026-06-18
updated: 2026-06-18
type: evidence-frontier
status: active
source_snapshot: c90ec8499c83db3d17f6132ec734698a8de2dbce
claim_ceiling: current contradiction/blocker dashboard with Packet 7 proof-audit updates; not release readiness
---

# Leviathan Evidence Frontier And Blockers Dashboard

## Bottom Line

The repo is not "no content" and not "hopelessly broken" in the clean source snapshot. It is a massive pre-release runtime repo with real implemented surfaces, a serious docs/spec stack, and a current-state problem: several front-door docs disagree about what is green, red, stale, or only proposal.

Packet 7 changed the largest open item from `contested-doc` to `split-verdict`: [[projects/leviathan-current/proof-audit-roadmap-vs-mvp-2026-06-18]] now command-tests the main `docs/ROADMAP.md` vs `mvp.md` disagreement in a disposable clean proof clone.

## Confirmed In This Packet

| Claim | Current status |
|---|---|
| Remote `main` and disposable clone match | Confirmed at `c90ec8499c83db3d17f6132ec734698a8de2dbce`. |
| Disposable clone was clean | Confirmed by `git status --short`. |
| Old local checkout conflict-marker claims are superseded for upstream current truth | Confirmed by clean snapshot scan with no conflict-marker hits. |
| Specs/architecture/design/inbox authority split exists | Confirmed by `docs/README.md`; specs normative, design rationale, `_inbox` not runtime truth. |
| Four-plane runtime boundary is canonical architecture | Confirmed by `docs/ARCHITECTURE.md`: FlowMind, Orchestration, Graph, Event Bus. |
| Source tree is huge and mixed | Confirmed by counts: 42 `core` dirs, 54 `plugins` dirs, 19 `apps` dirs, 43 `crates` dirs, 429 docs Markdown files, 115 docs inbox Markdown files, 1037 archive Markdown files. |
| High audit in clean proof clone | `pnpm run audit` exited 0; 8 low/moderate vulnerabilities remain. |
| Named SDK/Poly Pentagon gate | `lev pentagon run/gate --suite pentagon-sdk-poly-binding` exited 0 after package builds. |
| Default daemon Pentagon gate | `lev pentagon run/gate --project .` failed after package builds with 42 missing mini-app artifact diagnostics. |
| `@lev-os/testing test` | Fails before assertions in the clean proof packet due Vitest/package-resolution around `@lev-os/utils` built dist. |

## Current Contradictions

### 1. `docs/ROADMAP.md` vs `mvp.md`

`docs/ROADMAP.md` has a 2026-05-17 current-position refresh that says Pentagon/Run Fabric provider proof, `@lev-os/testing`, daemon state, stale S5 projection artifacts, and security P0 burn-down are still blockers.

`mvp.md` has a 2026-05-18 validation refresh that says the named S5 SDK/Poly provider proof, default daemon Run Fabric/Pentagon gate, `@lev-os/testing`, and scoped security P0 gate are green, while always-on daemon/event automation and downstream surfaces remain unimplemented or not rerun.

Packet 6 wiki verdict was `contested-doc`. Packet 7 verdict is `split-verdict`.

Do not choose the sunnier or scarier version by vibe. Use the proof audit:

- `mvp.md` is right that the named SDK/Poly provider proof can pass.
- `mvp.md` is too strong for default daemon Run Fabric/Pentagon gate and `@lev-os/testing` package tests.
- `docs/ROADMAP.md` is right that default daemon/testing proof is not green.
- `docs/ROADMAP.md` is stale for `@lev-os/daemon-pentagon` package presence/test health, and likely stale for the exact `new Function` executor claim.

Proof page:

- [[projects/leviathan-current/proof-audit-roadmap-vs-mvp-2026-06-18]]

Fresh commands already run in Packet 7:

```bash
lev pentagon run --project . --json
lev pentagon gate --project . --json
pnpm --filter @lev-os/testing test
pnpm audit --audit-level high
```

### 2. Three-plane README vs four-plane architecture

The root README says Lev is easiest to understand as three planes: FlowMind, Graph, Event Bus. `docs/ARCHITECTURE.md` canonizes a four-plane runtime boundary: FlowMind, Orchestration, Graph, Event Bus.

Wiki verdict: use four-plane boundary in technical pages; treat README three-plane language as public framing.

### 3. `core/graph/**` docs vs `core/context-graph/**` source

Current source has `core/context-graph` and `core/graph-algorithms`; this packet did not find an active `core/graph` package. Some docs/specs still say `core/graph/**`.

Wiki verdict: standardize current-source pages on `core/context-graph` unless a fresh source check proves `core/graph` returned.

### 4. World-model "live" vs source README

The roadmap says world-model carrier and predictor are active/partial and that the composition root flips predictor live. `core/world-model/README.md` says the package gates nothing and the reconciler still uses a test fake.

Wiki verdict: `core/world-model` is source-backed but experimental/unwired for production claims in this packet.

### 5. Daemon Pentagon "missing" vs source package present

`docs/ROADMAP.md` says missing `@lev-os/daemon-pentagon` is a next fix. The clean source tree contains `core/daemon-pentagon/package.json`, and `core/testing` delegates daemon-owned Pentagon suites to that package.

Wiki verdict: "missing package" is stale as source-presence wording. It might still be true as install/runtime resolution only if a fresh run fails that way.

### 6. Specs index count drift

`docs/specs/README.md` says 62 specs total. This packet counted 84 `spec-*.md` files and 217 Markdown files under `docs/specs`.

Wiki verdict: specs index is still useful as a router and normative root, but not count-bearing until refreshed.

## Product Surface Frontier

| Surface | Current reading | Blocker / falsifier |
|---|---|---|
| AgentPing | active human-loop direction, downstream of validators | Roadmap row changes or validator blockers close. |
| now/dashboard | active surface assets | Visual/browser QA must become enforced gate for stronger claims. |
| GenUI exec daemon | support infrastructure, not default product spine in this packet | Manifest/package/test promotion. |
| prompt-stack | proposal/standalone-first | `ships-with` / roadmap promotion. |
| SDLC | active but readiness proof still open | Starter `.flow.yaml` through `lev exec --flow` with receipts. |
| browser | proposal/capability | Default shipping status plus clear integration proof. |
| vision/voice | canonical surface family plus proposal plugin posture | Default-shipping plugin metadata and validation proof. |
| evolve-memory | optional experimental plugin | Plugin flipped to shipping posture and consumer path tests. |
| autowiki | inconsistent/provisional | Add package/workspace evidence or demote explicitly. |
| autoresearch | active plugin | Fresh plugin tests if claiming runtime health. |

## Security And Runtime Frontier

| Claim | Current packet status | What would settle it |
|---|---|---|
| `new Function` remains in FlowMind gate executor | Not found in the current executor by Packet 7 source scout; roadmap still says open | Fresh targeted grep plus repo doc correction if source remains clean. |
| ambient `process.env` child env leakage | Source hits exist in multiple places; severity not fully classified here | Shared safe env builder migration check and tests. |
| `pnpm audit --audit-level high` | Packet 7 high audit passes through `pnpm run audit`; 8 low/moderate vulnerabilities remain | Decide whether low/moderate vulnerabilities block any release/readiness claim. |
| Manual events mode | Source/CLI-help backed in Packet 7; targeted event-dispatch tests fail before assertions | Fresh `lev events tail` / trigger projection / dispatch dry-run after workspace imports are fixed. |
| Always-on daemon/event automation | Not proven here | Daemon loop/live EventBus subscription proof. |
| Event contract unification | Partially unified; multiple event contracts still visible | Fresh source proof that all lifecycle/provider/dispatch paths share one contract. |

## Claim Ceiling For Current Wiki

Safe:

```text
Leviathan has real source-backed runtime surfaces and a strong architecture/spec stack; after Packet 7 and Packet 8, the ROADMAP/MVP conflict is a command-backed split verdict: named SDK/Poly is green, while default daemon Pentagon, @lev-os/testing, event-dispatch proof-spine, and release readiness remain blocked/open.
```

Unsafe:

```text
The repo is fully green.
```

Unsafe:

```text
The repo is catastrophically broken upstream because of conflict markers.
```

## Next Useful Packets

1. Proof-fix packet:
   - repair or isolate the `@lev-os/testing` Vitest/Bun-condition source-entry mismatch around `@lev-os/utils`;
   - rebase or relativize daemon MCP mini-app `receiptPath` and `gateProofPath` values so default Pentagon gate checks clone-local artifacts;
   - build or alias `@lev-os/daemon` and `@lev-os/config/xdg-paths`, then rerun event-dispatch targeted tests.

2. Graph/world-model correction packet:
   - update wiki wording around `core/context-graph`, `core/graph-algorithms`, `core/reconciler`, and `core/world-model`;
   - keep world-model claim ceiling below production wiring.

3. Plugin posture packet:
   - reconcile `plugins/PLUGINS.md`, `package.json` workspaces, each plugin package/config, and roadmap rows;
   - classify every plugin as active, proposal, inconsistent, archive/provenance, or missing proof.

4. Docs truth-front-door patch proposal:
   - propose exact repo doc fixes for `ROADMAP.md`, `mvp.md`, docs/spec count drift, and stale path references;
   - do not patch Leviathan repo unless Josh explicitly asks.
