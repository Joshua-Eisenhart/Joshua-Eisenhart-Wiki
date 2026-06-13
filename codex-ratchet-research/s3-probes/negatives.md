# S3 Probes - Negatives

Status: standing research queue, not populated in this kickoff.

Expected negative controls: exact MUB/Pauli alias detection before batteries,
rank equality without effect equality, informational completeness without
projective/order identity, and finite-frame normalization failures.

## Wave 2 population - negative controls and kill conditions

Scope note: this file records what should block or demote S3 probe identity.
It is intentionally phrased as exclusion language.

### What frame/POVM theory forbids or does not grant

- Positivity and normalization are mandatory. A proposed effect row with a
  negative eigenvalue, weights not summing to identity, or a weighted Bloch
  centroid not closing to zero is not a POVM.
- IC requires span of the Hermitian operator space. In dimension `d`, fewer
  than `d^2` generic scalar probabilities cannot be minimal full-state IC;
  more outcomes can still fail IC if the effects are linearly dependent in the
  wrong subspace.
- A complete set of `d+1` MUBs is guaranteed by standard constructions for
  prime-power `d`, not for arbitrary composite `d`. `d=6` is the trap: at least
  three are known, but a complete seven-basis set is not a stable settled fact.
- SIC existence is not a solved theorem in every finite dimension in stable
  sources. Numerical tables and many exact constructions are evidence for
  particular dimensions/classes, not permission to instantiate arbitrary `d`.
- Projective measurements are a strict subset of POVMs. An IC POVM generally
  cannot be collapsed to a single projective measurement without changing the
  observation map.

### Alias traps

- `Pauli XYZ battery == qubit SIC`: false unless the row explicitly changes
  the measurement object. Three two-outcome projective contexts are not the
  same effect multiset as a four-outcome tetrahedral SIC.
- `same IC rank == same POVM`: false. IC rank says the effects span; it does
  not fix symmetry, weights, Gram matrix, or operational probabilities.
- `same number of outcomes == same quotient class`: false. Four rank-one qubit
  outcomes can be SIC, non-SIC IC, or even fail the intended symmetry test.
- `same pairwise absolute overlaps == same projective frame`: incomplete in
  general. Projective unitary equivalence may need phase-sensitive Bargmann
  invariants or an explicit reconstruction/equivalence test.
- `basis set == measurement battery`: only true under a declared convention
  translating bases to projective effects and preserving context labels.
- `coarse-grained equality == identity`: only valid for the coarse-grained
  task. It does not identify the underlying fine effects.

### Conditions that kill probe identity

- Missing source for the mathematical family or construction.
- Unspecified quotient: no clear answer to whether relabeling, unitary,
  antiunitary, phase, scaling, coarse-graining, or noise is allowed.
- Weight loss: rays/projectors are recorded but POVM weights are dropped.
- Context loss: a measurement battery is flattened into an unordered effect
  bag when the row depends on which effects belong to the same measurement.
- Dimension mismatch or prime-power leakage, especially treating `d=6` like
  `d=4` or `d=5`.
- IC/span unverified for a row whose purpose is tomography.
- Symmetry asserted from a visual pattern only, without Gram/effect checks.
- Continuous family represented by one sample without the row saying
  "sample", "family member", or "finite representative".

### Nonexistence/unknown register

- `d=6 complete MUB`: unknown/open in conservative sources; use "at least
  three known" or "complete set not established", not "nonexistent" unless a
  future proof is explicitly admitted by the controller.
- `all-d SIC theorem`: conjectural/open in stable sources; cite exact/numerical
  dimensions when using a known case.
- `real MUBs`: real-vector MUB questions have different bounds and should not
  be silently imported into complex Hilbert-space rows.
- `ETF/SIC transfer`: equiangular tight frame facts over real spaces, finite
  fields, or arbitrary frame settings do not automatically instantiate complex
  SIC POVMs with the required quantum normalization.

### Sources

- Scott and Grassl, "SIC-POVMs: A new computer study", arXiv:0910.5784,
  https://arxiv.org/abs/0910.5784
- Szollosi, "The problem of mutually unbiased bases in dimension 6", conference
  proceedings PDF, https://math.bme.hu/~matolcsi/proceedingsmub0904.pdf
- McNulty and Weigert, "Mutually Unbiased Bases in Composite Dimensions - A
  Review", Quantum 10, 2051 (2026), https://quantum-journal.org/papers/q-2026-04-01-2051/
- Chien and Waldron, "A characterisation of projective unitary equivalence of
  finite frames", arXiv:1312.5393, https://arxiv.org/abs/1312.5393
- D'Ariano, Lo Presti, Perinotti, "Classical randomness in quantum
  measurements", J. Phys. A 38 (2005), PDF:
  https://wordpress.qubit.it/wp-content/uploads/publications-dariano/extrpovm_JPA.pdf
