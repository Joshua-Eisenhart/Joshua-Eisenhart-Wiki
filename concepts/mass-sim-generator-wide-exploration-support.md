---
type: concept
created: 2026-05-18
updated: 2026-05-18
tags: [simulation, exploration, generator, evidence, systems, constraints]
sources:
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/READ ONLY Legacy core_docs/deep_research_results/DR_mass_sim_generator.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/READ ONLY Legacy core_docs/deep_research_results/DR_parallel_sim_evaluations.md
  - /tmp/attractor_holodeck_source_cluster_read_20260518.json
---

# Mass Sim Generator and Wide Exploration Support

## Purpose
This page processes the mass/parallel sim generator sources into the current wiki.

The useful kernel:

Wide exploration is not waste when strong constraints are doing real work. A mass sim generator can throw many bounded hypotheses at the constraint field, while KILL_IF checks and evidence ledgers keep the work finite and auditable.

## Current-use boundary
Strongest use:
- process support for wide exploration, bounded hypothesis specs, and evidence-ledger discipline.

Weak use:
- proof that any generated sim is currently valid, canonical, or rerun-backed.

Authority boundary:
- this is source-derived support. Current sim status still depends on repo contracts and rerun evidence.

## Owner kernel
The source cluster preserves several strong process ideas:

### 1. Separate hypothesis generation from code rendering
A mass sim generator should not free-write arbitrary code. It should move through an intermediate representation:
- hypothesis name;
- mathematical claim;
- tensor/shape expectations;
- backend/tool needs;
- invariants;
- negative controls;
- expected result artifact;
- KILL_IF conditions.

### 2. Evidence ledgers over prose claims
Each generated sim should emit structured results, not a narrative success note.

Needed fields:
- classification;
- evidence ledger;
- pass/kill tokens;
- measurement values;
- kill reasons;
- tool manifest;
- result JSON path.

### 3. Compatibility mode before parallel speed
Parallel execution is useful only if serial compatibility is preserved.

Safe pattern:
- run with `max_workers=1` to match sequential semantics;
- compare golden result artifacts;
- then widen parallelism;
- keep shared writes serialized.

### 4. KILL_IF checks as basin-edge exploration
Mass generation becomes aligned when every hypothesis has explicit kill boundaries.

That connects to [[negative-sims-and-kill-tests-support]] and [[systems-philosophy-attractor-basin-inversion]].

## Relation to anti-teleology
Mass sim generation supports anti-teleology because it keeps many futures live at once.

Instead of choosing one future/story and narrating backward, the system can:
- generate many bounded hypotheses;
- run them through the same constraint field;
- preserve pass/kill/open outcomes;
- infer basin structure from the distribution of survivors and failures.

MMM sentence:
- Wide sim generation is how possible futures are allowed to pressure the present without one future owning it.

## Good generator constraints
A generated sim should include:
- one bounded claim;
- one explicit support/carrier assumption;
- one positive witness target;
- at least one negative control;
- exact tool-role declaration;
- result JSON schema;
- stop/kill condition;
- no hidden side effects;
- deterministic seed when randomness appears.

## Overclaim fences
Do not say:
- mass generation proves the system;
- parallel execution improves truth;
- many sims imply a basin automatically;
- generated code is valid because it compiles;
- a PASS token promotes a claim without stage/gate context.

Safer language:
- generated candidate;
- bounded hypothesis packet;
- evidence-ledger row;
- KILL_IF boundary;
- compatibility-mode checked;
- parallel execution preserves serial semantics.

## Research lanes
- property-based testing and Hypothesis-style generation;
- fuzzing and metamorphic testing;
- quality diversity / novelty search;
- benchmark harness design;
- deterministic replay and provenance logging;
- parallel test execution with shared-state isolation;
- program synthesis with proof/contract checks.

## Related pages
- [[sim-run-catalogue-and-result-family-router]]
- [[multi-tool-constraint-manifold-packet-router]]
- [[hypothesis-z3-property-guard-router]]
- [[property-fuzz-metamorphic-testing-support]]
- [[deep-research-source-cluster-status-2026-05-18]]
- [[negative-sims-and-kill-tests-support]]
- [[systems-philosophy-attractor-basin-inversion]]
- [[anti-teleology-future-option-selection]]
- [[attractor-basin-classifier-case-table]]
- [[repo-tool-use-router]]
- [[sim-math-geometry-result-surface-router]]
