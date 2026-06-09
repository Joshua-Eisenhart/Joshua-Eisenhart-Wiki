---
title: Wizard v4.1 Run Protocol and Retry Rules
type: run_protocol
packet: v4.1
framing: standalone
---

# Run Protocol And Retry Rules v4.1

The basic Wizard run should not be the hard part.

The runtime loads MMMs, assigns bounded member cards, runs the workers, collects receipts, retries bad lanes, and renders a clear answer.

## Full Run Minimum

A full visible Wizard run needs:

1. Main thread loaded `mmm/main/full/md/MMM_MAIN_FULL_v4_1.md` for FULL mode or `mmm/main/compact/md/MMM_MAIN_COMPACT_v4_1.md` for COMPACT mode.
2. Decision Council ran its three nested parent councils: `decision.voices_council`, `decision.six_hats_council`, and `decision.experts_council`.
3. Failure Council ran its three nested parent councils: `failure.premortem_council`, `failure.falsifier_council`, and `failure.loophole_auditor_council`.
4. Follow-Up Council ran its three nested parent councils: `follow_up.prompt_voice_council`, `follow_up.lane_council`, and `follow_up.compile_gate_council`.
5. Each visible parent member loaded an exact mini-MMM slice.
6. Each required parent either completed, blocked with a reason, or was retried smaller.
7. Every accepted parent council satisfied its formal child obligation. One child per parent never satisfies v4.1; the child count is derived from the route definition, not a generic fixed denominator.
8. The four non-voting management parents completed with receipts:
   `manager.rerouter`, `manager.child_health`, `manager.route_truth`, and
   `manager.resource_pressure`.
9. Each child-launching parent exposed parent-local child-management fields:
   `management_parent_id`, `management_scope`, `formal_child_obligation`,
   counted/deferred/rerouted child ids, child health summary, and terminal
   disposition. `management_parent_id` must be `manager.child_health`.
10. Each accepted parent member reports `member_utility`: distinct contribution, decision use, sim relevance, theater cut, current disposition, and reboot note.
11. Follow-up options passed the universal bounded-work compile gate.
12. The final answer includes a run header, council notation, score, and follow-up prompts.

If any required item is missing, the run is not full. Mark it partial, retry, or show the blocker.

## Wizard Harness

The Wizard Harness is the receipt, conformance, and run-health layer around the
Wizard. Harness work comes before sim promotion or broad cleanup claims. It
checks whether the Wizard actually loaded the right salience, ran the assigned
members, launched and rerouted children, preserved tool/child separation, and
rendered an answer that lowers human cognitive load.

Harness results are not sim results. A green harness means the route-truth
machinery can be trusted for the next bounded move; it does not prove the
underlying sim, refactor, research synthesis, or implementation succeeded.

## Parallel Trajectories, Sequential Deliberation

Wizard v4.1 already uses a parallel-then-sequential shape: workers create
independent trajectories, then controller synthesis deliberates over them.
The deliberator contract makes that shape explicit without adding a fourth
council.

After a plural worker wave, the controller builds a serialized trajectory cache
from receipt-bound entries, not from free-form memory. The cache may be pruned
for length, but pruning must preserve source receipt ids, evidence anchors,
executable deltas, dissent, and the evidence boundary.

Sequential deliberation must classify the query, judge each trajectory, preserve
or test high-value minority paths, and re-derive when all trajectories are wrong.
Majority agreement, coherent prose, or route labels do not satisfy this gate.

## Partial Run Minimum

A partial visible run needs:

1. Main thread loaded the full MMM.
2. At least one Decision member, one Failure member, and one Follow-Up member ran or were explicitly blocked.
3. The final option passed the universal compile gate or was marked blocked/deferred.
4. The answer does not claim full run.

COMPACT is valid only when `WIZARD_COMPACT_v4_1.md` and the compact main MMM were loaded. Otherwise use FULL, PARTIAL, or BLOCKED according to receipt truth.

## Council Member Assignment

Decision Council uses these three parent councils:

- `decision.voices_council`: Strategy, Systems, Factory, Feynman, and Hume children.
- `decision.six_hats_council`: Blue, White, Red, Black, Yellow, and Green children.
- `decision.experts_council`: Domain Specialist, Operator, Outside Evaluator, Adversarial Reviewer, and Standard Checker children.

Failure Council uses these three parent councils:

