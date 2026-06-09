# Hermes matrix14 compare — opus max / codex xhigh / sonnet / gemini — 2026-04-22

Purpose: bounded compare for the user's chosen lean bundle with max subagents/subsubagents, explicit Opus 4.7 max and Codex 5.4 xhigh, plus Sonnet and Gemini checks.

## What ran
Full 14-role packet run id:
- `matrix14_compare_20260422a`

Standardized contradiction synthesis run id:
- `contradiction_compare_20260422a`

Families/runtime paths:
- `opus_max` -> `claude -p --model claude-opus-4-7 --effort max`
- `sonnet_high` -> `claude -p --model claude-sonnet-4-6 --effort high`
- `gemini_full` -> `gemini -p -m gemini-3-flash-preview`
- `codex_xhigh` -> `omx exec --xhigh -m gpt-5.4`

Count summary:
- 56 role workers = 14 roles x 4 families
- 4 full syntheses
- 4 contradiction syntheses
- 3 compare subagents
- total bounded runs in this packet: 67

Machine summary:
- `/tmp/subagent-format-harness/matrix14_compare_20260422a_summary.json`

## Artifact roots
Full packet merged surfaces:
- `/tmp/subagent-format-harness/matrix_opus_max/matrix14_compare_20260422a/final_surface.md`
- `/tmp/subagent-format-harness/matrix_sonnet_high/matrix14_compare_20260422a/final_surface.md`
- `/tmp/subagent-format-harness/matrix_gemini_full/matrix14_compare_20260422a/final_surface.md`
- `/tmp/subagent-format-harness/matrix_codex_xhigh/matrix14_compare_20260422a/final_surface.md`

Contradiction synthesis surfaces:
- `/tmp/subagent-format-harness/matrix_opus_max/contradiction_compare_20260422a/final_surface.md`
- `/tmp/subagent-format-harness/matrix_sonnet_high/contradiction_compare_20260422a/final_surface.md`
- `/tmp/subagent-format-harness/matrix_gemini_full/contradiction_compare_20260422a/final_surface.md`
- `/tmp/subagent-format-harness/matrix_codex_xhigh/contradiction_compare_20260422a/final_surface.md`

## Landed facts
- all 4 families landed full 14-role packets
- all 4 families landed full merged surfaces
- all 4 families landed contradiction synthesis surfaces
- Hume patch remained compatible with the full 14-role packet across all four families
- codex_xhigh background wrapper later closed cleanly with `exit_code: 0`; no remaining async ambiguity on that family

## Full-packet comparison
Best overall / closest to current Hermes tuning:
- `sonnet_high`
  - strongest body-first discipline
  - clearest readable follow-up field
  - best overall scaffold fidelity

Strongest anti-collapse / pressure / bundle design:
- `opus_max`
  - strongest visible pressure in body
  - best bundle usefulness
  - strongest plurality/anti-collapse texture

Best concise/compression pass:
- `codex_xhigh`
  - shortest honest body
  - clearest compressed next-packet framing
  - loses some of the distinct role texture compared with Sonnet/Opus

Weakest final user-facing surface / useful negative contrast:
- `gemini_full`
  - rougher synthesis
  - more collapse into grouped consensus language
  - useful as ambiguity-stress sample rather than best final surface

## Contradiction-preservation ranking
Using the standardized contradiction pack (promote now vs hold until tested):
1. `sonnet_high` — best explicit preservation of both live branches
2. `opus_max` — strong preservation, slightly more leaned toward hold
3. `codex_xhigh` — preserves tension but compresses it faster into sequence
4. `gemini_full` — weakest; names the tension but tends toward consensus flattening

## Representative role-level findings
Best Hume after the latest Hume patch:
- `sonnet_high`

Best role split by family:
- best Hume: `sonnet_high`
- best Popper: `sonnet_high`
- best Systems: `opus_max`
- best Strategy: `sonnet_high`
- best Direct: `opus_max`

Gemini weaknesses that mattered in this packet:
- weaker scaffold discipline on representative role files
- more overclaim/consensus drift in synthesis
- still useful as a check/falsifier family

## Useful hybrid carry-forward
Do not flatten to one winner-story.
Current best hybrid reading:
- `sonnet_high` = base scaffold
- `opus_max` = anti-collapse / pressure / bundle overlay
- `codex_xhigh` = compression guard
- `gemini_full` = ambiguity / collapse stress sample

## What this does not prove
- not a durable Hermes-core promotion yet
- not a proof that every contradiction shape is preserved
- not a proof that all families are equal; evidence is split by role vs synthesis quality

## Best next bounded move
Promising next bundle:
1. keep `sonnet_high` as the base merged surface reference
2. import `opus_max` bundle language + anti-collapse pressure rules
3. run `codex_xhigh` as the compression/verifier pass
4. keep `gemini_full` as the negative/falsifier sample
5. only then decide what leaves `/tmp` for durable Hermes surfaces
