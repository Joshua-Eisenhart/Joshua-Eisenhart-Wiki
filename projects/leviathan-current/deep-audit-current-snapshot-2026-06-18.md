---
title: Leviathan Deep Audit - Current Clean Snapshot
created: 2026-06-18
updated: 2026-06-18
type: deep-audit
status: active
source_snapshot: c90ec8499c83db3d17f6132ec734698a8de2dbce
claim_ceiling: read-only source/wiki synthesis; not build proof, not maintainer acceptance, not release readiness
---

# Leviathan Deep Audit - Current Clean Snapshot

## Snapshot

This page is the current source-grounded reset point for the Leviathan wiki after the damaged local checkout was deleted.

- Source repo: `https://github.com/lev-os/leviathan.git`
- Fresh clone used for this pass: `/tmp/leviathan-wiki-src-20260618`
- Commit audited: `c90ec8499c83db3d17f6132ec734698a8de2dbce`
- `git status --short`: clean.
- Submodules were not initialized in the disposable clone; `git submodule status --recursive` lists gitlinks with `-` prefixes. This pass audits the superproject plus checked-in files, not submodule internals.

Claim ceiling: this is a wiki/source audit. It does not prove build health, package tests, release readiness, or maintainer acceptance.

## Current Bottom Line

Leviathan is a pre-release open runtime for agent-human systems. The root README says the architecture is real and usable, but hardening is active and workflows are still moving (`README.md:17`). It frames Lev as a runtime where agents act through real surfaces, operate under policy/control, remember/classify context, emit auditable events, and compose into ecosystems/products (`README.md:21-31`).

The current repo still preserves a deliberately mixed truth:

- The foundation exists: FlowMind compiler/execution surfaces, `@lev-os/exec`, broad CLI/package surfaces, graph/memory work, and AgentPing-oriented human-loop work (`README.md:45-66`).
- The universal context graph is not fully landed, the system is not fully enterprise-ready, and some implementation areas lag the architecture (`README.md:56-66`).
- The roadmap says the current truth is mixed: runtime-governance, lifecycle, event-dispatch, manual event projection CLI, receipt/trace CLI, and S4 provider-backed `lev exec` have real proof, while the MVP spine is not complete (`docs/ROADMAP.md:22-30`).
- Current roadmap blockers include Pentagon/Run Fabric provider proof, `@lev-os/testing`, daemon-state uncertainty, stale S5 projections, security P0 burn-down, `new Function`, ambient `process.env` child-process leakage, and high-audit vulnerabilities (`docs/ROADMAP.md:26-45`, `docs/ROADMAP.md:53-90`).

## Authority Stack

The repo's own docs define the reading order:

1. Root README for the public frame (`README.md:17-66`).
2. `docs/README.md` for where truth lives (`docs/README.md:1-11`).
3. `docs/specs/**` as normative contracts (`docs/README.md:61-72`; `docs/specs/README.md:1-54`).
4. `docs/ARCHITECTURE.md` for topology and ownership (`docs/ARCHITECTURE.md:21-29`, `docs/ARCHITECTURE.md:45-63`, `docs/ARCHITECTURE.md:161-208`).
5. `docs/VISION.md` for stable destination framing.
6. `docs/ROADMAP.md` for current execution truth (`docs/README.md:13-25`, `docs/README.md:27-49`).
7. `docs/design/**` for rationale.
8. `docs/_inbox/**`, `_archive/**`, chats, and older wiki notes as source/provenance, not current implementation truth by default.

The wiki should follow that order. Old Hermes/workers/chat material can help generate questions, but it cannot override the clean source snapshot.

## Runtime Shape

Current canonical architecture separates:

- FlowMind: control/policy plane.
- Orchestration: execution plane.
- Graph: state/knowledge plane.
- Event Bus: causality plane.
- Exec, Poly, Daemon, Logger, Telemetry, UI, plugins, and domain contracts as separately owned surfaces.

The architecture doc explicitly says Lev compiles and validates workflow declarations through FlowMind, executes through Orchestration, routes/persists events through the event bus, runs cross-runtime bindings through Poly, and extends behavior through plugins (`docs/ARCHITECTURE.md:21-29`). It also rejects a single universal storage substrate: code facts, operational state, event streams, graph relationships, overlays, config, and policy each use the right representation, with gate-checked mutation plus events/receipts/proof as the invariant (`docs/ARCHITECTURE.md:45-63`).

The root package is a TypeScript/PNPM monorepo with many workspaces, plus a Rust workspace under `crates/`. The clean clone contains large checked-in archives/workshop material, so raw file counts should not be used as product maturity claims.

## Major Current Correction

Earlier wiki pages from the damaged local checkout claimed unresolved source conflict markers in Event Bus, build/skills, and Rust TUI files. That was a valid historical observation for the deleted local checkout, but it is not current upstream truth for the clean snapshot.

Current evidence:

- `docs/ROADMAP.md` says source conflict markers are gone (`docs/ROADMAP.md:28` and `docs/ROADMAP.md:53-60`).
- A fresh scan for actual conflict starts/ends, `rg -n "^(<<<<<<<|>>>>>>>)" /tmp/leviathan-wiki-src-20260618`, returned no matches.
- `core/event-bus/src/index.ts` in the clean clone reads as normal exports, including event, context, runtime, aggregate, policy, bridge, and workflow exports (`core/event-bus/src/index.ts:17-260`).

Do not infer green build health from this. The correct update is narrower: old conflict-marker blockers are historical/damaged-checkout findings, while current runtime health remains open until build/typecheck/test commands are run on the clean snapshot.

## What The Wiki Should Say Now

Safe current statement:

```text
Lev is a pre-release, source-visible agent-human runtime with real architecture and many implemented surfaces. Its current blockers are not "no repo" or "all conflict markers"; they are the roadmap's live hardening issues: Pentagon/Run Fabric proof, security P0 burn-down, @lev-os/testing, daemon proof, stale S5 projections, dependency audit, and release/onboarding gates.
```

Unsafe current statements:

- "Event Bus is blocked by current upstream conflict markers."
- "The repo is dirty."
- "Submodule status fails in upstream."
- "The system is enterprise-ready."
- "The wiki proves runtime health."

## Constraint And Provenance Boundary

Current Leviathan constraint surfaces support `C1/F01` and `C2/N01` as root axioms. `C3-C5` are present and important, but current FlowMind tiering treats them as governance or derived-aligned constraints unless repo evidence promotes them.

Treat Josh/root-constraint language as provenance and design alignment. Treat JP/Lev runtime language as implementation and architecture. Treat FlowMind Ratchet Harness language as a bridge, not identity between Leviathan and Codex Ratchet.

## Next Useful Audit

The next source pass should be a clean-clone build/test audit, not another content inventory:

1. Install dependencies in a disposable clone.
2. Run the smallest safe root checks: `pnpm run docs:validate:json`, `pnpm run test:guard:legacy-paths`, `pnpm run test:guard:runtime-routing`, and a targeted `pnpm --dir core/event-bus run typecheck`.
3. If dependency install is too expensive, document that as blocked and keep claims at source-doc/manifests level.
