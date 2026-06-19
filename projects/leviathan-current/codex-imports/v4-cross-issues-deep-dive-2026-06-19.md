---
title: Leviathan V4 Cross-Issues Deep Dive
date: 2026-06-19
type: codex-import-bundle
status: imported-from-chat-v4
source_repo: lev-os/leviathan
source_snapshot: 5dd98ac4ce7afeb9e4351787179c60208de6d23f
claim_ceiling: source/wiki synthesis; not fresh runtime proof; not maintainer acceptance; not release certification
---

# Leviathan V4 Cross-Issues Deep Dive

This V4 bundle continues the wiki/repo audit after V3. It is focused on undercovered cross-cutting issues, not a repeat of the previous strengths/weaknesses pack.

Use this as a Codex-readable source for the next wiki update. Split it into real pages after review.

## Read order before using this bundle

1. `specs/leviathan-current/README`
2. `projects/leviathan-current/proof-backed-status-dashboard`
3. `projects/leviathan-current/nuanced-assessment-and-josh-provenance-2026-06-19`
4. `projects/leviathan-current/codex-imports/v3-deep-repo-nuance-bundle-2026-06-19`
5. This file

## V4 thesis

Leviathan's biggest current problem is not lack of vision. It has too much vision relative to verified runtime closure.

The next wiki layer should therefore shift from:

```text
What is Leviathan?
```

toward:

```text
Which claims are operating-contract, source-backed, package-backed, command-backed, product-backed, or just narrative/provenance?
```

V4 adds a cross-issue map around:

- operating contract vs product proof;
- docs authority and stale-status mechanics;
- AGENTS / autonomy culture risk;
- package-surface posture vs actual readiness;
- app-layer maturity;
- DX/onboarding gap;
- security gate stack;
- plugin manifest inflation;
- surface/product split;
- topology naming drift;
- economics/moat claims;
- release-readiness ladder.

## 1. Operating contract vs product proof

Leviathan has a strong operating contract culture. The docs define where truth should live, and AGENTS.md defines how agents should operate. That is a strength.

But an operating contract is not product proof.

Use this ladder:

| Rung | Meaning | Example |
|---|---|---|
| narrative | product/vision language | `one runtime, every agent, every surface` |
| contract | spec/architecture declares ownership or behavior | `docs/specs/**`, `docs/ARCHITECTURE.md` |
| package surface | package exists with exports/scripts/deps | `core/exec/package.json`, `core/poly/package.json`, `core/daemon/package.json` |
| source implementation | actual code implements behavior | `core/eval/src/constraint-manifold.ts` |
| test surface | tests exist or package has test command | package scripts / test files |
| proof receipt | command run recorded with exit/result | proof dashboard / packet receipts |
| product surface | user-facing app/API flow actually works | app/daemon/dashboard/E2E smoke |
| release-ready | install/docs/security/smoke/community gates green | not currently established |

Most false claims collapse rungs. The wiki should make the rungs visible.

## 2. Current proof split remains the main gate

The wiki's proof dashboard already gives the correct posture:

- manual event projection is source-aligned but needs current proof rerun;
- S4 `lev exec` is source-aligned by named receipt;
- Pentagon/Run Fabric is split verdict;
- `@lev-os/testing` is split verdict;
- Security P0 is split verdict;
- F01/N01 root validator is implemented narrowly;
- YAML System FlowMind rules are design-backed / not broadly runtime-enforced;
- launch readiness is not established.

Do not flatten these into one status.

The next proof packet should run a clean clone at the current SHA and record:

```bash
git rev-parse HEAD
git status --short
pnpm install
pnpm --filter @lev-os/testing test
lev pentagon run --project . --json
lev pentagon gate --project . --json
lev pentagon run --suite pentagon-sdk-poly-binding --json
pnpm audit --audit-level high
```

If install or command prerequisites fail, the claim stays blocked rather than silently downgraded into prose.

## 3. Docs authority exists, but status docs disagree

The repo has a healthy docs hierarchy:

1. specs for normative contracts;
2. architecture for ownership/topology;
3. vision for strategic destination;
4. roadmap + mvp for current execution state;
5. design for rationale;
6. inbox/archive/PM material as provenance.

