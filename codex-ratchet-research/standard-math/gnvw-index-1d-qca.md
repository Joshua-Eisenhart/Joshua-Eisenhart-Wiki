# GNVW Index for 1D Quantum Cellular Automata

provenance-label: standard-math research note (recall-based; no live web access confirmed
available this session — items marked [recall] should be cross-checked against primary
sources before citing in a build card). Primary references: Gross, Nesme, Vogts, Werner
(2012), "Index theory of one dimensional quantum walks and cellular automata," Commun.
Math. Phys. 310:419-454; Fidkowski, Haah, Hastings (2019), "Exactly solvable model for a
deconfined quantum critical point in 1D," and related finite-ring discussions [recall];
Hastings (2004), Freedman et al., various.

date: 2026-06-11

---

## 1. The Object: 1D QCA on an Infinite Chain

### Informal description [recall]

A one-dimensional quantum cellular automaton (QCA) is a unitary map alpha on the algebra
of quasi-local observables of a 1D lattice system, satisfying:

- LOCALITY: alpha maps each local observable on a site (or bounded region) to an observable
  supported on a bounded neighborhood of that region. The locality radius r is the smallest
  integer such that alpha(A_X) is supported on the r-thickening of X for every finite X.
- TRANSLATION COVARIANCE: alpha commutes with the lattice translation by one site (for the
  standard index theory; relaxable for the partitioned/brickwork variant).
- UNITARITY: alpha is a *-automorphism of the quasi-local C*-algebra.

The prototypical example is a brickwork (partitioned / Margolus-style) circuit: pair up
sites as (0,1), (2,3), ..., apply a two-site unitary U to each pair (even phase), then
pair (1,2), (3,4), ... and apply V (odd phase). The result is a locality-radius-1 QCA.

### Quasi-local C*-algebra notation [recall]

The algebra of observables on the infinite chain is the inductive limit

    A = lim_{n->inf} M_{d^n}(C)

where d = local Hilbert space dimension. A region X carries a matrix algebra A_X =
M_{d^|X|}(C). A QCA alpha is automorphism satisfying alpha(A_X) subset A_{X+r} (where
X+r = the r-neighborhood of X).

---

## 2. The GNVW Index: Finite Definition via Support Algebras

### The key construction [Gross-Nesme-Vogts-Werner 2012, recall]

For a QCA alpha on a chain with local dimension d, fix a finite contiguous region L and its
complement R. Define:

    C_L = alpha(A_L) cap A_{L cup partial-right}   (the "right cross-algebra of L")
    C_R = alpha(A_R) cap A_{R cup partial-left}    (the "left cross-algebra of R")

More concretely, for a brickwork circuit:

- Choose the cut between sites n and n+1.
- The RIGHT support algebra of the cut is the subalgebra of alpha(A_{left half}) that
  "crosses" the cut to the right: the algebra of operators in alpha(A_L) that are not
  confined entirely to L (they have support on the right side of the cut).
- The LEFT support algebra is defined symmetrically for alpha(A_R).

### Rank computation [recall]

Each of C_L and C_R is a full matrix algebra (because alpha is unitary and local). Write:

    dim(C_L) = d^{k_R}    (right-crossing rank exponent)
    dim(C_R) = d^{k_L}    (left-crossing rank exponent)

These are always perfect powers of d when alpha is a finite-range QCA on a system with
local dimension d.

### The index [recall]

    ind(alpha) = dim(C_L) / dim(C_R) = d^{k_R - k_L}

Equivalently in log form:

    log_d(ind(alpha)) = k_R - k_L

This is the net number of "information channels" flowing right minus left per step.

Key properties:
- ind is a positive rational number (always a ratio of powers of d).
- ind = 1 (i.e., log-index = 0) for any QCA that is a finite-depth local unitary circuit
  (i.e., any product of local unitaries with bounded depth).
- ind(alpha composed with beta) = ind(alpha) * ind(beta).
- ind(alpha^{-1}) = 1 / ind(alpha).
- The index is gauge-invariant: conjugating alpha by any local unitary (onsite basis change
  or finite-depth circuit) does not change ind(alpha). This is the critical property that
  makes it an invariant rather than a coordinate-dependent quantity.

