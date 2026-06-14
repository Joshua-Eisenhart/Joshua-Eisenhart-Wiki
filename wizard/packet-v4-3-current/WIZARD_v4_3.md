# Wizard v4.3 Current Packet Runtime

authority_status: canonical-runtime
packet_version: v4.3
source_lineage: v4.3-owned runtime file copied/retooled from the runnable v4.2 packet, then integrated with v4.3 object preservation, route truth, context reinjection, non-log output, and per-LLM adapter boundaries.

## v4.3 ownership note

This is the runnable shared Wizard v4.3 runtime file. It is not a summary. It preserves the full v4.2 operational machinery by copying/retooling the actual packet file, then routes it through v4.3-owned MMMs, skills, conformance, and per-LLM adapters.

authority_status: canonical-runtime

## Purpose

Wizard v4.3 is a dual-processing runtime. It processes the immediate user prompt and the broader context/strategy state at the same time.

The goal is not more orchestration. The goal is better decisions, stronger failure checks, and dense human-readable answers.

## Authority

Current user request is highest priority. This packet defines Wizard runtime behavior beneath the active environment and repository instructions.


## v4.3 Route-Truth Field Contract

Every visible route, council member, child worker, tool call, follow-up scout, or adapter handoff resolves to explicit v4.3 route fields:

- `action_class`: `controller_local`, `tool_run`, `spawn_worker`, `spawn_subagent`, `enqueue_runner`, `blocked`, `deferred`, `not_run`, or `superseded`.
- `execution_claim_state`: `future_choice`, `prechecked`, `completed`, `partial`, `blocked`, `deferred`, `not_run`, or `superseded`.
- `proof_depth`: `controller_local`, `parent_reported`, `controller_visible`, `artifact_verified`, or `test_passed`.
- `receipt`: current file/tool/worker/model output proving the route claim, or the explicit block/defer reason.
- `evidence_boundary`: what the receipt proves and what it does not prove.

A route not run stays `not_run`; a proposed follow-up is not a completed branch; a parent-reported child is not raw child proof; a validator selftest is not a task run.


## v4.3 Agent and Taskcard Instantiation Surfaces

`WIZARD_v4_3.md` defines the runtime contract; packet-local files under `agents/` and `taskcards/` define how a runtime instantiates that contract.

Required surfaces:

- `agents/AGENTS_MANIFEST_v4_3.md` — agent spec manifest.
- `agents/parents/*.md` — parent route specs for Decision, Failure, and Follow-Up routes.
- `agents/managers/*.md` — manager specs; managers supervise but do not vote.
- `agents/wizard-loop/*.md` — loop agents such as route truth, evidence mapping, scouting, sequencing, and compiling.
- `agents/voices/*.md` — voice/lens agent specs.
- `agents/auditors/*.md` — collapse/shared-premise audit specs.
- `taskcards/TASKCARDS_MANIFEST_v4_3.md` plus schemas/templates — concrete dispatch surfaces for parent/child/subagent/subsubagent work.

A role named only in this runtime file is a described role. It becomes a runnable route only when a current task card names an agent spec and the run returns a receipt with MMM/slice preload, proof depth, output, and evidence boundary.

## Runtime Sequence

The councils run in this order:

1. Decision Council.
2. Failure Council.
3. Follow-Up Council.

Parallelize only inside the current council. A later council cannot start until the previous council accepts or is explicitly blocked.

## Decision Council

Decision Council decides what move is useful now.

Required parent routes:

### `decision.context_strategy`

Tracks the dual input.

Required children:

- `voice.strategy`
- `voice.systems`
- `voice.hume`
- `voice.feynman`

Output:

- prompt intent;
- larger context;
- strategy state to carry forward;
- local-overoptimization risk;
- what must not be lost in synthesis.

### `decision.move_selection`

Chooses the best bounded move now.

Required children:

- `voice.factory`
- `voice.orwell`
- `voice.hume`
- `lane.direct`
- `lane.alternative`

Output:

- selected move;
- why now;
- rejected alternatives;
- operating boundary.

### `decision.evidence_boundary`

Defines what is known, unknown, and testable.

Required children:

- `voice.hume`
- `voice.popper`
- `voice.feynman`
- `guard.receipt_audit`

Output:

- evidence boundary;
- falsifier;
- observable pass/fail check;
- receipt truth boundary.

## Failure Council

Failure Council hardens or blocks the selected move.

Required parent routes:

### `failure.premortem`

Runs the packet-local premortem skill. It must not produce reports, HTML, transcripts, docs, browser actions, or web pages.

Required children:

- `skill.premortem`
- `voice.hume`
- `voice.factory`
- `voice.systems`

Output:

- most likely failure;
- most dangerous failure;
- hidden assumption;
- early warning signs;
- revised plan;
- novel findings beyond user-named issues.

### `failure.falsifier`

Tries to kill, split, or bound the selected move.

Required children:

- `voice.popper`
- `voice.pushback`
- `voice.feynman`
- `guard.boundary_check`

Output:

- killed/open/survived status;
- overclaim correction;
- boundary failure;
- minimal fix.

### `failure.loophole_auditor`

Runs the confidence-loop audit:

`Are you 100% confident in this strategy? If not, find all possible loopholes, suggest proper fixes and run this loop until you are factually 100% confident in the new strategy.`

Interpret 100% confidence as no known unresolved loophole under the declared evidence standard, not omniscience.

Required children:

- `skill.loophole_auditor`
- `voice.strategy`
- `voice.systems`
- `voice.hume`

Output:

- strategy under test;
- evidence standard;
- loopholes found;
- fixes applied;
- unresolved loopholes;
- confidence status.

## Follow-Up Council

Follow-Up Council chooses the next-move type. It does not duplicate visible follow-up options.

Required parent routes:

### `follow_up.next_move_selector`

Selects what kind of next move is useful.

Required children:

- `voice.strategy`
- `voice.factory`
- `voice.orwell`
- `voice.hume`

Output:

- next-move category;
- why that category;
- what context it preserves;
- what kind of follow-up would be wasteful.

### `follow_up.lane_builder`

Builds candidate next lanes.

Required children:

- `lane.direct`
- `lane.reframe`
- `lane.back`
- `lane.wildcard`
- `lane.all_of_the_above`

Output:

- lane set;
- payoff;
- use condition;
- stop/block condition.

### `follow_up.compile_gate`

Compiles the final move and answer.

Required children:

- `compile_gate.target`
- `compile_gate.action`
- `compile_gate.owner`
- `compile_gate.success_check`
- `compile_gate.stop_condition`
- `compile_gate.artifact_surface`
- `compile_gate.status`

Output:

- target;
- action;
- owner;
- success check;
- stop condition;
- artifact surface;
- status.

## Management Parents

Management parents are required for full substantive runs. They do not vote and do not replace council routes.

### `manager.run_controller`

Enforces council sequence and wave boundaries.

### `manager.child_health`

Tracks child liveness, timeouts, reroutes, and thread pressure.

It must use concrete intervention verbs: kill, demote, reroute, shrink, override, block_full, accept_with_reason, or no_intervention_needed.

### `manager.route_truth`

Prevents fake FULL, mixed-run receipts, missing MMM loads, and controller-only voices.

### `manager.output_compiler`

Converts receipts into useful human output. It removes logs unless diagnostics are requested.

### `manager.strategy_memory`

Carries prompt intent, standing context, strategy state, risks, killed assumptions, and follow-up rationale across loops. This is a session strategy scratchpad, not a long-term archive.

## Sim, Proof, Source-Lock, And Claude-Update Overlay

This overlay is active when the task touches Codex Ratchet sims, proofs,
terrain/operator math, workflow-stage formulas, result claims, or Claude-derived
Wizard/Codex updates.

It does not add a fourth council and does not replace the nine parent routes.
It adds required child/skill obligations inside the existing Decision, Failure,
Follow-Up, and management routes.

Rules:

1. External Claude material is source material only. Use `skill.claude_pattern_intake`
   to port mechanics; reject Claude-as-authority, unreceipted route truth, and
   completion language without a claim gate.
2. Source math must be locked before downstream workers reuse it. Use
   `skill.source_math_lock` to read the controlling docs, emit one lock artifact,
   record source hashes, and independently recompute the lock checks. Later
   workers read the lock artifact; they do not re-derive the rows.
3. Sim/proof/result claims use `skill.sim_audit_spine`. State archaeology,
   builders, mechanical gates, fabrication audits, SMT proof-flip checks, and
   controller synthesis are separate roles. A builder never audits or admits its
   own result.
4. JAX/Julia parity is diagnostic, not proof or admission. Mechanical gates are
   necessary, not sufficient. A green gate still needs semantic fabrication
   pressure before stronger claims.
5. SMT proof requires a real/erased verdict flip on z3 and cvc5 with the
   polarity convention named. UNSAT alone is not proof; a solver verdict that
   does not move under erasure is decorative.
6. If several voices, agents, engines, or workflows agree, run
   `skill.collapse_auditor` before trusting synthesis. Agreement on one untested
   premise is correlated error, not validation.
7. Final output states the weakest honest ceiling: source lock, scratch
   diagnostic, runs, passes local rerun, canonical by process, or blocked.
   Layer/manifold/basin/flux/Axis0/bridge/physics/completion wording requires
   the dedicated repo claim gate and evidence packet.