- `failure.premortem_council`: Likely Failure, Dangerous Failure, Hidden Assumption, Early Warning, Revised Plan, and Sim/Evidence Corruption children.
- `failure.falsifier_council`: Popper, Pushback, Calibration, Receipt Audit, and Boundary Check children.
- `failure.loophole_auditor_council`: Strategy Under Test, Evidence Standard, Find All Loopholes, Fix Plan, Verify Fixes, and Confidence Status children. It loads `skills/council-members/loophole-auditor/SKILL.md` and interprets "100% confident" as no known unresolved loophole under the declared evidence standard, not literal certainty.

There is only one Six Hats council in the default 3x3 shape:
`decision.six_hats_council`. Do not run a second Failure Six Hats council by
default. Failure pressure belongs to Premortem, Falsifier, and Loophole
Auditor.

The retained Six Hats coverage is deliberative and lives in Decision. Failure
does not need a second hats rotation: Black-hat risk pressure is carried by
`failure.falsifier_council` and `failure.loophole_auditor_council`, while the
Premortem remains a separate future-failure method.

`failure.premortem_council` is mandatory for every substantive Wizard run. A Failure
Council that runs Black Hat, Popper, Pushback, calibration, or expert critique
but does not run `failure.premortem_council` has not completed the Failure Council. It
must retry the premortem lane once with a smaller, sharper future-failure card
before Follow-Up synthesis. If the retry cannot run because of a real runtime,
access, safety, or timeout blocker, the visible output must mark Failure
partial/blocked and the `Members:` line must show `Premortem 0/N blocked`.
Do not replace premortem with generic risk prose, Black Hat, Popper,
postmortem, or receipt audit.

`failure.premortem_council` is bound to the Premortem skill. In Codex, load
`skills/premortem/SKILL.md` before running that
parent. The parent must use the skill's prospective-hindsight frame: "it is
six months from now; the plan has failed"; gather the plan, stakeholders, and
success criteria; generate raw failure reasons; run or degrade the deep-dive
agent wave; synthesize Most Likely Failure, Most Dangerous Failure, Hidden
Assumption, Revised Plan, and Pre-Launch Checklist; and return receipt fields
without creating reports, transcripts, HTML, or opening a browser. A non-skill risk paragraph
is not a completed premortem.

Premortem must discover failure modes beyond the user's already-stated
complaints. If every load-bearing failure reason is just a restatement of the
user's critique, the premortem member is partial. Each accepted premortem child
must return `failure_story`, `hidden_assumption`, `early_warning_signs`, and
`prevention`; otherwise it is not countable child evidence.

Substantive Codex-adapter Wizard runs are also bound to Claude Bridge when
Claude external-worker capacity is available. Load `skills/claude-bridge/SKILL.md`
and use the packet-local wrapper scripts under `skills/claude-bridge/scripts/`.
Claude work counts only when a wrapper receipt records terminal status, model,
output path, receipt path, and usable route signal. Claude prose without a
receipt is advisory only.

`failure.premortem_council` is not a label-only risk paragraph. In every substantive
Wizard run it must do real prospective-hindsight work: a future-failure story,
hidden assumption, early warning signs, and prevention. If that evidence is
missing, the Failure Council is partial even when other failure members ran.

Failure output must be load-bearing before Follow-Up task cards are drafted.
The `premortem_follow_up_join_gate` maps every open premortem finding into one
of four dispositions: `out_of_scope`, `stop_condition`,
`required_hardening`, or `dismissed_by_artifact`. If an open finding is not
mapped, the compiled move is `blocked` or `split_smaller`, not runnable.

Follow-Up Council uses these three parent councils:

- `follow_up.prompt_voice_council`: Orwell, Strategy, Factory, and Hume children.
- `follow_up.lane_council`: Direct, Alternative, Reframe, Back, Wildcard, and All-of-the-Above children.
- `follow_up.compile_gate_council`: Target, Action, Owner, Success Check, Stop Condition, Artifact Surface, and Status children.

Individual lanes and composition labels are not default council parent seats.
They shape option generation, prework, and the visible follow-up cards through
`follow_up.lane_council`.

The universal compile gate runs after Follow-Up synthesis. `guard.compile_gate`
may be selected as an explicit guard for difficult runs, but it is not required
as a default parent member when the post-council compile gate is already
enforced.

Post-council gates are mandatory and non-voting:

- the post-Follow-Up compile gate runs after Follow-Up and must pass before any
  option is called ready, runnable, executable, or preworked;
- the divergence preservation gate runs after each council synthesis and
  verifies that parent receipts cite child receipts, preserve dissent, and name
  killed or dropped options;