### Calibration rows [recall]

- RIGHT SHIFT by one site (alpha(A_j) = A_{j+1} for all j): ind = d (log-index = +1 in
  base-d units).
- LEFT SHIFT: ind = 1/d (log-index = -1).
- ANY finite-depth brickwork with no net flow: ind = 1 (log-index = 0).
- Onsite unitaries (alpha(A_j) = U A_j U* for fixed U): ind = 1.

---

## 3. The Quantization Theorem and Its Hypotheses

### Statement [recall, Gross-Nesme-Vogts-Werner 2012]

For a translation-invariant QCA on an infinite chain with local dimension d, the index
ind(alpha) is always a rational number of the form d^k for some integer k (positive,
negative, or zero). In particular:

- The index takes values in the discrete group Z (under log_d), not a continuum.
- This quantization is exact: there is no irrational index for a finite-locality QCA.
- The map ind: QCA -> Z is a group homomorphism (under composition).
- QCAs with ind = 0 (in log form) are exactly those in the identity connected component of
  the group of QCAs — they can be continuously deformed to the identity through local
  unitaries (this is the "triviality" characterization).

### Hypotheses (what the theorem requires) [recall]

1. INFINITE CHAIN: the quantization proof uses properties of the quasi-local C*-algebra of
   an infinite system. The proof proceeds by showing C_L and C_R are full matrix algebras
   whose dimensions must be integral powers of d — this uses that the algebras are
   irreducible and complete over the whole semi-infinite chain.
2. FINITE LOCALITY RADIUS r: alpha must satisfy alpha(A_X) subset A_{X+r} for a fixed
   finite r. Without this, "support algebra" is not well-defined.
3. TRANSLATION INVARIANCE (for the simplest form): the standard statement assumes
   translation-invariant QCAs. Translation invariance is not strictly required for the
   index to be definable (it can be defined for single QCAs without translation
   invariance), but the full classification result — that QCAs are classified up to
   finite-depth circuits by the index — uses translation invariance.
4. UNITARITY: alpha must be a unitary (*-)automorphism. For CPTP maps (channels), there is
   no direct GNVW index; the theory applies to unitary QCAs.

### What breaks on finite rings (DECISIVE for the repo)

This is the critical subtlety. On a FINITE PERIODIC ring of N sites:

a) TRIVIALITY OF THE INDEX: every unitary QCA on a finite ring has trivial (=1) index.
   Reason: on a finite ring there is no meaningful "left half vs right half" of an infinite
   chain; the cut between L and R wraps around. The support algebra C_L ends up being the
   full matrix algebra of the left-crossing part, but the ring closure means
   alpha(A_L) already sees all of A — the left and right crossing ranks equal each other
   for any unitary automorphism of a finite-dimensional algebra (a unitary on a finite ring
   is just a unitary conjugation on M_{d^N}(C), which is always an inner automorphism up
   to relabeling — Skolem-Noether). So the ratio is always 1 on a finite ring.

b) WHAT THIS MEANS OPERATIONALLY: you CANNOT distinguish a right-shifting QCA from a
   left-shifting QCA using a well-defined GNVW index on a finite ring. Both give index 1
   (trivial). The chirality/flux information is "hidden" in the global permutation, not
   detectable by local support-algebra methods.

c) THE CORRECT FINITE-RING SUBSTITUTE: to recover chirality information on a finite ring,
   one must either:
   - Use the WINDING NUMBER / PERMUTATION CHARACTER of the global action on the state
     space (classifiable by the net cycle structure of the shift permutation, not by local
     algebra supports).
   - Embed the finite ring in a larger system or use a "twisted" boundary condition
     where the boundary term explicitly breaks the periodicity.
   - Directly count net left-vs-right wire flows in the brickwork circuit, which is a
     property of the CIRCUIT DESCRIPTION (the rule table), not an invariant of the
     implemented automorphism class. This is exactly the failure mode of ring_checkerboard_qca_v1
     (see section 6 below).

