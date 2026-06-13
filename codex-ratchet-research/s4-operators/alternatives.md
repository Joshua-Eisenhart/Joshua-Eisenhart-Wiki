# S4 Operators - Alternatives

Source registry: `system_v6/receipts/round3_discriminator_registry_20260611.md`.
Evidence ceiling: finite alternative-space research, not result evidence.

## Canonicalizer

The registry canonicalizes each alphabet as role-preserving rows:

`[(role_id, M_exact, c_exact, CPTP_choi_spectrum_class, fixed_axis_set)]`.

Axis relabels are aliases only if they preserve the documented parent z-probe
and N01 row. Role-preserving equality is stricter than sharing a channel type.

## Candidate Families

- `S4.R3.0_committed_DzDxRxRz`: the pinned committed dephasing/rotation affine
  maps. It is the comparator.
- `S4.R3.1_z_amplitude_damping_pair`: `AD_z(gamma)` for
  `gamma in {1/5,3/10}` plus committed rotations. This is a close non-unital
  neighbor because it keeps CPTP structure while shifting the fixed point.
- `S4.R3.2_x_amplitude_damping_pair`: x-frame amplitude damping plus committed
  z maps. It tests whether a frame-shifted non-unital row descends through the
  parent z-probe quotient.
- `S4.R3.3_dephase_rotate_hybrid`: `D_z(lambda) o R_x(theta)` with listed
  finite pairs. Composition order and shell leakage are part of the object.
- `S4.R3.4_axis_permuted_committed`: cyclic axis relabels. These are
  convention-neighbors, but not automatic aliases when the parent probe role
  changes.
- `S4.R3.5_weak_nonunital_pauli_channel`: small affine translations with a
  committed-like diagonal contraction. It is deliberately close and should be
  separated by Choi positivity, fixed-axis, and non-unital rows.

## Classification Bounds

Ruskai-Szarek-Werner bounds the qubit CPTP set by canonical forms and Choi
complete-positivity constraints. The registry then adds role and parent-probe
constraints. Sharing a Choi spectrum class is not enough for alias if the role
tuple, translation vector, or fixed-axis set differs.
