---
title: Runtime State Status
created: 2026-05-22
updated: 2026-05-23
type: status-mirror
framing: current_snapshot_with_dated_inputs
generated_at: 2026-05-23T11:59:16Z
tags: [specs, codex-ratchet, runtime, queue, lint, never-run]
sources:
  - /Users/joshuaeisenhart/Codex-Ratchet/scripts/queue_claim.py
  - /Users/joshuaeisenhart/Codex-Ratchet/scripts/runner_queue_preflight.py
  - /Users/joshuaeisenhart/Codex-Ratchet/scripts/lint_sim_contract.py
  - /Users/joshuaeisenhart/Codex-Ratchet/scripts/never_run_cohort_report.py
  - /Users/joshuaeisenhart/Codex-Ratchet/system_v5/ops/blocked_reason_breakdown.json
  - /Users/joshuaeisenhart/Codex-Ratchet/system_v5/ops/never_run_cohorts.json
  - /Users/joshuaeisenhart/Codex-Ratchet/system_v5/ops/runner_taxonomy_unknowns.json
  - /Users/joshuaeisenhart/Codex-Ratchet/system_v5/ops/stage_gate.json
---

# Runtime State Status

This is a repo-runtime status mirror. It is not a concept page, not a sim result, and not an admission surface.

## Boundary

This page reports queue, runtime-preflight, static contract-lint, blocked-backlog, never-run, runner-taxonomy, and stage-gate state. It does not prove formal-scout claims, manifold admission, or theory content. Formal-scout and sim-estate counts live in their own mirrors.

## Source Freshness

- Mirror generated: `2026-05-23T11:59:16Z`
- `blocked_reason_breakdown.json` source mtime: `2026-05-23T04:57:01-0700`
- `never_run_cohorts.json` source mtime: `2026-05-23T04:59:01-0700`
- `runner_taxonomy_unknowns.json` source mtime: `2026-05-23T04:59:16-0700`
- `stage_gate.json` source mtime: `2026-04-30T17:40:54-0700`

Command-derived counts below were refreshed during this audit pass and should stay dated to this mirror generation time unless rerun.

## Queue Snapshot

Fresh `scripts/queue_claim.py counts`:

- `lane_A`: `0`
- `lane_B`: `0`
- `claimed`: `0`
- `blocked`: `840`
- `done`: `8868`

Fresh `scripts/runner_queue_preflight.py`:

- `all_pass`: `true`
- `active_stage`: `lego`
- atomic queue junk: `0` in root, lanes, claimed, blocked, and done
- blocked default queue rows: `0`
- blocked stage-gate priority rows: `0`
- findings: `[]`

## Runtime Heartbeat

Queue preflight is green, but the runtime is not broadly clear: `840` blocked records still exist. The previously admitted triple and sci-method micro lanes drained cleanly to `done`; treat those as bounded micro-fixture receipts, not as broader coupling or theory completion.

Do not describe this as a queue-preflight failure. The accurate split is:

- queue preflight: green
- recent strict-validating micro fixtures in this audit slice: `12` done (`6` triple, `6` sci-method)
- blocked backlog: red
- full runtime health: not closed until blocked backlog, full lint, and never-run debt are reconciled; worker-topology freshness needs its own cited runtime-audit receipt if discussed

## Blocked Backlog

From `system_v5/ops/blocked_reason_breakdown.json`:

- blocked rows: `840`
- wizard-admission blocked: `620`
- all wizard-admission blocked rows have subreasons: `true`

Blocked reasons:

- `wizard_admission_blocked`: `620`
- `stage_gate_blocked`: `88`
- `done_duplicate_conflict`: `72`
- `stale_atomic_claim_dead_pid_after_72h_review`: `57`
- `gate_denied`: `1`
- `receipt_validation_failed`: `1`
- `stale_claim`: `1`

Contract subreasons:

- `contract_clean_or_not_static_lint_blocked`: `822`
- `C4_divergence_log_missing`: `7`
- `C1_classification_missing`: `7`
- `C2_manifest_missing`: `5`
- `C3_depth_missing`: `5`
- `missing_sim_path`: `4`

Interpretation guard: `contract_clean_or_not_static_lint_blocked` is a fallback subreason for rows where the source exists and the static contract linter did not name a C-rule violation. It does not mean there are `822` simple source-contract repairs. It means the row remains blocked by admission, stage, duplicate, claim, or receipt state and needs the exact blocker inspected before any action.

## Actionability Partition

Read-only partition audit, no queue mutation:

