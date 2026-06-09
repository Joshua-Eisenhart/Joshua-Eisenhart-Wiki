---
title: v3.3→v3.4 Cutover — Per-Hit R6 Classification
created: 2026-04-29
type: cutover-record
tags: [wizard, cutover, v3.4, r6, classification]
---

# v3.3→v3.4 Cutover — Per-Hit R6 Classification

This file closes Final-Audit Item 6 (P3) by recording, per-hit, how each `v3-3` / `v3_3` / `v3.3` reference in the original Systems sweep was classified and acted on. R6 (Zhuangzi's versioned-cohort reading) is the audit's term for distinguishing live-pointer vs versioned-artifact vs negative-directive vs provenance-note.

## Classification key

- **L** — live-pointer to the active packet (must bump)
- **V** — versioned-cohort artifact (do not rename; provenance bound to original cohort)
- **N** — negative-directive (do not flip; flipping inverts intent)
- **P** — provenance / source-hierarchy reference (intentional historical mention; keep)

## Per-hit table

| File | Line(s) | Hits | Class | Action |
|---|---|---|---|---|
| `~/wiki/wizard/01-wizard-general.md` | 16, 17, 37, 189 | 4 | L | bumped to v3.4 |
| `~/wiki/wizard/02-mmm-reference.md` | 12, 20, 21, 29, 30, 31, 32, 33, 34, 42, 43, 49, 55 | 15 (13 raw + 2 prose) | L | bumped to v3.4 |
| `~/wiki/wizard/03-followups-and-compositions.md` | 14 | 1 | L | bumped to v3.4 (prior edit, owner or earlier turn) |
| `~/wiki/wizard/harness-consolidated/README.md` | 9 | 1 | L | bumped to v3.4 |
| `~/wiki/wizard/harness-consolidated/README_CONSOLIDATED_BY_WIZARD.md` | 15 | 1 | L | bumped to v3.4 |
| `~/wiki/harness/README.md` | 11 | 1 | L | bumped to v3.4 |
| `~/Desktop/Codex Ratchet/AGENTS.md` | 35, 37 | 2 | L | bumped to v3.4 (Codex authority file; under unify cohort policy) |
| `~/Desktop/Codex Ratchet/AGENTS.md` | 180 | 1 | N | generalized: "v3.3 Wizard packets" → "Wizard packets" (preserves negative-directive intent without aging) |
| `~/Desktop/Codex Ratchet/system_v5/ops/WIKI_STEWARD.md` | 31 | 1 | L | bumped to v3.4 |
| `~/Desktop/Codex Ratchet/system_v5/docs/plans/plans/2026-04-29-wizard-runtime-adapter-cleanup.md` | 13, 15, 16, 35 | 3+ | L (×3) + restructure | bumped + section restructured to name v3.4 active, v3.3 archive |
| `~/Desktop/Codex Ratchet/AGENTS.md` (route-truth doctrine + header template) | 93, 94, 97, 113 | 4 | L | bumped: `future-only` → `simulated` (Wave 8 A1 scout surfaced; D3 follow-up executed; v3.4 retired vocabulary aligned with wiki AGENTS.md) |
| `~/wiki/wizard/validation/WIZARD_OUTPUT_SMOKE_TEST_v3_3.md` | filename + body | n/a | V | not renamed (cohort artifact bound to v3.3 validation run) |
| `~/wiki/wizard/validation/WIZARD_VOICE_FOLLOWUP_COLLAPSE_TEST_v3_3.md` | filename + body | n/a | V | not renamed |
| `~/wiki/wizard/validation/WIZARD_VOICE_PRESERVATION_AUDIT_v3_3.md` | filename + body | n/a | V | not renamed |
| `~/wiki/wizard/packet-v3-4-current/README_FIRST_v3_4.md` | 53, 54, 61 | 3 | P | kept as predecessor reference (source-hierarchy, "what changed from v3.3") |
| `~/wiki/wizard/README.md` | 15, 78 | 2 | P | kept as predecessor pointers explicitly demoted in-line ("Reference only; use v3.4 for boot") |
| `~/wiki/wizard/01-wizard-general.md` | 133 | 1 | P | kept as v3.3-label retirement statement (Orwell-pass: keeps the deprecation legible) |
| `~/Desktop/Codex Ratchet/MMM_WIZARD_CLEAN_SYSTEM_PACKET_v3_3/` (dir + zip + sha256) | n/a | n/a | V | retained as archive at repo root; not deleted |

## Cohort policy applied

**Unify at v3.4** — single cohort across Claude / Codex / Hermes consumer surfaces. Wiki and repo both read the v3.4 packet on the live boot path. v3.3 retained as archive/provenance.

## Out-of-scope for this cutover

- Hermes consumer boot path: not audited this turn. Council Reviewer A flagged as M1 missing item; carry forward.
- Cold-boot probes of Codex / Hermes: deferred (Claude cannot spawn those CLIs from this seat). Owner-run probe is the closing test.
- Validation cohort `_v3_4.md` siblings: deferred. Build only if owner wants v3.4-cohort validation runs to mirror the v3.3-cohort artifacts.

## v3.4 → v3.5 cohort jump (2026-04-30)

Owner introduced v3.5 ("two-doc simple") which retires the entire mmm/mini-MMM/registry/adapter tree. Cohort-rule application:

- **L (live pointers):** wiki README, 00-read-first, AGENTS.md rewritten to point at v3.5 two docs. Repo AGENTS.md L33-40 boot rule rewritten to v3.5 (drop mmm/main/ tree references). Repo AGENTS.md output-shape header rewritten to v3.5 telemetry shape.
- **V (versioned cohort artifacts pinned):** v3.4 packet directory + repo `MMM_WIZARD_CLEAN_SYSTEM_PACKET_v3_4/` retained as archive. v3.3 packet retained as deeper archive. v3.4 validation cohort `_v3_3.md` files still pinned.
- **N (negative directive):** repo AGENTS.md L180 (already generalized to "Wizard packets") stays generalized — no version-specific flip needed.
- **P (provenance / predecessor):** wiki README and 00-read-first carry brief predecessor pointers to v3.4 packet for archive reference.
- **Pending follow-ups carried forward from v3.4:** wiki secondary docs `01-wizard-general.md`, `02-mmm-reference.md`, `03-followups-and-compositions.md` describe the now-retired packet model (registry, mini-MMMs, follow-up subsystem). Under v3.5 §2 ("only two active docs") they should be retired or shrunk to redirect stubs. Not done this turn — owner-call.
- **Hermes side:** still on parallel route_status enum (zero `simulated` adoption). v3.5 doctrine is consistent with v3.4 on route truth, so the prior L3 follow-up (Hermes vocabulary migration) still stands.
