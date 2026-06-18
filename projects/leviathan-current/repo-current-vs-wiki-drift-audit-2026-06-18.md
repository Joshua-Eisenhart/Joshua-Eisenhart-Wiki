---
title: Leviathan Repo Current vs Wiki Drift Audit
created: 2026-06-18
updated: 2026-06-18
type: drift-audit
status: active
source_snapshot: c90ec8499c83db3d17f6132ec734698a8de2dbce
claim_ceiling: wiki drift audit; not repository proof
---

# Leviathan Repo Current vs Wiki Drift Audit

## Purpose

This page tells future readers which wiki pages remain useful but need current-source re-anchoring after the clean snapshot audit.

The short version: the wiki exists, but several runtime pages still carry historical damaged-checkout blockers as if they were current upstream truth. They should be read through [[projects/leviathan-current/deep-audit-current-snapshot-2026-06-18]].

## Fresh Evidence

- Clean snapshot: `/tmp/leviathan-wiki-src-20260618` at `c90ec8499c83db3d17f6132ec734698a8de2dbce`.
- `git status --short`: clean.
- Actual conflict-marker scan for `<<<<<<<` or `>>>>>>>`: no matches.
- Repo roadmap says source conflict markers are gone while `new Function`, ambient child-process environment leakage, and audit vulnerabilities remain open (`docs/ROADMAP.md:28`, `docs/ROADMAP.md:53-60`).
- Event Bus package entrypoint now reads as ordinary exports, not conflict text (`core/event-bus/src/index.ts:17-260`).
- Packet 6 found source-doc contradictions that are not historical local-checkout drift: `docs/ROADMAP.md` vs `mvp.md` disagree about S5/Pentagon/security/default-daemon gate status, README three-plane wording is weaker than the architecture four-plane boundary, and graph docs still mention `core/graph/**` while current source uses `core/context-graph/**`.

## Drift Classes

### Current and useful

These pages remain good reader entrypoints after front-door updates:

- [[projects/leviathan-current/what-is-leviathan]]
- [[projects/leviathan-current/current-state-and-roadmap]]
- [[projects/leviathan-current/architecture-planes-and-ownership]]
- [[projects/leviathan-current/contract-surface-map]]
- [[projects/leviathan-current/josh-root-constraints-in-leviathan]]
- [[projects/leviathan-current/lev-five-constraints-vs-f01-n01]]
- [[projects/leviathan-current/codex-ratchet-vs-leviathan-boundary]]
- [[projects/leviathan-current/chat-evidence-promotion-protocol]]

### Useful but superseded by clean-current audit

These pages preserve local-incident evidence and early maps, but their current-health language must be treated as superseded where it says conflict markers or dirty local state are current upstream blockers:

- [[projects/leviathan-current/event-bus-causality-plane]]
- [[projects/leviathan-current/runtime-module-map-full-2026-06-18]]
- [[projects/leviathan-current/runtime-build-test-surface-map-2026-06-18]]
- [[projects/leviathan-current/event-graph-orchestration-start]]
- [[projects/leviathan-current/runtime-module-map-start]]
- [[projects/leviathan-current/packet-2-runtime-map-receipt-2026-06-17]]
- [[projects/leviathan-current/packet-2-full-runtime-map-receipt-2026-06-18]]
- [[projects/leviathan-current/doing-well-failing-promising-start]]

### Historical/provenance only

These are still useful as provenance or bounded receipts, not as current source state:

- [[projects/leviathan-current/source-inventory-2026-06-17]]
- old local-path citations to `/Users/joshuaeisenhart/GitHub/leviathan`
- earlier `projects/levos/*` intake pages
- [[projects/leviathan-current/chat-provenance-queue-2026-06-17]]

## Correction Matrix

| Old wiki claim shape | Current replacement |
|---|---|
| Current repo is dirty. | The damaged local checkout was dirty before deletion; the disposable clean clone at `c90ec849...` was clean. |
| Event Bus source has unresolved current conflict markers. | Current clean snapshot has no `<<<<<<<`/`>>>>>>>` hits and Event Bus barrel reads normally; build/typecheck health is still unproven. |
| Submodule status failure blocks current repo truth. | The disposable clone did not initialize submodules; `-` submodule status means unchecked-out gitlinks, not a dirty superproject. |
| Runtime health is blocked by conflict markers. | Runtime health is mixed. This drift page did not run proof commands, but Packet 7 later ran bounded clean-clone checks and found named SDK/Poly proof green while default daemon Pentagon and `@lev-os/testing` remain red/blocked. |
| Packet 2 is the current runtime baseline. | Packet 2 is a historical local-checkout inventory; this clean snapshot is the current wiki baseline. |
| `docs/ROADMAP.md` alone settles current execution truth. | `docs/ROADMAP.md` must be read with `mvp.md` until fresh proof reruns reconcile their contradictory gate status. |
| Graph state plane is simply `core/graph/**`. | Current source evidence points to `core/context-graph/**` plus `core/graph-algorithms/**`; `core/graph/**` wording is stale unless source changes. |
| World-model predictor is production-live. | `core/world-model` is source-backed but experimental/unwired for production claims in this packet. |

## Required Wording For Future Pages

Use:

```text
Historical local checkout observation from June 17-18; superseded for current upstream truth by clean snapshot c90ec8499c83db3d17f6132ec734698a8de2dbce.
```

Use:

```text
Current clean snapshot shows no unresolved conflict start/end markers. This drift page did not run build/typecheck/test commands; for the later bounded proof run, read [[projects/leviathan-current/proof-audit-roadmap-vs-mvp-2026-06-18]].
```

Do not use:

```text
The current repo has unresolved conflict markers.
```

## Remaining Work

This drift page does not rewrite every old page. It marks the current interpretation layer. The next wiki-cleanup pass should either:

1. update each superseded runtime page in place, or
2. archive/demote the stale local-checkout pages under a historical incident section.
