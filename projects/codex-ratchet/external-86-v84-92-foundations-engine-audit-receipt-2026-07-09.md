# External 86 / v84 / 92 Foundations and Engine Audit Receipt

Date: 2026-07-09

Status: fresh executable audit, bounded repair added, no canon promotion and no Lev state mutation.

## Authority and lineage

Live code authority for this audit:

`/Users/joshuaeisenhart/Codex-Ratchet`

The Desktop archives are external intake artifacts, not live repo authority:

| Artifact | SHA256 | Files | Role |
|---|---|---:|---|
| `86.zip` | `abb9596ab4675ddcbefb61a20908087565ba6167996ec6e55a187241eb44306f` | 437 | direct parent of 92 |
| `constraint_core_unified_v84_plus_v7runner_20260708.zip` | `319462f941bac25186750cd5c9643ea15749f4b107b9d66a321d11c02f690639` | 528 | separate integration and replication branch |
| `92.zip` | `8518e88a2a99c5bc02061c7d050a58e3fdae94e41a921fa7825254a23cebb834` | 447 | 86 plus five source/result pairs |

`92.zip` is not the successor of the v84-plus-runner packet. The two packages carry different work and neither supersedes the other.

The five 86-to-92 additions are:

- Alfsen-Shultz dynamical-correspondence deficit
- L5 Schmidt shells
- L6 BKM shell metric / connection
- Petz DPI forces the pawl
- finite modular/Umegaki identity

## What actually ran

Runtime:

```text
/Users/joshuaeisenhart/.local/share/sim-stack/bin/python3
```

The environment doctor passed both its normal and `--skip-julia` routes. No package install or repo-local environment was introduced.

Fresh `92.zip` full harness:

```text
130 pass / 0 fail / 0 skip -> GREEN
```

Runner SHA256:

`9bb0a55173336f1522fdcdf219bba4ace9cc989a2351f9978484746f2aee5c17`

Report SHA256:

`baf1429ffec2700b1159418b5d4915a8ad4c87b45f2101a3d0650b4d4e629d06`

This is a real execution result, including JAX, PyTorch, and Julia validators. It is not by itself a scientific proof: much of the harness checks exit status and expected output tokens.

All five new v92 programs also exited zero when rerun directly. Their contract audit failed `15` checks: every file lacks a module-level classification, `TOOL_MANIFEST`, and `TOOL_INTEGRATION_DEPTH`. None is process-eligible for canonical admission as supplied.

The v84 package-held report says `123 pass / 0 fail / 0 skip`. That report was inspected, but the full v84 harness was not independently rerun in this audit. Its two replication packets were rerun from fresh stranger seeds.

## Scientific verdicts

| Probe | Finite result that survives | Claim that does not survive |
|---|---|---|
| Alfsen-Shultz | selected Jordan-derivation residuals and one pair-commutator witness | no all-observable correspondence theorem and no computed 52-dimensional `f4` span |
| L5 Schmidt | radius decreases while entropy rises on one restricted Schmidt family | no tori, nested sets, connection, holonomy, or independently measured flux |
| L6 BKM | one local BKM/Umegaki Hessian match and one depolarizing contraction | no connection; the one-dimensional curvature reading is a coordinate artifact; the old non-CPTP tangent control is malformed |
| Petz/DPI | finite no-violation and recovery examples | no uniqueness or forcing of Umegaki; all four implemented family members pass the same positive criterion |
| finite modular identity | selected full-rank qubit modular expressions agree with Umegaki; swapped and singular controls fire | no BKM extraction, thermal time, terrain provenance, or universal forcing |

The live repo already holds stronger bounded versions of the Alfsen, Petz-family, and modular checks. The external copies were not imported as replacements.

## Grok 4.5 pressure

The xAI API was called as actual model `grok-4.5`, not simulated by another model.

Persisted response ID:

`676e6453-275e-948a-88c5-4b17bc82b1c6`

Prompt SHA256:

`458f54601da6e8575826074e20154a1eabef612ac3951ef2dc3a328737685df4`

Receipt:

`/Users/joshuaeisenhart/Codex-Ratchet/system_v7/constraint_core/sims_and_scripts/grok45_v92_foundations_pressure_20260709.json`

Grok independently reached the same ceiling: the bounded modular/Umegaki scalar identity survives; the correspondence, shell/flux, intrinsic-curvature, and Umegaki-forcing narratives do not.

Classification remains `external_pressure_not_proof`.

## Engine teeth: fresh stranger seed

The v84 replication seed `20260709` was selected before opening either `expected_ours.json`.

### Sixteen-stage re-identification

Result: **PASS**

