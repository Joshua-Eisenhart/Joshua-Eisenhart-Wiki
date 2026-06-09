---
title: v3.4 → v3.3 Rollback Runbook
created: 2026-04-29
type: cutover-record
tags: [wizard, cutover, rollback, v3.4, v3.3]
---

# v3.4 → v3.3 Rollback Runbook

Reverse-edit map for the v3.3→v3.4 cutover (see `V3_4_CUTOVER_R6_CLASSIFICATION.md`). Source of truth for which lines flipped is the R6 classification table; this runbook names the inverse for each L-class hit.

## When to fire

Trigger on any of the following:

- Codex/Claude/Hermes cold-boot returns broken output sourced to v3.4 packet content (route registry, MMM, universal core, follow-up system).
- A v3.4 universal core or main-MMM bug is discovered post-cutover and a fix is more than one session away.
- Cohort policy reverses from `unify at v3.4` to `pin at v3.3` or `split cohorts`.
- Validation regression: a v3.3-cohort acceptance probe that previously passed now fails on v3.4 with no in-place fix.

Rollback is one-way per session. Do not partial-rollback (some files v3.3, some v3.4); that re-creates the M2 split-cohort state.

## Pre-rollback verification

1. v3.3 packet present at repo root: `ls /Users/joshuaeisenhart/Desktop/Codex Ratchet/MMM_WIZARD_CLEAN_SYSTEM_PACKET_v3_3/` shows `mmm/`, `universal_core/`, `validation/`, `definitions/`, manifest, README. Confirmed 2026-04-29.
2. Wiki `packet-v3-3-current/` directory still present at `/Users/joshuaeisenhart/wiki/wizard/packet-v3-3-current/`. Confirmed 2026-04-29.
3. ZIP + SHA256 present: `MMM_WIZARD_CLEAN_SYSTEM_PACKET_v3_3_DOWNLOADABLE.zip` + `.sha256` at repo root.
4. R6 classification file `V3_4_CUTOVER_R6_CLASSIFICATION.md` reachable for cross-reference.

If any prerequisite is missing, halt; rollback is not safe.

## Reverse edits — wiki

For each, replace `packet-v3-4-current` with `packet-v3-3-current`, `v3.4` with `v3.3`, `v3_4` with `v3_3` in the cited spans.

- `~/wiki/wizard/01-wizard-general.md` — lines 16, 17, 37, 189: revert `packet-v3-4-current/...` and `v3.4 Wizard harness` → v3.3 form.
- `~/wiki/wizard/02-mmm-reference.md` — lines 12, 20, 21, 29, 30, 31, 32, 33, 34, 42, 43, 49, 55: revert all `packet-v3-4-current/...` and `v3.4 packet` mentions → `packet-v3-3-current/...` / `v3.3 packet`.
- `~/wiki/wizard/03-followups-and-compositions.md` — line 14: `WIZARD_FOLLOWUP_SYSTEM_v3_4.md` → `WIZARD_FOLLOWUP_SYSTEM_v3_3.md`.
- `~/wiki/wizard/harness-consolidated/README.md` — line 9: `v3.4 Wizard work` → `v3.3 Wizard work`.
- `~/wiki/wizard/harness-consolidated/README_CONSOLIDATED_BY_WIZARD.md` — line 15: `v3.4 Wizard boot law` → `v3.3 Wizard boot law`.
- `~/wiki/harness/README.md` — line 11: `Wizard v3.4 work` → `Wizard v3.3 work`.

## Reverse edits — repo

