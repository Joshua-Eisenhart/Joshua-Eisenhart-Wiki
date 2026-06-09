---
title: Wizard Full v4.1
type: runnable_wizard
packet: v4.1
mode: full
compiled_from: split_specs
---

# Wizard Full v4.1

This is the runnable FULL Wizard v4.1 document compiled from the active v4.1 packet docs. Load the FULL MMM first, then this file, then task/source material and any route-required local skill.

## Boot Shortcut

1. Load `mmm/main/full/md/MMM_MAIN_FULL_v4_1.md`.
2. Load this file.
3. Load `skills/SKILLS_MANIFEST_v4_1.md`.
4. Load task/source material.
5. For substantive Codex-adapter Wizard work, load `skills/claude-bridge/SKILL.md` when Claude capacity is available.
6. For `failure.premortem_council`, load `skills/premortem/SKILL.md`; it returns receipt fields only and does not create reports, transcripts, HTML, or open a browser.
7. For skill-backed council members, load the relevant embedded council-member skill from the compiled source below or the packet-local file under `skills/council-members/`.

## Compiled Source


---

# Source: `00_BOOT.md`


---
title: Wizard v4.1 Boot Contract
type: boot_contract
packet: v4.1
framing: standalone
---

# Wizard v4.1 Boot Contract

## Main Thread Boot

The main thread loads the selected main MMM first.

FULL mode:

```text
mmm/main/full/md/MMM_MAIN_FULL_v4_1.md
WIZARD_FULL_v4_1.md
skills/SKILLS_MANIFEST_v4_1.md
task material
source material
runtime adapter, if needed
skills/claude-bridge/SKILL.md, for substantive Codex-adapter external-worker routes
skills/premortem/SKILL.md, for failure.premortem_council
```

COMPACT mode:

```text
mmm/main/compact/md/MMM_MAIN_COMPACT_v4_1.md
WIZARD_COMPACT_v4_1.md
skills/SKILLS_MANIFEST_v4_1.md
task material
source material
runtime adapter, if needed
skills/claude-bridge/SKILL.md, for substantive Codex-adapter external-worker routes
skills/premortem/SKILL.md, for failure.premortem_council
```

The main thread owns synthesis, visible claims, final compile gate status, and user-facing output.

## Subagent Boot

A subagent loads only the material needed for its assignment:

```text
shared positive task summary
exact route/member mini-MMM
route-bound council-member skill, if assigned
assigned route/member card
source slice or tool surface
receipt schema
adapter binding, if needed
```

A subagent does not load the full MMM by default. It does not load every route definition unless its assignment is a composition or council role.
For worker boot, compact means compact member mini-MMM from
`mmm/mini/compact/...`, not the compact main MMM.

## Subsubagent Boot

A subsubagent is narrower than its parent.

It loads:

```text
parent route summary
exact child route/member mini-MMM
route-bound council-member skill, if assigned
child task card
source slice or tool surface
receipt schema
adapter binding, if needed
```

It exists to inspect one source slice, test one claim, run one tool surface, or produce one child receipt.
If no exact child mini-MMM exists, it loads the sparse registry slice plus
definition row, then nearest family fallback marked `mini_mmm_family_fallback`,
or blocks when no valid salience source exists.

## Route Truth

A visible member, voice, hat, expert lens, lane, guard, council, or composition counts as run only when a worker or tool actually ran and returned a usable receipt.

Controller synthesis is not a member.

Council agreement is not execution.

MMM salience is not execution.

Pending worker starts are not completed receipts.

## Header Shape

Use this only when visible route truth matters:

```text
🧙 Wizard v4.1 | {FULL|PARTIAL|BLOCKED} | waves:{completed/3}[ partial-coverage] | parents:{completed/required} | children:{completed/obligation}[ blocked|deferred|not-run] | [tools:{completed} | ]score:{0-100} | runtimes:{names}
```

`waves` means completed receipt-boundary passes. Parent and child counts do not multiply wave count.

`children` means completed child/subsubagent receipts over the current child route obligation. If the runtime supports child routes and the run required them, do not hide a missed obligation as `children:0/0 not-run`; show the obligation, for example `children:0/3 not-run`.

Use `COMPACT` only when `WIZARD_COMPACT_v4_1.md` and
`mmm/main/compact/md/MMM_MAIN_COMPACT_v4_1.md` were loaded.

If no councils actually ran, do not use a Wizard run header.

## Visible Output Self-Repair Gate

Before sending a visible Wizard answer, the main thread must perform one private repair pass over the drafted answer.

Repair, then send, when any of these are true:

- section labels are bold pseudo-headings such as `**Main Answer**` instead of Markdown headers like `## ✨ Answer`;
- the footer is not a real final `## 🧙 Footer` section;
- the first nonblank footer line is not `🧙 Time/value:`;
- follow-up options are labels without copy-pasteable prompts, payoff, use condition, and stop/block condition;
- a required compile-gate field is missing from the compiled move;
- the header counts tools as children;
- the header hides incomplete parent/member coverage behind plain `waves:3/3`;
- the header hides a required child route behind `children:0/0 not-run`;
- verification counts are not tied to exact fresh commands.

Do not ask the user to catch or approve these repairs. Fix the answer shape before sending.

## Stop Rule

The Wizard stops when the next bounded move is compiled, blocked, deferred, or executed and a useful visible answer has been emitted.

Stop does not mean idle-wait for "authorization" when source context is available. If a thread wakes with no new prompt, perform Ambient Start Mode: scan the available repo/docs/artifacts, infer the smallest useful bounded move, run the three council barriers as far as the runtime honestly allows, and render the next compiled move plus follow-up options.

Only ask for explicit input when the source context is missing, the next safe bounded scan cannot be inferred, or the next branch would be destructive or externally side-effectful.

---

# Source: `01_UNIVERSAL_THREE_COUNCIL_WIZARD.md`


---
title: Universal Three-Council Wizard v4.1
type: universal_model
packet: v4.1
framing: standalone
---

# Universal Three-Council Wizard v4.1

The Wizard is a bounded-work compiler.

It turns broad thinking, disagreement, critique, and follow-up generation into one or more executable bounded moves.

## Primary Job: Reduce Cognitive Load

The Wizard exists to make the next move easier for a human.

It should:

- read the room, repo, docs, or source context before asking for more input;
- surface only the important information;
- make the answer pleasant to scan;
- use a little warmth, structure, and visual rhythm;
- turn uncertainty into a small next move;
- produce follow-up prompts that reduce user effort.

If the user has to decode route machinery, the Wizard failed even when the receipts are true.

## Wide Search, Strict Gate

The Wizard is strict at the gate and expansive before the gate.

The compile gate is intentionally conservative: a move advances only when it
has an addressable target, action, owner, success check, stop condition,
artifact surface, and status. Adapter profiles may add stricter fields for
their own domains, but those fields are adapter-specific.

That strictness is not a reason to make the search conservative. The Wizard
should use broad, sometimes wild exploration inside bounded task cards: many
voices, hats, model variants, falsifiers, scouts, candidate targets, prompt
variations, and nested worker readings. Most candidates are allowed to
fail. A failed variant that names a falsifier, boundary, demotion condition, or
reason it cannot pass is useful evidence for the ratchet.

The system advances by letting many possible futures contend against a strict
present gate. Agreement, salience, and receipt shape do not promote work. They
only help generate candidates that the gate may accept, shrink, reroute, or
reject.

## Ambient Start Mode

The Wizard can run with no initial prompt.

When no prompt is supplied, it should inspect available source context and infer the smallest useful bounded move.

This is not an authorization gap. Empty input, a hook wake, a resumed thread with no new user text, or a chosen follow-up option should all be treated as Wizard input when source context is available.

Do not answer with "waiting for the next explicit input," "no further action is authorized," or equivalent idle language unless source context is missing and no safe bounded scan can be performed.

Minimum ambient context:

- source surfaces inspected;
- inferred target;
- evidence boundary;
- why this target matters now;
- one bounded next action;
- stop condition.

Prompted runs are allowed. Promptless runs are first-class.

## Three Sequential Councils

### Wave 1: Decision Council

Purpose: choose the smallest useful bounded move now.

It should preserve live alternatives, name the evidence boundary, and pass risky claims forward to Failure Council.

Return:

- selected bounded move;
- one or two live alternatives;
- evidence boundary;
- accepted risks;
- risky claims for Failure Council;
- falsifier seed.

### Wave 2: Failure Council

Purpose: assume the selected move may fail, then kill, block, split, harden, or pass it.

Mandatory premortem binding: the Failure Council's Premortem member is
`failure.premortem_council`, and in Codex it must load
`skills/premortem/SKILL.md`. The Wizard may route
and receipt the premortem, but the prospective-hindsight method comes from the
Premortem skill. Generic risk prose, Black Hat critique, Popper falsification,
or a label named "Premortem" does not satisfy this member.

Return:

- operational outcome: `pass_to_execution`, `split_smaller`, `harden_then_execute`, `block_for_missing_input`, or `kill`;
- target claim;
- strongest falsifier;
- decisive check;
- hidden assumption;
- required hardening;
- early warning signs;
- whether control returns to Decision Council.

Failure Council should avoid two failures: rubber-stamping because the move sounds bounded, and blocking everything without returning a smaller executable replacement.

### Wave 3: Follow-Up Council

Purpose: generate divergent next moves and compile useful ones into executable prompt options.

Return visible options only when each has:

- target;
- immediate action;
- owner/lane;
- success check;
- stop condition;
- artifact/output surface;
- status;
- payoff;
- use condition;
- blocker/defer condition.

## Sequential Barrier Rule

The councils are sequential write barriers.

Parallelism happens inside a wave. Wave 2 reads Wave 1 results. Wave 3 reads Wave 2 results. A later council does not rewrite an earlier council silently; it returns control explicitly if needed.

## Council Identity Lock

The three councils are always:

1. Decision Council.
2. Failure Council.
3. Follow-Up Council.

Do not rename the three councils to the current option sequence, route labels, lanes, tools, or proof tasks.

Examples of invalid council replacement:

- `Proof`, `Premortem`, `Scout`;
- `Make`, `Run`, `Audit`;
- `Direct`, `Alternative`, `All of the Above`;
- `Route-Truth`, `Verification`, `Cleanup`.

Those can be lanes, follow-up options, subroutes, or child tasks inside the real councils. They are not the three councils.

A chosen follow-up option is the next Wizard input. Boot the Wizard again and run Decision, Failure, and Follow-Up on the chosen option plus prior prework. If those councils cannot run, report a partial or blocked Wizard run with the missing council/member obligations instead of treating the option as outside the Wizard.

When a visible Wizard header says `waves:{n}/3`, `waves` refers only to completed Decision, Failure, and Follow-Up council barriers. It does not refer to option steps such as Proof -> Premortem -> Scout.

## Member Families

The Wizard can draw from these families:

- voices;
- Six Thinking Hats;
- failure lenses;
- expert lenses;
- lanes;
- compositions;
- guards;
- manager/rerouter.

Members are salience roles until a runtime adapter turns them into workers or tools with receipts.

## Anti-Theater Principle

The three councils exist to cut theater: the appearance of work, divergence, and many voices without decision value.

For now, visible full runs should call the full required member set so the system can learn which members produce useful signal. Over time, members may be tuned down, but only from member-utility receipts showing what each member contributed, what it changed, how it helped bounded work in the active adapter domain, and what theater it cut.

Council output should preserve wisdom, not ceremony. Show what changed, what was killed or hardened, and the compiled next move. Keep route machinery in receipts unless it changes the user's decision.

## General Bounded-Work Status

Use these statuses for ordinary work:

- `salience_only`
- `proposal`
- `bounded_work_candidate`
- `ready_for_execution`
- `executed`
- `accepted`
- `partial`
- `blocked`
- `deferred`

## Non-Sim Work

For documentation cleanup, bug triage, refactor planning, research synthesis, product strategy, hiring decisions, or implementation handoff, the universal bounded-work compile gate is enough.

Do not require adapter-specific packet fields unless the adapter classifies the task into that stricter profile.

## Max Assembly

Max Assembly is the maximum useful route-family integration.

It is not a quota to run every route.

It should combine useful work from prior routes into one coherent plan, prompt, or execution packet.

## Looping Wizard

Wizard v4.1 is a loopable skill system, not a one-shot prompt improver.

Each loop takes the current goal, context, receipts, failures, open questions,
and prior follow-up bank, then runs Decision, Failure, and Follow-Up again. The
Wizard may step back to inspect the whole system, strategy, queue, repo, or
artifact landscape before optimizing the local prompt. Local optimization is
allowed only after the Systems/Strategy/Factory pressure says the local target
is still the right target.

Loop control requires:

- a goal or bounded target;
- a loop cap or configured stop condition;
- receipt-backed parent and child work;
- a Failure Council loophole/premortem pass each loop;
- Follow-Up selection that chooses the next loop input instead of merely
  listing prompts;
- a compile gate that decides execute, loop again, split smaller, launch
  autoresearch, or stop.

The Wizard can generate next prompts, pre-run them, audit them, improve them,
select one, execute or delegate it, then loop. It stops when the goal is
reached, the loop cap is reached, confidence is sufficient for the configured
standard, or a hard blocker remains after one smaller reroute.

The prompt pattern:

```text
Are you 100% confident in this strategy? If not, find all possible loopholes,
suggest proper fixes, and run this loop until you are factually 100% confident
in the new strategy.
```

is a Wizard confidence-loop driver. In v4.1, "100% confident" means "no known
unresolved loophole remains after the configured evidence standard, child
coverage, and verification checks." It does not permit pretending certainty.
If literal certainty is impossible, the loop returns the remaining uncertainty,
the evidence needed to resolve it, and the safest compiled move.

---

# Source: `02_MEMBER_REGISTRY_AND_MINI_MMMS.md`


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

---

# Source: `03_RECEIPTS_AND_COMPILE_GATES.md`


---
title: Wizard v4.1 Receipts and Compile Gates
type: receipt_and_gate_contract
packet: v4.1
framing: standalone
---

# Receipts And Compile Gates v4.1

Receipts prove what ran.

Compile gates decide whether an output is actionable.

They are separate.

## Receipt Truth

A receipt records:

- route/member id;
- runtime;
- worker or tool id if available;
- source slice or tool surface;
- loaded mini-MMM or full MMM;
- task card;
- terminal status;
- output or artifact;
- evidence boundary;
- parent/child relation when applicable.

Completed means terminal completion plus usable evidence.

Started, streamed, pending, timed out, or self-described work is not completed.

## Anti-Theater Member Utility Gate

For visible full runs, every accepted parent member receipt needs:

```yaml
member_utility:
  distinct_contribution:
  decision_use:
  sim_relevance:
  theater_cut:
  current_disposition:
  reboot_note:
  initialization_assessment:
  suppression_scope:
  retirement_evidence:
```

The goal is not to keep every member forever. The goal is to measure which
nested parent councils and formal children changed the work: Decision Voices,
Decision Six Hats, Decision Experts, Premortem, Falsifiers, Loophole Auditor,
Follow-Up Prompt Voices, Follow-Up Lanes, and Follow-Up Compile Gate. A member
can later be tuned down only from this evidence, not from controller taste.
Individual voices, hats, lanes, experts, falsifiers, and compile-gate fields
change the work as child/subsubagent receipts under their parent council.

Nested child work is load-bearing only when the parent synthesis binds it.
Parent receipts must cite child ids, record dissent or state that none was
observed, name killed options, and include a child impact ledger. This is the
divergence preservation gate: child fanout that does not change, kill, add,
reject, or block anything is route theater, even when the child receipts are
real.

Do not accept a member as useful because it had a label, sounded wise, agreed with the council, or increased the count. It must name the distinct contribution it made, how it affected the compiled move, how it protects sim/proof/QIT bounded evidence when relevant, and what theater it removed.

Cutting theater is not the same as retiring the member. A member can fail because it was initialized poorly, loaded the wrong source slice, got too broad a task card, used the wrong model/runtime, or received a prompt that collapsed its role. Use `current_disposition` to distinguish:

- `kept`: useful in this run;
- `cut_this_run`: not useful enough to show or count here;
- `reboot_candidate`: likely worth retrying with a sharper card, source slice, model, or mini-MMM variant;
- `suppress_this_context`: probably not useful for this task shape;
- `retire_candidate`: repeatedly unhelpful across contexts, not from one failed run.

Use `reboot_note` to say what should change before retrying. Do not reboot automatically; retry only when it can change the decision, falsifier, evidence boundary, or compiled next move.

If `current_disposition` is `reboot_candidate`, `reboot_note` must name a concrete boot, task-card, source-slice, model/runtime, or mini-MMM delta. If `current_disposition` is `retire_candidate`, require repeated evidence across contexts; a single theatrical run can never retire a member.

## Universal Bounded-Work Compile Gate

Every visible executable option needs:

```yaml
bounded_work_compile_gate:
  target:
  immediate_action:
  owner_lane:
  success_check:
  stop_condition:
  artifact_output_surface:
  status:
```

The gate fails closed when its fields are only narrative completeness. The target and success check must point to addressable evidence: a file, command, result surface, receipt id, issue, document section, or other artifact a later worker can inspect.

For ordinary non-sim work, addressable evidence can be a doc path, test command, bug reproduction, implementation handoff artifact, or research source list.

For adapter-classified sim/proof/QIT work, addressable evidence is stricter and belongs in the adapter strict profile. Do not let a polished universal compile gate imply sim readiness.

The universal Wizard is not innately a sim-running system. It is a bounded-work compiler for docs cleanup, bug triage, refactor planning, research synthesis, implementation handoff, product decisions, strategy choices, and other work. Local sim runner output belongs to a domain adapter/profile.

For Codex Ratchet sim/proof/QIT work, local sim runner output is cheap evidence, not expensive deliberation. The Wizard may use it inside follow-up prework when the strict sim profile is present. The next Wizard loop should audit that runner evidence, delete or retool bad rows, and run another bounded local packet when useful. Nothing is promoted from "cheap local result" to "ready" unless the relevant compile gate still passes after audit.

The gate is strict so exploration can be broad. Failed candidates, failed
children, failed tool rows, rejected lego targets, and killed follow-up options
can still be load-bearing receipts when they name the falsifier, boundary,
demotion condition, or missing evidence. They support the ratchet by narrowing
what can advance; they do not advance themselves.

Allowed universal statuses:

- `salience_only`
- `proposal`
- `bounded_work_candidate`
- `ready_for_execution`
- `executed`
- `accepted`
- `partial`
- `blocked`
- `deferred`

## Adapter Domain Profiles

Adapters may add strict profiles for special domains.

A strict profile must not become universal. It activates only when the adapter classifies the task for that domain.

When a strict profile activates, the universal gate is not enough. Council agreement, salience, member utility, and receipts about framing do not prove execution readiness.

Example strict domain profile:

```yaml
strict_packet_compile_gate:
  stage:
  claim:
  carrier_or_fixture:
  exact_tool_or_function:
  positive_check:
  negative_or_boundary_check:
  expected_result_surface:
  prior_receipts:
  adapter_status:
```

## Sim Loop State Gate

For Codex Ratchet sim/proof/QIT adapters, cheap local pre-runs may be useful before admission, but their loop states must not self-promote.

Illegal transition:

```yaml
from_state: pre_run_passed_unadmitted
to_state: queue_ready | admitted_evidence | admitted
admitted_by: null
```

That transition is blocked unless a separate non-runner admission gate writes `admitted_by`, an addressable `admission_artifact`, and the controller reads that artifact before advancing.

