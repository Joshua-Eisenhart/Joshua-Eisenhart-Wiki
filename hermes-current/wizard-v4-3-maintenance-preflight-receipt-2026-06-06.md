---
title: Wizard v4.3 Maintenance Preflight Receipt 2026-06-06
created: 2026-06-06
updated: 2026-06-06
type: maintenance-receipt
status: v4-3-object-preservation-preflight-plus-control-refresh
claim_ceiling: object-preservation preflight and controller/tool-backed maintenance tranche only; not a full Wizard v4.2 council run
---

# Wizard v4.3 Maintenance Preflight Receipt — 2026-06-06

## Why this exists

User asked: `wizard 4.3 . go on` after the prior maintenance correction. This receipt records the bounded continuation: run the v4.3 object-preservation guard, use it as a preflight against proxy drift, then refresh the current wiki/Wizard maintenance control surface without pretending v4.3 is the runtime.

## Route truth

```text
mode: v4.3-object-preservation-preflight + maintenance-governor
wizard_status: PARTIAL / controller-tool-backed
v4.3_status: PASS against repo validator
v4.2_council_claim: not claimed
subagents: not run
multimodel_pressure: not run
MMM_preload_receipts: not run
reason: v4.3 is a preflight guard over the object card; this tranche patched shared wiki/control surfaces serially
```

## Authority and frame loaded

- `hermes-wizard`, `hermes-wizard-v4-3-object-preservation`, `harness-bootstrap`, `memory-offload-to-wiki-harness`, and `wiki-maintenance-and-harness` skills loaded.
- Hermes spine sampled/read: `read-first.md`, `about-me-and-how-to-work-with-me.md`, `active-intentions.md`, `environment-and-rules.md`, `current-vs-legacy.md`, `skills-and-agent-rules.md`, `active-plans.md`, and `hermes-memory-offload.md`.
- Wizard surfaces sampled/read: `wizard/hermes-version-current/README.md`, `00_READ_FIRST.md`, `15_HERMES_WIZARD_V4_3_OBJECT_PRESERVATION.md`, `16_HERMES_WIZARD_MAINTENANCE_GOVERNOR.md`, receipt schema, validation checklist, and the Hermes v4.3 packet.
- Repo authority stat/read verified: `~/Desktop/Codex Ratchet/system_v5/docs/WIZARD_V4_3_PRIMARY_OBJECT_PRESERVATION_SPEC_20260526.md` and `~/Desktop/Codex Ratchet/scripts/wizard_v4_3_object_preservation.py`.

## v4.3 guard receipts

Run from `/Users/joshuaeisenhart/Desktop/Codex Ratchet` with the repo validator as sole authority:

- Initial validate of Hermes packet:
  - command: `python3 scripts/wizard_v4_3_object_preservation.py validate --input /Users/joshuaeisenhart/wiki/wizard/hermes-version-current/packets/hermes_v4_3_retrocausal_object_card.json`
  - output: `/tmp/v43_validate_20260606.json`
  - result: `ok=true`, `errors=0`
  - sha256: `d80936e4424b21865b661cf9d6a4cd34c0cb5bfcff19fb6f2495981273152877`
- Selftest negative controls:
  - output: `/tmp/v43_selftest_20260606.json`
  - result: `ok=true`
  - sha256: `affafb63b2732b34c41c61c4674e07c50f7627adb542aa0dc8255676be42daa2`
- Full loop smoke:
  - output: `/tmp/v43_loop_20260606.json`
  - result: `ok=true`, `loops=1`, failed cases `0`
  - sha256: `67ed37c28e5b4f21cea82bf87ab081a16b9ff384fa0f3ad50fa1064e0affb2`
- Carrier-drift patch and revalidation:
  - patched positive primary-card PEPS3D mentions in `plain_language_definition`, `allowed_operations`, and `adapter_policy` to current nested PEPS2D/Hopfield / certified-carrier language.
  - retained PEPS3D only in negative/kill-control fields where it is explicitly rejected as a single-fused retired carrier.
  - packet sha256 after patch: `fe8c20c7124930a1c95e14287d8540d18437345d63a5dfd92558a30177992d39`
  - output: `/tmp/v43_validate_after_carrier_patch_20260606.json`
  - result: `ok=true`, `errors=0`
  - positive-field check: `plain_contains_PEPS3D=False`, `allowed_contains_PEPS3D=False`, `adapter_contains_PEPS3D=False`