- the sim-admissibility gate runs for sim/probe/queue-visible work and returns
  one exact bounded packet or `blocked_none_ready`.

Runner construction and validation must use the same strictness predicate:
explicit strict classification or detected sim/probe/queue-visible surface in
the prompt, source context, or bounded-work gate. If strictness is detected from
surface language but no explicit strict packet is supplied, the runtime must
return `blocked_none_ready`, not fabricate a generic packet. A blocked universal
compile gate is contagious: visible output, handoff, score, and follow-up
language must all remain blocked until a later artifact clears the gate.

Runtime status matrix:

- non-sim work with a passing universal gate: no sim-admissibility gate, general
  bounded-work status decides readiness;
- detected sim/probe/queue-visible surface without an explicit strict packet:
  `BLOCKED`, `adapter_status: blocked`, `result: blocked_none_ready`;
- explicit sim/probe/queue-visible classification without a strict packet:
  `BLOCKED`, `adapter_status: blocked`, `result: blocked_none_ready`;
- supplied strict packet: may produce `one_exact_packet` only when it carries
  the current `source_task_ref`, `source_context_digest`, and
  `source_receipt_bundle_digest`; stale or unbound strict packets remain
  `BLOCKED`.

Parent receipts that launch children must carry a child impact ledger. Each
child is marked `changed`, `killed`, `added`, `rejected`, `blocked`, or
`no_delta`. `no_delta` children do not count toward child quorum. Parent
synthesis must cite at least two child receipts when three or more children ran,
and must preserve dissent or explicitly state `no_dissent_observed`.

All visible full runs should use dedicated parent workers for the nine nested
parent councils: Decision Voices, Decision Six Hats, Decision Experts,
Premortem, Falsifiers, Loophole Auditor, Follow-Up Prompt Voices, Follow-Up
Lanes, and Follow-Up Compile Gate. Controller synthesis may summarize them,
but it cannot replace them.

## Ratchet Exploration Mode

Wizard v4.1 is conservative at advancement gates and expansive in candidate
generation. The runtime should not become cautious in the places where ordinary
LLM behavior is already cautious. It should push many bounded alternatives,
falsifiers, source slices, model/reasoning variants, lego targets, and
child/subsubagent readings through the strict gate.

Failures are not wasted when they are specific. A blocked child, killed option,
failed sim packet, demoted tool role, or rejected follow-up can strengthen the
ratchet when it records the exact boundary, falsifier, demotion condition, or
missing evidence. The gate remains strict; the search before the gate remains
wide.

Rerouters support this mode. They keep liveness, shrink stalled work, and
reboot poorly initialized members so wide exploration does not become
deadlocked or decorative. They do not loosen the gate or promote a candidate.

## Wizard Loop Mode

Loop mode repeats the full Wizard barrier sequence until a goal, loop cap,
confidence gate, or hard blocker stops the run.

Management starts before voting parent routes. `manager.rerouter`,
`manager.child_health`, `manager.route_truth`, and
`manager.resource_pressure` must initialize a live state table before Decision
parents launch. "From start" means before task cards or child batches are
issued, not after a parent stalls. The management state table records active
parents, active child batches, liveness deadline, reroute action, model-family
status, compile-gate status, and terminal disposition. If this table is absent
until render time, the loop is partial.

Premortem and Loophole Auditor are distinct gates. Premortem asks: "it is six
months from now and this move failed; what happened?" Loophole Auditor asks:
"given the current strategy and evidence standard, what known loopholes remain
and what loop input fixes them?" If their receipts collapse to the same finding
without different evidence paths, the Failure Council is partial and must rerun
one of them with a sharper task card.

Loop state:

```yaml
wizard_loop:
  goal:
  loop_index:
  loop_cap:
  current_strategy:
  selected_next_prompt:
  receipts_used:
  unresolved_loopholes:
  confidence_standard:
  confidence_status: open | sufficient | impossible | blocked
  cross_loop:
    prior_loop_id:
    supersedes:
    kills:
    extends:
    new_findings:
    resolved_findings:
    unchanged_findings:
  next_action: run_next_loop | execute | launch_autoresearch | split_smaller | stop
```

Each loop must run Decision, Failure, and Follow-Up. It must not keep polishing
one prompt when the Systems, Strategy, Factory, Premortem, or Loophole Auditor
skill says the whole target should change.

The confidence loop driver is:

```text
Are you 100% confident in this strategy? If not, find all possible loopholes,
suggest proper fixes, and run this loop until you are factually 100% confident
in the new strategy.
```

