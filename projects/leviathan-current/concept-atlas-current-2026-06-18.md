---
title: Leviathan Current Concept Atlas
created: 2026-06-18
updated: 2026-06-18
type: concept-atlas
status: active
source_snapshot: c90ec8499c83db3d17f6132ec734698a8de2dbce
claim_ceiling: source-backed wiki concept map; not build proof, not test proof, not maintainer acceptance
---

# Leviathan Current Concept Atlas

## Purpose

This page is the next layer after [[projects/leviathan-current/deep-audit-current-snapshot-2026-06-18]].

The clean snapshot audit says which source tree was read. This atlas says what the major concepts are, what names they travel under, what evidence supports them, and where the wiki should route them.

Source baseline:

- GitHub repo: `https://github.com/lev-os/leviathan`
- Remote `main`: `c90ec8499c83db3d17f6132ec734698a8de2dbce`
- Disposable clone: `/tmp/leviathan-wiki-src-20260618`
- Remote `HEAD` matched clone `HEAD` during this pass.
- Clone status was clean.

No build, typecheck, package install, or test suite was run in this packet.

## Evidence Levels

Use these labels when reading rows:

| Evidence level | Meaning |
|---|---|
| `source-backed` | Current checked-in source files implement or define the surface. |
| `canonical-doc` | Current docs/specs/architecture define the contract or boundary. |
| `roadmap-claim` | Current roadmap or MVP document claims status, but this packet did not rerun the proof. |
| `contested-doc` | Current repo docs disagree and need a fresh rerun or reconciliation. |
| `proposal-inbox` | Useful source/proposal material under `docs/_inbox/**` or similar. |
| `archive-provenance` | Historical material under `_archive/**` or old PM/handoff paths. |
| `worker-pressure` | Subagent conclusion; useful only after controller source checks or explicit receipt. |

## Core Runtime Concepts

| Concept | Aliases | Evidence | Current wiki wording |
|---|---|---|---|
| FlowMind | control plane, policy plane, declaration compiler, Graph Blueprint admission | `canonical-doc` + `source-backed` | FlowMind declares, validates, compiles, routes policy, and gates. It does not own worker dispatch or runtime scheduling. |
| Orchestration | execution plane, DAG scheduler, iterative runner, `ecStart` / `ecNext` | `canonical-doc` + `source-backed` | Orchestration owns scheduling, worker coordination, retry/concurrency strategy, and execution progression. |
| Graph / context graph | state/knowledge plane, entity graph, context projection, lineage | `source-backed` with stale-path caveat | Current JS package is `core/context-graph`; docs that say `core/graph/**` need current-source re-anchoring. |
| Event Bus | causality spine, `LevEvent`, replay/audit spine | `canonical-doc` + `source-backed`, partially unified | The event plane is real, but code still has multiple event contracts/surfaces. Do not claim one completely unified event contract without a fresh proof. |
| Exec | `@lev-os/exec`, execution SDK, `createExec(dispatch)` | `canonical-doc` + `source-backed` | Exec is the execution SDK and real execution plane. It owns provider execution semantics, structured results, preflight, budgets, and evidence handling. |
| Poly Runtime | binder, router, registry, surface projection, transport selection | `canonical-doc` + `source-backed` | Poly binds and routes. It does not own lifecycle or execution; Exec executes and Daemon supervises. |
| Daemon | process supervisor, worker pool, task queue, heartbeat/core loop | `source-backed`, readiness contested | Daemon code exists. Live daemon/event automation proof remains a separate, contested claim. |
| Runtime governance | policy loader, admission/preflight, budgets, lifecycle trace writing | `source-backed` | Governance is implemented across event-bus, exec, and lifecycle surfaces. Do not collapse that into launch readiness. |

Primary current pages:

- [[projects/leviathan-current/architecture-planes-and-ownership]]
- [[projects/leviathan-current/flowmind-control-plane]]
- [[projects/leviathan-current/graph-state-knowledge-plane]]
- [[projects/leviathan-current/event-bus-causality-plane]]
- [[projects/leviathan-current/orchestration-execution-plane]]
- [[projects/leviathan-current/exec-poly-daemon-boundary]]

## State, Memory, And Predictive Substrate

| Concept | Aliases | Evidence | Current wiki wording |
|---|---|---|---|
| Context graph | `@lev-os/context-graph`, `ContextProjector`, JSONL event store, lineage adapters | `source-backed` | Use `context-graph` for the current JS package unless a fresh source check proves `core/graph` returned. |
| Graph algorithms | topo sort, dependency resolution, critical path, causal sort | `source-backed` | Treat as active graph/DAG utility code used by multiple packages, not the whole graph state plane. |
| Reconciler | surprise-gated reconcile loop, content-addressed supersede-CAS, predictive kernel spine | `source-backed` + `canonical-doc` | Reconciler is a real code surface and a key predictive-kernel spine. |
| World-model | carrier, readout, predictor substrate, QIT belief state | `source-backed` but experimental | Current source says world-model gates nothing and reconciler still uses a test fake. Treat as experimental carrier/readout work, not production wiring. |
| Memory | hybrid memory, working/episodic/semantic/procedural, query classifier, RRF | `source-backed` + `canonical-doc` | Keep memory separate from semantic/vector index. |
| Index | LEANN/vector index, semantic search, `VectorIndexClient`, `quickSearch` | `source-backed` + `canonical-doc` | Index is search/index infrastructure, not the whole memory system. |
| Rust graph/memory crates | `lev-graph`, `lev-entity-graph`, `lev-memory` | crate-metadata-backed | Treat as active or parallel Rust surfaces only after integration checks; current packet did not prove runtime binding. |

