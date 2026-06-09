---
title: Finite Feynman Path Integral Foundation Packet 2026-06-07
created: 2026-06-07
type: project-receipt-intake
status: scratch-foundation-packet
claim_ceiling: finite foundation scratch packet only; no continuum physics or canonical M(C) admission
framing: codex-ratchet
---

# Finite Feynman Path Integral Foundation Packet 2026-06-07

## Boot rule

Load this after:

1. [[projects/codex-ratchet/read-first]]
2. [[constraint-manifold-architecture]]
3. [[projects/codex-ratchet/current-toe-contender-graveyard-workspace-2026-06-07]] when the task is external-theory/graveyard routing

This page records a Hermes-built finite foundation packet for a Josh-aligned Feynman path-integral analogue. It is not continuum path integration and not physics admission.

## Source artifacts checked

Scratch root:

```text
/tmp/josh_finite_path_integral_packet_001/
```

Files:

```text
finite_path_integral.py
test_finite_path_integral.py
results/finite_path_integral_summary.json
```

Observed rerun:

```text
7 passed in 0.11s
artifact: josh_finite_feynman_path_integral_v0
classification: scratch_foundation_packet_keep_not_admitted
admissible_path_count: 8
noncommuting_AB_BA_distance: 1.414213562373095
naive_unconstrained_control_active: true
promotion_allowed: false
formal_admission_allowed: false
```

The tests were written first. The initial RED run failed because `finite_path_integral` did not exist. The GREEN rerun passed after implementation.

## Safe mathematical shape

The Josh-aligned finite path-integral object is:

```text
finite support S_C
+ active constraints C
+ ordered noncommuting path products
+ path-sum amplitude
+ named probe quotients S/~_M
+ controls
```

Finite path sum:

```text
Σ over admissible paths p in S_C of <target | U_p | start>
```

where `U_p` is an ordered product. The order is load-bearing.

## Scratch configuration

| Field | Value |
|---|---|
| Alphabet | `{A, B}` |
| Path length | `4` |
| Constraint | forbid substring `BB` |
| Carrier | `C^2` scratch carrier |
| Readout | target index `1` |
| Claim ceiling | `scratch_foundation_packet_keep_not_admitted` |

Admissible paths:

```text
AAAA
AAAB
AABA
ABAA
ABAB
BAAA
BAAB
BABA
```

## Root alignment

| Root / layer | Packet behavior |
|---|---|
| F01 finitude | finite path support only |
| N01 noncommutation | ordered operator products are load-bearing |
| Probe-relative identity | paths are equal only under a named probe quotient |
| `M(C)` pressure | finite words satisfying explicit admissibility constraints |
| Carrier/readout | `C^2` scratch carrier with named target-index readout |

This is a pressure packet for `M(C)`, not the full `M(C)` object.

## Observables

### Finitude

Observed:

```text
admissible_path_count = 8
```

### Noncommutation

Observed:

```text
AB vs BA matrix distance = 1.414213562373095
```

So the path integral is not a commutative path count.

### Constraint load-bearing

Observed:

```text
constrained path-sum amplitude = 2 + 0i
unconstrained operator expansion amplitude = 3.414213562373095 + 1.414213562373095i
```

Dropping the constraint changes the finite path sum. `C` is load-bearing.

### Probe-relative quotienting

Observed class counts:

```text
full_word classes = 8
endpoint_parity classes = 2
letter_count classes = 3
```

So path identity is not bare. Paths collapse only under named probes.

### Density/probability erasure

Observed same probability but different complex path amplitudes:

```text
paths: AAAB, AABA
probabilities: 0.5, 0.5
amplitudes:
  AAAB -> 0.707106781186547 + 0i
  AABA -> 0 + 0.707106781186547i
```

This supports the `rho-first is not rho-only` fence: probability/density quotienting can erase path/phase data.

## Gained

- finite Feynman path integral rewritten as sum over admissible paths in `M(C)` pressure-space
- noncommuting path order is load-bearing
- probe-relative path identity is explicit via named quotients
- density/probability quotients can erase phase/path data

## Not gained

- not continuum path integral
- not action extremization or least-action principle
- not physics admission
- not geometry, gravity, or axis claim
- not canonical `M(C)`

## Graveyard / resurrection role

This packet belongs to the live foundation workspace. It is a bridge between external Feynman path-integral language and the Josh-native finite admissibility program.

Future variants should be treated as resurrection/workspace rows, not guaranteed promotions:

| Variant | Why it matters | Status |
|---|---|---|
| `spinor_holonomy_path_integral_variant` | connects path sums to lifted spinor/sign/720/holonomy data | high-priority next packet |
| `state_on_algebra_process_path_integral_variant` | rewrites paths as finite process/state-on-algebra compositions | live foundation variant |
| `finite_action_phase_function_from_constraint_violations` | makes the path phase depend on constraint violation/admissibility pressure | candidate variant |
| `retrocausal_boundary_condition_path_sum_variant` | tests boundary-conditioned admissible histories without primitive time/causality | open variant |
| `Hopf_torus_sheet_path_sum_variant` | routes path sums through candidate Hopf/Weyl sheet structure | blocked until carrier relation is clearer |

## Suggested next queued packet

Suggested next queued packet:

```text
spinor_holonomy_path_integral_variant
```

Minimum contract:

```text
finite path set S_C
ordered SU(2)/spinor transport operators
closed-loop sign/holonomy observable
probe quotients that erase vs preserve sign/path data
reverse-order and density-only controls
claim ceiling: scratch_foundation_packet_keep_not_admitted
```

This is the natural continuation because it touches the currently important fence:

```text
rho-first is not rho-only
```

and the spinor/vector surplus:

```text
sign, holonomy, and path data can be invisible under density/Bloch/probability readouts.
```

## Claim ceiling

This page records a finite foundation packet that ran locally. It does not admit:

- full `M(C)`
- no QIT engine
- spinor carrier finality
- Hopf/Weyl/chirality geometry finality
- Axis0 / Xi / Phi0
- gravity, dark sector, cosmology, Standard Model, GR, or physics
- continuum Feynman path integral
- canonical process status

Promotion requires a later result with an explicit gate.