Runtime interpretation: factual 100% confidence means no known unresolved
loophole remains under the declared evidence standard. If the standard cannot
be met, the loop must say so and return the strongest surviving strategy,
remaining loopholes, and exact evidence needed. It must not manufacture
certainty.

If the user gives a loop cap, use it. If no cap is supplied, the Loophole
Auditor subloop defaults to three repair attempts before returning
`confidence_status: impossible | blocked | open` with the strongest surviving
strategy and the exact evidence still needed. A configured higher cap, such as
10 loops, overrides the default but does not waive the stop conditions.

`Done` is operational: two consecutive loops with no new load-bearing findings,
all open findings resolved or explicitly accepted as residual risk, and a
separate audit fixed point. A loop after the first must cite prior finding ids
in `cross_loop`; otherwise it is a new prompt, not a loop. Rewording a prior
finding without superseding, killing, extending, or resolving it does not
advance the loop.

`cross_loop` is a join gate, not a note field. Loop iterations after the first
must cover every prior load-bearing open finding exactly once in
`cross_loop.dispositions`. `extends` requires a new delta; `resolved` requires
an artifact or clause reference; `unchanged` requires a reason it remains
load-bearing. Missing, duplicated, or rationale-free dispositions block the
loop counter.

For `extends`, `resolved`, or `supersedes`, the loop must cite the active
artifact or clause digest after the current edit. `extends` must name a
material delta since the prior loop, not a synonym or restatement. If the
digest is stale, placeholder, malformed, or unchanged while the disposition
claims progress, the finding remains open.

Read-only premortem or audit loops are explicit: set
`wizard_loop_state.loop_kind: read_only` or `audit_only`. These loops may keep a
prior finding `unchanged` against the same active digest without fabricating a
fresh edit. They cannot resolve an edit-required finding unless the already
existing artifact satisfies the fix and a validator recomputes the cited
digest.

When the full cross-loop ledger grows past the visible cognitive-load budget,
write or cite it as `cross_loop.dispositions_ref` and render only
`disposition_summary`. The validator must still inspect the full referenced
ledger before accepting loop advancement.

The audit fixed point requires independent audit receipts, not controller
self-certification. Minimum fixed point: two consecutive audit receipts from a
worker id distinct from the synthesizing controller, both with zero new
load-bearing findings against the same strategy and receipt bundle. Record the
audit receipt ids in `done_predicate.audit_receipt_ids`.

The two audit receipts must also record an independence vector. Distinct
worker ids alone are not enough. At least one of model family, runtime/account,
prompt seed/digest, sampled receipt-bundle digest, or adversarial task card
must differ. Shape-identical sibling audits under one controller prompt are
not an audit fixed point.

Model-label-only or timestamp-only prompt seed differences do not count. The
audit fixed point must be validated against actual receipt fields, not the
natural-language `divergence_vector` string.

Audit fixed-point validation reads structured receipt fields. At least one
accepted audit pair must set `structural_axis_verified:true` and must not be
timestamp-only or model-label-only. Prose claims of independence cannot close
the loop.
The validator computes the structural axis from primitive receipt fields and
ignores the receipt author's boolean if the primitive fields do not differ.
Use the boolean only as a cached result after recomputation.

Premortem loop modes:

- `cold_premortem`: no tools, no file reads, no child claims. It may produce
  useful failure hypotheses, but it cannot claim the packet-local skill body was
  read or that child/subagent hierarchy ran.
- `council_premortem`: read-only packet/skill load plus receipt-backed Opus
  high premortem analysis. This is required before a Wizard loop can close a
  premortem-driven strategy as done.

Premortem receipts must separate `skill_method_invoked` from
`skill_body_read`. `skill_body_read:true` requires the packet-local
`skills/premortem/SKILL.md` body to have been read by the worker or a concrete
read blocker to be recorded.
They must also include a short `skill_body_quote_anchor` or
`body_quote_anchor` whose hash is recomputed from the packet-local skill body.
This prevents controller-level worker-id spoofing from passing as same-worker
skill-body provenance.

When the runtime has no spawn surface for a substantive Wizard route, it must
emit `BLOCKED` with the missed parent/child obligation. It must not collapse
the obligation to `children:0/0`, and it must not call the run `FULL`.

When a substantive Codex-adapter run has only partial child-model surface, it
must be `PARTIAL` unless every required family either completed or has a
smaller-retry/degraded receipt accepted by `manager.resource_pressure`. A
single available spawn family does not satisfy the child matrix.

