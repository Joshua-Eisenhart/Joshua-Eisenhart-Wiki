---
title: LLM Research Gap Matrix
created: 2026-04-10
updated: 2026-04-16
type: summary
tags: [reference, research, system, planning]
sources:
  - raw/articles/new-docs/LLM_RESEARCH_GAP_MATRIX.json
framing: current
---

# LLM Research Gap Matrix

## Overview
This page summarizes the machine-readable gap matrix used by the research-enforcement lane. It tracks mathematical families against the execution ladder and keeps the current state explicit: which cells are still GAP, which are PARTIAL, and which are DONE.

The matrix belongs with [[llm-controller-contract]] and [[enforcement-and-process-rules]]. It is the controller-side bookkeeping layer that prevents broad claims from outrunning the evidence.

Treat this as a support/reference snapshot surface, not as a front-door authority page by itself.

The repo-side companion reread for this snapshot is `system_v4/skills/llm_research_enforcement_validator.py`, which checks closeout schema fields, strong-claim gates, and matrix shape before a controller should accept the update.

Status-term alignment for the matrix/validator pair in this 2026-04-15 snapshot is:
- public/controller status spine: `exists`, `runs`, `passes local rerun`, `canonical by process`
- gap-matrix JSON vocabulary: the same four public terms plus `proof-backed`
- validator implementation snapshot: the same set as the gap matrix, but the run-level state is still spelled `runs locally`

That means the repo's public controller contract and one implementation surface are not perfectly vocabulary-aligned yet. For wiki/controller summaries, keep the public four-label spine primary and treat `proof-backed` / `runs locally` as closeout-schema or implementation-detail language unless the public controller docs are deliberately updated.
Those implementation-detail terms are freshness-sensitive and should stay snapshot-labeled when mirrored into summary pages.

## Execution ladder
The matrix uses five ordered classes:
- A_local
- B_pairwise_coupling
- C_multi_shell_coexistence
- D_topology_variant
- E_emergence

The point of the ladder is to keep the work moving from local objects to coupled objects and only then to emergence claims.

## Claim-tool map
The matrix also records which tool family should be load-bearing for each claim type:
- `z3` + `cvc5` for impossibility and forced-structure claims
- `geomstats` + `numpy` for shell metrics
- `XGI` + `rustworkx` for multi-way interaction
- `TopoNetX` + `GUDHI` for cell complexes and persistence
- `rustworkx` + topological sort for DAG ordering claims
- `clifford` + `numpy_roundtrip` for geometric algebra
- `PyTorch` + finite differences for gradient flow

That map is the enforcement version of "decorative tool use = fail."

## Families tracked
The initial matrix seeds seven families:
- density_matrices
- quantum_channels
- distinguishability_metrics
- information_geometry
- fiber_bundle_spin_geometry
- process_philosophy_support
- llm_controller_enforcement

Every family starts with all cells at GAP until there is a result file and a fresh rerun.

## Why it matters
This matrix is the bridge between the controller vocabulary and the actual sim ledger. It keeps `canonical by process` from being claimed too early and keeps emergence claims subordinate to the lower ladder classes.

For the current lego surfaces, see [[lego-build-catalog]] and [[actual-lego-registry]].

## Related pages
- [[llm-controller-contract]]
- [[enforcement-and-process-rules]]
- [[llm-research-enforcement-validator]]
- [[lego-build-catalog]]
- [[actual-lego-registry]]
- [[current-architecture-core]]
