---
title: Hermes Wizard Source Map
type: source_map
runtime: hermes
created: 2026-05-04
updated: 2026-05-16
---

# Source Map

## Hermes current frame

- `/Users/joshuaeisenhart/wiki/hermes-current/read-first.md` — Hermes front door; wiki as long-form frame.
- `/Users/joshuaeisenhart/wiki/hermes-current/active-intentions.md` — low-coupling, fail-closed, support-first current intentions.
- `/Users/joshuaeisenhart/wiki/hermes-current/environment-and-rules.md` — Hermes/Codex/Claude boundary, profile/workspace rules.
- `/Users/joshuaeisenhart/wiki/hermes-current/current-vs-legacy.md` — provenance and authority ranking.
- `/Users/joshuaeisenhart/wiki/hermes-current/skills-and-agent-rules.md` — skills are procedures; wiki is long-form doctrine/frame.
- `/Users/joshuaeisenhart/wiki/hermes-current/active-plans.md` — active Hermes runtime/output/subagent planning surfaces.

## Hermes runtime/control sources

- `/Users/joshuaeisenhart/.hermes/HERMES.md` — profile control law, output scaffold, lane/runtime mechanics.
- `/Users/joshuaeisenhart/.hermes/SOUL.md` — body voice and anti-collapse method.
- `/Users/joshuaeisenhart/.hermes/task-cards/TASK_CARD_SCHEMA.md` — existing Hermes worker task-card schema.
- `/Users/joshuaeisenhart/.hermes/task-cards/RUNTIME_CONTROL_OBJECTS_SCHEMA.md` — runtime registry/lane/worker receipt objects.
- `/Users/joshuaeisenhart/.hermes/task-cards/FOLLOWUP_RUNTIME_ADAPTER.md` — follow-up candidate/scout/audit pipeline.
- `/Users/joshuaeisenhart/.hermes/task-cards/MMM_PREPROMPT_INDEX.md` — MMM preload and receipt fields.

## General Wizard sources

- `/Users/joshuaeisenhart/wiki/wizard/packet-v4-1-current/README.md`
- `/Users/joshuaeisenhart/wiki/wizard/packet-v4-1-current/PACKET_MANIFEST_v4_1.md`
- `/Users/joshuaeisenhart/wiki/wizard/packet-v4-1-current/00_BOOT.md`
- `/Users/joshuaeisenhart/wiki/wizard/packet-v4-1-current/01_UNIVERSAL_THREE_COUNCIL_WIZARD.md`
- `/Users/joshuaeisenhart/wiki/wizard/packet-v4-1-current/03_RECEIPTS_AND_COMPILE_GATES.md`
- `/Users/joshuaeisenhart/wiki/wizard/packet-v4-1-current/04_FOLLOW_UP_COUNCIL.md`
- `/Users/joshuaeisenhart/wiki/wizard/packet-v4-1-current/05_RUN_PROTOCOL_AND_RETRY.md`
- `/Users/joshuaeisenhart/wiki/wizard/packet-v4-1-current/06_OUTPUT_FORMAT_AND_SCORING.md`
- `/Users/joshuaeisenhart/wiki/wizard/packet-v4-1-current/adapters/HERMES_ADAPTER.md`
- `/Users/joshuaeisenhart/wiki/wizard/packet-v4-1-current/adapters/CODEX_ADAPTER.md`

## Codex process sources

- `/Users/joshuaeisenhart/Desktop/Codex Ratchet/AGENTS.md`
- `/Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/ops/SIM_FULL_WIZARD_PARALLEL_RUNBOOK.md`
- `/Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/ENFORCEMENT_AND_PROCESS_RULES.md`
- `/Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/LLM_CONTROLLER_CONTRACT.md`
- `/Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/wizard/bootstrap_cards/schemas/BOOTSTRAP_CARD_SCHEMA_v4_1.yaml`

## Skill source family

Audited under:

`/Users/joshuaeisenhart/.hermes/skills/`

Corrected Codex-local audit also inspected:

`/Users/joshuaeisenhart/.codex/skills/`

Important Codex-local skill surfaces include `three-council-wizard-v4-1`, `three-council-wizard`, `premortem`, `claude-bridge`, thread dispatch/monitor/closeout, automation, safe maintenance, and Codex Ratchet A2/A1/refinery skills. See `../07_CODEX_LOCAL_SKILL_STACK_AUDIT.md`.