The FULL/PARTIAL renderer must read `manager.resource_pressure.model_family_statuses`
and `degraded_alt_child_families` before emitting the header. Family coverage
is header-blocking, not a footer note.
If a required family key is missing from `model_family_statuses`, treat that
family as blocked for header computation. The renderer must not infer success
from silence.
The substantive Codex-adapter classifier is receipt-derived. If accepted
parent, child, management, or bridge receipts use Codex-native, Claude Bridge,
Opus, Sonnet, Haiku, Gemini, or OMX/tmux surfaces for Wizard route truth, the
run is substantive for model-family accounting unless an explicit
atomic/low-decomposition override was accepted before rendering. Tool and
harness checks are reported under `tools:{n}` and do not activate model-family
accounting by themselves.

Loop closeout separates premortem hypotheses from load-bearing findings.
Premortem may generate raw hypothetical failures every loop. Only findings
promoted to `load_bearing_for_done:true` count against the done predicate and
reset the consecutive-empty counter.

## Codex Autoresearch Integration

The Wizard may call codex-autoresearch when the selected next move is a
measurable repeated improve/verify loop. The Wizard prepares the launch packet:
goal, scope, metric, direction, verification command, guard, loop/iteration
cap, run tag, stop condition, and foreground/background recommendation.

For interactive launches, codex-autoresearch keeps its ask-before-act rule. The
Wizard may recommend and prepare the run, but it must ask for the required
launch approval and run-mode choice before starting foreground or background
autoresearch. For non-interactive `exec` mode, the launch packet must already
be fully configured.

Autoresearch results are loop-runtime evidence. They can feed the next Wizard
loop, but they do not replace Decision, Failure, Follow-Up, parent children,
Premortem, or compile-gate receipts.

## Child/Subsubagent Rule

Parent workers spawn children for useful divergence. A counted parent does not
get child credit from a single child. One child per parent is route theater
unless the task is explicitly atomic and the override is recorded before
synthesis. Most children should be
narrower than the parent, but "no exact child implementation task" is not a
valid blocker. A child can always contribute one bounded independent signal:
same prompt with a different model or reasoning level, mini-MMM salience check,
outside-frame critique, falsifier, source-slice scout, receipt audit,
follow-up prompt improvement, or boundary-condition review.

Useful child work includes:

- inspect one source slice;
- test one claim;
- run one tool surface;
- compare one alternative;
- audit one receipt;
- compile one follow-up option.
- run the same invariant with a different model/runtime/reasoning level;
- test whether the parent task card or mini-MMM initialization was poor;
- produce one adversarial, outside-frame, or independent sanity-check reading.

Children do not synthesize the whole answer.

Children do not count unless their parent launch and child completion are both represented in receipts.

Each parent that launches children also owns a local child rerouter. Parent-local child rerouters are required for counted child health. The global
`manager.rerouter` watches councils and resource pressure, but it does not
replace parent-local child health. If a child times out, returns a started-only
stream, produces `no_delta`, or comes back shape-identical to a sibling, the
parent must reroute one smaller child task before returning, unless the child
was explicitly non-load-bearing and can be marked `deferred`.

Runtime capacity is not a reason to give up on child labor. If a launch returns
`agent thread limit reached`, `too many agents`, or an equivalent capacity
failure, the parent/controller must close or release completed agents whose
receipts have already been collected, then retry the missed child lane as a
rolling batch at the observed capacity ceiling. Only after cleanup plus one
smaller retry fails may the child be marked `blocked`. The rerouter ledger must
record the capacity error, completed-agent release, retry batch size, retry
result, and any remaining child obligation. A parent that returns after a
thread-limit error without this cleanup/retry ledger failed child quorum.

The global parent/council liveness ledger is `manager_rerouter`. It records the
parent receipt ids it watched, each parent terminal state, slow/rerouted/blocked
parent ids, the action taken, an addressable evidence reference, and terminal
disposition. It can mark a council run partial or blocked, but it cannot vote
and it cannot substitute for a parent-local `child_rerouter`.

Use `blocked` only for real runtime, access, safety, timeout, or destructive-scope
failures. Do not mark a child blocked because the parent cannot think of a
coding task for it. Reroute to a same-prompt variant, scout, falsifier, salience
check, or receipt audit first.

When children/subsubagents are used to compare models or reasoning levels, each counted child must record `variant_signature.model` and `variant_signature.reasoning_effort`, plus the exact task card, source slice, operation/falsifier, usable work product, distinct delta, `outcome_delta`, `work_unit_fingerprint`, `blind_spot_declaration`, and value score. A model/reasoning variant that only changes the label, repeats the same answer, lacks a usable work product, returns `no_delta`, shares a sibling `work_unit_fingerprint`, or scores below `2/3` is redundancy, not evidence.