But ROADMAP and MVP disagree. This is not a minor documentation bug; it is a governance issue.

Recommended wiki page:

```text
projects/leviathan-current/docs-authority-vs-status-drift-v4-2026-06-19.md
```

Core thesis:

```text
Leviathan has a good authority hierarchy, but current status truth still depends on proof receipts because ROADMAP and MVP disagree on the most important readiness gates.
```

## 4. ROADMAP is more conservative than MVP

`docs/ROADMAP.md` says the current truth is mixed. It lists real proof surfaces but says MVP spine is not complete because Pentagon/Run Fabric provider proof is red, `@lev-os/testing` fails, daemon state is unknown, stale S5 projections remain, and security P0 burn-down is open.

`mvp.md` is more optimistic. It reports named/default Pentagon proof, `@lev-os/testing`, and scoped security P0 as green, while still blocking full launch on daemon/event automation and downstream surfaces.

Interpretation:

- ROADMAP is safer for public current-state claims.
- MVP is useful as an optimistic validation ledger and feature roadmap.
- The wiki should not pick one; it should use proof receipts to adjudicate each row.

## 5. AGENTS.md is a force multiplier and a risk surface

AGENTS.md is not product truth. It is an operating contract for coding agents.

Strengths:

- autonomous completion posture;
- explicit evidence-over-assumption rule;
- small reversible diffs;
- no new dependencies without request;
- lint/typecheck/test/static analysis expectations;
- lore commit protocol with constraints, rejected options, tested/not-tested;
- delegation rules and team-mode boundaries;
- package API rules against sloppy re-exporting;
- explicit model-routing and skill-trigger conventions.

Risks:

- very strong autonomy language can push agents to over-act if task scope is unclear;
- keyword auto-triggering can create unexpected workflow activation;
- AGENTS.md is long and dense, so partial readers may obey the wrong section;
- it is an internal coding contract, not an end-user product guarantee;
- the repo could appear more disciplined than its actual proof state if people confuse agent rules with runtime proof.

Recommended wiki page:

```text
projects/leviathan-current/agents-md-operating-contract-risk-2026-06-19.md
```

Safe claim:

```text
AGENTS.md gives Leviathan a serious agent-work operating contract, but it is not evidence that the product runtime itself is green.
```

## 6. Package posture: Exec, Poly, Daemon are distinct and should stay distinct

### Exec

`@lev-os/exec` describes itself as the SDK-first execution contract for CLI/MCP/poly surfaces. It exports run, gate, transport, handlers, semaphores, clients, types, and poly adapters. It depends on config, domain, effect, eval, event-bus, event-machines, execution-ledger, flowmind, logger, orchestration, telemetry, and utils.

Safe claim:

```text
Exec is the execution contract package and central SDK surface. It is not the daemon and not the poly registry.
```

### Poly

`@lev-os/poly` describes itself as a Poly Registry System: unified runner registry for binaries, daemons, and SDK commands. It owns the `lev` binary, registry build scripts, CLI surface exports, MCP surface export, plugin validator export, and build-time integration.

Safe claim:

```text
Poly is the registry/binder/surface projection layer. It routes and projects; it does not own execution semantics or daemon lifecycle.
```

### Daemon

`@lev-os/daemon` describes itself as lifecycle, supervision, health monitoring, and task execution. It depends on config, daemon-grpc/http/mcp/websocket, domain, event-bus, exec, graph-algorithms, logger, and utils.

Safe claim:

```text
Daemon owns runtime process/lifecycle surfaces and supervision, but default daemon proof remains a separate proof gate.
```

Recommended page:

```text
projects/leviathan-current/exec-poly-daemon-package-posture-v4-2026-06-19.md
```

## 7. The app layer is real but uneven

The root package includes app workspaces such as desktop, expo, landing, lev-now, nextjs, shift-app, video, and voice-api.

Observed app posture examples:

- `apps/desktop` is an Electron desktop service manager with package/make/publish scripts and many Electron Forge dependencies.
- `apps/lev-now` has dev/build/start/renderer scripts, but deploy is literally `echo 'deploy target not configured yet'`.

Interpretation:

