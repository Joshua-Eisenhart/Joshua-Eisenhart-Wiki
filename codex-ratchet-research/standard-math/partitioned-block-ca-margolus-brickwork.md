# Partitioned/Block Cellular Automata: Margolus Neighborhoods, Brickwork Normal Forms

**Date written:** 2026-06-11
**Recall-based unless cited otherwise.** Key theorems with authors/papers are standard-math provenance;
interpretive remarks are labeled [interpretation].
**Ceiling:** standard-math research note; no promotion, no sim admission.

---

## 1. Core Definitions

### 1.1 Cellular Automaton (CA)

A **cellular automaton** over lattice L (typically Z^d) with finite alphabet Q is a triple
(L, Q, f) where f: Q^N(0) -> Q is a **local update rule** and N(i) is the finite neighborhood
of cell i.  The global map F: Q^L -> Q^L applies f simultaneously at every cell.  For finite
L = Z_n (a ring), this is a function on Q^n.

Key distinguishing properties compared to a generic finite map:
- **Locality**: f depends only on a bounded neighborhood N(0), not the full configuration.
- **Homogeneity** (classical CA): the same f applies at every cell (translation-invariant).
- **Synchrony**: all cells update simultaneously.

### 1.2 Partitioned / Margolus Automaton

A **partitioned CA** (also "block CA," "Margolus CA") breaks the lattice into non-overlapping
blocks and applies a **blockwise map** g: Q^B -> Q^B to each block simultaneously, then shifts
the partition for the next phase.

**Margolus neighborhood (1D ring):**
For n even, the **even partition** is the set of non-overlapping pairs {(0,1), (2,3), ...}.
The **odd partition** is {(1,2), (3,4), ..., (n-1,0)}.  One full **Margolus step** is:
1. Apply g to every pair in the even partition (phase A).
2. Shift the partition offset by 1; apply g to every pair in the odd partition (phase B).

