---
title: Constraint Geometry Axis0 Separation
created: 2026-04-10
updated: 2026-04-10
type: concept
tags: [reference, system, constraints, geometry, research]
sources:
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v4/docs/CONSTRAINT_GEOMETRY_AXIS0_SEPARATION.md
framing: current
---

# Constraint Geometry Axis0 Separation

## Overview
Repo-current separation card for four layers that were getting mixed together: root constraints, geometry induced by those constraints, the allowed math that can live on that geometry, and `Axis 0` as a later slice on the constrained manifold.

## The build order
The live repo packet is explicit:
1. root constraints
2. admissible manifold `M(C)`
3. geometry induced on `M(C)`
4. axis slices on that constrained geometry

That means geometry is not `Axis 0`, and `Axis 0` is not the root constraint.

## Root constraints
- finitude / bounded distinguishability
- noncommuting, order-sensitive composition

These constrain what math is admissible before any later bridge or cut story is admitted.

## Why it matters
This packet is the repo’s antidote to premature Axis 0 closure. It protects the build order:
- constraints before geometry
- geometry before allowed operator families
- bridge/cut doctrine after those layers, not before

## Current wiki use
Use this page when a reader is starting to blur together the constraint charter, the geometry seat, and the later Axis 0 doctrine problem. It is a separation page, not a final-theorem page.

For the live queue/build-order rendering of the same separation, pair it with [[aligned-sim-backlog-and-build-order]] and [[sim-build-spine-and-wiki-maintenance]]. Those pages explain how the separation cashes out operationally as geometry-before-axis and lower-local-before-bridge scheduling discipline.

## Related pages
- [[aligned-sim-backlog-and-build-order]]
- [[sim-build-spine-and-wiki-maintenance]]
- [[axis0-current-doctrine-state-card]]
- [[current-authoritative-stack-index]]
- [[constraint-surface-and-process]]
- [[qit-engine-geometry-entropy-bridge]]
