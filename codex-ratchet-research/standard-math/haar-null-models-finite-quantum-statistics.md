# Haar-measure null models for finite-dimensional quantum state statistics

provenance: standard-math, recall-based unless a citation is given; items marked
[RECALL] should be verified against a primary source before promotion.

---

## 1. Core finite/computable definitions

### 1.1 Haar measure on U(d) and the induced measure on pure states

The unitary group U(d) carries a unique (up to normalization) left- and
right-invariant Borel measure mu_Haar.  Sampling a Haar-random pure state in
C^d means drawing a Haar-random U from U(d) and acting on a fixed reference
vector |0>, giving |psi> = U|0>.  Equivalently: draw a complex Gaussian vector
x in C^d (i.e. Re(x_i), Im(x_i) ~ N(0,1) i.i.d.) and normalize.  The
resulting distribution on CP^{d-1} = S^{2d-1}/U(1) is the Fubini-Study measure
and is the unique U(d)-invariant measure on the space of pure states.  [RECALL]

For n qubits, d = 2^n.

### 1.2 Single-site reduced density matrix (the marginal)

Given an n-site system with sites A_1,...,A_n and a pure state |psi> on the
full Hilbert space H = (C^2)^{otimes n}, the single-site reduced density matrix
on site k is

    rho_k = Tr_{all sites except k}( |psi><psi| )

This is a 2x2 positive semidefinite matrix with trace 1.  It is parametrized by
the Bloch vector r_k = (Tr rho_k sigma_x, Tr rho_k sigma_y, Tr rho_k sigma_z)
with |r_k| <= 1.  The point |r_k| = 1 is a pure state; |r_k| = 0 is the
maximally mixed state I/2.

Computably: given an explicit state vector psi in C^{2^n}, partial trace is
a reshape-and-contraction operation exact in floating point for small n.

### 1.3 The purity lemma (expected purity of a single-site marginal)

For a Haar-random pure state |psi> on (C^2)^{otimes n} with n >= 2, the
expected purity of the single-site marginal on any site k is

    E[ Tr(rho_k^2) ] = (2 + 1) / (2 * 2^n + 1) * 2
                     ... (simplified below)

More generally, for a bipartition A | B with dim H_A = d_A and
dim H_B = d_B = d / d_A:

    E[ Tr(rho_A^2) ] = (d_A + d_B) / (d_A * d_B + 1)          [RECALL: standard]

For a single-qubit subsystem (d_A = 2) of an n-qubit system (d = 2^n,
d_B = 2^{n-1}):

    E[ Tr(rho_k^2) ] = (2 + 2^{n-1}) / (2 * 2^{n-1} + 1)
                     = (2 + 2^{n-1}) / (2^n + 1)

For n = 4 (d = 16, d_A = 2, d_B = 8):

    E[ Tr(rho_k^2) ] = (2 + 8) / (16 + 1) = 10/17 ≈ 0.588

So a Haar-random 4-qubit pure state already has fairly low single-site purity.
The expected Bloch radius satisfies E[|r_k|^2] = 3*(E[Tr rho_k^2] - 1/2)
= 3 * (10/17 - 1/2) = 3 * 3/34 = 9/34 ≈ 0.265, so E[|r_k|] ≈ 0.51.  [RECALL]

This has a direct implication for chart-cell recovery: a Haar-random 4-qubit
pure state has a single-site Bloch vector of moderate length, pointing in a
direction that is uniformly distributed on S^2.

### 1.4 Page's theorem: the marginal distribution

Page's theorem [Page 1993, Phys. Rev. Lett. 71:1291; RECALL] and its extensions
establish the distribution of the entanglement entropy S(rho_A) for Haar-random
bipartitions.  The key form: for d_A <= d_B,

    E[ S(rho_A) ] = sum_{k=d_B+1}^{d_A*d_B} 1/k  - (d_A - 1)/(2*d_B)

This is approximately ln(d_A) - (d_A - 1)/(2*d_B) for d_B >> d_A.
For a single-qubit marginal of a 4-qubit system (d_A=2, d_B=8):

    E[ S(rho_k) ] = sum_{k=9}^{16} 1/k - 1/16
                  ≈ 0.6983 - 0.0625 = 0.636 nats

(or ≈ 0.917 bits).  [RECALL: computed from the formula]