- full affine maps: `16/16` stages correctly re-identified
- maximum self-noise: `2.304e-15`
- minimum nearest-wrong distance: `0.2769475`
- SVD-only proxy: `7/16`
- chirality mirror pairs collapsed by SVD: `3`

This is real finite evidence that the 16 stage channels do distinguishable work under the full affine representation and that a weaker spectral proxy fakes collapse. It is not yet evidence for 64 unique reasoning personalities.

### Type-2 order-carried replication

Result: **FAIL**

- ordered distance: `0.8944733859`
- unordered distance: `0.0004859447`
- self-null band: `0.0003244589`
- minimum segment R2: `0.9999999996`

Order is strongly detectable, but the stronger claim that the two loops become equivalent after best permutation failed because unordered distance remained above the null band.

The package's reference seed `0` passed that criterion, while its related 20-seed context reports `90%` above-band cases. The right reading is instability of the stronger content-equivalence claim, not a green Type-2 theorem.

## Geometry / entropy repair

The supplemental L7 program computes a real Berry holonomy but falsely says it derives L5's asserted `+2*pi*delta_r` flux. Its own computed formula is `-pi*delta_r`, a sign and factor-of-two mismatch. It also incorrectly calls a single closed-loop Berry phase pure gauge.

A new bounded repair was added:

`/Users/joshuaeisenhart/Codex-Ratchet/system_v7/constraint_core/sims_and_scripts/schmidt_bkm_berry_dual_ratchet_repair_sim.py`

Result:

`PASS_BOUNDED_REPAIR`

Contract lint:

`0` violations.

Fresh read-only fabrication audit: `found_fabrication=false`. It independently reproduced the finite identities. Low-severity receipt issues were repaired before hashes were frozen: all global-bundle naming was removed, the partial-trace check now compares the full reduced matrix, the four-edge rectangle orientation is explicit, and exact SymPy derivatives establish continuous radius decrease and entropy increase on `0 < eta < pi/4` instead of inferring them from five samples.

Measured results:

- Umegaki Hessian gives `g_eta_eta=4`, maximum error `8.88e-16`.
- Spectral BKM gives the same metric, maximum error `8.88e-16`.
- Pulling `g_rr=1/(1-r^2)` back through `r=cos(2 eta)` gives the same constant metric, error `2.66e-15`.
- A depolarizing CPTP map contracts the tested BKM metric.
- A unitary basis change preserves it within `4.44e-16`.
- A nonpositive Bloch amplifier increases the metric and produces a `-0.125` eigenvalue on the pure-state kill control.
- The global Schmidt phase family has Berry curvature, while the one-qubit marginal erases phase.
- The Berry rectangle / external L5 flux ratio is `-0.4999999898`, independently rejecting the claimed normalization.
- The full-rank BKM formula correctly refuses the pure-state support boundary.

The real finite dual object is now clearer: entropy geometry lives on the reduced full-rank state family, while Berry phase lives on the global phase-carrying pure-state bundle. They are related through the Schmidt parameter but cannot be collapsed into one marginal-radius scalar.

This does not establish nested tori, a global bundle, Chern quantization, a manifold spine, terrain forcing, Axis0, or physics.

## Lev boundary

The v84 Lev adapter material is structurally parseable as evidence input, but this audit found no fresh ProofBundle-compatible, idempotent, end-to-end no-mutation consumer receipt for these packet results in `/Users/joshuaeisenhart/lev-main`.

No Lev file was changed and no mesh, graph, ontology, MMM, or object state was mutated.

Before live consumption, the lane still needs:

- a current adapter with durable RunEvidence
- proof-bound trace, gate, and claim receipts
- idempotency tests
- enforcement of `promotion_allowed=false`
- an end-to-end no-state-mutation test

## Exact claim ceiling

The engines are not all fake: the 130-case process really executes, the three numerical runtimes are exercised, and the fresh 16-stage affine re-identification has measurable teeth.

The system is not yet the whole claimed machine. The intended architecture has 16 intelligence-bearing stages; the 64-row surface is only their provisional four-substage expansion. This intake does not establish four internal substages per stage, complete Type-1/Type-2 bidirectional science, learning, QIT perception, object formation, MMM/ontology driving, Axis0 closure, a full geometry/entropy co-ratchet, or live Lev mesh utility.

The deepest earned result from this intake is narrower and useful: a finite modular/Umegaki identity, an exact local BKM metric on the Schmidt marginal, a separate real Berry connection on the global phase family, and a fresh stage-noncollapse result with a preserved Type-2 failure.

Full machine-readable audit:

`/Users/joshuaeisenhart/Codex-Ratchet/system_v7/constraint_core/spec_and_reports/EXTERNAL_PACKET_86_V84_92_AUDIT_20260709.json`
