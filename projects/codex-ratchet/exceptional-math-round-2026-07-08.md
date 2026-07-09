# Exceptional Math Round - 2026-07-08

## Status

Round digest from the live Codex-Ratchet repo, commit window ending at `799b7fc79` and bundle sync `4e15f2b46`.

Classification: repo-derived wiki digest.

Claim ceiling: exceptional statics, cone-menu pawl uniformity, measured dynamical deficit, Petz/recovery structure, and named H-ceiling are earned at scratch-diagnostic / local-rerun level. Nonassociative DPI is still open. The octonion dynamics leg is not earned after three attempts.

Source authority for this page is the recent commit record in `/Users/joshuaeisenhart/Codex-Ratchet` plus the result JSONs under:

```text
system_v7/constraint_core/sims_and_scripts/
```

## What Was Tested

The round tested whether exceptional/Jordan/octonion mathematics is forced, merely compatible, or actively blocked by current constraint-core instruments:

- Petz quasi-entropy family behavior across the eight existing terrain flows.
- J3(O) / Albert static machinery and primitive-idempotent entropy-pawl probes.
- Araki modular relative entropy as an independent associative crosscheck.
- F4 / Spin(9) / OP2 stabilizer ranks and stretch ranks.
- Candidate Jordan dissipator / DPI dynamics on J2(O) and J3(O).
- Symmetric-cone menu behavior across classical, spin, associative PSD, and exceptional cones.
- Alfsen-Shultz dynamical-correspondence deficit for H3(O).
- Malcev-not-Lie search for whether present engines demand the octonion bracket class.
- Petz recovery / reversibility equality structure on the existing terrain grid.

## Survived Audit

### Petz Family Structure

`ffce1761b` survives after audit in `9eafe5a63`, with corrections.

The forced object is the operator-convex Petz family on this engine grid, not Umegaki alone. Umegaki is installed within that family. The result JSON reports uniform pawling for the operator-convex rows, with impostors flipping:

- `alpha=3` fails on the four damp/non-unital terrains.
- the wavy non-convex impostor fails everywhere.
- wrong fixed point breaks every family member.

Audit correction: the family has five distinct operator-convex members in this finite census because Hellinger duplicates the alpha-0.5 row up to scale. Uniform pass is Petz-DPI-theorem-guaranteed once the instrument is verified; the grid is instrument validation, not a theorem discovery.

### Araki Crosscheck

`963c4cae5` is useful but demoted by `9eafe5a63`.

The sim independently reproduces finite-dimensional Araki relative entropy as Umegaki on 2048 associative terrain/state pairs, max discrepancy about `1.66e-13`. It also catches swapped-Delta and singular-sigma controls. Its ceiling is an associative matrix-algebra crosscheck only. It does not apply to the exceptional Albert factor.

### Cone-Menu Pawl Uniformity

`8e491ee2a` survives after audit in `799b7fc79`.

The symmetric-cone menu census ran one linear map family across 9 cone families:

- classical `R3`;
- spin `J2(R)`, `J2(C)`, `J2(H)`, `J2(O)`;
- PSD `Sym3(R)`, `Herm3(C)`, `Herm3(H)`;
- exceptional `H3(O)`.

All 9 cells had zero DPI violations on the finite grid. The H3(O) cell reports dimension `27`, octonion content, zero violations, and max increase `-0.007356401505583227`. Wrong sigma breaks all cones; corrupted Fano breaks O-cells upstream. Audit tightened the ceiling: this is pawl uniformity for one finite map family, not a general symmetric-cone theorem.

### Alfsen-Shultz Dynamical Deficit

`e4ce4140a` survives after audit in `799b7fc79`.

The special controls work:

- Herm2(C): Hamiltonian-flow generator is realized; product defect about `3.6e-17`.
- Herm3(C): correspondence rank `8`, matching `su(3)`, commutator residual about `5.8e-16`.

The exceptional branch gives up the single-observable dynamical correspondence:

- H3(O) feasibility rank `1352/1352`;
- nullity `0`;
- measured single-observable correspondence rank `0`;
- traceless observable dimension `26`;
- deficit `26/26`.

This is the cleanest dynamical negative in the round: the exceptional cone keeps the cone-menu pawl but loses observable-generated dynamics under this finite Alfsen-Shultz-style test.

### Spin9 / Spin7 / G2 / SU3xSU3 Chains

`efac1007a` survives after audit in `9eafe5a63`.

Computed ranks:

- F4 derivations of J3(O): `52`.
- primitive idempotent stabilizer: `36`, read as Spin(9) by rank.
- OP2 / Cayley-plane coset: `52 - 36 = 16`.
- point plus one Peirce spinor stabilizer: `21`, Spin(7)-sized.
- point plus two compatible Peirce spinors stabilizer: `14`, G2-sized.
- embedded J3(C) preserver: `16`, SU(3)xSU(3)-sized.

Controls flip: generic non-idempotents produce stabilizer dimension `28`, and corrupted Fano breaks the upstream F4 gate to dimension `7`.

Audit correction: the z3 certificate language was too strong because the rank result is carried by the SVD gap; z3 is supportive only.

### Malcev-Named H-Ceiling

`acafb895d` gives the H-ceiling an algebraic name.

Detector controls:

- Im(H) classifies as Lie.
- Im(O) classifies as Malcev-not-Lie, Jacobiator about `11.7`, Malcev identity residual about `5.8e-15`.
- random R7 classifies as neither.
- corrupted signs break the reference.

Harvest over 10 engine-native bracket families found:

- `7` Lie;
- `3` neither;
- `0` Malcev-not-Lie.

Ceiling: the current engines do not demand the octonion fork's bracket class. H remains the present grouping-demand ceiling.

### Petz Recovery / Reversibility Structure

`6fe7b58d3` survives as the ratchet's undo-structure census.

The equality case of DPI matches Petz recovery exactly on the finite grid with zero anomalies. Reversible step counts:

- damp terrains: `0`;
- depol/proj unital terrains: `288` duplicated maximally mixed fixed-point steps each.

Unitary flow control is all-reversible. Wrong-sigma recovery fails. The earned structure is narrow but important: no free reversible unitary-direction face appears inside the dissipative segments; free moves occur only at fixed points.

## Refuted Or Demoted

### J3O Pawl Dynamics Demotion

`c3727b213` claimed the pawl lifted to full J3(O). `9eafe5a63` weakened it.

What survives:

- J3(O) statics.
- Octonions exercised: `168/290` all-blocks-nonzero random states.
- Spectral machinery.
- Sedenion kill.
- Genuine invariance under a later exp(G2-derivation) check.

Why dynamics is demoted:

- for `p=diag(1,0,0)`, the quadratic representation degenerates to `U_p(rho)=rho_00*p`;
- the flow is bitwise convex mixing;
- a 3-outcome classical simplex reproduces the pawl table;
- the F4 gate used in the first sim was tautological on a 48-element monomial subgroup.

Retroactive correction: the older J2(O) pawl-flow receipt shares the same trivial flow form. It remains a useful finite statics / spectral-entropy receipt, not evidence for nontrivial octonion dynamics.

### Jordan v2 Refutation

`5cf2c7f2e` tried a nonlinear Jordan dissipator and reported DPI failure. `4a8c3cc5e` refuted the claim.

Why refuted:

- the per-tick map is nonlinear because state-dependent trace normalization makes it a conditioned single-Kraus branch;
- DPI does not apply to conditioned branches;
- the same architecture gives 117 classical-simplex "violations";
- J2(O) never calls the octonion table and spin factors are special, so the "exceptional rung" label was overclaim;
- J3(O) samples lived in an associative C-slice: zero multi-block octonion content in the sampled states, associator about `6.6e-24`;
- the relative-entropy formula used a diagonal-shadow expression against a non-diagonal fixed point with off-diagonal drift about `0.0032`;
- correcting to full Jordan functional-calculus log flips the headline violation into a decrease and collapses the signal about 60x.

Survivors from v2: determinism, derivation machinery at about `1e-16`, trace-distance contraction, and useful negative controls. It supports no claim about DPI on the Albert algebra.

### Jordan v3 Weakening

`1f630bdde` fixed the v2 issues and found zero DPI violations for one linear J3(O) map. `799b7fc79` weakened it decisively.

What the v3 sim did correctly before audit:

- linearity gate max error about `1.4e-16`;
- trace/positivity preserved;
- full-log regression about `2.2e-16`;
- associator floor met on all sampled trajectories;
- zero DPI violations on 36 states, max increase `-0.009207645136616538`.

Why the audit still demoted it:

- the map is block-scalar: transfer spectrum `{1.0 x3, 0.97 x24}`;
- it is exactly a convex mixture of frame automorphisms / diagonal pinching;
- fixed-point set is the whole diagonal simplex, making the selected sigma decorative;
- an associative qutrit surrogate reproduces the entire trajectory dataset to `6.7e-16`;
- the associator gate is tautological under the sampler construction even though the measured trajectory minimum passes;
- classical control is vacuous.

The octonion dynamics leg remains unearned after three attempts: J2(O)/J3(O) primitive mixing, v2 nonlinear filter, and v3 block-scalar map.

## Exact v4 Instrument Spec

The next instrument must not be another stronger-looking version of the same reducible architecture.

Required v4 spec, from the `799b7fc79` audit:

```text
Jordan-positive trace-preserving map on J3(O)
whose transfer matrix does not commute with diagonal pinching,
mixes Peirce blocks non-scalar-wise,
and passes an associative-surrogate-provably-fails gate.
```

Operational gates:

- non-scalar Peirce mixing, not block-scalar frame averaging;
- full spectral-projector log for relative entropy;
- state-independent linear map, not conditioned filter normalization;
- explicit multi-block octonion state pool;
- associative qutrit surrogate must fail to reproduce the trajectory data;
- classical control must test a non-vacuous analogue, not identity compared to itself.

## Open Question

Nonassociative DPI remains open. The Grok-4.5 advisory reported no literature theorem for DPI on the Albert algebra under non-automorphism positive semigroups. Treat that as advisory search pressure, not proof.

Current round ceiling:

```text
exceptional statics earned
+ cone-menu pawl uniformity earned for one map family
+ Alfsen-Shultz dynamical deficit measured
+ Petz/recovery structure measured on associative terrain engines
- nontrivial octonion dynamics not earned
- nonassociative DPI theorem not found/proved
- no Axis0, bridge, manifold, physics, or runtime admission
```

## Related Pages

- [[projects/codex-ratchet/fabrication-modes-catalog]]
- [[projects/codex-ratchet/jordan-octonion-entropy-pawl-floor-receipt-2026-07-08]]
- [[projects/codex-ratchet/engine-field-choi-albert-probe-receipt-2026-07-08]]
- [[projects/codex-ratchet/choi-field-multiaxis-null-albert-stress-receipt-2026-07-08]]
- [[projects/codex-ratchet/CHANGELOG_HARDENING]]