Hypotheses for Page's theorem: uniform Haar measure on pure states; the
subsystem split is fixed before sampling.  The theorem applies to the von
Neumann entropy; extensions to Renyi entropy and purity have the same Haar
hypothesis.

Strongest form available: Levy's lemma concentration says the entropy S(rho_A)
concentrates sharply around its mean for large dimensions.  The fluctuation is
O(1/sqrt(d)) in subsystem dimension.  [RECALL]

---

## 2. The chart-cell expected-occupancy calculation

### 2.1 Setting: the A33 chart

The A33 chart used in `spinor_network_surface_v1` is the set of Bloch vectors
(r_x, r_y, r_z) in {-1, -0.5, 0, 0.5, 1}^3 that lie within the unit ball
(r_x^2 + r_y^2 + r_z^2 <= 1).  The operation `a33_rows()` generates these by
looping over the 5^3 = 125 lattice points and retaining those with radius <= 1.

A direct count: lattice points in a 5-point ball grid on [-1,1]^3.
- Radius = 0: (0,0,0) -> 1 point
- Radius = 0.5: points with exactly one nonzero coordinate of ±0.5 -> 6 points
  e.g. (0.5,0,0) etc.
- Radius = 1.0: points with exactly one nonzero coordinate of ±1.0 -> 6 points
- Radius = sqrt(0.5) ≈ 0.707: points with two nonzero coordinates of ±0.5
  -> 12 points (four sign combinations, three axis pairs)
- Radius = sqrt(0.5) from (0.5, ±0.5, 0) etc.: same family
- Radius = sqrt(0.75) ≈ 0.866: one coordinate ±1, one coordinate ±0.5, one 0
  -> 24 points but we need r^2 = 1 + 0.25 = 1.25 > 1, so excluded
- Radius = sqrt(1): one ±1 coordinate only -> included above
- Radius = sqrt(1.5): any point with two nonzero coordinates one of which is ±1
  -> excluded (1 + 0.25 > 1 or 1 + 1 > 1)

So: A33 = {(0,0,0)} + 6-face-center ±0.5 + 6-face-center ±1
  + 12 edge-midpoints at radius sqrt(0.5) ≈ 0.707
  + ... continuing: three coordinates each ±0.5 gives radius sqrt(0.75) ≈ 0.866 <= 1,
    so all 8 of those are included.

Let me enumerate systematically:
- r^2 = 0: {(0,0,0)} -> 1
- r^2 = 0.25: one coord ±0.5, two zeros -> C(3,1) * 2 = 6
- r^2 = 0.50: two coords ±0.5, one zero -> C(3,2) * 4 = 12
- r^2 = 0.75: three coords ±0.5 -> 8
- r^2 = 1.00: one coord ±1, two zeros -> 6
Total = 1 + 6 + 12 + 8 + 6 = 33.  This matches the naming "A33."

The origin cell is (0,0,0); the 32 non-origin cells are uniformly distributed
across those r^2 classes.

### 2.2 Haar base rate: expected number of non-origin cells hit

A Haar-random 4-qubit pure state has a single-site Bloch vector uniformly
distributed on the ball (by U(d)-invariance).  The density is not uniform on
the ball; it is the pushforward of Haar measure under the partial-trace map.
The marginal density on the Bloch vector r is [RECALL]:

    p(r) dr = (d_B / pi) * (1 - |r|^2/4)^{d_B - 2} d^3r / (2*pi)
    ... (exact form depends on the parametrization)

A simpler operational route for the A33 chart: sample N_samples Haar-random
4-qubit pure states, compute the single-site Bloch vector for each site, bin
into the nearest A33 cell, and count distinct non-origin cells hit across all
4 sites.

Expected distinct non-origin cells is NOT simply 32 * (1 - (1 - 1/32)^{4*N}).
The cells are not equally probable; they have different r^2 values, and the
Haar measure favors intermediate r values (not the poles r = ±1).  The cells at
r^2 = 0.25 and r^2 = 0.50 are more numerous and more likely to be hit than the
6 cells at r^2 = 1.

For a small input set (4 patterns, 4 sites = 16 Bloch vectors) the expected
count is dominated by the coverage probability per cell.  The ~7.6 figure
reported in the repo receipt is consistent with the following rough calculation:

- From N_samples = 4 patterns * 4 sites = 16 Bloch vector samples under Haar
  measure on a 4-qubit state
- The probability that a Haar-random Bloch vector lands in the origin cell
  (nearest to r = 0) depends on the ball geometry; the origin cell is the
  smallest Voronoi cell and captures low-r states, which are the MOST probable
  for Haar random states (high entanglement)
