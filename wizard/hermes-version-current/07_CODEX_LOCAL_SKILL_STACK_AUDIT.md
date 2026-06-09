---
title: Codex Local Skill Stack Audit
type: skill_stack_audit
runtime: hermes
created: 2026-05-04
updated: 2026-05-04
status: corrected
---

# Codex Local Skill Stack Audit

## Correction

The earlier Hermes Wizard import audit was incomplete. It inspected Wizard packet docs, Codex Ratchet process docs, and Hermes skills, but it did not systematically inspect the local Codex skill stack under:

`/Users/joshuaeisenhart/.codex/skills/`

This file is the corrected audit surface for the skills Codex uses or can use to run its Wizard/Codex-Ratchet version.

## Coverage

Inspected:

- 20 non-system local Codex `SKILL.md` files under `/Users/joshuaeisenhart/.codex/skills/*/SKILL.md`.
- 5 Codex `.system` skill `SKILL.md` files under `/Users/joshuaeisenhart/.codex/skills/.system/*/SKILL.md` for boundary classification.
- linked reference files for the Wizard and runtime-critical skills where they change execution semantics:
  - `three-council-wizard-v4-1/references/v4-1-file-map.md`
  - `three-council-wizard-v4-1/references/v4-1-run-checklist.md`
  - `three-council-wizard/references/receipt-admission.md`
  - `three-council-wizard/references/followup-council.md`

Not claimed:

- This audit does not prove a current Codex Wizard run happened.
- This audit does not import every Codex skill into Hermes.
- This audit does not make Codex Ratchet A2/A1 or sim gates general Hermes law.

## Direct Codex Wizard stack

| Codex skill | Role in Codex version | Hermes import decision |
|---|---|---|
| `/Users/joshuaeisenhart/.codex/skills/three-council-wizard-v4-1/SKILL.md` | Active v4.1 Wizard skill. Boots full MMM, then boot/core/receipt/follow-up docs; enforces Decision -> Failure -> Follow-Up sequence; requires parent/child receipt truth, visible v4.1 header, score, MMM proof, and output self-repair. | Import mechanisms only: three barriers, route truth, receipt boundaries, follow-up prework, output repair. Reject fixed child quorums, scored header default, and mandatory Max Assembly for Hermes. |
| `/Users/joshuaeisenhart/.codex/skills/three-council-wizard-v4/SKILL.md` | Earlier v4/v4.1 transition skill. Similar v4.1 contract but older surface; keeps v4 runner/conformance references. | Treat as historical/transition source, not current Hermes authority. |
| `/Users/joshuaeisenhart/.codex/skills/three-council-wizard/SKILL.md` | General Codex Ratchet Wizard orchestration layer. Defines three waves, compile gate profiles, receipt admission, salience packs, and specialist-skill delegation. Explicitly calls `$premortem` and `$claude-bridge` instead of absorbing them. | Import the decomposition: core Wizard skill should call specialized skills instead of becoming a mega-skill. Already patched `hermes-wizard` to call `premortem` when needed. |
| `/Users/joshuaeisenhart/.codex/skills/premortem/SKILL.md` | Standalone Gary Klein prospective-hindsight skill: context minimum, already-failed frame, raw failure reasons, one deep-dive agent per reason, synthesis, optional report/transcript. | Imported as `/Users/joshuaeisenhart/.hermes/skills/productivity/premortem/SKILL.md`. |
| `/Users/joshuaeisenhart/.codex/skills/claude-bridge/SKILL.md` | Codex-to-Claude external worker bridge. Supplies Opus/Sonnet/Haiku/Gemini-ish child fanout wrappers, budgets, timeouts, receipts, stream evidence, receipt summarizer, and measured fanout throttles. | Do not copy to Hermes. Hermes has native `delegate_task`, `claude-code`, process, and provider routing. Import only the evidence rule: external worker claims require receipt path/status/model/cost/output, not prose. |
| `codex-autoresearch` | Not found as a local Codex skill at `/Users/joshuaeisenhart/.codex/skills/codex-autoresearch/SKILL.md`, and the older repo path `/Users/joshuaeisenhart/Desktop/Codex Ratchet/.agents/skills/codex-autoresearch/SKILL.md` is also absent. It is present as a Wizard Harness adapter contract at `/Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/ops/codex_autoresearch_contract.md`, and referenced by Wizard v4.1 run protocol / Codex adapter. | Audit as a runtime contract, not a local skill. Import the boundary: Wizard compiles a bounded launch packet with metric/verify/guard/receipt; autoresearch owns repeated improve/verify execution only after owner-authorized foreground/background launch. |

