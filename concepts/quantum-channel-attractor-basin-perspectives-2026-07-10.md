# Quantum-Channel Attractor Basin Perspectives - 2026-07-10

Status: researched possibility space plus a bounded Ratchet measurement. This
page is not canon.

## Question

Does repeated geometry/entropy co-ratcheting reveal a real attractor basin, or
does a chosen dissipative map merely install one?

Those are different questions. A finite contraction can have a completely real
global attractor while supplying no evidence that the Ratchet selected the map,
its schedule, or its language.

## Current Measurement

The preregistered Ratchet packet
`system_v7/sims/coratchet_basin_depth_multiview_v0` independently constructs the
sixteen source terrain/operator compositions in Julia and JAX. Axis 6 remains
composition precedence only.

Both runtimes recover the same Bloch affine maps to roughly machine precision:

| installed cycle | largest Bloch singular value | spectral contraction gap |
|---|---:|---:|
| Type1 left | 0.3988799053 | 0.6420135561 |
| Type2 right | 0.3406122483 | 0.6731681786 |

For a qubit, trace distance is proportional to Euclidean Bloch distance. A
largest singular value below one therefore means each complete installed cycle
is a strict global trace-distance contraction. Each has one full-rank fixed
state and the entire Bloch ball is its basin.

This is stronger than endpoint clustering: it is a real global attracting fixed
point of the explicitly written map. It is also substantially true by
construction because every terrain map installs dissipation. The independent
fabrication audit therefore permits the map-level contraction statement but
rejects the artifact's `coratchet` and `basin depth` framing.

## What Did Not Survive

The native source order is not jointly exceptional:

- Type1 spans ranks `17..32` of 33 after ties, with a `27.3%` midrank
  percentile among schedules made from the same channels.
- Type2 spans ranks `3..18` of 33 after ties, with a `69.7%` midrank
  percentile, below the preregistered `95%` boundary.
- matched random dissipative cycles also contract and defeat the genericity
  gate.
- the independent free-length and SMT lanes still do not derive four.

The accepted description is therefore:

```text
installed global attracting fixed points;
generic dissipation;
native order not selected;
no Ratchet basin admission
```

Calling this a co-ratchet basin would collapse three distinctions:

1. channel evolution versus constraint tightening;
2. a whole-carrier global basin versus internal sub-basins and separatrices;
3. a property of an installed map versus a map forced by the Ratchet.

The two runtimes replicate one mathematical construction. They do not provide
two independent physical models, and changing installed rates does not by
itself create two engine personalities. The random-channel controls also differ
between the runtimes, so their numerical null distributions cannot be presented
as cross-engine replicas.

## Perspectives On The Same Fixed Point

### Liouville Spectrum

The eigenvalue at one identifies the fixed operator. The transverse eigenvalues
measure asymptotic mixing. Peripheral eigenvalues would expose recurrent or
non-mixing structure. The general structure of quantum-channel spectra and
peripheral eigensystems is studied by
[Wolf and Perez-Garcia](https://arxiv.org/abs/1005.4545).

### Bloch Geometry

The affine form `r -> M r + c` exposes contraction directions, offsets, and
anisotropy. Singular values are stronger than one endpoint distance because
they describe contraction over all state differences.

A recent extension replaces a single extremal contraction coefficient with a
sequence of contraction/expansion values under channel composition:
[Ibarrondo and Sanz](https://arxiv.org/abs/2607.04950). This suggests a future
Ratchet readout using the full transverse contraction profile rather than only
`max singular value`.

### Relative Entropy And BKM Geometry

If `rho_star` is a channel fixed point, data processing gives

```text
D(Phi(rho) || rho_star) <= D(rho || rho_star).
```

That makes stroboscopic Umegaki decrease a consistency theorem once the fixed
point and CPTP map are established. It is not by itself a discriminator for the
native schedule. Hiai and Ruskai compare contraction of relative entropies,
monotone metrics, geodesic distance, and trace distance under noisy channels:
[Contraction coefficients for noisy quantum channels](https://arxiv.org/abs/1508.03551).

Exponential relative-entropy decay is a stronger statement tied to modified
log-Sobolev structure, not merely to one finite trajectory:
[Wirth](https://arxiv.org/abs/2505.07549). This is a possible deeper certificate
for a future semigroup lane.

In the present artifact, this data-processing check is a theorem-level
consistency control once CPTP and the fixed point are established. It cannot
count as independent evidence for a native co-ratchet pawl.

### Bures/QFI View

Packet 112 robustly distinguishes the SLD/QFI fidelity curvature from the BKM
relative-entropy curvature on nine noncommuting mixed-state directions. They
agree on commuting directions. These are two views of the same state space, but
the finite witness does not select a Ratchet metric or prove Umegaki uniqueness.

### Schedule View

Permuting the same sixteen channels changes fixed points and depths. This is the
correct null for schedule selection because it preserves the channel multiset
and dissipation budget. A native map that is not an outlier under this null is
an installed schedule, not an earned one.

### Quotient And Mesh View

A perspective map can preserve a basin only when it is a semiconjugacy or a
lumpable quotient. Basin fibers must not mix states assigned to different
terminal classes. Global-phase quotient, density spectrum, finite probe
quotient, Type1/Type2 mirror, and chart changes require separate tests; they are
not interchangeable uses of "perspective."

## Existing Finite-Basin Boundary

Earlier finite `R_C` work found one terminal singleton plus a 32-cell leaky or
metastable SCC. Every cell may reach the singleton, but only the singleton must
reach it. Rotating the finite chart also merged apparent terminal classes.

This means the repo already has:

- installed finite recurrent structure;
- may/must and leakage machinery;
- a counterexample to naive chart-invariant sub-basin claims.

It does not yet have one object that is simultaneously perturbation-stable,
multi-perspective invariant, and Ratchet-selected.

## Next Deep Experiment

Construct rational Bloch lattices at several resolutions and project the native
channels with two tie-break rules. Search schedule lengths `2..8`, not only
four. For every exact finite transition graph compute:

- recurrent classes and exact cycles;
- may and must basins;
- hitting-time and mixing-depth distributions;
- boundary depth, leakage, and metastability;
- resolution and tie-break stability;
- semiconjugacy and basin-fiber purity under declared perspectives;
- native-order rank among same-channel permutations;
- erased-dissipation, commuting, all-unitary, terrain-only, and operator-only
  controls.

That experiment can reveal internal basin structure and separatrices. The
current continuous affine cycles cannot: their basin is the whole Bloch ball.

## Routes

- [[projects/codex-ratchet/engine-16x4-axis6-current-state-2026-07-09]]
- [[projects/codex-ratchet/current-research-frontier-2026-07-09]]
- [[projects/codex-ratchet/packet-112-canonical-rerun-and-basin-audit-2026-07-10]]
- [[concepts/dual-ratchet-geometry-entropy-jordan-research-2026-07-09]]