- App surfaces are real enough to audit as product layer.
- They are not all product-ready.
- The wiki should split app type: demo, dashboard, desktop shell, service manager, production candidate, archive, unknown.

Recommended page:

```text
projects/leviathan-current/app-layer-readiness-map-2026-06-19.md
```

## 8. Onboarding and DX remain gates, not paperwork

The README has a standard quickstart:

```bash
git clone https://github.com/lev-os/leviathan.git
cd leviathan
corepack enable
pnpm install
pnpm build
```

But quickstart existence is not quickstart proof.

DX gates should include:

- clean clone install;
- root build;
- `lev --help` / `lev doctor` / `lev health` status;
- first useful command;
- docs link validity;
- starter `.flow.yaml` path;
- no hidden local-only assumptions;
- no reliance on old local checkout paths;
- clear distinction between developer setup and operator runtime start.

Recommended page:

```text
projects/leviathan-current/onboarding-dx-proof-ladder-v4-2026-06-19.md
```

## 9. Security is a stack of gates, not one audit

The roadmap names security blockers such as `new Function`, legacy shell execution, ambient `process.env` leakage, and audit vulnerabilities.

The wiki should not use `pnpm audit --audit-level high` as the whole security story.

Security ladder:

1. no known secret leaks in docs/wiki;
2. no obvious unsafe dynamic execution in critical paths;
3. child-process env is explicitly whitelisted;
4. audit high passes;
5. low/moderate risk reviewed;
6. auth/token/cache surfaces reviewed;
7. agent execution sandbox/bounds tested;
8. daemon/service exposure reviewed;
9. AgentGuard/leases/ABAC enforcement proven on real flows;
10. release candidate security signoff.

Recommended page:

```text
projects/leviathan-current/security-gate-stack-v4-2026-06-19.md
```

## 10. Plugin manifest inflation risk

`plugins/PLUGINS.md` reports 61 plugins with config, 59 with README, 47 with src, and 38 with tests. This is impressive but dangerous if summarized as “61 working plugins.”

Use plugin posture categories:

- `ships-with:true + tests + src + command proof`
- `ships-with:true + source only`
- `ships-with:false + mature source`
- `ships-with:false + shell`
- `manifest-only / no src`
- `proposal / capability direction`
- `archive / provenance`
- `unknown until package-specific audit`

Important examples:

- `qit-engines`: source/provenance rich, `ships-with:false`, no src/tests in manifest posture.
- `vision`: `ships-with:false`, explicit provider selection, privacy settings, surface architecture.
- `voice`: `ships-with:false`, `autostart:false`, rich daemon/session/realtime config.
- `browser`: command surfaces and FlowMind programs, but needs command/test proof.
- `sdlc`: `ships-with:true`, rich flow surface, but full live SDLC loop remains proof-gated.
- `autowiki`: earlier evidence showed inconsistent/provisional posture; must not overclaim.

Recommended page:

```text
projects/leviathan-current/plugin-manifest-inflation-risk-v4-2026-06-19.md
```

## 11. Vision document contains strategic truth and speculative overhang

`docs/VISION.md` is useful because it says what belongs there: strategic architecture and boundaries, not day-to-day task lists or package health.

Strong stable ideas:

- contract-first substrate;
- Poly protocol vs Poly runtime;
- authoring -> IR -> derived registry -> consumers;
- op-owned guidance;
- thin terminal / rich GenUI;
- receipt-first economics;
- predictive kernel half;
- local-first / federate-ready;
- representation boundary;
- FlowMind as experiment substrate;
- not merging Hermes or any external agent into core.

High-risk overhang:

- living mesh;
- thousands of installs thinking in unison;
- DAO/tax/economic claims;
- avatar / ugly mirror / human-collective experiment language;
- “magnus opus” claims.

Safe wiki posture:

```text
VISION.md is the strategic-destination layer. It is useful for structural direction, but its mesh/economic/avatar sections are long-horizon vision unless backed by current runtime/product proof.
```

Recommended page:

```text
projects/leviathan-current/vision-strategic-truth-vs-magnus-opus-overhang-2026-06-19.md
```

## 12. North Star is product narrative, not runtime proof