## Runtime and controller support skills

These are not the portable Wizard itself, but they show how Codex keeps long-running worker/process work bounded.

| Codex skill | Role | Hermes import decision |
|---|---|---|
| `/Users/joshuaeisenhart/.codex/skills/thread-dispatch-controller/SKILL.md` | Launch bounded fresh-thread worker lanes with role labels, scope, boot files, expected outputs, stop condition, and handoff into monitor/closeout. | Import as task-card discipline for Hermes `delegate_task`: exact scope, output, stop condition. Do not import Codex Ratchet role labels as general Hermes defaults. |
| `/Users/joshuaeisenhart/.codex/skills/thread-run-monitor/SKILL.md` | Diagnose worker health: healthy-ready-to-stop, needs one bounded final step, stalled, duplicate, drifted, metadata-polish-only, waiting-on-external. Routes to stop/continue/correct. | Import liveness states and stop-law thinking for Hermes worker/background work. |
| `/Users/joshuaeisenhart/.codex/skills/thread-closeout-auditor/SKILL.md` | Convert returned thread closeouts into repo-held packets; one returned thread = one packet; do not smooth contradictions. | Import closeout/capture discipline where Hermes workers return long outputs. Do not import Codex Ratchet sink paths. |
| `/Users/joshuaeisenhart/.codex/skills/closeout-result-ingest/SKILL.md` | Normalizes closeout replies into repo-held artifacts and summaries. | Import only as artifact-ingest pattern. |
| `/Users/joshuaeisenhart/.codex/skills/codex-automation-controller/SKILL.md` | Designs safe recurring Codex automations: one loop class, safety contract before schedule, quarantine-first, fail-closed. | Import as cron/background safety pattern for Hermes. Hermes cron prompts must be self-contained and scoped. |
| `/Users/joshuaeisenhart/.codex/skills/safe-run-maintenance/SKILL.md` | Archive-first, move-only, fail-closed maintenance for generated artifacts; never delete; protect active owner surfaces. | Import as maintenance safety pattern. Useful for Hermes file cleanup work, not Wizard core. |

## Codex Ratchet research / A2-A1 upper-loop skills

These are Codex Ratchet-specific. They should not become general Hermes Wizard defaults, but they matter when Hermes is controlling Codex Ratchet or importing Codex process lessons.

| Codex skill | Role | Hermes import decision |
|---|---|---|
| `/Users/joshuaeisenhart/.codex/skills/ratchet-a2-a1/SKILL.md` | Reads Codex Ratchet corpus in order, preserves contradictions, builds A2 understanding and A1 proposal-only distillation. | Project-specific. Load Codex Ratchet/wiki skills when working that project. |
| `/Users/joshuaeisenhart/.codex/skills/a2-brain-refresh/SKILL.md` | Refreshes A2 understanding when repo changes/user corrections/new evidence make it stale. | Import only the stale-state refresh idea for wiki/harness work. |
| `/Users/joshuaeisenhart/.codex/skills/a1-from-a2-distillation/SKILL.md` | Derives proposal-only A1 outputs from refreshed A2 inputs. | Project-specific. Do not generalize into Hermes Wizard. |
| `/Users/joshuaeisenhart/.codex/skills/a2-a1-memory-admission-guard/SKILL.md` | Gates writes into active A2/A1 memory surfaces. | Import the admission-guard concept for memory/wiki writes, but keep Hermes memory tiny. |
| `/Users/joshuaeisenhart/.codex/skills/brain-delta-consolidation/SKILL.md` | Consolidates many bounded outputs into small append-safe A2/A1 deltas. | Import as anti-sprawl consolidation principle for wiki edits. |
| `/Users/joshuaeisenhart/.codex/skills/external-research-refinery-launcher/SKILL.md` | Builds bounded external research ZIP jobs. | Use only for research-lane packetization analogies; not a Hermes Wizard default. |
| `/Users/joshuaeisenhart/.codex/skills/external-research-return-ingest/SKILL.md` | Routes returned research packs through audit, A2 refresh, A1 distillation, admission, consolidation. | Import as returned-work ingestion chain, not as a default answer style. |
| `/Users/joshuaeisenhart/.codex/skills/pro-return-instant-audit/SKILL.md` | Fast audits external research returns for citation, overclaim, ontology smuggling, provenance. | Import as audit checklist when Hermes ingests external research. |

