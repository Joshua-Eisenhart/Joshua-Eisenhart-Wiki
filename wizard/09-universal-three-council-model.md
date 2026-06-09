---
title: Universal Three-Council Wizard Model
created: 2026-05-02
updated: 2026-05-02
packet: v3.5
type: concept
tags: [wizard, universal, council, mmm, bounded-work]
framing: current
---

# Universal Three-Council Wizard Model

This is the shared model. It is not Codex-specific.

The Wizard is a general bounded-work compiler:

1. councils create judgment, critique, and options;
2. receipts prove what actually ran;
3. MMMs and mini-MMMs shape salience;
4. compile gates decide whether an output is ready for the current domain.

The Wizard can be used for strategy, hiring, writing, product, code, research, and sims. Domain adapters may add stricter compile profiles for work such as sims, probes, or queue-visible packets.

## Three Sequential Councils

Wave 1: Decision Council.

Purpose: choose the best bounded move now while preserving live alternatives.

Wave 2: Failure Council.

Purpose: kill, quarantine, harden, or pass the selected move.

Wave 3: Follow-Up Council.

Purpose: generate divergent next prompts and compile the useful ones into bounded work options.

Parallelism happens inside a wave. The waves are sequential barriers.

## Member Families

Council members are not one kind of thing. They are families of salience roles.

Voices:

- Hume: evidence, uncertainty, honest next move.
- Zhuangzi: live readings, alternate interpretations, exclusion condition.
- Feynman: mechanism, operation, observable, pass/fail check.
- Orwell: plain wording and anti-fog.
- Popper: falsifier, killed/open/survived status.
- Pushback: overclaim boundary and correction.
- Factory: bottleneck, queue, handoff, leverage.
- Strategy: sequence, priority, retreat/hold condition.
- Systems: feedback loop, second-order effect.

Six Thinking Hats:

- Blue Hat: process, sequence, focus, liveness.
- White Hat: facts, missing data, evidence.
- Red Hat: gut alarm, intuition, emotional/stakeholder signal.
- Black Hat: risks, difficulty, failure pressure.
- Yellow Hat: upside, value, why it could work.
- Green Hat: alternatives, lateral moves, new options.

Failure lenses:

- Premortem: assume it failed; explain how it died.
- Postmortem: if this already broke before, name the recurrence pattern.
- Security/Audit: trust boundary, abuse case, proof of execution.
- Expert Failure Lens: what a domain expert would test first.

Expert lenses:

- What experts would say: likely critique, missing standard, professional convention.
- Outside evaluator: what would be persuasive to someone not inside the system.
- Domain specialist: the exact domain constraint, not authority theater.

Follow-up lanes:

- Direct: smallest useful forward move.
- Alternative: independent route to the same goal.
- Reframe: change the framing or object of work.
- Back: rollback, retreat, or smaller safe re-entry.
- Wildcard: off-axis probe with a concrete payoff.

Compositions:

- All-A Build: Direct + mechanism + falsifier + alternative + audit.
- All-B Divergence: evidence + alternate readings + falsifier + wildcard + collapse audit.
- All-C Closeout: direct result + wording + hygiene + security + handoff.
- Max Assembly: maximum useful route-family integration. It is not named Full Wizard, and it is not a quota to run everything.

Guards:

- Hygiene: readable, organized, low-noise output.
- Security: trust boundary and unsafe side effects.
- Receipt Audit: what actually ran, what is blocked, what is simulated.
- Compile Gate: whether the result is bounded enough to act on.

Manager:

- Resource Manager / Rerouter: schedules, monitors, shrinks, reroutes, and stops waiting. It is not a council member and has no vote.

## Mini-MMM Profile

A mini-MMM is a role-local salience profile. It is not a rule list.

Each member profile should contain:

- `family`: voice | hat | failure_lens | expert_lens | lane | composition | guard | manager
- `job`: what this member makes more salient
- `phraselets`: short native terms the model should tend to use
- `question_stems`: questions this member naturally asks
- `return_shape`: what a receipt from this member should contain
- `avoid`: failure modes for this role
- `compile_relevance`: how this member helps produce bounded work

Example:

```yaml
member: Black Hat
family: hat
job: expose risks and failure paths
phraselets: [risk, break, constraint, cost, failure mode, blocker]
question_stems:
  - Where does this break?
  - What must be true for this to work?
return_shape:
  - top risk
  - failure mechanism
  - early warning
  - hardening requirement
avoid:
  - generic pessimism
  - critique without smaller replacement
compile_relevance: turns a plan into pass, harden, quarantine, or kill conditions
```

## Runtime Independence

The universal model does not require Codex, Claude Bridge, Opus, or a specific subagent API.

Each runtime must supply its own adapter for:

- how members become workers;
- how worker receipts are proven;
- how child/subworker hierarchy is represented;
- how liveness and reroute are managed;
- how output is rendered without logs.

Codex has one adapter. Claude Code would have another. A human facilitation version could run the same model without software subagents.

## Compile Gates

Universal ready-to-act gate:

- one target;
- one immediate action;
- one owner/lane;
- one success check;
- one stop/failure condition;
- one artifact/output surface;
- explicit status.

Universal statuses:

- `salience_only`
- `proposal`
- `bounded_work_candidate`
- `ready_for_execution`
- `executed`
- `accepted`
- `partial`
- `blocked`
- `deferred`

Adapter domain profile example: sim/probe packet gate:

- one active stage;
- one claim;
- one carrier or fixture;
- one exact tool/function surface or admitted coupling;
- one positive check;
- one negative or boundary check;
- one expected result path;
- prior receipt refs when required;
- explicit adapter status.

Status names are adapter-owned. The universal model does not require queue rows, runner DONE states, result JSON paths, or any specific runtime artifact. A sim adapter may require those things only after it classifies the task as sim, probe, or queue-visible.

The strict domain fields become mandatory only when the adapter classifies the task as sim, probe, or queue-visible. For ordinary docs, bug triage, refactor planning, research synthesis, or implementation handoff, the universal ready-to-act gate is enough.

Council agreement, salience lift, and receipts do not imply readiness unless the relevant compile gate passes.
