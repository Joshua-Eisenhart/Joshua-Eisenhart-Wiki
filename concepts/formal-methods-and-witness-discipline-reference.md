---
title: Formal Methods And Witness Discipline Reference
created: 2026-04-07
updated: 2026-04-08
type: summary
tags: [reference, research, validation]
sources:
  - raw/articles/new-docs/references/FORMAL_METHODS_AND_WITNESS_DISCIPLINE_REFERENCE.md
framing: legacy
priming: false
---

# Formal Methods And Witness Discipline Reference

## Overview
Reference doc covering model checking, SAT/SMT solving, proof-carrying code, CEGAR, bisimulation, trace theory, refinement, invariant checking, and fail-closed design. The actual formal frameworks, not the system's application.

## Model Checking (Clarke, Emerson, Sifakis — 2007 Turing Award)

Algorithmic method: given finite-state model M and temporal logic formula φ, determine whether M ⊨ φ. Exhaustively enumerates ALL reachable states. A passed model check is a PROOF, not a sample — differs from testing which checks some executions. CTL (branching-time): path quantifiers (A=all, E=some) + temporal operators (G=always, F=eventually, X=next, U=until). LTL (linear-time): operators over individual traces, PSPACE-complete. Tradeoff: state explosion grows exponentially with concurrent components.

## SAT/SMT Solving

SAT: given Boolean formula φ, does a satisfying assignment exist? Canonical NP-complete (Cook-Levin 1971). SMT generalizes to first-order formulas over background theories — linear arithmetic, arrays, bit vectors. Key solvers: Z3 (Microsoft Research), CVC5 (Stanford/Iowa). The fundamental asymmetry: FINDING may be hard (NP), CHECKING is cheap (P). SAT result → satisfying assignment (witness), checkable in O(|φ|). UNSAT result → proof of unsatisfiability (DRAT format), checkable by verified tools.

## Proof-Carrying Code (Necula & Lee, 1996-97)

Untrusted code arrives with machine-checkable proof that it satisfies a safety policy. Architecture: code producer (untrusted) generates code + proof. Code consumer (trusted) runs proof checker — small, trusted, fast. The proof IS the witness. Checking is polynomial. No trust in network, compiler, or producer required — only checker and policy must be trusted. Foundational PCC (Appel, Princeton): checker trusts only machine semantics and logic, not even the type system.

## CEGAR (Counterexample-Guided Abstraction Refinement)

Clarke et al. (2000/2003). Loop: (1) Abstract — construct overapproximating finite model. (2) Model-check — verify property. If satisfied, done. (3) Analyze counterexample — check if real (concrete trace exists) or spurious (no concrete counterpart). (4) Refine — if spurious, split abstract states to eliminate this trace. Key: only refine where needed. The counterexample tells you exactly which part of the abstraction is too coarse.

## Witness / Certificate in Formal Verification

A witness is evidence that a property holds or fails: satisfying assignment (witnesses satisfiability), UNSAT certificate / DRAT proof (witnesses unsatisfiability), counterexample trace (witnesses safety violation), inductive invariant (witnesses safety — predicate I such that Init ⟹ I, I ∧ T ⟹ I', I ⟹ Safe). The fundamental asymmetry: finding witnesses may be NP-hard, PSPACE-hard, or undecidable. CHECKING witnesses is polynomial. This is the entire basis of NP: hard to find, easy to verify.

## Bisimulation

Given labeled transition system (S, Act, →), relation R is a bisimulation if whenever (p,q) ∈ R: every p --a→ p' has matching q --a→ q' with (p',q') ∈ R, and vice versa. Bisimilarity (~) is the largest bisimulation. No external observer can distinguish bisimilar systems by any sequence of interactions. Strictly stronger than trace equivalence. Connection to operational equivalence: bisimilarity formalizes "indistinguishable under all possible interaction sequences."

## Trace Theory / Labeled Transition Systems

LTS: (S, Act, →) — states, actions, transition relation. Trace: finite sequence of actions recording only observable actions. Trace equivalence: traces(p) = traces(q). Bisimulation ⟹ trace equivalence (but not reverse). For deterministic systems they coincide. Order matters: traces are ordered sequences. Different orderings → different traces → trace-inequivalent systems. Directly connects to N01 (order-sensitive composition).

## Refinement

System A refines system B (A ≤ B) if A satisfies all properties B satisfies. In CSP (Hoare): traces refinement (safety properties), failures refinement (deadlock freedom, liveness). Lattice structure: specifications ordered by refinement form a lattice. Refinement is compositional: if A refines B, then C[A] refines C[B] for any context C. Modular verification.

## Invariant Checking

Inductive invariant: (1) Initiation: Init(s) ⟹ I(s). (2) Consecution: I(s) ∧ T(s,s') ⟹ I(s'). (3) Safety: I(s) ⟹ Safe(s). Mirrors mathematical induction. Connection to viability: viability kernel = set where system CAN stay (existential — at least one path stays). Inductive invariant = set where system MUST stay (universal — all paths stay). Viability is existential, invariance is universal. Finding inductive invariants is undecidable in general; practical methods: abstract interpretation, IC3/PDR, k-induction.

## Fail-Closed / Fail-Safe Design

Fail-safe: upon failure, defaults to state that does not endanger. Fail-closed (fail-secure): default on failure is DENY, REJECT, CLOSE, HALT. Formal property: for all failure states f ∈ F, Safe(f) holds. Connection to formal verification: fail-closed is the operational analog of UNSAT-as-default. Cannot prove property holds → reject. System requires evidence of safety (witness/certificate), not assumption of safety.

## Fit for this wiki
Best fit:
- gate claims that should not be promoted without a witness
- keep admission rules fail-closed when evidence is missing
- treat counterexamples as load-bearing rather than embarrassing noise

Mismatch:
- it does not by itself specify the system's domain math
- it is a control discipline, not a substitute for the carrier/probe geometry
- a passing checker means the witness is acceptable, not that the broader theory is complete

## How it connects
This reference grounds [[constraint-surface-and-process]] (finite witness discipline, fail-closed admission) and [[system-architecture-reference]] (admissibility fences). See [[distinguishability-formal-reference]] for the formal spine connecting witness to indistinguishability.

## Related pages
- [[constraint-surface-and-process]]
- [[system-architecture-reference]]
- [[distinguishability-formal-reference]]
- [[nominalism-in-this-system]]
- [[current-research-overlays]]
- [[llm-controller-contract]]
