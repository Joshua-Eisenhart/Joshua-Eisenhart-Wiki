---
title: Field Wide Compression Geometry
created: 2026-06-05
updated: 2026-06-05
type: concept
tags: [concept, axis0, compression, geometry, entropy, finite-witness, bookkeeping, jk-fuzz]
sources:
  - raw/owner-prompts/entropic-monism-axis0-fuzz-field-owner-prompts-2026-06-05.md
  - concepts/entropic-monism-axis0-field-compression-spine.md
  - concepts/jk-fuzz-field.md
  - projects/codex-ratchet/whole-physics-model-processing-ledger-2026-06-05.md
framing: current
claim_ceiling: finite bookkeeping proposal; no theorem, sim result, empirical admission, or final Axis0 geometry
---

# Field Wide Compression Geometry

## Claim ceiling

This page formalizes the owner phrase "compression that expands as it runs" as a finite bookkeeping model. It is proposal-level. It does not prove the physics model, close Axis0, admit gravity, or identify all readouts.

For formal/probe/falsifier work, use [[field-wide-compression-probe-contract]]. This page gives the conceptual finite bookkeeping object; the contract page says what a later packet must name before readouts, invariants, or kill conditions can become load-bearing.

## Owner-kernel line

The source correction:

> "it compresses acrosss its whole field and space."

> "the geometry and all its domain is like a big compression algorithm that ironically expands as it runs."

This page keeps that as a field-wide update rule, not a local-only mechanical rule.

## Finite bookkeeping object

At witness step `n`, define a finite field-bookkeeping state:

```text
B_n = (X_n, P_n, w_n, E_n, H_n, Q_n)
```

where:

```text
X_n   = finite support cells
        (sites, shell cells, cuts, graph/cell nodes, or history windows)

P_n(x) = finite admissible possibility set at support cell x

w_n(x,p) = finite weight / salience / compatibility score for p in P_n(x)

E_n   = finite relation data across support cells
        (adjacency, cut relation, shell order, history relation, constraint edge)

H_n   = finite history/provenance/graveyard bookkeeping

Q_n   = finite probe family available at this witness
```

Finitude is local to the witness: `X_n` and every `P_n(x)` are finite. The run may still expand support or refine possibilities at later witness steps.

## Whole-field compression operator

The compression/update operator acts on the whole represented field:

```text
C_n : B_n -> B_{n+1}
```

It is not merely:

```text
local_update(x) -> x'
```

Guide-safe reading:

```text
C_n reads the current finite support, its admissible possibilities, its
relations, its history, and its probes, then rebooks the whole field into the
next finite witness.
```

This preserves the owner's correction that the geometry compresses across its domain/space.

## How compression can expand

Compression does not have to mean fewer cells or fewer branches at each step. It can mean a lower-ambiguity bookkeeping state, even when resolution grows.

Allowed transitions:

| Transition | Meaning |
|---|---|
| Add support | `X_{n+1}` adds shell cells, cuts, graph/cell nodes, or history windows needed by the next witness. |
| Split support | one cell in `X_n` becomes several finer cells in `X_{n+1}`. |
| Merge support | several cells become one quotient/summary cell when probes cannot distinguish them. |
| Kill support | a support cell is removed or moved to graveyard bookkeeping when no admissible continuation survives. |
| Add possibilities | a new probe or refinement exposes admissible continuations not represented at `n`. |
| Split possibilities | one possibility becomes several distinguishable refinements. |
| Merge possibilities | possibilities become probe-equivalent under `Q_{n+1}`. |
| Kill possibilities | a possibility violates constraints, loses support, or fails a required probe. |

So `size(B_n)` need not decrease:

```text
|X_{n+1}| + sum_x |P_{n+1}(x)| may be greater than
|X_n|     + sum_x |P_n(x)|
```

The compression target is better finite bookkeeping of admissible continuation structure, not monotone shrinkage.

## Proposal-level equations

For each new support cell `y in X_{n+1}`, use a finite dependency neighborhood over the whole prior field:

```text
D_n(y) subseteq X_n
```

Then:

```text
P_{n+1}(y) =
  refine_merge_kill(
    {P_n(x) : x in D_n(y)},
    {E_n(x,x') : x,x' in D_n(y)},
    H_n,
    Q_n
  )
```

Weights update from whole-field compatibility:

```text
w_{n+1}(y,p') =
  normalize_y(
    compatibility(p', D_n(y), E_n, H_n, Q_n)
  )
```

This is intentionally schematic. Later formal work must choose exact carriers, relations, normalization, probe families, and invariants.

## Relation to JK fuzz

`JK fuzz` can be read as the finite admissible-continuation field inside `B_n`:

```text
F_jk(n,x) = P_n(x)
```

or, when a cut-state bridge is in scope:

```text
rho_AB(n,x,j,k) = candidate cut state for branch (j,k)
Xi_fuzz(n,x,h)  = sum_{j,k} w_n(x,j,k | h) rho_AB(n,x,j,k)
phi_0           = Phi_0(Xi_fuzz)
```

This keeps the order:

```text
finite field bookkeeping
  -> admissible-continuation field
  -> bridge/cut object
  -> Axis0/gravity/entropy readout candidate
```

## Probe readouts

Readouts are not automatically identical. They are probe outputs over finite objects:

| Probe/readout | Candidate reading |
|---|---|
| Entropy | bookkeeping of distinguishability, branch/path entropy, state entropy, graph/cell entropy, or cut entropy depending on object. |
| Time | ordering/refinement/entropy-increase readout on the support/history field. |
| Gravity | binding/synchronization/cut-consistency readout after a bridge object exists. |
| Dark energy | expansion/support-growth readout, especially where support grows or resolution expands. |
| Entanglement-information | finite cut/correlation readout, such as mutual information, coherent information, conditional entropy, or entanglement witness. |
| Chirality | orientation/order/asymmetry readout on support, carrier, or cut structure. |

Each readout must name its object:

```text
readout = Phi_R(B_n, named subobject, named probe family)
```

No scalar `entropy` or `information` admits the model by itself.

## Pass, fail, and kill conditions

Later formalization should require at least:

| Condition | Requirement |
|---|---|
| Finite witness pass | `X_n`, every `P_n(x)`, and the relation/probe data are finite at each witness. |
| Whole-field pass | `C_n` demonstrably uses cross-cell/domain data, not only isolated local state. |
| Expansion pass | at least one legal transition adds/splits support or possibilities while preserving finite witness discipline. |
| Compression pass | the update reduces ambiguity, contradiction, unsupported branches, or probe-equivalence clutter under explicit criteria. |
| Readout pass | entropy/time/gravity/dark-energy/entanglement/chirality readouts name their finite object and probe. |
| Variant pass | physics-first, politics-first, consciousness-first, and ToE-first readings can be represented without silent collapse. |
| Kill | infinite actual support at one witness, unbounded possibility set at one cell, local-only update smuggled as field-wide compression, readout without object/probe, or owner-doctrine asserted as empirical admission. |

See [[field-wide-compression-probe-contract]] for the stricter version of these requirements: finite witness slots, whole-field dependency controls, compression-vs-expansion measures, readout pass/fail conditions, variant preservation, candidate invariants, anti-invariants, and concrete falsifiers.

## Wizard/autoloop use

Use this page as the next bounded Wizard maintenance/wiki route when a worker needs to formalize the owner phrase without running sims:

```text
task: turn field-wide compression into finite bookkeeping
allowed: source reading, page patching, finite object definitions, pass/fail gates
blocked: sim runs, proof claims, empirical gravity admission, final Axis0 theorem
```

If the worker is moving from finite bookkeeping into formal packet shape, probe design, or falsifier routing, hand off to [[field-wide-compression-probe-contract]] instead of expanding this page into a proof or result surface.

## Related pages

- [[entropic-monism-axis0-field-compression-spine]]
- [[cross-field-toe-genealogy]]
- [[field-wide-compression-probe-contract]]
- [[jk-fuzz-field]]
- [[constraint-geometry-axis0-separation]]
- [[axis0-current-doctrine-state-card]]
- [[anti-teleology-future-option-selection]]
- [[systems-philosophy-attractor-basin-inversion]]
- [[basin-manifold-claim-contract]]
