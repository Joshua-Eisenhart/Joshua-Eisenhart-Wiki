# Conley Index and Morse Decompositions for Finite Dynamical Systems

Date: 2026-06-11
Status: research corpus, not admitted sim evidence
Provenance: recall-based standard-math items are marked [recall]; external
  citations are named where available; repo-specific observations cite
  committed packet paths.

---

## 1. Core Finite / Combinatorial Definitions

### 1.1 Finite Transition System

The base object is a finite directed graph `G = (S, E)` where `S` is a finite
set of states and `E subset S x S` is the allowed transition relation. This is
the canonical input for combinatorial Conley theory.

In the Kalies-Mischaikow-Vandervorst (KMV) framework [recall: Kalies, Mischaikow,
Vandervorst, "Lattice Structures for Attractors I", J. Comput. Dyn. 1(2), 2014],
this finite graph is taken as a combinatorial approximation of a continuous
flow, usually obtained by a box/cell decomposition of phase space and outer
approximation of the flow within each box. The graph is not the flow — it is
a finite representor that the theory asks to be a valid outer approximation.

### 1.2 Strongly Connected Components (SCCs) and Morse Sets

The strongly connected components of `G` are the maximal subsets `M_i subset S`
such that every state in `M_i` can reach every other state in `M_i` via directed
edges. SCCs are computable in O(|S| + |E|) via Tarjan or Kosaraju [recall:
standard algorithmic graph theory].

The condensation of `G` is the DAG of SCCs. The condensation is always a DAG
(acyclic), so it carries a partial order by reachability.

A Morse decomposition of a continuous dynamical system is a finite ordered
family `(M_1, ..., M_k)` of pairwise disjoint compact invariant sets such that
every trajectory either stays in some `M_i` or connects from `M_i` to `M_j`
with `i > j` in the ordering (the Morse ordering). In the finite-graph setting,
the SCCs of `G` are the discrete Morse sets. The condensation DAG gives the
connection graph: an edge from SCC `i` to SCC `j` in the condensation means
there exist orbits that exit `i` and enter `j`.

Admissible Morse ordering: a total order on SCCs consistent with the partial
order on the condensation DAG. Multiple admissible orderings exist when the
condensation has incomparable SCCs; the partial order is the invariant, not any
particular total order.

### 1.3 Terminal / Closed Communicating Classes

A terminal SCC is a sink of the condensation DAG: no edge leaves it. Terminal
SCCs are the candidates for attractors in the finite-graph sense because there
is no allowed transition out. Non-terminal SCCs are transient under the dynamics:
every orbit through them eventually leaves for a lower SCC (in any admissible
Morse ordering).

In nondeterministic / generator-choice settings the distinction between may and
must reachability matters:
- `can_reach_terminal` (may): there exists a sequence of allowed generator
  applications that sends state `x` to a terminal SCC.
- `sure_basin_omega_containment` (must): every sequence of allowed generator
  applications from `x` eventually stays inside the terminal SCC.

These are different predicates. Confusing them overstates the basin.

### 1.4 Attracting Blocks and Isolating Neighborhoods

An attracting block for a continuous flow is an isolating neighborhood `N` with
`f(cl N) subset int N` (or `phi_t(cl N) subset int N` for all small `t > 0`).
The attractor captured by the block is `A = intersection_{t >= 0} phi_t(N)`.

In the finite-graph analog, an attracting block is a subset `B subset S` with
`E(B) subset B` (all allowed transitions from `B` stay inside `B`). The
attractor analog is the maximal strongly connected sub-DAG inside `B` whose
SCCs are terminal within `B`. In KMV language this is a combinatorial attractor
for the finite system.

The basin of an attracting block `B` in the finite system is
`Basin(B) = {x in S : omega_G(x) subset B}` where `omega_G(x)` is the set of
states reachable from `x` by some infinite walk on `G`. For a finite
deterministic transition function this is simply the set of states from which
forward iteration eventually enters `B` and stays.

### 1.5 The Attractor Lattice (KMV)

KMV [recall: "Lattice Structures for Attractors I and II"] proved that the
collection of attractors (more precisely, the collection of attracting
neighborhoods / attracting blocks up to an appropriate equivalence) for a
continuous map carries bounded distributive lattice structure. The operations
are:
- meet (greatest lower bound): `A1 ^ A2` is the attractor inside the
  intersection of their attracting neighborhoods;
