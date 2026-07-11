# Gradient drive: the reason the Ratchet moves

> **RATCHET_V0_3_GRADIENT_DRIVE.** This document specifies a process invariant, not an earned physical theory:
> **constrained distinguishability is the root; a licensed intrinsic gradient is the drive. No gradient, no tooth.**

## 1. Five roles that must not be collapsed

| Role | Function |
|---|---|
| Root | Constrained distinguishability supplies the least installed starting condition. |
| Drive | A finite, intrinsic, obligation-coupled distinction gradient supplies a reason and direction to test movement. |
| MSS | Minimal sufficient structure selects the weakest tested response that still meets the frozen obligation. |
| Gate | Hostile controls decide whether that response is permitted to become a provisional tooth. |
| Pawl | The append-only evidence ledger remembers tests, defeats, dependencies, and reopenings. |

The gradient is not a second primitive and it does not override MSS or controls. MSS without a gradient has no reason to
choose a transition. A gradient without MSS can select needless structure. A gradient and MSS without controls can
ratify an artifact. None of these alone earns a rung.

## 2. Finite gradient before continuum calculus

Freeze a finite run scope, an obligation \(O\), an admissible state \(\sigma_t\), and a candidate update \(u\). Let

\[
V_{t,O}(\sigma)
\]

be a licensed finite functional of unresolved constrained distinctions. It can be a count, weighted count, code length,
or another explicitly typed finite functional. Its definition, orientation, and tolerance are frozen before outcomes.
The directed finite gradient witnessed by update \(u\) is

\[
g_{t,O}(u)=V_{t,O}(\sigma_t)-V_{t,O}(u\sigma_t).
\]

The receipt uses \(|g|>\varepsilon\) to witness a non-flat surface and records the sign convention in words. This is a
finite difference on the current admissible distinction surface; it does not presume a real continuum, infinitesimal
cut, differentiable manifold, or pre-existing object space.

At the root the safe name is **distinction potential** or **pre-entropic drive**. Once a particular entropy type
\(S_\tau\) has itself survived the Ratchet, the same operational relation may be represented as

\[
g^{(\tau)}_{t,O}(u)=\epsilon_O\!\left(S_\tau(\sigma_t)-S_\tau(u\sigma_t)\right),
\]

where \(\epsilon_O\) fixes the obligation-relative orientation. A named entropy formula must not be smuggled into the
root merely because a gradient is required.

## 3. Entropy and geometry are one licensed surface

The drive is not entropy running on an independently installed geometry. The admissible distinctions and their finite
update relations are the current surface. Its accessible/deleted distinctions give the informational reading; its
adjacency, reachability, separation, curvature surrogate, or later earned manifold structure give the geometric
reading. They are co-typed views of one running constraint object.

Consequently, the measured total entropy of a larger system may increase while an obligation-relative unresolved
potential decreases. The receipt must state which functional is being measured. It may not trade silently between
thermodynamic entropy, von Neumann entropy, path entropy, algorithmic description length, unresolved-obligation count,
or any other entropy-like quantity.

## 4. Drive license

A proposed gradient can drive a tooth only when every item below is recorded:

1. **Typed:** its functional, domain, codomain, orientation, tolerance, and finite scope are explicit.
2. **Licensed:** the current rung has enough structure to define that functional without smuggling later structure.
3. **Nonzero:** its magnitude exceeds the frozen tolerance.
4. **Intrinsic:** it arises from the constrained system and obligation, not an injected schedule or result-dependent
   potential.
5. **Obligation-coupled:** at least one candidate update changes the frozen obligation-relative potential.
6. **Freeze-sensitive:** freezing admissible change collapses the drive and prevents the tooth.
7. **Closure-sensitive:** satisfying or removing the obligation collapses its residual drive.
8. **Representation-robust:** admissible relabeling or carrier changes do not manufacture it.

The four gradient-specific hostile controls are `gradient_freeze`, `gradient_closure`, `gradient_injection`, and
`gradient_obligation_coupling`.

## 5. Transition law

| Observed state | Required decision |
|---|---|
| Licensed, nonzero, intrinsic, obligation-coupled gradient; MSS frontier exists; all controls pass | `CLIMB` and record a provisional evidence tooth |
| Magnitude at or below tolerance | `HOLD_NO_GRADIENT` |
| Functional is not licensed at the current rung | `HOLD_UNLICENSED_GRADIENT` |
| Slope is externally injected or result-fitted | `HOLD_EXTRINSIC_DRIVE` |
| Gradient exists but candidate responses do not change the frozen obligation | `HOLD_UNCOUPLED_GRADIENT` |
| New evidence defeats a dependency or earlier drive license | `REOPEN` and propagate invalidation |

A HOLD is a successful process outcome, not a failed experiment. Exploration may continue by changing candidates,
resolution, probes, or the explicitly versioned obligation. It may not pretend the old run climbed. `next_rung` must be
null and `evidence_tooth_recorded` false for every HOLD decision.

## 6. Relationship to objects and canon

Candidate objects remain functional stories: finite presentations that organize surviving distinctions. A surface-level
match does not establish shared internal structure, and an object may be weakened, rebuilt, split, or discarded. The
Ratchet earns only receipt-scoped provisional structure. The hypothesis wiki, source documents, simulations, and named
mathematical towers are proposal reservoirs until they pass the current drive, MSS, and control contract.

Only evidence history ratchets monotonically. Scientific structure remains defeasible because a weaker MSS candidate,
a better functional, a failed gradient license, or a downstream dependency failure can reopen it.

## 7. Executable anchors and their ceiling

- `ratchet/examples/process_fixture.json` demonstrates a licensed nonzero drive and `CLIMB` at synthetic scope.
- `ratchet/examples/no_gradient_hold_fixture.json` demonstrates a flat surface and mandatory `HOLD_NO_GRADIENT`.
- `ratchet/ratchet_kernel.py --self-test` rejects zero-gradient, extrinsic, uncoupled, missing, and numerically false
  drive records.
- Historical gradient simulations—including foundational, cosmogenesis, witness-memory, and Axis0 drive tests—are
  evidence sources for future migrated packets. Their local reruns do not by themselves earn a physical entropy type,
  geometry, cellular automaton, or cosmological rung under v0.3.
