# Hermes follow-up collapse hardening — 2026-04-21

Purpose: record the bounded hardening work after ordinary tuning-mode replies about late process notifications collapsed their follow-up block to 3 options.

## Bottom line
- The collapse was real.
- It was not justified by the issue being "small" or by the turn being a bookkeeping/system notice.
- The main durable fix was to make tuning/stress/wizard mode explicitly override the generic 1–3 follow-up cap for process-notification / wrapper-exit / bookkeeping replies.
- A repeatable lint corpus now catches the known bad shape.

## Files patched
1. `~/.hermes/skills/note-taking/hermes-follow-up-menu-style/SKILL.md`
- narrowed the tiny-issue shortcut to user-explicit tiny issues
- added: do not route process-notification / wrapper-exit / bookkeeping replies into the tiny/state-clarification shortcut during tuning/stress/wizard mode

2. `~/.hermes/HERMES.md`
- in the format-tuning visibility gate, added explicit rule:
  - do not shrink the main follow-up block to the generic 1–3 default on ordinary tuning/stress/wizard replies, including process-notification / wrapper-exit / bookkeeping turns, unless the user explicitly asks for compression
- in the verbosity-failure gate, changed the 1–3 rule to apply outside tuning/stress/wizard mode

3. `~/.hermes/task-cards/FOLLOWUP_RUNTIME_ADAPTER.md`
- added explicit controller-mapping rule that the executable visible lane field must not collapse on process-notification / wrapper-exit / bookkeeping turns in tuning/stress/wizard mode

## Corpus + lint
Corpus directory:
- `/tmp/subagent-format-harness/followup_collapse_corpus_20260421/`

Main files:
- `manifest.json`
- `lint_followup_collapse.py`
- `lint_report.json`

Negative examples extracted from real Hermes session receipts:
- `collapsed_proc_old.md`
- `collapsed_proc_wrapper1.md`
- `collapsed_proc_wrapper2.md`

Positive controls:
- `positive_gold_bookkeeping.md`
- `positive_codex_final_surface.md`

## Current lint result
From `lint_report.json`:
- 3 real collapsed bookkeeping replies fail
- 1 gold bookkeeping fixture passes
- 1 broader tuning positive control passes, with a warning that some options remain abstract

Observed bad-shape signature for the real collapsed replies:
- visible core lanes present: `1/7`
- follow-up option count: `3`
- route/runtime status tokens absent from Results

## Current rule summary
For this workspace:
- ordinary tuning/stress/wizard replies keep the full scaffold
- late process notifications do not justify shrinking to a tiny/state-clarification reply
- the broad visible route field remains visible unless the user explicitly asks for compression
- blocked launchers stay blocked and should be named plainly rather than smoothed over

## Open
- File-side hardening is landed.
- A fresh live render proof after these exact patches is still the next bounded check.
- The lint is strongest for bookkeeping-turn collapse; it is not yet a full general quality judge for every tuning-mode answer.

## Best next bounded move
Run one fresh live process-notification reply under the patched rules and verify:
1. full scaffold remains present
2. follow-up block stays broad
3. Results exposes route/runtime status
4. blocked paths remain explicit