- join (least upper bound): `A1 v A2` is the attractor inside the union of
  their attracting neighborhoods.

The bottom element is the empty attractor; the top element is the whole chain-
recurrent set or global attractor when it exists.

The lattice is bounded distributive, not automatically Boolean. Boolean
complement structure requires extra assumptions (Booleanization, regular-closed-
set context, or a finite block representation that admits complementation). Do
not default to Boolean algebra language.

In the purely finite-graph setting, the attractor lattice is the lattice of
unions of terminal SCCs. Unions of terminal SCCs form a sublattice of the power
set. For a finite graph with `k` terminal SCCs, there are `2^k` attractor
candidates (subsets of terminal SCCs). The full lattice is Boolean on `k`
generators in the finite case, which is stronger than the general distributive
result — this is a finite-graph special case, not the generic theorem.

### 1.6 Conley Index

The Conley index of an isolated invariant set `S_inv` inside an isolating
neighborhood `N` is the pointed homotopy type of the quotient space `N / exit(N)`
where `exit(N)` is the exit set (points on the boundary of `N` that are
immediately leaving).

For finite graphs / cubical complexes, the Conley index has a computable version
as a graded group (homology of the index pair). KMV and the CHomP/CAPD software
projects implement this for cubical and simplicial outer approximations [recall:
CHomP — Computational Homology Project, Mischaikow group].

What the Conley index proves: the index is an invariant of the isolated invariant
set, not of the neighborhood. If two neighborhoods isolate the same invariant
set they give the same index. A nontrivial index implies the invariant set is
nonempty and has computable topological complexity.

What the Conley index does NOT prove:
- Basin volume or basin measure.
- That the invariant set is an attractor (rather than a saddle, repeller, or
  more complicated invariant object).
- Persistence of the invariant set under large perturbations outside the
  isolating neighborhood.

The index classifies the invariant set's internal topology, not its attraction
direction. To get attraction direction you need the attractor-repeller pair
structure or an explicit attracting block.

### 1.7 Complete Lyapunov Functions and Morse Ordering

Conley's fundamental theorem [recall: C. Conley, "Isolated Invariant Sets and
the Morse Index", AMS CBMS 38, 1978; D. E. Norton, "The Fundamental Theorem of
Dynamical Systems", Commentationes Math. Univ. Carolinae 36(3), 1995] states:

For any continuous flow on a compact metric space, there exists a continuous
function `L : X -> R` (the complete Lyapunov function) such that:
- `L` is strictly decreasing along orbits outside the chain-recurrent set;
- `L` is constant on each chain-recurrent component;
- `L` maps chain-recurrent components to distinct values.

This function witnesses the Morse order on the chain-recurrent components: the
ordering by `L`-values is a valid Morse ordering. The components are
the Morse sets.

Finite graph analog: a complete Lyapunov function on the finite graph is an
assignment of values to states such that values strictly decrease along any
transition outside terminal SCCs, and are constant within each terminal SCC.
This is equivalent to a topological sort of the condensation DAG extended to
assign constant values within SCCs. It always exists for finite DAG condensations
[recall: standard graph theory — topological sort exists for any DAG].

---

## 2. Key Theorems with Hypotheses (and Where Each Fails)

### 2.1 Conley Decomposition Theorem

**Statement:** For any continuous flow on a compact metric space, there exists a
Morse decomposition into chain-recurrent components with gradient-like motion
between them. A complete Lyapunov function witnesses the order.

**Hypotheses:** continuous flow, compact metric space, invariance under the flow.

**Where it fails or requires care:**
- Finite graphs are not continuous flows. The theorem does not apply literally;
  the combinatorial analog applies to the finite graph as a formal object, not
  as a certified approximation of a continuous flow.
- Compactness is essential. Unbounded systems can have dynamics escaping to
  infinity without any recurrent core.
- The chain-recurrent set can be the entire space (e.g., conservative Hamiltonian
  flows, volume-preserving flows). In that case the decomposition is trivial and
  gradient-like parts may be absent.
- Small perturbations can change the chain-recurrent set discontinuously. The
  decomposition is structurally stable only under additional Morse-Smale or
  hyperbolicity assumptions.

### 2.2 KMV Attractor Lattice Theorem

**Statement:** The collection of attractors of a continuous map on a compact
metric space forms a bounded distributive lattice.

**Hypotheses:** continuous map, compact metric space, attractors defined via
attracting neighborhoods (the KMV notion, not Milnor basins).

