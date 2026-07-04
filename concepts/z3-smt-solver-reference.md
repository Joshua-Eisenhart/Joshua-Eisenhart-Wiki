---
title: Z3 SMT Solver Reference
created: 2026-04-13
updated: 2026-04-13
type: concept
tags: [concept, research, formal, tooling, proof, constraints, mathematics]
sources:
  - raw/articles/new-docs/TOOLING_STATUS.md
  - raw/articles/new-docs/references/FORMAL_METHODS_AND_WITNESS_DISCIPLINE_REFERENCE.md
framing: current
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Z3 SMT Solver Reference

## Overview
Z3 is the main impossibility / satisfiability proof tool in the stack. Its strongest role is not generic theorem proving but bounded constraint discharge:
- prove a configuration is impossible via `UNSAT`
- produce satisfying witnesses via `SAT`
- enforce finite admissibility and fence conditions

## Why it matters here
The project's constraint-first method needs explicit witnesses for exclusion, not only positive construction. Z3 is one of the cleanest tools for that.

## Best-fit jobs in this stack
- impossibility proofs
- admissibility gates
- fence enforcement
- noncommutation/order-sensitive structural checks
- proving that a proposed configuration cannot survive a required condition

## Why UNSAT is special here
The current project language repeatedly treats `UNSAT` as the strongest proof form for exclusion. That makes Z3 more than a convenience tool: it is one of the main ways the graveyard becomes rigorous.

## Limits
Z3 does not replace:
- geometric sims
- numerical carrier experiments
- symbolic derivation layers

It is strongest when the question can be turned into a finite logical constraint problem.

## How it connects
- [[formal-methods-and-witness-discipline]]
- [[formal-methods-witness-discipline-reference]]
- [[tooling-status]]
- [[controller-prompt-rules]]
- [[llm-research-gap-matrix]]