d) PARTIAL RESCUE — FINITE BRICKWORK CONVENTION [recall, Freedman, Haah, Hastings variants]:
   For a brickwork (partitioned Margolus) circuit on a finite ring, the index can be
   defined AS A PROPERTY OF THE CIRCUIT PRESENTATION (not the automorphism class) by
   counting the crossing wires at the cut in the specific two-phase decomposition. This is
   a real, computable number, but it is:
   - NOT invariant under all local changes of basis (it can change if you absorb a
     gate from one phase into the other, or if you pick a different factorization into
     even/odd phases).
   - NOT an automorphism-class invariant on a finite ring (because the automorphism group
     of a finite-dimensional matrix algebra is trivial by Skolem-Noether — all inner).
   So "circuit-presentation index" and "GNVW automorphism index" are the same thing on an
   infinite chain but DIVERGE on a finite ring. On a finite ring, only the
   circuit-presentation form survives as a useful quantity, and it is a property of how you
   WROTE the circuit, not of what the circuit DOES to states.

---

## 4. Computable Procedure for a Finite Brickwork Circuit

This is the procedure that a finite sim can actually execute. Items marked (!) are places
where the finite-ring subtlety bites.

### Step 1: Fix the circuit and the cut

Given a brickwork (two-phase partitioned) unitary circuit U on N qudits of dimension d
arranged in a ring (or open chain):
- Phase A: gates {U_{0,1}, U_{2,3}, ...} acting on even-odd pairs.
- Phase B: gates {U_{1,2}, U_{3,4}, ...} acting on odd-even pairs.
- Fix a cut site c between site c and site c+1.

### Step 2: Extract the crossing unitary

At the cut, exactly ONE gate from each phase crosses the cut: in phase A, the gate on pair
(c-1, c) or (c, c+1) depending on parity; in phase B, the other boundary gate. The gate
that crosses the cut has a d x d block that maps "left of cut" modes to "right of cut"
modes. Write this d x d block as the "crossing sub-matrix."

### Step 3: Compute support-algebra ranks

For an ideal infinite-chain GNVW computation:
- C_R (right cross algebra) = the algebra generated by alpha(A_L) acting on the right half.
  Its dimension is d^{k_R} where k_R is the number of "right-going wire channels."
- C_L (left cross algebra): dimension d^{k_L}.

For a BRICKWORK CIRCUIT on an infinite chain, k_R and k_L equal the number of d-dimensional
wires in the circuit that cross the cut going right and left respectively. For a simple
two-site gate U_{c,c+1}: k_R = 1 (one d-dim wire crosses right), k_L = 1 (one crosses
left) when the gate couples both sides; the difference k_R - k_L depends on how many wires
are "net rightward" vs "net leftward" — this is zero for a non-shifting gate and +1/-1 for
a shift.

For a FINITE RING (!): step 3 must be done via the circuit presentation, not via
automorphism theory. The rank computation is:
- Extract the unitary matrix U_total in the full d^N Hilbert space.
- Trace out the left half: compute the partial trace / Schmidt decomposition at the cut.
- The right-going rank k_R = log_d(rank of the reduced state of the right half after
  applying U_total to a maximally entangled input state on the left half).

This is well-defined but gives the CIRCUIT-PRESENTATION index, not the automorphism-class
index. On a finite ring, all nonzero automorphism-class indices collapse to the trivial
value (see section 3d). (!)

### Step 4: Compute the ratio

    index_ratio = d^{k_R} / d^{k_L}
    signed_log_index = k_R - k_L

For a right shift: k_R = 1, k_L = 0, signed_log_index = +1.
For a left shift: k_R = 0, k_L = 1, signed_log_index = -1.
For a non-shifting two-site gate: k_R = k_L, signed_log_index = 0.

### Step 5: Gauge invariance check (the failing gate)

Apply a local basis change (onsite unitary V_c on site c) to the circuit. Recompute k_R
and k_L via the same procedure. The GNVW index must not change.

On an infinite chain: this is guaranteed by the theorem — the ratio is an automorphism
invariant.
On a finite ring with circuit-presentation index: gauge invariance is NOT guaranteed.
Changing the basis at the cut can absorb a wire into a different phase, changing k_R or k_L.
A sim that only changes a metadata field ("basis = rotated") without recomputing the
actual crossing matrices has NOT performed a gauge invariance check. This is a critical
failure mode: the check must recompute the partial trace / Schmidt rank at the new cut with
the new circuit, not just re-read a stored wire-count table.