**Where it fails or requires care:**
- Non-invertible maps require careful definition of the meet operation. Naive
  intersection of basins does not always give a basin; the meet must be computed
  as the attractor inside the intersection of attracting neighborhoods.
- The lattice is bounded distributive, not Boolean. The complement of an attractor
  need not be an attractor.
- The theorem is for the abstract lattice of attractors. Enumerating all
  attractors computationally is a separate (harder) task. Finite graph
  computations enumerate terminal SCC subsets, but these are attractors of the
  discrete graph, not provably all attractors of the underlying continuous system
  unless the outer approximation is certified tight.
- Fractal or complicated basin boundaries do not obstruct the lattice structure,
  but they do obstruct clean finite enumeration of attractors at finite resolution.

### 2.3 Persistence / Continuation of Attractors

**Statement:** An attractor with a certified attracting block persists under
sufficiently small perturbations of the map (persistence under Hausdorff
perturbation).

**Hypotheses:** the block condition `f(cl N) subset int N` holds strictly; the
perturbation is small in an appropriate topology.

**Where it fails or requires care:**
- Milnor attractors (positive-measure basins only, no open-neighborhood
  requirement) do not have automatic persistence. A positive-measure basin can
  be destroyed by perturbation without violating the theorem.
- Riddled basins are a strong obstruction: even a robust attractor can have
  riddled basins, meaning the basin cannot be certified locally.
- Blowout bifurcations can destroy attractors with riddled basins.
- In finite graphs the attracting block condition is `E(B) subset B`. This is
  exact for the graph and provides no persistence margin for the underlying
  continuous system unless the outer approximation is certified.

### 2.4 Conley Index Implies Nontrivial Invariant Set

**Statement:** If the Conley index of an isolating neighborhood is nontrivial,
then the maximal invariant set inside the neighborhood is nonempty.

**Hypotheses:** the neighborhood is genuinely isolating (no orbit tangent to or
exiting through the interior; the exit set is well-defined); continuous flow.

**Where it fails or requires care:**
- Trivial index means the theorem gives no information; the invariant set may
  or may not be nonempty.
- The index does not distinguish attractors from saddles or repellers. A fixed
  point and a limit cycle can both have nontrivial indices, but of different
  types.
- In finite graph approximations, the combinatorial index can be nontrivial
  without certifying that the corresponding continuous invariant set has the
  same topology. The approximation must be a valid outer approximation for the
  index to transfer.

### 2.5 Finite Graph Morse Decomposition vs. Continuous Morse Decomposition

**Statement:** The SCCs of a finite transition graph form a Morse decomposition
of the discrete dynamical system defined by that graph.

**Hypotheses:** the graph is taken as a formal discrete dynamical system.

**Where it fails as a statement about the underlying continuous system:**
- The finite graph is an outer approximation. Every orbit of the continuous
  system crosses some cell, and the allowed transitions encode which cells can
  follow which. But the outer approximation can include spurious transitions that
  are not actually realized by any trajectory. This means:
  - A terminal SCC in the graph that is spuriously connected by outer-approximation
    edges may not correspond to any continuous invariant set.
  - The number of terminal SCCs in the graph at a given resolution can differ from
    the number of actual attractors of the continuous system.
- Grid/discretization refinement can split or merge terminal SCCs. This is not a
  defect in the theory — it is the correct behavior, since the finer graph is a
  better approximation — but it means that terminal SCC counts are
  resolution-relative, not invariants of the continuous system.

---

## 3. What the Conley Index Adds Over Plain SCC Analysis

Plain SCC analysis on a finite transition graph gives:
- partition into communicating classes;
- terminal vs. transient classification;
- condensation DAG and reachability partial order.

It does NOT give:
- any information about what the SCCs correspond to in the underlying continuous
  system;
- distinction between attracting and non-attracting recurrent sets;
- topological type of the recurrent behavior.

The Conley index adds:
- a topological invariant (graded group from homology of the index pair) that
  classifies the internal topology of the invariant set;
- distinction between attractor (index is the homotopy type of a point, or a
  sphere depending on dimension), saddle, and repeller;
- algebraic machinery for proving the existence of connecting orbits via the
  Conley continuation / Morse-Conley-Floer chain complex and the connection
  matrix;
- invariance under continuous deformation: if the isolating neighborhood deforms
  continuously without the invariant set touching the boundary, the index does
  not change. This is the invariance that makes the index a genuine topological
  invariant.

