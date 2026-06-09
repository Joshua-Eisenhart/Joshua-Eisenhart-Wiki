---
title: Dual Carnot Szilard QIT Engine Witness 2026-06-09
created: 2026-06-09
updated: 2026-06-09
type: project
status: sim-target design / source-processing fold
claim_ceiling: bounded witness design only; no QIT-engine admission, no M(C) admission, no Axis0 closure, no physics claim
tags:
  - codex-ratchet
  - qit-engine
  - carnot
  - szilard
  - dual-stack
  - sim-target
  - hopf
  - weyl
  - source-processing
sources:
  - projects/codex-ratchet/qit-axes-terrain-operator-fold-2026-06-09.md
  - queries/packet-f-axes-math-apple-notes-dump-extraction-2026-05-19.md
  - /Users/joshuaeisenhart/Codex-Ratchet/system_v5/julia_carrier/eng_carnot_axiswired_julia_results.json
  - /Users/joshuaeisenhart/Codex-Ratchet/system_v5/julia_carrier/eng_szilard_axiswired_julia_results.json
  - /Users/joshuaeisenhart/Codex-Ratchet/system_v6/receipts/screenshots_math_report_20260609.md
---

# Dual Carnot Szilard QIT Engine Witness 2026-06-09

## Purpose

This page saves the 2026-06-09 correction that Carnot and Szilard should not be treated as rival complete engines. For the QIT-engine lane, they are two legality/readout grammars that must be **dual-stacked on the same finite QIT carrier**.

Safe short form:

```text
Carnot contributes thermodynamic legality.
Szilard contributes measurement / memory / feedback legality.
The QIT-engine witness is their noncommuting interaction on a shared psi/rho carrier.
```

This is a sim-target design note, not a proof or admission page.

## Checked source anchors

Carnot finite-map result checked:

- `/Users/joshuaeisenhart/Codex-Ratchet/system_v5/julia_carrier/eng_carnot_axiswired_julia_results.json`

Observed in the checked slice:

```text
engine = Carnot
classification = tool_lego_fit_probe
all_pass = true
promotion_allowed = false
```

Szilard finite-map result checked:

- `/Users/joshuaeisenhart/Codex-Ratchet/system_v5/julia_carrier/eng_szilard_axiswired_julia_results.json`

Observed in the checked slice:

```text
engine = Szilard
classification = tool_lego_fit_probe
all_pass = true
promotion_allowed = false
```

Packet F extraction:

- [[packet-f-axes-math-apple-notes-dump-extraction-2026-05-19]]

Axis/terrain/operator fold:

- [[projects/codex-ratchet/qit-axes-terrain-operator-fold-2026-06-09]]

Important correction: do not summarize the Carnot packet as simply failed unless citing the exact failing result surface. The Julia result checked here reports `all_pass=true` under a no-promotion ceiling.

## Core correction

Bad reading:

```text
Carnot OR Szilard is the QIT engine.
```

Also bad:

```text
Carnot and Szilard are just metaphors, detached from the channel math.
```

Working reading:

```text
QIT-like engine witness
=
shared finite QIT carrier
+ Carnot thermodynamic legality layer
+ Szilard measurement-memory-feedback legality layer
+ deductive loop
+ inductive loop
+ noncommuting schedule/order witness
```

Without the QIT carrier and channel algebra, Carnot/Szilard are analogies. Without the dual Carnot/Szilard legality stack, a narrow QIT channel sim is too thin to resemble the intended engine.

Related current router: [[projects/codex-ratchet/two-engine-winlose-carnot-szilard-pattern-2026-06-09]] preserves the paired Type1/Type2 WIN/LOSE pattern, Carnot loop orders, loop-selected readout rule, and finite discriminator result.

## IGT loop-readout layer over Carnot order

Owner correction, 2026-06-09: the Carnot-like order is not an unordered symbolic square. The two directed stroke orders are:

```text
Se -> Ne -> Ni -> Si
Se -> Si -> Ni -> Ne
```

The paired IGT stage word stores two loop components, but an active engine loop reads only its own selected component.

Example:

```text
Type 1 outer loop at WINlose reads WIN
```

Example:

```text
Ni stage word loseLOSE may contribute lose or LOSE depending on which loop is active.
```

Compact map:

| Engine | Loop | Carnot order | Active readout sequence |
|---|---|---|---|
| Type 1 | outer / deductive | Se -> Ne -> Ni -> Si | LOSE -> WIN -> LOSE -> WIN |
| Type 1 | inner / inductive | Se -> Si -> Ni -> Ne | win -> win -> lose -> lose |
| Type 2 | outer / inductive | Se -> Si -> Ni -> Ne | WIN -> WIN -> LOSE -> LOSE |
| Type 2 | inner / deductive | Se -> Ne -> Ni -> Si | lose -> win -> lose -> win |

This expands degrees of freedom inside a constrained geometry: four stage words, two Carnot cycles, two engine placements, loop-selected readouts, sign scaffold, and operator placement.

## Shared carrier requirement

Bad version:

```text
Carnot sim uses one state object.
Szilard sim uses another state object.
Compare summaries later.
```

Target version:

```text
one shared carrier
both legality layers act on it
then D o I and I o D are compared
```

Minimum carrier:

```math
\rho \in \mathcal D(\mathbb C^2)
```

Better carrier:

```math
\psi_L,\psi_R\in S^3\subset\mathbb C^2
```

with:

```math
\rho_L=\psi_L\psi_L^\dagger
```

```math
\rho_R=\psi_R\psi_R^\dagger
```

Weyl split:

```math
H_L=+H_0
```

```math
H_R=-H_0
```

Best bounded tool-test carrier:

```text
small finite spinor network
with psi_L / psi_R at nodes
and edge couplings carrying noncommutative updates
```

## Deductive and inductive loops

Deductive loop = constraint-first / legality-first / closure loop.

It asks:

```text
Given constraints C, which transitions remain admissible?
```

One compact form:

```math
D = U\circ E\circ U\circ E
```

Semigroup form:

```math
D=e^{\tau_R L_R}e^{\tau_C L_C}
```

Inductive loop = probe / measurement / feedback / expansion loop.

It asks:

```text
Given a probe result, which update becomes admissible?
```

One compact form:

```math
I = E\circ U\circ E\circ U
```

Semigroup form:

```math
I=e^{\tau_C L_C}e^{\tau_R L_R}
```

The basic order witness:

```math
\Delta_{DI}(\rho)=D(I(\rho))-I(D(\rho))
```

or:

```math
g_{DI}(\rho)=\|D(I(\rho))-I(D(\rho))\|_1
```

If this gap is absent under the real carrier, the dual stack is not doing N01/order-sensitive QIT work. If the gap appears and commuting/label controls erase it, the witness is meaningful.

## Carnot layer role

Carnot contributes thermodynamic legality:

```text
open / closed strokes
isothermal / adiabatic analogues
entropy bookkeeping
no-free-work controls
cycle closure checks
gradient/spectral generator split
```

Closed/spectral stroke:

```math
\rho\mapsto U\rho U^\dagger,\quad U=e^{-iHt}
```

Entropy is preserved:

```math
S(U\rho U^\dagger)=S(\rho)
```

Open/gradient stroke:

```math
\frac{d\rho}{dt}=\mathcal L(\rho)=-i[H,\rho]+\sum_k\left(L_k\rho L_k^\dagger-\frac12\{L_k^\dagger L_k,\rho\}\right)
```

Packet F uses this to separate finite-gradient algebra from finite-spectral algebra.

Carnot is most useful for:

| Axis | Carnot-facing role |
|---|---|
| Axis0 | entropy / Clausius / cut readout pressure |
| Axis1 | open/closed or CPTP/unitary legality |
| Axis2 | bath / chart / representation legality |
| Axis4 | stroke order |
| Axis5 | gradient vs spectral generator class |
| Axis6 | order / precedence when substages compose |

## Szilard layer role

Szilard contributes measurement / memory / feedback legality:

```text
probe
measurement channel
memory write
conditional update
reset
Landauer cost
```

Measurement channel:

```math
\mathcal M(\rho)=\sum_m P_m\rho P_m
```

Conditional branch:

```math
\rho_m=\frac{P_m\rho P_m}{\operatorname{Tr}(P_m\rho)}
```

Memory write:

```math
\rho\otimes |0\rangle\langle0|
\mapsto
\sum_m P_m\rho P_m\otimes |m\rangle\langle m|
```

Reset legality:

```math
W_{reset}\ge kT\ln 2\cdot H(M)
```

