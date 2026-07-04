---
title: Formal Methods Witness Discipline Reference
created: 2026-04-07
updated: 2026-04-08
type: summary
tags: [reference, research, formal, validation]
sources:
  - raw/articles/new-docs/archive_hermes_overlaps/FORMAL_METHODS_WITNESS_DISCIPLINE_REFERENCE.md
framing: legacy
priming: false
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Formal Methods / Witness Discipline Reference

## Overview
External formal-methods support for the system's admissibility grammar. Does not supply ontology -- supplies disciplined acceptance/rejection machinery.

## Exact Fit Terms

### Model Checking
Checks whether a transition system satisfies a property. Produces counterexamples when a property fails. Good fit for [[ladders-fences-admission-reference|fail-closed admission]]: if property is violated, reject. Counterexamples are finite artifacts.

### Theorem Proving
Proves statements from axioms and inference rules. Good for admissibility when a claim must be justified before acceptance. Best when proof object is machine-checkable.

### Proof-Carrying Code
Code is accepted only when accompanied by a valid proof/certificate. Best exact fit for fail-closed checking. No certificate = no admission.

### Invariant Checking
Verifies that an invariant holds over a system. Good for surface-style constraints: if state leaves the admissible surface, reject.

### Hoare Logic
Pairs preconditions and postconditions with proofs about programs. Good for admissibility as a proof obligation.

### Separation Logic
Strong fit for resource, ownership, and heap-structured invariants. Relevant if admissibility rules concern resource accounting.

### CEGAR
Abstract, check, then refine if counterexample is spurious. Good for iterative witness validation. Important: a candidate counterexample is not automatically a true witness.

## System Translation
- admissibility gate -> proof obligation / acceptance condition
- witness -> proof object or counterexample trace
- graveyard -> rejected counterexamples / invalid certificates archive
- fail-closed -> reject on missing or invalid proof/certificate
- finite witness discipline -> finite counterexample, finite proof object

## Mismatch Notes
"KILLED/SURVIVED" is not standard formal-methods terminology. Use accepted/rejected, verified/refuted. "Graveyard" is not standard -- use rejected witness archive or counterexample log.

## Best Support Cluster
1. proof-carrying code
2. model checking
3. invariant checking
4. theorem proving
5. CEGAR as the workflow around them

## Related pages
- [[ladders-fences-admission-reference]]
- [[current-formal-methods-core]]
- [[constraint-on-distinguishability-formal-reference]]
