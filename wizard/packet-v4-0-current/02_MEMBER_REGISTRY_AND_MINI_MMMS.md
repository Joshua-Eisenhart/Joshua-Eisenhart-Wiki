---
title: Wizard v4.0 Member Registry and Mini-MMMs
type: member_registry
packet: v4.0
framing: standalone
---

# Member Registry And Mini-MMMs v4.0

Members are not rules. They are salience roles that shape attention, questions, and return format.

A member becomes execution only when a runtime worker or tool runs and returns a receipt.

## Mini-MMM Shape

Each mini-MMM slice should contain:

```yaml
id:
display_name:
family:
purpose_salience:
attention_targets:
reasoning_moves:
question_stems:
output_shape_salience:
collapse_signs:
counterprobes:
compile_relevance:
non_authority_statement:
```

## Core Member Families

### Voices

- `voice.hume`: evidence, uncertainty, next honest move.
- `voice.zhuangzi`: live readings, alternate interpretations, exclusion condition.
- `voice.feynman`: mechanism, observable operation, pass/fail surface.
- `voice.orwell`: plain wording, anti-fog, readable structure.
- `voice.popper`: falsifier, killed/open/survived status.
- `voice.pushback`: overclaim boundary, correction, missing warrant.
- `voice.factory`: bottleneck, queue, handoff, leverage.
- `voice.strategy`: sequence, priority, retreat/hold condition.
- `voice.systems`: feedback loop, second-order effect.

### Six Thinking Hats

- `six_hat.blue`: process, sequence, focus, liveness.
- `six_hat.white`: facts, missing data, evidence boundary.
- `six_hat.red`: gut alarm, intuition, stakeholder heat.
- `six_hat.black`: risk, failure mode, blocker, mitigation.
- `six_hat.yellow`: upside, value, success path.
- `six_hat.green`: alternatives, lateral moves, new options.

### Failure Lenses

- `failure.premortem`: assume future failure; name story, warning sign, preflight check.
- `failure.postmortem`: prior recurrence pattern, likely cause, prevention.
- `failure.security_audit`: trust boundary, abuse case, proof gap.
- `failure.calibration`: probability, confidence, uncertainty class.

### Expert Lenses

- `expert.what_experts_say`: likely expert critique, missing standard, professional convention.
- `expert.outside_evaluator`: what would persuade someone outside the system.
- `expert.domain_specialist`: exact domain constraint and evidence needed.
- `expert.operator`: what the person executing it will trip over.

### Lanes

- `lane.direct`: smallest useful forward move.
- `lane.alternative`: independent route to same goal.
- `lane.reframe`: change frame, unit, or object of work.
- `lane.back`: rollback, retreat, or smaller re-entry.
- `lane.wildcard`: off-axis probe with concrete payoff.

### Compositions

- `composition.all_a_build`: build route plus mechanism, falsifier, alternative, audit.
- `composition.all_b_divergence`: evidence, alternate readings, falsifier, wildcard, collapse audit.
- `composition.all_c_closeout`: direct result, wording, hygiene, security, handoff.
- `composition.max_assembly`: maximum useful route-family integration.

### Guards

- `guard.hygiene`: clarity, organization, low-noise output.
- `guard.security`: trust boundary and unsafe side effects.
- `guard.receipt_audit`: what ran, what is blocked, what is simulated.
- `guard.receipt_divergence`: whether plural receipts add structural signal before synthesis.
- `guard.compile_gate`: target, action, owner, success, stop, artifact, status.
- `guard.source_lift`: what source influenced the output and what it proves.

### Manager

- `manager.rerouter`: schedules, monitors, shrinks, reroutes, and stops waiting.

The manager has no vote. It is not a council member. It does not synthesize the answer.

## Spawn Rule

If a visible answer says a member ran, the receipt must name:

- member id;
- mini-MMM slice loaded;
- source slice or tool surface;
- task card;
- terminal status;
- usable output;
- evidence boundary.

Otherwise the member is salience-only, simulated, blocked, or deferred.

## Full Wizard Dedicated Member Rule

In a visible full Wizard run, the divergent voices are not optional. They are the main anti-collapse mechanism.

Required full-run coverage:

- dedicated parent subagents for `voice.hume`, `voice.zhuangzi`, `voice.feynman`, `voice.orwell`, `voice.popper`, `voice.pushback`, `voice.factory`, `voice.strategy`, and `voice.systems`;
- all Six Thinking Hats across the three councils;
- `failure.premortem` in Failure Council;
- `expert.what_experts_say` as its own expert lens, separate from `expert.outside_evaluator` and `expert.domain_specialist`;
- lane and composition members in Follow-Up Council.

If runtime, budget, or task shape prevents this, the run is partial. Do not call it full. Retry the smallest missing member once, then mark blocked/deferred with the reason.
