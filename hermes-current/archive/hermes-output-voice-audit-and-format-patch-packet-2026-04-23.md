# Hermes output voice-audit + format patch packet — 2026-04-23

## Bottom line
Claude-side output/formatting issues do carry over to Hermes. I ran Hermes-side voice audits, then patched the smallest control surfaces instead of rewriting the whole stack.

## What was audited
Voice audits written to:
- `/tmp/hermes_output_hume_orwell_audit_20260423.md`
- `/tmp/hermes_output_zhuangzi_popper_audit_20260423.md`
- `/tmp/hermes_output_runtime_factory_strategy_audit_20260423.md`

Main findings:
- Results were still too close to worker receipt law, which made replies read like logs.
- Follow-up rendering was under-specified in `HERMES.md` and over-specified/conflicted in the skill.
- Runtime/control bridge still needed an explicit bookkeeping/process-event ingress rule.
- `Systems`, `Factory`, and `Strategy` needed stronger task-card boundary fields so they stay distinct at runtime.
- Plurality/format proof is still only partial; current lint proves scaffold shape better than plurality survival.

## Patches landed
### `~/.hermes/HERMES.md`
Added or tightened:
- active/requested voices must visibly shape the main answer before Results/Follow-up
- Results are plain-English receipts for the user, not a serialized worker ledger
- Results should use 2–5 short bullets and keep worker headings/action-class jargon out of ordinary output
- bookkeeping/process-notification/wrapper-exit turns must update control state first and then render the full scaffold
- Follow-up must be numbered, single-spaced, concise, and concrete
- bundle lines may wrap once only to name ordered work, first packet, and artifact/check
- route truth belongs in Results by default; only mark it inline when honesty/blocking requires it

### `~/.hermes/task-cards/FOLLOWUP_RUNTIME_ADAPTER.md`
Added:
- process/bookkeeping event ingress rule
- `superseded` handling for stale wrapper notices
- `render_constraint` carry from active voice/lens workers into synthesis
- explicit statement that worker receipt law must be compressed before user-facing Results

### `~/.hermes/task-cards/FOLLOWUP_LANE_TASK_CARD.md`
Added fields so runtime workers keep lane boundaries:
- `system_boundary`
- `cross_surface_edges`
- `propagation_check`
- `bottleneck_target`
- `queue_or_handoff`
- `repeatability_check`
- `campaign_front`
- `decisive_front`
- `hold_or_retreat_condition`
- `render_constraint`

### `hermes-follow-up-menu-style`
Patched the hygiene/security conflict:
- keep `🛡️` / `🧹` out of the main numbered Follow-up list
- when surfaced, place them in the separate `Hygiene & Security` block and keep the footer rails too

## What remains open
- no fresh rerender proof packet was run after these patches
- plurality/council/bundle-proof checks still need stronger enforcement in the lint path
- this packet hardened the control surface wording and task-card boundary, not the broader runtime code

## Current practical lesson
Use the voices to constrain the body and use the controller to keep the output human:
- voices make the main answer think differently
- Results stay plain and compressed
- Follow-up stays numbered, single-spaced, and concrete
- bundles must say what will actually be done
