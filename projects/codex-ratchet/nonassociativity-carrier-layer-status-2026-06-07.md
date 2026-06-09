---
title: Nonassociativity Carrier Layer Status 2026-06-07
type: project-status
created: 2026-06-07
updated: 2026-06-07
status: verified-current-snapshot
claim_ceiling: status and receipt routing only; no admission
framing: codex-ratchet
---

# Nonassociativity Carrier Layer Status 2026-06-07

## Scope

This is a Hermes controller reconciliation of the Claude/Codex non-associativity carrier-layer wave after the previous live session collapsed.

Machine receipt:

```text
projects/codex-ratchet/nonassociativity-carrier-layer-status-2026-06-07.hermes-verification.json
```

Claim ceiling: status/receipt routing only. Every repo artifact named here remains `scratch_diagnostic` with `promotion_allowed=false` and `formal_admission_allowed=false`. This page does not admit final `M(C)`, QIT-engine, carrier finality, Axis0, bridge, gravity, physics, Standard Model, GR, or canonical-by-process status.

## Current checked status

Hermes reran `scripts/validate_three_engine_sim_result.py --require-pytorch` on the current envelopes. All six returned `ok=true`.

| Rung | Current observed status | Safe reading |
|---|---|---|
| Associator | `foundation_r3_associator_xhigh_envelope_results.json` validator `ok=true`; prior strict panel and fresh source audit clean | genuine R3 bracketing scratch evidence: `H` has zero associator, `O` has nonzero associator |
| Alternativity | current JAX leg derives the antisymmetry defect from bound Cayley-Dickson table entries; grok-4.20 + grok-4.3 + Gemini all `GENUINE`; validator `ok=true` | genuine scratch evidence that `O` is disciplined non-associative while `S` is not alternative |
| Sedenion zero-divisor | current v2 derives zero-product equations from computed `O`/`S` structure constants and witness vector entries; grok-4.20 + grok-4.3 + Gemini all `GENUINE`; validator `ok=true` | genuine scratch evidence for the `O` division / `S` zero-divisor carrier break |
| J3(O) Jordan | current v2 derives Jordan/raw residual components from bound `J3(O)` entries and octonion structure constants; grok-4.20 + grok-4.3 + Gemini all `GENUINE`; validator `ok=true` | genuine scratch evidence for the octonionic Jordan observable side |
| G2 automorphism | xhigh derives derivation constraints and kernel/RREF relations; grok-4.20 + grok-4.3 + Gemini all `GENUINE`; validator `ok=true` | genuine scratch evidence for `dim Der(O)=14` / `g2` symmetry pressure |
| Octonion-Cl(6) link | initial current file split: Gemini and codex2 low/medium flagged precomputed residual binding; Hermes hardened the JAX leg to derive the witness anticommutator entry from bound `L_e1` matrix entries; rerun and envelope validator `ok=true`; grok-4.20 + grok-4.3 + Gemini and codex2 low/medium/high/xhigh now all `GENUINE` | genuine after hardening, still scratch only: octonion left action gives a finite Cl(0,6)-style carrier witness |

## Concrete values to carry forward

```text
Associator: H max norm 0.0; O max norm 2.0; O witness basis [1,2,4]; z3/cvc5 O-all-zero UNSAT -> erased SAT.
Alternativity: O antisymmetry defect 0.0; S antisymmetry defect 2.0.
Sedenion: O zero-divisor witness blocked; S zero-divisor witness product = 0 under computed product equations.
J3(O): Jordan identity residual derives to zero for Jordan product; raw/non-Jordan control flips.
G2: dim Der(R,C,H,O) = 0,0,3,14; O forced-commutative control changes dimension to 21; H-embedded control changes dimension.
Octonion-Cl(6): octonion first-six generated rank 64, spinor dimension 8; quaternion control rank 4, spinor dimension 2; wrong-sign anticommutator UNSAT -> erased SAT after the v2 matrix-entry SMT hardening.
```

## Methodological hardening from this wave

The repeated failure mode is now explicit:

```text
precompute a count/residual/rank/dimension in JAX or Julia
-> feed that number to z3/cvc5
-> let the solver re-check the number
```

That is decorative unless the solver derives the structural fact from bound finite-object coefficients.

Safe rule:

```text
SMT must derive product, associator, Jordan residual, derivation dimension, zero-divisor, rank, or anticommutator facts inside the solver from bound structure constants / entries / coefficients. It must not merely re-check a precomputed scalar count or residual.
```

The Cl(6) row is the useful live example: coefficient-level binding got a split panel; deriving the anticommutator witness entry from bound matrix entries made the dissenters flip to `GENUINE`.

## Placement rule

Non-associativity is root-native but still rung-later by current evidence.

Safe wording:

```text
Non-associativity is a natural expression of a=a iff a~b applied to grouping.
Current receipts place it as R3 carrier/bracketing pressure.
It should not be promoted to an R1/R2 root constraint unless a bounded discriminator shows that erasing associator sensitivity changes the R1/R2 admissible set itself.
```

## Next controller actions

1. Build `nonassoc_root_vs_carrier_discriminator`: does associator erasure change R1/R2 admissibility, or only R3 carrier/readout bracketing?
2. Build minimal `M(C)` profile v0 before bridge/physics/readout claims.
3. Continue `spinor_holonomy_path_integral_variant` and cross-model readout matrix v0 only under the explicit finite support/probe/control contract.
4. Keep all rows here under `scratch_diagnostic` unless a later repo admission gate changes them.
