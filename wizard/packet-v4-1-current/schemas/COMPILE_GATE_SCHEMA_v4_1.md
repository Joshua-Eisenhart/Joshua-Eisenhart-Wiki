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
