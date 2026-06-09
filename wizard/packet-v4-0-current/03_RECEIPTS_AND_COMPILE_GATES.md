---
title: Wizard v4.0 Receipts and Compile Gates
type: receipt_and_gate_contract
packet: v4.0
framing: standalone
---

# Receipts And Compile Gates v4.0

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

The goal is not to keep every member forever. The goal is to measure which voices, hats, failure lenses, expert lenses, lanes, compositions, and guards changed the work. A member can later be tuned down only from this evidence, not from controller taste.

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

Structural fields must be meaningful, not merely present. Missing keys, `null`, empty strings, empty lists, empty maps, or wrong-shape values block synthesis as missing structural evidence.

Do not use prose similarity, word overlap, embeddings, tone, or route labels as proof of divergence.

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
