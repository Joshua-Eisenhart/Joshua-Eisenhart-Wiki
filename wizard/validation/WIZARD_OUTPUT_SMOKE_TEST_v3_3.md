# Wizard Output Smoke Test v3.3

Date: 2026-04-29

## Purpose

Check whether the updated wiki front door can produce the intended Wizard output shape without turning into a worker log.

## Test Prompt

Use the Wizard harness to summarize the current consolidation task and propose the next useful follow-up menu.

## Expected Shape

1. Main Answer first.
2. Compact route truth in the header and Results boundary.
3. Distinct voice contributions when a voice wave ran; labels alone do not count.
4. Results with changed artifacts and blockers.
5. Follow-up as audited useful next prompts, mostly lanes and compositions.
6. No default Audit section.
7. Quality/audit score only in footer if used.

## Local Result

Status: runs.

Observed in this thread:

- Main answer stayed user-facing.
- Route truth distinguished Codex local work, Codex verifier subagent, and Claude Bridge advisory route.
- Follow-up remained optional and did not become a raw candidate bank.
- External Opus findings were inspected. Canon-compatible findings were repaired; non-canon drift was not accepted as law.

## Round 2 Repair Notes

The first Opus/Codex smoke audit found two output-surface seams:

- COMPACT had smaller boot/MMM payload but no explicit visible-output rule.
- The packet-native Wizard footer did not explain how it coexists with the global mesh closer.

Repairs applied:

- COMPACT now keeps the same ordered surface as FULL while suppressing optional sections more aggressively.
- Mesh-compatible local footer is documented as an adapter marker: `[lev://mesh]` may be inserted after the wizard emoji while preserving the Wizard footer fields.
- Follow-up docs now say the visible example is an audited subset drawn from five lanes plus four compositions, not a requirement to print exactly the example entries.

## Remaining Gate

This is a thread-level smoke test, not canonical behavior proof. Canonical behavior proof still requires same-task comparison across:

- no MMM;
- main MMM;
- exact mini-MMM;
- follow-up audit pass.
- voice/follow-up collapse test in `WIZARD_VOICE_FOLLOWUP_COLLAPSE_TEST_v3_3.md`.

## Regression Added

The smoke surface now rejects the specific failure where the answer proves route execution but gives no readable voices, or where Follow-up turns into route inspection instead of user-useful prompts.
