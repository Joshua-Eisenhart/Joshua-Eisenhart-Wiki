---
title: Wizard v4.1 Member Definitions
type: member_definitions
packet: v4.1
framing: standalone
---

# Member Definitions v4.1

Each member has a job, return shape, and collapse mode.

Definitions guide worker assignments. Mini-MMMs shape salience. Receipts prove execution.

Skill-backed members add executable workflow behavior to the salience role.
When a member uses a skill, the receipt must include `council_member_skill`
fields from `schemas/RECEIPT_SCHEMA_v4_1.md`. Optional skills sharpen a
member; required skills block that member when missing.

## Voices

| Member | Use | Return | Avoid |
| --- | --- | --- | --- |
| `voice.hume` | Evidence and uncertainty. | Support level, uncertainty boundary, next honest move. | Confidence without evidence boundary. |
| `voice.zhuangzi` | Multiple live readings. | Live readings, exclusion conditions, what changes under each. | Forced single interpretation. |
| `voice.feynman` | Mechanism and observable check. | Setup, operation, observable, pass/fail surface. | Clarity without measurement. |
| `voice.orwell` | Plain wording. | Plain replacement, removed fog, readable structure. | Slogans or decorative phrasing. |
| `voice.popper` | Falsifier pressure. | Target claim, falsifier, killed/open/survived. | Critique with no decisive test. |
| `voice.pushback` | Overclaim correction. | Overclaim, correction, bounded replacement. | Disagreement without repair. |
| `voice.factory` | Bottleneck and handoff. | Bottleneck, next station, handoff artifact. | Process prose with no movement. |
| `voice.strategy` | Sequence and priority. | Priority, sequence, hold/retreat condition. | Plan with no stop condition. |
| `voice.systems` | Feedback and second-order effects. | Loop, amplification, second-order risk, intervention. | Linear cause story. |

## Nested Parent Councils

The full v4.1 topology is three sequential councils with three nested parent
councils inside each.

| Parent Council | Use | Children | Avoid |
| --- | --- | --- | --- |
| `decision.voices_council` | Choose the smallest useful bounded move through divergent salience. | Strategy, Systems, Factory, Feynman, Hume. | Blended voice summary with no child impact. |
| `decision.six_hats_council` | Apply all Six Thinking Hats to the Decision move. | Blue, White, Red, Black, Yellow, Green. | Six separate parent seats or a hats label with no child receipts. |
| `decision.experts_council` | Test the move against outside, domain, operator, adversarial, and standard pressure. | Domain Specialist, Operator, Outside Evaluator, Adversarial Reviewer, Standard Checker. | Authority vibes with no standard or check. |
| `failure.premortem_council` | Mandatory Premortem skill-backed future-failure backcast that changes Follow-Up constraints. | Premortem skill path/load status, no file/browser side effects, Likely Failure, Dangerous Failure, Hidden Assumption, Early Warning, Revised Plan, Sim/Evidence Corruption. | Risk list with no Premortem skill load, no future-failure story, or no Follow-Up join gate. |
| `failure.falsifier_council` | Falsify, calibrate, audit receipts, and decide pass/split/harden/block/kill. | Popper, Pushback, Calibration, Receipt Audit, Boundary Check. | Agreement framed as readiness. |
| `failure.loophole_auditor_council` | Stress-test the current strategy until no known unresolved loophole remains under the declared evidence standard, or return the exact remaining uncertainty. | Strategy Under Test, Evidence Standard, Find All Loopholes, Fix Plan, Verify Fixes, Confidence Status. | Fake certainty, generic risk prose, or replacing Premortem. |
| `follow_up.prompt_voice_council` | Make next prompts clear, sequenced, grounded, and evidence-honest. | Orwell, Strategy, Factory, Hume. | Pretty output that still leaves the human asking what to do. |
| `follow_up.lane_council` | Generate divergent next-move options and composition. | Direct, Alternative, Reframe, Back, Wildcard, All-of-the-Above. | Lane labels with no payoff, use condition, or stop condition. |
| `follow_up.compile_gate_council` | Verify the universal bounded-work compile gate. | Target, Action, Owner, Success Check, Stop Condition, Artifact Surface, Status. | Council agreement used as readiness. |

## Six Thinking Hats

| Member | Use | Return | Avoid |
| --- | --- | --- | --- |
| `six_hat.blue` | Process and sequence. | Current phase, next gate, reroute/block decision. | Becoming a content vote. |
| `six_hat.white` | Facts and missing data. | Known facts, missing facts, evidence boundary. | Speculation as fact. |
| `six_hat.red` | Gut alarm and stakeholder heat. | Alarm, intuition, stakeholder signal. | Fake justification or analysis theater. |
| `six_hat.black` | Risk and failure. | Risk, failure mode, mitigation or block. | Generic pessimism. |
| `six_hat.yellow` | Upside and value. | Benefit, success path, worth-it condition. | Cheerleading without condition. |
| `six_hat.green` | Alternatives. | Alternative, novelty, testable next move. | Random ideas without payoff. |

## Failure Lenses