## Tool / generic skills

| Codex skill | Role | Hermes import decision |
|---|---|---|
| `/Users/joshuaeisenhart/.codex/skills/playwright/SKILL.md` | Codex CLI browser automation through Playwright wrapper. | Hermes already has browser tools. Import only the pattern: use real browser automation when UI evidence matters, and keep snapshots/traces distinct from claims. |
| `.system/skill-creator` | Codex system skill authoring. | Boundary only. Hermes uses Hermes skill manager/authoring rules, not Codex system skill creator. |
| `.system/skill-installer` | Codex skill install/list. | Boundary only. Hermes has Hermes skills tooling. |
| `.system/plugin-creator` | Codex plugin scaffolding. | Not part of Wizard import. |
| `.system/openai-docs` | Official OpenAI docs retrieval. | Use only when current OpenAI API docs are relevant. |
| `.system/imagegen` | Image generation/editing. | Not part of Wizard import. |

## Actual Codex Wizard dependency shape

Codex's version is not just `three-council-wizard-v4-1` alone. It is a stack:

1. Wizard v4.1 skill loads the universal packet and defines the run contract.
2. General `three-council-wizard` skill preserves compile gates, receipt admission, and the specialist-skill boundary.
3. `$premortem` supplies real prospective hindsight for Failure Council.
4. `$claude-bridge` supplies external Claude/Opus/Sonnet/Haiku/Gemini worker receipts and fanout summaries.
5. `codex-autoresearch` is not a found local skill in this filesystem; it appears as a Wizard Harness adapter contract for owner-authorized long improve/verify loops.
6. Thread dispatch/monitor/closeout skills handle long-running Codex worker lanes outside a single Wizard packet.
7. Automation and safe-maintenance skills constrain recurring/background controller loops.
8. A2/A1/refinery skills are Codex Ratchet project-specific upper-loop skills, not generic Wizard mechanics.

## Hermes import changes made from this corrected audit

Already completed:

- Created standalone Hermes skill: `/Users/joshuaeisenhart/.hermes/skills/productivity/premortem/SKILL.md`.
- Patched `hermes-wizard` to list `premortem` as related and to call it when prospective-hindsight work is needed.
- Patched `03_CODEX_PROCESS_IMPORT_AUDIT.md` to include premortem as real prospective-hindsight work.
- Patched `04_SKILL_IMPORT_AUDIT.md` to include Codex `$premortem` and the created Hermes skills.

Still proposed, not done:

- Add a Hermes worker-lifecycle/closeout skill only if repeated Hermes `delegate_task` or background-worker closeout work needs it.
- Add a Hermes cron/background safety skill only if recurring Hermes controller loops become common enough to warrant a standalone skill.
- Do not create Hermes clones of Codex Ratchet A2/A1 skills unless working inside Codex Ratchet specifically.

## Main falsifier

If the Hermes version says it imported Codex's Wizard process but did not inspect `/Users/joshuaeisenhart/.codex/skills/`, the audit is incomplete. The local Codex skill stack is part of the working Codex version.
