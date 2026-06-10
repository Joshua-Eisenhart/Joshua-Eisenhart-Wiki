---
title: Ring Checkerboard Three Presentations and Sim Engine Runbook 2026-06-09
created: 2026-06-09
updated: 2026-06-09
type: project
status: source-routing and build-runbook
claim_ceiling: finite support / sim-design runbook only; no M(C) admission, no QIT-engine admission, no Axis0 closure, no physics claim
sources:
  - projects/codex-ratchet/pre-ai-rosetta-ring-checkerboard-provenance-2026-06-09.md
  - projects/codex-ratchet/two-engine-winlose-carnot-szilard-pattern-2026-06-09.md
  - projects/codex-ratchet/dual-carnot-szilard-qit-engine-witness-2026-06-09.md
  - projects/codex-ratchet/qit-axes-terrain-operator-fold-2026-06-09.md
  - concepts/constraint-manifold-architecture.md
  - concepts/ring-checkerboard-gradient.md
  - concepts/hopf-fibration-mathematics.md
  - concepts/hopf-foliation-structure.md
  - concepts/terrain-laws-and-loop-geometry.md
  - concepts/field-wide-compression-probe-contract.md
  - /Users/joshuaeisenhart/Codex-Ratchet/system_v6/receipts/mct_mine_adjudication_20260610.md
  - /Users/joshuaeisenhart/Codex-Ratchet/system_v6/receipts/mct_wiki_source_map_20260610.md
tags:
  - codex-ratchet
  - ring-checkerboard
  - hopf
  - axis0
  - manifold
  - sim-engines
  - numpy
  - julia
  - jax
  - pytorch
---

# Ring Checkerboard Three Presentations and Sim Engine Runbook 2026-06-09

## Purpose

This page records how the owner’s ring-checkerboard model should enter the current Codex Ratchet build.

The key correction:

```text
The ring-checkerboard is not just a picture.
It supplies the finite support model for the geometric constraint manifold build.
```

It prevents two bad defaults:

```text
bad default 1: M(C,t) = abstract labels like {0..7}
bad default 2: Hopf/Weyl geometry = smooth shell language with no finite owner-native discretization
```

The ring-checkerboard gives the finite middle:

```text
finite cells / rings / shells / loops
that can be sampled, probed, quotiented, warped, folded, and reindexed
```

Safe use:

```text
finite support and sim-design runbook
not final M(C)
not final Axis0
not final QIT-engine
not physics admission
```

## The three presentations

The owner model currently has three presentations. They may be equivalent presentations of one finite support object, but that equivalence must be checked rather than assumed.

### 1. Flat nested checkerboard

Shape:

```text
flat board
nested cells
2x2 -> 4x4 -> 8x8 -> ...
```

Role:

```text
finite combinatorial chart / local cell grid
```

What it contributes:

- finite cells;
- refinement levels;
- local adjacency;
- support-size accounting;
- compression/expansion by dropping or adding probes/resolution;
- a simple control surface for quotient and graph tests.

This is the most natural place for a **NumPy baseline/control**:

```text
NumPy = flat-checkerboard baseline/reference implementation
```

Ceiling: NumPy is useful for a baseline, fixture, and array truth table, but it is not the repo’s claim path for nonclassical/QIT claims.

### 2. Spherical / hyperspherical checkerboard

Shape:

```text
checkerboard curved into a sphere / hypersphere
nested shells
inside/outside inversion
surface closes around the observer
```

Role:

```text
curved shell / boundary / Axis0-gradient surface
```

What it contributes:

- shell index;
- radial or inside/outside gradient;
- boundary/interior relation;
- folding/warping behavior;
- event-horizon-like crossing intuition;
- surface support for Axis0 polarity.

This is the presentation that makes the owner’s Axis0-gradient intuition most visible.

### 3. Nested rings / torus loops

Shape:

```text
ring or coin
rings attached at discrete edge points
rings on rings
nested spinning rings
torus made of discrete ring loops
```

Role:

```text
Hopf-torus / fiber-loop / phase-loop decomposition
```

What it contributes:

- loop/fiber structure;
- toroidal coordinates;
- nested Hopf-shell correspondence;
- phase/fiber dynamics;
- shell-to-shell flux candidate;
- recursive ring-on-ring structure.

This presentation is the natural bridge into:

```text
psi_s(phi_i, chi_j; eta_k)
```

and into Hopf/Weyl carrier sampling.

## Candidate equivalence

The three presentations should be treated as candidate-equivalent charts/decompositions:

```text
flat checkerboard
  = local finite chart / combinatorial grid

spherical checkerboard
  = curved global surface / shell embedding

nested rings / tori
  = fiber-loop / Hopf-torus decomposition
```

Candidate equivalence statement:

```text
flat grid <-> spherical shell <-> nested torus/ring foliation
```

This is a build target, not a settled theorem.

A useful pass condition for future packets:

```text
The three presentations agree on finite support counts, quotient classes,
shell/eta gradient, phi-blindness under density probes, and relation/adjacency readouts.
```

Controls should break agreement where expected:

- erase shell nesting;
- flatten spherical shell to board;
- drop fiber coordinate;
- shuffle labels;
- erase adjacency/relation structure;
- compare density probes vs phase-sensitive probes.

## Axis0 gradient role

The owner’s current interpretation:

```text
the three ring-checkerboard presentations form the Axis0 gradient support
```

Safe mathematical reading:

```text
Axis0 is not one of the three models.
Axis0 is the polarity/gradient readout that becomes visible across the nested finite surfaces.
```

The natural coordinate is the shell/nesting coordinate:

```text
eta_k = shell / nesting level
```

The existing Hopf-taijitu anchor is:

```text
b0 = sign(cos(2 eta))
```

So Axis0 can be tested as a finite-surface gradient:

```text
inner shell <-> outer shell
inside <-> outside
compression <-> expansion
positive feedback <-> negative feedback
allostasis <-> homeostasis
```

This preserves the standing doctrine:

```text
Ne/Ni = positive feedback / allostasis
Se/Si = negative feedback / homeostasis
```

but does not close final Axis0.

## How this applies to M(C,t)

The M(C,t) geometric packet should not start from abstract labels.

Bad main support:

```text
S = {0,1,2,3,4,5,6,7}
```

Better main support:

```text
S = finite samples on nested ring-checkerboard / Hopf-shell support
```

Concrete state key:

```text
state = (sheet s, shell eta_k, board/ring coordinate phi_i, fiber/ring coordinate chi_j)
```

Spinor sample:

```math
\psi_s(\phi_i,\chi_j;\eta_k)
=
\begin{pmatrix}
e^{i(\phi_i+\chi_j)}\cos\eta_k \\
e^{i(\phi_i-\chi_j)}\sin\eta_k
\end{pmatrix},
\quad s\in\{L,R\}
```

Density row:

```math
\rho_s = \psi_s\psi_s^\dagger
```

Probe rows should be computed from this finite table, not asserted from labels.

## What each sim engine should do

Do not map the three ring-checkerboard presentations one-to-one onto Julia/JAX/PyTorch.

Bad mapping:

```text
flat checkerboard = Julia
spherical checkerboard = JAX
nested rings = PyTorch
```

Better mapping:

```text
three presentations = three models/charts of the same finite support
three engines = independent evidence backends that compute/check those presentations
```

### NumPy baseline / flat checkerboard control

NumPy is appropriate for the flat-checkerboard baseline because the flat model is mostly finite arrays and simple adjacency tables.

Natural NumPy jobs:

- generate flat nested grids;
- compute cell IDs and refinement levels;
- compute local adjacency arrays;
- compute finite probe rows and bins;
- compute quotient classes by row equality;
- provide simple expected values and regression fixtures.

Required ceiling:

```text
NumPy is baseline/control/supportive only.
No NumPy-only claim path for QIT, nonclassical geometry, or admitted M(C,t).
```

### Julia engine

Natural Julia jobs:

- canonical finite table generation where exactness matters;
- `QuantumOptics.jl` / channel or density evolution where used;
- `Graphs.jl` relation/warping/folding checks;
- symbolic/exact checks through Julia-side tooling where available;
- arbitration of table values against JAX/PyTorch results.

Julia should be able to compute the same finite support/probe/quotient values as NumPy, but through the declared Julia path.

### JAX engine

Natural JAX jobs:

- vectorized dense sampling of `psi_s(phi_i, chi_j; eta_k)`;
- density/Bloch row computation;
- batched probe expectations;
- differentiable or vectorized Axis0-gradient readouts;
- order-gap arrays for committed operator/terrain dynamics;
- cross-checking quotient classes and probe bins against Julia/PyTorch.

JAX is a strong fit for the spherical/Hopf shell presentation, but it should still compute the flat-grid and nested-ring invariants where feasible.

### PyTorch engine

Natural PyTorch jobs:

- tensor implementation of the finite spinor/density table;
- `torch_geometric` / graph relation readouts when relation dynamics are load-bearing;
- adjacency-sensitive warping/folding/reindexing controls;
- message-passing or graph-lift controls over ring/checkerboard relations;
- cross-checking probe-row and quotient data against Julia/JAX.

PyTorch is a strong fit for relation dynamics and graph/network readouts, but it should not be the only engine that sees the flat grid or ring relation.

## Cross-engine agreement target

The minimum useful cross-engine matrix:

| Object/readout | NumPy baseline | Julia | JAX | PyTorch |
|---|---|---|---|---|
| flat-grid cell count | yes | yes | yes | yes |
| nested shell index `eta_k` | fixture | yes | yes | yes |
| ring/fiber coordinate table | fixture | yes | yes | yes |
| spinor sample table | no claim path / optional complex array | yes | yes | yes |
| density rows `rho=psi psi†` | optional baseline | yes | yes | yes |
| probe rows / bins | yes | yes | yes | yes |
| quotient classes | yes | yes | yes | yes |
| phi-blindness under density probes | baseline expected values | yes | yes | yes |
| Axis0 `b0=sign(cos 2eta)` | yes | yes | yes | yes |
| operator/terrain dynamics | no claim path | yes | yes | yes |
| graph/relation ablation | yes baseline | yes | optional | yes |
| folding/reindexing invariants | yes baseline | yes | yes | yes |

Pass condition for this layer:

```text
Julia/JAX/PyTorch independently agree with the NumPy flat baseline where the baseline is valid,
and exceed it where nonclassical/QIT/channel geometry is required.
```

## What the M(C,t) card should require

A geometric M(C,t) build card should include these sections:

1. **Finite support construction**
   - choose shell count `K`, grid counts `N_phi`, `N_chi`, sheets `L/R`;
   - emit support table hash;
   - emit flat/spherical/ring presentation IDs.

2. **Three-presentation consistency**
   - flat-grid chart;
   - spherical-shell chart;
   - nested-ring/Hopf-torus chart;
   - compare support counts, adjacency, shell gradients, quotient classes.

3. **Probe rows**
   - finite probe/readout family;
   - optional implementation bins;
   - density probes vs phase-sensitive probes.

4. **Quotient computation**
   - compute `S/~_M` from probe rows;
   - show global-phi/fiber blindness emerges under density probes;
   - show phase-sensitive probes can separate when included.

5. **Axis0-gradient readout**
   - compute `eta_k`, `b0=sign(cos 2eta_k)`, and finite gradient/polarity rows;
   - compare to Ne/Ni positive and Se/Si negative feedback predictions only under explicitly named functionals.

6. **Committed dynamics**
   - apply existing operator/terrain forms;
   - measure order gaps and controls on the finite geometric support.

7. **Five manifold operations as measured behavior**
   - compression: probe/resolution drop merges quotient classes or increases ambiguity;
   - expansion: added probe/resolution splits classes;
   - warping: relation/adjacency/order changes;
   - folding: legal quotient/gluing with self-loop policy exposed;
   - reindexing: label/chart change preserving declared invariants.

8. **Controls**
   - abstract 8-state/4-state fixtures as side-controls only;
   - relation ablation;
   - shell nesting erasure;
   - phase/fiber coordinate erasure;
   - label shuffle;
   - flat/spherical/ring disagreement controls.

9. **Ceiling**
   - `scratch_diagnostic` or `formal_probe_plan` until admitted by later gates;
   - no final M(C), no QIT-engine admission, no Axis0 closure, no physics claim.

## Why NumPy-as-flat-baseline seems right

The owner suggestion:

```text
NumPy would be the more flat checkerboard.
```

This is a good fit if stated carefully.

Correct version:

```text
NumPy is the natural flat-checkerboard baseline/control engine because the flat presentation is finite arrays, grids, bins, and adjacency matrices.
```

Incorrect version:

```text
NumPy is one of the claim-path engines for the nonclassical geometry.
```

The repo-safe role is:

```text
NumPy baseline proves the finite array bookkeeping is not hiding errors.
Julia/JAX/PyTorch carry the declared three-engine evidence path for the geometric/QIT packet.
```

## Short form

```text
Ring-checkerboard adds the finite support model.

It has three candidate-equivalent presentations:
1. flat nested checkerboard = finite grid / NumPy baseline;
2. spherical checkerboard = shell / Axis0-gradient surface;
3. nested rings/tori = Hopf/fiber-loop decomposition.

The sim engines should not own one presentation each.
They should cross-check the same finite object through those presentations.

NumPy is appropriate as the flat-grid baseline/control, not as the nonclassical claim path.
```