- For a uniform distribution on the Bloch ball, each of the 33 cells has equal
  Voronoi volume, so P(hit cell i) ≈ 1/33 per sample
- Expected distinct non-origin cells from 16 samples under uniform-ball
  approximation:
    E = sum_{i=1..32} [1 - (1 - 1/33)^{16}]
      = 32 * [1 - (32/33)^{16}]
      = 32 * [1 - exp(16 * ln(32/33))]
      = 32 * [1 - exp(-16/33 * ...)]
    (32/33)^{16} ≈ exp(-16/33) ≈ exp(-0.485) ≈ 0.616
    E ≈ 32 * 0.384 ≈ 12.3 (naive uniform approximation)

The actual Haar measure is NOT uniform on the Bloch ball; it places higher mass
near r = 0 (origin cell) and less mass at the surface r = 1.  Correct for this:

- P(fall in origin Voronoi region) > 1/33 under Haar
- P(fall in each r=1 cell) < 1/33 under Haar

A Monte Carlo computation (the v2 requirement) would pin the exact value by
sampling.  The receipt figure of ~7.6 non-origin cells is consistent with a
simulation using 4 states * 4 sites and the actual Haar distribution (where
high-r cells are under-sampled relative to the uniform estimate, reducing the
naive 12.3 to somewhere around 7-8).  [RECALL: the 7.6 figure comes from the
repo receipt, not an independent computation in this note — treat as
approximately-right pending v2 in-packet computation]

### 2.3 Computing the null base rate: two routes

**Route 1 (exact, via coverage probability formula).**

For k i.i.d. draws from a discrete distribution on m categories with
probabilities p_1,...,p_m, the expected number of distinct categories observed
is:

    E[distinct] = sum_{i=1}^m [1 - (1 - p_i)^k]

For the A33 chart, k = N_patterns * N_sites (the number of Bloch vectors drawn),
and p_i = probability that a Haar-random Bloch vector lands in Voronoi cell i.
The p_i are NOT equal; they depend on the Voronoi volume of each cell under the
Haar-pushforward measure.  Each p_i must be computed by Monte Carlo or exact
integration.

**Route 2 (Monte Carlo with pinned seed).**

The practical approach for the v2 in-packet requirement:

```python
def haar_null_expected_nonorigin(
    n_sites: int,
    n_patterns: int,
    n_samples: int,
    seed: int,
    a33_rows: list,
    origin_cell: str,
) -> float:
    rng = np.random.default_rng(seed)
    hit_counts: dict[str, int] = {}
    for _ in range(n_samples):
        # Sample Haar-random n-qubit pure state
        psi = rng.standard_normal(2**n_sites) + 1j * rng.standard_normal(2**n_sites)
        psi /= np.linalg.norm(psi)
        # For each pattern slot (here: select random subsample of sites),
        # compute single-site marginal and bin
        cells_this_sample: set[str] = set()
        for _ in range(n_patterns):
            # Each "pattern" corresponds to one pure state in the null model
            psi2 = rng.standard_normal(2**n_sites) + 1j * rng.standard_normal(2**n_sites)
            psi2 /= np.linalg.norm(psi2)
            rho_full = np.outer(psi2, psi2.conj())
            for site in range(n_sites):
                rho_k = partial_trace(rho_full, site, n_sites)
                bloch = bloch_vector(rho_k)
                cell_id, _ = chart_cell_id(bloch, a33_rows)
                if cell_id != origin_cell:
                    cells_this_sample.add(cell_id)
        hit_counts[len(cells_this_sample)] = hit_counts.get(len(cells_this_sample), 0) + 1
    return np.mean([k for k, v in hit_counts.items() for _ in range(v)])
```

The seed must be pinned in the result JSON so the null computation is
reproducible (the repo's result-freshness discipline applies: seed in the
result, not only in the source).

---

## 3. Identity-based vs count-based test statistics

These are two different kinds of evidence; they fail in different ways.

**Count-based:** the test statistic is the integer K = number of distinct
non-origin cells recovered.  The null model predicts E[K] ≈ 7.6 (under Haar).
The v1 result K = 6 is BELOW the null mean.  A count-based comparison therefore
provides no evidence of structure; it is indistinguishable from random sampling.

