---
title: Hermes Wizard Manifest
created: 2026-05-04
updated: 2026-05-16
type: manifest
runtime: hermes
---

# Manifest

## Files

- `README.md` — folder front door.
- `00_READ_FIRST.md` — boot and authority boundaries.
- `01_RUNTIME_CONTRACT.md` — Hermes-native Wizard runtime contract.
- `02_TOOL_ADVANTAGE_MAP.md` — Hermes tools mapped to Wizard jobs.
- `03_CODEX_PROCESS_IMPORT_AUDIT.md` — what to import/adapt/reject from Codex Wizard process.
- `04_SKILL_IMPORT_AUDIT.md` — audited Hermes skills that carry Codex/Wizard/controller behavior.
- `05_SOURCE_AND_LIFT_BOUNDARY.md` — source/lift separation and anti-copy rule.
- `06_ADOPTION_PLAN.md` — low-coupling path from docs to skill to runtime proof.
- `07_CODEX_LOCAL_SKILL_STACK_AUDIT.md` — corrected audit of `/Users/joshuaeisenhart/.codex/skills/`, including Wizard, premortem, Claude Bridge, thread, automation, maintenance, and A2/A1/refinery skills.
- `08_HERMES_WIZARD_RUN_HARNESS.md` — live run harness defining modes, wave topology, wide intra-council fanout obligations, receipt fields, human-load visual template, and validator.
- `09_V4_1_LLM_COUNCIL_TOPOLOGY_CORRECTION.md` — correction that v4.1 means three distinct LLM councils in sequence (Decision -> Failure -> Follow-Up) with wide parallel work inside each; the earlier Hermes minimal run proved only partial sequential topology.
- `schemas/HERMES_WIZARD_RECEIPT_SCHEMA.md` — compact receipt schema.
- `templates/task-card.yaml` — bounded worker/task template.
- `templates/worker-receipt.yaml` — receipt template.
- `conformance/VALIDATION_CHECKLIST.md` — acceptance checks for a Hermes Wizard run.
- `conformance/validate_hermes_wizard_run.py` — small executable validator for bounded Hermes Wizard run directories.
- `conformance/validate_hermes_wizard_wide_run.py` — stricter executable validator for `REAL_ATTEMPT_PARTIAL` wide-council fixtures; rejects hidden one-parent-per-council overclaims and requires evidence-tier/graph/negative-fixture markers.
- `10_HERMES_NEEDS_RECURSION_KB_PREMORTEM_INTEGRATION.md` — scout/integration plan for RLM-FORGE, Ouroboros, PageIndex, OpenKB, and stronger premortem integration into Hermes Wizard.
- `11_HERMES_WIZARD_LOOP_SANDBOX_RESULTS.md` — sandbox evidence summary for loop-smoke 0003-0012, profile-driven runner status, blocked recursive runtime, and next batch-profile loop direction.
- `12_HERMES_3X3_MMM_PILOT_RESULTS.md` — sandbox evidence summary for the first 9-subcouncil MMM-backed pilot; 9/9 receipt-backed workers, no overclaims, no collapse pairs, and next fresh-session calibration boundary.
- `13_HERMES_WIZARD_V4_1_LOOP_HARNESS.md` — Hermes-native v4.1 loop harness design for bounded docs/skills/wiki/tools/goals work; self-generated next steps, option pre-runs, premortem, autoresearch, subagent/subsubagent receipt boundaries, convergence gate, and apply-gate rules.
- `14_HERMES_WIZARD_V4_2_NATIVE_LOOP_BRIDGE.md` — Hermes-native bridge for current Wizard v4.2 loop work; maps v4.2 topology to Hermes action classes, external model pressure, premortem dispositions, wiki alignment receipts, and stop conditions.
- `15_HERMES_WIZARD_V4_3_OBJECT_PRESERVATION.md` — Hermes-native v4.3 object-preservation guard; runs the repo validator as a preflight over v4.2 councils. Hermes-authored packet lives in `packets/hermes_v4_3_retrocausal_object_card.json`.
- `packets/hermes_v4_3_retrocausal_object_card.json` — Hermes-owned v4.3 primary object card, validated by the repo guard (not a fork).
- `sources/SOURCE_MAP.md` — source files consulted and their role.

## Status labels for this folder

- `drafted`: file exists and has coherent content.
- `reviewed`: controller reread and corrected it against sources.
- `proved`: a bounded runtime proof used it successfully.
- `adopted`: the matching skill or HERMES/SOUL pointer was intentionally promoted.
- `deprecated`: kept for provenance, not current steering.

Current folder status: `drafted`.

## Non-goals

- no full universal packet copy
- no default high-fanout Codex Max Assembly
- no forced model-family quorum
- no global HERMES/SOUL rewrite
- no pretending memory/session recall is current execution evidence