Countable `outcome_delta` values name what changed in the work, not how the
child graded itself: `changed_outcome`, `killed_option`, `found_evidence`,
`found_bug`, `load_bearing_boundary`, or `load_bearing_fixture`. `no_delta`,
clarification-only output, duplicated sibling work, and non-load-bearing prose
may inform the parent, but they do not satisfy child quorum.

For model/reasoning matrix runs, also record a `rerouter_ledger` row. Count only rows whose invariant stays fixed: the same claim, exact tool/function/API surface, and carrier/fixture. The ledger must show the requested model, requested reasoning level, parent receipt id, route, terminal disposition, evidence reference, action taken, and value score. `accepted` and `useful` rows may count; `slow`, `redundant`, `not_worth_it`, `rerouted`, `blocked`, `deferred`, `superseded`, and `simulated` rows are diagnostics, not plurality.

Observed model-routing defaults:

- scout, liveness, and rerouter ledger probes: `gpt-5.3-codex-spark` with low reasoning;
- route-truth, receipt-schema, and output-contract checks: `gpt-5.5` with medium or high reasoning;
- premortem, falsifier, and hidden-assumption checks: `gpt-5.5` with high reasoning;
- `xhigh` is reserved for named high-stakes falsifiers, not tiny ledger checks;
- stop after two consecutive variants add no new falsifier, evidence reference, or conclusion shift.

Cross-runtime role fit:

- Sonnet-high: broad sim reasoning, failure interpretation, packet shaping, and "what should shrink next";
- GPT-low / Codex-low: strict audits, manifest/queue/result consistency, route-truth checks, and "does this claim follow from the artifact";
- Haiku: cheap inventory, counting, path scan, and low-stakes liveness checks;
- Opus: arbitration, hard boundary calls, hidden-assumption review, and final disagreement resolution;
- Gemini: outside scout, alternate mathematical framing, independent sanity check, and non-Codex/non-Claude contrast;
- Codex controller: file edits, local runner execution, verification, Git/index safety, and final synthesis.

For every substantive Codex-adapter Wizard run where external models are
available, the child model matrix is an obligation, not a bonus. Include a
Codex-native child when native child capacity exists, plus countable
child/subsubagent coverage from the external model families:

- Codex-native: route-truth audit, strict artifact check, controller-bias contrast, or source-slice scout;
- Opus: arbitration, hard boundary calls, hidden-assumption review;
- Sonnet: broad reasoning, packet shaping, failure interpretation;
- Haiku: cheap inventory, counting, liveness, receipt bookkeeping;
- Gemini: outside-model contrast, alternate frame, sanity check.

This requirement is about divergent thinking and salience alignment, not about
proving that every child can edit code. Multiple children from the same family
are allowed and often useful: Sonnet can run broad reasoning plus failure
interpretation; Codex can run strict audit plus source-slice scout; Haiku can
run path count plus liveness check. They only count when they use distinct task
cards, sibling-unique work units, and artifact-facing deltas. If one family
fails, record the
concrete runtime/access/safety/timeout failure and reroute one smaller child
task once. If any family remains missing, the run is partial or blocked. Do not
call the run FULL from Codex-native children, Claude-only fanout, Gemini-only
fanout, or tool checks.

For sims, a useful cheap loop is:

```text
runner output -> GPT-low audit: does result JSON satisfy contract?
runner output -> Sonnet-high audit: what does the failure mean and how should the packet shrink?
optional Gemini scout: is there an alternate interpretation or missed invariant?
Opus arbitration only if the audits disagree on admission or boundary.
controller -> decide rerun / admit / discard.
```

Tool or harness checks are separate from child/subsubagent routes. They may appear as `tools:{n}` or verification, but they do not satisfy the child route requirement.

If child routes are expected but not launched, the visible header must show the missed obligation. For example, a three-council run with no child receipts should use `children:0/3 not-run`, not `children:0/0 not-run`.

## Follow-Up Execution Loop

A visible follow-up option is the next Wizard input, not an escape hatch from the Wizard.

When the user chooses a follow-up option, the main thread boots v4.1 again, loads the full MMM, runs Decision, Failure, and Follow-Up councils on that chosen option plus any preworked evidence from the previous answer, and then emits the next compiled move and next follow-up options.

