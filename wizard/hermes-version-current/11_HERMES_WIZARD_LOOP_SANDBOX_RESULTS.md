---
title: Hermes Wizard Loop Sandbox Results
created: 2026-05-06
updated: 2026-05-06
type: runtime_evidence_summary
runtime: hermes
status: sandbox-evidence
---

# Hermes Wizard Loop Sandbox Results

## Purpose

Record the current sandbox evidence for Hermes-native Wizard loops without promoting temp artifacts into live Hermes runtime authority.

## Source bundle

Sandbox root:

`/tmp/hermes-loop-integration-20260505-135517/`

Aggregate report:

`/tmp/hermes-loop-integration-20260505-135517/artifacts/aggregate_loop_report.md`

Reusable profile runner:

`/tmp/hermes-loop-integration-20260505-135517/bin/hermes_wizard_loop_cli.py`

Latest profile-driven receipt:

`/tmp/hermes-loop-integration-20260505-135517/loop-runs/loop-smoke-0012/receipt.json`

First target profile:

`/tmp/hermes-loop-integration-20260505-135517/profiles/dr_refinement_micro_01.json`

## Current truth

- Whole wiki retrieval is useful as broad corpus / KB input.
- Whole wiki is not one authority surface.
- Authority/admission is per document by role, provenance, and evidence status.
- Scoped OpenKB/PageIndex-style structure-first artifacts can be used as diagnostic/context surfaces when scoped cleanly.
- TraceGuard-style evidence handles are usable now as an admission gate.
- Premortem is a required Failure barrier for consequential loop changes.
- Autoresearch/refinery output is candidate input until audited/admitted.
- Ouroboros/RLM-FORGE recursive runtime remains blocked/disabled until pinned dependency compatibility is proven in isolation.

## Loop outcomes

- `loop-smoke-0003` — ADMIT: broad wiki candidate classifier found 120 role/provenance-classified candidate docs with clean scoped OpenKB lint.
- `loop-smoke-0004` — HOLD: current Ouroboros checkout lacks `ouroboros.rlm`.
- `loop-smoke-0007` — ADMIT: read-only sandbox adapter passed after baseline tolerance hardening.
- `loop-smoke-0008` — HOLD: pinned Ouroboros dependency install blocked by approval policy; do not retry without approval.
- `loop-smoke-0009` — ADMIT: reusable read-only CLI runner passed on the bounded distinguishability target.
- `loop-smoke-0010` — ADMIT: explicit goal-policy join gate passed; negative checks for bad run id and broad claim ceiling behaved correctly.
- `loop-smoke-0011` — HOLD: overstrict claim-ceiling lint treated negative guard text as positive forbidden claim text.
- `loop-smoke-0012` — ADMIT: target-profile-driven runner passed with profile hash, per-profile paths, required z3 check, local claim ceiling, mapped premortem, protected-surface mutation manifest, and exact output surface.

## Admission shape now proven in sandbox

Each profile-driven loop carries:

- one target profile;
- role/provenance-scoped context candidates;
- premortem findings with mapped checks;
- classical baseline before target;
- target result predicates;
- load-bearing tool check, currently z3 for `dr_refinement_micro_01`;
- TraceGuard evidence handles;
- protected-surface before/after manifest;
- local claim ceiling;
- one `receipt.json`, one `summary.md`, and `raw/` evidence/logs.

## Corrected execution model

Boundedness is per packet/profile/admission path. It is not a one-at-a-time scheduling rule.

The next loop should batch multiple independent bounded profiles in parallel when prerequisites and file/state isolation allow it. Batch admission should not promote a broad scientific claim; it should report per-profile ADMIT/HOLD/BLOCK and preserve each profile's own claim ceiling.

## Non-adoptions

The following were not adopted into live Hermes:

- no live Hermes config change;
- no HERMES/SOUL rewrite;
- no MCP registration;
- no `ouroboros setup --runtime hermes`;
- no queue append;
- no recursive Ouroboros/RLM runtime enablement.

## Next safe loop

Build a separate Hermes docs/skills/MMM cleanup batch runner, not by widening the sim CLI:

- profiles: docs audit, skill audit, MMM saliency audit, Wizard format audit;
- mass parallel workers over isolated file clusters;
- premortem before and after autoresearch;
- autoresearch as candidate input only;
- one batch receipt, one human summary, raw worker evidence;
- no live writes unless a later explicit apply step is approved.

First read-only verification loop:

- runner: `/tmp/hermes-docs-cleanup-loop-20260506/bin/hermes_docs_cleanup_loop_cli.py`
- receipt: `/tmp/hermes-docs-cleanup-loop-20260506/runs/cleanup-loop-0001/receipt.json`
- status: `candidate_ready`
- scope: read-only verification over Hermes Wizard/wiki/skill/MMM cleanup surfaces
- wiki probe: clean
- autoresearch: candidate-only
- premortem: mapped findings, with future 3x3/MMM pilot hardening still open

## Related notes

- `10_HERMES_NEEDS_RECURSION_KB_PREMORTEM_INTEGRATION.md`
- `08_HERMES_WIZARD_RUN_HARNESS.md`
- `09_V4_1_LLM_COUNCIL_TOPOLOGY_CORRECTION.md`
- `sources/SOURCE_MAP.md`

Write mode: controller-maintained.