- `~/Desktop/Codex Ratchet/AGENTS.md` — lines 35, 37: `MMM_WIZARD_CLEAN_SYSTEM_PACKET_v3_4/...` → `MMM_WIZARD_CLEAN_SYSTEM_PACKET_v3_3/...` (both main-thread and subagent boot paths).
- `~/Desktop/Codex Ratchet/AGENTS.md` — line 180 (N-class generalization): **leave as `Wizard packets`**. The generalization is durable independent of cohort; reverting to `v3.3 Wizard packets` would re-introduce the aging bug. Flagged as durable.
- `~/Desktop/Codex Ratchet/system_v5/ops/WIKI_STEWARD.md` — line 31: `v3.4 packet` → `v3.3 packet`.
- `~/Desktop/Codex Ratchet/system_v5/docs/plans/plans/2026-04-29-wizard-runtime-adapter-cleanup.md` — lines 13, 15, 16, 35: revert "v3.4 active / v3.3 archive" framing back to v3.3-active / no-v3.4 mention. The section restructure must also revert: re-merge the v3.4-active and v3.3-archive paragraphs into the prior v3.3-only form.

## Stays in place (do not touch)

- All V-class validation artifacts: `WIZARD_OUTPUT_SMOKE_TEST_v3_3.md`, `WIZARD_VOICE_FOLLOWUP_COLLAPSE_TEST_v3_3.md`, `WIZARD_VOICE_PRESERVATION_AUDIT_v3_3.md` — already cohort-bound to v3.3, no rename needed.
- All P-class predecessor pointers: `~/wiki/wizard/packet-v3-4-current/README_FIRST_v3_4.md` lines 53–54, 61; `~/wiki/wizard/README.md` lines 15, 78; `~/wiki/wizard/01-wizard-general.md` line 133 — these are source-hierarchy references that should stay (they will become forward-pointers to a v3.4 that is no longer live; that is acceptable provenance).
- N-class line 180 in `AGENTS.md` — generalized form is durable.
- v3.3 packet dir, zip, sha256 — already in place; no regeneration.

## Regeneration / re-staging

- v3.3 packet: **no regeneration needed** — directory at repo root is intact.
- Wiki `packet-v3-3-current/`: **no regeneration needed** — present and unmoved.
- v3.4 packet directory: leave at repo root and at wiki path. It becomes archive/forward-reference; do not delete (preserves the option to re-cut forward later and supports P-class pointers).
- R6 classification table (`V3_4_CUTOVER_R6_CLASSIFICATION.md`): keep in place as historical record of the (rolled-back) cutover. Add a one-line frontmatter or section note: "Status: rolled back YYYY-MM-DD; see V3_4_TO_V3_3_ROLLBACK_RUNBOOK.md and corresponding rollback receipt." Do not archive or delete; the record is load-bearing for any future re-cutover attempt.

## Consumer-restart steps

- **Claude (this surface):** start a new session in the repo. Boot reads `AGENTS.md` + `~/wiki/wizard/00-read-first.md` + `~/wiki/wizard/01-wizard-general.md` cold. After reverse-edits land, the rolled-back surface is what cold-boot will see. No manual cache flush needed; sessions are stateless across restart.
- **Codex:** exit current Codex CLI and cold-boot a fresh session in the repo. Codex authority file is `AGENTS.md`; it will re-read the v3.3 packet paths on next boot. Confirm with a one-shot probe: ask Codex to name the active packet path and verify the response cites `MMM_WIZARD_CLEAN_SYSTEM_PACKET_v3_3/`.
- **Hermes:** cold-boot Hermes session. Hermes consumer boot path was not audited at cutover (M1 carryover); rollback inherits that gap. Owner-run probe is the closing test — ask Hermes to name its active packet on first turn.

## Rollback receipts

Record after rollback completes:

1. New file `V3_4_TO_V3_3_ROLLBACK_RECEIPT_<date>.md` in `~/wiki/wizard/validation/` naming: trigger condition, files reverted (with line numbers), files intentionally left in place (V/P/N classes), durable-generalization decision (line 180), consumer cold-boot probe results.
2. Cross-link from `V3_4_CUTOVER_R6_CLASSIFICATION.md` and from this runbook to the rollback receipt.
3. Append entry to `~/wiki/projects/codex-ratchet/_steward_log.md` with one-line summary.
4. Status ladder note: rolled-back state earns `runs` only after a successful Claude + Codex (+ Hermes if probed) cold-boot returns coherent output sourced to v3.3 packet. Do not claim `passes local rerun` without a re-run of any v3.3-cohort validation probe.