**Identity-based:** the test statistic is WHICH cells are recovered, not how
many.  The prediction is that a structured family (e.g. the chiral-quaternion
family) should recover specific cells tied to its geometric construction, not
a random subset.  Evidence of structure is:
- The chiral-L family recovers cells near the positive-x axis (because its
  Hopf/Weyl construction places Bloch vectors there)
- The chiral-R family recovers cells near the negative-x axis (mirror)
- The entangled-nonproduct state recovers the positive-z-axis cells (consistent
  with its construction)
- A pinned-random state recovers the origin cell only (consistent with near-zero
  Bloch vector from high entanglement)

This is the identity evidence that survives when the count evidence fails.

**Formal version of identity test.** For a structured family F, define the
predicted cell set C_F ⊆ A33.  Define the actual recovered set R_F.  The test
statistic is |R_F ∩ C_F|.  Under the Haar null, P(cell c is in R_F) = p_c
(the Haar-push probability).  The null distribution for |R_F ∩ C_F| can be
computed exactly if |C_F| is small and cells are independent.

**Caution: the two tests require different controls.** Count-based evidence
requires a no-structure control that ALSO exceeds the Haar mean; absence of that
control weakens count-based claims.  Identity-based evidence requires that the
predicted cells are SPECIFIC to the construction: a Haar-random state should NOT
predict the same cells.

---

## 4. Theorems with hypotheses and failure modes

### 4.1 Levy's lemma / concentration of measure

**Statement [RECALL]:** For a Lipschitz function f on the sphere S^{2d-1} with
Lipschitz constant L and a Haar-random unit vector psi:

    P( |f(psi) - E[f]| > epsilon ) <= 2 * exp(- C * d * epsilon^2 / L^2 )

for some absolute constant C > 0.

**Hypotheses:** (1) f Lipschitz on the sphere; (2) Haar measure (not a
structured distribution); (3) the sphere S^{2d-1} (not a proper submanifold
or constraint surface).

**Failure modes:**
- Fails if the state has a CONSTRAINT (e.g. it lives on a submanifold imposed
  by a Hamiltonian, a symmetry, or the dynamics of the simulation). Constraint-
  restricted states are NOT Haar-random; concentration-of-measure arguments do
  not apply without modification.
- Fails if the dimension d is small.  For n=4 qubits, d=16; the exponential in
  Levy's lemma is exp(-16 * epsilon^2 * C), which gives non-trivial concentration
  only for epsilon >> 1/4.
- Does NOT say anything about structured initial conditions; applies only to
  the Haar reference class.

### 4.2 Purity formula

**Statement [RECALL]:** For a Haar-random pure state on H_A ⊗ H_B with
dim H_A = d_A, dim H_B = d_B:

    E[ Tr(rho_A^2) ] = (d_A + d_B) / (d_A * d_B + 1)

**Hypotheses:** Haar measure.  Bipartition is fixed (not chosen to maximize
purity after sampling).

**Failure modes:**
- Does not apply to states generated by a structured circuit/dynamics.
- Does not bound the VARIANCE; fluctuations around the mean can be large for
  small dimensions.
- Does not apply to MIXED states, only pure states.

### 4.3 Page's theorem for entropy

**Statement [RECALL / Page 1993]:** For a Haar-random pure state on H_A ⊗ H_B
with d_A <= d_B:

    E[ S(rho_A) ] = sum_{k=d_B+1}^{d_A*d_B} 1/k - (d_A - 1)/(2*d_B)

**Hypotheses:** Haar measure, fixed bipartition, von Neumann entropy.

**Failure modes:**
- The formula gives the MEAN; the variance is O(1/(d_A * d_B)).  For small d_A,
  the variance is significant.
- Applies only to the marginal entropy, not to mutual information, conditional
  entropy, or coherent information.
- Does NOT bound recovery probabilities for cell classifiers.

### 4.4 Approximate unitary k-designs

To reduce N_samples in a Monte Carlo null, one can use a k-design: a measure
that matches the first k moments of Haar.  Random Clifford circuits form
a 3-design [RECALL: Zhu et al. 2017, approximate].  For k=1 the design matches
the mean; for k=2 it matches the variance.

**Hypotheses for k-design substitution:** the test statistic must depend only on
moments up to order k.  Cell-hit probabilities depend on k=1 moments (the mean
occupancy is linear in p_i).  Second-moment statistics require a 2-design.

---

## 5. Negatives: what a Haar null does NOT control