Every `next_input_ready` packet must carry a freshness gate: checked timestamp, git status reference, ledger reference, queue reference, runner-preflight reference when sim-related, and source artifact references. Stale prework is evidence to audit, not permission to execute.

Before rendering a visible Wizard answer, the pre-output route-truth gate must bind the newest request, receipt bundle path and digest, accepted child receipt ids, runtime receipt refs, child obligation status, header counts, and final output artifact into one joined `current_input_hash`. A green manager rerouter ledger is not enough if the joined hash still points to stale, foreign, or fallback-only receipt truth.

Runner success cannot self-certify advancement. A worker or runner summary counts only after the controller reads the cited result JSON or receipt artifact and records it in `controller_read_artifacts`.

## Next-Input And Pre-Output Route-Truth Gate

A next-input handoff is not durable just because freshness, receipts, and output formatting each look valid in isolation.

Before rendering a visible Wizard answer for a promptless wake, chosen follow-up option, resumed thread, or next-input packet, the runtime must join:

- active input identity or hash;
- newest request reference;
- receipt bundle path;
- receipt bundle digest;
- runtime receipt references;
- current child obligation status;
- handoff path;
- compiled move reference;
- freshness gate reference;
- accepted parent receipt ids;
- accepted child/subsubagent receipt ids;
- rendered header counts;
- runtime labels proven by receipts or tools;
- final output artifact surface;
- controller synthesis boundary.

This join is the pre-output route-truth gate. It prevents a thread from answering an older task, reusing prior-run receipts, hiding child obligations, counting tools as children, or emitting a worker log that happens to contain enough correct-looking sections.

If the join is missing or disagrees with accepted receipts, the output is blocked or rerun smaller. Controller synthesis can summarize the receipts, but it cannot replace the joined route truth.

## Source-And-Lift Receipt

Use this when MMMs, wiki material, memory, or prior documents shape the output.

```yaml
source_and_lift_receipt:
  source_slice_used:
  salience_surface_loaded:
  reasoning_move_changed:
  execution_evidence:
  evidence_boundary:
  what_this_does_not_prove:
  counterprobe:
  status:
```

Source-and-lift can prove framing quality. It does not prove the work itself succeeded unless execution evidence also exists.

## Receipt Divergence Gate

Before synthesis claims a plural council result, compare accepted receipts structurally.

Required comparison fields:

```yaml
receipt_divergence_fields:
  core_claim:
  reasoning_path:
  evidence_anchors:
  operation_or_falsifier:
  conclusion_direction:
```

Allowed classifications:

- `PATH_IDENTICAL`
- `DECORATIVE_SPLIT`
- `CONVERGENT_SIGNAL`
- `HEALTHY_DIVERGENCE`
- `SINGLE_ANSWER`

`PATH_IDENTICAL` and `DECORATIVE_SPLIT` trigger one smaller rerun with sharper task cards. If the rerun still collapses, block synthesis instead of pretending the council added signal.

`CONVERGENT_SIGNAL` is allowed when different structural paths reach the same conclusion. Legitimate agreement is not a failure.

Rejected, killed, or demoted candidates can still be structural signal when
they name the exact falsifier, boundary, demotion condition, or missing
artifact. They are not retry noise unless they fail to narrow the next
admissible move.

Structural fields must be meaningful, not merely present. Missing keys, `null`, empty strings, empty lists, empty maps, or wrong-shape values block synthesis as missing structural evidence.

Do not use prose similarity, word overlap, embeddings, tone, or route labels as proof of divergence.

## Deliberator Contract Gate

The receipt divergence gate checks whether plural work contains structural
signal. The deliberator contract checks whether controller synthesis preserves
and uses that signal.

The serialized trajectory cache must not turn receipts into clean but
uninspectable memory. Every cached trajectory keeps `trajectory_id`,
`source_receipt_id`, `evidence_anchor`, `operation_or_falsifier`,
`executable_delta`, `dissent_or_anomaly`, `pruning_reason`, and
`evidence_boundary`.

Every plural synthesis carries `deliberator_contract` with `query_class`,
`per_thinker_verdict`, `all_wrong_rederive`, `minority_report`,
`format_alignment_check`, and `status`.

If every thinker is wrong, stale, unsupported, or non-load-bearing, the
controller must re-derive from source material or block. It must not average
wrong receipts into a polished answer.

If a low-frequency trajectory is strange but testable, synthesis must preserve
it as a minority report, promote it to a bounded falsification task, or kill it
with an addressable artifact. Quiet pruning is blocked.

## Failure Council Outcomes

Failure Council can return:

- `pass_to_execution`
- `split_smaller`
- `harden_then_execute`
- `block_for_missing_input`
- `kill`

If it blocks, it should name the missing input.

If it splits, it should return the smaller executable replacement.

If it kills, it should say what would have to change before reconsidering.

---

# Source: `04_FOLLOW_UP_COUNCIL.md`


---
title: Wizard v4.1 Follow-Up Council
type: followup_contract
packet: v4.1
framing: standalone
---

# Follow-Up Council v4.1

Follow-Up Council makes divergent good next prompts.

It should generate a broad internal bank, then show only the useful few.

The visible options should reduce human cognitive load. They should feel like good choices, not internal route names.

## Follow-Up Option Shape

Each visible option needs:

```yaml
label:
prompt:
payoff:
use_when:
blocked_if:
pre_run_check:
audit_fix:
first_action:
target:
immediate_action:
owner_lane:
success_check:
stop_condition:
artifact_output_surface:
status:
```

## Follow-Up Deepening Loop

Visible follow-ups should be preworked before the user sees them.

Run this loop internally:

1. **Make**: generate divergent candidate prompts.
2. **Pre-run**: mentally or read-only walk each option through the first action, likely artifact, and first blocker.
3. **Audit**: check for ambiguity, scope creep, missing success check, missing stop condition, and hidden dependency.
4. **Improve**: rewrite the prompt so it is clearer, smaller, and easier to execute.
5. **Select**: show only the useful few.

For loop mode, **Select** also chooses the next Wizard input. The selected
prompt is not outside the Wizard; it becomes the next loop's task material
together with current receipts, context, open blockers, and the goal state.

The bank can be wide. A broad or wildcard follow-up is useful when its pre-run
returns an exact falsifier, boundary, demotion condition, missing-evidence
record, or smaller replacement. It is not useful when it only adds options,
labels, or agreement.

The visible option can summarize this as one short `Pre-checked` line. Do not expose the whole internal audit unless diagnostics are requested.

Visible wording should use:

- short labels that describe the human choice;
- a little visual character, such as a relevant emoji;
- plain-language payoff;
- the first action;
- the pre-check result;
- clear "use this when" and "do not use if";
- no raw route bookkeeping unless diagnostics are requested.

Show three to four options. If more than one option is genuinely useful, include an `All of the Above` option that sequences them safely.

## Useful Lanes

- Direct: do the smallest useful next move.
- Alternative: try a different route to the same goal.
- Reframe: change the object, unit, or premise.
- Back: retreat to the last stable smaller move.
- Wildcard: run one off-axis probe with a concrete payoff.

## Useful Compositions

- All-A Build: build plus mechanism, falsifier, alternative, audit.
- All-B Divergence: preserve alternatives and test collapse.
- All-C Closeout: clarity, safety, handoff, receipt audit.
- Max Assembly: integrate all useful candidates into one non-contradictory maximum plan.

## Combined Prompt Option

When several follow-ups are all useful, include one combined option.

The combined option should:

- sequence the moves;
- remove contradictions;
- pre-run the sequence;
- audit the handoffs between options;
- keep the first action small;
- include a stop condition;
- include an artifact/output surface.

Do not give the combined option a generic all-routes name. Use "Max Assembly" only when it means maximum useful integration.

Use `All of the Above` when the user-facing meaning is "do these useful options in sequence." Use `Max Assembly` when the system-facing meaning is maximum useful route integration.

## Loop Selection

When the Wizard is running toward a goal or loop cap, Follow-Up Council returns
one selected next prompt plus alternates. Selection should consider:

- whether this prompt advances the overall goal, not only the local artifact;
- whether Systems/Strategy/Factory found a reason to step back;
- whether Failure Council left a loophole that must be closed first;
- whether the prompt can be verified mechanically or by receipt;
- whether codex-autoresearch should own the next repeated improve/verify loop.

The selected prompt should include the payoff, use condition, stop condition,
artifact surface, and verification command or receipt check when available.

---

# Source: `05_RUN_PROTOCOL_AND_RETRY.md`


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
- `failure.loophole_auditor_council`: Strategy Under Test, Evidence Standard,
  Find All Loopholes, Fix Plan, Verify Fixes, and Confidence Status children.
  It loads `skills/council-members/loophole-auditor/SKILL.md` and interprets
  "100% confident" as no known unresolved loophole under the declared evidence
  standard, not literal certainty.

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

---

# Source: `06_OUTPUT_FORMAT_AND_SCORING.md`


---
title: Wizard v4.1 Output Format and Scoring
type: output_contract
packet: v4.1
framing: standalone
---

# Output Format And Scoring v4.1

The visible answer should be readable, structured, and useful.

It should not look like a raw log.

The visible answer should reduce cognitive load. It should feel pleasant to the eye and mind: short sections, useful labels, a little visual character, and no route machinery unless it helps the user decide.

## Cognitive Load Budget

Default visible output should fit this shape:

- one clear answer;
- one short context-aware voice block for Strategy, Systems, and Factory when the run is about the Wizard or a broad work system;
- three short council result blocks;
- one compiled move;
- three to four follow-up options;
- one footer.

Avoid:

- raw worker logs;
- long route inventories;
- duplicate caveats;
- more than four visible follow-up options;
- asking the user for a prompt when source context is enough.

## Beauty And Readability Gate

Wizard output is a user interface, not a receipt dump. A technically accurate
answer still fails if the user has to parse it like a log.

Before sending, apply this visible-surface filter:

- `## ✨ Answer` starts with the accepted outcome in one or two plain
  paragraphs. It does not open with paths, route counts, stale queue inventory,
  or command results.
- File paths are used only when they are the artifact the user should care
  about. Do not stack three or more file links in the opening answer unless the
  task is specifically a file audit.
- Council sections show the council wisdom first. Route truth supports the
  council; it is not the council.
- Repeated `Aggregate:`, `Blocked/deferred:`, `parents`, `children`,
  `obligation`, and runtime details are compressed into one `Proof:` line per
  council or the footer.
- The `Members:` line names conceptual members that ran, not controller
  plumbing. Prefer `Strategy 3/5, Systems 3/5, Factory 3/5` over
  `Decision parent 1/1, child count 3/5 obligation`.
- Follow-up options are pleasant prompt cards, never fenced prompt/code boxes.
  Use a normal quoted prompt sentence plus `Why this helps`, `Use when`, and
  `Stop if`.
- Diagnostics that mostly serve route-truth accounting belong in the footer,
  capped at two compact lines.

If a draft looks like a CI log, worker log, receipt inventory, or contract
audit, rewrite it into this order: outcome, council wisdom, compiled move,
pleasant next prompts, footer truth.

## Ambient Start Output

When the Wizard runs without an initial prompt, include a short source-scan line:

```text
Source scan: repo docs, active packet, and current verification artifacts.
```

Then proceed normally. Do not make the user supply a prompt just to start.

## Header

Use this header for visible Wizard runs:

```text
🧙 Wizard v4.1 | {FULL|PARTIAL|BLOCKED} | waves:{completed/3}[ partial-coverage] | parents:{completed/required} | children:{completed/obligation}[ blocked|deferred|not-run] | [tools:{completed} | ]score:{0-100} | runtimes:{names}
```

The first line of every visible Wizard operational answer must be this v4.1 scored header when any Decision, Failure, or Follow-Up council wave ran, or when the user is evaluating Wizard runtime/route truth.

Examples:

```text
🧙 Wizard v4.1 | FULL | waves:3/3 | parents:12/12 | children:9/9 | score:94 | runtimes:codex,claude,tools
🧙 Wizard v4.1 | PARTIAL | waves:3/3 partial-coverage | parents:18/32 | children:0/1 blocked | tools:1 | score:72 | runtimes:codex-native,tools
🧙 Wizard v4.1 | PARTIAL | waves:2/3 | parents:7/10 | children:2/6 blocked | score:63 | runtimes:codex
🧙 Wizard v4.1 | BLOCKED | waves:1/3 | parents:2/9 | children:0/9 not-run | score:31 | runtimes:self
```

Do not print `FULL` unless the full-run minimum passes.

Do not print `COMPACT` in v4.1. Compact mode is not specified yet.

Wizard-relevant work done without a proper Decision/Failure/Follow-Up run is not valid work product. Do not close it as successful ordinary output. If only boot, preflight, source scan, tool inspection, or implementation work ran, emit a `BLOCKED` or `PARTIAL` v4.1 header that names the missing council, parent, and child obligations, then retry the smallest missing route when safe.

A follow-up option is the next Wizard input. Do not say "no fresh three-council run header" because a chosen follow-up was "only option execution." The chosen option must boot v4.1, run Decision, Failure, and Follow-Up on the option plus prior prework, then compile the next move and next follow-up options.

Selector-only inputs such as `4`, `1-4`, `all`, and `All of the Above` are not the whole scope. They are pointers to the prior next-input handoff. The Wizard must join the selected option with current thread state, source context, packet docs, MMM surfaces, prior prework, and relevant artifacts before it drafts an answer. A repair-only or test-only report is valid only when it is explicitly shown as a blocked/partial Wizard run with the missing council, parent, and child obligations named.

The Wizard is general-purpose. Follow-up prework may inspect docs, run tests, map refactors, reproduce bugs, scout research sources, draft implementation handoffs, or use adapter-specific tools. For Codex Ratchet sim work, follow-up prework may run cheap local sims when the strict sim profile passes. Show those sim receipts as preworked evidence for the next Wizard loop, not as a replacement for the next loop or as queue/readiness proof.

## v4.1 Route-Truth Reconciliation Gate

Before emitting the visible header, footer, or follow-up options, reconcile four count families separately:

- waves: completed sequential receipt-boundary passes;
- parents: completed accepted parent subagents against required selected members;
- children: completed accepted child/subsubagent receipts against the current child route obligation;
- tools: completed tool or harness checks.

Do not count a tool check as a child/subsubagent receipt. If a conformance harness, command, or local checker ran, report it under `tools:{n}` or in verification, never under `children`.

Do not advertise a runtime in `runtimes:{names}` unless an accepted receipt or completed tool check proves that runtime. Model names and reasoning levels belong in child `variant_signature` and `rerouter_ledger` fields, not in the header runtime list unless the runtime itself was used and receipt-backed.

If all three waves crossed their sequential barriers but member coverage was incomplete, write `waves:3/3 partial-coverage`. Plain `waves:3/3` is reserved for complete selected-member coverage.

If children/subsubagents were attempted but did not complete, write a child status marker: `blocked`, `deferred`, or `not-run`. The footer must use the same truth as the header. It cannot say "no children were proven" while the header says `children:1/1`.

If the runtime supports parent-launched child/subsubagent routes and a visible three-council run required them, do not write `children:0/0 not-run`. Show the obligation, for example `children:0/3 not-run`.

Before any visible header counts Claude Bridge children from more than one
parent, run or inspect the fanout receipt summary helper and reconcile the
summary against the per-parent obligation. A fanout batch with global timeout,
budget failures, not-launched children, or weak/no-delta receipts is `PARTIAL`
until the failed children are rerun or explicitly marked blocked.

Quality drift beats raw completion. A large child batch can finish and still be
partial when the child receipts are shape-identical, do not change the parent,
or lack artifact-facing deltas.

Loop output must show loop state without becoming a loop log. The footer may
name `loop:{n}/{cap}`, `new_findings:{n}`, `resolved:{n}`, and
`done_status:{done|continue|cap_reached|blocked}`. The answer body should
describe the accepted move, not enumerate every receipt.

For loop closeout, do not write `done` unless the compile gate records the done
predicate: configured consecutive empty-new-finding loops observed, no
unresolved load-bearing findings, and audit fixed point. Otherwise say
`continue`, `cap_reached`, or `blocked`.

For loop iterations after the first, `cross_loop` must cite at least one prior
finding id under supersedes, kills, extends, resolved, or unchanged. If it does
not, the output is a non-advancing re-prompt and the score is capped at 70.

For loop iterations after the first, `cross_loop.dispositions` must cover every
prior load-bearing open finding under exactly one disposition: supersedes,
kills, extends, resolved, or unchanged. Missing prior ids, duplicate prior ids,
or dispositions without rationale and artifact/clause references forbid `done`
and cap score at 75.

If runtime has no spawn surface for a substantive Wizard route, the header must
be `BLOCKED` with the missed parent/child obligation. `FULL` is forbidden.

If any required child model family is blocked without a smaller-retry or
accepted degraded-family receipt, `FULL` is forbidden and the missing family
must be named in the footer.

The FULL/PARTIAL label must be computed from
`manager.resource_pressure.model_family_statuses` and
`degraded_alt_child_families`, not from a footer note.

If `post_follow_up_compile_gate.terminal_status` is not `passed`, visible
follow-up options cannot be labeled `ready_for_execution`.

Every visible loop answer after loop 1 must include a compact
`wizard_loop_state` YAML block or artifact reference with `cross_loop`,
`done_predicate`, and current unresolved count. Prose-only loop state fails
self-repair.

The `wizard_loop_state` block is the operative loop state. Prose may summarize
it, but prose must not duplicate, override, or contradict the YAML state.
If prose says `done`, `ready`, `resolved`, or `FULL` while the operative YAML
state or accepted receipts say `continue`, `blocked`, `unresolved`, `PARTIAL`,
or missing coverage, visible self-repair fails. The renderer must reconcile the
YAML and prose before output; it cannot hide the contradiction in the footer.
Visible prose must use the canonical loop status token from
`wizard_loop_state.done_predicate.terminal_status`; do not invent completion
synonyms such as closed, green, shipped, ratcheted, finished, or clean outside
the operative block. If human-readable prose needs to mention status, write
`done_status:<token>` and keep the token identical to YAML.

When the cross-loop ledger is large, the visible answer may cite
`cross_loop.dispositions_ref` and show only `disposition_summary`. It may not
truncate the only copy of the disposition list.

If `manager.resource_pressure.model_family_statuses[family]` is absent for a
required family in a substantive Codex-adapter run, treat that family as
`BLOCKED` for the header computation until an accepted smaller-retry or
degraded-family receipt names the reason and substitute signal.
Whether a run is substantive Codex-adapter work is computed from receipts, not
renderer discretion. Accepted Wizard route receipts involving Codex-native,
Claude Bridge, Opus, Sonnet, Haiku, Gemini, or OMX/tmux activate model-family
accounting unless an accepted atomic/low-decomposition override says otherwise.
Tool and harness checks remain separate proof surfaces; they do not activate
or satisfy model-family accounting by themselves.

Visible verification counts must be current and tied to the exact command or harness that produced them:

```text
- `python3 -m pytest system_v5/tests/test_wizard_v4_conformance.py -q` -> 41 passed
```

Do not write naked stale summaries like `35 passed` or `48 passed` unless the exact command and fresh result are also shown.

## Visible Output Self-Repair Gate

Before sending, the main thread privately checks the drafted answer. If it fails, rewrite the answer and send only the repaired version.

The answer fails this gate when:

