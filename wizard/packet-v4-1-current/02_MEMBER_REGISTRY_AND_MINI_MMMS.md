---
title: Wizard v4.1 Member Registry and Mini-MMMs
type: member_registry
packet: v4.1
framing: standalone
---

# Member Registry And Mini-MMMs v4.1

Members are not rules. They are salience roles that shape attention, questions, and return format.

A member becomes execution only when a runtime worker or tool runs and returns a receipt.

## Skill Bindings

Members may be salience-only or skill-backed. A skill-backed member must load
the packet-local canonical skill or a runtime-local mirror that declares its
upstream wiki source path and adapter delta.

```yaml
member_skill_binding:
  member_id:
  skill_id:
  binding: required | optional
  canonical_skill_path:
  allowed_runtime_mirror_paths:
  side_effect_boundary:
  count_rule:
```

Current portable bindings:

- `voice.strategy` -> optional `strategy-loop` at
  `skills/council-members/strategy-loop/SKILL.md`.
- `voice.systems` -> optional `systems-strategy` at
  `skills/council-members/systems-strategy/SKILL.md`.
- `voice.factory` -> optional `factory-handoff` at
  `skills/council-members/factory-handoff/SKILL.md`.
- `follow_up.prompt_voice_council` and `follow_up.lane_council` -> optional
  `follow-up-selector` at
  `skills/council-members/follow-up-selector/SKILL.md`.
- `failure.falsifier_council`, `failure.premortem_council`, and loop audits ->
  optional `loophole-auditor` at
  `skills/council-members/loophole-auditor/SKILL.md`.
- `failure.premortem_council` -> required `premortem` at
  `skills/premortem/SKILL.md`.

Optional skill bindings do not block a member when the skill is unnecessary for
the task card. Required skill bindings block the member unless the receipt
records a concrete runtime/access/path blocker and degraded route.

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
- `expert.adversarial_reviewer`: route-altering objection or blocker.
- `expert.standard_checker`: minimum external standard and pass/fail threshold.

### Lanes

- `lane.council`: one Follow-Up parent that runs all lane options as children.
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
- `manager.child_health`: verifies formal child obligations, parent-local child rerouters, and child quorum.
- `manager.route_truth`: reconciles waves, council parents, children, tools, runtimes, footer, and proof lines.
- `manager.resource_pressure`: watches model/runtime capacity, quota, timeout, fallback, and degraded-alt behavior.
- `manager.member_rebooter`: proposes bounded reinitialization when a member failed from boot, task card, source slice, or model fit.

Managers have no vote. They are not council members. They do not synthesize the answer.

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

In a visible full Wizard run, the topology is three sequential councils with
three nested parent councils inside each. Divergence moves downward into
formal child/subsubagent routes instead of expanding the parent council
forever.

Required full-run parent coverage:

- Decision Council parents: `decision.voices_council`,
  `decision.six_hats_council`, and `decision.experts_council`.
- Failure Council parents: `failure.premortem_council`,
  `failure.falsifier_council`, and `failure.loophole_auditor_council`.
- Follow-Up Council parents: `follow_up.prompt_voice_council`,
  `follow_up.lane_council`, and `follow_up.compile_gate_council`.
- `decision.voices_council` launches Strategy, Systems, Factory, Feynman, and
  Hume children.
- `decision.six_hats_council` launches Blue, White, Red, Black, Yellow, and
  Green children. This is the only default Six Hats council.
- `decision.experts_council` launches Domain Specialist, Operator, Outside
  Evaluator, Adversarial Reviewer, and Standard Checker children.
- `failure.premortem_council` launches Likely Failure, Dangerous Failure,
  Hidden Assumption, Early Warning, Revised Plan, and Sim/Evidence Corruption
  children.
- `failure.falsifier_council` launches Popper, Pushback, Calibration, Receipt
  Audit, and Boundary Check children.
- `failure.loophole_auditor_council` launches Strategy Under Test, Evidence
  Standard, Find All Loopholes, Fix Plan, Verify Fixes, and Confidence Status
  children using `skills/council-members/loophole-auditor/SKILL.md`.
- `follow_up.prompt_voice_council` launches Orwell, Strategy, Factory, and
  Hume children.
