---
title: Wizard v4.0 Receipt Schema
type: schema
packet: v4.0
framing: standalone
---

# Receipt Schema v4.0

```yaml
receipt_id:
packet: v4.0
kind: parent | child | tool | adapter | source_lift | compile_gate
wave: decision | failure | follow_up | audit | none
member_id:
family:
runtime:
worker_id:
parent_receipt_id:
loaded_salience:
  full_mmm:
  mini_mmm:
task_card:
source_slice:
tool_surface:
terminal_status: completed | blocked | timed_out | rerouted | superseded | simulated | deferred
execution_evidence:
artifact_or_output:
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
  runtime:
  task_card:
  source_slice:
  operation_or_falsifier:
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

The five structural fields are required when a receipt participates in a plural council synthesis or receipt-divergence gate. They may be omitted for narrow tool, adapter, or source-lift receipts that are not used as council evidence.

`member_utility` is required for accepted parent member receipts in a visible full run. It records why this member was useful, how it affected the decision, how it relates to sim/QIT bounded evidence when relevant, and what theater it cut. This makes later tuning possible without pretending every member must remain mandatory forever.

`theater_cut` is a current-run judgment, not a permanent verdict on the member. A member that produced theater may be `cut_this_run`, `reboot_candidate`, or `suppress_this_context` depending on whether the problem was the member's value, the task card, the source slice, the model/runtime, or the initialization. `retire_candidate` should require repeated evidence across contexts, not one bad run.

If `current_disposition` is `reboot_candidate`, `reboot_note` must name the concrete delta for the next attempt: boot, task card, source slice, model/runtime, or mini-MMM variant. If `current_disposition` is `retire_candidate`, `retirement_evidence` must summarize repeated cross-context failure.

`variant_signature` is adapter-local and required only when a child/subsubagent is counted as a same-triple variant for sim/proof/QIT work. The invariant is the same exact claim, exact tool/function/API surface, and carrier/fixture; the variant signature records what changed in initialization, model/runtime, task card, source slice, or falsifier. Variants that differ only by label or wording are redundancy, not proof.

## Acceptance

A receipt is accepted only when:

- the assigned member/route is clear;
- required MMM or mini-MMM load is named;
- terminal status is explicit;
- evidence is usable;
- evidence boundary is honest.

Controller synthesis cannot create accepted receipts.
