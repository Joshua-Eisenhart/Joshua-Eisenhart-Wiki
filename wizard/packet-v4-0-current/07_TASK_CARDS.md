---
title: Wizard v4.0 Task Cards
type: task_cards
packet: v4.0
framing: standalone
---

# Task Cards v4.0

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
must_not:
  - widen scope
  - synthesize council
  - load sibling member cards
  - claim parent or sibling routes ran
  - count itself
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