Tiny option-selector inputs are not tiny Wizard scopes. `4`, `1-4`, `all`,
`All of the Above`, and similar selector-only prompts must be expanded into the
selected option plus current thread state, repo/source docs, packet docs, MMM
surfaces, prior prework, and relevant artifacts before council assignment. The
system may run a narrow patch inside that full loop, but it must not render the
answer as if only the selected option/test lane was the whole job.

If the full loop cannot run, the answer is `PARTIAL` or `BLOCKED` with missing
Decision, Failure, Follow-Up, parent, and child obligations named. A
repair-only/test-only report is not a successful Wizard answer.

The prior answer may prework follow-ups with Make/Assembly, Run/Scout, Audit/Improve, and local tool checks. That prework is evidence for the next Wizard run, but it cannot replace the next run's three council barriers.

Do not answer that no further action is authorized just because the chosen option was already displayed or the hook supplied no new text. The chosen option, prior prework, repo/docs/artifacts, and current verification surfaces are enough task material for a new Wizard loop unless they are unavailable or unsafe to inspect.

The Wizard is general. Follow-up prework can be docs inspection, test scouting, source research, refactor mapping, bug reproduction, implementation handoff drafting, or domain-adapter work. Sim runner prework is one adapter case, not the default identity of the Wizard.

For Codex Ratchet sims, local runner probes are cheap enough to be part of follow-up prework when the strict sim profile passes. A follow-up can queue or run one bounded local sim packet before the user chooses it if the packet has stage, claim, carrier/fixture, exact tool/function or admitted coupling, positive check, negative/boundary check, expected result path, prior receipts when required, and explicit sim status. The next input should audit, delete, retool, or rerun from that evidence instead of starting from a blank prompt.

Do not let cheap local sim output imply queue visibility, runner success, or scientific readiness by itself. It is a receipt surface to audit in the next Wizard loop.

The Premortem Council's open findings must join the follow-up loop. If the
premortem leaves an open failure mode, hidden assumption, early warning, or
prevention gap, every visible follow-up option either carries that finding as a
stop condition/hardening target or explicitly marks it out of scope. The
Follow-Up Council must not smooth premortem findings out of the next prompts.

For sim/evidence work, the Sim/Evidence Corruption child must block promotion
when it sees report-before-code, placeholder `TOOL_MANIFEST` reasons, missing
`classification`, missing classical `divergence_log`, uncited canonical result
paths, or a runner/result claim that is not backed by the exact result artifact.
These are not cosmetic lint issues; they are queue-readiness blockers.

## Autoresearch Integration

`codex-autoresearch` can be a Wizard Harness runtime for long improve/verify
loops, especially harness tuning and sim packet improvement. Use it when the
work has a mechanical metric, a bounded scope, and repeated iterations would
outperform a single patch.

The Wizard owns the epistemic shape: councils, members, premortem, compile
gate, follow-up prompts, and route truth. `codex-autoresearch` owns the loop
runtime: baseline, one focused change, verification, keep/discard, logging,
pause/resume, and foreground/background execution.

Do not launch an interactive autoresearch run from inside the Wizard without
the autoresearch launch choice. The Wizard may compile an autoresearch plan or
exec-mode packet, but a foreground/background interactive loop must follow the
`codex-autoresearch` launch rules. For sims, useful metrics include failing
strict sim-profile cases reduced, harness conformance cases added/passing,
runner preflight stability, and admitted micro receipts without queue-promotion
overclaim.

## Visible Output Repair Rule

The main thread must repair the visible answer before sending it. This is not optional polish; it is part of the run protocol.

Minimum repair checklist:

- real section headers: `## ✨ Answer`, `## 🏛️ Council Results`, `## ✅ Compiled Move`, `## 🧭 Follow-Up Options`, and final `## 🧙 Footer`;
- no bold pseudo-headings as substitutes for sections;
- header/footer route truth agrees across waves, parents, children, and tools;
- required child/subsubagent obligations are visible even when not run;
- compiled move has target, immediate action, owner/lane, success check, stop/failure condition, artifact/output surface, and status;
- each visible follow-up option has a copy-pasteable prompt, payoff, use condition, and stop/block condition;
- verification counts are tied to exact commands.

If this checklist fails, rewrite the visible answer. Do not report the failed draft.

## Management Parent Set

For Max Assembly, run four management parents alongside the council parents or
immediately after each council boundary:

- `manager.rerouter`: liveness, deadline, retry, and resource pressure;
- `manager.child_health`: parent-local child rerouter fields, child quorum,
  child retry, and missing-child obligations;
