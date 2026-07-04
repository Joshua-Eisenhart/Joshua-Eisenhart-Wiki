---
title: Entropy Sweep Protocol
created: 2026-04-07
updated: 2026-04-08
type: summary
framing: current
tags: [reference, research, validation]
sources:
  - raw/articles/new-docs/06_entropy_sweep_protocol.md
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Entropy Sweep Protocol — Base Constraints Upward

## Overview
Layer-by-layer protocol for testing which entropy family is actually admissible. Do not assume a single entropy functional for the whole stack. At each admissible layer, test the entropy family that the layer may force. Only promote a measure when the layer rejects the alternatives.

## Core Rule

Entropy is not primitive. Entropy is a later admissible measure on a constrained substrate. The correct quantity may differ by layer.

## Known Layer Placement

- Layer 17: signed/unsigned entropy objects become admissible
- Layer 18: Axis 0 kernel / preferred signed scalar on bridge output
- Layer 19: dynamics on entropy

Earlier layers must still be tested because they constrain which entropy family survives.

## Candidate Entropy Families

**Classical/scalar:** Shannon, von Neumann, Rényi, Tsallis, min-entropy, max-entropy, relative entropy.

**Bipartite/cut-state:** conditional entropy S(A|B), mutual information I(A:B), coherent information I_c(A>B), entanglement entropy/spectrum, logarithmic negativity, negativity.

**Geometry-sensitive:** shell-cut weighted entropy, bridge-weighted coherent information, history-window entropy, transport-weighted entropy, operator-ordered entropy.

## What to Test at Each Layer

For every candidate: (1) admissibility on current layer object, (2) sensitivity to layer's geometric constraint, (3) sensitivity to negative controls, (4) invariance under allowed symmetries, (5) survival under composition-order changes, (6) survival under chirality or bridge ablations.

## Current Evidence

- Shannon/purity shortcuts were killed in entropy-structure search
- von Neumann survived
- mutual information alone did not kill fake coupling
- concurrence/negativity were more discriminating than MI
- coherent information is leading signed cut quantity

## Layered Interpretation
Different layer depths test different properties: low layers test whether candidates make sense on the current object; mid layers test whether candidates distinguish geometry from fake geometry; bridge layers test whether candidates see real bipartite structure; entropy layers test which signed/unsigned quantity is forced; axis layers test which scalar survives dynamics. This connects to [[ladders-fences-admission-reference]] and [[constraint-on-distinguishability]]. (from 06_entropy_sweep_protocol.md)

## Critical Correction
Do not collapse entropy families into one universal metric. The stack forces different quantities at different stages: S(rho) for state entropy structure, S(A|B)/I_c for signed cut behavior, concurrence/negativity for [[entanglement-theory|entanglement witness]] behavior, mutual information for total correlation (but not as sole witness). Each family serves a distinct role in the [[constraint-surface-and-process|constraint surface]]. (from 06_entropy_sweep_protocol.md)

## Promotion Rule

A measure becomes primary only if it survives the relevant layer's geometry, bridge, and negative-control tests. Until then it remains a candidate family, not canon.

## How it connects
This protocol governs [[axis-and-entropy-reference]] and [[08-aligned-sim-backlog-and-build-order]]. See [[entropy-and-information-families]] for the comparison taxonomy.

## Open questions
- Whether geometry-sensitive entropy families should be tested before or after the standard bipartite families.