- it uses bold pseudo-headings such as `**Main Answer**`, `**Council Results**`, `**Follow-Up**`, or `**Verification**` instead of real Markdown sections;
- it lacks the required visible sections: `## ✨ Answer`, `## 🏛️ Council Results`, `## ✅ Compiled Move`, `## 🧭 Follow-Up Options`, and final `## 🧙 Footer`;
- it replaces the three council identities with option/route labels such as Proof, Premortem, Scout, Make, Run, Audit, Direct, or All of the Above;
- the `### 🛡️ Failure` section's first `Members:` line does not include
  `Premortem` with a compact passed or blocked ratio;
- it treats follow-up option execution as outside the Wizard loop;
- it lacks a concise MMM proof line showing full-MMM and mini-MMM receipt evidence;
- the footer is not the final top-level section or does not begin with `🧙 Time/value:`;
- the compiled move omits owner/lane, stop/failure condition, artifact/output surface, or status;
- follow-up options are not readable prompt cards with payoff, use condition, and stop/block condition;
- the header hides route obligations or contradicts the footer;
- the header advertises unproven runtime/model breadth;
- any Decision, Failure, or Follow-Up council wave ran and the first line is not the Wizard v4.1 scored header;
- the `## ✨ Answer` section opens with route bookkeeping such as `I ran`, `Option`, `Parent receipt`, `Child receipt`, `Parents:`, `Children:`, `Tools:`, `Route truth:`, or `Truth boundary:` instead of the accepted move/outcome in plain language;
- the visible `score:{n}` does not match the computed conformance score;
- it relies on `from the prior run` council or receipt counts in a current Wizard header;
- verification counts are stale, naked, or not command-tied;
- it treats a selector-only input as the whole scope instead of joining the prior handoff, current thread state, repo/source docs, packet docs, MMM surfaces, and artifacts;
- it answers a Wizard-relevant input as only a repair/test pass without route-truth status;
- it omits route-truth status for Wizard-relevant output when no council waves ran;
- it closes Wizard-relevant work as useful or accepted when no proper Decision/Failure/Follow-Up run happened;
- it says no further action is authorized, waits for the next explicit input, or otherwise idles when Ambient Start Mode has enough source context to infer a bounded move.
- the visible answer reads like a worker log: repeated aggregate counts,
  route-obligation prose in every council, dense file/path lists in the opening
  answer, or follow-up options wrapped as fenced boxes instead of readable
  prompt cards;
- council `Members:` lines name plumbing such as `Decision parent`,
  `Follow-Up parent`, or `child count obligation` instead of meaningful member
  families and compact ratios;
- `Blocked/deferred` appears before the council result, or appears repeatedly
  in multiple council sections when one footer truth line would suffice;
- the `## ✨ Answer` section contains more route bookkeeping than user-facing
  decision content;
- follow-up options lack an `All of the Above` option when multiple useful
  options are shown.
- loop output says `done` without a compile-gate done predicate;
- loop output lacks a `cross_loop` relationship after loop 1;
- a premortem route says the skill loaded when it only invoked the method and
  did not read `skills/premortem/SKILL.md`.
- prose claims a loop is done, ready, resolved, or full while the operative
  `wizard_loop_state`, manager resource-pressure fields, or receipts say
  continue, blocked, unresolved, partial, or missing family coverage;
- prose uses completion synonyms outside the canonical
  `done_status:<terminal_status>` token;
- a required model-family key is absent from
  `manager.resource_pressure.model_family_statuses` during a substantive
  Codex-adapter run.
- a loop after the first lacks prior finding ids in `cross_loop`;
- `FULL` appears when the runtime had no spawn surface for required
  parent/child work;
- a follow-up option says `ready_for_execution` while the post-Follow-Up
  compile gate is missing or blocked.
- a loop after the first fails to cover every prior load-bearing open finding
  under exactly one `cross_loop` disposition;
- a `cross_loop` disposition lacks rationale, artifact/clause reference, or a
  real delta for `extends`;
- a loop fixed point uses sibling audits with no independence vector;
- a loop fixed point uses only timestamp or model-label differences as its
  independence vector;
- premortem skill body read provenance comes from a different worker than the
  premortem synthesis without marking the route `degraded_local`;
- premortem skill body read provenance names an unversioned or stale skill path
  without packet/source digest or adapter-delta mirror proof;
- loop state appears only as prose when `loop_iteration > 1`.

This gate repairs the answer. It should not appear as a visible audit section unless the user explicitly asks for diagnostics.

## Council Results

Each council section must begin with a compact `Members:` line so the user can
see the actual council composition and route-truth ratios immediately. This
comes before the result sentence, proof, counts, or commentary.

Use this order for every visible council section:

1. `Members:` named members with compact `passed/total-ran-agents` ratios.
2. `Result:` what the council changed.
3. `Why it matters:` or `What changed:` when useful.
4. `Proof:` aggregate parent/child/tool truth.

Do not move `Members:` to the end. If the named members and ratios are not
visible before the result, the output fails self-repair.

For a visible full run, name the three nested parent councils in each wave:
Decision `Voices`, `Six Hats`, `Experts`; Failure `Premortem`, `Falsifiers`,
`Loophole Auditor`; Follow-Up `Prompt Voices`, `Lanes`, `Compile Gate`. Do not hide
this as a raw count; show the human meaning of the council and then the
proof/counts. Individual voices, hats, lanes, and compile-gate fields should
appear as child/subsubagent proof under their council parent, not as parent
council seats.

When a parent member represents nested children, the visible council result
should show the child impact, not the raw child log. Good examples:
`Six Hats 6/6, impact: Black killed broad launch; Green added smaller probe`.
`Lanes 5/5, impact: Back set stop condition; Direct became accepted move`.

The `Members:` line is not a substitute for the council result. It is the
visible route-truth proof that named members actually ran. Use each member's
accepted-child ratio in `member passed/total-ran-agents` form, for example
`Systems 4/4`, `Factory 3/4`, `Premortem 4/5 after reroute`, `Six Hats 6/6`,
`Lanes 5/5`. The denominator is the number of agents/children actually
attempted for that member, plus accepted reroutes when they replace a failed
core child. The numerator is accepted useful receipts only. Do not count tool
checks, controller synthesis, pending starts, or timed-out children as passed
agents.

If a council section names members but omits the ratios, the output fails
self-repair. If a member is important to the result and has `0/N`, mark the run
`PARTIAL` or `BLOCKED` and explain the reroute/stop boundary.

Keep each council section compact. In normal visible output, use at most four
short lines after the heading:

```text
Members: Strategy 3/5, Systems 3/5, Factory 3/5.
Result: ...
Why it matters: ...
Proof: ...
```

Do not repeat the same child-coverage caveat in all three councils. State the
local implication once where it changes the council result, then put global
route truth in the footer.

```text
Members: Feynman 5/5, Factory 5/5, Strategy 5/5, Systems 5/5, Six Hats 6/6, Experts 5/5.
Result: The smallest useful move is ...
Why it matters: ...
Proof: 12/12 parent members accepted, 60/60 child receipts accepted across Codex-native, Opus, Sonnet, Haiku, and Gemini-attempt/degraded coverage. Tool checks reported separately. Blocked: none. Rerouted: none.
```

```text
Members: Premortem 6/6, Falsifiers 5/5, Loophole Auditor 6/6.
Result: Outcome is harden_then_execute because ...
What changed: ...
Proof: 3/3 Failure parent members accepted, 17/17 Failure child receipts accepted across Codex-native, Opus, Sonnet, Haiku, and Gemini-attempt/degraded coverage. Tool checks reported separately. Blocked: none.
```

Failure Council requires `Premortem` in this line. If premortem did not run,
show the blocked ratio and mark the run partial or blocked; do not silently
replace it with Black Hat, Popper, Pushback, postmortem, calibration, expert
critique, or receipt audit.

```text
Members: Orwell 5/5, Strategy 5/5, Factory 5/5, Six Hats 6/6, Lanes 5/5, Experts 5/5.
Result: Best next prompts are ...
Why they are useful: ...
Proof: 11/11 parent members accepted, 55/55 child receipts accepted across Codex-native, Opus, Sonnet, Haiku, and Gemini-attempt/degraded coverage. Tool checks reported separately. Accepted options: 4.
```

Council result sections must not start with raw route bookkeeping such as
`Blocked:`, `Rerouted:`, `Run truth:`, `Receipts:`, receipt inventory, or
parent/child inventory. `Members:` is the required first line because it is
human council composition plus compact route truth, not a raw log.

The visible council subsections must preserve the canonical council identities:

- `### 🧠 Decision`
- `### 🛡️ Failure`
- `### 🧭 Follow-Up`

Do not replace them with route labels such as `### 🧪 Proof`, `### 🛡️ Premortem`, or `### 🧭 Scout`. Route labels belong inside results, follow-up options, or execution reports.

## Recommended Visible Shape

🧙 Wizard v4.1 | FULL | waves:3/3 | parents:9/9 | children:49/49 | score:94 | runtimes:codex,claude,gemini,tools

## ✨ Answer
The best bounded move is ...

## 🧩 Context-Aware Voices
♟️ Strategy:
🔁 Systems:
🏭 Factory:

## 🏛️ Council Results
Wizard Harness council results: Three LLM councils ran as sequential write barriers: Decision chose the move, Failure tested it, and Follow-Up compiled usable next prompts.

### 🧠 Decision
Members: Feynman 5/5, Factory 5/5, Strategy 5/5, Systems 5/5, Six Hats 6/6, Experts 5/5.
Result:
Why it matters:
Proof:

### 🛡️ Failure
Members: Premortem 6/6, Falsifiers 5/5, Loophole Auditor 6/6.
Result:
What changed:
Proof:

### 🧭 Follow-Up
Members: Orwell 5/5, Strategy 5/5, Factory 5/5, Six Hats 6/6, Lanes 5/5, Experts 5/5.
Result:
Accepted options:
Proof:

## ✅ Compiled Move
- Target:
- Immediate action:
- Owner/lane:
- Success check:
- Stop condition:
- Artifact/output:
- Status:

## 🧭 Follow-Up Options
1. 🧰 Direct: "..."
   Why this helps:
   Pre-checked:
   Use this when:
   Stop if:

2. 🔁 Alternative: "..."
   Why this helps:
   Pre-checked:
   Use this when:
   Stop if:

3. 🧪 Proof: "..."
   Why this helps:
   Pre-checked:
   Use this when:
   Stop if:

4. 🧩 All of the Above: "..."
   Why this helps:
   Pre-checked:
   Use this when:
   Stop if:

## 🧙 Footer
🧙 Time/value: {worth_it|marginal|not_worth_it} | time:{short|medium|long} | value:{low|medium|high} | reason:{one plain sentence}
Status:
Proof:
MMM proof:
Verification:
Limit:
Next retry if needed:
Source scan: only when the run had no initial prompt.

The footer is mandatory for every visible Wizard output. It must be the final top-level section, must be led by `## 🧙 Footer`, and its first nonblank line must be `🧙 Time/value:`. The time/value line states whether the output's expected value is commensurate with the reader's time cost.

## Score

Score out of 100:

- 20 points: main full MMM loaded before runtime rules.
- 20 points: three council waves completed in sequence.
- 20 points: required parent members completed with exact mini-MMM load receipts.
- 15 points: child/subsubagent receipts completed where supported, with tool
  and harness checks scored separately under verification.
- 15 points: compile gate passed for accepted options.
- 10 points: visible output is readable, not a worker log, and includes blockers.

Automatic caps:

- Cap at 40 if main full MMM was not loaded.
- Cap at 50 if any council is missing.
- Cap at 60 if no parent workers actually ran.
- Cap at 70 if no child/subsubagent was attempted despite runtime support.
- Cap at 70 if child lanes were marked blocked because there was "no exact
  implementation task" or "nothing useful for a child to do." Those are not
  valid blockers; use a model/reasoning variant, falsifier, scout, salience
  check, receipt audit, or follow-up improver.
- Cap at 75 if a substantive Codex-adapter run with available child runtimes
  lacks the Codex-native/Opus/Sonnet/Haiku/Gemini child model matrix.
- Cap at 75 if any counted parent in a substantive Codex-adapter run has fewer
  than five accepted child/subsubagent receipts and no explicit
  atomic/low-decomposition override.
- Cap at 80 if any counted parent has more than ten child/subsubagent receipts
  without a stress-test label and receipt-shape/divergence audit.
- Cap at 80 if follow-up options fail compile gate.
- Cap at 85 if output lacks council notation.
- Cap at 85 if output hides the three LLM councils or omits Strategy, Systems, and Factory context voices for a Wizard/system run.
- Cap at 85 if output lacks a footer.
- Cap at 85 if the footer is not the final section or lacks a leading `🧙 Time/value:` signal.
- Cap at 85 if follow-up options lack a human-readable `All of the Above` option.
- Cap at 85 if council sections read like a worker log instead of result-first synthesis.
- Cap at 85 if visible follow-up options were not pre-run/audited/improved.
- Cap at 85 if tools are counted as children or if the footer contradicts the header route truth.
- Cap at 85 if `waves:3/3` hides partial parent/member coverage.
- Cap at 85 if `children:0/0 not-run` hides a required child/subsubagent route obligation.
- Cap at 85 if verification counts are stale or not command-tied.
- Cap at 85 if the answer uses pseudo-headings instead of the required Markdown sections.
- Cap at 85 if the answer replaces Decision/Failure/Follow-Up with option or lane labels.
- Cap at 85 if the answer does not surface full-MMM and mini-MMM proof.
- Cap at 85 if MMM proof counts contradict header parent counts.
- Cap at 85 if the header score does not match computed conformance.
- Cap at 85 if a current Wizard header relies on prior-run council receipts.

## Retry Decision

- `score >= 90`: full accepted.
- `75 <= score < 90`: usable partial; show blockers and one retry prompt.
- `50 <= score < 75`: retry missing route(s) before presenting as useful unless user asked for diagnostics.
- `score < 50`: blocked/failed run; rerun the smallest missing route or report the blocker.

If the system can safely retry, it should retry before final output.

---

# Source: `07_TASK_CARDS.md`


---
title: Wizard v4.1 Task Cards
type: task_cards
packet: v4.1
framing: standalone
---

# Task Cards v4.1

Use task cards to keep workers bounded.

## Parent Member Task Card

```yaml
task_card_type: parent_member
member_id:
council: decision | failure | follow_up
mini_mmm_slice:
task_summary:
source_slice:
assignment:
must_return:
  - member finding
  - evidence boundary
  - compile relevance
  - member_utility: distinct contribution, decision use, sim relevance, theater cut, current disposition, reboot note
  - structural divergence fields when the receipt will feed plural synthesis
  - child routes needed
must_not:
  - synthesize whole answer
  - claim other members ran
  - skip receipt fields
receipt_required: true
```

## Child/Subsubagent Task Card

```yaml
task_card_type: child_member
parent_member_id:
parent_route_summary:
child_member_id:
mini_mmm_slice:
source_slice_or_tool_surface:
narrower_than_parent_by: source_slice | claim | fixture | falsifier | follow_up_option | boundary
assignment:
must_return:
  - one finding
  - one evidence boundary
  - completed | blocked | deferred
  - if negative: one exact falsifier, boundary, demotion condition, or missing artifact
must_not:
  - widen scope
  - synthesize council
  - load sibling member cards
  - claim parent or sibling routes ran
  - count itself
receipt_required: true
```

A child can succeed by killing or demoting a candidate. Negative child results
count as useful only when they narrow the admissible space for the parent route.

Packet-local child card defaults live in
`taskcards/CHILD_TASK_CARDS_v4_1.md`. When a parent launches Claude Bridge
children, include the relevant formal child group from that file so Claude
receipts do not have to infer the task-card surface from the parent prose.

## Skill-Backed Member Task Card

```yaml
task_card_type: skill_backed_member
member_id:
skill_id:
canonical_skill_path:
runtime_local_skill_path:
mmm_load:
  main_thread_full_mmm:
  worker_compact_general_mmm:
  exact_or_family_mini_mmm:
assignment:
loop_state:
must_return:
  - skill_loaded
  - upstream wiki skill path
  - adapter differences if any
  - receipt fields
  - parent/child linkage
  - what changed
  - unresolved loopholes or blockers
  - next prompt or stop condition
must_not:
  - replace the council wave
  - claim certainty without evidence standard
  - continue past loop cap
  - start codex-autoresearch interactive mode without launch approval
receipt_required: true
```

## Receipt-Divergence Gate Task Card

```yaml
task_card_type: receipt_divergence_gate
receipt_set:
reruns_used:
rerun_cap: 1
assignment: classify whether accepted receipts add structural signal before synthesis
must_compare:
  - core_claim
  - reasoning_path
  - evidence_anchors
  - operation_or_falsifier
  - conclusion_direction
must_return:
  - PATH_IDENTICAL | DECORATIVE_SPLIT | CONVERGENT_SIGNAL | HEALTHY_DIVERGENCE | SINGLE_ANSWER
  - pass | rerun | block
  - smallest sharper rerun card when action is rerun
must_not:
  - accept empty or malformed structural values
  - use prose similarity
  - count route labels as divergence
  - block legitimate convergent signal
```

## Compile-Gate Task Card

```yaml
task_card_type: compile_gate
option_label:
target:
candidate_prompt:
assignment: decide whether the option is bounded enough to act on
must_return:
  - target
  - immediate_action
  - owner_lane
  - success_check
  - stop_condition
  - artifact_output_surface
  - status
must_not:
  - infer readiness from council agreement
  - infer execution from salience
```

## Reroute Task Card

```yaml
task_card_type: reroute
failed_or_slow_route:
failure_reason:
smaller_replacement:
deadline:
must_return:
  - completed replacement receipt
  - or blocked/deferred reason
must_not:
  - broaden task
  - become a council vote
  - synthesize the answer
```

## Oversight/Rerouter Task Card

```yaml
task_card_type: oversight_or_rerouter
role_id: guard.* | manager.rerouter
observed_route_or_receipt_set:
assignment:
must_return:
  - pass | block | shrink | rerun_once | defer
  - exact reason
  - smallest repair card when action is shrink or rerun_once
must_not:
  - vote as a council member
  - synthesize the answer
  - count starts as completed receipts
  - widen the route
receipt_required: true
```

---

# Source: `taskcards/CHILD_TASK_CARDS_v4_1.md`


---
title: Wizard v4.1 Child Task Cards
type: task_cards
packet: v4.1
framing: standalone
---

# Wizard v4.1 Child Task Cards

Every parent-launched child receives this minimum card:

- parent route summary;
- exact child id;
- exact mini-MMM slice or sparse registry slice plus definition row;
- route-bound council-member skill when assigned;
- source/tool slice;
- one required output shape;
- one falsifier or check;
- receipt id and parent id.

Children do not load sibling routes or the full main MMM unless explicitly
assigned a gate or aggregator role.

## Formal Child Groups

- `failure.premortem_council`: `premortem.likely_failure`,
  `premortem.dangerous_failure`, `premortem.hidden_assumption`,
  `premortem.early_warning`, `premortem.revised_plan`,
  `premortem.sim_evidence_corruption`.
- `failure.falsifier_council`: `voice.popper`, `voice.pushback`,
  `failure.calibration`, `guard.receipt_audit`, `guard.boundary_check`.
- `follow_up.lane_council`: `lane.direct`, `lane.alternative`,
  `lane.reframe`, `lane.back`, `lane.wildcard`,
  `lane.all_of_the_above`.