### Step 6: Calibration rows (required)

Any honest finite sim must include:
- right_shift (the N-site cyclic permutation rightward): signed_log_index must equal +1.
  On a finite ring, this is the one case where the circuit-presentation index is
  unambiguous (the shift has no local gate description — it IS a shift, globally).
- left_shift: signed_log_index must equal -1.
- onsite_unitary (any local V at every site): signed_log_index must equal 0.
- paired_block gate (identity times identity, no net flow): signed_log_index must equal 0.

These calibrations can fail if the computation is wrong. If the calibrations are
passed in directly as a wire-count table (not recomputed from the implemented operators),
they do not constitute earned calibrations.

---

## 5. Negatives: What the Index Cannot Do, and Where It Is Undefined

### 5a. Cannot distinguish within the trivial class

Two finite-depth local unitary circuits (both with index 0) can be topologically distinct
in ways the GNVW index does not see. For example:
- Two distinct non-trivial finite-depth circuits with the same index are not distinguished.
- In higher dimensions (2D+), the index theory breaks down entirely: there exist 2D QCAs
  with trivial GNVW-like invariants that are NOT finite-depth circuits (e.g., from
  invertible topological phases). The GNVW theory is specific to 1D.

### 5b. Undefined for CPTP maps (channels)

The GNVW index is defined for UNITARY (*-)automorphisms. For quantum channels (CPTP maps
that are not unitary), the support algebra construction does not apply directly. An
extension to "approximately unitary" QCAs is possible but technically harder and requires
additional assumptions [recall].

### 5c. Undefined for non-local rules

If the update rule has unbounded locality radius, the support algebra C_L is no longer a
finite-dimensional matrix algebra and the rank computation is undefined. Any finite-range
approximation introduces an error in the index computation.

### 5d. The finite-ring triviality [DECISIVE]

As stated in section 3: on a finite periodic ring, the automorphism-class index is always
trivial. The circuit-presentation variant survives but is:
- Dependent on which phase you call "even" and which "odd" (the factorization is not
  canonical for an arbitrary QCA; it IS canonical for a standard brickwork circuit with
  a fixed phase labeling).
- Not invariant under local basis change at the cut (see step 5 above).
- Not a topological invariant of the realized dynamics on the ring; it is a property of
  the circuit DESCRIPTION.

Implication: a sim on a finite ring that computes the "index" by reading a wire-count
table embedded in the rule definition and calling it an invariant is computing the circuit
description index without checking that the same number would emerge from a genuinely
different factorization or a genuine local-basis reparameterization. If it passes in
right_wires=1 and left_wires=0 and reads back signed_log_index=1, it has not shown that
the number 1 is an invariant of the realized quantum channel — only that the rule was
written with those flow parameters.

### 5e. Sensitivity to boundary conditions

On a finite open chain (not a ring): the index can sometimes be extracted from the Schmidt
rank at the boundary, and it is more well-defined because the two ends are genuinely
separate. On a periodic ring: the circuit wraps around and boundary effects compound.
The ring is the harder case.

### 5f. Does not classify all 1D QCA in finite dimensions

For systems with matrix-product-operator (MPO) representations, there are additional
invariants beyond the GNVW index (e.g., the "beta invariant" from group cohomology H^1(Z,
U(1)) when the QCA has a symmetry group). The GNVW index alone does not classify all 1D
QCAs with symmetry [recall].

---

## 6. Repo Relevance: Codex-Ratchet Packets

### ring_checkerboard_qca_v1 (REJECTED, failed adjudication)

Path: `system_v6/sims/ring_checkerboard_qca_v1/audit_verdict.md`

The audit verdict is: REJECT for the index claim. The exact failure mode is the
finite-ring circuit-description problem described in sections 3d and 5d above.

Concretely, from the audit:
- `ring_checkerboard_qca_v1_common.py:163` computes
  `raw_index_fraction = Fraction(QUBIT_DIM**right_wires, QUBIT_DIM**left_wires)`.