Szilard is most useful for:

```text
probe-relative distinguishability
measurement update
memory preservation
reset legality
Landauer accounting
information-to-work comparison
```

## Axis placement in the dual stack

| Axis | Dual-stack role |
|---|---|
| Axis0 | entropy / coherent-information / shell-cut readout; not a stage bit |
| Axis1 | open vs closed / CPTP vs unitary / expand-compress legality |
| Axis2 | direct vs conjugated frame / bath or chart lens |
| Axis3 | inner/fiber vs outer/base loop; IN/OUT flux remains a candidate overlay |
| Axis4 | deductive vs inductive order |
| Axis5 | finite-gradient vs finite-spectral generator algebra |
| Axis6 | operator-first vs terrain-first / signed operator precedence |

## Minimal sim object

Working name:

```text
dual_stack_carnot_szilard_hopf_weyl_qit_probe
```

State:

```text
rho_L, rho_R
or psi_L, psi_R with density reductions
```

Channel families:

```text
U_H       spectral/unitary
Lambda_L  gradient/Lindblad
M_P       measurement/probe
R_M       memory reset/update
```

Deductive loop:

```math
D=U_H\circ \Lambda_L\circ U_H\circ \Lambda_L
```

Inductive/Szilard loop:

```math
I_{Sz}=R_M\circ \mathcal M\circ \Lambda_L\circ U_H
```

Dual-stack comparison:

```math
\rho_{DI}=D(I(\rho))
```

```math
\rho_{ID}=I(D(\rho))
```

Observables:

```math
\|\rho_{DI}-\rho_{ID}\|_1
```

```math
S(\rho_{DI})-S(\rho_{ID})
```

```math
I_c(A\rangle B)_{\rho_{DI}}-I_c(A\rangle B)_{\rho_{ID}}
```

```math
W_{reset}-kT\ln2\cdot H(M)
```

## Required controls

| Control | Expected use |
|---|---|
| commuting control | replace noncommuting operators with same-basis commuting ones; order gap should vanish |
| no-measurement Szilard control | remove measurement/memory branch; feedback advantage should disappear or become undefined |
| no-bath Carnot control | remove open/CPTP branch; thermodynamic exchange should collapse to unitary orbit |
| chirality erasure | set `H_L=H_R`; L/R asymmetry should vanish |
| schedule reversal | compare `D o I` vs `I o D`; N01 gap should be order-sensitive |
| label shuffle | shuffle labels while keeping raw operations; label-only claims should fail |

## Tool-testing role

This witness is useful because each rich tool has a natural bounded job.

| Tool family | Natural job in the witness |
|---|---|
| `QuantumOptics.jl` / `dynamiqs` | density evolution, Lindblad/CPTP strokes |
| `z3` / `cvc5` | legality constraints, impossible reset/free-work controls |
| `sympy` / `Symbolics` | exact commutators and channel identities |
| `geomstats` / `Manifolds.jl` | Hopf/Bloch/geodesic distances |
| `clifford` / `torch_ga` | spinor/geometric product variants |
| `PyG` | finite spinor-network message passing |
| `e3nn` / `e3nn_jax` | equivariant update under rotations |
| `ITensors` / `quimb` | cut-state / shell contraction |
| `GUDHI` / `TopoNetX` / `XGI` | topology of basin / shell / hypergraph structure |

## Success criteria for this phase

This is tool-testing and base-ladder sim work, not full proof.

Sufficient for this phase:

```text
1. The same finite carrier runs.
2. Both deductive and inductive loops run.
3. Carnot legality and Szilard legality are both represented.
4. D o I and I o D produce a measurable N01 order gap.
5. Controls erase the gap where expected.
6. Rich tools compute real intermediate objects.
7. Julia/JAX/PyTorch independently reproduce core scalars or report a useful divergence.
```

Not required here:

```text
final M(C)
final Axis0 bridge
final 64-state closure
full physics interpretation
canonical QIT-engine admission
```

## Relation to the current sim ladder

This witness should sit at the base tool/sim layer:

```text
tool capability / tool-in-sim tests
-> same-carrier dual-stack witness
-> 64-cell decoding matrix
-> axis-independence discriminators
-> later M(C) / bridge work
```

It is a good candidate for the next bounded Hermes/Wizard or codex2 sim packet because it keeps the carrier small while giving the tools real work.
