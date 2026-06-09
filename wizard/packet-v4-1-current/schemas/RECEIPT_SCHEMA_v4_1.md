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
