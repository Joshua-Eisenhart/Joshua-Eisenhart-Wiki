---
title: Geomstats Manifold Geometry Reference
created: 2026-04-13
updated: 2026-05-18
type: concept
tags: [concept, research, tooling, geometry, mathematics]
sources:
  - raw/articles/new-docs/TOOLING_STATUS.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/ops/formal_scouts/results/clifford_sympy_geomstats_nested_g_structure_live_state_probe_results.json
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/ops/wizard_admission_receipts/sim_spinor_s3_hypersphere_angle_pi_over_479_geomstats_hidden_coordinate_gap_survivor_classes_admission_artifact.json
framing: current
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Geomstats Manifold Geometry Reference

## Overview
Geomstats is the manifold-geometry tool in the stack. It provides computational access to Riemannian metrics, geodesics, tangent spaces, hyperspheres, and manifold-side comparisons.

In this project, geomstats is not a generic geometry label. It is useful only when a probe needs an actual manifold operation: metric distance, tangent projection, geodesic/log-exp behavior, hypersphere coordinates, or a support-geometry crosscheck that cannot be honestly replaced by a graph or symbolic-only witness.

## Evidence boundary
This page is a tool-role reference, not a proof page.

Observed repo evidence:
- `clifford_sympy_geomstats_nested_g_structure_live_state_probe_results.json` reports `classification: formal_scout`, `all_pass: true`, `promotion_allowed: false`, and `geomstats: load_bearing` alongside load-bearing Clifford and SymPy roles.
- `sim_spinor_s3_hypersphere_angle_pi_over_479_geomstats_hidden_coordinate_gap_survivor_classes_admission_artifact.json` reports `classification: tool_lego_fit_probe`, `all_pass: true`, `promotion_allowed: false`, and `geomstats: load_bearing` with z3.

Safe claim: geomstats has existing artifacted load-bearing uses in formal-scout and tool-lego-fit contexts.

Unsafe claim: geomstats proves that the system runs on a particular manifold, closes a bridge, or promotes a geometry family to canon. Those require the current sim/result contracts and stage gates, not tool presence.

## Best-fit jobs in this stack
- shell metrics and support-geometry comparisons;
- hypersphere / S3 coordinate checks when spinor or Hopf-side probes need a manifold witness;
- geodesic, log/exp, distance, curvature, and tangent-space sanity checks;
- metric comparisons on curved state spaces;
- geometry-side crosschecks against symbolic tools such as [[sympy-symbolic-math-reference]], [[clifford-geometric-algebra-reference]], or falsifier tools such as [[smt-formal-falsifier-lane]].

## Bad-fit jobs
Geomstats should not be used to:
- replace full tensor, entanglement, chirality, or correlation structure with a reduced geometric toy;
- promote a support surface merely because a manifold class exists in the library;
- smooth graph, hypergraph, cell-complex, or persistence questions into ordinary manifold language;
- stand in for proof assistants, SMT falsifiers, or result-contract validation.

## What would count as a good geomstats receipt
A useful geomstats receipt should name:
1. the manifold or metric object being used;
2. the operation run, such as distance, geodesic, log/exp, projection, curvature, or tangent operation;
3. the observable compared;
4. the falsifier or negative control;
5. the claim ceiling: supportive, load-bearing tool-lego fit, formal scout, or stronger only if current process earned it.

Pass condition: the manifold operation distinguishes the intended branch, support, or coordinate relation under the active constraint without erasing the full-structure requirement.

Fail condition: the same result survives under a toy/reduced encoding, the negative control also passes, or the operation merely restates the chosen geometry without testing it.

## Current role in the tool program
Geomstats belongs in the tool-first stage as a carrier/support probe for manifold geometry. It pairs naturally with:
- [[clifford-geometric-algebra-reference]] for rotor, spin, bivector, and chirality checks;
- [[sympy-symbolic-math-reference]] for exact symbolic sanity checks;
- [[smt-formal-falsifier-lane]] for finite countermodels or branch exclusions;
- [[topology-carrier-tool-lane]] when the question shifts from smooth manifold geometry to persistence, hypergraph, cell, or carrier topology.

When a result uses geomstats, future wiki tranches should classify the use as `mentioned`, `imported`, `supportive`, `load_bearing`, or `blocked`. Mention count and import count are only routing signals.

## Why it matters here
The project has many claims about support, carrier geometry, nested torus/Hopf structure, and spinor-side admissibility. Geomstats helps test the manifold part of those claims without pretending that a named manifold is already the substrate.

Its strongest use is as a constraint witness: a concrete operation can show that one support relation survives, fails, or remains open under a specific metric/manifold probe.

## How it connects
- [[repo-tool-use-router]]
- [[tooling-status]]
- [[current-tool-status-installed-vs-missing-vs-not-wired]]
- [[tool-capability-sim-program]]
- [[sim-run-catalogue-and-result-family-router]]
- [[quantum-geometry-fubini-study]]
- [[geometry-ingredient-map]]
- [[clifford-geometric-algebra-reference]]
- [[sympy-symbolic-math-reference]]
- [[topology-carrier-tool-lane]]
- [[controller-prompt-rules]]

## Next bounded wiki work
A good next geomstats tranche would choose one result family, read the exact JSON result and sim file, and add a receipt-level row to a tool-function matrix or result-family page. Do not widen from geomstats into all manifold/topology tools in one pass.