- The wire counts `right_wires` and `left_wires` are SUPPLIED IN THE RULE TABLE, not
  extracted from a realized QCA operator via partial trace / Schmidt rank computation.
- `index_table()` in `ring_checkerboard_qca_v1_common.py:210-295` manually constructs rows
  with preset wire counts: right shift (1,0), left shift (0,1), onsite (0,0), etc.
- The JAX and PyTorch legs validate the table values, not derive them from operators.
- The Julia leg hard-codes the shorter index table directly.

This is the "circuit-description index read-back" failure: the number emerged from the
circuit design (flow metadata), not from a computation on the realized operator. As the
audit states: "a value forced by the realization choices, not discovered from the rule."

The gauge-invariance check fails for the same reason: the "basis" field was metadata
that the index function ignores. A genuine gauge check requires recomputing the crossing
rank after applying a local unitary to the circuit, not just relabeling a stored field.

The GNVW section of this note explains WHY this failure was predictable from the theory:
on a finite ring, the circuit-description index and the automorphism-class index diverge,
and only a genuine crossed-rank computation from the realized operators distinguishes them.

### The v2 design rule (binding)

From `owner_doctrine_cellular_automata_ring_checkerboard_20260611.md`, the correction entry
at lines 88-94:

> The v2 design rule (binding): rules enter as local unitaries WITHOUT flow metadata; the
> index is extracted by the genuine finite GNVW-class procedure over the realized operators'
> support algebras, with calibrations (+1/-1/0) that could fail and a gauge-invariance
> check that could fail.

This note provides the standard-math backing for why each element of that rule is
necessary:

- "rules enter WITHOUT flow metadata": eliminates the v1 failure mode where wire counts
  were supplied and read back. The index must emerge from the operator, not be injected.
- "genuine finite GNVW-class procedure": means partial trace / Schmidt decomposition at
  the cut on the actual implemented unitary (not the rule table), using the circuit
  decomposition into even/odd phases with a fixed cut.
- "calibrations (+1/-1/0) that could fail": shift circuits must be implemented as genuine
  shift unitaries (cyclic permutation matrices or equivalent), and the crossing-rank
  computation must return +1/-1/0 respectively. If it returns the wrong value, the
  computation is broken — the calibration is a real test, not a table-lookup.
- "gauge-invariance check that could fail": apply a local basis change V at the cut site
  (i.e., replace the circuit U by (I otimes...otimes V otimes...otimes I) U (I
  otimes...otimes V* otimes...otimes I)), recompute the crossing ranks from the new
  circuit. The index must be unchanged. On a finite ring with a circuit-presentation
  index, this CAN fail if the basis change changes the phase structure.

### Finite-ring caveat for v2

The v2 packet will still operate on a finite ring (the committed support is finite
periodic). The design rule requires honest handling of the following:

a) The computed quantity is the CIRCUIT-PRESENTATION index on the finite ring, not the
   automorphism-class index. Label it as such.
b) The gauge-invariance test should use a specific LOCAL UNITARY at a specific site, not
   global re-labeling. The test is: does the circuit-presentation index change when a
   single onsite unitary is inserted at the cut? For an ideal infinite chain, the answer
   is always no. For a finite ring, the answer depends on how the circuit phases interleave
   at the boundary. A failing gauge test on a finite ring is informative (it means the
   circuit-presentation index is phase-convention-dependent at the cut); a passing gauge
   test is evidence (not proof) of robustness.
c) The shift calibration on a finite ring requires the cyclic shift permutation to be
   implemented as a genuine unitary (the N x N permutation matrix in the computational
   basis, or its d^N x d^N lift to the full Hilbert space), with k_R extracted from the
   Schmidt rank of the partial trace. Not from a stored k_R = 1 field.

### Connection to L/R flux doctrine (O1)

The doctrine receipt registers the expectation that L/R engine types carry opposite index
signs (+1 for R, -1 for L). From the standard math: this is the claim that the two engine
types, realized as local unitary circuits on the ring support, have crossing-rank
computations that give k_R - k_L = +1 and k_R - k_L = -1 respectively. For this to be
an earned claim:
- Both circuits must be implemented as genuine local unitaries (not flow tables).
- The partial trace / Schmidt rank computation must give the appropriate crossing ranks.
- The index-0 control (a non-chiral circuit) must give k_R = k_L.
- The calibration (right shift = +1, left shift = -1, onsite = 0) must all pass.

