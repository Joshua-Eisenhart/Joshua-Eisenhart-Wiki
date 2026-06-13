# S3 Probes - Standard Math

Status: standing research queue, not populated in this kickoff.

Expected scope: POVMs, projective measurements, SIC/MUB frames, informational
completeness, Bloch-vector effect rows, frame Gram matrices, and alias
detection for probe families.

Do not sample this placeholder into MMM heads.

## Wave 2 population - bounded standard math

Scope note: this file is a source register for S3 probe/canonicalizer rows, not
a claim that any Codex Ratchet probe identity has already been promoted.

### POVM and frame basics

- A POVM is a finite family of positive semidefinite effects `{E_i}` with
  `sum_i E_i = I`. For probe rows, the stored object should be the effect
  multiset, weights included, not only the underlying rays.
- In dimension `d`, an informationally complete POVM (IC POVM) has effects
  spanning the real vector space of Hermitian operators, dimension `d^2`.
  Minimal IC POVMs have `d^2` outcomes; overcomplete IC POVMs have more.
- Frame-language translation: rank-one POVMs are finite weighted projective
  frames. The frame/Gram data can support equivalence tests, but the tested
  quotient must say which symmetries are allowed: unitary/antiunitary, phase,
  relabeling, weight preservation, and coarse-graining.
- For finite vector sequences, equality of ordinary Gram matrices is enough
  for unitary equivalence of the ordered vectors. For projective unitary
  equivalence of lines, Chien and Waldron use Bargmann/projective invariants;
  this is closer to a probe quotient than raw pairwise overlaps alone.

### SIC status

- A SIC POVM in complex dimension `d` is a set of `d^2` rank-one effects from
  equiangular lines, usually normalized as `E_i = Pi_i / d`, with constant
  Hilbert-Schmidt overlaps. SICs are minimal IC POVMs when they exist.
- Existence in every finite complex dimension remains a conjectural/global
  problem in the stable literature. Scott and Grassl report numerical SIC
  solutions through `d <= 67` and a putatively complete Weyl-Heisenberg
  covariant list through `d <= 50`; older and newer exact/numerical tables are
  evidence, not a universal proof.
- For S3 rows, call a qubit tetrahedron a `d=2 SIC` only when the four effects
  have the tetrahedral Bloch geometry and the correct equal weights. A generic
  rank-four qubit IC POVM is not thereby a SIC.

### MUB classification register, d=2..6

- Definition: bases `B_a` and `B_b` are mutually unbiased when all cross
  transition probabilities are `1/d`.
- Prime-power dimensions have complete sets of `d+1` MUBs by finite-field or
  Heisenberg-Weyl constructions. This covers `d=2,3,4,5`.
- Brierley, Weigert, and Bengtsson classify all inequivalent MU basis sets in
  dimensions two to five. Relevant S3 summary: complete sets are unique up to
  equivalence below six, while lower-cardinality families can still have
  parameters, e.g. triples in `d=4`.
- `d=6` remains the canonical low-dimensional composite trap in conservative
  references: at least three MUBs are known, a complete set would have seven,
  and the existence of seven is not settled by the stable review literature.
  Do not write a probe row that treats `d=6` as if the prime-power rule applies.

### IC frame/probe quotient hooks

- IC is a span condition, not a symmetry condition. Equal outcome count,
  equal rank profile, or equal Gram rank does not identify two POVMs.
- Useful canonicalizer invariants: ordered/unordered effect spectrum, trace
  weights, Hilbert-Schmidt Gram matrix of effects, vector-line projective
  invariants for rank-one effects, IC rank, tightness, and allowed relabeling.
- Probe quotient should preserve the tested observation map: two probes may be
  equivalent for one task if they induce the same probabilities after an
  explicitly allowed relabel/coarse-grain, but inequivalent for tomography or
  canonical row identity.

### Sources

- Renes, Blume-Kohout, Scott, Caves, "Symmetric Informationally Complete
  Quantum Measurements", arXiv:quant-ph/0310075,
  https://arxiv.org/abs/quant-ph/0310075
- Scott and Grassl, "SIC-POVMs: A new computer study", arXiv:0910.5784,
  https://arxiv.org/abs/0910.5784
- Brierley, Weigert, Bengtsson, "All Mutually Unbiased Bases in Dimensions Two
  to Five", arXiv:0907.4097, https://arxiv.org/abs/0907.4097
- Szollosi, "The problem of mutually unbiased bases in dimension 6", conference
  proceedings PDF, https://math.bme.hu/~matolcsi/proceedingsmub0904.pdf
- McNulty and Weigert, "Mutually Unbiased Bases in Composite Dimensions - A
  Review", Quantum 10, 2051 (2026), https://quantum-journal.org/papers/q-2026-04-01-2051/
- Chien and Waldron, "A characterisation of projective unitary equivalence of
  finite frames", arXiv:1312.5393, https://arxiv.org/abs/1312.5393
