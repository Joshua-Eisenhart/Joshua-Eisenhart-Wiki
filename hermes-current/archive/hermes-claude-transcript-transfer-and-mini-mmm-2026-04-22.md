# Hermes Claude transcript transfer + mini-MMM note — 2026-04-22

Purpose: capture the Claude-side control-surface lessons that should transfer into Hermes without treating the Claude transcript as canon.

## Bottom line
- The Claude transcript reinforced several things already true in Hermes:
  - body before follow-up
  - full visible lane/voice field during tuning
  - concise numbered follow-up
  - Hume is plain conditional prose, not a log
  - bundles must describe actual work
- The most useful new transfer was structural:
  - each surfaced lane/voice worker should load a small role-specific mini-MMM before the task
  - the mini-MMM is vocabulary/salience/anti-collapse infrastructure, not personality theater

## What was extracted
From the Claude transcript, the transferable corrections were:
1. even a format turn still needs a real reply body
2. all-of-the-above lines must name concrete ordered work
3. surfaced lanes/voices should map to real workers or be marked plainly as blocked/not-run
4. Hume should stay warm, plain, conditional, nominalist, and not turn into support-tag bureaucracy
5. wiki/harness/MMM loading is pre-task infrastructure that shifts salience before the task lands
6. the control surface is one layered system with several access points, not separate prompt islands

## What was designed
Artifacts under `/tmp/hermes-claude-xfer-20260422/` now capture the transfer:
- `transcript_lessons.md`
- `mini_mmm_design.md`
- `harness_patch_plan.md`

The mini-MMM design treats each worker prompt as:
1. boot bundle
2. mini-MMM role profile
3. authoritative task card
4. verification block
5. output contract

Load-bearing fields:
- `read_ref`
- `method_contract`
- `scope_contract`
- `fail_if`
- `out_of_scope`
- `closeout_check`
- `voice_method_check`

## What was patched in the live /tmp harness
1. `roles.json`
- added per-role:
  - `read_ref`
  - `method_contract`
  - `scope_contract`
  - `fail_if`

2. `run_role_batch_matrix.py`
- `role_prompt()` now injects a compact mini-MMM preamble
- role workers now explicitly load:
  - `context_v2.md`
  - lane/voice reference note via `read_ref`
- prompt now carries:
  - method contract
  - scope contract
  - collapse guard
  - Hume guard
  - bundle guard

3. `context_v2.md`
- added a short `Non-collapse contract` near the top:
  - main body = judgment first
  - Results = what checked/ran
  - Follow-up = genuinely different next packets
  - Hume = warm/plain/point-first, not log-shaped
  - bundles = ordered work, not lane coverage

4. `run_role_synthesis_matrix.py`
- synthesis prompt now requires bundles to name:
  - composition
  - first packet
  - why the bundle exists
- also says Follow-up should be next work only, not repeated Results receipts

## Smoke proof
Ran:
- `python3 /tmp/subagent-format-harness/run_role_batch_matrix.py sonnet_high harness_patch_smoke_20260422a`
- `python3 /tmp/subagent-format-harness/run_role_synthesis_matrix.py sonnet_high harness_patch_smoke_20260422a`

Observed:
- batch passed
- final surface landed
- patch effects visible in role receipts and merged surface

Useful spot checks:
- `hume.md` now opens with judgment prose instead of receipt-first shape
- `systems.md`, `factory.md`, and `strategy.md` stay whole-project/campaign scale
- `direct.md` and `wildcard.md` now imply genuinely different first artifacts
- merged surface bundles describe actual ordered work instead of lane-name theater

Artifacts:
- `/tmp/subagent-format-harness/matrix_sonnet_high/harness_patch_smoke_20260422a/`

## What this does not prove
- This does not prove the whole Hermes default-controller question.
- It does not by itself fix core Hermes docs or runtime loading.
- It does show that the current /tmp lane/voice harness can absorb the Claude transcript lessons in a concrete way and produce better worker prompts.

## Best next bounded move
Use the patched /tmp harness for one more bounded packet focused on:
1. semantic follow-up divergence
2. bundle honesty
3. body vs Results separation
Then carry only the winning changes into durable Hermes control surfaces.