If a child lacks an exact mini-MMM file, the sparse registry slice plus the
definition row is the required salience source. If both are missing, the child
is blocked and the parent cannot count it as accepted.

Compact child loading means compact member mini-MMM under
`mmm/mini/compact/...`, not the compact main MMM. Child receipts keep
`loaded_salience.full_mmm` empty unless the child was explicitly assigned a
gate or aggregator role that requires broader boot.

---

# Source: `08_EXAMPLE_OUTPUT.md`


---
title: Wizard v4.1 Example Output
type: example
packet: v4.1
framing: standalone
---

# Example Output v4.1

🧙 Wizard v4.1 | FULL | waves:3/3 | parents:9/9 | children:49/49 | score:94 | runtimes:codex,claude,gemini,tools

## ✨ Answer
The smallest useful bounded move is to make one runnable packet that proves the
Wizard can choose, harden, and hand off work without turning route machinery
into the answer.

The packet is ready for execution when the compile gate passes and the next
prompt is clear enough that a fresh thread can act without asking what to do.

## 🧩 Context-Aware Voices
♟️ Strategy: close the first failing gate before adding more fanout.
🔁 Systems: route machinery is feedback input, not the user-facing output.
🏭 Factory: the handoff artifact is final_answer.md plus validation.json.

## 🏛️ Council Results
Three LLM councils ran as sequential write barriers: Decision chose the move, Failure tested it, and Follow-Up compiled usable next prompts.

### 🧠 Decision
Members: Voices 5/5, Six Hats 6/6, Experts 5/5.
Result: build the runnable packet before expanding adapters.
Why it matters: more members will not help if boot order, receipt truth, and compile-gate separation are still fuzzy.
Proof: 3/3 parent councils and 16/16 child receipts accepted; tools reported separately.

### 🛡️ Failure
Members: Premortem 6/6, Falsifiers 5/5, Loophole Auditor 6/6.
Result: `harden_then_execute`.
What changed: add retry and conformance checks so partial runs cannot claim `FULL`.
Proof: 3/3 parent councils and 17/17 child receipts accepted; no blocked core route.

### 🧭 Follow-Up
Members: Prompt Voices 4/4, Lanes 6/6, Compile Gate 7/7.
Result: use the harness as the next guardrail, then close or wire it into the normal validation path.
Accepted options: Direct closeout, CI-ready wiring, live runtime proof, and all-of-the-above.
Proof: 3/3 parent councils and 17/17 child receipts accepted; option prompts passed compile gate.

## 🎭 Theater Cut
Member count is not value. Every kept member had to name a distinct contribution, a decision use, sim relevance when relevant, and the theater it removed.

## 🔌 Adapter Profile
For Codex Ratchet sims, readiness means the strict adapter profile passed: one stage, one claim, one carrier/fixture, exact tool/function or admitted coupling, positive check, boundary check, prior receipts when needed, and expected result path.

## ✅ Compiled Move
- Target: v4 runtime packet
- Immediate action: add output, scoring, and retry docs
- Owner/lane: Direct
- Success check: a full run can show councils, counts, score, and compiled option
- Stop condition: member receipts cannot be represented
- Artifact/output: v4 packet docs
- Status: ready_for_execution

## 🧭 Follow-Up Options
1. 🧰 Direct Closeout: "Run the harness once more and write a short readiness note."
   Why this helps: closes the current work without widening scope.
   Pre-checked: passes if current verification stays green; fails cleanly if any fixture regresses.
   Use this when: you want the change reviewable now.
   Stop if: any verification command regresses.

2. 🔌 CI-Ready Wiring: "Add the harness to the normal validation path."
   Why this helps: future Wizard changes cannot skip the guardrail.
   Pre-checked: safe only if it does not change Wizard semantics.
   Use this when: durability matters more than keeping this as a manual check.
   Stop if: the validation entrypoint is ambiguous.

3. 🧪 Live Runtime Proof: "Run a fresh v4 Wizard with receipt artifacts and validate them."
   Why this helps: upgrades parent-reported truth into machine-checkable route truth.
   Pre-checked: blocked until parent/child artifacts can be written.
   Use this when: live Max Assembly proof is the goal.
   Stop if: parent/child receipt artifacts cannot be written.

4. 🧩 All of the Above: "Close out the harness, wire it into validation, then run one live receipt-backed Wizard proof."
   Why this helps: turns the fix into a durable system loop.
   Pre-checked: sequence is safe only if each earlier option passes before the next begins.
   Use this when: you want maximum confidence and have time for a full pass.
   Stop if: any earlier option fails.

## 🧙 Footer
🧙 Time/value: worth_it | time:short | value:high | reason: the harness blocks fake full runs before they waste review time.
Status: accepted baseline.
Proof: 9 parent council receipts and 49 child receipts accepted; tool checks were separate.
Verification: conformance and runner checks pass.
Limit: live receipt-backed Max Assembly is still a separate proof.
Next retry if needed: rerun Failure Council only with smaller hardening cards.

---

# Source: `09_CONFORMANCE_HARNESS.md`


---
title: Wizard v4.1 Conformance Harness
type: conformance_harness
packet: v4.1
framing: standalone
---

# Conformance Harness v4.1

The packet is not accepted just because the docs are clear.

A runtime should be able to test whether Wizard v4.1 actually ran.

The discoverable loop-contract fixture index is
`conformance/fixtures/loop_contract_fixtures_v4_1.json`. New loop, premortem,
audit-independence, and output-format clauses must either map to an entry in
that index or name a concrete external test id.

The packet-local validator is
`conformance/validate_loop_contract_fixtures.py`. It reads the fixture index,
checks fixture ids and clause references, runs in-memory pass/fail cases for
digest recomputation, structural audit divergence, model-family key presence,
loop-kind digest handling, prose/YAML contradiction handling, and fixture
mapping. It also asserts packet-root identity, recomputes skill and quote
digests from files, checks stale mirror and cross-loop ledger fixtures, and
requires family statuses to be accepted terminal values rather than merely
truthy strings. It writes no reports and opens no browser.

## Required Checks

The conformance harness should verify:

- main thread loaded the selected main MMM before the runnable Wizard doc;
- selected skill or runtime surface is explicitly v4.1;
- no older packet path or old header shape appears in accepted receipts;
- parent receipts name exact member mini-MMM slices;
- parent member utility distinguishes current-run cut, reboot candidate, suppression, and retirement evidence;
- child receipts count only when terminal status is completed and accepted;
- substantive Codex-adapter child model matrix coverage is proven by accepted
  child receipts for Codex-native, Opus, Sonnet, Haiku, and Gemini-attempt/
  degraded coverage, not by header labels;
- counted parents in substantive Codex-adapter runs prove 5-10 accepted
  child/subsubagent receipts each, or fail closed unless an explicit
  atomic/low-decomposition override is present;
- same-triple sim/QIT child variants do not reuse the same initialization signature;
- non-sim tasks pass with only `bounded_work_compile_gate`;
- sim/probe/queue-visible tasks require the strict adapter gate;
- visible output is answer-first and includes the compiled move before council detail.
- no-prompt runs include source-scan context, inferred target, evidence boundary, and a bounded action;
- visible output has a cognitive-load budget: council results, three to four follow-ups, all-of-the-above, and footer.
- every visible follow-up option includes evidence that it was pre-run, audited, and improved.
- the footer is the final section and begins with a `🧙 Time/value:` signal, so slow runs must justify their reader cost.
- route-truth reconciliation separates waves, parent subagents, child/subsubagents, and tool checks before the header is emitted.
- tool checks never satisfy child/subsubagent counts.
- `waves:3/3` includes `partial-coverage` when sequential barriers completed but selected parent/member coverage did not.
- footer truth cannot contradict header route counts.
- visible verification counts are tied to exact commands and current pass totals.
- pseudo-heading answers using bold labels instead of required Markdown sections fail.
- `children:0/0 not-run` fails when a visible three-council run has a child/subsubagent route obligation.
- option/route labels replacing Decision, Failure, and Follow-Up council identities fail.
- visible Wizard output without a concise full-MMM and mini-MMM proof line fails.
- v4.1 visible headers fail after the v4.1 upgrade.
- displayed header score must equal computed conformance score.
- MMM proof parent counts must match accepted parent receipt counts.
- prior-run council receipts cannot be counted as the current Wizard header.
- next-input handoff packets cannot render output until a pre-output route-truth gate joins current input identity, freshness refs, accepted receipt ids, header counts, runtime labels, handoff path, and final output artifact.
- loop iteration greater than 1 must include `cross_loop` with every prior
  load-bearing open finding under exactly one disposition.
- `cross_loop` dispositions must include rationale, artifact/clause reference,
  and a real delta for `extends`; synonym-only disposition drift fails.
- loop `done` must fail unless done predicate fields are satisfied, including
  independent audit receipt ids and an audit independence vector.
- audit independence must fail when the only difference is timestamped prompt
  seed or model label; at least one structural axis must differ.
- premortem loaded status must fail when `skill_body_read_ref` is empty or
  when the skill body reader worker differs from the synthesis worker without
  `degraded_local`.
- premortem loaded status must fail when the skill body source is unversioned,
  stale, or not tied to the active v4.1 packet/local mirror.
- a substantive Codex-adapter run with partial child-model family coverage must
  fail `FULL` unless missing families have accepted smaller-retry/degraded
  receipts.
- loop state rendered only as prose must fail for loop iterations after the
  first.
- every new conformance clause must have a discoverable fixture or named test
  id before it can raise the score.
- `extends` and `resolved` cross-loop dispositions must fail unless the cited
  artifact or clause digest is fresh and the delta/rationale is material.
- audit independence must be validated from structured fields, not prose
  divergence claims.
- stale, placeholder, malformed, or non-recomputed premortem skill digests
  must fail.
- prose/YAML loop-state contradictions must fail before visible output.
- absent required `model_family_statuses` keys must fail `FULL` in substantive
  Codex-adapter runs.
- read-only loops must not be forced to fabricate digest changes, and edit
  loops must not resolve findings with stale digests.
- skill-body quote anchors must be recomputed from packet-local file lines.
- fixture mapping must be bidirectional: every new clause has a fixture/test id
  and every fixture id maps back to a live clause.
- done predicate validation must count only load-bearing findings, not raw
  premortem hypotheses.

## Golden Fixture Classes

At minimum, keep fixtures for:

- documentation cleanup;
- bug triage;
- refactor planning;
- research synthesis;
- implementation handoff;
- valid sim packet;
- vague sim packet that must fail;
- fake `FULL` with started child that must fail;
- version drift that must fail;
- worker-log output that must fail.
- promptless ambient source scan that must pass;
- promptless run with no source context that must fail;
- promptless hook wake that idles with "no further action is authorized" while source context exists, which must fail;
- output with too many visible follow-ups that must fail.
- output with un-preworked follow-up options that must fail.
- `pre_run_passed_unadmitted` self-promoting to `queue_ready` or admitted evidence without `admitted_by`, which must fail;
- stale `next_input_ready` packet without a freshness gate, which must fail;
- runner success cited without controller-read result artifact, which must fail;
- receipt-divergence collapse that requests a sharper rerun;
- receipt-divergence cap hit that blocks after the rerun cap;
- malformed structural fields that block instead of passing as fake evidence.
- deliberator contract missing `query_class`, `per_thinker_verdict`,
  `all_wrong_rederive`, `minority_report`, or `format_alignment_check`;
- serialized trajectory cache entry that prunes away source receipt id,
  evidence anchor, executable delta, dissent/anomaly, pruning reason, or
  evidence boundary;
- all-agree plural synthesis without distinct evidence anchors or a divergence
  audit;
- strange but testable minority trajectory dropped without bounded
  falsification, preservation, or artifact-backed kill.
- reboot candidate without concrete boot/task/source/model delta that must fail;
- retire candidate without repeated evidence that must fail;
- same-triple child variants with duplicate initialization signatures that must fail.
- tool check claimed as child/subsubagent that must fail;
- partial parent coverage with plain `waves:3/3` that must fail;
- footer denying child receipts while the header counts children that must fail;
- stale verification count without the matching fresh command that must fail.
- substantive sim/proof/queue-visible run with missing Codex-native/Opus/Sonnet/Haiku/Gemini
  child model matrix coverage that must fail;
- pseudo-heading output that must fail even when route truth is otherwise honest;
- hidden child obligation output that must fail when child routes were expected but not launched.
- child routes marked blocked merely because there was no exact implementation
  task or "nothing useful" for an external model to do. That must fail: child
  lanes can still run variants, scouts, falsifiers, mini-MMM checks, receipt
  audits, or follow-up improvers.
- council identity drift output that must fail when Proof/Premortem/Scout replace the three councils;
- missing visible MMM proof output that must fail.
- stale v4.1 visible header that must fail;
- score mismatch output that must fail;
- MMM proof/header contradiction that must fail;
- prior-run receipt reuse output that must fail.
- next-input handoff with a valid freshness gate and joined pre-output route-truth gate that must pass;
- next-input handoff missing the joined pre-output route-truth gate that must fail;
- pre-output route-truth gate whose header counts disagree with accepted receipts that must fail.
- loop output after loop 1 missing full prior-open-finding coverage in
  `cross_loop`, which must fail;
- loop output saying `done` without two independent audit receipts and an
  independence vector, which must fail;
- premortem receipt with `skill_method_invoked:true` but missing
  `skill_body_read_ref` or mismatched worker provenance, which must fail;
- partial child-model surface labeled `FULL`, which must fail;
- loop state flattened into prose with no `wizard_loop_state` block or artifact
  reference, which must fail.
- cross-loop disposition drift where every prior id is present but `extends`,
  `resolved`, and `unchanged` lack rationale/artifact deltas, which must fail;
- audit receipts with only timestamp/model-label differences, which must fail;
- premortem receipt reading a stale or unversioned skill path, which must fail;
- new harness fixture file not referenced by a discoverable test id, which must
  fail.
- `FX-NF-11b-prose-divergence-only`: audit receipts claim divergence in prose
  but lack a verified structural axis; this must fail.
- `FX-NF-11b-structural-divergence`: audit receipts include a verified
  structural axis and non-timestamp/non-label differences; this should pass.
- `FX-NF-12b-boilerplate-rationale`: cross-loop dispositions cite all ids but
  reuse boilerplate rationales or stale digests; this must fail.
- `FX-NF-12b-fresh-delta`: `extends` cites a fresh digest and material delta;
  this should pass.
- `FX-OF-03b-missing-status-key`: required family key is absent from
  `model_family_statuses`; this must fail `FULL`.
- `FX-OF-10b-prose-yaml-contradiction`: prose says done/full while YAML says
  continue/partial; this must fail.
- `FX-NF-14a-bogus-digest`: premortem skill digest is malformed or placeholder;
  this must fail.
- `FX-NF-14a-stale-mirror`: mirror digest differs from active packet-local
  source without an adapter delta; this must fail.
- `FX-meta-clause-fixture-mapping`: every new loop-contract clause maps to a
  fixture id or named test id; this should pass.
- `FX-NF-15a-index-without-validator`: fixture ids exist but no validator
  consumes them; this must fail.
- `FX-NF-15b-recomputed-skill-digest`: validator recomputes the premortem
  skill digest from the packet-local path; this should pass.
- `FX-NF-15c-author-asserted-structural-axis`: receipt asserts
  structural-axis verification while primitive fields match; this must fail.
- `FX-NF-15d-read-only-loop-unchanged-digest`: read-only loop keeps a finding
  unchanged against the same digest; this should pass.
- `FX-NF-15e-receipt-derived-substantive-classifier`: accepted route receipts
  activate family accounting regardless of renderer label; this should pass.
- `FX-NF-15f-completion-synonym-prose`: prose uses a completion synonym that
  contradicts YAML; this must fail.
- `FX-NF-15g-skill-body-quote-anchor`: quote anchor hash matches the cited
  packet-local skill line range; this should pass.
- `FX-NF-15h-dispositions-ref-summary`: large ledgers may be cited by
  `dispositions_ref` with summary while validator inspects the full ledger;
  this should pass.
- `FX-NF-15i-hypothesis-not-load-bearing`: raw premortem hypotheses do not
  reset done predicate unless promoted to load-bearing; this should pass.

## Codex Ratchet Harness

The Codex Ratchet adapter may use:

```bash
python3 scripts/wizard_v4_conformance.py --out-dir work/wizard_v4_conformance/latest
```

This is an adapter harness. The universal packet does not require this exact script.

The Codex Ratchet adapter may render supplied v4 receipts through:

```bash
python3 scripts/run_wizard_v4.py --receipts work/wizard_v4_runs/latest/input_receipts.json --out-dir work/wizard_v4_runs/latest
```

This is an adapter runner. It must remain v4-only and must not import or mutate old Wizard runner paths.

## Acceptance Rule

Do not improve more Wizard prose until the conformance harness passes its golden fixtures.

---

# Source: `conformance/validate_loop_contract_fixtures.py`