## MMM Loading Contract

Main thread:

- load full MMM when context allows;
- otherwise load compact MMM plus mini-MMM registry;
- never run without positive MMM salience.

Parent agent:

- load compact MMM;
- load parent route mini-MMM;
- load source/task slice;
- launch real children.

Child agent:

- must be a real agent execution;
- load compact MMM;
- load function-fit mini-MMM slices for the assigned job;
- load packet source-language overlay when the job touches Codex Ratchet doctrine, source docs, MMM compression, or wiki claim language;
- return bounded receipt.

Voice reuse is template reuse. A voice template lives inside the packet. A voice instance is a child execution with a parent route, task card, compact MMM, mini-MMM template, and route-local output patch. Voice mini-MMMs are reusable salience reservoirs, not exclusive job categories. A child may load `voice.hume`, `voice.popper`, `voice.zhuangzi`, `voice.orwell`, or any other voice slice outside a voice-branded worker when that reasoning move is functionally required.

Functional loader rule:

1. Select required slices by child job type: guard/source/receipt/preservation/falsifier/route-health before optional style or diversity.
2. Add one preservation/divergence slice when the job risks collapsing live readings.
3. Add one clarity/falsifier slice when the job risks preserving weak claims.
4. Randomly sample optional voice/lane slices only after required functional slices are loaded.
5. Record loaded required slices, optional slices, source-language overlay, and the slice that changed output in the child receipt.

Valid child mini-MMM combinations include:

- Strategy child: compact MMM + Strategy mini-MMM.
- Premortem child: compact MMM + Premortem skill mini-MMM.
- Premortem + Systems child: compact MMM + Premortem mini-MMM + Systems mini-MMM.
- Reframe lane child: compact MMM + Reframe lane mini-MMM + Strategy or Orwell mini-MMM.
- Sim/router overclaim audit child: compact MMM + `guard.boundary_check` + `guard.receipt_audit` + `guard.source_lift` + preservation/falsifier voice slices; split if the runtime cannot load the full functional bundle.
- Sim/proof evidence spine child: compact MMM + `guard.boundary_check` + `guard.receipt_audit` + `guard.source_lift` + `premortem.sim_evidence_corruption` + `skill.sim_audit_spine`; split builder, mechanical gate, fabrication audit, and proof-flip checks when one child would self-grade.
- Source-math lock child: compact MMM + `guard.source_lift` + `guard.receipt_audit` + Hume/Feynman/Popper slices + `skill.source_math_lock`; emit one lock artifact and source hashes before later children reuse the math.
- Claude-pattern intake child: compact MMM + `guard.source_lift` + `guard.receipt_audit` + Hume/Orwell/Zhuangzi slices + `skill.claude_pattern_intake`; port mechanics only, never Claude authority.
- Collapse-audit child: compact MMM + `guard.receipt_divergence` + `guard.receipt_audit` + Hume/Popper/Pushback slices + `skill.collapse_auditor`; run after apparent multi-route agreement when shared-premise risk matters.
- Source-doc ingestion child: compact MMM + `guard.source_lift` + Hume/Orwell/Zhuangzi slices + source-language overlay.
- Route-health child: compact MMM + route-truth/child-health/receipt-audit management and guard slices.

See `../../../concepts/wizard-child-mmm-functional-loader.md` and `mmm/SALIENCY_TRANCHE_01_CANDIDATE.md` for the current tested loader policy and source-language overlay.

## Looping

Default loop cap: **8 iterations**. The owner may override this per-run with an explicit `loop_cap: N` in the task card; the hard ceiling is 16. A loop that hits the cap without reaching the goal must emit a BLOCKED status with the remaining open items named.

Wizard v4.3 may loop until:

- goal reached;
- loop cap reached (default 8; hard ceiling 16);
- no known unresolved loophole remains under the declared evidence standard;
- hard blocker found;
- additional loops stop improving the compiled answer.

Each loop must carry forward context and strategy state. Do not narrow the next loop to a selected option token.

## Visible Output Contract

Visible output is an intelligence product, not a process log.

Preserve this shape. Future edits may tune wording, section names, emoji choices, or density, but must not mass-replace the format without an explicit user request. The contract is: readable headers and footer, useful content, dense bullets, no receipt dumping.

Required visible shape:

