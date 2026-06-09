# Hermes carry-forward from current Claude context — 2026-04-22

Purpose: capture what the user's latest Claude-side work changes for Hermes tuning.

## Main carry-forward
The Claude-side work reinforces that voices are not labels or output decorations. They are saliency attractors: correlated language bodies that bias what the model attends to next. The mini-MMM is therefore not a behavior checklist. It is a dense language body loaded before task execution.

## Voice / MMM lessons to carry into Hermes
1. Keep an 8-voice map in mind, not the older 7-voice map.
   - Hume
   - Zhuangzi
   - Feynman
   - Orwell
   - Popper
   - Factory
   - Strategy
   - Systems
2. Systems is not Strategy or Factory.
   - Systems = loops, propagation, second-order effects, incentives, emergence
   - Factory = bottleneck, queue, handoff, leverage point
   - Strategy = campaign sequence, retreat condition, resource ordering
3. Orwell / Popper / Feynman should stay distinct by target object.
   - Orwell targets language/fog itself
   - Popper targets claims/falsifiers
   - Feynman targets procedures/observables/pass-fail
4. Hume / Zhuangzi are the most coupled and the most nominalistic/human.
   - Hume = retrospective honesty about what was encountered, conditional and particular
   - Zhuangzi = prospective preservation of live readings not yet excluded by the next probe
5. Mini-MMMs should be made from wiki/harness slices and language samples, not mostly from rules about what the voice does.
6. L0 ambient preamble + per-voice dense mini-MMM body is the right stack.

## Process lessons to carry into Hermes
1. Same-session calibration is contaminated. Fresh-session calibration is the real Step 3 gate.
2. When plurality is the point, active lanes/routes/lenses should get real bounded subagents. Subsubagents are valid when branch-local audit/falsifier work is needed.
3. Synthesis should preserve multiple live routes and present multiple ways of bringing things together; automatic flattening is the failure mode.
4. Output shape is part of governance because emitted language reshapes later saliency.
5. Small deterministic validators are worth keeping when they are tied only to observed failures.
6. Checked truth must stay separate from proposal and from attractive `/tmp` surfaces.
7. Dense MMM files do not close the proof question; mechanism questions remain open and should stay open until a separating probe runs.
8. There is a real perverse-incentive risk: writing attractor-coherent prose can select for one underlying basin in many costumes unless contradiction tests and cross-basin probes are used.

## Grounded Claude-side facts checked now
- Claude MMM directory currently contains 9 markdown files:
  - `00_L0_PREAMBLE.md`
  - `hume.md`
  - `zhuangzi.md`
  - `feynman.md`
  - `orwell.md`
  - `popper.md`
  - `factory.md`
  - `strategy.md`
  - `systems.md`
- Current checked total across the 8 voice files is `30,788` words.
- Current checked per-voice word counts are:
  - `hume.md` `4072`
  - `zhuangzi.md` `3774`
  - `feynman.md` `3572`
  - `orwell.md` `3957`
  - `popper.md` `3947`
  - `factory.md` `3424`
  - `strategy.md` `3520`
  - `systems.md` `4522`
- Current checked `~/.claude/generate_voice_prompt.py` now includes `systems` in the `VOICES` table and `--list` shows all 8 voices with MMM files present.
- So Hermes should carry forward the corrected 8-voice architecture, not the older stale 7-voice assumption from earlier notes.
- Opening-shape check is suggestive but not yet decisive:
  - `systems.md`, `popper.md`, `strategy.md`, `orwell.md`, and `zhuangzi.md` front-load their register strongly in the first 25 words
  - `hume.md` opens in its register too, but more by sentence shape and support-honesty framing than by simple fallback-vocabulary hits
  - this suggests a useful caution for Hermes: keyword-density heuristics alone will underread some voices, especially Hume
- Additional live Claude-side questions worth carrying forward:
  - mechanism remains open between vocabulary-loading, syntax-groove, and truncation-dominance readings
  - header stripping is not yet a proven improvement; current checked state is mixed because 7 files are headerless while `systems.md` still starts with a header
- `probe-test-log.md` exists and records Step 3 as still open
- `mmm_calibration_log.md` does not yet exist
- `stance_hold_test.py` loader seam is currently fixed to prefer `~/.claude/mmm/` and `python3 ~/.claude/mmm/stance_hold_test.py --dry-run` now passes with all 8 voices loaded and `name/preamble/hold_vocab` present

## What Hermes should do with this now
- treat the Claude-side 8-voice / mini-MMM work as a live comparative source for Hermes
- do not copy it blindly into Hermes core docs yet
- use it to sharpen Hermes voice/lane distinctness, especially:
  - Systems as its own attractor
  - Hume/Zhuangzi distinction
  - mini-MMMs as language bodies rather than rule lists
- keep subagent-heavy routing when the point is preserving many narratives at once

## Best next bounded move
1. compare these carry-forward notes against current Hermes control surfaces
2. land only the missing parts into Hermes tuning artifacts
3. do the next Hermes-side packet with:
   - 8-voice awareness
   - subagent-per-active-lane rule
   - mini-MMM language-body loading as the primary saliency mechanism
