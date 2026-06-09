---
title: Hermes 3x3 MMM Pilot Results
created: 2026-05-06
updated: 2026-05-06
type: runtime_evidence_summary
runtime: hermes
status: sandbox-evidence
---

# Hermes 3x3 MMM Pilot Results

## Purpose

Record the first sandbox pilot for Hermes Wizard's 3 councils x 3 subcouncils MMM-backed behavior.

This is evidence of a bounded pilot, not live runtime adoption and not proof of raw nested worker traces beyond the visible receipt files.

## Source bundle

Sandbox root:

`/tmp/hermes-3x3-mmm-pilot-20260506/`

Pilot summary:

`/tmp/hermes-3x3-mmm-pilot-20260506/summary.md`

Pilot receipt:

`/tmp/hermes-3x3-mmm-pilot-20260506/receipt.json`

Audit report:

`/tmp/hermes-3x3-mmm-pilot-20260506/audit/audit_report.json`

## Pilot shape

The pilot created:

- one shared L0 nominalist / constraint MMM body;
- nine subcouncil MMM bodies;
- one bounded task: choose the next safest concrete Hermes cleanup move;
- nine delegate workers, one per subcouncil;
- one receipt JSON per worker;
- one deterministic audit over receipt shape, preload fields, overclaim, salience hits, and output similarity.

## Status

`PASS` as sandbox pilot.

Proof strip:

`Hermes Wizard MMM Pilot | councils:3/3 | subcouncils:9/9 receipt-backed | mass_workers:9 completed/0 blocked | MMM:preload-receipted | audit:distinct/no-overclaim | boundary:sandbox pilot, not full runtime adoption`

## Audit result

- receipts: 9/9
- schema/preload errors: 0
- overclaims: 0
- high-similarity collapse pairs: 0
- salience gaps: 0

## Council outputs

Decision:

- Scope/Target: next move should stay bounded to read-only verification receipts; scope excludes Codex TUI sim work and live config mutation.
- Evidence/Context: create/read evidence receipt bundles with source path, observed state, provenance, authority class, uncertainty, and missing handles.
- Action/Route: run a read-only wiki/skill link audit, compare expected 3x3 references against receipts, record mismatches, then stop.

Failure:

- Premortem: hidden failure is assuming stale roots are gone everywhere; run read-only regression probes and promote only evidence-handled discrepancies.
- Falsifier/Route Truth: kill unsupported parent-reported cleanup claims lacking raw verified evidence; survivor-set report stops at receipts.
- Regression/Safety: freeze protected surfaces and record wiki probe / skill pointer checks; route any change through explicit permission.

Follow-Up:

- Option Generator: offer reversible choices, not mutation; audit receipts, scout stale refs, or hand off a read-only checklist.
- Scout/Autoresearch: verify by receipts; keep/discard stale candidates by evidence; stop at first unreceipted claim.
- Audit/Selector: select missing-receipt or stale-pointer checks; mark duplicates/no_delta; block proof beyond existing handles.

## Interpretation

This pilot supports a narrower claim:

- Hermes can run a 9-subcouncil MMM-backed sandbox pilot with current receipt files and visibly distinct subcouncil outputs.

It does not yet prove:

- durable fresh-session calibration;
- production-grade MMM bodies;
- automatic Wizard runtime adoption;
- raw nested worker transcript visibility;
- live HERMES/SOUL integration.

## Next safe step

Turn the temp L0 and subcouncil bodies into durable draft MMM body files or skill references, then run a fresh-session calibration battery:

1. no-MMM baseline;
2. L0-only;
3. L0 + council body;
4. L0 + council + subcouncil body;
5. independent collapse/contamination/overclaim audit.

Do not claim full MMM-backed Wizard until fresh-session calibration passes.

## Related notes

- `11_HERMES_WIZARD_LOOP_SANDBOX_RESULTS.md`
- `09_V4_1_LLM_COUNCIL_TOPOLOGY_CORRECTION.md`
- Hermes skill reference: `voice-mini-mmm-saliency-calibration/references/wizard-3x3-mmm-saliency-alignment.md`
- Hermes skill reference: `hermes-wizard/references/hermes-wizard-3x3-loop-and-pretty-format.md`

Write mode: controller-maintained.