- `follow_up.lane_council` launches Direct, Alternative, Reframe, Back,
  Wildcard, and All-of-the-Above children.
- `follow_up.compile_gate_council` launches Target, Action, Owner, Success
  Check, Stop Condition, Artifact Surface, and Status children.
- Individual hats and individual lanes are not default parent council seats.
- The universal compile gate still runs after Follow-Up synthesis; the
  `follow_up.compile_gate_council` children make the gate fields visible and
  harder to fake before that final pass.

Required full-run management coverage:

- `manager.rerouter` supervises global council liveness, deadline, retry, and
  reroute behavior.
- `manager.child_health` supervises formal child obligations, parent-local
  child rerouter evidence, child quorum, and missing-child retry pressure.
- `manager.route_truth` supervises header/footer agreement, parent/child/tool
  separation, runtime claims, MMM proof, and score truth.
- `manager.resource_pressure` supervises quota, timeout, model-family
  fallback, degraded-alt signals, and waste throttling.

These four management parents are receipt-backed orchestration parents, but
they are not council parents and do not vote. Header `parents:{n}` counts the
nine council parents unless an adapter explicitly adds a separate management
diagnostic line. A management parent can block, reroute, shrink, or require a
sharper child task; it cannot replace Decision, Failure, Follow-Up, premortem,
Six Hats, experts, lanes, or compile-gate children.

Every child-launching parent must also expose a parent-local child-management
surface: `management_parent_id`, `management_scope`,
`formal_child_obligation`, counted/deferred/rerouted child ids, child health
summary, and terminal disposition. A global manager receipt does not substitute
for this parent-local child rerouter. `management_parent_id` must name
`manager.child_health`; other managers can observe or block, but child-council
health belongs to the child-health manager.

For sim/probe/queue-visible work, management parents also carry sim-specific
supervised surfaces:

- `manager.rerouter`: `queue_liveness` and `runner_preflight`.
- `manager.child_health`: `sim_admissibility_gate`, `queue_readiness`, and
  `formal_sim_profile`.
- `manager.route_truth`: `stage_gate`, `expected_result_surface`, and
  `controller_read_artifacts`.
- `manager.resource_pressure`: `runner_preflight`, `model_family_fallback`,
  and `degraded_alt_child_families`.

Without those sim-specific surfaces, management receipts are route accounting
only. They cannot support queue visibility, runner movement, or sim admission.
No management parent can be `admitted_by` for a sim pre-run promotion. Admission
requires a separate non-runner, non-controller, non-management authority and a
controller-read artifact.

Parent receipts with children must include binding evidence: `children_cited`,
`dissent_recorded`, `killed_options`, `binding_clause`, and
`child_impact_ledger`. Child fanout is not countable when the parent cannot
show what the child changed, killed, added, rejected, or blocked.

If runtime, budget, or task shape prevents this, the run is partial. Do not call it full. Retry the smallest missing member once, then mark blocked/deferred with the reason.

## Mandatory Failure Premortem

`failure.premortem_council` is the required Failure Council backcasting parent for
substantive Wizard work. It must appear in the visible Failure `Members:` line
with a compact ratio, for example `Premortem 6/6` or `Premortem 0/6 blocked`.

`failure.premortem_council` must load and use the runtime Premortem skill when
that skill is available. In Codex, the required skill path is
`skills/premortem/SKILL.md`. The council's
future-failure frame, raw failure reasons, deep-dive child prompts, and
synthesis sections come from that skill. The Wizard-embedded premortem returns
receipt fields only; it does not create reports, transcripts, HTML, or open a
browser.
The Wizard supplies the council slot, receipt truth, child counting, and
Follow-Up join gate; it does not replace the skill with generic risk prose.

If the Premortem skill cannot be loaded because of a real runtime/access/path
blocker, `failure.premortem_council` is blocked or degraded. The receipt must
name the missing skill path and cannot count as a completed Premortem member
unless it ran the skill workflow locally as an explicit degraded route.

The Wizard may add Black Hat, Red Hat, Popper, Pushback, calibration,
postmortem, receipt audit, or expert critique, but none of those replace
premortem. If `failure.premortem_council` is missing, the Failure Council is incomplete
and Follow-Up cannot be treated as compiled from a valid Failure wave.
