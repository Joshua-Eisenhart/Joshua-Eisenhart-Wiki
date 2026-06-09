# Hermes validator gate packet — 2026-04-22

Purpose: continue the Opus-heavy control-surface window with a contained validator/gate step, then check it against current hybrid-fix outputs.

## User routing note active for this packet
- use Opus 4.7 max heavily while quota window is open
- still check Opus work with other models
- Codex is the preferred containment/audit layer when it behaves
- Opus is the higher-upside idea/plurality layer, not a trust authority by itself

## What was done
1. asked Opus max for a compact validator spec
2. used that spec to implement a small deterministic validator
3. ran the validator across 8 current hybrid-fix surfaces
4. treated the Codex validator-audit lane as failed after it hung and was killed

## Artifacts written
Prompts/spec:
- `/tmp/subagent-format-harness/opus_validator_spec_prompt.txt`
- `/tmp/subagent-format-harness/surface_validator_spec.md`
- `/tmp/subagent-format-harness/codex_validator_audit_prompt.txt`

Validator:
- `/tmp/subagent-format-harness/validate_final_surface.py`
- `/tmp/subagent-format-harness/validator_report_20260422a.json`

Status summary:
- `/tmp/subagent-format-harness/hybrid_fix_summary_20260422a.json`

## Validator scope
Hard-fail checks currently cover only already-observed defects:
- missing or empty `final_surface.md`
- missing scaffold headings
- banned consensus phrases
- literal `Dropped narratives: ...`
- contradiction-mode missing key anti-collapse lines
- simple verdict inconsistency heuristic

Warnings only:
- bundle count drift
- repeated route-status phrases
- overlong opening
- duplicate first-packet smell
- repeated Results lines in Follow-up

## What the validator found
Passes:
- `matrix_opus_max/matrix14_hybrid_fix_20260422a/final_surface.md`
- `matrix_sonnet_high/matrix14_hybrid_fix_20260422a/final_surface.md`
- `matrix_gemini_full/matrix14_hybrid_fix_20260422a/final_surface.md`
- `matrix_codex_xhigh/matrix14_hybrid_fix_20260422a/final_surface.md`
- `matrix_opus_max/contradiction_hybrid_fix_20260422a/final_surface.md`
- `matrix_gemini_full/contradiction_hybrid_fix_20260422a/final_surface.md`
- `matrix_codex_xhigh/contradiction_hybrid_fix_20260422a/final_surface.md`

Hard fail:
- `matrix_sonnet_high/contradiction_hybrid_fix_20260422a/final_surface.md`
  - reason: missing_or_empty_file

Important concrete wins this gate confirmed:
- Gemini full hybrid fix now writes a real `final_surface.md`
- Codex contradiction hybrid fix no longer contains literal `Dropped narratives: ...`

## Lane closeout truth
Opus validator-spec lane:
- process `proc_f4ae9be1d1df`
- completed cleanly with `exit_code: 0`
- produced `/tmp/subagent-format-harness/surface_validator_spec.md`
- counted as real input to the validator packet

Codex validator-audit lane:
- process `proc_3ad1b64e8d24`
- hung
- killed
- no `codex_validator_audit.md` artifact landed
- excluded from proof story

## Current best reading
- keep the validator
- keep the microfix
- keep using Opus max for bounded idea/plurality work during the window
- keep treating Codex as the preferred containment layer when it actually lands
- next open defect is still Sonnet contradiction synthesis under the heavier prompt

## Best next bounded move
1. keep `validate_final_surface.py` in the loop after synthesis runs
2. shorten the contradiction-only synthesis contract for Sonnet instead of adding more rules
3. continue Opus-heavy packets with validator + Codex containment when Codex responds
