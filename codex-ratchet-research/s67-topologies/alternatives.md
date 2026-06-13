# S6/S7 Topologies - Alternatives

Status: wave-2 populated research register.

Scope: finite topology/support-graph alternatives useful for future rows. These
are candidate families and controls, not admitted equivalents.

## Candidate Support Graph Families

- Untwisted torus grid: `C_m square C_n`. Baseline periodic boundary condition
  with two commuting cycle directions.
- Shear torus: identify one boundary after a cyclic shift. Useful for separating
  "same local degree and same node count" from "same cycle basis / same quotient
  action".
- Shifted Mobius strip: identify one boundary after reflection plus optional
  shift. Useful for testing whether the probe detects orientation-reversing
  global holonomy rather than only local neighborhoods.
- Klein grid: one periodic direction and one reflected/twisted direction. Useful
  as a nonorientable closed-surface support model when the finite gluing rule is
  explicit.
- Double-twist Klein variant: use two named flips/shifts where the resulting
  quotient remains well defined. Useful only if the finite action preserves
  adjacency/incidence.
- Prism/ladder graph: finite low-dimensional control family with regular local
  structure and obvious covers. Useful as a small fixture before grid-scale
  twisted rows.
- Cycle with one chord: designed-fail graph for alias traps. It can share many
  local cycle features with cleaner graphs while having a distinguished shortcut
  edge that breaks uniform quotient assumptions.
- Cayley graph quotient candidates: finite groups with generators provide
  controlled support graphs where quotient/lift maps can be written as group
  homomorphisms. Good for later voltage-graph and lens-action tests.
- Cell-complex grid: promote from graph-only to a finite 2-complex by adding
  square faces with explicit boundary cycles. Use when the probe needs incidence,
  orientability, Euler characteristic, or homology rather than adjacency alone.
- Hypergraph/support-complex variant: when interactions are not pairwise edges,
  use a hypergraph or simplicial/cell complex and record that graph topology is
  only the 1-skeleton.

## Quotients And Covers Worth Keeping Separate

- `2:1 cover`: a cardinality and projection claim. It does not imply Mobius,
  Klein, spin, or lens semantics by itself.
- Regular graph cover from voltage data: a finite lift with group-labelled
  edges. Good candidate mechanism for cyclic, dihedral, and signed twist rows.
- Orbit quotient by a finite group action: requires an explicit action on nodes
  and, if using graph/cell structure, action compatibility with adjacency or
  incidence.
- Lens-style cyclic quotient: only a finite analogue unless the row supplies a
  sphere/triangulation/cell-complex model and a free cyclic action. On a grid,
  call it a cyclic quotient probe unless lens descent is checked.
- Cover composition: composition of regular covers can lose regularity. Keep
  the intermediate cover receipts if a later row chains two quotient operations.

## Probe Targets For Future Rows

- Node count, edge count, degree multiset, cycle rank, girth, diameter.
- Cycle-basis signatures before and after quotient.
- Orbit-size multiset for the claimed group action.
- Lift/descent check: every base edge lifts to the expected number of edges and
  every quotient edge has a valid preimage.
- Orientation/twist witness: a loop that returns with reversed transverse label
  in Mobius/Klein-style rows.
- Locality witness: nearest-neighbor radius-`r` neighborhoods are identical
  while a global invariant differs.
- Cost/profile witness: boundary size or contraction path changes under the
  support graph, without claiming topology identity from cost alone.

## Source Anchors

- Torus grid graph: Wolfram MathWorld,
  https://mathworld.wolfram.com/TorusGridGraph.html
- Regular graph cover: Wolfram MathWorld,
  https://mathworld.wolfram.com/RegularGraphCover.html
- Pask and Yeend, "Voltage Graphs" (1998),
  https://documents.uow.edu.au/~dpask/index_files/papers/voltage.pdf
- Malnic, Nedela, and Skoviera, "Lifting graph automorphisms by voltage
  assignments", European Journal of Combinatorics 21 (2000) 927-947,
  DOI: 10.1006/eujc.2000.0383
- Bahmanian and Sajna, "Composition of regular coverings of graphs and voltage
  assignments", Australasian Journal of Combinatorics 28 (2003) 131-148,
  https://ajc.maths.uq.edu.au/pdf/28/ajc_v28_p131.pdf
- Slapal, "Topological structuring of the digital plane", DMTCS 15:2 (2013),
  165-176, https://dmtcs.episciences.org/601/pdf