Concretely, in the finite-graph setting: two finite grids can produce SCCs with
the same terminal-SCC structure but different Conley indices. The index detects
whether the terminal recurrent behavior is truly an attracting fixed point, a
repelling fixed point, or a more complicated object — plain SCC analysis cannot
make this distinction.

Connection matrix / Conley index for connecting orbits: the Conley index gives
algebraic necessary conditions for connecting orbits to exist between Morse sets.
If the homology does not support a needed map, the connection is forbidden. This
is an algebraic obstruction not visible from plain reachability.

---

## 4. Negatives: What Finite-Graph Morse Decompositions Cannot See

### 4.1 Grid / Discretization Dependence (the Live Instance in This Repo)

The most important negative for this project is that terminal SCC structure is
grid-dependent, not an invariant of the underlying continuous system.

A finite grid produces a transition graph whose outer-approximation edges may
include spurious connections not realized by any actual orbit. Consequently:

- A coarse grid may lump distinct attractors into one terminal SCC.
- A fine grid may split one attractor's basin into multiple terminal SCCs.
- A rotated or rescaled grid may change the SCC counts entirely, even for the
  same underlying dynamics.

The repo's `basin_grid_refinement_control_v0` (commit via envelope, all_pass=true)
directly measured this. The G1 generator family on a 33-cell anchor grid produces
3 terminal SCCs (sizes 1, 14, 18). Refining the grid produces different SCC
counts. An axis-snapped fake class dies under grid rotation because its closure
property depends on the grid alignment, not the dynamics. The continuous
cross-check shows that the Ne rotations generate SO(3) on the ball, so the
continuous system has one recurrent class after radius erasure — the finite-grid
SCCs are genuinely discretization artifacts.

The c1_answer from that sim: "C1 closes as discretization-scale structure, not
invariant continuum basin geometry." This is the finite-discretization negative
in live form.

Implication: reporting SCC counts or terminal class counts as attractor counts
is a provenance error unless the outer approximation is certified or the grid
dependence is controlled. The terminal SCC count at resolution R is evidence
about the R-scale structure of the finite transition graph, not about the number
of attractors of the continuous dynamics.

### 4.2 What Plain Finite Morse Decompositions Miss in Continuous Systems

- Attractor vs. saddle distinction: a terminal SCC is a candidate; whether it
  is attracting requires additional evidence (attracting block condition, Lyapunov
  test, eigenstructure of the map at fixed points).
- Basin measure and geometry: finite SCCs carry no measure. They say which cells
  lead to which terminal class under the outer approximation, not what fraction
  of phase space those basins occupy.
- Riddled / fractal boundary: if the continuous basin boundary is fractal or
  riddled, no finite-resolution grid can certify a clean basin partition. The
  finite graph will assign cells to one class, but nearby cells in the continuous
  phase space may belong to different basins.
- Metastability / transient structure: a finite terminal SCC may correspond to
  a long-lived transient in the continuous system, not a genuine attractor, if
  the outer approximation includes spurious self-loops or if the continuous
  dynamics has very slow drift.
- Infinite-time vs. finite-time behavior: the omega-limit set in the continuous
  system may not be an attractor in the KMV sense (e.g., quasi-periodic orbits
  on a torus, or a Milnor attractor without an open basin).

### 4.3 What the Conley Index Cannot Tell You

- Basin volume, measure, or robustness.
- Whether an attractor actually attracts from a practical neighborhood: the
  index is topological, not metric.
- The exact number of attractors: the index proves the existence (or rules out
  the existence) of invariant sets in a given neighborhood, but enumerating all
  attractors requires a covering argument across all possible neighborhoods.
- Direct falsification of multistability from a trivial index: a trivial index
  means no simple invariant set inside the neighborhood, but it does not mean
  the whole system has no other attractor somewhere else.

### 4.4 Chart/Convention Dependence (the Repo's Convention-Sweep Instance)

The `basin_two_engine_joint_v3_convention_sweep` packets show a sharper version
of the same phenomenon at the level of generator conventions. Under convention
A (order-sensitive, readout-transition-dwell), the sync terminal class count is
28; under convention D (direction-as-loop), the sync count is 24. Under all
order-blind rows, the moving-engine dynamics has one terminal cycle traversing
the full 32-state carrier.