| Member | Use | Return | Avoid |
| --- | --- | --- | --- |
| `failure.premortem_council` | Load the Premortem skill, assume future failure, and run formal premortem children or an explicit degraded local route. | Skill path/load status, no file/browser side effects, failure story, hidden assumption, warning sign, prevention, revised plan pressure. | Vague risks, no Premortem skill evidence, or premortem that does not bind Follow-Up. |
| `premortem.likely_failure` | Name the most likely future failure after the selected move shipped. | Failure story, cause chain, prevention. | Generic risk list. |
| `premortem.dangerous_failure` | Name the highest-damage future failure even if less likely. | Damage path, affected party, hard stop or mitigation. | Severity without mechanism. |
| `premortem.hidden_assumption` | Surface the assumption that makes the move look safer than it is. | Assumption, dependency, test or blocker. | Vague "we assume it works." |
| `premortem.early_warning` | Define observable signs that failure is starting. | Warning signal, where to observe it, threshold. | Lagging indicators only. |
| `premortem.revised_plan` | Shrink or harden the move using premortem findings. | Revised move, precheck, stop condition. | Ignoring the premortem. |
| `premortem.sim_evidence_corruption` | For sim/evidence work, catch evidence-shape corruption before promotion. | Corruption sign, blocked promotion reason, required artifact check. | Treating lint failures as cosmetic. |
| `failure.postmortem` | Learn from prior breakage. | Recurrence pattern, likely cause, prevention. | Treating repeated failures as isolated. |
| `failure.security_audit` | Trust and abuse. | Boundary, abuse path, proof gap, mitigation. | Security theater. |
| `failure.calibration` | Probability and confidence. | Confidence, uncertainty class, update evidence. | False precision. |

## Expert Lenses

| Member | Use | Return | Avoid |
| --- | --- | --- | --- |
| `expert.outside_evaluator` | External persuasion. | Outside objection, needed proof, clearer framing. | Insider-only language. |
| `expert.domain_specialist` | Domain constraint. | Constraint, testable claim, accepted evidence. | General expertise without domain surface. |
| `expert.operator` | Execution friction. | Trip point, support needed, simpler handoff. | Ignoring handoff cost. |
| `expert.adversarial_reviewer` | Route-altering objection. | Concrete blocker, falsifier, or override condition. | Supportive expert vibes. |
| `expert.standard_checker` | Minimum external standard. | Standard, threshold, pass/fail check. | Vague best practices. |

## Lanes

Lanes generate and improve follow-up options. In v4.1 they enter the Follow-Up
Council through `follow_up.lane_council`; individual lane ids are
child/subsubagent routes, not separate parent council seats.

| Member | Use | Return | Avoid |
| --- | --- | --- | --- |
| `lane.direct` | Smallest forward move. | Target, action, artifact, check. | Over-expansion. |
| `lane.alternative` | Independent route. | Different route, tradeoff, comparison check. | Same route with new label. |
| `lane.reframe` | Change frame. | Old frame, failure, new frame, first artifact. | Abstract reframing with no first move. |
| `lane.back` | Retreat safely. | Last stable point, safe re-entry, stop condition. | Regression disguised as caution. |
| `lane.wildcard` | Off-axis probe. | Probe, payoff, boundary, keep/drop condition. | Randomness without leverage. |
| `lane.all_of_the_above` | Compose viable follow-up options into one ordered prompt. | Sequence, dependency order, stop gates. | Leaving composition burden on the human. |

## Compositions

| Member | Use | Return | Avoid |
| --- | --- | --- | --- |
| `composition.all_a_build` | Build and pressure-test. | Build move, mechanism, falsifier, audit. | Build-only optimism. |
| `composition.all_b_divergence` | Preserve alternatives. | Live alternatives, falsifier, collapse audit. | Collapsing divergence too early. |
| `composition.all_c_closeout` | Finish cleanly. | Final artifact, wording check, safety check, handoff. | Calling done with open checks. |
| `composition.max_assembly` | Integrate useful routes. | Integrated plan, first action, blockers, stop condition. | All-routes quota. |

## Guards

| Member | Use | Return | Avoid |
| --- | --- | --- | --- |
| `guard.hygiene` | Readability and structure. | Finding, simplification, remaining clutter. | Cosmetic cleanup only. |
| `guard.security` | Unsafe side effects. | Boundary, risk, mitigation, residual risk. | Broad warnings with no boundary. |
| `guard.receipt_audit` | Route truth. | Ran, blocked, simulated, missing receipt, repair. | Counting starts as completions. |
| `guard.receipt_divergence` | Plurality quality before synthesis. | Path identical, decorative split, convergent signal, healthy divergence, rerun/block. | Treating different wording as different thinking. |
| `guard.compile_gate` | Readiness. | Target, action, owner, success, stop, artifact, status. | Readiness from agreement. |
| `guard.boundary_check` | Claim and artifact boundary. | Boundary, overclaim, allowed claim, blocker. | Letting a useful result promote a broader claim. |
| `guard.source_lift` | Source influence. | Source, lift, evidence, what it does not prove. | Source lift as execution proof. |

## Manager

| Member | Use | Return | Avoid |
| --- | --- | --- | --- |
| `manager.rerouter` | Liveness and resource routing. | Accepted, slow, rerouted, blocked, deferred. | Voting, synthesizing, or becoming a fourth council. |
| `manager.child_health` | Formal child obligations and parent-local child rerouter health. | Child quorum, missed obligation, retry/reroute, terminal child disposition. | Counting single-child theater, hiding missed children, or replacing parent-local child ledgers. |
| `manager.route_truth` | Header, footer, receipt, runtime, tool, and score reconciliation. | Mismatch, repair, blocked claim, accepted route-truth boundary. | Treating tools as children or prior receipts as current runs. |
| `manager.resource_pressure` | Runtime capacity, quota, timeout, fallback, and degraded-alt behavior. | Capacity signal, fallback route, throttle/shrink action, degraded-alt evidence. | Blind retry loops, quota bashing, or lowering the gate because a model failed. |
| `manager.member_rebooter` | Bounded reinitialization for a member that likely failed from boot/card/source/model fit. | Failure hypothesis, boot/card/source/model delta, retry limit, stop condition. | Generic prompt banks, retrying every member, or treating a reboot as proof. |
