# Wiki Wizard v4.3 MMM Maintenance Template

Purpose: self-contained on-demand / cron prompt template for bounded Hermes Wizard v4.3 maintenance ticks that actually preload MMM salience before task rules and improve MMM surfaces without pretending v4.3 is a replacement runtime.

Status: active v4.3 maintenance template; controller-maintained.

Use this when:
- the user asks to run Wizard v4.3 maintenance;
- a scheduled finite steward tick invokes this note;
- a task touches object-preservation, proxy/salience drift, MMM improvement, memory offload, or wiki/Hermes maintenance.

Do not use this to:
- create recursive cron jobs from inside a tick;
- mutate Codex Ratchet repo state;
- claim v4.2 FULL council coverage without receipt-backed v4.2 obligations;
- promote candidate MMMs into canonical boot salience without dedup and conformance.

## Version boundary

- **v4.3** is the visible maintenance/object-preservation surface for this template.
- v4.3 runs the repo-held object-preservation guard and keeps the primary object alive.
- legacy v4.2 packet references are provenance; do not run v4.2 as current; v4.3 adds object-preservation / maintenance guardrails and does not replace topology.
- Say that boundary plainly. Do not call v4.3 a full replacement runtime.

## MMM preload block — must appear before task rules

```text
MMM_PRELOAD_BEFORE_TASK_RULES=true
MMM_L0_REF=voice-mini-mmm-saliency-calibration/references/wizard-3x3-mmm-saliency-alignment.md
MMM_SHARED_L0=constraint before cause; support/carrier before object; probe-relative distinguishability before identity; evidence handle before claim promotion; survivor sets before consensus; finite receipts before completed-infinity language; negative evidence and graveyard states are signal.
MMM_V4_3_REF=/Users/joshuaeisenhart/wiki/wizard/packet-v4-2-current/mmm/SALIENCY_TRANCHE_02_V4_3_OBJECT_PRESERVATION_MAINTENANCE_CANDIDATE.md
MMM_PACKET_REFS=/Users/joshuaeisenhart/wiki/wizard/packet-v4-2-current/mmm/SALIENCY_TRANCHE_01_CANDIDATE.md;/Users/joshuaeisenhart/wiki/wizard/packet-v4-2-current/mmm/mini/MEMBER_MINI_MMM_REGISTRY_v4_2.md
MMM_RECEIPT_REQUIRED=true
```

Every worker or controller-local receipt claiming MMM-backed status must name:

```yaml
mmm_l0_ref:
mmm_v4_3_ref:
mmm_council_or_function_ref:
saliency_preload_before_rules: true
loaded_required_slices:
which_loaded_slice_changed_output:
claim_boundary:
output_artifact:
```

If those fields are absent, mark the route `not_MMM_backed`, `blocked`, or `controller_local`.

## Self-contained tick prompt

Copy/paste or use as a cron prompt body:

```text
Run one bounded Hermes Wizard v4.3 MMM maintenance tick.

First load skills: hermes-wizard, hermes-wizard-v4-3-object-preservation, harness-bootstrap, memory-offload-to-wiki-harness, wiki-maintenance-and-harness, voice-mini-mmm-saliency-calibration.

Read the Hermes spine front door and current control surfaces:
- /Users/joshuaeisenhart/wiki/hermes-current/read-first.md
- /Users/joshuaeisenhart/wiki/hermes-current/current-vs-legacy.md
- /Users/joshuaeisenhart/wiki/hermes-current/skills-and-agent-rules.md
- /Users/joshuaeisenhart/wiki/hermes-current/active-plans.md
- /Users/joshuaeisenhart/wiki/hermes-current/wiki-wizard-v4-3-mmm-maintenance-template.md
- /Users/joshuaeisenhart/wiki/hermes-current/wiki-wizard-v4-3-object-preservation-guard.md
- /Users/joshuaeisenhart/wiki/hermes-current/wiki-wizard-v4-2-autoloop-control.md only as legacy/topology bridge when needed.

Before task-specific rules, preload MMM salience:
- L0: constraint before cause; support/carrier before object; evidence handle before claim promotion; survivor sets before consensus.
- v4.3 object-preservation candidate: /Users/joshuaeisenhart/wiki/wizard/packet-v4-2-current/mmm/SALIENCY_TRANCHE_02_V4_3_OBJECT_PRESERVATION_MAINTENANCE_CANDIDATE.md
- Required functional slices for wiki/source corrections: `v43.object_card_guard`, `v43.maintenance_route_truth`, `v43.wiki_processing_router`, and `v43.mmm_admission_gate` as relevant.
- Candidate/source packet: /Users/joshuaeisenhart/wiki/wizard/packet-v4-2-current/mmm/SALIENCY_TRANCHE_01_CANDIDATE.md
- Mini registry: /Users/joshuaeisenhart/wiki/wizard/packet-v4-2-current/mmm/mini/MEMBER_MINI_MMM_REGISTRY_v4_2.md

Run preflight checks:
1. Run wiki_probe.py and save a /tmp preflight receipt.
2. Run the repo v4.3 validator from `/Users/joshuaeisenhart/Codex-Ratchet`:
   python3 scripts/wizard_v4_3_object_preservation.py validate --input /Users/joshuaeisenhart/wiki/wizard/hermes-version-current/packets/hermes_v4_3_retrocausal_object_card.json
3. Run the positive-field drift scan on the v4.3 object card: PEPS3D must not appear in plain_language_definition, allowed_operations, or adapter_policy.

Then perform exactly one bounded tranche, chosen in this order:
1. If preflight is dirty, repair only the failing preflight/control surface.
2. If the user supplied a source/model correction that the wiki does not yet route, process one bounded wiki receiver page first; preserve owner thesis, claim ceiling, and links before discussing future sims.
3. If MMM candidate admission is the target, dedup candidate terms against FULL_MMM_v4_2.md, COMPACT_MMM_v4_2.md, and MEMBER_MINI_MMM_REGISTRY_v4_2.md; do not promote to canonical without conformance.
4. If memory pressure is the target, snapshot live MEMORY.md and USER.md to hermes-current before compression.
5. If wiki routing is the target, patch one front-door/control surface and verify.

Use Decision -> Failure -> Follow-Up barriers with MMM preload receipts. Native delegate_task may be attempted, but if blocked, record the exact blocker and use external read-only workers only if available. Do not hide blocked routes.

Verification before final response:
- inspect touched files directly;
- rerun wiki_probe.py;
- rerun v4.3 validator if the object card or v4.3 MMM guard changed;
- run semantic scans for stale positive PEPS3D drift and for any false v4.3-as-replacement-runtime wording;
- append one log entry or receipt with changed files, route truth, pre/post probes, MMM preload receipts, and next bounded tranche.

Final answer must say: changed state, verification, blocked/not-run routes, durable receipt path, cron status if relevant, and next bounded tranche. Do not claim v4.2 FULL or v4.3 replacement runtime.
```

## Default finite cron profile

If the user asks for a finite scheduled steward and gives no cadence, use the historical safe default unless they override it:

```yaml
schedule: every 45m
repeat: 8
workdir: /Users/joshuaeisenhart/wiki
toolsets: file, terminal, delegation, skills, cronjob
claim_ceiling: v4.3 object-preservation/MMM maintenance only
historical_job_id: 497a2eaaa178
historical_created: 2026-06-06
current_scheduler_status: not_live_as_of_2026-06-13_cronjob_list_count_0
new_job_requires: explicit scheduler creation receipt
deliver: origin
```

Cron ticks must not create, edit, remove, or recursively schedule cron jobs.

## Related notes

- [[wiki-wizard-v4-3-object-preservation-guard]]
- [[wiki-wizard-v4-2-autoloop-control]]
- [[active-plans]]
- [[wizard-v4-3-maintenance-preflight-receipt-2026-06-06]]

Write mode: controller-maintained template/control surface.
