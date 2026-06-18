---
title: Leviathan Read Order By Intent
created: 2026-06-18
updated: 2026-06-18
type: read-order
status: active
source_snapshot: c90ec8499c83db3d17f6132ec734698a8de2dbce
claim_ceiling: reading guide; not source proof
---

# Leviathan Read Order By Intent

## For A Human Trying To Understand Lev

1. [[projects/leviathan-current/what-is-leviathan]]
2. [[projects/leviathan-current/concept-atlas-current-2026-06-18]]
3. [[projects/leviathan-current/evidence-frontier-and-blockers-dashboard-2026-06-18]]
4. [[projects/leviathan-current/architecture-planes-and-ownership]]
5. [[projects/leviathan-current/agentping-human-loop-surfaces]]
6. [[projects/leviathan-current/doing-well-failing-promising-start]]

Use this path when the question is "what is this system, really?"

## For A Technical Agent Auditing Current Source

1. Root GitHub page: `https://github.com/lev-os/leviathan`
2. Root `README.md`
3. `docs/README.md`
4. `docs/specs/README.md`
5. `docs/ARCHITECTURE.md`
6. `docs/VISION.md`
7. `mvp.md`
8. `docs/ROADMAP.md`
9. `docs/NORTH_STAR.md`
10. relevant `docs/specs/spec-*.md`
11. relevant `core/**`, `plugins/**`, `packages/**`, `crates/**`
12. [[projects/leviathan-current/deep-audit-current-snapshot-2026-06-18]]
13. [[projects/leviathan-current/evidence-frontier-and-blockers-dashboard-2026-06-18]]
14. [[projects/leviathan-current/proof-audit-roadmap-vs-mvp-2026-06-18]]

Reason: `mvp.md` conflicts with `docs/ROADMAP.md`; read both before making execution-state claims, then use the proof audit for the current clean-clone split verdict.

## For A Wiki Worker

1. [[projects/leviathan-current/read-first]]
2. [[projects/leviathan-current/README]]
3. [[projects/leviathan-current/index]]
4. [[projects/leviathan-current/deep-audit-current-snapshot-2026-06-18]]
5. [[projects/leviathan-current/repo-current-vs-wiki-drift-audit-2026-06-18]]
6. [[projects/leviathan-current/concept-atlas-current-2026-06-18]]
7. [[projects/leviathan-current/evidence-frontier-and-blockers-dashboard-2026-06-18]]
8. [[projects/leviathan-current/proof-audit-roadmap-vs-mvp-2026-06-18]]
9. [[projects/leviathan-current/packet-7-clean-clone-proof-audit-receipt-2026-06-18]]
10. [[projects/leviathan-current/packet-8-wizard-mass-swarm-receipt-2026-06-18]]
11. [[projects/leviathan-current/packet-9-external-upgrade-report-intake-2026-06-18]]
12. source files from GitHub/raw or a clean `/tmp` clone
13. old packet maps only after reading the clean-current reset pages

Do not use the deleted `/Users/joshuaeisenhart/GitHub/leviathan` checkout. It is historical/damaged-context only.

## For Runtime/Execution Questions

1. `docs/ARCHITECTURE.md`
2. `docs/specs/spec-exec.md`
3. `docs/specs/spec-poly.md`
4. `docs/specs/spec-daemon.md`
5. `docs/specs/spec-event-architecture.md`
6. `docs/specs/spec-event-bus.md`
7. `docs/specs/spec-event-providers.md`
8. `core/exec/**`
9. `core/poly/**`
10. `core/daemon/**`
11. `core/event-bus/**`
12. `core/event-dispatch/**`
13. [[projects/leviathan-current/exec-poly-daemon-boundary]]
14. [[projects/leviathan-current/event-bus-causality-plane]]
15. [[projects/leviathan-current/evidence-frontier-and-blockers-dashboard-2026-06-18]]
16. [[projects/leviathan-current/proof-audit-roadmap-vs-mvp-2026-06-18]]

Correction to preserve: manual events mode does not prove daemon mode.

## For FlowMind/Policy Questions

1. `docs/specs/spec-flowmind.md`
2. `docs/ARCHITECTURE.md` four-plane section
3. `docs/design/design-flowmind*.md`
4. `core/flowmind/**`
5. `core/domain/src/execution-contract/**`
6. `core/orchestration/src/execution-contract/**`
7. [[projects/leviathan-current/flowmind-control-plane]]
8. [[projects/leviathan-current/concept-atlas-current-2026-06-18]]

Correction to preserve: FlowMind is not the worker dispatcher.

## For Graph/Memory/World-Model Questions

1. `docs/specs/spec-graph.md`
2. `docs/specs/spec-memory.md`
3. `docs/specs/spec-index.md`
4. `docs/design/world-model-substrate-product-definition.md`
5. `core/context-graph/**`
6. `core/graph-algorithms/**`
7. `core/reconciler/**`
8. `core/world-model/**`
9. `core/memory/**`
10. `core/index/**`
11. related Rust crates only after integration role is checked
12. [[projects/leviathan-current/graph-state-knowledge-plane]]
13. [[projects/leviathan-current/concept-atlas-current-2026-06-18]]

Correction to preserve: `core/graph/**` wording is stale in current docs unless source changes.

## For Product/Surface Questions

1. `docs/NORTH_STAR.md`
2. `docs/VISION.md`
3. `docs/ARCHITECTURE.md`
4. `docs/ROADMAP.md`
5. `mvp.md`
6. `plugins/PLUGINS.md`
7. relevant `plugins/*/package.json`, `README.md`, and `config.yaml`
8. `apps/**` only when the surface is being audited directly
9. [[projects/leviathan-current/agentping-human-loop-surfaces]]
10. [[projects/leviathan-current/plugin-ownership-map]]
11. [[projects/leviathan-current/evidence-frontier-and-blockers-dashboard-2026-06-18]]

Correction to preserve: architecture can list a surface family before plugin metadata proves it is default-shipping.

## For Provenance Or Josh/JP Boundary Questions

1. [[projects/leviathan-current/codex-ratchet-vs-leviathan-boundary]]
2. [[projects/leviathan-current/josh-root-constraints-in-leviathan]]
3. [[projects/leviathan-current/lev-five-constraints-vs-f01-n01]]
4. [[projects/leviathan-current/provenance-ledger-josh-jp-pass-1-2026-06-18]]
5. [[projects/leviathan-current/chat-evidence-promotion-protocol]]
6. current source docs and code
7. chat/transcript rows only after source matching

Do not collapse Codex Ratchet math/proof work into Leviathan runtime implementation.

## Sources To Demote By Default

| Source | Default role |
|---|---|
| `docs/_inbox/**` | proposal/source material, not runtime truth |
| `_archive/**` | historical/non-owning reference |
| old `/Users/joshuaeisenhart/GitHub/leviathan` citations | historical damaged-checkout evidence |
| chat transcripts | provenance candidates only |
| worker summaries | pressure reports, not source proof |
| product metrics in `NORTH_STAR.md` | positioning/supporting until revalidated |
