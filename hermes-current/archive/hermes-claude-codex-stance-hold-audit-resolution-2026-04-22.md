# Hermes carry-forward from Claude/Codex stance-hold audit dispute — 2026-04-22

Purpose: record the checked current state after the Claude-side deep audit and the Codex-side correction on `stance_hold_test.py`.

## Bottom line
Codex caught a real blocker at the time it was raised: the proposed Step 3 next command was not clean while the loader seam pointed at the wrong `generate_voice_prompt.py` surface. Current checked state has moved forward: the seam is now fixed and the no-model smoke passes. Step 3 fresh-session behavioral calibration is still open.

## Checked now
- `/Users/joshuaeisenhart/.claude/mmm/stance_hold_test.py` now inserts `~/.claude/mmm` into `sys.path` before importing `generate_voice_prompt`.
- `/Users/joshuaeisenhart/.claude/generate_voice_prompt.py` still does not define `load_voice` / `load_all_voices`.
- `/Users/joshuaeisenhart/.claude/mmm/generate_voice_prompt.py` does define `load_voice` / `load_all_voices`.
- `python3 ~/.claude/mmm/stance_hold_test.py --dry-run` now passes with 8 voices loaded and all required fields present (`name`, `preamble`, `hold_vocab`).
- `python3 ~/.claude/mmm/stance_hold_test.py --null-baseline` over the full default set timed out after 600s in this packet; it was not retried indefinitely.
- bounded reroute runs landed:
  - `--voice popper --null-baseline` -> `1.0`
  - `--voice popper` -> latest `1.0`
  - `--voice hume --null-baseline` -> `0.5`
  - `--voice hume` -> latest `1.0`
- `/Users/joshuaeisenhart/.claude/probe-test-log.md` still marks Step 3 open and now also records this partial stance-hold pilot.
- z3 axiom-sensitivity flip on `z3_voice_divergence_test.py` changes `CHECK 5` from `unsat` to `sat` when `systems_rejects_instance_check_as_final_remedy` is flipped false in the receipt-fact slots. Current honest reading: the script models a useful divergence/collapse signal, but `proves` is too strong.

## Correct current wording
- Old stronger wording: `audit clean`
- Better historical wording for the earlier moment: `audit useful, but not clean — loader seam blocker on the proposed gate command`
- Correct wording now: `loader seam fixed; smoke passes; Step 3 behavioral calibration still open`

## What this does and does not close
Closed enough to proceed:
- calibration-tool admission smoke for `stance_hold_test.py`

Still open:
- null baseline run
- Popper/Hume live stance-hold runs
- fresh-session Step 3 closure
- basin-distinctness proof beyond tool admission

## Best next bounded move
1. run `python3 ~/.claude/mmm/stance_hold_test.py --null-baseline`
2. run `python3 ~/.claude/mmm/stance_hold_test.py --voice popper`
3. run `python3 ~/.claude/mmm/stance_hold_test.py --voice hume`
4. append the first real Step 3 entry to `probe-test-log.md`

## Routing lesson
When a model or tool path catches a real blocker, keep the correction. Then re-check the live file state before repeating the blocker as current truth. If the blocker is already fixed, do not keep narrating it as still open.