If all four conditions hold, the L/R opposite-index expectation is earned as a
computable chirality invariant for those specific circuit realizations on the finite ring
(with the finite-ring caveat: it is circuit-presentation, not automorphism-class).

### ring_checkerboard_automaton_v0 (classical floor, earned at corrected scope)

Path: `system_v6/sims/ring_checkerboard_automaton_v0/`
Doctrine path: `system_v6/receipts/owner_doctrine_cellular_automata_ring_checkerboard_20260611.md`

The classical floor is earned at the corrected (narrower) scope after the 28fc221a1
correction: the genuine structural result is the TRANSIENT SCC TOPOLOGY difference between
alternating and paired update phases (ratios 1.75, 2.75, 4.75 at sizes n=4/8/16 — growing,
non-integer, not predictable from the period identity). The period-2 vs period-4 headline
is an implementation identity, not a discovered result.

The GNVW index theory is irrelevant to the classical floor — the v0 packet is purely
classical. The index theory becomes relevant at v1+ where a genuine quantum rule is
implemented. The standard-math note above applies to the QCA/index gate, which opened
after the classical floor was earned.

---

## 7. Alternatives and Open Questions (nominalist/empiricist register)

### Alternative index definitions that survive on finite rings [recall]

- WINDING NUMBER OF THE PERMUTATION: for a classical CA on a finite ring (bijective rules),
  the net displacement of the rule's permutation action on configurations. For the quantum
  version, replace with the winding number of the unitary's action on state labels. This
  survives on finite rings but is hard to compute and depends on the full N-body state
  space, not just the local circuit.
- TRANSFER MATRIX TOPOLOGICAL INDEX: for translation-invariant QCAs, the transfer matrix
  of the quantum walk has a winding number in K-theory / K_1(C(S^1)). This is the
  mathematical object behind the GNVW index at the C*-algebra level [recall, Gross et al.].
  It requires the infinite chain for the full invariant.
- PARTIAL TRACE RANK ON AN OPEN CHAIN: on an OPEN finite chain (not a ring), the crossing
  rank at each interior cut is a well-defined quantity and equals the GNVW index of the
  corresponding infinite-chain QCA for a brickwork circuit. This is the cleanest finite
  computable version — it avoids the ring closure problem.

### What remains open in the standard theory [recall]

- Classification of 1D QCAs with symmetry beyond translation invariance: the GNVW index
  is a complete invariant for the group of all 1D QCAs modulo finite-depth circuits, but
  for QCAs with an additional symmetry group G, the classification involves G-equivariant
  K-theory and is not fully worked out for all G.
- Extension to 1D CPTP dynamics (open QCAs): no index theory in the unitary sense; the
  analog uses completely positive semigroup generators.
- Computability gap: for a general (non-brickwork) QCA with locality radius r > 1, the
  support algebra computation requires exponentially large matrices (d^{2r+1} x d^{2r+1}
  blocks). The brickwork case is the tractable one — crossing rank = the rank of a d x d
  matrix, computed in polynomial time.

### Alternatives the repo should consider for v2

If the goal is a computable chirality invariant that is genuinely invariant (not
circuit-description-dependent) on a finite ring, the strongest options are:
1. Use an OPEN CHAIN instead of a ring. The crossing rank at an interior cut is well-defined
   and equals the GNVW index. This avoids all finite-ring subtleties.
2. Use the WINDING NUMBER of the shift permutation on the N-site state space for the
   classical baseline, then extend to the quantum case via the Schmidt rank on an open chain.
3. Accept that the computed quantity on a finite ring is a CIRCUIT-PRESENTATION index
   (phase-convention-dependent, not automorphism-invariant), label it as such in every
   result row, and include a genuine gauge check that could fail (not a metadata relabeling).

Option 3 is the minimal repair; option 1 is the cleanest from a standard-math standpoint.
The v2 design rule as written is compatible with any of these, as long as the computation
genuinely extracts the crossing rank from the implemented operators.