`docs/NORTH_STAR.md` is valuable for product category. It describes Leviathan as an operating system for agent-human symbiosis and a stream-of-consciousness router. It also makes strong claims about what already exists.

Safe use:

- product positioning;
- category thesis;
- AgentPing / AgentGuard / FlowMind relationship;
- Joshua constraint attribution;
- constraint manifold story;
- world-model narrative.

Unsafe use:

- proving tests pass;
- proving enterprise readiness;
- proving world-model production wiring;
- proving every listed feature is fully productized.

Recommended page:

```text
projects/leviathan-current/north-star-narrative-vs-proof-map-2026-06-19.md
```

## 13. Memory and context economy still need implementation grading

`core/memory/README.md` describes an ambitious hexagonal memory system with episodic, procedural, semantic, temporal, and working memory; multiple backends; provenance tracking; context budgets; and feature flags.

But the same README contains TODO-like development structure and performance targets.

Safe claim:

```text
Memory architecture is well-shaped as a ports/adapters design with provenance and context-budget concepts, but implementation/readiness must be graded backend by backend.
```

Recommended page:

```text
projects/leviathan-current/memory-backend-readiness-ladder-2026-06-19.md
```

## 14. Config and XDG are important but underdocumented in wiki

`core/config/README.md` is tiny relative to how central config is. It just shows `loadConfig()` and basic structure.

The architecture and plugin configs depend heavily on:

- XDG paths;
- config cascade;
- project/module/env layering;
- plugin config;
- FlowMind declarations;
- runtime paths.

This gap deserves a page because config is the hidden skeleton of local-first/federate-ready claims.

Recommended page:

```text
projects/leviathan-current/config-xdg-fractal-root-gap-2026-06-19.md
```

## 15. Surface strategy is plural, not one app

Leviathan is not one UI. It has multiple surface families:

- AgentPing / dashboard / human-loop;
- LevUI IR;
- GenUI;
- voice;
- vision/capture;
- browser ops;
- desktop service manager;
- lev-now;
- mobile/expo;
- CLI;
- MCP/HTTP/gRPC/WebSocket;
- prompt-stack sessions;
- SDLC/autodev flows.

The wiki should represent this as a surface matrix, not a single product screen.

Recommended page:

```text
projects/leviathan-current/surface-family-matrix-v4-2026-06-19.md
```

## 16. AgentPing / AgentGuard / FlowMind need separate product lanes

North Star has three systems: Lev, AgentPing, AgentGuard.

Do not collapse them:

- Lev = runtime/control/policy/graph/architecture model.
- AgentPing = human-loop surface system and interaction layer.
- AgentGuard = scoped permission grants / accountability / containment direction.

The wiki should mark whether evidence lives in Leviathan repo, adjacent repo, submodule, community folder, docs/spec, plugin, or external GitHub.

Recommended page:

```text
projects/leviathan-current/lev-agentping-agentguard-three-system-map-2026-06-19.md
```

## 17. Enterprise readiness is a separate product track

Enterprise readiness should not be inferred from architecture. It needs its own checklist:

- ABAC and leases;
- audit trails;
- kill switches;
- cost tracking;
- resource governor;
- approval queues;
- compliance posture;
- admin surfaces;
- secrets handling;
- deployment topology;
- observability;
- incident response;
- update/migration story;
- data retention.

Current status remains not enterprise-ready unless proof pages say otherwise.

Recommended page:

```text
projects/leviathan-current/enterprise-readiness-gap-v4-2026-06-19.md
```

## 18. Economic / moat claims require adoption proof

North Star compares Lev to Kubernetes and open-source commoditization of agent platform primitives. This is a valid strategic story, but moat claims need evidence.

Possible moat ingredients:

- contract-first runtime;
- plugin architecture;
- event/receipt discipline;
- local-first + federate-ready posture;
- AgentPing/AgentGuard ecosystem;
- proof culture;
- Codex/FlowMind/Wizard/agent-operating method;
- Joshua-origin constraint/QIT material;
- JP runtime architecture and product build.

Missing moat proof:

- active users;
- third-party contributors;
- stable install;
- package release;
- external plugin authors;
- deployment stories;
- production use cases;
- docs that onboard strangers without JP/Josh context.

