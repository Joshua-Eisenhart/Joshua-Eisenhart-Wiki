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