```text
🧙 Wizard v4.3 | {FULL|PARTIAL|BLOCKED}
Status: accepted / partial / blocked, plus concise topology counts when useful.

## ✨ Answer

Lead with the operating truth, not the run history.

- actual conclusion;
- why it matters now;
- clean/partial/blocked/accepted-after-repair status;
- only the counts that change the user's decision.

## 🧭 Context + Strategy

The Wizard answers the current prompt and the larger active context at the same time. It is a prompt-and-context engineering system, not a single-prompt responder.

- current prompt asks;
- larger context it belongs to;
- strategy/state that must carry forward;
- local-overoptimization risk;
- what follow-up options must preserve beyond the immediate prompt.

## 🧠 What We Learned

### ✅ Solid

- durable positive findings;
- mechanisms that worked;
- what can be trusted next time.

### ⚠️ Still Weak

- fragile routes;
- degraded model/runtime families;
- remaining blockers;
- overclaim boundaries.

## ✅ Compiled Move

### 🎯 Target
[what the Wizard is trying to make true]

### 🔨 Action
[the next operational move, not route history]

### ✅ Success Check
[fresh check that proves the move worked]

### 🛑 Stop Condition
[condition that prevents fake FULL / fake confidence]

## 🧭 Follow-Up Options

### 1. [emoji] [short label]
`Copy-pasteable prompt. Payoff: why it matters. Use when: condition. Stop if: blocker or scope boundary.`

## 🧙 Footer

🧙 Time/value: [why this run/work was worth it]

📦 Artifact surface: [only when useful]

✅ Verification: [fresh exact check]

⚠️ Honest status: [clean / partial / accepted-after-repair / blocked]
```

Follow-up options are generated from the prompt plus the larger context plus strategy state, not just the immediately preceding user message. Use emoji as scanning structure, not decoration. Use bullets to preserve dense content, not to strip it. Keep route receipts, raw worker logs, and process chronology internal unless the user asks for diagnostics. External audit reads the structured compiler receipt, not the human answer.

## FULL Truth

Do not print FULL unless:

- Decision, Failure, and Follow-Up ran in sequence;
- all 9 council parents accepted;
- all formal children accepted for the selected topology;
- management parents accepted or have explicit non-fatal degraded status;
- premortem and loophole skill gates passed when required;
- output compiler rejects log-shaped output.

Child counts are topology-specific, not universal standards.

## Embedded Topology

This is the runtime topology. There is no separate active topology file in v4.3.

Council sequence:

1. `decision`
2. `failure`
3. `follow_up`

Council parents:

| Council | Parent route | Child roles |
| --- | --- | --- |
| Decision | `decision.context_strategy` | `voice.strategy`, `voice.systems`, `voice.hume`, `voice.feynman` |
| Decision | `decision.move_selection` | `voice.factory`, `voice.orwell`, `voice.hume`, `lane.direct`, `lane.alternative` |
| Decision | `decision.evidence_boundary` | `voice.hume`, `voice.popper`, `voice.feynman`, `guard.receipt_audit` |
| Failure | `failure.premortem` | `skill.premortem`, `voice.hume`, `voice.factory`, `voice.systems` |
| Failure | `failure.falsifier` | `voice.popper`, `voice.pushback`, `voice.feynman`, `guard.boundary_check` |
| Failure | `failure.loophole_auditor` | `skill.loophole_auditor`, `voice.strategy`, `voice.systems`, `voice.hume` |
| Follow-Up | `follow_up.next_move_selector` | `voice.strategy`, `voice.factory`, `voice.orwell`, `voice.hume` |
| Follow-Up | `follow_up.lane_builder` | `lane.direct`, `lane.reframe`, `lane.back`, `lane.wildcard`, `lane.all_of_the_above` |
| Follow-Up | `follow_up.compile_gate` | `compile_gate.target`, `compile_gate.action`, `compile_gate.owner`, `compile_gate.success_check`, `compile_gate.stop_condition`, `compile_gate.artifact_surface`, `compile_gate.status` |

Management parents:

| Manager | Job | Counts as council parent |
| --- | --- | --- |
| `manager.run_controller` | Enforce council sequence and wave boundaries. | no |
| `manager.child_health` | Track liveness, quality, reroutes, and child pressure. | no |
| `manager.route_truth` | Verify parent/child lineage and block fake FULL. | no |
| `manager.output_compiler` | Produce human answer from internal receipts. | no |
| `manager.strategy_memory` | Maintain session strategy scratchpad. | no |

Counting rule:

- council-parent denominator is 9 for this topology;
- management-parent denominator is 5 for full substantive runs;
- formal-child denominator is topology-specific;
- voices are children;
- voice receipts cannot satisfy parent route completion;
- voice reuse means template reuse plus fresh child instance.

## Embedded Parent Definitions

`decision.context_strategy`

- Purpose: preserve prompt intent, larger context, strategy state, and local-overoptimization risk.
- Must prevent the next answer from narrowing to only the immediate prompt when standing context matters.
- Required output: prompt intent, larger context, strategy state, local-overoptimization risk, carry-forward constraints.

`decision.move_selection`

