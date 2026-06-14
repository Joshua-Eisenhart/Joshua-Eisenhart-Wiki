---
title: Wizard v4.3 MMM Maintenance Run Receipt 2026-06-06
created: 2026-06-06
updated: 2026-06-06
type: maintenance-receipt
status: real-attempt-partial-v4-3-mmm-maintenance
claim_ceiling: v4.3 object-preservation/MMM maintenance only; not v4.2 FULL and not v4.3 replacement-runtime proof
---

# Wizard v4.3 MMM Maintenance Run Receipt — 2026-06-06

## Why this exists

User corrected the previous next-move framing: `1-3. but its 4.3. and mmms need to be used and improved`.

This run does the three requested moves under a v4.3 maintenance/object-preservation surface:

1. Create an on-demand v4.3 MMM maintenance template.
2. Create a finite scheduled steward job.
3. Run a receipt-backed Wizard attempt with MMM preloads and improve the MMM surfaces.

## Route truth

```text
mode: v4.3 MMM maintenance / REAL_ATTEMPT_PARTIAL
v4.3_status: object-preservation guard and maintenance surface used
v4.2_topology_status: retained council/runtime/output machinery; not replaced by v4.3
native_delegate_task: attempted, blocked before task work by invalid xAI key
external_worker: Claude Code Sonnet/high used for Decision, Failure, Follow-Up receipts
multimodel_pressure: not full; Claude Sonnet/high only plus native route block
MMM_preload: prompt-preloaded before task rules for external workers
cron: created finite job 497a2eaaa178
claim: not FULL; not v4.3 replacement-runtime proof
```

## MMM-backed worker receipts

Run manifest:
- `/Users/joshuaeisenhart/wiki/wizard/hermes-version-current/runs/20260606-v43-mmm-maintenance/manifest.md`

Native Hermes delegate attempt:
- Decision 3-way `delegate_task` attempted first.
- Result: all three failed before task work with invalid xAI key.
- Boundary: blocked route, not a council result.

External worker receipts:

- Decision Council / Claude Sonnet high:
  - prompt: `/tmp/v43_mmm_decision_prompt_20260606.txt`
  - raw JSON: `/tmp/v43_mmm_decision_worker_20260606.json`
  - durable receipt: `/Users/joshuaeisenhart/wiki/wizard/hermes-version-current/runs/20260606-v43-mmm-maintenance/decision-worker-claude-sonnet.md`
  - coverage: scope/target, evidence/context, action/route
  - observed model route: `claude-sonnet-4-6` with Haiku overhead in `modelUsage`
- Failure Council / Claude Sonnet high:
  - prompt: `/tmp/v43_mmm_failure_prompt_narrow_20260606.txt`
  - raw JSON: `/tmp/v43_mmm_failure_worker_20260606.json`
  - durable receipt: `/Users/joshuaeisenhart/wiki/wizard/hermes-version-current/runs/20260606-v43-mmm-maintenance/failure-worker-claude-sonnet.md`
  - coverage: premortem, falsifier/route truth, regression/safety
  - note: first broad read-enabled run timed out with no output; narrower no-tool prompt succeeded
- Follow-Up Council / Claude Sonnet high:
  - prompt: `/tmp/v43_mmm_followup_prompt_20260606.txt`
  - raw JSON: `/tmp/v43_mmm_followup_worker_20260606.json`
  - durable receipt: `/Users/joshuaeisenhart/wiki/wizard/hermes-version-current/runs/20260606-v43-mmm-maintenance/followup-worker-claude-sonnet.md`
  - coverage: option generator, scout/autoresearch, audit/selector

All three successful external worker prompts placed the MMM preload block before task rules and asked the worker to report `saliency_preload_before_rules: true` plus which MMM slice changed output.

## What changed

Created / patched:

- `/Users/joshuaeisenhart/wiki/hermes-current/wiki-wizard-v4-3-mmm-maintenance-template.md`
  - new self-contained on-demand/cron template;
  - includes explicit MMM preload block before task rules;
  - includes default finite cron profile and live job id after creation.
- `/Users/joshuaeisenhart/wiki/wizard/packet-v4-2-current/mmm/SALIENCY_TRANCHE_02_V4_3_OBJECT_PRESERVATION_MAINTENANCE_CANDIDATE.md`
  - new reference-only v4.3 MMM candidate overlay;
  - adds object-card guard, proxy-drift scanner, maintenance route-truth, and MMM admission-gate functional slices;
  - does not promote itself to canonical runtime.
- `/Users/joshuaeisenhart/wiki/wizard/packet-v4-2-current/PACKET_MANIFEST_v4_2.md`
  - registers the v4.3 candidate as reference-only.
- `/Users/joshuaeisenhart/wiki/hermes-current/current-vs-legacy.md`
  - says v4.3 is the v4.3 object-preservation/maintenance surface and any v4.2 topology bridge must be named explicitly.
- `/Users/joshuaeisenhart/wiki/hermes-current/active-plans.md`
  - points to the v4.3 MMM maintenance template and records finite cron job `497a2eaaa178`.
- `/Users/joshuaeisenhart/wiki/hermes-current/wiki-wizard-v4-2-autoloop-control.md`
  - links the v4.3 template and updates scheduler truth so the old v4.2 job is historical while the new v4.3 finite steward is live.

## Cron created

```text
job_id: 497a2eaaa178
name: Wizard v4.3 MMM maintenance steward — finite
schedule: every 45m
repeat: 8 times
deliver: origin
workdir: /Users/joshuaeisenhart/wiki
toolsets: file, terminal, delegation, skills, cronjob
skills: hermes-wizard; hermes-wizard-v4-3-object-preservation; harness-bootstrap; memory-offload-to-wiki-harness; wiki-maintenance-and-harness; voice-mini-mmm-saliency-calibration
next_run_at: 2026-06-06T17:06:23.811265-07:00
```