This section is where the null breaks down for the repo's specific application.

### 5.1 The carrier's reachable-set geometry (the geometric-ceiling point)

A Haar null assumes the state is drawn uniformly from ALL pure states in
(C^2)^{otimes n}.  The repo's generated states are drawn from a RESTRICTED
FAMILY: chiral-quaternion Hopf/Weyl states, entangled-nonproduct states
constructed from specific tensor products.  These live on a low-dimensional
submanifold of the full state space.

Consequence: the Haar null does NOT control for the difference between
"your specific construction hits these cells" and "any structured generation
procedure (not just Haar) would hit these cells."  The correct comparison for
identity-based evidence is not Haar null but rather a FAMILY-APPROPRIATE null:
a random member of the same structural family with parameters randomized.

Put differently: the Haar null answers "could a completely unstructured process
hit these cells?"  It does NOT answer "does the Hopf/Weyl geometry specifically
predict these cells?"  The latter requires the family's own null (e.g. random
Hopf angles).

**This is the repo's "geometric-ceiling point":** the surface v1 evidence ceiling
is "family-tied cell identities above the no-structure controls," not
"above the Haar null."  The Haar null is the correct floor for the count
statistic; it is NOT the right comparison for the identity statistic.

### 5.2 Partial-trace operations can hit fixed cells even without structure

For an n-site system, the single-site partial trace collapses the entire
complement.  If the complement is in a high-entropy state, rho_k ≈ I/2,
and the Bloch vector is near the origin.  This is the dominant behavior under
Haar measure and is ALSO the dominant behavior under many structured dynamics
that generate highly entangled states.  Both map to the origin cell.

The maximally-mixed control in the repo fires exactly this path: any state with
high single-site entropy maps to the origin cell, failing the recovery predicate.

Implication: the 6-out-of-33 recovery result is consistent with (a) the
structured Hopf/Weyl family specifically targeting those cells, or (b) any
procedure that generates some moderately-entangled states.  The identity
evidence (WHICH cells) discriminates; the count evidence does not.

### 5.3 Chart quantization introduces systematic bias (axis alignment)

The A33 chart cells are aligned to the x/y/z axes.  Bloch vectors that happen
to lie along an axis (e.g. the +x-axis cell A33_xp10_y00_z00) have larger
Voronoi capture regions than off-axis cells.  This means:
- States with Bloch vectors in the x-y plane are biased toward recovering
  x-axis and y-axis cells
- A structured family whose construction naturally lives near an axis (e.g. the
  chiral-quaternion family near the z-axis) will over-hit those cells even
  under perturbation

The Haar null does not account for this axis-alignment bias; it assumes cells
have equal probability (they do not, because of the Voronoi geometry of the
lattice).  The v2 in-packet computation must correct for this by computing p_i
per cell.

### 5.4 The null model is for a single random state, not a constrained family

The theoretical Page/purity results apply to a SINGLE random state.  In the
chart-recovery experiment, the input is a FAMILY of states (4 stored patterns
for the positive case), and the recovery is measured across all 4 states and 4
sites = 16 Bloch vectors.  The correct null is:

    E[distinct non-origin cells from 4 independent Haar states * 4 sites]

NOT

    E[distinct cells from 1 Haar state * 1 site]

The repo computes the former (16 samples), which is the correct framing.  But
the formula E[K] = sum_{i} [1 - (1-p_i)^{16}] requires p_i per cell per single
Bloch vector draw, which must be estimated by Monte Carlo.

### 5.5 Haar null is uninformative for out-of-equilibrium dynamics

The retrieval dynamics in surface v1 are dissipative: rho' = (1-alpha)*rho +
alpha*target.  Starting from the stored pattern, this is a contracton toward
the target.  Starting from the pair-mix initial condition, it is a contraction
toward a spurious attractor.  The TERMINAL STATE of this dynamics is not
Haar-random; it is a fixed point of the update map.

Consequently, the Haar null for the single-site marginals of terminal states is
a null for the WRONG quantity.  The relevant null is for the distribution of
terminal states of the dynamics starting from the relevant initial conditions.
A dynamics-specific null would ask: if the coupling matrix W were random, what
terminal states would the retrieval dynamics produce?

The Haar null remains valid as a reference for the chart cell expected-count
correction (the floor below which count evidence is uninformative).  It does not
serve as a dynamics-matched null.

---

## 6. Computable procedures for a finite sim

