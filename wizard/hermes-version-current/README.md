---
title: Hermes Wizard Version
created: 2026-05-04
updated: 2026-05-16
type: runtime_design
runtime: hermes
framing: current-proposed
---

# Hermes Wizard Version

This folder is Hermes's own version of the Wizard idea.

It is not a copy of `../packet-v4-1-current/`.
It is not a replacement for `~/.hermes/HERMES.md` or `~/.hermes/SOUL.md`.
It is a low-coupling design/proof folder for making Wizard behavior work through Hermes's strengths:

- skill-first routing
- persistent memory and session recall
- built-in toolsets
- bounded `delegate_task` workers
- cron/background/gateway surfaces when explicitly admitted
- profile-scoped state
- compact Results receipts instead of raw route logs
- SOUL's small load-bearing voice stack

## Current status

`drafted`: this folder exists as a Hermes-owned design and audit surface.

Not yet `adopted`: no global HERMES/SOUL/control-file changes were made by creating this folder.

## Read order

1. `00_READ_FIRST.md`
2. `01_RUNTIME_CONTRACT.md`
3. `02_TOOL_ADVANTAGE_MAP.md`
4. `03_CODEX_PROCESS_IMPORT_AUDIT.md`
5. `04_SKILL_IMPORT_AUDIT.md`
6. `05_SOURCE_AND_LIFT_BOUNDARY.md`
7. `06_ADOPTION_PLAN.md`
8. `07_CODEX_LOCAL_SKILL_STACK_AUDIT.md`
9. `08_HERMES_WIZARD_RUN_HARNESS.md`
10. `09_V4_1_LLM_COUNCIL_TOPOLOGY_CORRECTION.md`
11. `10_HERMES_NEEDS_RECURSION_KB_PREMORTEM_INTEGRATION.md`
12. `11_HERMES_WIZARD_LOOP_SANDBOX_RESULTS.md`
13. `12_HERMES_3X3_MMM_PILOT_RESULTS.md`
14. `13_HERMES_WIZARD_V4_1_LOOP_HARNESS.md`
15. `14_HERMES_WIZARD_V4_2_NATIVE_LOOP_BRIDGE.md`
16. `15_HERMES_WIZARD_V4_3_OBJECT_PRESERVATION.md`
17. `16_HERMES_WIZARD_MAINTENANCE_GOVERNOR.md`
18. `schemas/HERMES_WIZARD_RECEIPT_SCHEMA.md`
19. `conformance/VALIDATION_CHECKLIST.md`

## Core claim

A general Wizard packet cannot run a system by itself. A system has to make a native version that binds the general mechanisms to its own tools, state, failure modes, and output discipline.

For Hermes, that means:

- Hermes Wizard is a composable controller over standalone skill, agent, model, and tool routes. Each component should remain usable on its own; Wizard composes them only when composition changes the answer, verification, or next move.
- Hermes Wizard may also act as a maintenance governor for Hermes, its durable memory, skills, subagent ledger, and wiki spine. That role coordinates existing Hermes surfaces; it does not replace `HERMES.md`, `SOUL.md`, memory tooling, skills, or `hermes-current/` authority.
- `full` and `auto` are breadth selectors, not truth labels. `full` attempts all admitted relevant councils/lanes/skills for the declared scope. `auto` selects only routes likely to change the answer. A decision-relevant skipped route must stay visible as `not_run` or `deferred` with a reason.
- Current Wizard binding is **v4.3-gated v4.2**: v4.3 validates the current-task object card before object-bearing work, while v4.2 supplies the council/runtime/output machinery;
- Wizard v4.2 topology is three distinct LLM councils in sequence: Decision -> Failure -> Follow-Up;
- Hermes needs the v4.2 native bridge to map that topology onto Hermes tools, cron, workers, premortem, and route truth after the v4.3 object-preservation gate has passed;
- wide parallel parent/member and child/subchild work belongs inside each council when the runtime supports it;
- premortem is an essential Failure Council member for substantive Wizard runs, and Follow-Up must not render options until open premortem findings are mapped to stop conditions, required hardening, out-of-scope, or dismissed-by-artifact;
- RLM-FORGE/Ouroboros are source models for evidence-gated recursion and replayable child evidence handles, not default Hermes authority;
- PageIndex/OpenKB are source models for structure-first retrieval and compiled wiki/KB maintenance, not replacements for the current wiki spine;
- a one-parent-per-council run is only partial/minimal topology, not full/proper current Wizard council conformance;
- memory can retrieve context, but cannot prove current execution;
- skills carry procedures, but do not replace the wiki or current source checks;
- `delegate_task` can spawn real bounded workers, but controller-local synthesis is not worker proof;
- cron can schedule durable work, but only from self-contained prompts and explicit scope;
- follow-up options are future choices unless Results says a scout/audit already ran;
- visible route truth must be compact, not a worker ledger.

## Folder role

This folder is the current Hermes-owned Wizard adaptation and proof surface. It supports the live `hermes-wizard` skill and should not be pasted wholesale into Hermes's profile prompt.
