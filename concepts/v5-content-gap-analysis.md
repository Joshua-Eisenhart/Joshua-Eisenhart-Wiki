---
title: V5 Content Gap Analysis
created: 2026-04-07
updated: 2026-05-21
type: summary
tags: [reference, research, audit]
sources:
  - raw/articles/new-docs/V5_CONTENT_GAP_ANALYSIS.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/V5_CONTENT_GAP_ANALYSIS.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/CURRENT_DOCS_MAP.md
spec_mirrors:
  - /Users/joshuaeisenhart/wiki/specs/codex-ratchet/process-contract-mirror-index.md
  - /Users/joshuaeisenhart/wiki/specs/codex-ratchet/lego-sim-contract-current.md
  - /Users/joshuaeisenhart/wiki/specs/codex-ratchet/sim-estate-integration-status.md
framing: historical_gap_snapshot
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# V5 Content Gap Analysis

## Overview
Date: 2026-04-05. What the v5 docs contain that the clean docs are MISSING. This is the integration guide for the next doc pass.

Status boundary: this is a dated gap/delta snapshot from 2026-04-05. Several gaps are now routed through newer concept pages or current spec mirrors. Do not use this page as live coverage truth without checking [[specs/codex-ratchet/process-contract-mirror-index|process-contract-mirror-index]], [[specs/codex-ratchet/lego-sim-contract-current|lego-sim-contract-current]], and [[specs/codex-ratchet/sim-estate-integration-status|sim-estate-integration-status]].

Current owner-surface routing should start from repo `system_v5/docs/CURRENT_DOCS_MAP.md`, not from this old gap list.

## Critical Missing Content

### 1. Four Base Operators -- Explicit Kraus Forms
Clean docs mention Ti/Te/Fi/Fe by name but lack: full Kraus form expansions (K0, K1, K2 matrices for each), trace-preserving checks, continuous-time generators (Lindbladian forms). Key claim: UP/DOWN is NOT additional operator math -- it only appears after a terrain map is chosen. Now covered in [[engine-math-reference]].

### 2. Full 16 Placements with Exact Tuples
Clean docs mention 16 placements loosely. V5 has: exact mathematical tuples for each, paired (spinor law, density law) per placement, set-theoretic hierarchy: 4 loops -> 8 terrain laws -> 16 placements. Structural lock notation.

### 3. Horizontal Condition A(gamma_out) = 0
Clean docs mention fiber/base loops. V5 source claims/derives that the horizontal condition on base loop is a geometric necessity; route this into current proof/receipt pages before treating it as current proof by this page. Inner loop keeps density constant (density-stationary). Outer loop changes density (density-traversing). Loops are density-constrained paths, not free spinor curves.

### 4. Loop Vector Fields
V5 defines Y_in and Y_out as explicit partial derivatives on spinors. How they relate to the Hopf connection. Now covered in [[engine-math-reference]].

### 5. Pre-Entropy Ladder (19 Layers)
Clean docs have 8 resolution levels. V5 has 19-layer explicit ladder from root constraints to entropy. Key claim: entropy is layer 17. Layers 1-16 are prerequisites. Now covered in [[ladders-fences-admission-reference]].

### 6. Weyl Chirality Algebra
V5 has: exact pseudoscalar treatment in Cl(3,0), sign flip as eigenvalue of e_123 on each sheet, joint state rho_AB in D(C^2 x C^2). Clean docs describe chirality loosely.

### 7. Composition Grammar with Terrain Assignments
V5 has: 8 terrains = 4 topologies x 2 loops, Type 1/Type 2 inversion, STAGE_OPERATOR_LUT, 16 placements = 4 topologies x 2 sheets x 2 loops.

## What This Analysis Found
The v5 docs have significant mathematical content (Kraus forms, loop vector fields, 16 placements, 19-layer ladder) that the clean docs flattened or omitted. Integration priority: engine math, loop geometry, pre-entropy ladder, chirality algebra.

## Related pages
- [[engine-math-reference]]
- [[ladders-fences-admission-reference]]
- [[constraint-on-distinguishability-full-math]]
- [[new-docs-manifest]]