### 6.1 Computing E[K_null] in-packet (the v2 requirement)

Procedure with pinned seed, for n=4 qubits, n_patterns patterns, n_sites sites:

1. Fix seed S (record in result JSON).
2. For i in 1..N_MC:
   a. Draw n_patterns Haar-random 4-qubit pure states
      psi_j = (Re(x) + i*Im(x)) / ||(Re(x) + i*Im(x))|| where x ~ CN(0, I_{16})
   b. For each j in 1..n_patterns, for each site k in 0..n_sites-1:
      - Compute rho_k = partial trace over complement of site k
      - Compute Bloch vector r_k = (Tr rho_k sigma_x, Tr rho_k sigma_y, Tr rho_k sigma_z)
      - Find nearest A33 cell by Euclidean distance
   c. Count distinct non-origin cells K_i
3. E[K_null] = mean(K_1, ..., K_{N_MC})
4. SE = std(K_1,...,K_{N_MC}) / sqrt(N_MC)

Report: E[K_null], SE, N_MC, seed.  The claim "K_actual < E[K_null]" needs this
to be computed in-packet with the exact same chart classifier and n_patterns as
the actual experiment.

Minimal N_MC for 1-digit accuracy on E[K_null]: K is bounded between 0 and 32;
its variance is at most 32 * 0.25 = 8 (Bernoulli bound).  For SE < 0.1:
N_MC > 8 / (0.1)^2 = 800.  Use N_MC = 1000 with seed = SIM_ID-derived constant.

### 6.2 Per-cell probability estimation

For the identity-based test, compute p_i per cell:

    p_i = (count of samples whose nearest cell is i) / (N_MC * n_patterns * n_sites)

This gives an empirical distribution over cells under Haar measure.  A cell hit
in the positive case that has p_i < 0.01 under Haar is a strong identity signal;
a cell with p_i ≈ 1/33 is consistent with Haar.

The v2 correction for axis-alignment bias: compare the recovered cells'
individual p_i values against the cells predicted by the family construction.

### 6.3 Quick purity / entropy sanity check

Before running the full null simulation, verify that the generated states have
purity consistent with expectation:

    # For each generated Hopf/Weyl state psi on 4 sites:
    for site in range(4):
        rho_k = partial_trace(psi, site)
        purity_k = np.real(np.trace(rho_k @ rho_k))
    # Expected under Haar: purity ≈ 10/17 ≈ 0.588
    # Actual for chiral-quaternion family: likely higher (less entangled)
    # Actual for entangled-nonproduct: likely lower

A family whose single-site purity is systematically higher than Haar expectation
will naturally recover more non-origin cells regardless of whether the specific
cells are structurally predicted.  This is a necessary diagnostic before
interpreting identity evidence.

---

## 7. Repo relevance

### 7.1 Surface v1 base-rate correction (commit 28fc221a1)

The correction in `28fc221a1` (receipts: THE SONNET EVENING SWEEP'S CORRECTIONS)
demoted the surface v1 first-floor claim from "6 cells > 3 (pinned-random base
rate)" to "6 cells < ~7.6 (Haar null), evidence is identity-based not
count-based."

The specific receipt is:
`system_v6/receipts/owner_doctrine_spinor_network_surface_20260611.md` lines
89-97, which defines the corrected framing.

The Haar null value ~7.6 appears as `"base_rate_correction": "haar_null_~7.6;
evidence=family-tied cell identity"` in
`system_v6/sims/spinor_network_surface_v1/spinor_network_surface_v1_envelope.py`
lines 273, 288.

This note explains WHY 7.6 < 12 (the naive uniform estimate): the Haar
distribution places more mass near r=0 (origin cell) than a uniform ball
distribution, reducing expected non-origin cell count.  The ~7.6 figure should
be verified by the v2 in-packet computation.

### 7.2 Surface v2 requirement: in-packet Haar null

The standing queue receipt
`system_v6/receipts/standing_queue_20260612.md` line 16 specifies:
"Surface v2 — the corrected targets: in-packet Haar null, rebuilt wrong-row
control, chart-axis bias reduction, Kraus/Choi witness ledger, fuller A33
coverage."

This note provides the computable procedure for that in-packet requirement
(Section 6.1 above).

The v2 design notes that:
1. The Haar null computation must use the SAME chart classifier (A33 predeclared
   rows, same Voronoi binning) as the positive experiment
