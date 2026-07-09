# Fabrication Modes Catalog

## Status

Reusable audit doctrine distilled from the July 2026 Codex-Ratchet fabrication-audit campaign, including the exceptional-math round. This page is not a new proof surface. It is a failure-mode router for future audits.

Claim ceiling: audit doctrine only. Each row records a mode, the one-line diagnostic, and the commit where this campaign caught or named it.

## Catalog

| Mode | One-line description | Caught in commit |
| --- | --- | --- |
| Aliased controls | The control reuses the witness object or path byte-for-byte, so the ablation never reruns. | `854fef5b3` |
| Predicate controls | The control makes the predicate false by construction instead of testing the mechanism. | `854fef5b3` |
| Self-comparison controls | Null and witness compare a run to itself, so the reported gap cannot falsify the claim. | `81d712ae6` |
| Hardcoded drifts | Reported pawl drift or lock values are source literals, not computed measurements. | `81d712ae6` |
| Hardcoded verdicts | `lock=True`, pass booleans, or verdict strings are assigned unconditionally rather than derived from the measurement. | `81d712ae6` |
| Label-keyed constants | Engine/type labels choose numeric constants, so the "engine split" tracks injected labels rather than dynamics. | `e7629ef19` |
| By-construction separations | Slots or stages are distinct only because the author gave them distinct positions or names. | `22735ca16` |
| Label arithmetic | Depth or count claims are arithmetic over authored face strings, not over independently measured structure. | `81d712ae6` |
| Filter-lag-as-memory | A finite-time exponential smoother lag is relabeled as hysteresis, path dependence, or basin memory. | `34a824b42` |
| Negligible-drive evidence | A drive too weak to challenge the state is used to claim resistance or memory. | `709bc8352` |
| Coupling-window blindness | A global failure/success claim hides the real threshold window where behavior flips. | `709bc8352`, `81d712ae6` |
| Tautological threshold gate | A pass condition like `10*tau >= 10*tau` cannot fail and adds no evidence. | `709bc8352` |
| Tautological subgroup gate | A symmetry gate samples only a subgroup constructed to preserve the tested object. | `9eafe5a63` |
| Max-statistic sampler floor | A gate passes because the sampler is built to exceed the floor, not because the dynamics independently earns it. | `799b7fc79` |
| Diagonal-shadow formula misuse | A diagonal relative-entropy formula is applied to a non-diagonal fixed point/reference. | `4a8c3cc5e` |
| C-slice confinement | A claimed nonassociative flow stays inside an associative complex slice, so the octonion content is decorative. | `4a8c3cc5e` |
| Name-overclaim on special spin factors | J2(O) is called an exceptional rung even though the spin-factor dynamics does not exercise the Albert exceptionality. | `4a8c3cc5e` |
| Nonlinear conditioned-filter DPI | A state-dependent normalized branch is tested as though DPI for linear channels applied. | `4a8c3cc5e` |
| Block-scalar reducibility | The transfer matrix is scalar on Peirce/off-diagonal blocks, so the "exceptional" map reduces to frame averaging. | `799b7fc79` |
| Associative surrogate reproduction | An associative qutrit surrogate reproduces the entire data table, proving zero nonassociative discrimination. | `799b7fc79` |
| Vacuous identity control | The classical control compares identity to identity, so zero violations do not test the proposed mechanism. | `799b7fc79` |
| Algebraic-identity erasure | An erasure control collapses because the same function and same inputs are evaluated twice. | `e7629ef19` |
| Count-only overclaim | Matching a tempting dimension is treated as structure before product/action identities are tested. | `9eafe5a63` |
| Theorem-guaranteed zero as discovery | A theorem-guaranteed pass is presented as a new grid finding instead of instrument validation. | `9eafe5a63` |
| Decorative sigma/fixed point | A chosen reference looks meaningful but cancels from the map or lies in a whole fixed-point face. | `799b7fc79` |

## Audit Use

Before accepting a new survivor, ask:

1. Did the control rerun an independent path, or is it aliased/self-compared?
2. Is the claimed signal computed, or encoded in labels, constants, thresholds, or authored strings?
3. Does a classical or associative surrogate reproduce the whole table?
4. Does the sampled state pool actually exercise the algebraic feature named in the claim?
5. Does the formula match the object actually used, especially for spectral logs and non-diagonal references?
6. Is a theorem-guaranteed pass being reported as discovery rather than instrument validation?

## Related Pages

- [[projects/codex-ratchet/exceptional-math-round-2026-07-08]]
- [[projects/codex-ratchet/overclaim-kill-switches-2026-06-19]]
- [[projects/codex-ratchet/sim-evidence-and-status-label-discipline-2026-06-19]]
- [[projects/codex-ratchet/CHANGELOG_HARDENING]]
