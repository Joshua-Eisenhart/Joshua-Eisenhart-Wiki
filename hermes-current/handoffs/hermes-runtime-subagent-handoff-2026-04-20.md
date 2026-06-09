# Hermes runtime + output-format handoff — 2026-04-20

Purpose: carry the live Hermes prompt/runtime/subagent thread into a fresh Hermes terminal without losing the key constraints, checked state, or next bounded move.

Status: active handoff note for a fresh Hermes session.

## Bottom line
- The built-in Hermes subagent boot path is fixed on disk and locally proved.
- The currently running chat backend stayed stale after the patch, so a fresh Hermes session / restarted backend is needed to pick up the new delegate code.
- Output-surface corrections are load-bearing: point first, no log-shaped Hume answers, and follow-up options must be concrete and non-empty.
- Important runtime fact: in a repo-backed Hermes session, `SOUL.md` is auto-loaded from `~/.hermes`, but `~/.hermes/HERMES.md` and `~/.claude/CLAUDE.md` are not auto-loaded by default; they must be read explicitly if their rules are required.

## Directly checked in the current session

### Files read / patched now
- `/Users/joshuaeisenhart/.hermes/SOUL.md`
- `/Users/joshuaeisenhart/.hermes/HERMES.md`
- `/Users/joshuaeisenhart/.hermes/hermes-agent/tools/delegate_tool.py`
- `/Users/joshuaeisenhart/.hermes/hermes-agent/tests/tools/test_delegate.py`
- `/Users/joshuaeisenhart/.hermes/skills/note-taking/hermes-follow-up-menu-style/SKILL.md`

### Delegate runtime/subagent state checked now
- `tools/delegate_tool.py` was patched so delegated children receive the Hermes boot bundle:
  - `HERMES.md`
  - `SOUL.md`
  - `SUBAGENT_BOOT.md`
- The delegated child closeout request was tightened to require a receipt-shaped summary:
  - what you checked
  - what you changed or concluded
  - what remains open
  - artifact paths
  - next bounded move or explicit block
- Local delegate tests passed:
  - command: `venv/bin/python -m pytest -o addopts='' tests/tools/test_delegate.py -q`
  - result: `69 passed`
- Fresh local delegated proof succeeded:
  - direct runtime artifact: `/tmp/hermes_delegate_boot_proof/direct.runtime.txt`
  - Hume runtime artifact: `/tmp/hermes_delegate_boot_proof/hume.runtime.txt`
  - both listed: `HERMES.md, SOUL.md, SUBAGENT_BOOT.md`
- The still-running Hermes backend in this chat remained stale after the patch:
  - built-in `delegate_task` smoke still returned `NONE`
  - so: fresh local imports saw the patch; the loaded chat backend did not

### Output-surface corrections checked now
- `SOUL.md` now includes a Hume point-first rule:
  - lead with the 1–3 key things that matter
  - do not open with a log-shaped dump
  - receipts support the point; they do not replace it
- `SOUL.md` ordinary-answer binding now explicitly requires:
  - bottom line first
  - no raw log shape in normal replies
- `HERMES.md` now includes:
  - main-answer rule: answer the actual question first, evidence second
  - follow-up quality gate: every option must name a real next move
  - suppress empty/filler options
  - suppress `Back` when there is no real branch context
- A bounded reply-quality check was run against a draft answer for:
  - key point first
  - not log-shaped
  - concrete non-empty follow-ups
  - result: `PASS`

## Recovered from prior-session summaries / compaction, not directly reread now
These items are useful continuity, but they are not direct re-reads from this session.

- Prior work restored and enriched the Hermes prompt/control surfaces:
  - `~/.hermes/SOUL.md`
  - `~/.hermes/HERMES.md`
  - `~/.hermes/SUBAGENT_BOOT.md`
  - `~/.hermes/task-cards/FOLLOWUP_LANE_TASK_CARD.md`
  - `~/.hermes/task-cards/FOLLOWUP_RUNTIME_ADAPTER.md`
- Prior work also ran real OAuth CLI worker receipts across:
  - Claude
  - Codex
  - Gemini
  and wrote artifacts under:
  - `/tmp/hermes_cli_lane_workers/`
- Prior thread intent strongly emphasized:
  - keep the established visible answer surface
  - make voices/lenses real rather than theatrical
  - use actual subagents where they have distinct bounded work
  - keep plurality alive instead of collapsing it into one story

## User corrections that must steer the next session
- Do not destroy the tuned output format while fixing runtime/subagent internals.
- Clear communication is required: say the key thing first.
- `🦉 Hume` is failing if it sounds like logs.
- Follow-up options are failing if they are hollow or padded.
- If asking the user to do something like opening a new Hermes session, provide the exact path/prompt needed to do it.

## Important artifacts
### Current-session local proof
- `/tmp/hermes_delegate_boot_proof/report.md`
- `/tmp/hermes_delegate_boot_proof/direct.result.json`
- `/tmp/hermes_delegate_boot_proof/hume.result.json`
- `/tmp/hermes_delegate_boot_proof/direct.runtime.txt`
- `/tmp/hermes_delegate_boot_proof/hume.runtime.txt`

### Earlier runtime receipts (recovered from session summary)
- `/tmp/hermes_cli_lane_workers/`
- `/tmp/hermes_voice_harness/`

## Next bounded move for a fresh Hermes terminal
1. Read this handoff note.
2. Run a tiny built-in delegate smoke in the new Hermes session.
   - Goal: ask a delegated child to report the first three boot/control files it was instructed to read before acting.
3. Classify the result:
   - if it returns `HERMES.md, SOUL.md, SUBAGENT_BOOT.md` -> the new backend is fresh
   - if it returns `NONE` -> the new backend is still stale
4. If fresh, continue the runtime integration work by adding a first-class task-card field/path for delegated workers instead of relying only on freeform context.
5. Keep the output surface stable:
   - point first
   - evidence second
   - no hollow follow-ups
   - the compact first-reply smoke rule does not persist after the first reply; ordinary outputs revert to main answer + follow-up block + footer

## Read-next in a fresh terminal
- `[[handoffs/hermes-next-terminal-prompt-2026-04-20]]`
- `[[active-plans]]`
- `[[read-first]]`

Write mode: controller-maintained handoff.