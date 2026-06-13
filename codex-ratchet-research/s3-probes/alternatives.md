# S3 Probes - Alternatives

Status: standing research queue, not populated in this kickoff.

Registry space to research later: committed Pauli XYZ, MUB XYZ alias probe, SIC
tetrahedron, noisy Pauli IC, z-refined equatorial trine, and deterministic
rank-four null-fixed frame.

Future work should keep exact effect-multiset aliasing separate from equal rank
or equal six-state separation.

## Wave 2 population - alternative probe families

Scope note: this is a candidate-family register for finite S3 rows. It does not
promote any family to canonical identity without an explicit effect-level test.

### d=2 POVM moduli

- Any qubit effect can be written in Bloch form, e.g. a positive weighted
  identity-plus-vector operator with positivity bounded by the vector length.
  A qubit POVM is a finite set of such effects whose scalar weights sum to the
  identity trace condition and whose weighted Bloch vectors sum to zero.
- This gives a continuous moduli space, not only named examples. For S3, use
  finite representatives as probes, but keep the underlying family continuous
  unless the row explicitly fixes weights, vectors, and relabel quotient.
- Extremal qubit POVMs are a useful finite boundary source: the non-projective
  rank-one cases have three or four outcomes; the four-outcome boundary includes
  IC examples, and the regular tetrahedron is the symmetric special case.
- Three-outcome qubit POVMs, including trine-like/equatorial variants, are
  useful non-IC or task-specific probes. They can distinguish projective-vs-
  nonprojective behavior without pretending to reconstruct arbitrary states.

### Finite alternatives useful for rows

- `Pauli XYZ battery`: three two-outcome projective measurements along X, Y,
  and Z. It is tomographically complete as a collection but not a single
  four-outcome SIC. Preserve measurement context/order in the row.
- `MUB XYZ alias probe`: in `d=2`, the three Pauli eigenbases form the complete
  MUB set. It can alias a Pauli battery if context is erased; store basis labels
  and outcome labels to prevent false identity.
- `SIC tetrahedron`: four equally weighted rank-one effects at regular
  tetrahedron Bloch vectors. Minimal IC, symmetric, and a good positive control
  for Gram/effect-multiset canonicalizers.
- `Noisy Pauli IC`: mix Pauli projective effects or use depolarized Bloch
  vectors to test whether IC rank survives noise. This is a rank/span test, not
  a projective-equivalence test.
- `z-refined equatorial trine`: a three-outcome equatorial trine plus a small
  z-sensitive refinement or separate z row can expose when a canonicalizer loses
  the distinction between planar coverage and full Bloch tomography.
- `Rank-four null-fixed frame`: any four-effect qubit IC frame with nonzero
  determinant in the Hermitian-coordinate matrix, fixed weights, and an explicit
  null/degeneracy guard. Useful as a non-SIC minimal IC control.
- `MUB d=4 family sampler`: complete MUB set in `d=4` is unique up to
  equivalence, but triples have parameter families. Use this to test that the
  canonicalizer does not collapse all partial MUB triples to the complete-set
  class.
- `MUB d=6 product triple`: the guaranteed product-style three-MUB construction
  is a stable positive control; never label it a complete seven-MUB object.

### Row-construction guard

- Store each alternative as `(dimension, effects or basis projectors, weights,
  outcome labels, measurement context, allowed quotient, intended observable)`.
- A finite representative can be a probe label, but not evidence that the whole
  continuous moduli family has been classified.
- Use paired controls: one positive alias pair with an explicit relabel/unitary,
  and one near-alias pair killed by weights, context, or IC rank.

### Sources

- D'Ariano, Lo Presti, Perinotti, "Classical randomness in quantum
  measurements", J. Phys. A 38 (2005), PDF:
  https://wordpress.qubit.it/wp-content/uploads/publications-dariano/extrpovm_JPA.pdf
- Renes, Blume-Kohout, Scott, Caves, "Symmetric Informationally Complete
  Quantum Measurements", arXiv:quant-ph/0310075,
  https://arxiv.org/abs/quant-ph/0310075
- Brierley, Weigert, Bengtsson, "All Mutually Unbiased Bases in Dimensions Two
  to Five", arXiv:0907.4097, https://arxiv.org/abs/0907.4097
- McNulty and Weigert, "Mutually Unbiased Bases in Composite Dimensions - A
  Review", Quantum 10, 2051 (2026), https://quantum-journal.org/papers/q-2026-04-01-2051/
- Czerwinski, "Quantum state tomography with informationally complete POVMs
  generated in the time domain", arXiv:2010.13777,
  https://arxiv.org/abs/2010.13777
