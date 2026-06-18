---
title: Memory Source Coverage Matrix
type: coverage-audit
created: 2026-06-17
updated: 2026-06-17
tags: [memory, provenance, claude, codex, hermes, cocoindex, wiki]
status: active-coverage-matrix
claim_ceiling: inventory-and-routing-only
promotion_allowed: false
formal_admission_allowed: false
---

# Memory Source Coverage Matrix — 2026-06-17

## Purpose

This page tracks whether Claude, Hermes, Codex app, codex1, and codex2 memory/source stores have been processed into the wiki. It is an inventory and routing surface, not a memory dump and not doctrine.

## Processing rule

All memory-derived rows must pass through: opaque source ID, privacy/secret scan, bounded redacted quote or owner-confirmed paraphrase, owner-kernel vs owner-uncertainty vs assistant-elaboration split, evidence/research lane, and claim ceiling.

## Source estate counts

| Source class | exists | files | md | json | jsonl | txt | size MB | newest | wiki status | note |
|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| `hermes_profile_memory` | True | 4 | 2 | 0 | 0 | 0 | 0.0 | 2026-06-17T15:09:20 | **processed/native** | Hermes profile memory is compact and fronted by hermes-current; use as bootstrap only. |
| `claude_project_memory_cr` | True | 270 | 270 | 0 | 0 | 0 | 1.1 | 2026-06-14T18:20:46 | **thin/partial** | claude-memory has a small landing zone; project memory rows are not fully ledgered. |
| `claude_project_memory_desktop_cr` | True | 196 | 196 | 0 | 0 | 0 | 0.8 | 2026-06-17T16:06:17 | **thin/partial** | Desktop CR Claude memory is a separate source class and not fully ledgered. |
| `codex1_memory` | True | 2210 | 1090 | 0 | 0 | 0 | 13.3 | 2026-06-17T16:07:59 | **mostly-missing** | codex-memory landing zone is hollow relative to codex1 memory estate. |
| `codex1_sessions` | True | 1025 | 0 | 0 | 1023 | 0 | 592.7 | 2026-06-17T16:02:16 | **mostly-missing** | session JSONL estate needs source-class inventory, not raw copy. |
| `codex2_memory` | True | 129 | 50 | 0 | 0 | 0 | 1.0 | 2026-06-17T12:01:57 | **mostly-missing** | codex2 memory files exist but are not represented as a ledger. |
| `codex2_sessions` | True | 2520 | 0 | 0 | 2518 | 0 | 2794.8 | 2026-06-17T12:02:01 | **mostly-missing** | codex2 sessions are large and unprocessed except scattered project pages. |
| `codex_app_support` | True | 2486 | 0 | 48 | 0 | 7 | 190.1 | 2026-06-17T16:11:48 | **unprocessed/needs-subpath-inventory** | App support files exist; exact task-store semantics require a separate app-storage pass. |
| `openai_chat_support` | True | 129 | 0 | 1 | 0 | 0 | 96.2 | 2026-06-16T22:50:48 | **unprocessed/needs-subpath-inventory** | OpenAI Chat app support exists; no curated wiki landing found. |
| `openai_atlas_support` | True | 774 | 0 | 68 | 0 | 7 | 162.6 | 2026-05-10T09:17:41 | **unprocessed/needs-subpath-inventory** | Atlas support exists; no curated wiki landing found. |

## Wiki landing zones

| Wiki zone | exists | files | md | json | jsonl | size MB | newest |
|---|---:|---:|---:|---:|---:|---:|---|
| `hermes_current` | True | 64 | 63 | 0 | 0 | 0.4 | 2026-06-17T15:44:43 |
| `claude_memory` | True | 7 | 6 | 0 | 0 | 0.0 | 2026-06-17T12:54:40 |
| `codex_memory` | True | 1 | 0 | 0 | 0 | 0.0 | 2026-06-17T14:19:43 |
| `codex_ratchet_project` | True | 112 | 91 | 0 | 0 | 2.5 | 2026-06-17T16:10:47 |

## Verdict

- Hermes is comparatively well represented through `hermes-current/`, though its compact memory should still be treated as bootstrap rather than doctrine.
- Claude project memories are only partially represented; the wiki has a thin `claude-memory/` landing zone relative to hundreds of source markdown rows.
- Codex1, Codex2, Codex app/OpenAI app support are the largest unprocessed source estates. They need ledgered tranches, not bulk import.
- The existing prompt-memory router/tranche define the correct method, but the first provenance ledger had not existed before this campaign tranche.

## Candidate inventory artifact

- Redacted candidate snippets were written to `/tmp/memory_candidate_inventory_20260617.json` for this session-local processing pass. Do not copy this JSON into the wiki; use it only to build bounded markdown ledger rows.

## Next tranche order

1. Fix router/frontmatter validity before reindexing.
2. Build provenance-ledger tranche 001 from high-signal, low-secret rows across source classes.
3. Add research comparator lanes only where they discipline the wording; do not treat external papers as owner doctrine.
4. Wire pages into front doors and verify via wiki probe plus CocoIndex retrieval.