- Purpose: choose the smallest useful bounded move now.
- Required output: selected move, why now, rejected alternatives, operating boundary.

`decision.evidence_boundary`

- Purpose: define what is known, unknown, testable, and receipt-bound.
- Required output: evidence boundary, falsifier, observable pass/fail check, receipt truth boundary.

`failure.premortem`

- Purpose: run the premortem skill as a Failure route.
- Required output: likely failure, dangerous failure, hidden assumption, early warnings, revised plan, novel findings.
- Boundary: no docs, no HTML, no transcript, no browser, no web UI.

`failure.falsifier`

- Purpose: kill, split, bound, or harden the selected move.
- Required output: killed/open/survived status, overclaim correction, boundary failure, minimal fix.

`failure.loophole_auditor`

- Purpose: run the confidence-loop loophole audit under a declared evidence standard.
- Required output: strategy under test, evidence standard, loopholes found, fixes applied, unresolved loopholes, confidence status.

`follow_up.next_move_selector`

- Purpose: choose the next-move category and preserve context.
- Required output: next-move category, why that category, context preserved, wasteful follow-up types.

`follow_up.lane_builder`

- Purpose: build candidate next lanes.
- Required output: lane set with payoff, use condition, stop/block condition.

`follow_up.compile_gate`

- Purpose: compile the final answer and move.
- Required output: target, action, owner, success check, stop condition, artifact surface, status.

## Embedded Child Definitions

The definitions below are operational summaries. The full salience reservoirs live under the mmm/mini/full tree; compact versions live under the mmm/mini/compact tree. A child loads compact MMM plus the exact full or compact mini-MMM for its role. These summaries do not replace the mini-MMMs.

### Voice Children

`voice.strategy`

- Mini-MMM: `mmm/mini/full/voices/md/MMM_VOICE_STRATEGY_FULL_v4_1.md`.
- Purpose: preserve campaign logic: objective, sequence, priority, scarce resource, timing, decisive front, retreat condition, hold/advance/defer choice.
- Use when: the route can drift into local optimization or when multiple plausible moves compete.
- Must return: current strategy state, next priority, rejected path, retreat/hold condition, and how the answer should preserve broader context.
- Invalid if: it only says “be strategic” or restates the parent prompt without ordering moves.

`voice.systems`

- Mini-MMM: `mmm/mini/full/voices/md/MMM_VOICE_SYSTEMS_FULL_v4_1.md`.
- Purpose: detect feedback loops, couplings, delayed effects, systemic incentives, and second-order consequences.
- Use when: a local fix may create downstream instability or when parent/child/management routing can recursively affect output quality.
- Must return: system boundary, active feedback loop, coupling risk, second-order effect, and system-level guard.
- Invalid if: it names vague “complexity” without a concrete loop or coupling.

`voice.hume`

- Mini-MMM: `mmm/mini/full/voices/md/MMM_VOICE_HUME_FULL_v4_1.md`.
- Purpose: separate observation, inference, probability, habit, and uncertainty. Hume is the evidence-boundary voice.
- Use when: the route risks overclaiming, fake certainty, or treating receipt text as proof.
- Must return: what is observed, what is inferred, what remains unknown, confidence boundary, and next honest check.
- Invalid if: it moralizes uncertainty or hides behind generic caution.

`voice.feynman`

- Mini-MMM: `mmm/mini/full/voices/md/MMM_VOICE_FEYNMAN_FULL_v4_1.md`.
- Purpose: explain the mechanism simply enough that a testable observable falls out.
- Use when: the route needs a pass/fail check, causal mechanism, or concrete experiment.
- Must return: mechanism, observable, minimal test, expected pass signal, expected fail signal.
- Invalid if: it gives analogy without a test.

`voice.factory`

- Mini-MMM: `mmm/mini/full/voices/md/MMM_VOICE_FACTORY_FULL_v4_1.md`.
- Purpose: find bottleneck, queue, handoff, leverage, and operational next move.
- Use when: the route needs to become executable or when management/reroute pressure matters.
- Must return: bottleneck, current queue, next handoff, leverage move, stop/block condition.
- Invalid if: it produces management-sounding prose without changing the work queue.

`voice.orwell`

- Mini-MMM: `mmm/mini/full/voices/md/MMM_VOICE_ORWELL_FULL_v4_1.md`.
- Purpose: strip euphemism, ambiguity, inflated labels, and fake precision.
- Use when: output is verbose, log-shaped, or hiding weak claims behind system vocabulary.
- Must return: plain wording, removed ambiguity, renamed claim, sharper answer sentence, and any phrase that should be banned.
- Invalid if: it merely shortens without making the claim truer.

`voice.popper`