- `wizard_admission_blocked`: `620` rows. Actionable only by choosing one exact row and inspecting its admission failure. Do not broad requeue.
- `stage_gate_blocked`: `88` rows / `80` unique sims. Mostly should remain blocked until exact prerequisite receipts exist. Current split: `60` `scientific_coupling`, `27` `default_late_stage`, and `1` blank stage claim.
- `done_duplicate_conflict`: `72` rows / `66` unique sims. Terminal unless doing explicit dedupe cleanup.
- `stale_atomic_claim_dead_pid_after_72h_review` plus `stale_claim`: `58` rows. Queue hygiene only, not research progress.
- `gate_denied`: `1` row. Needs exact gate/admission diagnostic.
- `receipt_validation_failed`: `1` row. Needs exact receipt-validation diagnostic.

Named C-rule debt inside blocked rows is much smaller than the fallback bucket: `7` C4 rows, `7` C1 rows, `5` C2 rows, and `5` C3 rows. The best narrow repair lane is one `wizard_admission_blocked` row with named C-rule debt, followed by exact lint/admission validation for that row. A second narrow diagnostic lane is one repeated `wizard_admission_blocked + contract_clean_or_not_static_lint_blocked` row, inspected with the actual Wizard admission checker.

Latest narrow repairs: three reviewed bridge/lego source files now expose top-level metadata matching their own emitted bounded results. A separate family-local scalarization formal scout was added after the broad-stress scout and validated as `formal_scout` only; it kills the tested simple/prototype scalarizations, keeps the section candidate section-only, and leaves scalar Phi0, final Xi, final tensor scaling, and final manifold admission blocked. This is micro-fixture/formal-scout evidence only; no claim should move beyond the stated claim ceilings.

## Contract Lint

Fresh full static AST pass over `system_v4/probes/sim_*.py`, excluding duplicate-space and `_archive_lane_c` paths:

- checked: `10497`
- violation total: `836`
- sims with violations: `615`
- mode: `parallel_static_ast_no_sim_execution`

Violation buckets:

- `C1_classification_missing`: `545`
- `C2_manifest_missing`: `139`
- `C3_depth_missing`: `84`
- `C4_divergence_log_missing`: `68`

## Never-Run Cohorts

Fresh `scripts/never_run_cohort_report.py`:

- never-run count: `3741`

Top families:

- `calibration`: `576`
- `coupling`: `361`
- `cvc5`: `334`
- `geometry`: `167`
- `gtower`: `100`
- `pure`: `74`
- `gap`: `65`
- `weyl`: `63`
- `hopf`: `58`
- `lego`: `50`

Buckets:

- `exploratory`: `2608`
- `core_ladder`: `1000`
- `framework_doctrine`: `133`

Never-run contract-rule counts:

- `contract_clean`: `3146`
- `C1_classification_missing`: `538`
- `C2_manifest_missing`: `129`
- `C3_depth_missing`: `75`
- `C4_divergence_log_missing`: `57`

Never-run interpretation guard: this is backlog and coverage debt, not proof of readiness or failure. `3146` never-run rows are contract-clean, but they still need admission and stage fit. Useful low-risk families exist, including isolated capability probes and micro tool/function probes, but they should be selected one at a time rather than pushed into a generic queue pile.

The current `never_run_cohorts.json` schema exposes `rows`, `family_counts`, `bucket_counts`, and `contract_rule_counts`; it no longer exposes the older verified-candidate marker fields in this mirror. Select exact rows from the machine report before queue movement.

## Runner Taxonomy Unknowns

From dated `system_v5/ops/runner_taxonomy_unknowns.json`:

- unknown rows: `50`

This source was refreshed in this pass. The current allowlist still covers all `50` unknown runner classes, so taxonomy drift is `0`; unknown classification remains review debt, not a current blocker for this checkpoint.

## Stage Gates And Admission

From dated `system_v5/ops/stage_gate.json`:

- `active_stage`: `lego`
- `allow_default_queue_late_stage`: `false`
- `allow_tier_d_launch`: `false`

The stage-gate note remains: tools -> tool integration -> all legos -> only then couplings.

## Regeneration Commands

```bash
/Users/joshuaeisenhart/.local/share/codex-ratchet/envs/main/bin/python3 scripts/queue_claim.py counts
/Users/joshuaeisenhart/.local/share/codex-ratchet/envs/main/bin/python3 scripts/runner_queue_preflight.py
/Users/joshuaeisenhart/.local/share/codex-ratchet/envs/main/bin/python3 scripts/blocked_reason_decompose.py
/Users/joshuaeisenhart/.local/share/codex-ratchet/envs/main/bin/python3 scripts/never_run_cohort_report.py
```

For full contract lint, use `scripts/lint_sim_contract.py` or an equivalent static AST wrapper. Do not treat this as sim execution.

## Claim Ceiling

This mirror supports runtime repair routing only. It does not prove repo cleanliness, runner readiness, formal-scout admission, or theory claims.
