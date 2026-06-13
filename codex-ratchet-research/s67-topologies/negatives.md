# S6/S7 Topologies - Negatives

Status: wave-2 populated research register.

Scope: what graph/cell-complex/lattice locality results forbid, plus alias traps
and designed-fail controls.

## Results Do Not Permit These Claims

- Local graph isomorphism does not imply global topology identity. Two support
  graphs can have identical radius-`r` neighborhoods and still differ in cycle
  structure, twist, orientability, quotient action, or cover data.
- Equal node count, equal edge count, equal degree multiset, and equal orbit
  sizes do not imply a valid quotient/lens/Mobius/Klein alias.
- A `2:1` cover count is not a Mobius strip, spin double cover, or lens descent
  unless the projection, action, and preserved structure are named.
- A finite graph is not automatically a manifold. A cell complex needs explicit
  incidence; a manifold-like claim needs local link conditions or an explicit
  triangulated/simplicial surface model.
- Digital topology is not just graph adjacency. Khalimsky/Alexandroff-style
  digital spaces show that different finite topologies can sit over the same
  integer lattice; adjacency-only probes cannot silently import continuous
  manifold results.
- Lieb-Robinson locality does not classify support topology. It bounds
  propagation/correlation behavior for local dynamics; it does not prove that two
  graphs with the same boundary-cost profile are the same topology.
- Area-law language does not imply holography, manifold boundary duality, or
  topology identity. In this register it only supports boundary-size/locality
  cost context for finite probes.

## Designed-Fail Controls

- Same cover cardinality without descent: construct two `2:1` covers over the
  same base graph where one projection preserves adjacency/incidence and the
  other breaks it. Expected result: cover-count-only alias fails.
- Same orbit-size multiset, bad action: define a cyclic permutation on nodes
  whose orbits have the expected size but which maps at least one edge to a
  non-edge. Expected result: quotient action is not graph-well-defined.
- Shear/twist local clone: compare an untwisted torus grid and a shifted/twisted
  grid with the same local degree. Expected result: local-radius probes pass,
  global cycle/twist witness differs.
- Chord trap: add one chord to a cycle or ladder. Expected result: many local
  statistics remain close, but cycle-basis and quotient uniformity fail.
- Lens-name trap: call a cyclic grid quotient "lens" without a sphere/cell model
  or free cyclic action. Expected result: demote to cyclic quotient probe.
- Boundary-cost trap: use a support graph with the same boundary-size profile as
  a target row but different cycle rank or quotient action. Expected result:
  cost profile co-survives; topology alias fails.

## Alias Rules

- "Torus", "Mobius", "Klein", "lens", "cover", "quotient", and "support graph"
  are labels until the finite construction and probe relation are supplied.
- Use `same graph isomorphism class` only after an actual graph isomorphism check
  or a proof by construction.
- Use `same cover relation` only after the projection map and lift behavior are
  checked.
- Use `same quotient action` only after the action is well defined and preserves
  the structure under test.
- Use `same cost profile` only for the measured cost observable. It does not
  imply support identity.

## Source Anchors

- Hatcher, covering spaces and lift constraints:
  https://pi.math.cornell.edu/~hatcher/AT/ATch1.pdf
- Gross and Tucker, `Topological Graph Theory`, graph embeddings and voltage
  covers: https://store.doverpublications.com/products/9780486417417
- Regular graph cover: https://mathworld.wolfram.com/RegularGraphCover.html
- Slapal, digital plane topology and quotient topologies:
  https://dmtcs.episciences.org/601/pdf
- Bravyi-Hastings-Verstraete, locality/correlation/topological-order time
  constraints: DOI 10.1103/PhysRevLett.97.050401,
  https://arxiv.org/abs/quant-ph/0603121
- Hastings area law: DOI 10.1088/1742-5468/2007/08/P08024,
  https://arxiv.org/abs/0705.2024
