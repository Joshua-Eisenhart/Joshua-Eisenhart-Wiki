---
type: concept
created: 2026-05-18
updated: 2026-05-18
tags: [formal, tooling, smt, z3, cvc5, proof, falsifier]
sources:
  - /tmp/wiki_smt_formal_methods_scan_20260518.json
---

# SMT Formal Falsifier Lane

## Purpose
This page routes the Z3/CVC5 side of the repo into the wiki's tool-use and MMM harness.

The central rule is simple:

SMT is strongest as a bounded falsifier and witness surface. It should kill inadmissible claims, cross-check finite encodings, and return countermodels or UNSAT surfaces. It should not be allowed to promote a simplified encoding into whole-system proof.

## Current repo signal
A 2026-05-18 scan found heavy repo use of Z3/CVC5/SMT language and many concrete CVC5/Z3 probe files. The top file families include:

- `system_v4/probes/sim_cvc5_effect_subtyping_constraint.py` — scan score 542
- `system_v4/probes/sim_cvc5_shells_crosscheck.py` — scan score 494
- `system_v4/probes/sim_cvc5_clifford_rotor_constraint.py` — scan score 471
- `system_v4/probes/sim_cvc5_mi_subadditivity_constraint.py` — scan score 451
- `system_v4/probes/sim_cvc5_colimit_cocone_pushout_constraint.py` — scan score 449
- `system_v4/probes/sim_gap_fully_extended_tqft_symmetric_monoidal_constraint_canonical.py` — scan score 438
- `system_v4/probes/sim_gap_cobordism_hypothesis_dualizable_constraint_canonical.py` — scan score 437
- `system_v4/probes/sim_cvc5_limit_universal_cone_constraint.py` — scan score 436
- `system_v4/probes/sim_cvc5_arrow_calculus_constraint.py` — scan score 433
- `system_v4/probes/sim_cvc5_hopf_fiber_constraint.py` — scan score 430
- `system_v4/probes/sim_cvc5_symplectic_preservation.py` — scan score 428
- `system_v4/probes/sim_cvc5_institution_satisfaction_constraint.py` — scan score 425
- `system_v4/probes/sim_cvc5_hodge_decomposition_constraint.py` — scan score 418
- `system_v4/probes/sim_cvc5_gradual_typing_consistency_constraint.py` — scan score 406
- `system_v4/probes/sim_cvc5_algebraic_effect_handler_constraint.py` — scan score 404
- `system_v4/probes/sim_cvc5_ads_cft_central_charge_constraint.py` — scan score 404
- `system_v4/probes/sim_cvc5_mirror_symmetry_constraint.py` — scan score 401
- `system_v4/probes/sim_cvc5_markov_chain_constraint.py` — scan score 398
- `system_v4/probes/sim_integration_cvc5_z3_unsat_agreement_micro.py` — scan score 396
- `system_v4/probes/sim_cvc5_subtyping_constraint.py` — scan score 393


Scan artifact:
- `/tmp/wiki_smt_formal_methods_scan_20260518.json`

These are routing signals only. A file appearing here proves neither fresh rerun nor canonical status.

## Admissible SMT roles

### 1. Falsifier
Use Z3/CVC5 to show that a proposed claim cannot satisfy the encoded constraints.

Good output:
- `unsat` for a prohibited claim shape;
- unsat core where available;
- exact encoded assumptions;
- which wiki/repo rule the encoding represents.

Bad output:
- “Z3 proved the theory.”

### 2. Countermodel / witness
Use `sat` to produce a concrete model that exposes an allowed or problematic configuration.

Good output:
- model values;
- bounded domain;
- why this model matters to the claim;
- which stronger claim it prevents.

Bad output:
- treating one satisfying model as general proof.

### 3. Cross-solver agreement
Use CVC5 to cross-check Z3 on a bounded encoding, or vice versa.

Good output:
- same bounded claims;
- same verdicts;
- model/UNSAT comparison;
- named disagreement path if any.

Bad output:
- vague “two solvers agree” without exact shared encoding.

### 4. SyGuS / synthesis pressure
Use CVC5 where a boundary expression or candidate invariant needs synthesis, not just checking.

Good output:
- grammar;
- synthesized expression;
- constraints satisfied;
- rejected alternatives.

Bad output:
- importing CVC5 but not using synthesis or solver pressure.

## Relationship to harness/MMM work
SMT gives the MMM harness a machine-checkable refusal layer.

Useful MMM nouns:
- satisfiable, unsatisfiable, model, countermodel, witness, certificate, unsat core, obligation, invariant, refinement, solver, theory, bounded domain, encoding, cross-check, disagreement, synthesis grammar.

Useful MMM sentences:
- SAT shows a model survived this encoding; it does not close the theory.
- UNSAT kills the encoded claim under the named constraints.
- The proof is only as honest as the reduction from prose to record.
- A countermodel is not noise; it names the boundary the prose missed.
- Cross-solver agreement is stronger than one solver, but weaker than a full support proof.

## Required status discipline
When reporting SMT evidence, use the weakest honest label:

- `exists`: file/artifact exists.
- `runs`: command completed.
- `passes local rerun`: current session reran and checked the expected result.
- `canonical by process`: current repo process admits the result under the relevant contract.

Do not upgrade status because the output sounds formal.

## Related pages
- [[hypothesis-z3-property-guard-router]]
- [[property-fuzz-metamorphic-testing-support]]
- [[negative-sims-and-kill-tests-support]]
- [[repo-tool-use-router]]
- [[tooling-status]]
- [[current-formal-methods-core]]
- [[formal-methods-and-witness-discipline-reference]]
- [[cvc5-smt-and-sygus-reference]]
- [[z3-smt-solver-reference]]
- [[mmm-formal-noun-and-great-sentence-reservoir]]
- [[llm-controller-contract]]
- [[enforcement-and-process-rules]]