In 2D: Margolus defined the 2x2 block-partitioned scheme (Margolus 1984, "Physics-like models
of computation," Physica D 10(1-2):81-95).  The block is a 2x2 cell group; alternating phases
offset the partition by (1,1).

In 1D with pair blocks the scheme is sometimes called the "checker" or "brick" partition.  With
larger blocks or hexagonal lattices, the same idea generalizes.

### 1.3 Brickwork / Circuit-Layer Form

A **brickwork** in the quantum context is a specific 1D qubit-lattice circuit pattern (Bravyi,
Gosset, Konig; also Gross, Nesme, Vogts, Werner 2012):

```
Layer 1: |  (0,1)  |  (2,3)  |  (4,5)  |  ...
Layer 2: |  (1,2)  |  (3,4)  |  (5,6)  |  ...
```

Each gate in layer 1 acts on an even-offset pair; each in layer 2 acts on an odd-offset pair.
This is the 1D Margolus scheme with 2-cell blocks, expressed as a two-layer circuit.

**Standard-math fact (Gross, Nesme, Vogts, Werner 2012 — "Index theory of one-dimensional
quantum walks and cellular automata," Commun. Math. Phys. 310:419-454):** every **translation-
invariant** 1D QCA over a finite-dimensional qudit lattice is **unitarily equivalent** to a
brickwork circuit (finite depth, nearest-neighbor gates), possibly composed with a global shift.
The "brickwork normal form" theorem names this equivalence.

The **brickwork normal form theorem** (GNVW theorem, after Gross, Nesme, Vogts, Werner): every
1D QCA U (translation-invariant, finite range) has an index alpha(U) in Q* (the positive
rationals under multiplication), computable as:

    alpha(U) = dim(A_R) / dim(A_L)

where A_R is the right-crossing support algebra and A_L is the left-crossing support algebra of
U at any bond of the lattice.  The index is:
- a complete invariant of the stable equivalence class (= equivalence up to tensor product with
  finite-depth circuits + ancillas);
- multiplicative under composition: alpha(U composed with V) = alpha(U) * alpha(V);
- equal to 1 for any finite-depth (brickwork) circuit.

### 1.4 QCA Formal Definition

A **quantum cellular automaton** (QCA) on a 1D qudit chain (finite sites, each carrying a
d-dimensional Hilbert space H_d) is a unitary map U on the full tensor product, satisfying:
- **Locality**: for every observable O supported on region R, U(O) = U O U^dagger is supported
  on R + neighborhood r (finite, uniform).  Equivalently U is a **quasi-local automorphism**
  with finite Lieb-Robinson velocity.
- **Translation invariance** (for the GNVW theorem to apply).

More general QCAs drop translation-invariance; the index then requires additional structure.
CPTP-map QCAs (non-unitary) also appear in open-system settings.

---

## 2. Key Theorems with Hypotheses

### 2.1 Block CA Reversibility

**Theorem (Toffoli 1977; folklore for block CAs):** A partitioned/block CA is **bijective**
(reversible as a global map) **if and only if** the blockwise map g: Q^B -> Q^B is a
**bijection** on each block.

Hypotheses needed:
- Finite lattice OR translation-invariant infinite lattice.
- Simultaneous uniform application of the same g to all blocks in each phase.

Where it fails:
- If the partition is non-uniform (different block shapes in different regions), the per-block
  bijectivity characterizes a local condition but the global map's reversibility needs a
  compatibility argument.
- For non-partitioned CAs (e.g. Rule 110, totalistic rules), bijectivity of the global map
  does NOT follow from any single-cell-neighborhood criterion; it must be checked globally.

[interpretation] This is the theorem that motivates the partitioned form as a natural venue for
reversible simulation: the reversibility of F collapses entirely to the per-block condition,
which is cheap to verify and enforce.

### 2.2 GNVW Brickwork Normal Form (1D QCA)

**Theorem (Gross, Nesme, Vogts, Werner 2012):** Let U be a translation-invariant unitary QCA
on a periodic 1D qudit chain (finite cell dimension d, finite range r).  Then:

    U is stably equivalent to a brickwork circuit  iff  alpha(U) = 1.

Every U decomposes as: U = (shift^k) composed with (brickwork circuit), for a unique integer k
(the "shift number" mod n) and a finite-depth brickwork.

The **index** alpha(U) is computed at any bond as:
    alpha(U) = dim(A_right) / dim(A_left)

where A_right (resp. A_left) is the algebra of right-going (resp. left-going) information
crossing that bond.

Hypotheses needed — all of these are necessary; the theorem fails without them:
1. **1D lattice** (chain or ring).  For 2D or higher, no complete index theory exists; partial
   results are known for abelian anyons / SPT phases.
2. **Translation invariance**.  Without it, the bond algebras can vary along the chain and the
   single ratio is not well-defined.
3. **Finite cell dimension** (qudit, not qubit field).  For bosonic chains the algebra analysis
   extends with care.
4. **Unitary** U.  For CPTP (open-system) QCAs the index generalizes to a capacity-like
   quantity, but the GNVW integer/rational form no longer applies directly.
5. **Finite range** (Lieb-Robinson locality).  Long-range interactions can evade the bond-
   algebra decomposition.

### 2.3 Index Invariance

**Theorem (GNVW 2012, Cor. 2):** alpha(U) is invariant under:
- conjugation by any finite-depth QCA (local-basis reparameterization);
- appending ancilla qudits initialized in a product state;
- composition on either side with any brickwork circuit.

This is the invariance that makes alpha a genuine topological invariant (in the sense of
stable equivalence), not merely a computational artifact.

**What the invariance test requires:**  alpha must be computed from the *realized* support
algebra of the implemented rule, not from metadata supplied alongside the rule.  Changing the
local-basis labeling while leaving the physical operator unchanged must leave alpha unchanged;
swapping in a different local rule (with different physical support) may change alpha and
would constitute a genuine test.

### 2.4 Classical Reversible CA and Margolus Normal Form

**Theorem (Morita 2008, "Reversible computing and cellular automata -- a survey"):** Every
reversible CA on a 1D lattice is topologically conjugate to a partitioned CA (block bijective).
Specifically, any bijective global map F on Q^n can be realized by a finite sequence of
partitioned steps with block size |B| <= (range of F) + 1.

The "brickwork" for classical reversible CAs is the same two-phase offset scheme.

---

## 3. The Negatives — What the Formalism Cannot Do

### 3.1 Dimensionality Barrier

The GNVW index is **only complete in 1D**.  For d >= 2:
- No analogue of the rational-index invariant exists for all 2D QCAs.
- Classification attempts involve higher K-theory (Freedman, Haah, Hastings 2020 for certain
  2D phases), but no finite-procedure complete invariant is known for generic 2D QCAs.
- The brickwork normal form (finite depth implies index 1) still holds; the converse (index 1
  implies finite depth) does not hold in 2D without extra structure.

### 3.2 Non-Translation-Invariant Cases

The GNVW index requires a **uniform** lattice with translation symmetry.  For a finite non-
homogeneous lattice (e.g. the owner's ring-checkerboard: a ring with ATTACHED rings at discrete
steps, different cell types at base-ring vs. attached-ring positions), the bond-algebra
decomposition does not directly apply.  Adaptations exist:
- Fidkowski, Haah, Hastings (2022) handle inhomogeneous QCAs via local resource theories;
- For a finite lattice (no infinite periodic extension), the index becomes a finite-sample
  approximation; its stability under perturbation is not guaranteed.

[interpretation] For Codex-Ratchet's ring-checkerboard support: the support is not a uniform
1D qudit chain.  Any QCA-index computation on this structure is either (a) an approximation
that treats the support as locally 1D at each bond, or (b) a different formalism (e.g. a
"flow" version of the index for networks).  Neither directly inherits the GNVW theorem.

### 3.3 Non-Unitary (CPTP) QCAs

For open-system evolution (CPTP maps instead of unitaries), the index generalizes to an
"information-flow" or "quantum capacity" quantity.  The rational-index invariant does not
carry over; the GNVW theorem does not apply.  The Szilard-engine connection the owner describes
(measurement + memory per step) places the rule in the CPTP / open-system class unless the
measurement outcome is post-selected or absorbed into an ancilla system treated as part of the
system.

### 3.4 Configuration Space vs. Single-Token Dynamics

There are two distinct objects one can analyze over a CA support:

**Full configuration space:** the set Q^n of all possible state assignments to every cell
simultaneously.  The global map F: Q^n -> Q^n operates on this.  Period of a configuration c
= smallest T such that F^T(c) = c.  Basin = set of configurations that flow to a given
terminal SCC under iteration of F.

**Single-token / single-particle dynamics:** a single "active cell" or "token" moves on the
support graph according to a local transition rule.  The state space is just {active cell} x
{internal state of token}, which is O(n) rather than O(|Q|^n).  Period and SCC structure here
are properties of the token trajectory, not the full cellular automaton.

These are **not the same object**:
- Period-2 behavior in single-token dynamics does NOT imply period-2 behavior of the full
  configuration-space automaton.
- Reversibility of the single-token walk does NOT imply bijectivity of the full CA map.
- SCC counts, terminal-class counts, and basin sizes from single-token analysis apply only
  to the token state space.

This distinction is the **primary caveat on Codex-Ratchet's `ring_checkerboard_automaton_v0`**
(see Section 6 below).

### 3.5 Forced-by-Definition Results Are Not Empirical Findings

A result is **definitionally forced** (not empirical) when the measured quantity is an
algebraic consequence of the definition of the object, not of its structural properties.

Example (directly from the repo's correction entry): if an "alternating" update rule is defined
as "apply TWO phase-steps per transition call" and a "paired" rule is defined as "apply ONE
phase-step per transition call," then the ratio of their observed periods is 2:1 by construction.
Measuring it at multiple sizes adds no information: the ratio is zero-variance by definition.
Such a result should be cited only as an implementation-correctness check, not as evidence of
structural dynamical distinction.

The structural content that IS non-trivial in this setting: the transient SCC topology
(how many SCCs are transient vs. terminal, and how their counts scale with system size).
These counts are NOT forced by the phase definition and can in principle fail to differ.

### 3.6 What SMT Over Aggregate Counts Does and Does Not Prove

z3/cvc5 assertions over aggregate scalar quantities (SCC count, terminal state count,
period histogram) are **consistency and reachability proofs**, not **structural isomorphism
proofs**.  Specifically:

- "The solver asserts that SCC_alternating != SCC_paired" is a proof that the two scalars
  differ, given the realized counts.
- It is NOT a proof that the underlying transition graphs are non-isomorphic (two different
  graphs can have equal SCC counts).
- It is NOT a proof over all configurations or all sizes.

To prove non-isomorphism of the full transition graphs at a given size, one needs either
explicit certificate (e.g. a structural invariant that differs) or an enumeration/hash of
the edge multisets.

---

## 4. Computable Procedures

These are the operations a finite sim can actually execute.

### 4.1 Building the Transition Graph

Given: finite state set S, local rule f.
Output: directed graph G = (S, {(s, f(s)) : s in S}).

For a partitioned CA on n cells with alphabet Q:
- S = Q^n, so |S| = |Q|^n.  For n=4, Q={0,1}: |S|=16.  For n=20: |S|=2^20 ~ 1M.
- Each state s maps to exactly one successor f(s), so G is a **functional graph**
  (out-degree 1 everywhere).

For a single-token automaton on support of size n:
- |S| = n * |internal_states|, linear in n.

### 4.2 SCC Decomposition

Tarjan's algorithm or Kosaraju's algorithm on G: O(|S| + |edges|) time.
For a functional graph (out-degree 1): every connected component has exactly one cycle
(the terminal SCC) and a set of "rho-shaped" tails (transient SCCs are singletons in
a functional graph, since repeated application of f visits the cycle).

**Key measurables:**
- SCC count = total number of SCCs.
- Terminal SCC count = SCCs with no outgoing edges to other SCCs.
- Terminal state count = total states in terminal SCCs.
- Transient SCC count = SCC count - terminal SCC count.
- Period histogram = {T: count of terminal SCCs with period T}.

### 4.3 Basin Partition

For each terminal SCC T, the **basin** of T = {s in S : F^k(s) in T for some k >= 0}.
Basins partition S.  Sizes are computable by BFS/DFS backwards from terminal SCCs.

**May/must basin language:**
- May(T) = states that COULD reach T (under some sequence, if any non-determinism exists).
- Must(T) = states that CERTAINLY reach T (for deterministic F: Must(T) = Basin(T)).

For a deterministic functional graph, may = must.

### 4.4 Bijectivity / Reversibility Check

For a partitioned CA: check that each blockwise map g_B is a bijection on Q^B.
This requires enumerating Q^B (feasible for small blocks: |Q|=2, |B|=2 means 4 entries).

For the full global map F on Q^n: check |Image(F)| = |Q^n|.  Only feasible for small n.

### 4.5 Index Computation (GNVW, 1D QCA)

Given a unitary QCA U on a 1D ring of n qudits (dim d each):

1. Fix any bond position j (say between sites j and j+1).
2. Compute A_L = the left-crossing algebra = the operator algebra generated by
   {U(O) : O supported strictly to the left of j}  intersected with
   (operators supported to the right of j).
3. Compute A_R = symmetrically.
4. alpha(U) = dim(A_R) / dim(A_L).

For practical computation on small systems:
- Represent U as a matrix on (C^d)^n.
- Represent each O as a matrix, compute U O U^dagger, restrict support, count linearly
  independent elements of the resulting algebra.
- Alternatively, use the "cell-bond" decomposition: write U = V_even * V_odd where V_even
  acts on even bonds and V_odd acts on odd bonds; then A_L and A_R are readable off the
  factors' support.

This procedure can fail (return undefined) if:
- U is not genuinely local (the bond-algebra computation diverges).
- U is not translation-invariant (each bond gives a different ratio).
- The local rule was supplied as metadata rather than as an operator.

### 4.6 Period and Cycle Detection in Single-Token Dynamics

For a functional graph on a small state set:
- Floyd's cycle detection or Brent's algorithm: O(|S|) time and O(1) extra space.
- Period histogram: for each terminal SCC, count its size (= its period for a functional graph).

**Caveat:** period here is the period of the TOKEN trajectory, not of a full CA configuration.

---

## 5. Computable Procedures for Distinguishing Alternating vs. Paired Phases

The repo's v0 packet compared two update disciplines on the same ring-checkerboard support.
Here is the standard-math description of what is and is not computable:

### 5.1 Definitionally forced

If discipline A is defined as "apply two sub-steps per outer step" and discipline B as "apply
one sub-step per outer step," then period(A) = 2 * period(B) is a consequence of counting
operations, not of dynamical content.  This is computable and confirms implementation
correctness; it is not structural evidence.

### 5.2 Genuinely computable structural differences

- **Transient SCC count:** the number of SCCs that are not terminal.  This IS sensitive to
  the structure of the phase rule, because transient SCCs depend on which states collapse
  toward attractors — a property of the specific graph topology, not the step-count definition.
  In the v0 data: alternating transient counts 112/352/1216 vs. paired 64/128/256 at n=4/8/16,
  with a non-integer growing ratio (1.75, 2.75, 4.75).  This pattern is not predicted by the
  period identity and is genuine structural content.

- **Graph isomorphism test:** a complete test whether the two transition graphs, with states
  relabeled to remove discipline tags, are isomorphic.  More expensive (graph isomorphism is
  not known to be poly-time in general), but definitive.

- **Orbit-structure entropy:** entropy of the period histogram or basin-size distribution.

- **Control: label-permuted graph.**  Relabeling states (not discipline tag) should preserve
  structural metrics.  If it does not, the measurement was label-dependent.

---

## 6. Repo Relevance

**Primary packets:**

`system_v6/sims/ring_checkerboard_automaton_v0/` — the classical floor of the owner's
ring-checkerboard model.

**The single-token vs. full-configuration-space distinction** (Section 3.4 above) is the
binding caveat on this packet.  From the audit verdict (`audit_verdict.md` line 13-14):
"This is a single-active engine/readout-token transition graph over the support, not the full
cellular-automaton configuration space of all cells."

What the v0 packet computes:
- Transition graph of a SINGLE TOKEN moving on an owner-shaped support with local rules.
- SCC decomposition, terminal classes, basin partition — all in the single-token state space.
- These are genuine computable measurements, but they characterize the token trajectory, not
  the 2^n-configuration CA dynamics.

**The period-definitional lesson** (Section 3.5 above) is captured in the correction entry at
`owner_doctrine_cellular_automata_ring_checkerboard_20260611.md` lines 66-82:
"The period-2 vs period-4 headline is DEFINITIONALLY FORCED, not discovered."  The alternating
rule applies TWO phase updates per transition call; paired applies ONE — the ratio is an
algebraic identity.  The standard-math name for this: a result that follows from the definition
of the measured object (here: counting sub-steps) rather than from the structural properties of
the dynamics.  The corrected citation is the transient SCC topology difference.

**What would be needed to earn the full CA result:**
Per the standard definitions in Section 1 and the v0 audit's "QCA/index v1 requirements"
(audit_verdict.md lines 158-165):
1. Enumerate the full configuration space Q^n (feasible up to n ~ 20 for Q={0,1} with care).
2. Construct the full transition graph F: Q^n -> Q^n, not the single-token graph.
3. Show the two phase disciplines yield structurally distinct dynamics on Q^n (not just on
   the token state space).
4. Only then can block-bijectivity and reversibility be checked.

**On the brickwork normal-form connection:**
The doctrine receipt (`owner_doctrine_cellular_automata_ring_checkerboard_20260611.md` lines
15-19) aligns the ring-checkerboard two-phase update with the Margolus/brickwork scheme.  This
alignment is standard-math (LLM/Hermes alignment, not owner-source vocabulary — confirmed by
the provenance receipt's absence-of-grep finding).  The GNVW theorem would apply to a QCA
version of this rule IF the rule is:
- on a 1D qudit chain (the base ring satisfies this; the attached-ring nesting does not
  without a 1D embedding);
- translation-invariant (the owner's attached-rings-at-each-step structure is not translation-
  invariant unless all attachment points are identical);
- implemented as an explicit unitary/CPTP operator (not as a wire-count table).

Until all three hold, the GNVW index is a standard-math reference frame for what needs to be
built, not an applicable theorem.

`system_v6/sims/ring_checkerboard_qca_v1/` — the QCA attempt.  Audited as
`scratch_diagnostic_failed_adjudication_for_index_claim`.  The failure mode (audit_verdict.md
lines 28-34) is exactly Section 4.5's "this procedure can fail if the local rule was supplied
as metadata rather than as an operator."  The packet supplied wire-crossing counts as table
entries and read them back.  That computes `right_wires - left_wires` from the table, not
alpha(U) = dim(A_R)/dim(A_L) from the realized operator.

What v2 needs (doctrine entry, lines 91-94):
- Rules enter as local unitaries WITHOUT flow metadata.
- Index extracted by the genuine finite GNVW-class procedure over the realized operators'
  support algebras.
- Calibrations (+1/-1/0) that could fail.
- A gauge-invariance check that could fail (i.e. the check perturbs the actual operator,
  not a metadata field).

The **gauge/local-basis invariance** requirement (Section 2.3) is specifically the open gate:
for a genuine computation, changing the local basis (e.g. conjugating each qudit by a single-
site unitary) must leave alpha unchanged; the packet's current "invariance check" varies only
a metadata field and therefore cannot fail regardless of the underlying operator.

**Supporting packets:**
- `system_v6/foundations/two_engine_readout_automaton_20260609.md` — the structural ground
  for the alternating/paired distinction in the owner's model.  Deductive order = alternating
  period-2 readout; inductive order = paired period-4 readout.  This is the structural input
  to v0; the definitional-forcing lesson does not remove this structural grounding, it only
  restricts what the period measurement proves.

- `system_v6/sims/ring_checkerboard_support_graph_probe/` — the base-ring support graph
  diagnostic.  Scratch diagnostic for the graph structure (kappa coloring, V_inner/V_outer,
  phi0 gradient, ladder rows).  Not a CA dynamics packet; no SCC or basin computation.

**Open structural question not yet probed (from the negatives, Section 3.2):**
The owner's nested-ring structure (attached ring at each base-ring step) is not a uniform 1D
chain.  The bond-algebra analysis needed for GNVW would require either (a) an embedding of the
support into a 1D qudit chain with extra "internal" dimensions at each site, or (b) a different
formalism (e.g. the Kitaev/Haah index for network QCAs).  No Codex-Ratchet packet has yet
addressed this embedding question; it is a gating precondition for v2.

---

*provenance: standard-math results cited by author/year are recall-based standard references.
GNVW theorem: Gross, Nesme, Vogts, Werner 2012, Commun. Math. Phys. 310:419-454.
Margolus partition: Margolus 1984, Physica D 10:81-95.
Reversibility/bijectivity: Toffoli 1977, "Computation and construction universality of
reversible cellular automata"; Morita 2008 survey.
No claims beyond scratch research note.*
