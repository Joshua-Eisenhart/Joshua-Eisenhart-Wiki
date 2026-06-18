---
title: Wizard Swarm Current Wiki Receipt - 2026-06-18
created: 2026-06-18
updated: 2026-06-18
type: receipt
status: active
source_snapshot: c90ec8499c83db3d17f6132ec734698a8de2dbce
claim_ceiling: route and wiki-edit receipt; not full Wizard proof, not build proof
---

# Wizard Swarm Current Wiki Receipt - 2026-06-18

## What Ran

This was a partial, receipt-backed Wizard v4.3/wiki audit pass, not a full formal Wizard topology.

- Clean source clone: `/tmp/leviathan-wiki-src-20260618`.
- Source commit: `c90ec8499c83db3d17f6132ec734698a8de2dbce`.
- Clean status: `git status --short` returned no output.
- Wizard v4.3 object card: `/tmp/leviathan_wiki_v43_object_card.json`.
- Wizard v4.3 validation: `/tmp/leviathan_wiki_v43_validation.json`, `ok: true`, no warnings.
- Native Codex subagents completed: 4/4.
- Claude Bridge advisory workers attempted: 2/2 blocked by `401 Invalid authentication credentials`.

## Native Worker Receipts

Authority/docs lane:

- Confirmed the source authority stack should include `docs/specs/`, `ARCHITECTURE.md`, `VISION.md`, `ROADMAP.md`, `NORTH_STAR.md`, root README, and then design/inbox/archive/provenance material.
- Flagged that `README.md` and `read-first.md` skipped `VISION.md`, `docs/specs/README.md`, and `AGENTS.md` in useful places.
- Flagged that the wiki still said runtime verification was open because Event Bus had unresolved conflict markers, while current source roadmap says source conflict markers are gone.

Runtime/source lane:

- Confirmed current implementation topology is a TypeScript/PNPM monorepo plus Rust workspace.
- Noted `pnpm-workspace.yaml` is the fuller JS workspace inventory and includes current entries not in root `package.json` workspaces: `core/graph-algorithms`, `core/reconciler`, `core/world-model`, and `plugins/sim-eval`.
- Flagged stale old-page paths: `core/graph` should not be treated as current when the clean clone has `core/context-graph`, `core/reconciler`, and `core/world-model`; `plugins/core-sdlc` should be `plugins/sdlc`; `crates/levd` is not an active member in current `crates/Cargo.toml`.
- Confirmed conflict-marker claims in old runtime pages should be quarantined as different-checkout history.

Constraint/provenance lane:

- Confirmed `C1/F01` and `C2/N01` are the current source-supported roots.
- Confirmed `C3/C4/C5` should remain governance or derived-aligned unless later repo evidence promotes them.
- Confirmed Josh/JP, FlowMind Ratchet Harness, and QIT glossary material should stay provenance/bridge material, not implementation proof.

Wiki navigation lane:

- Recommended first-screen path: `read-first` -> `README` -> `index`, then current-authority pages, then runtime maps.
- Recommended demoting starter pages and older Packet 2 receipts.
- Reported broken Markdown links in `josh-contribution-signal-index-2026-06-17.md` from raw snippets.

## Local Controller Checks

Commands/observations used in this pass:

- `git -C /tmp/leviathan-wiki-src-20260618 rev-parse HEAD`
- `git -C /tmp/leviathan-wiki-src-20260618 status --short`
- `git -C /tmp/leviathan-wiki-src-20260618 submodule status --recursive`
- `rg -n "^(<<<<<<<|>>>>>>>)" /tmp/leviathan-wiki-src-20260618 ...`
- Read root `README.md`, `AGENTS.md`, `docs/README.md`, `docs/NORTH_STAR.md`, `docs/ROADMAP.md`, `docs/ARCHITECTURE.md`, `docs/specs/README.md`, root `package.json`, `pnpm-workspace.yaml`, and `crates/Cargo.toml`.

## Wiki Changes From This Pass

Added:

- [[projects/leviathan-current/deep-audit-current-snapshot-2026-06-18]]
- [[projects/leviathan-current/repo-current-vs-wiki-drift-audit-2026-06-18]]
- [[projects/leviathan-current/wizard-swarm-current-wiki-receipt-2026-06-18]]

Updated:

- [[projects/leviathan-current/index]]
- [[projects/leviathan-current/README]]
- [[projects/leviathan-current/read-first]]
- stale runtime pages annotated as superseded historical local-checkout maps.

## Blockers

- No build/typecheck/test commands were run against the clean clone.
- Claude Bridge external model lanes failed authentication and do not count as completed external worker results.
- Submodules were not initialized in the disposable clone, so submodule internals were not audited.
- Old runtime maps are still useful, but some details need a future line-by-line rewrite around current package names and workspace surfaces.