Recommended page:

```text
projects/leviathan-current/moat-vs-adoption-proof-v4-2026-06-19.md
```

## 19. The repo's strongest unusual combination

Most agent frameworks have one or two of these:

- prompt framework;
- tool calling;
- memory;
- workflow DAG;
- UI;
- plugin system;
- audit logs;
- local-first story.

Leviathan's unusual combination is:

```text
FlowMind contract language + Poly/Exec/Daemon runtime split + EventBus receipts + graph/context memory + plugin/surface system + AGENTS/OMX operating culture + Joshua constraint/QIT material.
```

This combination is promising. It is not the same as finished product.

## 20. New page split plan

Codex should split this bundle into these pages:

```text
projects/leviathan-current/operating-contract-vs-product-proof-2026-06-19.md
projects/leviathan-current/docs-authority-vs-status-drift-v4-2026-06-19.md
projects/leviathan-current/agents-md-operating-contract-risk-2026-06-19.md
projects/leviathan-current/exec-poly-daemon-package-posture-v4-2026-06-19.md
projects/leviathan-current/app-layer-readiness-map-2026-06-19.md
projects/leviathan-current/onboarding-dx-proof-ladder-v4-2026-06-19.md
projects/leviathan-current/security-gate-stack-v4-2026-06-19.md
projects/leviathan-current/plugin-manifest-inflation-risk-v4-2026-06-19.md
projects/leviathan-current/vision-strategic-truth-vs-magnus-opus-overhang-2026-06-19.md
projects/leviathan-current/north-star-narrative-vs-proof-map-2026-06-19.md
projects/leviathan-current/memory-backend-readiness-ladder-2026-06-19.md
projects/leviathan-current/config-xdg-fractal-root-gap-2026-06-19.md
projects/leviathan-current/surface-family-matrix-v4-2026-06-19.md
projects/leviathan-current/lev-agentping-agentguard-three-system-map-2026-06-19.md
projects/leviathan-current/enterprise-readiness-gap-v4-2026-06-19.md
projects/leviathan-current/moat-vs-adoption-proof-v4-2026-06-19.md
projects/leviathan-current/release-readiness-ladder-v4-2026-06-19.md
```

## 21. Index patch recommendation

Add this bundle to `projects/leviathan-current/index.md` under Current reset point and Assessment/research pages:

```text
- [[projects/leviathan-current/codex-imports/v4-cross-issues-deep-dive-2026-06-19]] — V4 cross-issues deep dive: docs/status drift, AGENTS operating contract risk, package posture, app layer, DX, security, plugins, surfaces, enterprise, moat/adoption proof.
```

After splitting pages, replace that single import link with the split page links.

## 22. Claim lint rules

Flag these as red:

- fully green
- enterprise-ready
- launch-ready
- all plugins work
- QIT engine runs in production
- world-model gates production decisions
- System FlowMinds all enforce YAML rules
- AgentPing is production-ready
- AgentGuard is fully enforced
- default daemon proof is settled
- ROADMAP and MVP agree
- Codex Ratchet came from Leviathan
- JP originated Ratchet root constraints

Flag these as yellow unless supported by current proof receipts:

- works
- green
- certified
- implemented
- production
- default
- universal
- every surface
- every agent
- OS

Use these instead:

- source-backed
- contract-backed
- package-backed
- implemented-narrowly
- proof-backed at packet/SHA
- split-verdict
- design-backed
- provenance-only
- plugin-shell
- product-direction
- needs current proof packet

## 23. Final V4 verdict

Leviathan's current value is real: it has a serious agent-runtime architecture, broad package/plugin surface area, strong docs/spec culture, and an unusually explicit constraint/proof lineage. Its current danger is also real: it can sound more complete than it is because the repo mixes architecture, vision, PM memory, generated manifests, active code, speculative product story, and proof receipts in one giant source field.

The wiki should therefore become a claim-level router. Every important sentence should answer:

```text
Is this narrative, contract, package, source, test, proof receipt, product surface, or release certification?
```

That one discipline will make the Leviathan wiki far more useful than a normal docs site.
