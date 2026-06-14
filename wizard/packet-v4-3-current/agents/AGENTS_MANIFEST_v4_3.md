# Agents Manifest v4.3

authority_status: canonical-agent-spec
packet_version: v4.3

Packet-local agent specifications for Wizard v4.3. These files let runtimes instantiate parent routes, manager checks, voice agents, loop agents, and auditors without relying on scattered external Claude/Codex files.

## Rule

An agent file is not a run receipt. A route counts as run only when the current run receipt names the agent spec, task card, MMM/slice preload, runtime target, output, and proof depth.

## Source families

- `agents/wizard-loop/`: seeded from `/Users/joshuaeisenhart/.claude/agents/wizard/`.
- `agents/voices/`: seeded from `/Users/joshuaeisenhart/Codex-Ratchet/.claude/agents/voice-*.md` and scrubbed so project-specific engine policy stays adapter-local.
- `agents/parents/`: generated from v4.3 parent route list in `WIZARD_v4_3.md`.
- `agents/managers/`: generated from v4.3 manager route list in `WIZARD_v4_3.md`.
- `agents/auditors/`: seeded from current collapse-auditor agent.

## Active agent specs

- `agents/parents/decision.context_strategy.md` (parents)
- `agents/parents/decision.evidence_boundary.md` (parents)
- `agents/parents/decision.move_selection.md` (parents)
- `agents/parents/failure.falsifier.md` (parents)
- `agents/parents/failure.loophole_auditor.md` (parents)
- `agents/parents/failure.premortem.md` (parents)
- `agents/parents/follow_up.compile_gate.md` (parents)
- `agents/parents/follow_up.lane_builder.md` (parents)
- `agents/parents/follow_up.next_move_selector.md` (parents)
- `agents/managers/manager.child_health.md` (managers)
- `agents/managers/manager.output_compiler.md` (managers)
- `agents/managers/manager.route_truth.md` (managers)
- `agents/managers/manager.run_controller.md` (managers)
- `agents/managers/manager.strategy_memory.md` (managers)
- `agents/wizard-loop/evidence-mapper.md` (wizard-loop)
- `agents/wizard-loop/falsifier-agent.md` (wizard-loop)
- `agents/wizard-loop/premortem-agent.md` (wizard-loop)
- `agents/wizard-loop/prompt-packetizer.md` (wizard-loop)
- `agents/wizard-loop/route-sequencer.md` (wizard-loop)
- `agents/wizard-loop/route-truth-agent.md` (wizard-loop)
- `agents/wizard-loop/scope-keeper.md` (wizard-loop)
- `agents/wizard-loop/scout-runner.md` (wizard-loop)
- `agents/wizard-loop/selector-compiler.md` (wizard-loop)
- `agents/voices/voice-factory.md` (voices)
- `agents/voices/voice-feynman.md` (voices)
- `agents/voices/voice-hume.md` (voices)
- `agents/voices/voice-orwell.md` (voices)
- `agents/voices/voice-popper.md` (voices)
- `agents/voices/voice-pushback.md` (voices)
- `agents/voices/voice-strategy.md` (voices)
- `agents/voices/voice-systems.md` (voices)
- `agents/voices/voice-zhuangzi.md` (voices)
- `agents/auditors/council-collapse-auditor.md` (auditors)

## Required taskcard surfaces

- `taskcards/TASKCARDS_MANIFEST_v4_3.md`
- `taskcards/PARENT_ROUTE_TASK_CARD_SCHEMA_v4_3.md`
- `taskcards/CHILD_TASK_CARD_SCHEMA_v4_3.md`
- `taskcards/SUBAGENT_BOOT_RULES_v4_3.md`
- `taskcards/SUBSUBAGENT_BOOT_RULES_v4_3.md`
