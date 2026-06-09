---
title: Hermes Wizard Validation Checklist
type: conformance_checklist
runtime: hermes
created: 2026-05-04
updated: 2026-05-04
---

# Validation Checklist

A Hermes Wizard run passes only if these checks pass.

## Boot/source check

- [ ] Hermes current spine or relevant source surfaces were read when needed.
- [ ] HERMES.md/SOUL.md authority split was not overwritten by this folder.
- [ ] Universal Wizard and Codex docs were treated as sources, not live Hermes authority.

## Route truth check

- [ ] Every visible route has a receipt, or an explicit blocked/deferred/not-run status.
- [ ] Controller-local synthesis is not described as spawned worker work.
- [ ] Tool checks are not counted as subagent/child receipts.
- [ ] Memory/session_search hits are not used as current execution proof.
- [ ] Background/cron/process routes distinguish scheduled/running/completed.

## Compile gate check

- [ ] Accepted move has target.
- [ ] Accepted move has immediate action.
- [ ] Accepted move has owner/lane.
- [ ] Accepted move has success check.
- [ ] Accepted move has stop/failure condition.
- [ ] Accepted move has artifact/output surface.
- [ ] Accepted move has status and evidence boundary.

## Follow-up check

- [ ] Follow-up entries are future choices unless Results says a scout/audit ran.
- [ ] Each visible follow-up has payoff, use condition, and stop/block condition.
- [ ] Scout/audit receipts are not claimed when not run.

## Output check

- [ ] Main answer says the point first.
- [ ] Results are compact receipts, not raw logs.
- [ ] Surviving splits are preserved when evidence did not kill them.
- [ ] Hygiene/security names side effects, scope, and shared-state risks.
- [ ] Footer does not invent route proof.

## Failure examples this checklist must reject

- “Full Wizard ran” when no delegate/tool receipts exist.
- “Memory confirms X” when memory only recalls a prior note.
- Follow-up item offered as future work but also counted as completed branch execution.
- A voice label that does not change evidence, falsifier, explanation, wording, bottleneck, or strategy.
- Codex child matrix copied into Hermes as mandatory without runtime need.
