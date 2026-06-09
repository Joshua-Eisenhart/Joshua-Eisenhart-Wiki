---
title: Codex Ratchet Specs
created: 2026-05-21
updated: 2026-06-05
type: index
framing: current
tags: [specs, codex-ratchet, repo-status, process]
sources:
  - /Users/joshuaeisenhart/Codex-Ratchet/AGENTS.md
  - /Users/joshuaeisenhart/Codex-Ratchet/system_v5/docs/ENFORCEMENT_AND_PROCESS_RULES.md
  - /Users/joshuaeisenhart/Codex-Ratchet/system_v5/docs/LLM_CONTROLLER_CONTRACT.md
  - /Users/joshuaeisenhart/Codex-Ratchet/system_v5/docs/LEGO_SIM_CONTRACT.md
  - /Users/joshuaeisenhart/Codex-Ratchet/system_v5/docs/FORMAL_SCOUT_READINESS_INDEX.md
  - /Users/joshuaeisenhart/Codex-Ratchet/system_v5/docs/SIM_ESTATE_INTEGRATION_INDEX.md
---

# Codex Ratchet Specs

This folder is for repo-facing spec mirrors, status snapshots, validation indexes, and process-contract summaries for Codex Ratchet.

It exists so `/concepts` does not have to pretend to be the live repo. The concept wiki can stay divergent: owner voice, source genealogy, speculative/candidate models, MMM salience material, reference math, cross-domain mappings, and alternate framings.

## Authority Boundary

The repo remains the authority for executable status:

1. current user request and local repo instructions
2. `AGENTS.md` / `CODEX.md` for Codex behavior
3. repo process docs under `system_v5/docs/`
4. live validator/result/readiness artifacts under `system_v5/`

This folder may mirror or summarize those surfaces, but it does not promote, admit, rerun, or canonicalize anything by itself.

## What Belongs Here

- live-status mirrors and generated snapshots
- repo process-contract mirrors
- tool/function/lego/status ledgers
- sim estate and formal-scout readiness routers
- dated migration plans for repo-facing wiki pages
- historical snapshots that are clearly labeled as historical

## What Stays In Concepts

- owner thesis and source voice pages
- legacy genealogy
- divergent conceptual options
- Holodeck, Leviathan, personality, consciousness, TOE, and MMM reservoir pages
- reference math pages, if they do not claim repo admission without receipts
- nominalist translation guidance

## Mirror Rules

1. Count-bearing pages must include a generated date and source file.
2. Concept pages should link to status mirrors instead of copying live counts.
3. `/tmp` artifacts are not durable authority unless promoted to a repo/wiki-held receipt.
4. If a page says `current`, it must either be refreshed from current sources or clearly labeled as a dated snapshot.
5. If a page uses `canonical`, `proven`, `verified`, `admitted`, `settled`, or `complete`, it must say which layer earned that word.
6. Generated/source-model text stays useful, but must not be mistaken for repo proof.

## Current Control File

- [[specs/codex-ratchet/concepts-migration-index|concepts-migration-index]] - migration map for pages currently sitting in `/concepts` that should become spec mirrors, snapshots, or historical pages.
- [[specs/codex-ratchet/process-contract-mirror-index|process-contract-mirror-index]] - router for current repo process-contract mirrors and historical concept mirrors.

## Status Mirrors

Result-estate caveat (2026-06-05): the formal-scout and sim-estate mirrors below are generated index snapshots. In this checkout, `formal_scout_readiness_index.json` has `404` index rows/result paths, while live `system_v5/ops/formal_scouts/results/` has `3` direct JSON artifacts and `401` index paths absent from live results. Use direct live artifacts for direct-result claims; use the mirrors as routing/index maps until restoration or rerun.

- [[specs/codex-ratchet/formal-scout-readiness-status|formal-scout-readiness-status]] - generated readiness mirror `2026-05-23T11:56:37.212338+00:00`
- [[specs/codex-ratchet/sim-estate-integration-status|sim-estate-integration-status]] - generated estate mirror `2026-05-23T11:56:40.398292+00:00`
- [[specs/codex-ratchet/runtime-state-status|runtime-state-status]] - generated runtime/queue/lint/never-run mirror `2026-05-23T11:59:16Z`
- [[specs/codex-ratchet/tool-function-receipt-status|tool-function-receipt-status]] - dated `2026-05-17` tool/function matrix snapshot

## Current Contract Mirrors

- [[specs/codex-ratchet/enforcement-process-rules-current|enforcement-process-rules-current]]
- [[specs/codex-ratchet/llm-controller-contract-current|llm-controller-contract-current]]
- [[specs/codex-ratchet/lego-sim-contract-current|lego-sim-contract-current]]
