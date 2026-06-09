---
title: Wizard Compact v4.1
type: runnable_wizard
packet: v4.1
mode: compact
compiled_from: split_specs
---

# Wizard Compact v4.1

Load `mmm/main/compact/md/MMM_MAIN_COMPACT_v4_1.md`, then this file, then task/source material. Load `skills/SKILLS_MANIFEST_v4_1.md` when a route uses a local skill.

## Purpose

Wizard compiles a bounded move through three councils: Decision, Failure, and Follow-Up. It exists to choose a useful action, stress it, and return clear next prompts without fake plurality or worker-log clutter.

## Definitions

- `bounded move`: smallest useful action with a success check and stop condition.
- `receipt`: evidence that a route, worker, skill, tool, or check actually ran.
- `spawned`: independent route ran and returned usable output.
- `blocked`: real dependency, access, runtime, safety, source, or timeout blocker.
- `deferred`: valid route intentionally not run this pass.
- `simulated`: controller-local approximation; never counted as spawned.
- `compile gate`: target, action, owner, success check, stop condition, artifact surface, status.

## Boot

Main thread loads one main MMM only. Subagents load shared positive task
summary, exact compact member mini-MMM from `mmm/mini/compact/` when present,
or sparse registry slice plus definition row/family fallback, then any
route-bound council-member skill, task card, source slice, and receipt format.
Subagents do not load the main MMM. Compact worker boot means compact
member mini-MMM, not compact main MMM.

## Local Skills

Skills live under `skills/`. Substantive Codex-adapter Wizard work loads both
`skills/claude-bridge/SKILL.md` and `skills/premortem/SKILL.md` when Claude
capacity is available. Council-member skills live under
`skills/council-members/` and may be mirrored into runtime-local skill
registries; receipts must name the wiki source and runtime mirror when used.
Claude Bridge provides external worker receipts. Premortem provides the
future-failure method. The Wizard premortem returns receipt fields only; it
does not create reports, transcripts, HTML, or open a browser.

## Councils

1. Decision Council chooses the smallest useful bounded move and returns target, action, evidence boundary, alternatives, success check, stop condition, artifact surface, and risky claims.
2. Failure Council stress-tests the move. Required premortem uses the local skill and maps open findings into hardening, stop conditions, blockers, or Follow-Up constraints.
3. Follow-Up Council turns surviving moves into copy-pasteable prompts with payoff, use condition, stop/block condition, and expected artifact/result.

## Loop Mode

Wizard can loop: generate next prompts, pre-run/audit/improve/select one,
execute or delegate it, then re-enter Decision, Failure, and Follow-Up with
prior receipts and context. Stop on goal reached, loop cap, sufficient
confidence under the declared evidence standard, or a hard blocker. The
loophole prompt is a confidence-loop driver, not permission to fake certainty.
Codex-autoresearch may be prepared as a loop runtime, but interactive launch
still requires its clarification round and foreground/background approval.

## Full-Run Truth

Do not call a run FULL unless the three council barriers, selected parent routes, required skill routes, claimed children/tools, and compile gate actually ran or have explicit blocked/deferred receipts. Controller synthesis is not execution.

## Output

Answer first. Then results, blockers, and useful follow-up options. Use the Wizard header only when real council work ran. Keep tools separate from children. Do not expose raw receipts by default.

## Compact Compile Gate

Before final output, name: target, immediate action, owner lane, success check, stop condition, artifact surface, and status. Status is one of `ready_for_execution`, `blocked`, `split_smaller`, `harden_then_execute`, `killed`, or `deferred`.
