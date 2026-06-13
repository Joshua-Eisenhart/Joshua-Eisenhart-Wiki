# S3 Probes - Distillate

Status: standing research queue, not populated in this kickoff.

Future MMM-register extraction should name only tested effect-row distinctions:
same effect multiset, same Gram matrix, same IC rank, same z-coarsening, or
excluded by projective/order row.

## Wave 2 population - MMM register only

This file is wording discipline for S3. It is not a theorem file and not an
admission surface.

### Exclusion language

- Use "excluded by effect normalization" when positivity or `sum E_i = I`
  fails.
- Use "excluded by span/IC rank" when the effects do not span Hermitian
  operator space for the claimed dimension.
- Use "excluded by context loss" when a battery of measurements was flattened
  into an unordered POVM or a basis register was treated as a single effect row.
- Use "excluded by quotient mismatch" when two rows only match after a symmetry
  that the row did not allow.
- Use "excluded by dimension/status" for `d=6` complete-MUB leakage or
  all-d SIC overclaim.
- Use "near alias, not identity" when Gram/rank/outcome counts match but
  weights, phases, projective invariants, or operational probabilities differ.

### No reified abstractions

- "Probe" names a finite test object or family representative, not a physical
  substrate.
- "Canonicalizer" names a comparison procedure, not a proof that the compared
  objects are naturally identical.
- "Quotient" names declared equivalences; it does not erase distinctions that
  were not explicitly placed in the quotient.
- "IC" names a span property. It does not imply SIC, projective measurement,
  MUB structure, optimality, or uniqueness.
- "SIC", "MUB", "ETF", and "frame" remain labels for cited mathematical
  structures with their own conditions.

### Names as labels

- Prefer row labels like `qubit_sic_tetrahedron_sample`,
  `pauli_xyz_battery`, `mub_d6_product_triple`, `rank4_non_sic_ic_control`,
  and `equatorial_trine_non_ic_control`.
- Do not let a label carry hidden admission. A row named `canonical` still
  needs explicit effects, weights, quotient, and pass/fail checks.
- When using a sample from a continuous moduli family, include `sample` or
  `representative` in the label unless the family has been classified in the
  row's quotient.

### Probe-relative identity

- Identity is always relative to the declared probe question:
  effect-multiset identity, projective-frame identity, tomography equivalence,
  coarse-grained task equivalence, or battery/context equivalence.
- Store the observation boundary with the row. If the observation map changes,
  the identity claim must be rechecked.
- Positive control pattern: one pair known equivalent by explicit relabel or
  unitary under the declared quotient.
- Negative control pattern: one near pair killed by weight, context, IC rank,
  phase-sensitive invariant, or dimension/status.
- S3 phrasing should end at "this row can/cannot distinguish under this
  quotient" unless a separate admission artifact upgrades the claim.

### Source handles for MMM extraction

- SIC: Renes et al. arXiv:quant-ph/0310075; Scott and Grassl arXiv:0910.5784.
- MUB d=2..5: Brierley, Weigert, Bengtsson arXiv:0907.4097.
- MUB d=6/composite caution: Szollosi proceedings; McNulty and Weigert,
  Quantum 10, 2051 (2026).
- Projective frame quotient: Chien and Waldron arXiv:1312.5393.
- Extremal qubit POVM boundary: D'Ariano, Lo Presti, Perinotti, J. Phys. A 38
  (2005).
