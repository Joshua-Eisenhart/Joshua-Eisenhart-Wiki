# Follow-Up Receipt

run_id: 20260504-155235
mode: REAL_ATTEMPT
wave: Follow-Up
parent_route_id: followup-parent
input_receipts: decision-receipt.md + failure-receipt.md
input_consumption_order: decision-receipt.md, then failure-receipt.md
model_request: gpt-5.5 low requested if runtime supports it
model_observed: parent runtime is gpt-5.5; child route metadata reported gpt-5.5; low-effort support not independently observable
artifact_surface: terminal summary written by controller
nested_visibility: parent consumed receipt file contents and received delegate_task child summaries/tool metadata only; raw nested transcripts were not visible

## Member routes

| route_id | label | status | concrete follow-up item | payoff | use_when | blocked_if | evidence_boundary |
|---|---|---:|---|---|---|---|---|
| followup-make | 🧭 Follow-up make | completed | Make the next terminal summary validator-gated and source-labeled: require one unique run directory, run `conformance/validate_hermes_wizard_run.py` against that exact directory, and label every substantive claim as `live-Hermes`, `fixture/receipt replay`, or `parent-reported`. | Converts narrative repair into executable evidence and prevents route/evidence overclaim. | Immediate narrow evidence-first Wizard repair/run. | No unique run dir, missing validator output, or unlabeled claims. | Validator output, single run-dir artifacts, explicitly labeled fixture/receipt replay, and parent-visible receipts only. |
| followup-scout-audit | 🧪 Follow-up scout/audit | completed | Gate the bounded proper Wizard smoke run behind read-only preflight: verify harness/validator path, name executable validation path, allocate one unique run dir, then run at most one Hermes-native Wizard smoke and validate that run dir. | Prevents repeat harden verdict for missing harness proof, ambiguous execution source, duplicate dirs, or unsupported nested claims. | Before any repair/run step claiming Wizard smoke evidence. | Validator cannot be found/invoked, unique run dir cannot be reserved, or evidence categories cannot be separated. | Terminal summary, validator output, run-dir artifacts, and receipts only; no raw nested transcript visibility. |
| followup-orwell-factory | ✂️ Orwell + 🏭 Factory formatting | completed | Add a Terminal Provenance Strip: `run=<unique_run_dir> | validator=conformance/validate_hermes_wizard_run.py | route_label_source=<live|receipt|parent-reported> | evidence=<paths-or-receipts-only>`. | Makes the v4.1 terminal artifact honest, attractive, scannable, and validation-oriented. | Final terminal summary after evidence-first repair/run. | No unique run dir, no executable validation path, or unclear live-vs-receipt labels. | Decision/Failure receipts, validator path/output, unique run dir, and controller-observed artifacts only. |

## Verdict

proceed_with_hardened_follow_up

## Chosen follow-ups

1. Require validator-gated terminal summary against one unique run directory.
2. Require read-only preflight before smoke-run or repair claims.
3. Require terminal provenance strip and explicit evidence-source labels.

## Visual formatting recommendation

Use a compact terminal-first layout:

- Provenance strip at top.
- Short Status / Validator / Evidence Labels block.
- Route table with route_id, source, status, claim, evidence.
- Final Evidence Boundary block.
- Use semantic emojis without hiding provenance or validation status.

## Evidence boundary

This Follow-Up parent consumed the Decision and Failure receipts and spawned three delegate_task member routes. The parent received member summaries and metadata only. This receipt does not claim raw nested transcript visibility, hidden route logs, or verified low effort.
