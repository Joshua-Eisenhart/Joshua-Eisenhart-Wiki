---
title: Current Docs Map Mirror
created: 2026-06-19
type: spec-mirror
status: draft_upgrade_pack
claim_ceiling: wiki routing / documentation upgrade only; no sim admission, no repo status promotion
tags: [codex-ratchet, docs-map, spec]
sources:
  - Codex-Ratchet/system_v5/docs/00_manifest.md
  - Codex-Ratchet/system_v5/docs/CURRENT_DOCS_MAP.md
---


# Current Docs Map Mirror — 2026-06-19

## Processing states

| State | Wiki handling |
|---|---|
| canonical | safe starting point for summaries, but repo exact-read still required |
| working | use with canonical docs, not alone |
| draft | useful structure, expect rewrites |
| audit | use to find gaps, not final doctrine |
| plan | intended work, not execution |
| source-note | provenance/source capture |
| intake-only | feeder material, not settled |
| archived | history/fact recovery only |

## Fast routes

| Need | Start with |
|---|---|
| system core | `CONSTRAINT_SURFACE_AND_PROCESS.md`, `OWNER_THESIS_AND_COSMOLOGY.md`, `SYSTEM_ARCHITECTURE_REFERENCE.md` |
| live status | `TIER_STATUS.md`, `SIM_CORRECTIONS_AND_CLASSIFICATIONS.md`, `SIM_SESSION_INDEX.md`, then current result/validator surfaces |
| math spine | `CONSTRAINT_ON_DISTINGUISHABILITY_FULL_MATH.md`, `ENGINE_MATH_REFERENCE.md`, `LADDERS_FENCES_ADMISSION_REFERENCE.md` |
| source provenance | `03_source_notes.md`, `09_research_inventory_and_foundations.md`, `LEGACY_CONTEXT_AND_GENEALOGY.md` |
| partially processed material | `new content/README.md`, specific digest, then promoted owner surface if it exists |

## Wiki repair pattern

When a concept page duplicates a repo docs-map role, replace the duplicate with a link to this mirror or to the repo exact path.

## Claim ceiling

This mirror does not settle topic ownership if the repo docs map has changed. Refresh from repo before calling it current.
