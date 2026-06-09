# Hermes wizard-mode stress handoff — 2026-04-21

Purpose: preserve the current Hermes output/routing tuning state so a fresh terminal can resume quickly without losing the packet artifacts, the adaptive-routing rules, or the wiki alignment.

Status: active handoff note.

## Bottom line
- The output/routing work is in a good state and is now partially externalized into the wiki, skills, packet artifacts, and Hermes runtime/control files.
- A real bounded council-loop packet was run at:
  - `/tmp/subagent-format-harness/packets/wizard_loop_002/`
- The packet proved a useful controller rule:
  - if a sampled lane hangs, cancel or route around it fast; do not sit and wait for a dead step
- Global Hermes control law loading was hardened on disk:
  - `~/.hermes/HERMES.md` now has a stronger full-scaffold / follow-up rule surface
  - `~/.hermes/hermes-agent/agent/prompt_builder.py` and `run_agent.py` now load global `~/.hermes/HERMES.md` into the ordinary system prompt alongside `SOUL.md`
- Wizard mode is now part of the live style expectations:
  - more semantic emojis are okay
  - `🧙` should lead the ending rail in wizard mode
  - voice/lane emojis and system/structural emojis are now separated more explicitly

## Directly checked this session

### Wiki / skills / harness surfaces updated now
- `/Users/joshuaeisenhart/wiki/hermes-current/hermes-subagent-stress-and-adaptive-routing-plan-2026-04-21.md`
- `/Users/joshuaeisenhart/wiki/hermes-current/hermes-answer-surface-stress-rubric-2026-04-21.md`
- `/Users/joshuaeisenhart/wiki/hermes-current/active-plans.md`
- `~/.hermes/HERMES.md`
- `~/.hermes/SOUL.md`
- `~/.hermes/SUBAGENT_BOOT.md`
- `~/.hermes/skills/note-taking/hermes-follow-up-menu-style/SKILL.md`
- `~/.hermes/skills/autonomous-ai-agents/tribunal/SKILL.md`
- `~/.hermes/skills/autonomous-ai-agents/claude-runtime-smoke-test/SKILL.md`
- `~/.hermes/task-cards/FOLLOWUP_RUNTIME_ADAPTER.md`
- `~/.hermes/task-cards/FOLLOWUP_LANE_TASK_CARD.md`
- `~/.hermes/hermes-agent/agent/prompt_builder.py`
- `~/.hermes/hermes-agent/run_agent.py`
- `~/.hermes/hermes-agent/tests/run_agent/test_run_agent.py`
- `/tmp/subagent-format-harness/context_v2.md`
- `/tmp/subagent-format-harness/adaptive_council_policy.json`
- `/tmp/subagent-format-harness/runtime_registry_template.json`
- `/tmp/subagent-format-harness/packet_report_template.json`
- `/tmp/subagent-format-harness/run_council_loop_packet_parallel.py`

### Packet `wizard_loop_002` checked now
Artifacts:
- `/tmp/subagent-format-harness/packets/wizard_loop_002/worker_gemini.md`
- `/tmp/subagent-format-harness/packets/wizard_loop_002/worker_claude_parallel.md`
- `/tmp/subagent-format-harness/packets/wizard_loop_002/audit_sonnet.md`
- `/tmp/subagent-format-harness/packets/wizard_loop_002/recall_hume.md`
- `/tmp/subagent-format-harness/packets/wizard_loop_002/recall_popper.md`
- `/tmp/subagent-format-harness/packets/wizard_loop_002/recall_zhuangzi.md`
- `/tmp/subagent-format-harness/packets/wizard_loop_002/final_opus.md`
- `/tmp/subagent-format-harness/packets/wizard_loop_002/runtime_registry.json`
- `/tmp/subagent-format-harness/packets/wizard_loop_002/packet_report.json`
- `/tmp/subagent-format-harness/packets/wizard_loop_002/report.md`

Observed packet result:
- sampled Gemini worker succeeded
- parallel default Sonnet worker succeeded
- sampled Codex audit lane hung / produced no audit artifact
- the controller routed around that failure with a Sonnet fallback audit
- Hume / Popper / Zhuangzi recall then ran
- the in-script Opus round 4 later hit `error_max_turns`, but the packet was then closed by a separate direct Opus rerun writing `final_opus.md`

## Important operating rule recovered from this session
If a sampled worker/audit lane is hanging or unlikely to complete:
1. cancel it quickly
2. mark it blocked in the runtime registry
3. spin up an alternate live path immediately
4. keep the packet moving
5. do not waste time waiting on a likely-dead step

## User steering that must persist
- Save context to the wiki and keep Hermes memory aligned with it.
- Skills matter more than only stuffing behavior into HERMES/SOUL text.
- Voices and lanes should have measurable tuning criteria.
- Preserve plurality; do not collapse everything into one narrator.
- Repeated voice use is allowed when the reasoning job genuinely recurs.
- Some bounded randomness in worker/audit choice is good, but it must stay legible.
- Wizard mode should use more semantic emoji and `🧙` at the start and end.

## Good next bounded moves
1. Use the hardened parallel runner:
   - `/tmp/subagent-format-harness/run_council_loop_packet_parallel.py`
   so packet reports and runtime registries are auto-emitted, and hanging lanes are cancelled/fallback-routed automatically.
2. Add one canonical pointer/note so a fresh session can find the best current packet without grepping old tune dirs.
3. Continue polishing the skills because they are the durable output-governance layer.
4. Run another bounded packet with the new parallel runner and compare it against `wizard_loop_002`.

## Read next in a fresh terminal
- `[[read-first]]`
- `[[active-plans]]`
- `[[hermes-subagent-stress-and-adaptive-routing-plan-2026-04-21]]`
- `[[hermes-answer-surface-stress-rubric-2026-04-21]]`
- `[[handoffs/hermes-wizard-mode-stress-handoff-2026-04-21]]`

Write mode: controller-maintained handoff.