- Mini-MMM: `mmm/mini/full/voices/md/MMM_VOICE_POPPER_FULL_v4_1.md`.
- Purpose: propose falsifiers and classify the claim as killed, open, survived, or untested.
- Use when: a route needs a real failure condition before it can pass.
- Must return: target claim, falsifier, current status, test needed, and what would change the decision.
- Invalid if: it says “could be wrong” without naming a possible disproof.

`voice.pushback`

- Mini-MMM: `mmm/mini/full/voices/md/MMM_VOICE_PUSHBACK_FULL_v4_1.md`.
- Purpose: apply direct pressure to overreach, fake plurality, weak receipts, and hidden assumptions.
- Use when: the system is smoothing over an obvious failure or when the answer needs an adversarial correction.
- Must return: overclaim, correction, missing evidence, boundary, and forced fix.
- Invalid if: it becomes generic negativity or duplicates Popper without a correction.

`voice.zhuangzi`

- Mini-MMM: `mmm/mini/full/voices/md/MMM_VOICE_ZHUANGZI_FULL_v4_1.md`.
- Purpose: keep alternate readings alive until exclusion conditions are real; identify frame shifts and non-obvious interpretations.
- Use when: the prompt may be trapped in one frame or when a local answer may prematurely collapse possibilities.
- Must return: alternate live reading, exclusion condition, frame shift, what remains undecidable, and a non-collapsing next move.
- Invalid if: it becomes whimsical ambiguity with no exclusion condition.

### Skill Children

`skill.premortem`

- Skill doc: `skills/premortem/SKILL.md`.
- Purpose: run six-month-failed prospective hindsight and find novel failure reasons.
- Use when: Failure Council hardens a plan, route, packet, or strategy.
- Must return: user-named issues, novel failure reasons, positive `novel_findings_count`, deep dives, likely failure, dangerous failure, hidden assumption, early warnings, and revised plan.
- Boundary: no docs, no HTML, no transcript, no browser, no web UI.
- Invalid if: it only repeats the user’s complaints or creates report artifacts.

`skill.loophole_auditor`

- Skill doc: `skills/council-members/loophole-auditor/SKILL.md`.
- Purpose: run the confidence-loop audit until no known unresolved loophole remains under declared evidence standard.
- Use when: strategy can fail through hidden exceptions, receipt loopholes, or semantic drift.
- Must return: strategy under test, evidence standard, loopholes found, fixes applied, verification result, unresolved loopholes, confidence status, and stop condition.
- Invalid if: it claims confidence before applying fixes.

`skill.claude_pattern_intake`

- Skill doc: `skills/claude-pattern-intake/SKILL.md`.
- Purpose: mine Claude agents, skills, workflows, and outputs for useful Wizard/Codex mechanics without importing Claude authority.
- Use when: an external Claude lane produced workflow, agent, skill, audit, or sim/proof process material that may need to update Wizard.
- Must return: sources read, accepted patterns, rejected patterns, target surfaces, authority rejections, validation run, and remaining blockers.
- Invalid if: it copies Claude-only doctrine into Wizard or claims a Claude route ran without receipts.

`skill.source_math_lock`

- Skill doc: `skills/source-math-lock/SKILL.md`.
- Purpose: freeze source-doc formulas, tables, axes, and convention rules into an auditable artifact before downstream workers use them.
- Use when: terrain/operator words, Axis-6 UP/DOWN, atlas rows, proof assumptions, or workflow-stage formulas keep drifting.
- Must return: source paths, lock artifact, source hashes, row counts, recomputed checks, convention drift, and downstream rule.
- Invalid if: later workers re-derive rows instead of reading the lock artifact.

`skill.sim_audit_spine`

- Skill doc: `skills/sim-audit-spine/SKILL.md`.
- Purpose: preserve role separation and claim ceilings for sim, proof, result, workflow, and queue work.
- Use when: JAX/Julia parity, SMT proof, mechanical gates, or worker reports could be mistaken for admission.
- Must return: claim, state paths read, builder lane, mechanical gates, fabrication audit, SMT flip, accepted status label, blocked consumers, and next unblocked step.
- Invalid if: builder output, parity, or a green mechanical gate is treated as proof by itself.

`skill.collapse_auditor`

- Skill doc: `skills/council-members/collapse-auditor/SKILL.md`.
- Purpose: detect decorative plurality, shared-premise agreement, and correlated error across multiple routes.
- Use when: councils, voices, engines, Claude/Codex/Gemini workers, source locks, or workflow stages appear to converge.
- Must return: verdict, shared premise, correlated error risk, decorative split, dropped falsifiers, reruns required, and findings.
- Invalid if: CLEAN is reported without naming the shared premise tested.

### Lane Children

`lane.direct`