Cron prompt is self-contained and says not to recursively schedule cron jobs.

## Verification receipts

- Preflight wiki probe: `/tmp/wiki_probe_pre_v43_mmm_maintenance_20260606.json`
  - `page_count=438`, `broken_links=0`, `missing_pages=0`, `malformed_wikilinks=0`, `stale_namespace_wikilinks=0`
  - sha256 `1cef82652002d804d1232e5b1b103cddb2fbfad6eacc43828fae85d470cf8ce0`
- Mid-patch wiki probe: `/tmp/wiki_probe_mid_v43_mmm_maintenance_20260606.json`
  - same clean counts and sha256.
- v4.3 validator after MMM/control patches: `/tmp/v43_validate_mmm_maintenance_20260606.json`
  - `ok=true`, `errors=0`, sha256 `d80936e4424b21865b661cf9d6a4cd34c0cb5bfcff19fb6f2495981273152877`
- v4.2 packet conformance after adding reference-only candidate:
  - command: `python3 wizard/packet-v4-2-current/conformance/validate_v4_2_packet.py`
  - result: `v4.2 packet conformance: PASS`
  - `runtime_doc=WIZARD_v4_2.md sha256:c7ba2df556dd6572`, `council_parents=9`, `management_parents=5`

Final post-log probe and live scheduler verification:

- Final wiki probe: `/tmp/wiki_probe_final_v43_mmm_maintenance_20260606.json`
  - `page_count=438`, `broken_links=0`, `missing_pages=0`, `malformed_wikilinks=0`, `stale_namespace_wikilinks=0`
  - sha256 `1cef82652002d804d1232e5b1b103cddb2fbfad6eacc43828fae85d470cf8ce0`
- Final v4.3 validator: `/tmp/v43_validate_final_mmm_maintenance_20260606.json`
  - `ok=true`, `errors=0`, sha256 `d80936e4424b21865b661cf9d6a4cd34c0cb5bfcff19fb6f2495981273152877`
- Final v4.2 packet conformance:
  - `v4.2 packet conformance: PASS`
  - `runtime_doc=WIZARD_v4_2.md sha256:c7ba2df556dd6572`, `council_parents=9`, `management_parents=5`
- Cron list after creation:
  - `count=1`, job `497a2eaaa178`, enabled, scheduled, deliver `origin`, repeat `8 times`
- Semantic guard scan:
  - `positive_PE3D_plain=False`, `positive_PE3D_allowed=False`, `positive_PE3D_adapter=False`
  - `SALIENCY_TRANCHE_02` has `authority_status: reference-only` and a no-promotion rule.
  - `v4.3 is the runtime`, `v4.3 replaces v4.2`, and `packet-v4-3-current` appear only inside explicit negative/guard wording, not as positive claims.

Context-continuation closeout verification after the thread collapse:

- Closeout wiki probe: `/tmp/wiki_probe_close_v43_mmm_wiki_processing_20260606.json`
  - `page_count=439`, `index_header_count=439`, `missing_pages=0`, `orphans=0`, `broken_links=0`, `stubs=0`, `malformed_wikilinks=0`, `stale_namespace_wikilinks=0`
  - sha256 `49342744dd40a12b7fa5401160a5fb308d0f15fa90b6885b6075a0036778c679`
- Closeout v4.3 validator: `/tmp/v43_validate_close_v43_mmm_wiki_processing_20260606.json`
  - `ok=true`, `errors=0`, `warnings=0`
  - sha256 `4f110575af199c3d58b56555ec236d4eddfee5841c69f8c07249df847f5ea200`
- Closeout v4.2 packet conformance: `/tmp/v42_conformance_close_v43_mmm_wiki_processing_20260606.txt`
  - `v4.2 packet conformance: PASS`
  - `runtime_doc=WIZARD_v4_2.md sha256:c7ba2df556dd6572`, `council_parents=9`, `management_parents=5`
  - sha256 `ab1ccac1893bb867bec0fa04ccd4049ec4ebaa07b402c00265a8bf1702ac7665`
- Closeout semantic scans:
  - `/tmp/v43_semantic_scan_close_v43_mmm_wiki_processing_20260606.json`: no `PEPS3D` in `plain_language_definition`, `allowed_operations`, or `adapter_policy`; the only remaining `PEPS3D` hits are forbidden-substitution / kill-control language.
  - `/tmp/v43_replacement_runtime_wording_scan_close_20260606.json`: `9` targeted replacement-runtime wording hits, `0` unguarded; all are negative/guard/drift-rewrite contexts.
- Closeout cron list:
  - live job `497a2eaaa178` remains enabled/scheduled, schedule `every 45m`, repeat `8 times`, deliver `origin`, next run `2026-06-06T17:52:16.290609-07:00`.

## Open / blocked

- Native Hermes `delegate_task` remains blocked by invalid xAI key in this session; it was attempted and failed before task work.
- This is not full multimodel pressure. Claude Sonnet/high ran; native delegates failed; no Grok/Gemini/Opus lane was completed in this tranche.
- `SALIENCY_TRANCHE_02` is reference-only. Canonical MMM promotion remains blocked pending dedup, behavior comparison, and conformance.
- v4.3 is used as the maintenance/object-preservation surface. It is not asserted as a full replacement runtime.

## Next bounded tranche

The first scheduled tick should improve MMMs directly by deduping v4.3 candidate slice terms against `FULL_MMM_v4_2.md`, `COMPACT_MMM_v4_2.md`, `SALIENCY_TRANCHE_01_CANDIDATE.md`, and `mini/MEMBER_MINI_MMM_REGISTRY_v4_2.md`, then write a no-promotion admission report.