Object preserved by the card: finite shell-indexed retrocausal possibility field. Not promoted: Axis0, FEP, scalar entropy, PEPS3D, Wolfram analogy, physics/cosmology/gravity claim, or any v4.2 FULL council status.

## Maintenance classification

The next safe tranche from the previous receipt was to audit whether the Wizard wiki-autoloop control surface was current and whether any maintenance cron job existed.

Findings:
- `cronjob(action='list')` returned `count=0`; there is no live scheduled maintenance job in this profile.
- `wiki-wizard-v4-2-autoloop-control.md` still carried an older embedded structural snapshot (`page_count=429`) even though the current preflight probe reports `page_count=438`.
- The v4.3 guard route is already present, but the control note needed a fresh local-preflight receipt and explicit scheduler truth so future agents do not infer a live cron from the historical job id.

## Patch cluster

Changed files in this tranche:

- `/Users/joshuaeisenhart/wiki/wizard/hermes-version-current/packets/hermes_v4_3_retrocausal_object_card.json` — removed residual positive-field PEPS3D carrier language from the v4.3 primary object card while preserving PEPS3D as an explicit forbidden/kill-control only.
- `/Users/joshuaeisenhart/wiki/hermes-current/wiki-wizard-v4-2-autoloop-control.md` — refreshed current operating truth with current wiki probe, v4.3 guard receipts, and scheduler state.
- `/Users/joshuaeisenhart/wiki/hermes-current/active-plans.md` — updated the memory snapshot pointer to the 2026-06-06 receipt and clarified that no live cron job is assumed.
- `/Users/joshuaeisenhart/wiki/hermes-current/wizard-v4-3-maintenance-preflight-receipt-2026-06-06.md` — this receipt.
- `/Users/joshuaeisenhart/wiki/log.md` — added one bounded log entry.

## Verification

Pre-edit wiki probe:

```text
path: /tmp/wiki_probe_pre_v43_maintenance_20260606.json
page_count: 438
broken_links: 0
missing_pages: 0
malformed_wikilinks: 0
stale_namespace_wikilinks: 0
sha256: 1cef82652002d804d1232e5b1b103cddb2fbfad6eacc43828fae85d470cf8ce0
```

Post-edit wiki probe:

```text
path: /tmp/wiki_probe_post_v43_maintenance_20260606.json
page_count: 438
broken_links: 0
missing_pages: 0
malformed_wikilinks: 0
stale_namespace_wikilinks: 0
sha256: 1cef82652002d804d1232e5b1b103cddb2fbfad6eacc43828fae85d470cf8ce0
```

Final probe after recording this receipt's post-edit section:

```text
path: /tmp/wiki_probe_final_v43_maintenance_20260606.json
page_count: 438
broken_links: 0
missing_pages: 0
malformed_wikilinks: 0
stale_namespace_wikilinks: 0
sha256: 1cef82652002d804d1232e5b1b103cddb2fbfad6eacc43828fae85d470cf8ce0
```

Final probe after the v4.3 carrier-drift packet patch:

```text
path: /tmp/wiki_probe_final3_v43_maintenance_20260606.json
page_count: 438
broken_links: 0
missing_pages: 0
malformed_wikilinks: 0
stale_namespace_wikilinks: 0
sha256: 1cef82652002d804d1232e5b1b103cddb2fbfad6eacc43828fae85d470cf8ce0
packet_sha256: fe8c20c7124930a1c95e14287d8540d18437345d63a5dfd92558a30177992d39
positive_peps3d: plain=False, allowed=False, adapter=False
```

Final probe matches the clean structural state. Passing v4.3 is not a substitute for the wiki probe; both receipts are recorded separately.

## Stop / next tranche

Stop after this v4.3 card/control-surface refresh unless the user explicitly asks for scheduling. Creating a recurring cron job remains a separate autonomous side effect and needs an explicit schedule or one-shot scope.

Next bounded tranche if continued: create a self-contained **on-demand maintenance prompt template** in the wiki, or, if the user names a cadence, create a finite cron job using that template.