#!/usr/bin/env python3
"""Validate Wizard v4.1 loop-contract fixture binding.

This validator writes no files and opens no browser. It is intentionally small:
the goal is to prove that the fixture index is consumed by executable checks
instead of being decorative packet prose.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path


REQUIRED_FAMILIES = ("codex_native", "opus", "sonnet", "haiku", "gemini")
PASSING_FAMILY_STATUSES = {"completed", "accepted", "useful", "accepted_smaller_retry", "accepted_degraded_alt"}
EXTERNAL_RUNTIMES = {
    "codex",
    "codex_native",
    "claude_bridge",
    "claude_code_builtin",
    "opus",
    "sonnet",
    "haiku",
    "gemini",
    "omx_tmux",
}
COMPLETION_SYNONYMS = {
    "done",
    "closed",
    "complete",
    "completed",
    "finished",
    "green",
    "shipped",
    "ratcheted",
    "ready",
    "resolved",
    "clean",
}
BOILERPLATE_DELTA_WORDS = {
    "wording",
    "updated",
    "update",
    "refined",
    "refine",
    "clarify",
    "clarified",
    "clarity",
    "intent",
    "text",
    "prose",
    "renamed",
    "phrasing",
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def quote_hash(path: Path, line_start: int, line_end: int) -> tuple[str, str]:
    lines = path.read_text().splitlines()
    quote = "\n".join(lines[line_start - 1 : line_end])
    return sha256_bytes(quote.encode("utf-8")), quote


def has_structural_divergence(a: dict, b: dict) -> bool:
    axes = (
        "model_family",
        "runtime",
        "prompt_seed_or_digest",
        "receipt_bundle_digest",
        "adversarial_task_card_id",
    )
    for axis in axes:
        av = a.get(axis)
        bv = b.get(axis)
        if av and bv and av != bv:
            if axis == "prompt_seed_or_digest" and not (
                re.fullmatch(r"[0-9a-f]{32,64}", str(av)) and re.fullmatch(r"[0-9a-f]{32,64}", str(bv))
            ):
                continue
            if axis == "receipt_bundle_digest" and not (
                re.fullmatch(r"[0-9a-f]{64}", str(av)) and re.fullmatch(r"[0-9a-f]{64}", str(bv))
            ):
                continue
            return True
    return False


def validate_skill_digest(receipt: dict, root: Path) -> bool:
    ref = receipt.get("skill_body_read_ref", [])
    digest = receipt.get("skill_body_source_digest", "")
    if not re.fullmatch(r"[0-9a-f]{64}", digest):
        return False
    if not ref:
        return False
    path = Path(ref[0])
    if not path.is_absolute():
        path = root / path
    if not path.exists():
        return False
    return sha256_file(path) == digest


def validate_quote_anchor(anchor: dict, root: Path) -> bool:
    path = Path(anchor.get("source_path", ""))
    if not path.is_absolute():
        path = root / path
    if not path.exists():
        return False
    try:
        expected, _ = quote_hash(path, int(anchor["line_start"]), int(anchor["line_end"]))
    except Exception:
        return False
    if expected != anchor.get("quote_sha256"):
        return False
    text = anchor.get("quote_text", "")
    return "This packet-local skill is embedded in Wizard" in text and "open a browser" in text


def ref_exists(root: Path, ref: str) -> bool:
    path_text, _, needle = ref.partition("#")
    path = root / path_text
    if not path.exists():
        return False
    return not needle or needle in path.read_text()


def material_delta(delta: str) -> bool:
    tokens = re.findall(r"[a-z0-9_]+", delta.lower())
    substantive = [token for token in tokens if token not in BOILERPLATE_DELTA_WORDS and len(token) > 2]
    return len(substantive) >= 4


def cross_loop_delta_ok(case: dict, root: Path) -> bool:
    loop_kind = case.get("loop_kind", "edit")
    disposition = case.get("disposition", "")
    old_digest = case.get("old_digest")
    new_digest = case.get("new_digest")
    delta = case.get("delta_summary", "")
    if loop_kind in {"read_only", "audit_only"} and disposition == "unchanged":
        return old_digest == new_digest and ref_exists(root, case.get("artifact_or_clause_ref", ""))
    if disposition in {"extends", "resolved", "supersedes"}:
        return old_digest != new_digest and material_delta(delta)
    return disposition == "unchanged"


def is_substantive_codex_adapter(receipts: list[dict]) -> bool:
    for receipt in receipts:
        if not receipt.get("accepted", True):
            continue
        runtime = str(receipt.get("runtime", "")).lower()
        family = str(receipt.get("family", "")).lower()
        if runtime in EXTERNAL_RUNTIMES or family in EXTERNAL_RUNTIMES:
            return True
    return False


def family_statuses_allow_full(statuses: dict, substantive: bool) -> bool:
    if not substantive:
        return True
    return all(statuses.get(family) in PASSING_FAMILY_STATUSES for family in REQUIRED_FAMILIES)


def prose_status_ok(prose_status_claims: list[str], terminal_status: str, prose_body: str = "") -> bool:
    canonical = f"done_status:{terminal_status}"
    if any(claim != canonical for claim in prose_status_claims):
        return False
    if terminal_status != "done":
        body_tokens = set(re.findall(r"[a-z]+", prose_body.lower()))
        if body_tokens & COMPLETION_SYNONYMS:
            return False
    return True


def done_gate_ok(done_predicate: dict) -> bool:
    return (
        done_predicate.get("consecutive_empty_new_finding_loops_observed", 0)
        >= done_predicate.get("consecutive_empty_new_finding_loops_required", 2)
        and done_predicate.get("unresolved_load_bearing_findings_count", 1) == 0
        and done_predicate.get("validator_or_audit_findings_count", 0) == 0
        and done_predicate.get("audit_chain_fixed_point") is True
        and len(done_predicate.get("audit_receipt_ids", [])) >= 2
    )


def assert_packet_identity(root: Path) -> bool:
    manifest = root / "PACKET_MANIFEST_v4_1.md"
    premortem = root / "skills/premortem/SKILL.md"
    return manifest.exists() and premortem.exists() and "packet: v4.1" in manifest.read_text()


def stale_skill_mirror_detected(root: Path) -> bool:
    source = root / "skills/premortem/SKILL.md"
    mirror = root / "conformance/fixtures/stale_mirror/premortem/SKILL.md"
    if not source.exists() or not mirror.exists():
        return False
    return sha256_file(source) != sha256_file(mirror)


def fixture_cases_are_bound(fixtures: list[dict], case_names: set[str]) -> bool:
    return all(fixture.get("validator_case") in case_names for fixture in fixtures)


def dispositions_ref_summary_ok(root: Path) -> bool:
    path = root / "conformance/fixtures/sample_cross_loop_ledger_v4_1.json"
    data = json.loads(path.read_text())
    summary = data["disposition_summary"]
    dispositions = data["dispositions"]
    return summary["dispositions_count"] == len(dispositions) and summary["prior_open_count"] == len({d["prior_finding_id"] for d in dispositions})


CASE_NAMES = {
    "audit_prose_only_divergence",
    "audit_structural_divergence",
    "cross_loop_boilerplate_delta",
    "cross_loop_fresh_delta",
    "missing_model_family_key",
    "prose_yaml_contradiction",
    "bogus_skill_digest",
    "stale_skill_mirror",
    "meta_clause_fixture_mapping",
    "index_without_validator",
    "recomputed_skill_digest",
    "author_asserted_structural_axis",
    "read_only_loop_unchanged_digest",
    "receipt_derived_substantive_classifier",
    "completion_synonym_prose",
    "skill_body_quote_anchor",
    "dispositions_ref_summary",
    "hypothesis_not_load_bearing",
}


def run_case(name: str, root: Path, validator_exists: bool, fixtures: list[dict]) -> bool:
    if name == "audit_prose_only_divergence":
        a = {"model_family": "opus", "runtime": "claude", "prompt_seed_or_digest": "seed-2026050701", "receipt_bundle_digest": "aaa"}
        b = {"model_family": "opus", "runtime": "claude", "prompt_seed_or_digest": "seed-2026050702", "receipt_bundle_digest": "aaa"}
        return has_structural_divergence(a, b)
    if name == "audit_structural_divergence":
        a = {"model_family": "opus", "runtime": "claude", "prompt_seed_or_digest": "seed-a", "receipt_bundle_digest": "aaa"}
        b = {"model_family": "sonnet", "runtime": "claude", "prompt_seed_or_digest": "seed-a", "receipt_bundle_digest": "aaa"}
        return has_structural_divergence(a, b)
    if name == "cross_loop_boilerplate_delta":
        return cross_loop_delta_ok({"loop_kind": "edit", "disposition": "extends", "old_digest": "aaa", "new_digest": "bbb", "delta_summary": "Updated wording for clarity and intent"}, root)
    if name == "cross_loop_fresh_delta":
        return cross_loop_delta_ok({"loop_kind": "edit", "disposition": "extends", "old_digest": "aaa", "new_digest": "bbb", "delta_summary": "validator recomputes digest from cited packet local bytes"}, root)
    if name == "missing_model_family_key":
        return family_statuses_allow_full({"opus": "completed", "sonnet": "completed"}, substantive=True)
    if name == "prose_yaml_contradiction":
        return prose_status_ok(["done_status:continue"], "continue", "The run is green across the board.")
    if name == "bogus_skill_digest":
        return validate_skill_digest({"skill_body_read_ref": ["skills/premortem/SKILL.md"], "skill_body_source_digest": "not-a-digest"}, root)
    if name == "stale_skill_mirror":
        return not stale_skill_mirror_detected(root)
    if name == "meta_clause_fixture_mapping":
        return validator_exists and fixture_cases_are_bound(fixtures, CASE_NAMES)
    if name == "index_without_validator":
        return fixture_cases_are_bound([{"validator_case": "missing_case"}], CASE_NAMES)
    if name == "recomputed_skill_digest":
        path = root / "skills/premortem/SKILL.md"
        return validate_skill_digest({"skill_body_read_ref": [str(path)], "skill_body_source_digest": sha256_file(path)}, root)
    if name == "author_asserted_structural_axis":
        a = {"model_family": "opus", "runtime": "claude", "prompt_seed_or_digest": "seed-a", "receipt_bundle_digest": "aaa", "structural_axis_verified": True}
        b = {"model_family": "opus", "runtime": "claude", "prompt_seed_or_digest": "seed-a", "receipt_bundle_digest": "aaa", "structural_axis_verified": True}
        return has_structural_divergence(a, b)
    if name == "read_only_loop_unchanged_digest":
        return cross_loop_delta_ok({"loop_kind": "read_only", "disposition": "unchanged", "old_digest": "aaa", "new_digest": "aaa", "artifact_or_clause_ref": "schemas/COMPILE_GATE_SCHEMA_v4_1.md#`loop_kind` controls digest freshness"}, root)
    if name == "receipt_derived_substantive_classifier":
        receipts = [{"kind": "parent", "runtime": "claude_bridge", "accepted": True}]
        return is_substantive_codex_adapter(receipts)
    if name == "completion_synonym_prose":
        return prose_status_ok(["done_status:continue"], "continue", "This is green and shipped.")
    if name == "skill_body_quote_anchor":
        path = root / "skills/premortem/SKILL.md"
        digest, quote = quote_hash(path, 17, 22)
        return validate_quote_anchor({"source_path": str(path), "line_start": 17, "line_end": 22, "quote_sha256": digest, "quote_text": quote}, root)
    if name == "dispositions_ref_summary":
        return dispositions_ref_summary_ok(root)
    if name == "hypothesis_not_load_bearing":
        return done_gate_ok({
            "consecutive_empty_new_finding_loops_required": 2,
            "consecutive_empty_new_finding_loops_observed": 2,
            "unresolved_load_bearing_findings_count": 0,
            "premortem_hypotheses_count": 9,
            "validator_or_audit_findings_count": 0,
            "audit_chain_fixed_point": True,
            "audit_receipt_ids": ["audit-1", "audit-2"],
        })
    raise KeyError(name)


def clause_ref_exists(root: Path, clause_ref: str) -> bool:
    path_text, _, needle = clause_ref.partition("#")
    path = root / path_text
    if not path.exists():
        return False
    if not needle:
        return True
    return path.read_text().count(needle) == 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--packet-root", default=str(Path(__file__).resolve().parents[1]))
    args = parser.parse_args()
    root = Path(args.packet_root).resolve()
    if not assert_packet_identity(root):
        print("loop_contract_fixtures: fail")
        print(f"- invalid packet root: {root}")
        return 1
    index_path = root / "conformance/fixtures/loop_contract_fixtures_v4_1.json"
    data = json.loads(index_path.read_text())
    fixtures = data.get("fixtures", [])
    validator_path = root / data.get("validator", "")
    validator_exists = validator_path.exists()

    ids = [fixture["id"] for fixture in fixtures]
    errors: list[str] = []
    if len(ids) != len(set(ids)):
        errors.append("duplicate fixture id")
    if not validator_exists:
        errors.append(f"validator missing: {validator_path}")

    for fixture in fixtures:
        if not fixture.get("covers"):
            errors.append(f"{fixture['id']}: missing covers")
        if not fixture.get("clause_refs"):
            errors.append(f"{fixture['id']}: missing clause_refs")
        for clause_ref in fixture.get("clause_refs", []):
            if not clause_ref_exists(root, clause_ref):
                errors.append(f"{fixture['id']}: stale clause_ref {clause_ref}")

    for fixture in fixtures:
        case_name = fixture["validator_case"]
        observed_pass = run_case(case_name, root, validator_exists, fixtures)
        expected_pass = fixture["expected"] == "pass"
        if observed_pass != expected_pass:
            errors.append(f"{fixture['id']}: expected {fixture['expected']} observed {'pass' if observed_pass else 'fail'}")

    if errors:
        print("loop_contract_fixtures: fail")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"loop_contract_fixtures: pass ({len(fixtures)} fixtures)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

---

# Source: `conformance/fixtures/loop_contract_fixtures_v4_1.json`


{
  "packet": "v4.1",
  "fixture_index": "loop_contract_fixtures_v4_1",
  "validator": "conformance/validate_loop_contract_fixtures.py",
  "fixtures": [
    {
      "id": "FX-NF-11b-prose-divergence-only",
      "expected": "fail",
      "validator_case": "audit_prose_only_divergence",
      "covers": ["audit_independence.structural_axis_verified"],
      "clause_refs": ["schemas/COMPILE_GATE_SCHEMA_v4_1.md#Validators must inspect `audit_independence` as structured data"],
      "case": "Audit receipts differ only by prose, timestamp, or model label."
    },
    {
      "id": "FX-NF-11b-structural-divergence",
      "expected": "pass",
      "validator_case": "audit_structural_divergence",
      "covers": ["audit_independence.structural_axis_verified"],
      "clause_refs": ["schemas/COMPILE_GATE_SCHEMA_v4_1.md#The validator computes `structural_axis_verified` from primitive audit fields"],
      "case": "Audit receipts include a verified structural axis beyond timestamp or model label."
    },
    {
      "id": "FX-NF-12b-boilerplate-rationale",
      "expected": "fail",
      "validator_case": "cross_loop_boilerplate_delta",
      "covers": ["cross_loop.dispositions.artifact_or_clause_digest", "cross_loop.dispositions.delta_summary"],
      "clause_refs": ["schemas/COMPILE_GATE_SCHEMA_v4_1.md#Boilerplate rationales"],
      "case": "Cross-loop dispositions cover all ids but reuse boilerplate rationale, stale digest, or synonym-only deltas."
    },
    {
      "id": "FX-NF-12b-fresh-delta",
      "expected": "pass",
      "validator_case": "cross_loop_fresh_delta",
      "covers": ["cross_loop.dispositions.artifact_or_clause_digest", "cross_loop.dispositions.delta_summary"],
      "clause_refs": ["schemas/COMPILE_GATE_SCHEMA_v4_1.md#`artifact_or_clause_digest` is required"],
      "case": "Extends/resolved dispositions cite fresh active clause digests and material deltas."
    },
    {
      "id": "FX-OF-03b-missing-status-key",
      "expected": "fail",
      "validator_case": "missing_model_family_key",
      "covers": ["manager.resource_pressure.model_family_statuses"],
      "clause_refs": ["06_OUTPUT_FORMAT_AND_SCORING.md#If `manager.resource_pressure.model_family_statuses[family]` is absent"],
      "case": "A substantive Codex-adapter header omits a required model family key and claims FULL."
    },
    {
      "id": "FX-OF-10b-prose-yaml-contradiction",
      "expected": "fail",
      "validator_case": "prose_yaml_contradiction",
      "covers": ["wizard_loop_state"],
      "clause_refs": ["06_OUTPUT_FORMAT_AND_SCORING.md#The `wizard_loop_state` block is the operative loop state"],
      "case": "Visible prose says done/full while operative loop YAML says continue/partial."
    },
    {
      "id": "FX-NF-14a-bogus-digest",
      "expected": "fail",
      "validator_case": "bogus_skill_digest",
      "covers": ["council_member_skill.skill_body_source_digest"],
      "clause_refs": ["schemas/RECEIPT_SCHEMA_v4_1.md#For packet-local Wizard skills"],
      "case": "Premortem skill body digest is placeholder, malformed, or not recomputed from the packet-local file."
    },
    {
      "id": "FX-NF-14a-stale-mirror",
      "expected": "fail",
      "validator_case": "stale_skill_mirror",
      "covers": ["council_member_skill.mirror_digest", "council_member_skill.source_digest"],
      "clause_refs": ["schemas/RECEIPT_SCHEMA_v4_1.md#stale mirror digests"],
      "case": "Runtime mirror digest differs from packet-local source without an adapter delta."
    },
    {
      "id": "FX-meta-clause-fixture-mapping",
      "expected": "pass",
      "validator_case": "meta_clause_fixture_mapping",
      "covers": ["conformance_harness.fixture_mapping"],
      "clause_refs": ["09_CONFORMANCE_HARNESS.md#fixture mapping must be bidirectional"],
      "case": "Every new loop-contract clause maps to a fixture id or named test id, and every fixture id maps back to a live clause."
    },
    {
      "id": "FX-NF-15a-index-without-validator",
      "expected": "fail",
      "validator_case": "index_without_validator",
      "covers": ["conformance_harness.validator_binding"],
      "clause_refs": ["09_CONFORMANCE_HARNESS.md#The packet-local validator is"],
      "case": "Fixture ids exist but no validator consumes them."
    },
    {
      "id": "FX-NF-15b-recomputed-skill-digest",
      "expected": "pass",
      "validator_case": "recomputed_skill_digest",
      "covers": ["council_member_skill.skill_body_source_digest"],
      "clause_refs": ["schemas/RECEIPT_SCHEMA_v4_1.md#Validators must recompute this digest"],
      "case": "Validator recomputes the premortem skill digest from the packet-local path."
    },
    {
      "id": "FX-NF-15c-author-asserted-structural-axis",
      "expected": "fail",
      "validator_case": "author_asserted_structural_axis",
      "covers": ["audit_independence.structural_axis_verified"],
      "clause_refs": ["schemas/COMPILE_GATE_SCHEMA_v4_1.md#receipt boolean is advisory"],
      "case": "Receipt asserts structural-axis verification while primitive fields match."
    },
    {
      "id": "FX-NF-15d-read-only-loop-unchanged-digest",
      "expected": "pass",
      "validator_case": "read_only_loop_unchanged_digest",
      "covers": ["wizard_loop_state.loop_kind", "cross_loop.dispositions.artifact_or_clause_digest"],
      "clause_refs": ["schemas/COMPILE_GATE_SCHEMA_v4_1.md#`loop_kind` controls digest freshness"],
      "case": "Read-only loop keeps a finding unchanged against the same digest."
    },
    {
      "id": "FX-NF-15e-receipt-derived-substantive-classifier",
      "expected": "pass",
      "validator_case": "receipt_derived_substantive_classifier",
      "covers": ["manager.resource_pressure.model_family_statuses"],
      "clause_refs": ["06_OUTPUT_FORMAT_AND_SCORING.md#computed from receipts"],
      "case": "Accepted route receipts activate family accounting regardless of renderer label."
    },
    {
      "id": "FX-NF-15f-completion-synonym-prose",
      "expected": "fail",
      "validator_case": "completion_synonym_prose",
      "covers": ["wizard_loop_state.done_predicate.terminal_status"],
      "clause_refs": ["06_OUTPUT_FORMAT_AND_SCORING.md#Visible prose must use the canonical loop status token"],
      "case": "Prose uses a completion synonym that contradicts YAML."
    },
    {
      "id": "FX-NF-15g-skill-body-quote-anchor",
      "expected": "pass",
      "validator_case": "skill_body_quote_anchor",
      "covers": ["council_member_skill.skill_body_quote_anchor"],
      "clause_refs": ["schemas/RECEIPT_SCHEMA_v4_1.md#Skill-backed receipts also need a short quote anchor"],
      "case": "Quote anchor hash matches the cited packet-local skill line range."
    },
    {
      "id": "FX-NF-15h-dispositions-ref-summary",
      "expected": "pass",
      "validator_case": "dispositions_ref_summary",
      "covers": ["cross_loop.dispositions_ref", "cross_loop.disposition_summary"],
      "clause_refs": ["schemas/COMPILE_GATE_SCHEMA_v4_1.md#Full disposition ledgers may live behind `dispositions_ref`"],
      "case": "Large ledgers may be cited by dispositions_ref with summary while validator inspects the full ledger."
    },
    {
      "id": "FX-NF-15i-hypothesis-not-load-bearing",
      "expected": "pass",
      "validator_case": "hypothesis_not_load_bearing",
      "covers": ["done_predicate.unresolved_load_bearing_findings_count"],
      "clause_refs": ["schemas/COMPILE_GATE_SCHEMA_v4_1.md#Premortem hypotheses are valuable raw"],
      "case": "Raw premortem hypotheses do not reset the done predicate unless promoted to load-bearing."
    }
  ]
}

---

# Source: `conformance/fixtures/sample_cross_loop_ledger_v4_1.json`


{
  "disposition_summary": {
    "prior_open_count": 2,
    "dispositions_count": 2,
    "supersedes": 0,
    "kills": 0,
    "extends": 1,
    "resolved": 0,
    "unchanged": 1
  },
  "dispositions": [
    {
      "prior_finding_id": "NF-sample-1",
      "finding_kind": "validator_gap",
      "load_bearing_for_done": true,
      "disposition": "extends"
    },
    {
      "prior_finding_id": "NF-sample-2",
      "finding_kind": "premortem_hypothesis",
      "load_bearing_for_done": false,
      "disposition": "unchanged"
    }
  ]
}

---

# Source: `conformance/fixtures/stale_mirror/premortem/SKILL.md`


---
name: premortem
description: stale mirror fixture for Wizard v4.1 validator tests
---

# Premortem Stale Mirror Fixture

This file intentionally differs from the packet-local premortem skill. It is a
negative fixture used by `validate_loop_contract_fixtures.py` to prove stale
mirrors are inspected instead of hardcoded.

---

# Source: `10_DELIBERATOR_CONTRACT.md`


---
title: Wizard v4.1 Deliberator Contract
type: deliberator_contract
packet: v4.1
framing: standalone
---

# Deliberator Contract v4.1

This contract hardens the Wizard synthesis step.

It is inspired by the HEAVYSKILL parallel-reasoning then sequential-deliberation
pattern, but it is not a new council, new voice family, or proof that the
preprint transfers locally. It is a small gate on the existing controller
synthesis: parallel receipts are useful only when the sequential deliberator
keeps their evidence, dissent, and executable deltas intact.

## Heavy Thinking Shape

For a substantive Wizard run, parent and child workers create independent
trajectories. The controller then performs sequential deliberation over a
serialized trajectory cache.

The cache is not free-form memory. Every cached trajectory needs:

```yaml
trajectory_cache_entry:
  trajectory_id:
  source_receipt_id:
  source_slice_or_surface:
  core_claim:
  reasoning_path:
  evidence_anchor:
  operation_or_falsifier:
  conclusion_direction:
  executable_delta:
  dissent_or_anomaly:
  pruning_reason:
  evidence_boundary:
```

If a trajectory is pruned, the cache must keep what was lost and why. Pruning
can reduce length; it cannot remove provenance, stage/status, dissent, or the
smallest executable delta.

## Synthesis Gate

Every controller synthesis over plural worker receipts must carry:

```yaml
deliberator_contract:
  query_class: verifiable | subjective | mixed | unclear
  per_thinker_verdict:
    - thinker_receipt_id:
      verdict: agree | dissent | wrong | abstain | hold_divergent
      reason:
      evidence_anchor:
  all_wrong_rederive:
    required: true | false
    performed: true | false
    derivation_anchor:
  minority_report:
    preserved:
    promoted_to_test:
    killed:
    why:
  format_alignment_check:
  status: passed | blocked | partial
```

The deliberator must critically evaluate trajectories. It must not vote, merge
pleasantly, or treat agreement as correctness. If all useful trajectories are
wrong, stale, unsupported, or non-load-bearing, the controller re-derives from
the source material or blocks.

## Query Classes

- `verifiable`: correctness can be checked against artifacts, commands, tests,
  formal results, citations, or other inspectable evidence.
- `subjective`: the output depends mainly on taste, positioning, voice,
  preference, or human judgment.
- `mixed`: both verifiable and subjective parts matter.
- `unclear`: the controller cannot classify the task yet.

For `subjective` tasks, the deliberator preserves live readings instead of
forcing agreement. Use `hold_divergent` when a trajectory remains useful
without becoming the final answer.

For `verifiable` tasks, at least one accepted conclusion must point to an
addressable evidence anchor. If no accepted trajectory has such an anchor, the
gate is blocked or the controller performs a fresh derivation with an anchor.

## Anti-Theater Rules

- A cache entry without `source_receipt_id` is memory theater.
- A cache entry without `executable_delta` cannot justify a runnable follow-up.
- A synthesis with all verdicts as `agree` must either prove earned convergence
  through distinct evidence anchors or trigger a divergence audit.
- A minority trajectory that is strange but testable must become a bounded
  falsification task, be killed by a named artifact, or remain visible as a
  preserved minority report.
- A deliberator may cite a preprint or outside method as inspiration, but local
  receipts decide readiness.

## What This Does Not Do

This contract does not add a fourth council.

It does not change the canonical council identities: Decision, Failure, and
Follow-Up.

It does not make parallel reasoning sufficient for execution readiness.

It does not let a serialized cache replace receipts, compile gates, or adapter
strict profiles.

---

# Source: `definitions/MEMBER_DEFINITIONS_v4_1.md`


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

---

# Source: `schemas/RECEIPT_SCHEMA_v4_1.md`


---
title: Wizard v4.1 Receipt Schema
type: schema
packet: v4.1
framing: standalone
---

# Receipt Schema v4.1

```yaml
receipt_id:
packet: v4.1
kind: parent | child | management_parent | tool | adapter | source_lift | compile_gate
wave: decision | failure | follow_up | audit | none
member_id:
family:
runtime:
worker_id:
parent_receipt_id:
loaded_salience:
  full_mmm:
  mini_mmm:
council_member_skill:
  skill_id:
  owning_member_id:
  canonical_skill_path:
  skill_method_invoked: true | false
  skill_body_read: true | false
  skill_body_read_ref:
    - <path-or-receipt-ref>
  skill_body_reader_worker_id:
  skill_body_source_packet: v4.1
  skill_body_source_digest:
  skill_body_quote_anchor:
    source_path:
    line_start:
    line_end:
    quote_sha256:
    quote_text:
  runtime_mirror_path:
  source_digest:
  mirror_digest:
  source_version:
  mirror_version:
  load_status: loaded | blocked | missing | stale_mirror | degraded_local
  mirror_status: not_needed | loaded | missing | stale | adapter_delta_declared
  adapter_delta:
  skill_side_effects:
    created_files:
    modified_files:
    opened_browser:
    external_network:
  accepted_for_member: true | false
  blocked_reason:
task_card:
source_slice:
tool_surface:
terminal_status: completed | blocked | timed_out | rerouted | superseded | simulated | deferred
execution_evidence:
artifact_or_output:
route_topology:
  spawn_surface:
  worker_id:
  launch_artifact:
  terminal_receipt:
  launched_by_parent_receipt_id:
  child_receipt_ids:
  usable_work_product:
child_rerouter:
  management_parent_id:
  management_scope:
  formal_child_obligation:
  liveness_deadline_sec:
  action_on_timeout:
  counted_child_ids:
  deferred_child_ids:
  rerouted_child_ids:
  child_health_summary:
  terminal_disposition: accepted | partial | blocked | deferred
children_cited:
  - <child_receipt_id>
dissent_recorded:
  - child_id:
    position:
    parent_handled_by:
no_dissent_observed: true | false
killed_options:
  - child_id:
    option:
    override_required:
binding_clause:
child_impact_ledger:
  <child_receipt_id>:
    impact: changed | killed | added | rejected | blocked | no_delta
    parent_effect:
    evidence_ref:
evidence_boundary:
what_this_does_not_prove:
core_claim:
reasoning_path:
evidence_anchors:
operation_or_falsifier:
conclusion_direction:
variant_signature:
  claim:
  exact_tool_or_function:
  carrier_or_fixture:
  mini_mmm:
  model:
  reasoning_effort:
  runtime:
  task_card:
  source_slice:
  operation_or_falsifier:
  distinct_delta:
  outcome_delta: changed_outcome | killed_option | found_evidence | found_bug | load_bearing_boundary | load_bearing_fixture | no_delta
  work_unit_fingerprint:
  blind_spot_declaration:
  value_score:
rerouter_ledger:
  lane_id:
  parent_receipt_id:
  requested_model:
  requested_reasoning:
  route:
  status: accepted | useful | slow | redundant | not_worth_it | rerouted | blocked | deferred | superseded
  reason_code:
  last_touch_at:
  evidence_ref:
  value_score:
  action_taken:
  superseded_by:
premortem:
  skill_loaded:
  skill_path:
  skill_load_status: loaded | blocked | degraded_local
  synthesis_worker_id:
  body_read_runtime:
  body_read_model:
  body_read_ref:
    - <path-or-receipt-ref>
  body_quote_anchor:
    source_path:
    line_start:
    line_end:
    quote_sha256:
    quote_text:
  side_effects:
    created_files: false
    opened_browser: false
  frame_set:
  context_minimum:
    what:
    who_affected:
    success_criteria:
  raw_failure_reasons:
    - id:
      reason:
  failure_story:
  hidden_assumption:
  early_warning_signs:
  prevention:
  synthesis:
    most_likely_failure:
    most_dangerous_failure:
    hidden_assumption:
    revised_plan:
    pre_execution_checklist:
  open_findings:
    - id:
      finding:
claude_bridge:
  skill_loaded:
  skill_path:
  wrapper:
  model:
  budget:
  timeout_sec:
  terminal_status: completed | blocked | timed_out | failed | degraded
  output_path:
  receipt_path:
  agent_task_evidence_observed: true | false
  usable_route_signal:
  cost:
premortem_follow_up_join_gate:
  source_parent_receipt_id:
  checked_before_follow_up: true
  mapped_findings:
    <premortem_open_finding_id>:
      disposition: out_of_scope | stop_condition | required_hardening | dismissed_by_artifact
      target:
      artifact_or_clause:
manager_rerouter:
  scope:
  liveness_deadline_sec:
  parent_statuses:
    <parent_receipt_id>: completed | slow | timed_out | rerouted | blocked | deferred
  slow_parent_ids:
  rerouted_parent_ids:
  blocked_parent_ids:
  action_taken:
  evidence_ref:
  terminal_disposition: accepted | partial | blocked | deferred
management_parents:
  - kind: management_parent
    member_id: manager.rerouter | manager.child_health | manager.route_truth | manager.resource_pressure
    runtime:
    worker_id:
    loaded_salience:
      mini_mmm:
    scope:
    supervised_surfaces:
      - parent_liveness | child_health | route_truth | resource_pressure | footer_truth | runtime_fallback
      - queue_liveness | runner_preflight | sim_admissibility_gate | queue_readiness | formal_sim_profile
      - stage_gate | expected_result_surface | controller_read_artifacts | model_family_fallback | degraded_alt_child_families
    terminal_status: completed | blocked | timed_out | rerouted | deferred
    accepted: true | false
    does_not_vote: true
    action_taken:
    evidence_ref:
    artifact_or_output:
manager_resource_pressure:
  capacity_probe:
  model_family_statuses:
    codex_native:
    opus:
    sonnet:
    haiku:
    gemini:
    omx_tmux:
    tools:
  global_max_active:
  per_parent_max_concurrency:
  timeout_policy:
  degraded_alt_child_families:
    - missing_family:
      blocker:
      smaller_retry_attempted: true | false
      alt_family:
      alt_receipt_id:
      counts_as_missing_family: true
  throttle_decision:
  waste_stop_condition:
member_utility:
  distinct_contribution:
  decision_use:
  sim_relevance:
  theater_cut:
  current_disposition: kept | cut_this_run | reboot_candidate | suppress_this_context | retire_candidate
  reboot_note:
  initialization_assessment:
  suppression_scope:
  retirement_evidence:
accepted: true | false
blocked_reason:
supersedes:
superseded_by:
```

`blocked_reason` must name a concrete runtime/access/safety/timeout/destructive
scope failure or an evidence dependency that cannot be inspected safely. "No
exact implementation task," "nothing useful for a child to do," or "advisory
only" are not valid blocked reasons for child/subsubagent routes. Use a
same-prompt variant, mini-MMM salience check, outside-frame critique, falsifier,
scout, receipt audit, or follow-up prompt improver instead.

`council_member_skill` is required when a member or child is skill-backed.
Accepted skill-backed members must prove the packet-local canonical skill path,
any runtime-local mirror path, digest/version or explicit unknown digest,
load status, side-effect boundary, and adapter delta. A runtime mirror with no
upstream wiki path or stale mirror explanation cannot count as the canonical
member skill.

For packet-local Wizard skills, `skill_body_source_digest` is the lowercase
hex SHA-256 digest of the exact canonical packet-local skill file bytes read
by the worker. Validators must recompute this digest from
`canonical_skill_path` or `skill_body_read_ref`; placeholder digests,
malformed digests, stale mirror digests, or digest/path mismatches invalidate
`skill_body_read:true`. A generic unversioned `skills/premortem/SKILL.md`
reference is not enough without `skill_body_source_packet: v4.1`, the
packet-local path, and the recomputed digest.

Skill-backed receipts also need a short quote anchor from the skill body. The
anchor is not a report or transcript; it is a compact provenance check. The
validator recomputes `quote_sha256` from the cited line range and rejects
worker-id-only provenance when the quote anchor is missing, stale, or does not
belong to the same packet-local file.

`skill_method_invoked` and `skill_body_read` are separate. A worker can apply
the known method from its prompt, but canonical closeout requires
`skill_body_read:true` or an explicit blocker. For Premortem, `skill_body_read`
must cite `skills/premortem/SKILL.md`; otherwise the route is a degraded
premortem-method attempt, not a loaded skill receipt.

When `council_member_skill.load_status` is `loaded`, `skill_body_read_ref`
must be non-empty. For `failure.premortem_council`, `premortem.body_read_runtime`,
`premortem.body_read_model`, and `premortem.body_read_ref` must also be present
or the premortem is `degraded_local`.

The worker that reads the skill body must be the worker that emits the
skill-backed synthesis, unless the receipt explicitly records a delegated-read
blocker and marks the route `degraded_local`. For premortem, this means
`premortem.synthesis_worker_id` and
`council_member_skill.skill_body_reader_worker_id` must match for loaded
status.

Premortem loaded status also requires the body-read source to be the active
v4.1 packet-local skill or a runtime mirror with an explicit adapter delta and
matching upstream source. A generic `skills/premortem/SKILL.md` path without
packet version/source digest is insufficient.

The five structural fields are required when a receipt participates in a plural council synthesis or receipt-divergence gate. They may be omitted for narrow tool, adapter, or source-lift receipts that are not used as council evidence.

`failure.premortem_council` parent receipts must include `premortem`. The values must
show that the Premortem skill was loaded from
`skills/premortem/SKILL.md`, or name a concrete
runtime/access/path blocker and mark the route `blocked` or `degraded_local`.
They must also show real prospective hindsight: the six-month future-failure
frame, context minimum, raw failure reasons, hidden assumption, observable
early warning signs, concrete prevention, revised plan pressure, and the
fact that no files were created and no browser was opened. A premortem parent without
skill-loading evidence is not a counted Failure Council member for a
substantive Wizard run.

When `failure.premortem_council` leaves open findings, the run must also include a
`premortem_follow_up_join_gate` before Follow-Up synthesis. Every open finding
must map to `out_of_scope`, `stop_condition`, `required_hardening`, or an
addressed `dismissed_by_artifact`. Unmapped findings block or split the
compiled move.

`member_utility` is required for accepted parent member receipts in a visible full run. It records why this member was useful, how it affected the decision, how it relates to sim/QIT bounded evidence when relevant, and what theater it cut. This makes later tuning possible without pretending every member must remain mandatory forever.

Accepted parent receipts that launch children must bind child work into parent
synthesis. `children_cited` names the child receipts explicitly used by the
parent. `dissent_recorded` preserves child disagreement or blockers, unless
`no_dissent_observed` is true. `killed_options` prevents the parent from
silently resurrecting an option a child killed without an override reason.
`binding_clause` states how child disagreement survived smoothing.
`child_impact_ledger` marks each child as `changed`, `killed`, `added`,
`rejected`, `blocked`, or `no_delta`; `no_delta` children do not count toward
child quorum.

Budget-success is not enough for child quorum. A counted child must produce a
usable route signal with at least one concrete claim, falsifier/check, artifact
boundary, failure story, prompt improvement, or parent-impact delta. Completed
external-worker receipts that are empty, generic, shape-identical to siblings,
or marked weak/no-delta remain evidence of a run attempt but do not count as
accepted children.

Before child fanout, the parent must establish a context minimum. For general
Wizard work this is target, user-visible success condition, artifact/output
surface, and stop condition. For premortem work this is what failed, who is
affected, and success criteria. If the context minimum is underspecified, the
parent must infer it explicitly or mark the child route `degraded_local`; it
must not let children hallucinate the frame.

`theater_cut` is a current-run judgment, not a permanent verdict on the member. A member that produced theater may be `cut_this_run`, `reboot_candidate`, or `suppress_this_context` depending on whether the problem was the member's value, the task card, the source slice, the model/runtime, or the initialization. `retire_candidate` should require repeated evidence across contexts, not one bad run.

If `current_disposition` is `reboot_candidate`, `reboot_note` must name the concrete delta for the next attempt: boot, task card, source slice, model/runtime, or mini-MMM variant. If `current_disposition` is `retire_candidate`, `retirement_evidence` must summarize repeated cross-context failure.

`variant_signature` is adapter-local and required only when a child/subsubagent is counted as a same-triple variant for sim/proof/QIT work. The invariant is the same exact claim, exact tool/function/API surface, and carrier/fixture; the variant signature records what changed in initialization, model/runtime, task card, source slice, or falsifier. Variants that differ only by label or wording are redundancy, not proof.

For counted child/subsubagent model experiments, `variant_signature.model` and `variant_signature.reasoning_effort` are required. A model/reasoning variant is useful only when the receipt also records a usable work product, a distinct delta, an artifact-facing `outcome_delta`, a sibling-unique `work_unit_fingerprint`, a concrete `blind_spot_declaration`, and a value score of at least `2/3`; changing the model label alone is not evidence.

For substantive Codex-adapter Wizard runs, accepted child receipts must cover
the child model matrix when runtimes are available: Codex-native, Opus, Sonnet,
Haiku, and Gemini-attempt/degraded coverage. A missing family is a missing
obligation, not a harmless runtime preference. The matrix can be fulfilled by
parent-launched children with narrower task cards; direct main-thread calls and
tool checks do not count.

Every counted parent in a substantive Codex-adapter run must also prove child
quorum: 5-10 completed accepted child/subsubagent receipts with reciprocal
parent linkage and sibling-unique work units. A parent below five is not
countable unless the adapter explicitly marks an atomic/low-decomposition
override with evidence that more children would be artificial. A parent above
ten is a stress run and needs a receipt-shape/divergence audit before synthesis.

`follow_up.prompt_voice_council` has an explicit low-decomposition override
when it runs exactly the four required prompt voices: Orwell, Strategy,
Factory, and Hume. It may count as complete at 4/4 only when each voice returns
a distinct prompt improvement and the parent records why a fifth child would be
padding.

Multiple children from the same model family may count only when they have
distinct task cards, sibling-unique `work_unit_fingerprint` values, concrete
artifact-facing `outcome_delta` values, and useful work products. A second
Sonnet child, Codex child, or Haiku child is evidence only when it changes the
bounded work, kills an option, finds evidence, finds a bug, or exposes a
load-bearing boundary/fixture. It is theater when it only repeats a sibling.

`outcome_delta` must name a real effect: `changed_outcome`, `killed_option`,
`found_evidence`, `found_bug`, `load_bearing_boundary`, or
`load_bearing_fixture`. `no_delta`, clarification-only output, duplicated
sibling work, and padded "no change" wording do not count toward quorum.
For sim/probe children, a countable delta must bind to the exact stage, claim,
tool/function/API surface, carrier/fixture, and positive plus
negative/boundary check. Child agreement does not promote sim status.

`rerouter_ledger` is required for counted child/subsubagent model/reasoning matrix runs. Count only ledger rows with the same `claim`, `exact_tool_or_function`, and `carrier_or_fixture` invariant, proven `route_topology`, terminal `completed` status, usable work product, non-empty `distinct_delta`, and `value_score` of at least `2/3`. Rows marked `slow`, `redundant`, `not_worth_it`, `rerouted`, `blocked`, `deferred`, `superseded`, or `simulated` are useful diagnostics, but they are not plurality evidence.

`manager_rerouter` is the global parent/council liveness ledger. It is separate
from parent-local `child_rerouter` and cannot substitute for child health.
Accepted global status requires every accepted parent receipt id to appear in
`parent_statuses`, no unresolved parent ids when terminal disposition is
`accepted`, and an addressable `evidence_ref`.

`management_parents` are required orchestration receipts for full Max Assembly:
`manager.rerouter`, `manager.child_health`, `manager.route_truth`, and
`manager.resource_pressure`. They must be non-voting and receipt-backed. They
may block, reroute, shrink, or request sharper child work, but they cannot cast
a council vote, replace a council parent, or synthesize the answer.

For sim/probe/queue-visible work, management-parent `supervised_surfaces` must
include the relevant sim live surfaces: queue liveness, runner preflight,
sim-admissibility, queue readiness, formal sim profile, stage gate, expected
result surface, controller-read artifacts, model-family fallback, and
degraded-alt child family tracking. Route accounting without these surfaces is
not sim admission evidence.

Every parent-local `child_rerouter` must name `management_parent_id`,
`management_scope`, and `formal_child_obligation`. The formal obligation must
match the parent route definition. A parent-local rerouter without these fields
does not prove child-council health even when the global manager completed.
`management_parent_id` must be `manager.child_health`; liveness, route-truth,
or resource-pressure managers cannot replace the child-health supervisor.

For sim loop state, `admitted_by` must not name a runner, controller,
self-certified route, or any `manager.*` parent. Management can supervise,
block, and reroute; it cannot admit its own supervised pre-run as queue-ready
evidence.

## Acceptance

A receipt is accepted only when:

- the assigned member/route is clear;
- required MMM or mini-MMM load is named;
- terminal status is explicit;
- evidence is usable;
- evidence boundary is honest.
- route topology proves the worker was actually launched, reached a terminal receipt, and produced a usable work product.
- child receipts link back to parent launch evidence and stay narrower than the parent route.
- child receipts pass parent-local rerouter checks before synthesis: terminal completion, reciprocal parent child id, sibling-unique work unit, non-`no_delta` outcome, and usable artifact-facing delta.
- parent receipts that launch children include a local `child_rerouter` summary
  whose counted child ids match the route topology.

Controller synthesis cannot create accepted receipts.

---

# Source: `schemas/COMPILE_GATE_SCHEMA_v4_1.md`


---
title: Wizard v4.1 Compile Gate Schema
type: schema
packet: v4.1
framing: standalone
---

# Compile Gate Schema v4.1

## Universal Gate

```yaml
bounded_work_compile_gate:
  target:
  immediate_action:
  owner_lane:
  success_check:
  stop_condition:
  artifact_output_surface:
  status: salience_only | proposal | bounded_work_candidate | ready_for_execution | executed | accepted | partial | blocked | deferred
```

## Optional Adapter Strict Gate

```yaml
adapter_strict_compile_gate:
  adapter_name:
  classification:
  stage:
  claim:
  carrier_or_fixture:
  exact_tool_or_function:
  positive_check:
  negative_or_boundary_check:
  expected_result_surface:
  prior_receipts:
  adapter_status:
```

Optional embedded Wizard loop state:

```yaml
wizard_loop_state:
  loop_input_ref:
  prior_compiled_move_ref:
  selected_followup_ref:
  loop_iteration:
  loop_cap:
  loop_kind: edit | read_only | audit_only | mixed
  loop_stop_condition:
  loop_receipt_bundle_ref:
  cross_loop:
    prior_loop_id:
    dispositions_ref:
    disposition_summary:
      prior_open_count:
      dispositions_count:
      supersedes:
      kills:
      extends:
      resolved:
      unchanged:
    max_visible_dispositions:
    dispositions:
      - prior_finding_id:
        finding_kind: premortem_hypothesis | validator_gap | audit_gap | implementation_gap | residual_risk
        load_bearing_for_done: true | false
        disposition: supersedes | kills | extends | resolved | unchanged
        disposition_rationale:
        artifact_or_clause_ref:
        artifact_or_clause_digest:
        delta_summary:
    new_findings:
  done_predicate:
    consecutive_empty_new_finding_loops_required:
    consecutive_empty_new_finding_loops_observed:
    unresolved_findings_count:
    unresolved_load_bearing_findings_count:
    premortem_hypotheses_count:
    validator_or_audit_findings_count:
    audit_chain_fixed_point: true | false
    audit_receipt_ids:
      - <audit-receipt-id>
    audit_independence:
      - audit_receipt_id:
        worker_id:
        model_family:
        runtime:
        prompt_seed_or_digest:
        receipt_bundle_digest:
        divergence_vector:
        structural_axis_verified: true | false
        timestamp_only_difference: true | false
        model_label_only_difference: true | false
    terminal_status: done | continue | cap_reached | blocked
  handoff_status: none | prepared | waiting_for_approval | launched | returned | blocked
  confidence_standard:
  confidence_status: open | sufficient | impossible | blocked
  unresolved_loopholes:
  from_state:
  to_state:
  admitted_by:
  admission_artifact:
  next_input_status:
  freshness_gate:
    checked_at:
    git_status_ref:
    ledger_ref:
    queue_ref:
    runner_preflight_ref:
    source_artifact_refs:
  runner_success_cited:
  runner_result_artifact:
  controller_read_artifacts:
```

The general loop fields apply to ordinary strategy, docs, code, research, and
system work. The sim freshness/admission fields are active only for
sim/proof/QIT adapter work.

For `loop_iteration > 1`, `cross_loop.dispositions` must cover every prior
load-bearing open finding exactly once. Each disposition needs a rationale and
an artifact or clause reference. If dispositions are missing, duplicated, or
rationale-free, the loop is an independent or malformed re-prompt and cannot
advance the loop counter. `done` requires the configured consecutive
empty-new-finding loops, zero unresolved load-bearing findings, and an audit
fixed point; otherwise the loop stops only as `cap_reached` or `blocked`.

`artifact_or_clause_digest` is required for `extends`, `resolved`, and
`supersedes`. It is the digest of the cited active artifact or clause after the
current loop's edit. `extends` also requires a non-reused `delta_summary` that
names the material change since the prior loop. Boilerplate rationales,
synonym-only wording changes, or reused artifact/clause digests cannot resolve
or advance a prior finding.

`loop_kind` controls digest freshness. For `edit` and `mixed` loops,
`extends`, `resolved`, and `supersedes` require a fresh changed digest unless
the referenced clause was intentionally unchanged and the disposition is
`unchanged`. For `read_only` and `audit_only` loops, unchanged findings may
cite the prior active digest without pretending an edit occurred; read-only
loops cannot close an edit-required finding unless the cited existing artifact
already contains the fix and the validator recomputes the digest.

Full disposition ledgers may live behind `dispositions_ref` when prior finding
count is large. Visible output should show `disposition_summary`; validators
must still read the full ledger. The visible answer fails if it truncates the
only copy of the disposition ledger.

`done_predicate.terminal_status` defaults to `continue`. A renderer must refuse
to emit `done` unless consecutive empty-new-finding loops meet the configured
threshold, `unresolved_findings_count` is zero, `audit_chain_fixed_point` is
true, and `audit_receipt_ids` names the independent audit receipts.

Audit independence requires more than distinct worker ids. The fixed point
needs at least one divergence vector across the audit receipts: different model
family, runtime/account, prompt seed or digest, receipt-bundle sample, or
explicit adversarial task card. Shape-identical sibling audits under the same
controller prompt do not satisfy `audit_chain_fixed_point`.

Timestamp-only prompt seed changes and model-label-only changes do not satisfy
audit independence. At least one structural axis must differ: runtime/account,
sampled receipt-bundle digest, adversarial task card, or materially different
prompt digest verified against the actual prompt text.
Validators must inspect `audit_independence` as structured data. A prose claim
that two audits were different does not count unless `structural_axis_verified`
is true and both `timestamp_only_difference` and
`model_label_only_difference` are false for at least one accepted audit pair.
The validator computes `structural_axis_verified` from primitive audit fields;
the receipt boolean is advisory. A pair passes only when at least one of
`model_family`, `runtime`, `prompt_seed_or_digest`, `receipt_bundle_digest`, or
an explicit adversarial task-card id materially differs, and the difference is
not merely a timestamp or label alias.

`unresolved_findings_count` is human-readable. The done gate uses
`unresolved_load_bearing_findings_count`. Premortem hypotheses are valuable raw
failure pressure, but they do not keep the consecutive-empty counter at zero
unless the controller promotes them to load-bearing validator, audit,
implementation, or residual-risk findings.

`pre_run_passed_unadmitted` may not become `queue_ready`, `admitted_evidence`, or `admitted` without `admitted_by` from a non-runner admission gate and a controller-read admission artifact. Runner success may not advance readiness unless the controller read the cited result artifact.

Optional pre-output route-truth gate, used when a next-input handoff, promptless wake, resumed thread, or visible Wizard output is being rendered:

```yaml
pre_output_route_truth_gate:
  current_input_hash:
  newest_request_ref:
  receipt_bundle_ref:
  receipt_bundle_digest:
  runtime_receipt_refs:
  child_obligation_status:
  handoff_path:
  final_output_artifact:
  compiled_move_ref:
  freshness_gate_ref:
  accepted_parent_receipt_ids:
  accepted_child_receipt_ids:
  header_counts:
    waves_completed:
    parents_completed:
    parents_required:
    children_completed:
    children_attempted:
    tools_completed:
  runtime_labels:
  checked_before_render: true
  controller_synthesis_boundary:
```

This gate joins the active input identity, receipt bundle path and digest, runtime receipt refs, current child obligation status, next-input handoff, current freshness check, accepted route receipts, rendered header counts, and final output surface. `current_input_hash` covers that joined identity. Separate freshness, receipt, and output checks are not enough if they are not joined before rendering.

The optional strict gate is invalid unless `classification` explicitly activates it.

Ordinary docs cleanup, bug triage, refactor planning, research synthesis, implementation handoff, product strategy, and decision support use only the universal gate unless an adapter says otherwise.

## Mandatory Post-Council Gates

These gates are not council parent members. They run after the relevant council
barrier and must be receipt-backed before the visible answer can imply
readiness.

```yaml
post_follow_up_compile_gate:
  source_gate_ref: bounded_work_compile_gate
  checked_after_follow_up: true
  terminal_status: passed | blocked
  status:
  blocked_reason:

divergence_preservation_gate:
  checked_after_each_council: true
  parent_receipt_ids:
  minimum_children_cited_per_parent:
  terminal_status: passed | blocked
  dropped_with_reason:
```

For sim, probe, proof, queue-visible, runner, or result work, add the
sim-admissibility gate:

```yaml
sim_admissibility_gate:
  classification:
  checked_after_decision: true
  result: one_exact_packet | blocked_none_ready
  blocked_reason:
  packet_ref:
  stage:
  claim:
  carrier_or_fixture:
  exact_tool_or_function:
  positive_check:
  negative_or_boundary_check:
  expected_result_surface:
  adapter_status:
  source_task_ref:
  source_context_digest:
  source_receipt_bundle_digest:
```

`post_follow_up_compile_gate` prevents polished Follow-Up options from implying
execution readiness before the universal compile gate passes.
`divergence_preservation_gate` prevents child/subsubagent fanout from being
smoothed away by requiring parent synthesis to cite child receipts and preserve
dissent or killed options. `sim_admissibility_gate` translates Wizard route
truth into sim truth: exactly one bounded packet, or `blocked_none_ready`.

Runner construction and validation use the same strictness predicate: explicit
strict classification or detected sim/probe/queue-visible surface in prompt,
source context, or bounded-work gate. Detected strictness without a supplied
exact strict packet must use `blocked_none_ready`; it must not auto-generate
placeholder stage, claim, fixture, tool/function, or result path fields.

Runtime status matrix:

| Case | Required status |
| --- | --- |
| Non-sim work with universal gate | No sim-admissibility gate; universal status decides |
| Detected sim/probe/queue-visible surface without strict packet | `BLOCKED`, `adapter_status: blocked`, `result: blocked_none_ready` |
| Explicit sim/probe/queue-visible classification without strict packet | `BLOCKED`, `adapter_status: blocked`, `result: blocked_none_ready` |
| Supplied strict packet | `one_exact_packet` only if `source_task_ref`, `source_context_digest`, and `source_receipt_bundle_digest` match current input |
| Stale or unbound supplied strict packet | `BLOCKED`, `adapter_status: blocked`, `result: blocked_none_ready` |

---

# Source: `skills/SKILLS_MANIFEST_v4_1.md`


---
title: Wizard v4.1 Skills Manifest
type: skills_manifest
packet: v4.1
framing: standalone
---

# Wizard v4.1 Skills Manifest

This packet carries local skills. Skills are executable workflow dependencies,
not reference prose.

## Skill Architecture

The wiki packet is the portable source of truth for Wizard skills. Runtime
systems mirror or adapt these skills into their own local skill surfaces
(`~/.codex/skills`, Claude project skills, Gemini/OMX wrappers, or other agent
skill registries), but the canonical definitions live here so every system can
reference the same member behavior.

Skill-backed council members are allowed and encouraged when a member has a
repeatable workflow rather than just a salience role. A member skill must be:

- portable: no runtime-specific paths unless in an adapter section;
- receipt-shaped: it returns what ran, what changed, what stayed blocked, and
  what evidence supports the claim;
- MMM-compatible: it names the main/compact/mini-MMM surface it expects;
- loop-safe: it has a stop condition, iteration cap, or confidence gate;
- non-authoritative: it informs the parent council but does not replace
  Decision, Failure, Follow-Up, child-health, or compile-gate receipts.

Agent systems may maintain runtime-local versions of these skills, but a
runtime-local copy must declare its upstream wiki source path and any adapter
differences. If the runtime copy diverges without a declared adapter reason,
the packet-local wiki skill wins.

## Required Skills

- `claude-bridge`
  - Local path: `skills/claude-bridge/SKILL.md`
  - Required by: substantive Codex-adapter Wizard runs when external Claude worker capacity is available.
  - Purpose: run Claude Code as an external worker pool with bounded model routing, budgets, timeouts, and receipts.
  - Required local wrappers:
    - `skills/claude-bridge/scripts/claude_bridge.py`
    - `skills/claude-bridge/scripts/claude_child_fanout.py`
    - `skills/claude-bridge/scripts/fanout_receipt_summary.py`
  - Count rule: Claude Bridge counts only when the wrapper returns a receipt with model, status, output path, receipt path, and usable route signal. Claude final prose without receipt evidence is advisory only.

- `premortem`
  - Local path: `skills/premortem/SKILL.md`
  - Required by: `failure.premortem_council`
  - Purpose: Gary Klein-style prospective-hindsight premortem.
  - Wizard boundary: returns receipt fields only; does not create reports,
    transcripts, HTML, or open a browser.
  - Count rule: A premortem route only counts when this skill is loaded and
    its workflow is used, or when the route is explicitly marked blocked or
    degraded with the missing skill path.

## Portable Council-Member Skills

Canonical portable council-member skills live under
`skills/council-members/`. These are wiki-level skills that any agent runtime
can mirror locally:

| skill_id | owning member/route | binding | canonical path | Codex mirror path | side-effect boundary | count/block rule |
| --- | --- | --- | --- | --- | --- | --- |
| `strategy-loop` | `voice.strategy`, loop controller children | optional | `skills/council-members/strategy-loop/SKILL.md` | `~/.codex/skills/wizard-strategy-loop/SKILL.md` | no external side effects | Counts only with skill receipt and loop-control return fields. |
| `systems-strategy` | `voice.systems`, strategy audit children | optional | `skills/council-members/systems-strategy/SKILL.md` | `~/.codex/skills/wizard-systems-strategy/SKILL.md` | no external side effects | Counts only when it names system boundary, feedback loop, and local-optimization risk. |
| `loophole-auditor` | Failure/loop audit routes | optional | `skills/council-members/loophole-auditor/SKILL.md` | `~/.codex/skills/wizard-loophole-auditor/SKILL.md` | no external side effects | Counts only when it declares evidence standard, loopholes, fixes, confidence status, and stop/next-loop condition. |
| `follow-up-selector` | `follow_up.prompt_voice_council`, `follow_up.lane_council` | optional | `skills/council-members/follow-up-selector/SKILL.md` | `~/.codex/skills/wizard-follow-up-selector/SKILL.md` | no external side effects | Counts only when it makes, pre-runs, audits, improves, and selects a next prompt. |
| `factory-handoff` | `voice.factory`, queue/handoff children | optional | `skills/council-members/factory-handoff/SKILL.md` | `~/.codex/skills/wizard-factory-handoff/SKILL.md` | no external side effects | Counts only when it returns bottleneck, next station, handoff artifact, leverage, and queue movement check. |

Digest/version rule: receipts should record `source_digest` and
`mirror_digest` when the runtime can compute them. If a digest is unavailable,
the receipt must say `unknown` and name the exact file path loaded. A stale
mirror is blocked unless the adapter delta explains why it is intentionally
different.

These skills can be assigned to council parents or children through task cards.
They still require receipts and child/parent linkage. A skill call is not a
council member unless a real worker or tool invoked it and returned a receipt.

## External Loop Skill

- `codex-autoresearch`
  - Canonical runtime skill: `~/.agents/skills/codex-autoresearch/SKILL.md`.
  - Wizard role: long-running improve/verify loop for measurable goals after
    the Wizard has produced a bounded goal, metric, scope, verification command,
    guard, iteration cap, and stop condition.
  - Boundary: interactive launches keep the codex-autoresearch ask-before-act
    rule. The Wizard may prepare an autoresearch launch packet and ask for the
    required run-mode approval; it must not silently start a background
    autoresearch loop unless the user explicitly approved that launch mode.
  - Count rule: autoresearch receipts are loop-runtime evidence, not
    Decision/Failure/Follow-Up council replacements.

## Runtime-Callable Codex Skill Registry

The Wizard may route council parents or children through existing Codex skills
when the task matches the skill and the worker returns a receipt-shaped result.
Do not load every skill into every worker. Select the narrowest useful skill for
the route, record the loaded path, and keep the skill inside the parent/child
receipt boundary.

| skill_id | default Wizard use | route fit | count/block rule |
| --- | --- | --- | --- |
| `codex-autoresearch` | bounded improve/verify loop after a compiled move has a metric, guard, cap, and approval | Follow-Up loop runtime, not a council replacement | Counts only as loop evidence with launch approval/run mode and verification command. |
| `prior-art` | check whether the repo/history already contains the same strategy, failure, or pattern | Decision experts, Failure falsifiers, Follow-Up scout | Counts only when it cites inspected local sources and says what is reused, contradicted, or absent. |
| `prompt-guard` | adversarial prompt/security boundary scan | Failure falsifier or loophole child | Counts only with explicit attack/failure class, affected surface, and fix/stop condition. |
| `arch` | architecture and trade-off review | Decision experts, Strategy/System voices | Counts only with quality attributes, trade-off, and boundary/rollback condition. |
| `testing-golden-artifacts` | make output regressions testable | Follow-Up compile gate, Failure prevention child | Counts only with a concrete golden artifact/check and update policy. |
| `safe-run-maintenance` | archive-first cleanup and repo hygiene | Factory/handoff, Follow-Up lane | Counts only when it avoids destructive cleanup and names archive/keep/delete classes. |
| `thread-run-monitor` | detect stalled/blocked workers | management.child_health, management.rerouter | Counts only with worker ids/statuses, deadlines, and reroute action. |
| `thread-dispatch-controller` | bounded worker launch planning | management.resource_pressure, management.rerouter | Counts only with launch plan, pool split, deadline, and receipt requirement. |
| `pro-return-instant-audit` | audit returned external/deep-research packets | Failure falsifier, Follow-Up audit | Counts only with accepted/rejected findings and evidence refs. |
| `a2-brain-refresh` | refresh Ratchet A2 context before memory-sensitive work | Decision context parent | Counts only with exact read/write boundary and no hidden memory promotion. |
| `ratchet-a2-a1` | inspect Ratchet brain/memory surfaces without flattening contradictions | Decision experts, Systems voice | Counts only with contradiction-preserving summary and source refs. |
| `brain-delta-consolidation` | consolidate accepted loop findings into small memory deltas | Follow-Up compile gate after acceptance | Counts only after the compile gate accepts the underlying finding. |
| `tribunal` | independent multi-model comparison | Decision or Failure child, never as controller synthesis | Counts only with distinct model receipts and disagreement summary. |
| `cdo` | multi-agent deliberation pattern when a route needs broader framing | Decision experts or Failure audit child | Counts only when route-specific receipts remain separate from synthesis. |

Skills with broad side effects, external accounts, publishing, UI/browser
automation, commits, pushes, reminders, or long-running background behavior are
not default Wizard council members. They may be prepared as Follow-Up options
only when the option includes approval boundary, run mode, stop condition, and
verification surface.

## Load Rule

Main Wizard docs name which routes require skills. The active route loads the
local skill before running. Global runtime copies, such as Codex skills under
`~/.codex/skills`, may mirror these skills, but packet-local skills are the
portable source for standalone Wizard.

For substantive Codex-adapter Wizard work, both required skills load:

1. `skills/claude-bridge/SKILL.md`
2. `skills/premortem/SKILL.md`

Premortem provides the future-failure method. Claude Bridge provides external
worker execution and receipt evidence. They are separate obligations.

---

# Source: `skills/premortem/SKILL.md`


---
name: premortem
description: Wizard-embedded premortem method for Failure Council. Assumes the selected move failed six months later, works backward to expose failure causes, hidden assumptions, early warnings, and revised-plan pressure. This packet-local version returns receipt fields only; it does not create documents or open a browser.
---

# Premortem

Use this skill inside `failure.premortem_council`.

This is Gary Klein-style prospective hindsight: imagine the selected move has
already failed six months from now, then work backward to identify why. The goal
is not generic risk analysis. The goal is specific failure pressure that changes
the compiled move, stop condition, or follow-up options.

## Wizard Boundary

This packet-local skill is embedded in Wizard. It does not:

- create an HTML report;
- create a markdown transcript;
- open a browser or web page;
- write files unless a separate route explicitly asks for an artifact.

It returns structured premortem evidence to the Wizard receipt.

## Context Minimum

Before running, establish:

1. What move is being premortemed.
2. Who or what it affects.
3. What success would have looked like.

Infer this from Wizard Decision Council receipts and task context when possible.
Ask only if the premortem would otherwise be meaningless.

## Workflow

### 1. Set The Frame

Use this frame:

```text
It is six months from now. The selected move failed. We are looking back to understand exactly what went wrong.
```

### 2. Generate Raw Failure Reasons

List the genuine ways this move could have failed. Each reason must be:

- specific to the selected move;
- plausible and consequential;
- grounded in the task/source context;
- not padded.

### 3. Deep Dive

For each load-bearing failure reason, produce:

- failure story;
- underlying assumption;
- early warning signs;
- prevention or hardening move.

Use child workers when the runtime supports them. If child workers cannot run,
mark the route `degraded_local` and do the deep dives locally. Do not pretend
children ran.

### 4. Synthesize

Return:

- most likely failure;
- most dangerous failure;
- hidden assumption;
- revised plan pressure;
- pre-execution checklist;
- open findings that must join Follow-Up as stop conditions, required
  hardening, or blockers.

## Receipt Output

Populate the Wizard receipt `premortem` field with:

```yaml
skill_loaded: true
skill_path: skills/premortem/SKILL.md
skill_load_status: loaded | blocked | degraded_local
frame_set: true
context_minimum:
  what:
  who_affected:
  success_criteria:
raw_failure_reasons:
  - id:
    reason:
deep_dives:
  - failure_reason_id:
    failure_story:
    hidden_assumption:
    early_warning_signs:
    prevention:
synthesis:
  most_likely_failure:
  most_dangerous_failure:
  hidden_assumption:
  revised_plan:
  pre_execution_checklist:
open_findings:
  - id:
    finding:
```

## Quality Bar

- Set the failed-six-months frame every time.
- Ground failure modes in the actual move and evidence boundary.
- Make hardening concrete.
- Feed unresolved findings into the Follow-Up join gate.
- Do not output generic risk lists.
- Do not create files or open a web page.

---

# Source: `skills/claude-bridge/SKILL.md`


---
name: claude-bridge
description: Run Claude Code from Codex when the user asks to use Claude, Opus, Sonnet, Haiku, Claude subagents, or a mixed Claude/Codex review. Provides simple model routing, budget caps, receipt capture, and stream-json evidence for real Agent/Task use.
---

# Claude Bridge

Use this skill when Codex should call Claude Code as an external worker from the current session.

## Quick Start

Prefer the wrapper script:

```bash
python3 ~/.codex/skills/claude-bridge/scripts/claude_bridge.py \
  --model opus \
  --prompt "Review this plan and return risks plus a verdict."
```

For prompts in a file:

```bash
python3 ~/.codex/skills/claude-bridge/scripts/claude_bridge.py \
  --model sonnet \
  --prompt-file /tmp/prompt.txt \
  --budget 3
```

For Claude Agent/Task evidence, use stream mode:

```bash
python3 ~/.codex/skills/claude-bridge/scripts/claude_bridge.py \
  --model opus \
  --stream \
  --tools Task,Read,Grep,Glob,Bash,Write \
  --prompt "Use Agent/Task to launch haiku and sonnet workers, then synthesize."
```

For bounded parent-to-child fanout from a Codex subagent, prefer the fanout
wrapper. It gives every child a wall-clock timeout and returns one parent-readable
receipt:

```bash
python3 ~/.codex/skills/claude-bridge/scripts/claude_child_fanout.py \
  --name parent-scale-test \
  --model sonnet \
  --effort high \
  --budget 1 \
  --timeout-sec 90 \
  --max-concurrency 4 \
  --jobs-file /tmp/child_jobs.json
```

Use direct `claude_bridge.py` for one child. Use `claude_child_fanout.py` for
two or more children.

When several Codex parents may launch Claude children at the same time, add a
shared model-level limiter:

```bash
python3 ~/.codex/skills/claude-bridge/scripts/claude_child_fanout.py \
  --name parent-wave-limited \
  --model haiku \
  --budget 1 \
  --timeout-sec 120 \
  --max-concurrency 4 \
  --stop-after-completed 4 \
  --global-timeout-sec 120 \
  --global-max-active 8 \
  --jobs-file /tmp/child_jobs.json
```

Use `--stop-after-completed` for scouting routes where a useful subset is
enough. Use `--global-max-active` to prevent many Codex parents from starting
too many Claude CLI children at once.

Summarize completed fanout receipts with:

```bash
python3 ~/.codex/skills/claude-bridge/scripts/fanout_receipt_summary.py \
  --route-prefix parent-wave-limited \
  --show-routes
```

Use the summary utility before reporting Wizard header counts. It counts
completed child receipts, separates abandoned/not-launched children, and avoids
turning final answers into log parsing.

## Model Routing

- `opus` -> `claude-opus-4-7`: deep audit, hard reasoning, final arbitration, large fanout controller.
- `sonnet` -> `claude-sonnet-4-6`: implementation, execution, debugging, test-running, medium-cost worker.
- `haiku` -> `claude-haiku-4-5-20251001`: inventory, counting, file summaries, cheap scout work.

Use explicit model names if the user asks for one.

## Operating Rules

1. Work through `/tmp` for experiments unless the user asks to change repo files.
2. Always set `--budget` for non-trivial calls. Default is conservative.
3. Use `--stream` when proving subagents actually ran; parse the stream for `Agent` tool calls, `task_started`, and `task_notification`.
4. Treat Claude output as an external worker receipt, not native Codex state.
5. Report the output path, receipt path, model used, cost, and whether Agent/Task evidence was observed.
6. If direct Claude fails with a socket/auth error, tell the user the Codex process lacks Claude/network access and retry only after access is restored.
7. For Codex parent -> Claude child scaling, use explicit timeouts. A child that starts but does not return a receipt is not a completed subsubagent.
8. If stream-mode Task fanout stalls, reroute through `claude_child_fanout.py` with no tools first. Let the Codex parent provide source slices in the prompt; add Claude tools only after no-tool fanout is stable.

## Verification Pattern

After a call, inspect the generated receipt JSON. For stream-mode subagent work, count:

- `Agent` tool-use events
- `task_started` events
- completed `task_notification` events
- returned worker tokens or report files
- `modelUsage` entries

Do not claim "subagents ran" from a final answer alone.

For `claude_child_fanout.py`, inspect `fanout_receipt.json` and count only
children with `"status": "completed"`. Prefer `fanout_receipt_summary.py` when
multiple parent receipts are involved. Current measured safe ladder from Codex
parent agents:

- 1 parent x 1 Sonnet-high child: stable.
- 1 parent x 2 Sonnet-high children: stable.
- 1 parent x 3 Sonnet-high children: stable.
- 1 parent x 4 Sonnet-high children: stable with a 60s+ timeout.
- 1 parent x 6 Sonnet-high children: stable with `--timeout-sec 90 --max-concurrency 4`.
- 1 parent x 8 Sonnet-high children: partial in the observed run, 7 completed and 1 timed out.
- 2 parents x 4 Sonnet-high children: usable, but one long-tail child timed out at 120s and rerouted cleanly.
- 2 parents x 4 Haiku children: stable and fast; 8/8 completed in the observed run.
- 1 parent x 2 Gemini children: partial under 45s, then a 1-child reroute completed under 60s.
- 2 parents x 6 Sonnet-high children: stable in the observed run with 12/12 completed under a 150s child cap.
- 4 parents x 4 Haiku children: stable in the observed run with 16/16 completed under a 75s child cap.
- 1 parent x 12 Haiku children: completed under a 90s child cap, but output quality started to drift.
- 1 parent x 4 Gemini children: partial in the observed run; keep Gemini narrow until more evidence exists.
- 1 parent x 1 Opus child: completed, but behaved as arbitration/conflict review rather than scout work.
- 4 parents x 6 Sonnet-high children: stable in the observed run with 24/24 completed under a 180s child cap.
- 4 parents x 8 Haiku children: stable in completion with 32/32 completed under a 100s child cap, but output quality drift increased.
- 4 parents x 2 Gemini children: stable in the observed run with 8/8 completed under a 120s cap, but CLI warning noise is present.
- Mixed four-parent wave with Sonnet 6 + Haiku 8 + Gemini 2 + Opus 1: 17/17 completed.
- 8 parents x 8 Sonnet-high children: stable in the observed run with 64/64 completed under a 210s child cap.
- 8 parents x 12 Sonnet-high children: stable in the observed run with 96/96 completed under a 260s child cap.
- 7 parents x 12 Sonnet-high children plus 1 parent x 4 Opus-high children: stable in the observed run with 88/88 completed, zero failures/timeouts, max observed parent duration about 70s.
- 7 parents x 16 Sonnet-high children at concurrency 8 plus 1 parent x 4 Opus-high children: stable in completion with 116/116 completed, zero failures/timeouts, max observed parent duration about 107s. Opus arbitration rated this a partial pass because quality drift and receipt homogeneity become the soft limit before raw spawn failure.
- 8 parents x 12 Haiku children: stable in completion with 96/96 completed after parent-return reroutes; use smaller per-parent concurrency or the limiter for normal use.
- 8 parents x 16 Haiku children at concurrency 8: unstable; completed 118 but timed out 14 because the run stampedes Claude child starts and drains slow tails.
- 8 parents x 8 Haiku with `--stop-after-completed 4 --global-max-active 8`: stable operating shape; 32 useful completions, 0 timeouts, tails abandoned or not launched by design.

Default starting point for future Codex parent tests:

```text
8 parents x 12 Sonnet-high children, timeout 260s, max concurrency 4 per parent
```

Default Wizard v4 throttle after the 116-child limit probe:

```text
Use 8 Codex parents when a real Max Assembly run needs broad plurality.
Use Sonnet-high as the main child pool at 6-8 children per parent per council wave.
Use 10 Sonnet-high children per parent only as the upper normal setting when the task genuinely decomposes that far.
Use 11+ children per parent only as a stress setting, with max concurrency 8 and a receipt-shape/divergence audit before synthesis.
Reserve Opus-high for arbitration, usually 1 parent x 4 children.
Throttle down when the last quartile of child receipts stops adding distinct throttle signals, Opus reports shape-identical receipts, or parent p95 latency approaches the timeout.
```

For wide cheap scout lanes, Haiku is currently the fastest stable Claude child
model, but it needs global child-start throttling when many parents overlap.
A proven scout shape is 8 parents x 8 Haiku children with
`--stop-after-completed 4 --global-max-active 8`. Use Gemini as a bounded
fallback for narrow, well-defined lanes rather than as the first high-width
child pool. Use Opus for rare arbitration, not wide fanout.

---

# Source: `skills/council-members/README.md`


# Wizard v4.1 Council-Member Skills

These are portable wiki-hosted council-member skills. Runtime systems can
mirror them into local skill registries, but mirrors must name the upstream
wiki path and adapter differences.

Canonical skills:

- `strategy-loop/SKILL.md`
- `systems-strategy/SKILL.md`
- `loophole-auditor/SKILL.md`
- `follow-up-selector/SKILL.md`
- `factory-handoff/SKILL.md`

These skills are executable workflow dependencies. A skill-backed member counts
only when a real worker or tool loads the skill and returns a receipt.

---

# Source: `skills/council-members/strategy-loop/SKILL.md`


---
name: wizard-strategy-loop
description: Strategy council-member skill for Wizard v4.1. Use when a parent or child must sequence work, decide priority, set hold/retreat conditions, or choose whether the Wizard should loop, execute, split, or stop.
---

# Wizard Strategy Loop Skill

Canonical source: `~/wiki/wizard/packet-v4-1-current/skills/council-members/strategy-loop/SKILL.md`

## Load

Load the assigned Strategy mini-MMM or sparse registry slice, the task card,
the current loop state, and the source/receipt slice. Do not load sibling
voices unless assigned a cross-voice composition.

## Return

```yaml
strategy_loop:
  priority:
  sequence:
  hold_condition:
  retreat_condition:
  next_loop_input:
  stop_condition:
  reason:
```

## Boundary

This skill recommends sequence and loop control. It does not replace Decision,
Failure, Follow-Up, child-health, or the compile gate.

---

# Source: `skills/council-members/systems-strategy/SKILL.md`


---
name: wizard-systems-strategy
description: Systems council-member skill for Wizard v4.1. Use when the Wizard must step back from local optimization and inspect whole-system context, feedback loops, second-order effects, or strategy drift.
---

# Wizard Systems Strategy Skill

Canonical source: `~/wiki/wizard/packet-v4-1-current/skills/council-members/systems-strategy/SKILL.md`

## Load

Load the assigned Systems mini-MMM or systems family slice, task/source
context, loop state, and relevant receipts. Do not optimize the local prompt
until the system boundary is named.

## Return

```yaml
systems_strategy:
  system_boundary:
  active_feedback_loop:
  second_order_effect:
  local_optimization_risk:
  step_back_recommendation:
  intervention:
  evidence_needed:
```

## Boundary

This skill can tell the Wizard to step back, split, or change target. It cannot
declare the compiled move ready without the normal compile gate.

---

# Source: `skills/council-members/loophole-auditor/SKILL.md`


---
name: wizard-loophole-auditor
description: Confidence and loophole audit skill for Wizard v4.1. Use when a strategy must be stress-tested until no known unresolved loophole remains under a declared evidence standard or loop cap.
---

# Wizard Loophole Auditor Skill

Canonical source: `~/wiki/wizard/packet-v4-1-current/skills/council-members/loophole-auditor/SKILL.md`

## Driver Prompt

```text
Are you 100% confident in this strategy? If not, find all possible loopholes,
suggest proper fixes, and run this loop until you are factually 100% confident
in the new strategy.
```

## Runtime Meaning

`100% confident` means no known unresolved loophole remains under the declared
evidence standard, verification checks, child coverage, and loop cap. If
literal certainty is impossible, return the remaining uncertainty and the
evidence needed. Do not manufacture certainty.

## Return

```yaml
loophole_audit:
  strategy_under_test:
  evidence_standard:
  loopholes:
    - loophole:
      severity:
      fix:
      verification:
      status: open | fixed | blocked | out_of_scope
  confidence_status: open | sufficient | impossible | blocked
  next_loop_input:
  stop_condition:
```

## Boundary

This skill drives another Wizard loop when loopholes remain. It is not launch
approval for codex-autoresearch and not a substitute for Premortem.

---

# Source: `skills/council-members/follow-up-selector/SKILL.md`


---
name: wizard-follow-up-selector
description: Follow-Up council-member skill for Wizard v4.1. Use to generate, pre-run, audit, improve, and select the next Wizard prompt.
---

# Wizard Follow-Up Selector Skill

Canonical source: `~/wiki/wizard/packet-v4-1-current/skills/council-members/follow-up-selector/SKILL.md`

## Loop

1. Make divergent candidate prompts.
2. Pre-run the first action and first blocker.
3. Audit ambiguity, scope creep, missing check, missing stop, and hidden dependency.
4. Improve the prompt.
5. Select the next Wizard input or mark blocked.

## Return

```yaml
follow_up_selector:
  candidate_count:
  selected_prompt:
  payoff:
  use_when:
  stop_if:
  artifact_output_surface:
  verification_or_receipt_check:
  alternates:
```

## Boundary

The selected prompt re-enters the Wizard loop with prior receipts and context.
It does not bypass Decision, Failure, and Follow-Up.

---

# Source: `skills/council-members/factory-handoff/SKILL.md`


---
name: wizard-factory-handoff
description: Factory council-member skill for Wizard v4.1. Use to identify bottlenecks, next station, handoff artifact, queue movement, and leverage.
---

# Wizard Factory Handoff Skill

Canonical source: `~/wiki/wizard/packet-v4-1-current/skills/council-members/factory-handoff/SKILL.md`

## Return

```yaml
factory_handoff:
  bottleneck:
  next_station:
  handoff_artifact:
  leverage_point:
  queue_movement_check:
  stop_condition:
```

## Boundary

This skill moves work through the system. It does not lower evidence gates or
turn process prose into execution proof.