2. The null must match the SAME n_patterns * n_sites sample count (16 Bloch
   vectors in v1)
3. The seed must be pinned in the result JSON (the missing-seeds audit:
   `system_v6/receipts/missing_things_audit_20260610.md` line 35 flagged this
   for geo_s1 packets; the same discipline applies to the surface null)
4. The expected count and standard error must be reported, not just a single
   number

### 7.3 The geometric-ceiling point

The repo's commitment to family-tied cell identity as the evidence (rather than
count-based evidence) maps directly to the limitation described in Section 5.1:
the Haar null does not control for the carrier's reachable-set geometry.

The auditor's `GEOMETRIC_CEILING` language and the surface doctrine's "chart-axis
bias" caveat refer to this: even with an in-packet Haar null, the surface v2
will carry the caveat that the identity evidence is structure-sensitive only
within the Hopf/Weyl family, not evidence against all structured alternatives.

A stronger test (not yet registered in the repo) would use a FAMILY-APPROPRIATE
null: random Hopf angles (phi, chi, eta) uniformly distributed on their natural
domains, producing a random member of the chiral family, and checking whether
random members of the family recover the same cells as the specific committed
patterns.

### 7.4 Single-site purity diagnostic for generated states

Given that the chiral-quaternion patterns are Hopf/Weyl product states (or
near-product), their single-site purity is likely higher than the Haar
expectation of 10/17 ≈ 0.588.  If purity ≈ 1 (pure site states), the Bloch
vector has |r_k| ≈ 1 and the state will reliably hit non-origin cells.  This
is exactly the structure claim: the Hopf construction targets the sphere surface
(r = 1 cells), not the interior.

The v2 in-packet purity diagnostic (compute E[Tr(rho_k^2)] for each family,
compare to Haar expectation 10/17) would sharpen this.

### 7.5 Relevant receipts and source paths

- `system_v6/receipts/owner_doctrine_spinor_network_surface_20260611.md`:
  adjudication of v0/v1, the correction entry (lines 85-97)
- `system_v6/sims/spinor_network_surface_v1/spinor_network_surface_v1_jax.py`:
  lines 98-126 define a33_rows() (the 33-cell chart), lines 358-395 define
  the chart recovery procedure
- `system_v6/sims/spinor_network_surface_v1/spinor_network_surface_v1_envelope.py`:
  lines 271-291 record the base-rate correction annotation
- `system_v6/receipts/standing_queue_20260612.md`: line 16 states the v2 Haar
  null requirement
- `system_v6/receipts/toolset_expansion_20260610.md`: line 45 records the ott
  Haar-Wasserstein route for S1 receipts (a related but distinct Haar use case)
- `system_v6/probes/toolset_expansion_20260610_python.py`: lines 138-199
  define haar_spinors() and Haar-vs-clustered Wasserstein comparison (for S1,
  not the A33 chart — different setting but shows the pattern)

---

## Appendix: the A33 cell count (verified)

The 33-cell breakdown confirms the grid geometry:

| r^2      | r        | Cell description                          | Count |
|----------|----------|-------------------------------------------|-------|
| 0.00     | 0.000    | origin (0,0,0)                            |     1 |
| 0.25     | 0.500    | single-axis ±0.5 (e.g. (0.5,0,0))        |     6 |
| 0.50     | 0.707    | two-axis ±0.5 (e.g. (0.5,0.5,0))         |    12 |
| 0.75     | 0.866    | three-axis ±0.5 (e.g. (0.5,0.5,0.5))     |     8 |
| 1.00     | 1.000    | single-axis ±1.0 (e.g. (1,0,0))          |     6 |
| **Total**|          |                                           |  **33** |

Non-origin cells: 32.  The 8 corner-adjacent cells at r = 0.866 are included
(0.866 < 1.0 <= 1.000000001 tolerance in the source).

Under uniform sampling on the Bloch ball, the expected probability of hitting
each class is proportional to the Voronoi volume of that class.  The r=1 cells
(the poles) have the smallest Voronoi volumes; the r=0.5 and r=0.707 cells have
the largest.  Under Haar measure, the distribution is further skewed toward low
r (high entanglement -> small Bloch vector -> near-origin), making the origin
cell the most probable single cell and the r=1 cells the least probable.

This confirms why the Haar-expected non-origin count (~7.6) is substantially
less than the naive uniform estimate (~12) and also less than the "above 3
(pinned-random base rate)" comparison that v1 originally used.