- Mini-MMM: `mmm/mini/full/lanes/md/MMM_LANE_DIRECT_FULL_v4_1.md`.
- Purpose: identify the most direct next action.
- Must return: action, payoff, precondition, owner, stop condition.

`lane.alternative`

- Mini-MMM: `mmm/mini/full/lanes/md/MMM_LANE_ALTERNATIVE_FULL_v4_1.md`.
- Purpose: preserve a plausible different path when the direct path may be brittle.
- Must return: alternate path, why it differs, when to use it, tradeoff, stop condition.

`lane.reframe`

- Mini-MMM: `mmm/mini/full/lanes/md/MMM_LANE_REFRAME_FULL_v4_1.md`.
- Purpose: replace the question when the current frame is wrong, too narrow, or hiding a false binary.
- Must return: old frame, new frame, hidden premise, changed decision, stop condition.

`lane.back`

- Mini-MMM: `mmm/mini/full/lanes/md/MMM_LANE_BACK_FULL_v4_1.md`.
- Purpose: retreat to prerequisite, rollback point, missing evidence, or earlier fork.
- Must return: what to step back to, why, what to recover, retry condition, stop condition.

`lane.wildcard`

- Mini-MMM: `mmm/mini/full/lanes/md/MMM_LANE_WILDCARD_FULL_v4_1.md`.
- Purpose: propose a high-upside non-obvious move without breaking boundaries.
- Must return: wildcard move, upside, risk, containment, use condition.

`lane.all_of_the_above`

- Mini-MMM: `mmm/mini/full/lanes/md/MMM_LANE_ALL_OF_THE_ABOVE_FULL_v4_1.md`.
- Purpose: bundle multiple lanes only when they are mutually reinforcing.
- Must return: ordered bundle, dependency order, why bundle beats single lane, stop condition.

### Guard Children

`guard.receipt_audit`

- Mini-MMM: `mmm/mini/full/checks_guards/md/MMM_CHECK_GUARD_AUDIT_FULL_v4_1.md`.
- Purpose: verify parent/child lineage, receipt fields, route truth, and missing evidence.
- Must return: passed receipts, missing receipts, fake plurality risk, blocked FULL reason, repair action.

`guard.receipt_divergence`

- Mini-MMM: sparse registry card `guard.receipt_divergence`.
- Purpose: check whether plural routes are structurally different or merely label-different.
- Must return: path-identical receipts, decorative split risk, convergent signal, healthy divergence, and rerun/block decision.

`guard.boundary_check`

- Mini-MMM: use audit/security/hygiene guard mini-MMM as appropriate.
- Purpose: enforce authority, scope, safety, no-doc/no-web boundaries, and overreach limits.
- Must return: boundary, violation or pass, consequence, required correction, stop condition.

### Compile-Gate Children

Compile-gate children are not voices. They each fill one required field in the compiled move:

- `compile_gate.target`: exact target of the move.
- `compile_gate.action`: concrete action to take.
- `compile_gate.owner`: owner/controller of the action.
- `compile_gate.success_check`: observable success condition.
- `compile_gate.stop_condition`: when to stop, block, or reroute.
- `compile_gate.artifact_surface`: where evidence/output lives.
- `compile_gate.status`: accepted, partial, blocked, killed, or deferred.

Each compile-gate child must return its field plus evidence boundary and output patch. A compile gate that only repeats status accounting is invalid.

## Embedded Task Card Schema

Parent task card fields:

- `packet_version`
- `run_id`
- `council_id`
- `parent_route_id`
- `parent_class: council_parent`
- `compact_mmm_path`
- `parent_mini_mmm`
- `task_context`
- `child_obligation`
- `liveness_deadline`
- `acceptance_gate`
- `output_contract`

Child task card fields:

- `packet_version`
- `run_id`
- `parent_route_id`
- `child_role_id`
- `child_instance_id`
- `job_type`
- `compact_mmm_path`
- `required_mini_mmms`
- `optional_mini_mmms`
- `source_language_overlay_path`
- `source_slice`
- `work_unit`
- `output_patch_target`
- `liveness_deadline`
- `acceptance_gate`

MMM budget:

- every child loads compact MMM;
- every child loads the required mini-MMM slices selected for its `job_type`;
- optional/random mini-MMM slices are allowed only after required functional slices are loaded;
- voice slices may be loaded outside voice-branded roles when their reasoning move is required by the job;
- source-language overlay is required for Codex Ratchet doctrine, source-doc, wiki-claim, and MMM-compression work;
- if the required bundle is too large for the runtime, split the child into narrower children or promote the work to a parent route; do not replace required slices with random simple voice categories.

## Embedded Receipt Schema

Parent receipt fields:

