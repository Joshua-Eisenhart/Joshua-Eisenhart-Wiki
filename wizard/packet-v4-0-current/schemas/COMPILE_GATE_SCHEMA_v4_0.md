---
title: Wizard v4.0 Compile Gate Schema
type: schema
packet: v4.0
framing: standalone
---

# Compile Gate Schema v4.0

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

The optional strict gate is invalid unless `classification` explicitly activates it.

Ordinary docs cleanup, bug triage, refactor planning, research synthesis, implementation handoff, product strategy, and decision support use only the universal gate unless an adapter says otherwise.