Primary current pages:

- [[projects/leviathan-current/graph-state-knowledge-plane]]
- [[projects/leviathan-current/runtime-module-map-full-2026-06-18]]
- [[projects/leviathan-current/repo-current-vs-wiki-drift-audit-2026-06-18]]

## Product And Surface Concepts

| Concept | Aliases | Evidence | Current wiki wording |
|---|---|---|---|
| AgentPing | human-loop surface, default dashboard host, interaction layer | active/downstream | Active human-loop direction, but roadmap says validator-led blockers remain. |
| AgentLease / scoped authority | leases, ABAC, scoped grants, authority expiration | mixed source/product | Keep as scoped-authority concept with code/doc anchors; avoid claiming complete product integration. |
| now / dashboard / GenUI | visual surfaces, renderer, dashboard assets | mixed active/proposal | Split the family: `now` and dashboard are active surface assets; `genui-exec-daemon` is support infrastructure, not a default shipping spine here. |
| prompt-stack | deterministic workflow/session stack | proposal/standalone-first | Treat as stopgap/manual/repo-local product surface unless manifest/roadmap promotes it. |
| SDLC | self-managing SDLC flow, `.flow.yaml`, task DNA, validation | active with proof gaps | Active pathway with pending readiness tasks around validators and flow proof. |
| platforms | integration adapters | active | Core integration adapter surface. |
| browser | 3-tier cascade, PinchTab/browser-use/Skyvern | proposal/capability | Capability/proposal surface, not default core runtime. |
| vision / voice | capture providers, voice-first interaction | proposal/canonical-family split | Architecture lists the surface family, but plugin metadata is not default-shipping proof. |
| evolve-memory | GEPA/mnemos-style memory evolution | proposal/experimental | Optional experimental plugin, not baseline shipped memory. |
| autoresearch | research automation plugin | active | Package/docs/workspace evidence support active status. |
| autowiki | wiki automation plugin | inconsistent/provisional | Manifest/config evidence exists, but no package/workspace evidence in this pass. |

Primary current pages:

- [[projects/leviathan-current/agentping-human-loop-surfaces]]
- [[projects/leviathan-current/agentlease-scoped-authority]]
- [[projects/leviathan-current/plugin-ownership-map]]

## Docs And Provenance Concepts

| Concept | Evidence | Current wiki wording |
|---|---|---|
| `docs/specs/**` | normative by `docs/README.md` | Treat as implementation contracts. Count-bearing index text is stale: it says 62 specs, while this pass counted 84 `spec-*.md` files. |
| `docs/ARCHITECTURE.md` | active canonical reference | Treat as topology and ownership authority. Its old "Current Violations" section needs careful reading because some listed items are later marked resolved. |
| `docs/VISION.md` | active strategic destination | Use for stable boundaries and direction, not package health. |
| `docs/NORTH_STAR.md` | product thesis/positioning | Use for narrative and thesis. Do not promote product metrics without fresh checks. |
| `docs/ROADMAP.md` | current execution roadmap, but contested | Important, but not sole truth while it conflicts with `mvp.md`. |
| `mvp.md` | newer 2026-05-18 validation refresh | Important contested status surface. Needs rerun/reconciliation against `ROADMAP.md`. |
| `docs/design/**` | rationale/reference | Read after specs and architecture. |
| `docs/_inbox/**` | source/proposal field | Useful but explicitly not runtime truth. |
| `_archive/**` | historical/non-owning | Do not use for current implementation or decision-making without a promotion note. |
| `.lev/pm/**` / `.lev/decisions/**` | PM/provenance | Use as staging, continuity, and decision provenance unless promoted to docs/specs. |

Primary current pages:

- [[projects/leviathan-current/read-order-by-intent-2026-06-18]]
- [[projects/leviathan-current/evidence-frontier-and-blockers-dashboard-2026-06-18]]
- [[projects/leviathan-current/repo-current-vs-wiki-drift-audit-2026-06-18]]

## Strong Corrections From This Packet

1. The wiki should prefer the four-plane boundary:
   - FlowMind: control/policy.
   - Orchestration: execution.
   - Graph/context graph: state/knowledge.
   - Event Bus: causality/audit spine.

2. `README.md` still says Lev is easiest to understand as three planes; that is public framing. `docs/ARCHITECTURE.md` and `docs/ROADMAP.md` preserve the stronger four-plane correction.

3. `docs/ROADMAP.md` and `mvp.md` conflict on S5/Pentagon/security/default-daemon gate status. The wiki should mark this as contested until a fresh rerun settles it.

4. Roadmap wording that says `@lev-os/daemon-pentagon` is missing is stale as source presence: `core/daemon-pentagon/package.json` exists in this snapshot. It may still be missing at install/runtime resolution, but that is a different claim.

5. The world-model is not production wiring just because the roadmap says the predictor flips live. The current source packet should call it experimental/unwired unless fresh integration proof is read.

6. Old conflict-marker claims are historical damaged-checkout evidence only. The clean snapshot had no `<<<<<<<` or `>>>>>>>` matches.

## Open Falsifiers

- Fresh `lev pentagon gate --project . --json` and daemon-owned Run Fabric reruns.
- Fresh `lev events tail`, `lev triggers project --dry-run`, and `lev triggers dispatch --exec-dry-run` checks.
- Fresh package install/build/typecheck/test proof in a clean clone.
- A source check proving current docs have replaced `core/graph/**` with `core/context-graph/**`.
- A source check proving `core/world-model` is wired into production reconciler behavior.
- Plugin manifest/package/workspace reconciliation for `autowiki`, `voice`, `vision`, `browser`, and `prompt-stack`.