Most important import families:

- autonomous agent runtime skills: Codex, Claude Code, Hermes Agent, delegate runtime proof
- Hermes output/runtime skills: output-surface stress, follow-up menu style, role receipts
- controller loop skills: hermes-autoresearch, bounded-autoresearch, subagent-driven-development
- Codex Ratchet sim/controller skills: sim planning, sim controller orchestration, geometry micro-packets, truth audit
- wiki/controller skills: wiki maintenance, wiki steward cron, harness authoring

## Sandbox loop integration sources

- `/tmp/hermes-loop-integration-20260505-135517/artifacts/aggregate_loop_report.md` — sandbox aggregate report for loop-smoke 0003-0012; evidence summary, not live runtime authority.
- `/tmp/hermes-loop-integration-20260505-135517/bin/hermes_wizard_loop_cli.py` — reusable profile-driven sandbox runner for bounded sim profiles.
- `/tmp/hermes-loop-integration-20260505-135517/loop-runs/loop-smoke-0012/receipt.json` — latest profile-driven admitted receipt.
- `/tmp/hermes-loop-integration-20260505-135517/profiles/dr_refinement_micro_01.json` — first bounded target profile.
- `/tmp/hermes-loop-integration-20260505-135517/loop-runs/loop-smoke-0008/receipt.json` — Ouroboros/RLM pinned runtime hold/block receipt.
- `/tmp/hermes-3x3-mmm-pilot-20260506/receipt.json` — first 9-subcouncil MMM pilot aggregate receipt.
- `/tmp/hermes-3x3-mmm-pilot-20260506/audit/audit_report.json` — deterministic receipt/collapse/overclaim/salience audit for the 3x3 MMM pilot.
- `/tmp/hermes-3x3-mmm-pilot-20260506/receipts/` — per-subcouncil worker receipts for Decision, Failure, and Follow-Up.
- `/tmp/hermes-wizard-autoresearch-cleanup-scout-20260506.md` — quarantined autoresearch scout artifact after a worker wrote to the live Codex Ratchet work directory; used as a failure-boundary lesson for loop harness design.
- `/Users/joshuaeisenhart/wiki/wizard/hermes-version-current/13_HERMES_WIZARD_V4_1_LOOP_HARNESS.md` — current proposed loop-harness design artifact; records self-generated next steps, option pre-runs, premortem/autoresearch, parent/child receipt boundaries, route truth, and apply-gate rules.
- `/tmp/hermes-v41-autoloop-rounds/round-0001/runner/receipt.json` — first enforcement-gated read-only autoloop runner receipt; status `admitted_plan`, candidate-only boundary preserved, no live config/git/Codex sim mutation.
- `/tmp/hermes-v41-autoloop-rounds/round-0002/audit/calibration_audit.json` — read-only MMM calibration candidate audit; 2 parent routes with 4 child receipts, 4/4 calibration condition receipts, no overclaims, no collapse pairs, MMM salience improved over no-MMM in same-session bounded audit.

These sources prove sandbox/pre-adoption behavior only. They do not install, enable, or register live Hermes runtime changes.

## Wizard v4.2 sources

- `/Users/joshuaeisenhart/wiki/wizard/packet-v4-2-current/WIZARD_v4_2.md` — canonical v4.2 runtime topology, output contract, parent/child/management route definitions, and FULL truth rules.
- `/Users/joshuaeisenhart/wiki/wizard/packet-v4-2-current/skills/SKILLS_MANIFEST_v4_2.md` — packet-local skill manifest for premortem, Claude bridge, loophole auditor, factory handoff, follow-up selector, strategy loop, and systems strategy.
- `/Users/joshuaeisenhart/wiki/hermes-current/wiki-wizard-v4-2-autoloop-control.md` — active finite wiki-autoloop control surface and tick contract.
- `/Users/joshuaeisenhart/.hermes/skills/autonomous-ai-agents/hermes-wizard/SKILL.md` — Hermes procedure skill that treats Wizard v4.2 as current and distinguishes legacy v4.1/provenance work from ordinary/current Wizard replies.
- Gemini direct CLI and attempted Grok/OpenRouter route from the 2026-05-16 alignment campaign — advisory premortem pressure only; Grok route blocked by model/credit availability during this pass.

## Source status

This source map proves only that these surfaces were consulted or identified during this design pass. It does not prove runtime adoption.