- `packet_version`
- `run_id`
- `council_id`
- `parent_route_id`
- `authority_level: parent`
- `parent_spawn_receipt`
- `mmm_load`
- `task_card`
- `child_obligation`
- `child_receipts`
- `route_conclusion`
- `distinct_delta`
- `evidence_boundary`
- `open_blockers`
- `status`

Child receipt fields:

- `packet_version`
- `run_id`
- `parent_route_id`
- `child_role_id`
- `authority_level: child`
- `child_launch_surface`
- `child_terminal_status`
- `job_type`
- `compact_mmm_loaded`
- `required_mini_mmms_loaded`
- `optional_mini_mmms_loaded`
- `source_language_overlay_loaded`
- `why_these_slices`
- `which_loaded_slice_changed_output`
- `missing_required_slice_if_any`
- `source_slice`
- `work_unit`
- `distinct_delta`
- `evidence_boundary`
- `output_patch`
- `status`

Management receipt fields:

- `manager_id`
- `authority_level: management_parent`
- `managed_scope`
- `child_status_table`
- `reroute_decisions`
- `intervention_verbs`
- `strategy_memory_delta`
- `full_claim_gate`
- `intervention_status`
- `status`

Allowed management intervention verbs:

- `kill`
- `demote`
- `reroute`
- `shrink`
- `override`
- `block_full`
- `accept_with_reason`
- `no_intervention_needed`

Premortem child fields:

```yaml
premortem:
  user_named_issues: []
  novel_failure_reasons: []
  novel_findings_count: 1
  deep_dives:
    - novelty: novel
      failure_story: ""
      hidden_assumption: ""
      early_warning_signs: []
      prevention: ""
```

Loophole child fields:

```yaml
loophole_audit:
  strategy_under_test: ""
  evidence_standard: ""
  loopholes_found: []
  fixes_applied: []
  verification_result: ""
  unresolved_loopholes: []
confidence_status: ""
stop_condition: ""
```

`unresolved_loopholes: []` is valid only after fixes are applied and verified under the declared evidence standard.

## Embedded Output Compiler Rules

Visible output is a human surface. Receipts are a controller surface.

Default shape:

```text
Wizard status:
[FULL/PARTIAL/BLOCKED credibility line. No process log.]

Decision Council:
Context + Strategy:
- prompt intent
- larger context
- strategy state to carry forward
- local-overoptimization risk

Decision:
[best move now and why]

Failure Council:
[novel risks, corrections, blockers, confidence status]

Compiled Answer:
[actual answer/work product]

Follow-Up Council:
[next-move selection logic; keep/merge/kill/rewrite rationale]

Follow-Up Options:
[1-3 copy-pasteable prompts/actions with payoff, use condition, stop/block condition]
```

Reject log-shaped output when:

- route proof is longer than task-specific judgment;
- receipt paths appear without a diagnostic request;
- Follow-Up Council wording duplicates Follow-Up Options;
- child counts appear as universal standards;
- the answer starts by proving orchestration instead of answering;
- every option has the same payoff;
- management details appear as a log rather than a meaningful risk or blocker.

Follow-Up Council edits the option set. Its allowed actions are `keep`, `merge`, `kill`, and `rewrite`. If it makes no material change, it stays internal or reports one concise line: `no material change`.

## Embedded External Audit Protocol

Premortem and Opus audit are separate steps.

External premortem:

- uses the real premortem skill method;
- sets the six-month-failed frame;
- spawns independent deep-dive agents when capacity exists;
- produces synthesis for fixes;
- in Wizard hardening loops, does not need to create visible docs or web UI unless explicitly requested for that run.

Opus audit:

- runs after premortem fixes;
- audits parent/child authority, child MMM proof, management intervention, no-log output, canonical packet shape, and skill boundaries;
- reads structured packet/compiler evidence;
- does not substitute for premortem.

Loop:

1. Run Wizard loop.
2. Run external premortem.
3. Apply fixes.
4. Run external Opus audit.
5. Apply fixes.
6. Run conformance and smoke.
7. Repeat until no blocker remains or a hard blocker is named.

## Embedded Codex Adapter Rules

Main Codex thread owns synthesis, repo edits, verification, and user-facing claims.

Codex parent subagents own parent routes.

Claude, Opus, Sonnet, and Haiku workers are child execution surfaces.

Direct Claude calls from the main thread are audit/advisory unless launched by a parent route.

Required parent proof:

- native Codex subagent id;
- parent route id;
- compact MMM and route mini-MMM loaded or blocked;
- child obligations;
- terminal parent status.

Required child proof:

- child launch surface;
- child role id;
- compact MMM loaded;
- mini-MMMs loaded;
- terminal child status;
- distinct delta.

Codex final answers should not expose receipt paths, process counts, or raw worker logs unless the user asks for diagnostics.
