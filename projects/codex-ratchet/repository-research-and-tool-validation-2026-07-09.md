# Repository Research and Tool Validation - 2026-07-09

## Purpose

This page records which external repositories were researched, pinned, tested,
and given a bounded Ratchet role. It is wiki research and routing, not canon.
The executable receipts live in `/Users/joshuaeisenhart/Codex-Ratchet`.

Third-party source checkouts live under `/Users/joshuaeisenhart/GitHub`.
Isolated runtimes live under
`/Users/joshuaeisenhart/.local/share/codex-ratchet`. Nothing here turns the
Desktop into a project repository.

## Validated Repositories

| Repository | Pin | Test state | Bounded useful role | Ceiling |
|---|---|---|---|---|
| PySINDy | `v2.1.0`, `1edf3126...` | six selected upstream tests pass; affine-generator capability receipt passes | identify continuous affine terrain generators from held-out exact derivatives | noisy trajectory perception remains poor; no engine derivation |
| PyKoopman | `v1.2.1`, `61d24f76...` | five selected EDMD tests pass in an old-stack Python 3.11 environment | `Identity + EDMD` with explicit affine coordinate identifies finite beat maps | full distribution, polynomial observable, and neural path quarantined |
| PyDMD | `2025.8.1` in canonical sim stack | package import and bounded discriminator rerun pass | independent spectral/dynamic-mode recognizer for competing finite orders | recognizer, not truth selector |
| deeptime | `v0.4.5`, `79837fdc...` | isolated VAMP runtime passes; bounded discriminator rerun passes | VAMP slow/kinetic feature judge independent of PyDMD | finite two-order discriminator only |
| ALCO | `v1.1.2`, `e10ec05a...` | six upstream GAP test files, zero failures | exact octonion and Albert/J3(O) algebra oracle | no spectral log, entropy, channel, or DPI |
| ResClasses | `v4.7.4`, `89986878...` | loads as ALCO dependency | required exact GAP residue-class support | dependency, not a Ratchet result |
| QICS | `v1.1.3`, `be18e5ef...` | upstream `22 passed`; local oracle 11/11, two byte-identical runs | independent fixed-input Umegaki and CPTP-contraction numerical oracle | associative finite-dimensional numerics; no exceptional Jordan lift |
| Physlib | `a1962508...`, Lean `v4.31.0` | exact `QuantumInfo.Entropy.DPI` build succeeds across 8,617 jobs; zero `sorry`/`admit` hits in the module | machine-checked associative finite-dimensional sandwiched-Renyi and relative-entropy DPI | not J3(O), no exceptional tensor product, no engine result |

## Ratchet Integrations

### Continuous and discrete system identification

`stage16x4_system_id_instrument_v0` makes PySINDy and the bounded PyKoopman
surface load-bearing. PySINDy reconstructs eight exact affine terrain
generators. PyKoopman learns the candidate signed beat maps and schedules.
Destructive controls bite. The four cells, order candidates, source slots,
exact derivative access, and finite house maps remain premises.

### Independent Type-2 trajectory discrimination

`stage_interior_spectral_kinetic_discriminator_v0` gives the same hashed
trajectory contract independently to PyDMD and deeptime. Clean held-out
accuracy is `1.0` for PyDMD and `0.9444444444` for VAMP; temporal shuffle,
block permutation, and reversal collapse to `0.5-0.5555555556`. The validator
passes 18/18.

This proves that the two supplied finite trajectory families are
distinguishable. It does not select which Type-2 order is true.

### Exact exceptional-Jordan algebra

`alco_j3o_exact_oracle_v0` cross-checks the local exact rational J3(O)
formulas against ALCO. It passes 23/23 gates over five frozen cases for product,
trace, determinant, cubic minimal polynomial, quadratic representation,
Cayley-Hamilton, homogeneity, determinant covariance, and the fundamental
formula. A corrupted Fano product is rejected.

This closes an exact algebra-oracle gap. It does not close the entropy gap.

### Associative entropy and DPI

QICS supplies numerical cones for quantum entropy, quantum relative entropy,
operator perspectives, and sandwiched Renyi quantities. Physlib supplies a
separate machine-checked associative DPI theorem path. These are complementary:
QICS is a numeric oracle; Physlib is a formal associative reference.

`qics_entropy_dpi_numeric_oracle_v0` makes the QICS role load-bearing on three
fixed state pairs. Nine solves report `optimal`; QICS and direct spectral
Umegaki values differ by at most `8.16396894531835e-10`. Pinching and
depolarizing maps contract all six pairs with a minimum direct margin of
`0.071557723709512`. Transposition and trace scaling are rejected as non-CPTP
controls before QICS is invoked. The independent validator passes both
byte-identical result files with SHA-256 `5792308a8e6b...`.

Neither repository implements exceptional J3(O) spectral entropy or proves a
Jordan-positive-map DPI. That remains the actual carrier-floor frontier.

## Repositories Researched But Not Promoted

- `Dynamax`: useful state-space machinery, but dependency compatibility did not
  justify another live runtime in this lane.
- `torchcde`: useful only if a continuous-time learned control problem becomes
  explicit; no current Ratchet gate requires it.
- `toqito`: broad QIT utilities overlap the current QuTiP/Dynamiqs/local
  channel stack; no nonredundant exceptional-Jordan function was found.

The rule is not "install every relevant package." A repository is retained
when it contributes a distinct judge, exact oracle, formal theorem surface, or
killable control that the current stack lacks.

## Primary Sources

- [PySINDy](https://github.com/dynamicslab/pysindy)
- [PyKoopman](https://github.com/dynamicslab/pykoopman)
- [PyDMD](https://github.com/PyDMD/PyDMD)
- [deeptime VAMP documentation](https://deeptime-ml.github.io/latest/notebooks/vamp.html)
- [ALCO package](https://bnasmith.github.io/alco/)
- [QICS](https://github.com/kerry-he/qics)
- [Physlib](https://github.com/leanprover-community/physlib)
- [Physlib DPI module](https://github.com/leanprover-community/physlib/blob/master/QuantumInfo/Entropy/DPI.lean)

## Routes

- [[concepts/sindy-koopman-system-identification-for-qit-engines-2026-07-09]]
- [[concepts/dual-ratchet-geometry-entropy-jordan-research-2026-07-09]]
- [[projects/codex-ratchet/engine-16x4-axis6-current-state-2026-07-09]]
- [[projects/codex-ratchet/source-intake/dual-ratchet-math-article-register-2026-07-09]]
