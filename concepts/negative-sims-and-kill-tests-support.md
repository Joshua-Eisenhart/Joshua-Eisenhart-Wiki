---
type: concept
created: 2026-05-18
updated: 2026-05-18
tags: [simulation, falsifier, negative-evidence, kill-tests, formal, basin]
sources:
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/READ ONLY Legacy core_docs/deep_research_results/DR_negative_sims_kill_tests.md
  - /tmp/attractor_holodeck_source_cluster_read_20260518.json
---

# Negative Sims and KILL Tests Support

## Purpose
This page processes the `DR_negative_sims_kill_tests.md` source into the current wiki.

Its kernel is central:

Negative sims are not failure noise. They are how the system draws the boundary of admissibility.

This supports the attractor-basin and anti-teleology work because basin edges are learned by what gets killed, blocked, or left open.

## Current-use boundary
Strongest use:
- process support for formal falsifiers, KILL conditions, negative controls, and basin-edge language.

Weak use:
- proof that any current negative sim has been freshly rerun.

Authority boundary:
- this is a source-derived support page. Current result status still belongs to repo artifacts and current rerun evidence.

## Core KILL families

### 1. Bounded Lie-algebra impossibilities
Negative sims should catch semantic mismatches where a model asserts impossible identity-bracket or unit-commutator behavior under boundedness constraints.

Useful wiki role:
- supports [[smt-formal-falsifier-lane]];
- supports noncommutation discipline;
- prevents algebraic wishful thinking.

### 2. Noncommutative limit swaps
Negative sims should catch illegal swapping of operations in noncommutative settings.

Useful wiki role:
- supports the noncommutation root constraint;
- supports “order matters” in sim and MMM language;
- connects to BCH/commutator discipline.

### 3. Entropy loss / free purification cheats
Negative sims should catch hidden entropy sinks, postselection accounting errors, and unital-mixing claims that falsely reduce entropy.

Useful wiki role:
- supports anti-teleology by blocking “future win” stories that smuggle in costless purification;
- supports thermodynamic path/flux language in [[empirical-math-rosetta]].

## Why negative sims matter for basins
A basin is not only where successful trajectories gather.

A basin also has edges:
- failed continuations;
- illegal swaps;
- impossible algebra;
- entropy cheats;
- KILL conditions;
- graveyard cases;
- open boundaries.

Without negative sims, the basin becomes a story center. With negative sims, it becomes a constrained region.

## Relation to row-level basin evidence
The row-level basin pages already preserve labels like:
- `anti_basin`
- `candidate_basin`
- `open_basin_boundary`
- `shallow_basin`
- `deep_basin`

Negative sims explain why `anti_basin` and `open_basin_boundary` are not second-class data. They are the shape of the constraint field.

## MMM sentences
- KILL is boundary evidence.
- Negative sims draw the basin edge.
- A failed continuation is still information about the attractor field.
- Noncommutation is not a warning label; it is a swap prohibition.
- Entropy cannot be spent twice.
- Postselection is not free purification.
- A graveyard is a map of exclusions.

## Research / tool lanes
- z3/cvc5: encode impossible claim shapes and return UNSAT/countermodels.
- sympy: expose algebraic identities and invalid simplifications.
- Clifford: check rotor/spin/chirality algebra under noncommutation.
- GUDHI/XGI/TopoNetX: map topology of killed/open/survived regions when data supports it.
- property-based testing: generate adversarial cases around KILL conditions.

## Related pages
- [[property-fuzz-metamorphic-testing-support]]
- [[mass-sim-generator-wide-exploration-support]]
- [[deep-research-source-cluster-status-2026-05-18]]
- [[smt-formal-falsifier-lane]]
- [[attractor-basin-result-surface-ledger]]
- [[attractor-basin-row-level-evidence-ledger]]
- [[attractor-basin-classifier-case-table]]
- [[anti-teleology-future-option-selection]]
- [[systems-philosophy-attractor-basin-inversion]]
- [[empirical-math-rosetta]]
