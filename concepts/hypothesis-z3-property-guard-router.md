---
type: concept
created: 2026-05-18
updated: 2026-05-18
tags: [hypothesis, z3, property-based, formal, testing, tooling]
sources:
  - /tmp/hypothesis_z3_property_guard_read_20260518.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_capability_hypothesis_isolated.py
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/probes/sim_integration_hypothesis_z3_property_guard.py
---

# Hypothesis + Z3 Property Guard Router

## Purpose
This page routes the live repo's Hypothesis + Z3 property-guard surfaces into the wiki.

The kernel:

Hypothesis supplies wide generated exploration. Z3 supplies formal exclusion. Together they are a concrete implementation of “wide exploration under strong constraints.”

## Source surfaces
Read artifact:
- `/tmp/hypothesis_z3_property_guard_read_20260518.json`

Repo files:
- `system_v4/probes/sim_capability_hypothesis_isolated.py`
- `system_v4/probes/sim_integration_hypothesis_z3_property_guard.py`

## Two-stage tool ladder

### 1. Hypothesis isolated capability
`sim_capability_hypothesis_isolated.py` is a classical baseline capability probe.

It tests that Hypothesis can:
- generate 100 cases for a simple invariant;
- confirm `reverse(reverse(xs)) == xs`;
- find a counterexample when the invariant is intentionally broken.

Boundary:
- this proves capability of the property-testing tool surface only;
- it is not a nonclassical witness;
- it is not integration with Z3.

### 2. Hypothesis + Z3 integration
`sim_integration_hypothesis_z3_property_guard.py` couples generated search with SMT admissibility.

Domain:
- 2-outcome probe states `(p0, p1)`;
- bounded probabilities;
- normalization;
- distinguishability from uniform.

Protocol:
- Hypothesis generates candidate states;
- Z3 checks admissibility constraints;
- Python-level checks assert admitted states satisfy the axioms;
- deliberately invalid uniform state is excluded by Z3;
- boundary cases near 0/1 are included.

Boundary:
- both tools are load-bearing for this integration;
- Hypothesis without Z3 lacks formal exclusion;
- Z3 without Hypothesis only checks hand-picked cases.

## Why this matters for the whole wiki
This is one of the clearest concrete examples of the broader system rule:

- wide exploration is necessary;
- strong constraints do the selection;
- counterexamples define boundaries;
- generated cases do not replace proof;
- formal proof over hand-picked cases does not replace exploration.

It belongs near:
- [[property-fuzz-metamorphic-testing-support]]
- [[smt-formal-falsifier-lane]]
- [[mass-sim-generator-wide-exploration-support]]
- [[negative-sims-and-kill-tests-support]]
- [[anti-teleology-future-option-selection]]

## MMM sentences
- Hypothesis widens the search; Z3 sharpens the exclusion.
- Generated cases are trajectories through the constraint field.
- A counterexample is useful because it compresses the boundary.
- Z3 without generated pressure sees only the examples we remembered to ask.
- Property testing without formal exclusion finds surprises but not admissibility.

## Stop conditions
Do not use this router to claim:
- Hypothesis proves the math;
- Z3 proves the whole theory;
- the 2-outcome probe state domain covers the full system;
- capability probe equals integration proof;
- integration proof equals canonical by process.


## Result-status routing fence
This router separates capability, source/probe design, and current result-backed claims. Hypothesis plus Z3 is a strong pattern for wide generation under formal exclusion, but source text alone does not prove current pass/canonical status. A stronger claim needs a current result artifact or rerun that records classification, tool manifest, tool integration depth, and the exact excluded/admitted cases.

## Related pages
- [[multi-tool-constraint-manifold-packet-router]]
- [[property-fuzz-metamorphic-testing-support]]
- [[smt-formal-falsifier-lane]]
- [[mass-sim-generator-wide-exploration-support]]
- [[negative-sims-and-kill-tests-support]]
- [[repo-tool-use-router]]
- [[anti-teleology-future-option-selection]]
