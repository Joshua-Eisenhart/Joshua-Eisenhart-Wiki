# Finite Behavioral-Object Engine - 2026-07-10

Status: noncanonical wiki digest of a validated Ratchet capability fixture.

## Why It Was Built

The packet-112 tool audit showed that a `143/0/0` NumPy-dominated console
harness was not evidence of running Julia/JAX/PyTorch engines. The replacement
card froze distinct runtime roles before source construction and asked a
smaller question:

> Can finite probe-relative objects, quotient dynamics, exact attractors, and a
> topology-dependent learned proxy be computed with honest claim boundaries?

## Fixture

The carrier is every binary state on a periodic six-site ring: 64 states. Two
action generators are elementary cellular automata rules 30 and 110. The probe
family contains only Hamming weight and periodic domain-wall count, so no site
is privileged.

Two states are the same object at depth `d` only when their probe outcomes
match after every action history through depth `d`. Partition refinement is the
object factory; labels are not supplied in advance.

## Exact Result

Julia and JAX independently obtain:

```text
two-probe classes by depth: [11, 14, 14, 14, 14, 14, 14]
weight-only classes:         [ 7, 13, 14, 14, 14, 14, 14]
stable behavioral objects:  14
cyclic rotation orbits:      14
order-disagreeing states:    56 / 64
```

The stable behavioral partition exactly equals the independently computed
cyclic-rotation orbits. The raw 11-class quotient is not dynamically valid:
both actions split two of its classes, with 108 and 72 conflicting ordered
pairs. The stable 14-object quotient has well-defined induced transitions.

Attractors are exact cycles of finite functional graphs, not endpoint clusters:

```text
A after B: five attractors; basin sizes [3, 7, 18, 18, 18]
B after A: five attractors; basin sizes [3, 13, 16, 16, 16]
```

This is real order-sensitive work on one classical finite fixture. It is not a
result about the source QIT schedule.

## Runtime Roles

- Julia uses `Graphs.SimpleDiGraph`, `add_edge!`, and
  `strongly_connected_components` for the quotient graph/SCC receipt while
  owning exact partition and cycle semantics.
- JAX x64 uses `vmap`, `lax.fori_loop`, and `lax.scan` for all states, histories,
  probe ablations, relabelings, quotient conflicts, and functional-graph traces.
- PyTorch/PyG uses directed `MessagePassing`, graph pooling, deterministic
  optimization, and `torch.func.jacrev` for the learned graph fit.

All three result files reproduce byte-identically.

## Learned Result And Demotion

PyTorch fits all 14 orbit representatives and all 50 held-out rotations. Ring
edge erasure lowers accuracy from `1.00` to `0.44`, establishing dependence on
relational topology.

The stronger perception claim fails. The held-out rows are rotations of objects
already represented in training, and global graph pooling installs relabel
invariance. The accepted statement is therefore:

```text
topology-dependent orbit fitting on isomorphic presentations
```

not unseen-object generalization.

The shuffled-target control is selected to fail, and the transition mutation
deliberately crosses a quotient class. Both are detector sanity checks rather
than scientific selection evidence.

## Why The Packet Is Red

T9 required an executable engine-removal test. It was not run. Julia and JAX
overlap on the exact core; independent agreement is useful reproducibility but
does not prove distinct engine intelligence. Both exact lanes therefore emit
`all_pass:false` on T9 while preserving every exact local result.

The independent validator:

- passes artifact and cross-lane exact-core checks;
- independently reconstructs the finite fixture;
- rejects five in-memory result corruptions;
- reports `all_scientific_gates_pass:false`;
- accepts only `EXACT_CORE_PLUS_TOPOLOGY_DEPENDENT_FIT_ONLY`.

## Next Cards

1. Train on some behavioral objects and test genuinely unseen objects generated
   from a held-out rule family, not merely rotations.
2. Run an engine-removal matrix with tasks that only one role can discharge;
   role prose is insufficient.
3. Replace selected-to-fail mutation controls with preregistered random and
   structure-preserving perturbation families.
4. Apply the exact object instrument to an independently sourced QIT, reaction,
   or Lev transition system; do not define domain dynamics from the core map.

## Ceiling

This is a capability anchor for finite behavioral objects, quotient dynamics,
exact finite attractors, and topology-dependent fitting. It does not earn the
16-by-4 QIT schedule, unique stage personalities, four substages, general
perception, MMMs, ontologies, cross-domain unification, Axis0, physics, life, or
consciousness.

## Routes

- [[projects/codex-ratchet/claude-science-tool-truth-audit-2026-07-10]]
- [[concepts/cross-view-attractor-nominalism-ledger-2026-07-10]]
- [[concepts/quantum-channel-attractor-basin-perspectives-2026-07-10]]
- [[projects/codex-ratchet/engine-16x4-axis6-current-state-2026-07-09]]