- `manager.route_truth`: header/footer agreement, parent/child/tool
  separation, runtime claims, MMM proof, and score truth;
- `manager.resource_pressure`: quota, timeout, model-family fallback,
  degraded-alt signals, and waste throttling.

Management parents have no vote. They can block, reroute, shrink, or require a
sharper child task. They cannot replace council members or synthesize the
answer. Header `parents:{n}` counts council parents; management receipts are
reported in proof/footer or a diagnostic line when useful.

For sim/probe/queue-visible work, the management parents must supervise live sim
surfaces, not just Wizard paperwork:

- `manager.rerouter`: queue liveness and runner preflight.
- `manager.child_health`: sim-admissibility gate, queue-readiness boundary, and
  formal sim profile.
- `manager.route_truth`: stage gate, expected result surface, and
  controller-read artifacts.
- `manager.resource_pressure`: runner preflight, model-family fallback, and
  degraded-alt child families.

If a sim-shaped run lacks these surfaces, the management layer is incomplete.
Do not treat the run as queue-ready or runner-safe.
Management parents also cannot admit their own supervised work. A sim pre-run
promotion that names `admitted_by: manager.*` is self-certification one layer up
and must fail like runner/controller/self-certified admission.

Guards such as `guard.receipt_audit`, `guard.receipt_divergence`,
`guard.compile_gate`, and `guard.hygiene` may run as child tasks under a
management parent, under a council parent, or as post-council gates. They are
not the management parent set by themselves.

Useful constrained Max Assembly is usually:

- 3-6 council parents per wave;
- four management parents per Max Assembly run, plus guard children where useful;
- 5-10 child/subsubagent tasks per counted parent, split by source slice, claim, falsifier, fixture, model/runtime, mini-MMM variant, or follow-up option.

Stress-test fanout may go wider, but useful runs should throttle down when added children produce shape-identical receipts.

A counted parent with fewer than five completed accepted child/subsubagent
receipts fails child quorum. A parent with more than ten child receipts needs a
stress-test label and a receipt-shape audit before its extra breadth can inform
synthesis.

For ordinary hardening work, prefer one controller plus three bounded lanes:

- an explore/map lane for current source truth;
- an execute/patch lane for one isolated target;
- a verify/audit lane for contracts, tests, and output shape.

Add an external scout only when it answers a specific uncertainty. Do not fan out for ceremony.

## Rerouter Rule

The rerouter watches liveness. It does not vote.

Default liveness thresholds:

- soft: 90 seconds without a useful receipt, file target, or clear progress;
- stall: 3 minutes without new evidence or narrower replacement;
- hard: 7 minutes per lane before close/reroute smaller.

The run is not worth more time when one obvious local edit and one verification command would prove the point, and extra lanes would only restate context instead of reducing risk or time.

Retry when:

- a required parent does not load its mini-MMM;
- a required parent returns generic synthesis instead of its member output shape;
- a child starts but does not return a usable receipt;
- a member drifts outside its task card;
- the compile gate fails but a smaller replacement is available.

Retry smaller, not broader.

## Retry States

Use these internal states:

- `planned`
- `launched`
- `active`
- `completed`
- `slow`
- `stalled`
- `timed_out`
- `rerouted`
- `superseded`
- `blocked`
- `deferred`
- `abandoned`
- `supplemental`

Only `completed` usable receipts count as ran.

## Retry Budget

For a normal full run:

- retry each required failed parent once with a smaller card;
- retry child fanout once per council with a smaller child task;
- after retry, mark blocked/deferred rather than hiding failure;
- if more than one required council remains under minimum, rerun the missing councils with smaller cards or report blocked.

## Member Reboot Rule

A member that became theater in one run is not automatically useless.

Before suppressing or retiring a member, classify the failure:

- bad task card;
- wrong source slice;
- prompt too broad;
- wrong model/runtime;
- role collapsed into another member;
- context not suited to that member;
- repeated cross-context uselessness.

Use `manager.member_rebooter` only when a reboot could change the decision, falsifier, evidence boundary, or compiled next move. It should produce one or two sharper initialization variants, not a large prompt bank.

Do not reboot for ceremony. If the rerouter says the member cannot change the answer, mark `cut_this_run` or `suppress_this_context` and continue.

## Automatic Rerun Rule

If the run header would say full but the receipts prove partial, do not output a fake full run.

First try one repair pass:

1. identify missing council/member/child;
2. rerun only the smallest missing part;
3. re-score;
4. if still below full threshold, report partial with blockers and a ready next prompt.