This is not a grid-scale artifact — it is a convention-level artifact. The
Morse decomposition of the joint system depends on which generating set is
chosen, which is a choice about which transitions are allowed, not an invariant
of the underlying dynamics. The c1_answer from the grid refinement sim applies
here too: finite-graph SCC counts close as convention/discretization-scale
structure, not invariant basin geometry.

### 4.5 Boundary Cases Where the Theory Applies But Gives Weaker Information

- Conservative / measure-preserving systems: the entire phase space is chain-
  recurrent. The Conley decomposition is trivial. Basin language is inappropriate.
- Systems with a continuum of fixed points (degenerate equilibria): the attractor
  lattice can be uncountably large; finite approximation is problematic.
- Non-autonomous systems: there are no fixed basins when the vector field depends
  on time. Conley theory for non-autonomous systems requires the skew-product
  formulation or random attractor theory.

---

## 5. Computable Procedures

### 5.1 Building the Finite Transition Graph

Input: a finite set of states (cells, cubes, interval boxes, or labeled discrete
states) and a rule for computing allowed transitions between adjacent states.

For continuous flows via outer approximation: for each cell `c`, compute an
enclosure of `{phi_tau(x) : x in c}` and mark all cells intersecting the
enclosure as targets of `c`. This requires a validated numerical integrator or
interval arithmetic. Without validated enclosures, the graph is a heuristic
approximation, not a certified outer approximation.

For finite/discrete dynamics: the transition relation is exact by definition.

### 5.2 SCC Computation

Algorithm: Tarjan's strongly connected components (linear time O(|S| + |E|)).
Output: partition of `S` into SCCs plus the condensation DAG.
Libraries: `networkx.strongly_connected_components` in Python; `Graphs.jl`
in Julia (both used in repo basin sims).

### 5.3 Terminal SCC Identification and Basin Partition

From the condensation DAG, terminal SCCs are sinks (no outgoing edges in the
condensation). For each terminal SCC `T_i`, the basin `B_i` is the set of states
in the original graph that have no path to any terminal SCC other than `T_i`
(under the deterministic or universal-must reading). In nondeterministic settings
this splits into:
- `can_reach(T_i)`: states from which some walk reaches `T_i`;
- `only_reach(T_i)`: states from which all walks reach `T_i` (must semantics).

These are different and must be reported separately when the generator relation
is not deterministic.

### 5.4 Attracting Block Construction from the Finite Graph

Given a candidate subset `B subset S`, check `E(B) subset B` (no outgoing edges
from `B` to `S \ B`). If this holds, `B` is a combinatorial attracting block.
The attractor inside `B` is the maximal terminal SCC union within `B`. This is
directly computable from the transition graph.

### 5.5 Conley Index Computation (Finite / Cubical Version)

For cubical complexes with interval-box outer approximations, the CHomP
computational homology project computes the Conley index as a graded group via
a reduction algorithm on the cubical chain complex of the index pair `(N, N^-)`.
The CAPD library (Computer Assisted Proofs in Dynamics) provides rigorous
interval arithmetic integrators for the outer approximation step.

For simple finite graphs, the combinatorial Conley index can be computed as the
reduced homology of the condensed SCC/exit-set structure. For terminal SCCs
(attractors), the index is that of a point (degree 0 contributes Z, higher
degrees trivial). For saddles, the index encodes the unstable manifold dimension.

### 5.6 Attractor Lattice Construction

Given the finite terminal SCC set `{T_1, ..., T_k}`, enumerate the `2^k`
subsets. For each subset `I subset {1,...,k}`, the union `union_{i in I} T_i`
is a candidate attractor. Compute the attracting basin for each candidate. The
lattice operations are:
- meet: intersection of basins (restricted to `S`);
- join: union of attractors.
For the finite graph, this is a Boolean lattice on `k` generators. The general
continuous-map case gives only a bounded distributive lattice.

### 5.7 Persistence / Refinement Testing

Run the SCC computation at multiple grid resolutions. Record the class count,
class sizes, and condensation DAG structure at each resolution. Check which
classes PERSIST (correspond by containment to a class at the next level),
MERGE (two classes join), SPLIT (one class divides), or DISSOLVE (class
disappears). Z3/CVC5 can certify the persistence identity: encode the fate
table as integer-valued constraints and prove UNSAT against a flipped fate to
confirm the fate was not asserted by hand.

