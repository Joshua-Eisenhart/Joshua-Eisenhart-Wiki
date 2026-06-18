# Hermes Native Controller System v0

status: runnable-v0
created: 2026-06-18
claim_ceiling: harness exists and selftest runs; not a full autonomous Hermes replacement; not canonical by process yet

## Purpose

This folder is the first runnable Hermes-owned controller system packet.

It exists because Hermes should not clone Claude or Codex controller files. Hermes can learn from them, but it must run through Hermes-native surfaces: profile memory, skills, `delegate_task`, cron/background routes, gateway routes, wiki receipts, Wizard v4.3 route truth, and compact human-facing answer scaffolds.

## What was built

- `hermes_controller_harness.py` — a small local Python harness that validates bounded controller scenarios and emits JSON receipts.
- `scenarios/*.json` — runnable packet/scenario inputs.
- `receipts/*.json` — machine receipts from actual runs.

## Imported lessons, not cloned systems

### From Codex

- Do not collapse `exists`, `runs`, `passes local rerun`, and `canonical by process`.
- Broad claims require claim/evidence/verification rows.
- Worker reports are audit inputs, not truth by themselves.

### From Claude

- Policy text is not enough if background or async completions render as raw log/status output.
- Measurement datasets need comparable schemas before they become promotion evidence.
- The output scaffold has to regenerate after background completions, not just at initial response time.

### Hermes-native additions

- Every route has Wizard v4.3 route fields: `action_class`, `execution_claim_state`, `proof_depth`, `receipt`, and `evidence_boundary`.
- Completed routes must cite a local receipt/artifact path.
- The harness can pass with blockers when the blocker is explicit; it must not turn blockers into success.
- The human-facing controller remains compact: route truth is available in receipts, while final answers summarize only what matters.

## Current status

Current checked status: **passes local rerun** for the built-in selftest and **pass_with_blockers** for the first real scenario.

Evidence:

- `receipts/selftest-2026-06-18.json` shows `ok: true` for the built-in selftest.
- `receipts/hermes-native-controller-v0-build-test-2026-06-18.json` shows verdict `pass_with_blockers`, `findings: []`, 3 completed routes, and 1 explicit blocker.
- The selftest proves one valid scenario passes and one intentionally overclaimed scenario fails.

This is not yet `canonical by process`: no fresh external audit, no broad Hermes CLI integration, no recurring cron/gateway path, and no default profile admission gate have been completed.

## Next admissible tests

1. Run a second scenario that includes a real blocked route and confirm the harness returns `pass_with_blockers`.
2. Add a fresh-context audit worker that tries to overclaim the harness and verifies the receipt boundaries.
3. If useful, wire a `/hermes-controller` style command or skill around this harness; do not do that until the v0 receipts stay clean.
