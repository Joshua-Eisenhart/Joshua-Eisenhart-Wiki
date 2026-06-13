# S6/S7 Topologies - Standard Math

Status: wave-2 populated research register.

Scope: citation-level math context for finite support graphs, grid quotients,
covers, twisted boundary conditions, and locality/cost language. This page is
not an admission receipt and does not promote any topology row.

## Discrete Tori And Covers

- A finite square torus grid can be represented as the Cartesian product
  `C_m square C_n`, equivalently an `m x n` grid whose opposite horizontal and
  vertical boundary vertices are identified. MathWorld's torus grid graph page
  is a stable citation anchor for the graph object and for the warning that the
  planar drawing is not the topology; the natural embedding is on a torus.
- For Ratchet rows, "same torus" should mean the same finite graph under a named
  graph isomorphism or the same quotient rule under a named probe. Equal node
  counts or equal local degree do not imply the same topology row.
- Cover language should stay at the graph-cover level unless a cell complex or
  manifold triangulation is explicitly supplied. Hatcher's algebraic topology
  text is the stable background for covering-space/lift language; Gross-Tucker
  style voltage graphs are the graph-theoretic mechanism for regular covers and
  lifts.
- Voltage assignments are a useful finite construction for candidate rows:
  choose a base graph, assign group elements to oriented edges, and form the
  derived graph/lift. This supports future tests where two candidates share
  cover cardinality but differ in voltage data.

## Lens Quotients On Grids

- Classical lens spaces are quotients of odd-dimensional spheres by free cyclic
  actions; the common 3D case starts from `S^3` and a cyclic group action. That
  literature is a quotient-action anchor, not proof that an arbitrary finite
  grid quotient is a lens-space model.
- For finite grid rows, a "lens-action" claim needs a well-defined action on the
  actual finite support set: closure under the action, orbit sizes, no unwanted
  fixed points if free action is being claimed, and compatibility with adjacency
  or cell incidence.
- A `Z_4`-style shift quotient can be useful as a finite candidate, but it must
  carry the exact action table. The row should fail if the shift does not descend
  to the grid, if orbit sizes are inconsistent with the claimed quotient, or if
  adjacency is not preserved.
- Keep `2:1 cover`, `Z_4 quotient`, and `lens descent` separate. They are
  related vocabulary, not aliases.

## Twisted Covers: Mobius And Klein

- Mobius/Klein language is safest as boundary-identification language on finite
  strips or grids: one periodic direction may identify with a flip; two
  directions may combine periodic and flipped identifications. The exact gluing
  rule matters.
- A finite Mobius strip graph can be modeled by a rectangular strip with one
  direction identified after reflection. A Klein-bottle grid can be modeled by
  one periodic direction and one twisted direction, or by related finite
  quotient presentations. These are support-graph/cell-complex models, not
  automatic smooth-surface claims.
- Twisted variants can preserve node count, degree distribution, and many local
  neighborhoods while changing global cycle holonomy. This makes them useful
  designed controls for "local same, global different" probes.
- Literature on toroidal versus Klein-bottle lattice graphs is useful because it
  shows why some graph indices can fail to distinguish twisted global topology.
  Treat such indistinguishability as probe-relative, not as identity.

## Locality, Area Laws, And The Cost Result Context

- Lieb-Robinson bounds provide the standard citation context for finite-speed
  propagation in local lattice/spin systems: locality restricts how quickly
  correlations and information can spread through the support graph.
- Bravyi-Hastings-Verstraete connect Lieb-Robinson locality with correlation
  growth, topological order preparation time, and entropy generation bounded by
  boundary size. Use this as boundary/locality context, not as a topology
  classifier.
- Hastings' one-dimensional area-law result is the standard citation anchor for
  gapped 1D local quantum systems: entanglement entropy is bounded in a way that
  supports matrix-product-state approximability. It does not say every finite
  graph with low boundary cost has the same topology.
- Local Ratchet cost probes such as
  `system_v5/ops/formal_scouts/sim_boundary_conditional_expectation_area_law_entropy_scaling_probe.py`
  should be described as finite boundary-support or entropy-scaling scouts. The
  standard literature justifies the locality/boundary vocabulary; it does not
  upgrade the scout into a manifold, holography, or topology-identity result.

## Source Anchors

- Torus grid graph: Wolfram MathWorld,
  https://mathworld.wolfram.com/TorusGridGraph.html
- Regular graph covers / voltage graphs: Wolfram MathWorld,
  https://mathworld.wolfram.com/RegularGraphCover.html
- Gross and Tucker, `Topological Graph Theory`, Wiley, 1987; Dover reprint page:
  https://store.doverpublications.com/products/9780486417417
- Hatcher, `Algebraic Topology`, Chapter 1 covering spaces:
  https://pi.math.cornell.edu/~hatcher/AT/ATch1.pdf
- Lens-space quotient background: nLab, https://ncatlab.org/nlab/show/lens+space
- Lieb and Robinson, "The finite group velocity of quantum spin systems",
  Communications in Mathematical Physics 28, 251-257 (1972),
  DOI: 10.1007/BF01645779,
  https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-28/issue-3/The-finite-group-velocity-of-quantum-spin-systems/cmp/1103858407.pdf
- Bravyi, Hastings, Verstraete, "Lieb-Robinson bounds and the generation of
  correlations and topological quantum order", Physical Review Letters 97,
  050401 (2006), DOI: 10.1103/PhysRevLett.97.050401,
  arXiv:quant-ph/0603121, https://arxiv.org/abs/quant-ph/0603121
- Hastings, "An Area Law for One Dimensional Quantum Systems", J. Stat. Mech.
  (2007) P08024, DOI: 10.1088/1742-5468/2007/08/P08024,
  arXiv:0705.2024, https://arxiv.org/abs/0705.2024