The repo's `basin_grid_refinement_control_v0` uses exactly this pattern: four
fate codes (PERSIST, MERGE, SPLIT_FURTHER, DISSOLVE), z3 and cvc5 proofs, and
an axis-artifact control that confirms grid-snapped fake classes dissolve under
rotation (designed-fail).

### 5.8 Order-Sensitive vs. Order-Blind Generating Sets

When the transition relation is generated by a set of generators (not a single
map), the terminal SCC structure can depend on whether generators are applied
in order, in parallel, or interleaved. Test both:
- sync (all generators applied simultaneously or as a single composed step);
- async (generators applied one at a time, union of all choices);
- l_only / r_only projections (only one factor's generators active).

The B-constraint from the repo: if the system has directed loops as a design
feature (two directed cycles, e.g., deductive and inductive order), any
realization that treats stage labels as unordered is source-invalid even if
computationally convenient. Order-blind SCC counts close as artifacts.

---

## 6. Repo Relevance

### 6.1 Basin Criterion Contract

`system_v6/receipts/attractor_basin_criterion_20260611.md` operationalizes
the attractor-basin doctrine as a finite `M(C)` / `R_C` build contract with
four requirements: invariance (`F_C(A) subset A`), attraction (computed
neighborhood with contraction), Lyapunov-type object (narrowing measure `V_narrow`
as primary, entropy ledger as typed telemetry), and failure semantics (six
labeled outcomes including `shell_breaking` and `empty_conditioned_survivor`).

The Conley/SCC vocabulary in Section 1 of this note maps directly to the
sub-basin program in Section 2 of that receipt: attracting blocks `(B_i, E_i)`,
the finite lattice (vertices = block-pair attractors, order = reachability),
Morse decomposition (SCCs give Morse sets, condensation edges are connecting-orbit
witnesses). The receipt explicitly keeps these as the Conley/lattice
implementation route in the BINDING-SPEC RECONCILIATION section.

The nine-card contract in that receipt maps to the procedures above:
card requirement 1 (finite `S`) = Section 5.1; requirement 3 (`R_C` explicit) =
Section 5.2-5.4; requirement 4 (trapping test) = Section 5.4; requirement 5
(Lyapunov/monotone observable) = Section 1.7 complete Lyapunov analog;
requirement 6 (escape tests) = Section 3 / Section 4; requirement 7 (basin
partition, terminal vs. metastable vs. leaky) = Section 5.3 with may/must
distinction; requirement 8 (engine DoF perturbation) = the order-sensitive
generator test in Section 5.8.

### 6.2 Grid Refinement Control

`system_v6/sims/basin_grid_refinement_control_v0` is the live instance of the
grid/discretization negative (Section 4.1 above). The sim's c1_answer directly
reports: "C1 closes as discretization-scale structure, not invariant continuum
basin geometry." The G1 anchor at 33 cells gives 3 terminal SCCs; the continuous
dynamics under Ne generators closes as SO(3) with one recurrent class. This
confirms the core negative: do not report finite-graph SCC counts as continuous-
system attractor counts without controlling for grid dependence.

The persistence fate taxonomy (PERSIST / MERGE / SPLIT_FURTHER / DISSOLVE) with
z3+cvc5 certification is the computable procedure from Section 5.7, instantiated
with load-bearing proofs.

### 6.3 Convention Sweep (Two-Engine Joint)

`system_v6/sims/basin_two_engine_joint_v3_convention_sweep` is the live instance
of the convention/generating-set dependence negative (Section 4.4 above). Sync
terminal counts vary from 24 to 28 depending on convention (A vs. D); all
order-blind rows reduce to one terminal cycle. The per-engine earned content is
the within-slice terminal core (28 or 24 states under order-sensitive conventions),
not the mechanical 32-state count from frozen-factor projections.

This directly instantiates the "admissible Morse ordering" subtlety from Section
1.2: multiple admissible orderings exist when SCCs are incomparable, and
different generating sets can change the condensation DAG.

### 6.4 Owner Prediction: 64 Sub-Sub-Basins

`system_v6/receipts/owner_prediction_64_subsubbasins_20260611.md` records the
pre-registered prediction of `2 x 2 x 4 x 4 = 64` subsubbasins under joint
L/R engine dynamics. The current standing is UNCONFIRMED across realized rows —
no source-valid B-sensitive row reaches 64 terminal classes at any natural
quotient level. The sharper positive from v3: the per-engine 32-state product
carrier is real and coherently traversed, but it has no internal sub-basin
structure under flux-blind conventions. The v4 question is whether carrying
Flux2 and chirality asymmetry creates within-engine sub-basin structure — which
maps to Section 4.4's observation that the number of terminal SCCs is convention/
generating-set dependent, and that the right generating set must be source-
faithful (Section 5.8 B-constraint).

The mathematical language from this note that applies: the attractor lattice is
determined by the terminal SCC structure; the terminal SCC structure depends on
the generating set; the generating set must come from source-admitted constraints
(the Morse decomposition is not convention-independent). Confirming the 64
prediction requires pinning the substage transition convention and verifying that
the resulting B-sensitive finite graph has exactly 64 terminal SCCs with the
`2 x 2 x 4 x 4` product factorization.

### 6.5 Terrain Flow Worked Examples

`system_v6/receipts/attractor_basin_criterion_20260611.md` Section 1 provides
two worked terrain rows (Ne_Spiral_R and Ni_Source_R) that instantiate the
attractor classification from Section 1.2-1.3 of this note. Ne_Spiral_R is
`invariant_not_attracting` (the Bloch ball is invariant but the fixed `z=1/2`
shell is not; the dynamics are rotational with purely imaginary eigenvalues,
exactly the conservative-system case in Section 4.5). Ni_Source_R is
`attracting` (all eigenvalues have negative real part, unique interior fixed
point, whole Bloch ball basin). These are the two sides of the attractor
classification in Section 2.3.

### 6.6 What This Note Does Not Cover (Deliberate Scope Boundaries)

- Quantum / completely positive map analogs of Conley theory: the repo uses
  Lindblad dynamics and density matrix flows; Conley theory for quantum channels
  exists in sketch form [recall: some recent literature on fixed points of
  quantum channels, e.g., Blume-Kohout et al. on steady states] but the
  combinatorial version for finite quantum state graphs is not as developed as
  the classical version. Claims about quantum basin structure need their own
  source backing.
- Stochastic Conley theory: the Freidlin-Wentzell large-deviations framework
  addresses basin escape under noise but does not use the Conley index. The two
  frameworks are complementary, not the same object.
- CW-complex / Morse theory for smooth manifolds: this is a different and older
  theory (Morse 1934). Morse index at a critical point is the dimension of the
  unstable manifold. It is related to the Conley index but the Conley framework
  generalizes to non-smooth and non-gradient systems. Do not conflate the
  classical Morse index with the Conley Morse-set ordering.

---

## Source Anchors

Standard-math items (recall-based, not independently fetched this session):
- C. Conley, "Isolated Invariant Sets and the Morse Index", AMS CBMS 38, 1978.
- D. E. Norton, "The Fundamental Theorem of Dynamical Systems", Commentationes
  Math. Univ. Carolinae 36(3), 1995.
- W. D. Kalies, K. Mischaikow, R. C. A. M. Vandervorst, "Lattice Structures for
  Attractors I", J. Comput. Dyn. 1(2), 2014.
- W. D. Kalies, K. Mischaikow, R. C. A. M. Vandervorst, "Lattice Structures for
  Attractors II", arXiv:1409.5405.
- W. D. Kalies, D. Kasti, R. C. A. M. Vandervorst, "An Algorithmic Approach to
  Lattices and Order in Dynamics", FAU preprint.
- W. D. Kalies, K. Mischaikow, R. C. A. M. Vandervorst, "An Algorithmic Approach
  to Chain Recurrence", FAU preprint.
- K. Mischaikow, "Conley Index Theory", Lecture notes, available via EUDML.
- J. Milnor, "On the Concept of Attractor", Commun. Math. Phys. 99, 1985.

Repo-committed evidence:
- `system_v6/receipts/attractor_basin_criterion_20260611.md`
- `system_v6/receipts/owner_prediction_64_subsubbasins_20260611.md`
- `system_v6/sims/basin_grid_refinement_control_v0/results/basin_grid_refinement_control_v0_jax_results.json`
- `system_v6/sims/basin_two_engine_joint_v3_convention_sweep/results/basin_two_engine_joint_v3_convention_sweep_envelope_results.json`
- `wiki/codex-ratchet-research/basins/standard-math.md` (prior corpus)
- `wiki/codex-ratchet-research/basins/negatives.md` (prior corpus)
- `wiki/codex-ratchet-research/basins/alternatives.md` (prior corpus)
