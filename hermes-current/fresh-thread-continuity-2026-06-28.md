# Fresh Thread Continuity — 2026-06-28

Purpose: preserve the active work recovered from the overwhelmed Hermes thread so a fresh session can continue without rehydrating the full transcript.

Status: active recovery / routing note.

Source thread:
- Hermes session: `20260628_004303_aa3f2b`
- Recovered in fresh thread after user clarified this was the target session ID.
- Support level: session-recovered plus current wiki/file checks; not a substitute for direct repo verification before editing Lev.

## What this note preserves

The prior thread had two intertwined lanes:

1. **Lev implementation/audit lane** — focused on ClaimGate, graph persistence, legacy-path guards, source-read receipts, notary/falsifier binding, model-lane collapse, and WaveGraph edge contracts.
2. **Wiki / Hermes continuity lane** — user asked Hermes to keep the wiki up to date, avoid losing the work, continue general wiki improvement/research/digestion, track projects, and keep Hermes memory routed through durable wiki surfaces.

This note is for the second lane first: continuity and routing. It does not authorize Hermes to mutate the Lev repo by itself.

## Direct user-pasted follow-up

The user later pasted the previous thread's last substantive output directly into the fresh thread. That pasted output is now routed into [[projects/leviathan-current/lev-claimgate-digging-status-2026-06-28]]. Treat the project page as the compact blocker map and this page as the cross-thread continuity router.

Cost/model guard added after user steering: do not mass-call OpenRouter, and do not route work to `gpt-3.5-turbo`. Current work should stay local/file-backed unless the user explicitly authorizes a model route.

## Recovered Lev state from the prior thread

Observed from the prior Hermes thread, not freshly re-run here:

- Orchestration tests and typechecks had been reported green in the prior thread.
- Graph full package test was reported red because ignored/stale `core/graph/dist/__tests__` was being discovered by `bun test`, while the source TypeScript test passed.
- Legacy-path guard was reported red and likely over-broad: it flags live package self-references and rejection-test text as if they were forbidden legacy imports.
- Source-read binding remained incomplete: the needed chain was `SourcePackReadReceipt -> loadedContextReceipts -> member/wave sourceRefs -> evidence_manifest contextContentHashes`.
- ClaimGate notary/falsifier binding was narrowed but not closed: a producer-authored falsifier file could still report `closed / 0` unless the host context/envelope or a trusted receipt path was required.
- Root package scripts had duplicate `test:pentagon` and `test:pentagon:gate` keys.
- The Lev worktree was dirty and not safe to land as one broad patch.

Claude-side handoff in the recovered thread named this order:

1. Persistence fix at `runtime.ts:171`: relative path to absolute or environment-anchored path.
2. Legacy-path guard: exempt live self-referencing packages rather than migrate them.
3. Clean commit of the coherent ClaimGate-and-graph slice, separated from the large dirty state.
4. Notary fix: wire existing `MechanicalProbeRunReceipt` through trusted refs/options override paths so gates trust host-produced execution, not producer-authored files.
5. Residual frontier: pre-commit or sign receipts before the claiming agent sees them, closing the producer-controls-engine-input hole.

Claim ceiling: this is a recovered order and blocker map. Before any Lev edit, re-check the live repo status, active Codex/Claude writers, exact files, and current tests.

## Failed/partial worker receipts from prior thread

A 4-worker audit batch returned no usable full summaries:

- Wizard Ratchet newest files: hit API usage limit before summary.
- ClaimGate source-bound evidence/notary bypass audit: connection error.
- Graph persistence/runtime and legacy guard audit: hit API usage limit before summary.
- Model-lane collapse and WaveGraph edge contract audit: connection error.

Status: these count as blocked/partial route attempts, not audit conclusions.

## Current fresh-thread checks

Checked in this fresh thread:

- `hermes-current/` spine read: `read-first.md`, `about-me-and-how-to-work-with-me.md`, `active-intentions.md`, `environment-and-rules.md`, `current-vs-legacy.md`, `skills-and-agent-rules.md`, `active-plans.md`, and `hermes-memory-offload.md`.
- Wiki probe before this note: `page_count=460`, `index_header_count=460`, `indexed_link_count=578`, and no missing pages, orphans, broken links, stubs, malformed wikilinks, or stale namespace wikilinks.
- Wiki git status was already dirty before this note, with Research Ratchet / Leviathan / Codex Ratchet changes and untracked branch-import material.
- Hermes cron list showed one wiki-deepening job: `33efc1f65a72`, `leviathan-current-wiki-bounded-deepening`, paused/disabled. In this TUI surface, default/origin cron delivery is local-only and should not be promised as a live notification channel.

## Active next move

For this fresh thread, the honest continuation is:

1. Preserve this recovery note and link it from the front door surfaces.
2. Keep wiki maintenance bounded: probe -> patch one routing/capture cluster -> probe again -> log.
3. Do not launch more broad audit councils just to look busy. The recovered bottleneck is implementation/verification plus durable wiki tracking.
4. Do not edit Lev until the controller verifies live repo state and the user explicitly assigns Hermes the edit lane or a read-only wiki-only tranche.

## Open choices for later

- Resume wiki-only maintenance: deepen Research Ratchet / Leviathan / Codex Ratchet routing and keep the wiki clean.
- Resume Lev repo implementation: only after checking live writers, dirty state, and exact target files.
- Restart a bounded wiki cron: only with a self-contained prompt, finite tranche scope, pre/post `wiki_probe.py`, and a gateway delivery target if user wants notifications.

## Claim ceiling

Recovery/routing note only. No Lev edit, no repo test rerun, no full Wizard council, no live multimodel proof, no project-status promotion.

Related notes:
- [[read-first]]
- [[active-plans]]
- [[hermes-memory-offload]]
- [[../log|wiki log]]

Write mode: controller-maintained.
