# Packet 107 Physics Source Register - 2026-07-09

## Intake Status

Primary-source research for the two scientific additions in `107.zip`:
redshift evolution of the characteristic galactic acceleration scale and the
geometric phase of a spinor path. This page is researched wiki context, not
Ratchet canon.

Local disposition:
[[projects/codex-ratchet/packet-107-physics-loopback-audit-2026-07-09]].

## Redshift Evidence

### Genzel et al. (2017)

[Strongly baryon-dominated disk galaxies at the peak of galaxy formation ten
billion years ago](https://arxiv.org/abs/1703.04310) reports declining outer
rotation curves for six massive star-forming disks at roughly `z=0.9-2.4`.
The authors attribute the behavior to strong baryon dominance within the
observed regions plus substantial pressure support. The sample is small and
does not itself fit a redshift-dependent MOND acceleration scale.

### Milgrom (2017)

[High-redshift rotation curves and MOND](https://arxiv.org/abs/1703.06110)
interprets the Genzel sample under MOND. It argues that a value around four
times the local `a0` at `z about 2`, including an example scaling resembling
`(1+z)^(3/2)`, is difficult to accommodate. The same paper says smaller values
cannot be excluded and that the observed curves do not reach the asymptotic
speeds required for a direct mass-asymptotic-speed-relation test.

Project consequence: this source constrains a rapid increase. It does not
select a constant de Sitter branch from an exhaustive model comparison.

### Ciocan et al., MUSE-DARK III (2026)

[The evolution of the radial acceleration relation at intermediate
redshifts](https://arxiv.org/abs/2604.22613) analyzes 79 star-forming galaxies
over `0.33 < z < 1.44` using three-dimensional forward modeling and disk-halo
decomposition. It reports:

- `a0(z about 1) = 2.38 +0.12/-0.10 x 10^-10 m/s^2` at 95% credibility;
- intrinsic scatter near `0.17 dex`;
- a linear phenomenological coefficient
  `a1 = 1.59 +0.10/-0.10 x 10^-10 m/s^2` per unit redshift;
- larger fitted `a0` under several halo profiles and a self-consistent MOND
  treatment;
- evolution described as faster than `H(z)`.

The authors explicitly frame the linear law as phenomenological and discuss
modeling, spatial-resolution, and data-quality limitations. This is strong
current evidence against the constant branch in packet 107, but it does not
therefore prove the packet's total-`H` formula.

## Geometric Phase

### Berry (1984)

[Quantal phase factors accompanying adiabatic
changes](https://doi.org/10.1098/rspa.1984.0023) develops the geometric phase
for cyclic adiabatic evolution. The physical phase is a holonomy of the ray
bundle and is gauge-invariant modulo `2 pi`; a connection integral in one
section is not independently physical.

### Samuel and Bhandari (1988)

[General setting for Berry's
phase](https://doi.org/10.1103/PhysRevLett.60.2339) extends geometric phase to
nonunitary and noncyclic paths using Pancharatnam comparison. Open-path phase
requires endpoint information; the bare connection integral can change under
a gauge transformation.

Project consequence: packet 107's path
`psi(phi)=(exp(i phi),0)` at the pole is one constant projective ray. Its
`-2 pi` connection integral can be gauged to zero. Including the endpoint
phase gives zero geometric phase modulo `2 pi` for both its full and half
paths.

## Ratchet Translation

- UP-135 internal branch arithmetic: reproducible.
- UP-135 claim that data select the constant/de Sitter branch: rejected.
- UP-136 flat-Lambda-CDM asymptote: correct imported arithmetic.
- UP-136 engine/KMS `2 pi` identity: rejected as gauge-dependent.
- 16-by-4 schedule effect: none.
- Axis0 effect: none; the missing bridge is not repaired by cosmological
  numerology or a projectively trivial phase loop.

## Routes

- [[projects/codex-ratchet/current-research-frontier-2026-07-09]]
- [[projects/codex-ratchet/engine-16x4-axis6-current-state-2026-07-09]]
- [[concepts/dual-ratchet-geometry-entropy-jordan-research-2026-07-09]]
