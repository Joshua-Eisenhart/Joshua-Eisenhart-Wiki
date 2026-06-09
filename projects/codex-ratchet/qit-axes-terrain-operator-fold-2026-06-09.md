---
title: QIT Axes Terrain Operator Fold 2026-06-09
created: 2026-06-09
updated: 2026-06-09
type: project
status: source-processed working fold
claim_ceiling: source-routing and sim-target design only; no M(C), QIT-engine, Axis0, bridge, physics, or canonical admission
tags:
  - codex-ratchet
  - qit-engine
  - axes
  - terrains
  - operators
  - taijitu
  - hopf
  - weyl
  - source-processing
sources:
  - concepts/igt-axes-terrain-source-extraction-2026-06-04.md
  - raw/articles/system-v5-reference-docs/TAIJITU_AXES_0_6_EXPLICIT_SYMBOLIC_LAYER copy.md
  - raw/articles/system-v5-reference-docs/JUNGIAN_FUNCTIONS_AND_IGT_EXPLICIT_MATH_GEOMETRY_MAP copy.md
  - raw/articles/system-v5-reference-docs/apple axes terrain operator math.md
  - concepts/operator-math-explicit.md
  - concepts/terrain-laws-and-loop-geometry.md
  - concepts/weyl-flux.md
  - projects/codex-ratchet/physics-model-unique-claim-atlas-2026-06-06.md
  - /Users/joshuaeisenhart/Codex-Ratchet/system_v6/receipts/screenshots_math_report_20260609.md
---

# QIT Axes Terrain Operator Fold 2026-06-09

## Purpose

This page saves the 2026-06-09 Hermes/Fable conversation fold about the actual axes / terrain / operator math so future workers do not have to reconstruct it from chat.

It is a **working fold**, not an admission page. It routes the taijitu / I Ching / Jung / IGT symbolic layer back down to the carrier, terrain laws, operator families, and current sim targets.

Safe use:

```text
source and sim-target router
not final M(C)
not final QIT engine
not Axis0 closure
not physics admission
```

## Source anchors checked in this fold

Primary router:

- [[igt-axes-terrain-source-extraction-2026-06-04]]
- [[projects/codex-ratchet/pre-ai-rosetta-ring-checkerboard-provenance-2026-06-09]] — owner-provenance route for the pre-AI Rosetta spreadsheet and ring-checkerboard / two-Möbius-strip source geometry.
- [[projects/codex-ratchet/two-engine-winlose-carnot-szilard-pattern-2026-06-09]] — current router for the paired Type1/Type2 WIN/LOSE pattern, Carnot loop orders, loop-selected readouts, and the 36 -> 1 discriminator result.

Direct symbolic source:

- `raw/articles/system-v5-reference-docs/TAIJITU_AXES_0_6_EXPLICIT_SYMBOLIC_LAYER copy.md`

Engine/operator source routes:

- `raw/articles/system-v5-reference-docs/JUNGIAN_FUNCTIONS_AND_IGT_EXPLICIT_MATH_GEOMETRY_MAP copy.md`
- `raw/articles/system-v5-reference-docs/apple axes terrain operator math.md`
- [[operator-math-explicit]]
- [[terrain-laws-and-loop-geometry]]
- [[weyl-flux]]

Screenshot reconciliation:

- `/Users/joshuaeisenhart/Codex-Ratchet/system_v6/receipts/screenshots_math_report_20260609.md`

Current full-stack router:

- [[model-convergence-qit-engine-full-stack]]
- [[projects/codex-ratchet/physics-model-unique-claim-atlas-2026-06-06]]

## Claim ceiling

This page preserves a current working map:

```text
root constraints
-> finite admissibility object M(C) still missing
-> finite spinor / density carrier pressure
-> Hopf / Weyl / nested-torus geometry
-> terrain + operator schedule
-> axes 0-6 as readout maps A_i : M(C) -> V_i
-> 8 terrains x 8 signed operators = 64 candidate engine-state lattice
```

It does not promote any of those downstream objects to canonical process status.

## Carrier floor

The local carrier floor is:

```math
\mathcal H = \mathbb C^2
```

A normalized spinor lives on:

```math
S^3 = \{\psi \in \mathbb C^2 : \|\psi\| = 1\}
```

Hopf-coordinate spinor:

```math
\psi_s(\phi,\chi;\eta)
=
\begin{pmatrix}
e^{i(\phi+\chi)}\cos\eta \\
e^{i(\phi-\chi)}\sin\eta
\end{pmatrix},
\quad s\in\{L,R\}
```

Density reduction:

```math
\rho_s = \psi_s\psi_s^\dagger
```

Bloch form:

```math
\rho_s = \frac12(I+r_x\sigma_x+r_y\sigma_y+r_z\sigma_z)
```

Hopf projection:

```math
\pi(\psi)=\psi^\dagger\vec\sigma\psi\in S^2
```

Nested Hopf torus family:

```math
T_\eta=
\{(e^{i\alpha}\cos\eta,e^{i\beta}\sin\eta):\alpha,\beta\in S^1\}
\subset S^3
```

Weyl split:

```math
H_L=+H_0
```

```math
H_R=-H_0
```

Keep the spinor lift `psi` whenever sign, phase, path, or 720-degree holonomy matters. The density quotient `rho=psi psi^dagger` is useful but may erase lifted signal.

## Loop geometry

Fiber / inner loop:

```math
\gamma_f^s(u)=\psi_s(\phi_0+u,\chi_0;\eta_0)
```

This is density-stationary:

```math
\rho_f^s(u)=\rho_f^s(0)
```

Lifted-base / outer loop:

```math
\gamma_b^s(u)=\psi_s(\phi_0-\cos(2\eta_0)u,\chi_0+u;\eta_0)
```

Working distinction:

```text
fiber / inner loop = phase/lift, density-stationary
base / outer loop = density-visible Bloch traversal
```

## Four current base operator families

The current compact operator packet is:

| Token | Current operator meaning |
|---|---|
| `Ti` | z-basis dephasing `D_z` |
| `Te` | x-basis dephasing `D_x` |
| `Fi` | x-axis rotation `R_x` |
| `Fe` | z-axis rotation `R_z` |

Z-dephasing:

```math
Ti(\rho)=(1-q_1)\rho+q_1(P_0\rho P_0+P_1\rho P_1)
```

X-dephasing:

```math
Te(\rho)=(1-q_2)\rho+q_2(Q_+\rho Q_+ + Q_-\rho Q_-)
```

X-rotation:

```math
Fi(\rho)=U_x(\theta)\rho U_x(\theta)^\dagger,
\quad U_x(\theta)=e^{-i\theta\sigma_x/2}
```

Z-rotation:

```math
Fe(\rho)=U_z(\varphi)\rho U_z(\varphi)^\dagger,
\quad U_z(\varphi)=e^{-i\varphi\sigma_z/2}
```

Compact split:

```text
dephasing family = {Ti, Te}
rotation family = {Fi, Fe}
```

## Broader operator backlog preserved from screenshots

The current four-token packet is intentionally smaller than the screenshot / older source menu. The 2026-06-09 screenshot report preserves this backlog:

| Candidate operator family | Why it matters |
|---|---|
| arbitrary-axis Hamiltonian `H_0=n_x sigma_x+n_y sigma_y+n_z sigma_z` | current x/z packet omits a full Pauli-axis Hamiltonian family |
| `sigma_y`-bearing rotations / dephases | no named `R_y` or `D_y` in the current four-token packet |
| projective channel `Pi_P(rho)=sum_k P_k rho P_k` | broader measurement/projection lane |
| normalized filter / POVM-like update `F_Q(rho)=F rho F^dagger / Tr(F rho F^dagger)` | spectral/filter lane from older source language |
| amplitude lowering / raising `D_-`, `D_+` | Pit/Source terrain laws need them |
| projector retention `D_P` | Hill/Citadel terrain laws need it |
| generic Lindblad / GKSL family `D[L]` | terrain laws are broader than two fixed dephases |
| observable probe `p_O(rho)=Tr(O rho)` | readout layer, not an engine operator |
| Axis0 cut functional `Phi_0` | cut/shell coherent-information readout, not an engine operator |

Working correction:

```text
current four-token packet = small x/z operational packet
screenshot / Packet-F material = broader candidate operator backlog
```

Do not replace the current four-token packet casually. Use the backlog to design bounded tool/probe sims.

## Terrain families and eight terrain laws

The four terrain families are:

```text
Se = open dissipative expansion / support transport
Ne = Hamiltonian circulation / tangential flow
Ni = contraction / sink-source amplitude family
Si = retention / invariant strata
```

The eight terrain realizations are:

```text
Type1 / left / IN:  Funnel, Vortex, Pit, Hill
Type2 / right / OUT: Cannon, Spiral, Source, Citadel
```

Generic dissipator:

```math
D_L(\rho)=L\rho L^\dagger-\frac12(L^\dagger L\rho+\rho L^\dagger L)
```

Left sheet / Type1:

```math
X_F^L(\rho_L)=\sum_k D[L_k^{F,L}](\rho_L)-i\epsilon_{F,L}[H_L,\rho_L]
```

```math
X_V^L(\rho_L)=-i[H_L,\rho_L]+\epsilon_{V,L}\sum_k D[M_k^{V,L}](\rho_L)
```

```math
X_P^L(\rho_L)=\gamma_{P,L}D[\sigma_-](\rho_L)-i\epsilon_{P,L}[H_L,\rho_L]
```

```math
X_H^L(\rho_L)=-i[K_L,\rho_L]+\sum_j\kappa_{H,L,j}\left(P_j^{H,L}\rho_LP_j^{H,L}-\frac12(P_j^{H,L}\rho_L+\rho_LP_j^{H,L})\right)
```

Right sheet / Type2:

```math
X_C^R(\rho_R)=\sum_k D[L_k^{C,R}](\rho_R)-i\epsilon_{C,R}[H_R,\rho_R]
```

```math
X_S^R(\rho_R)=-i[H_R,\rho_R]+\epsilon_{S,R}\sum_k D[M_k^{S,R}](\rho_R)
```

```math
X_{So}^R(\rho_R)=\gamma_{So,R}D[\sigma_+](\rho_R)-i\epsilon_{So,R}[H_R,\rho_R]
```

```math
X_{Ci}^R(\rho_R)=-i[K_R,\rho_R]+\sum_j\kappa_{Ci,R,j}\left(P_j^{Ci,R}\rho_RP_j^{Ci,R}-\frac12(P_j^{Ci,R}\rho_R+\rho_RP_j^{Ci,R})\right)
```

## Count discipline

Do not collapse these counts:

```text
4 terrain families = Se, Ne, Ni, Si
8 terrain realizations = Funnel, Cannon, Vortex, Spiral, Pit, Source, Hill, Citadel
4 loop placements = left-fiber, left-base, right-fiber, right-base
16 terrain placements = sheet x loop x terrain family
8 signed operators = 4 base operators x up/down precedence
64 engine states = 8 terrains x 8 signed operators
```

## Taijitu / I Ching Axis 0-6 map

The taijitu doc is proposal-only symbolic support. It does not replace the engine math.

| Axis | Taijitu / symbolic feature | Jung / IGT layer | Math anchor | Current status |
|---|---|---|---|---|
| `Axis 0` | black/white plus enclosing circle | white/yang `Ne,Ni`; black/yin `Se,Si` | `b0=sign(cos(2 eta))`, later `Phi0(rho_AB)` | strong symbolic alignment; cut bridge open |
| `Axis 1` | dot-in-opposite-teardrop split | `{Se,Ni}` vs `{Ne,Si}` | branch split, unitary/CPTP legality candidate | usable symbolic alignment |
| `Axis 2` | dots vs teardrops | `{Se,Ne}` vs `{Si,Ni}` | direct `rho` vs conjugated `V^dagger rho V` | usable symbolic alignment |
| `Axis 3` | inner tail-chasing vs outer fat-tip-chasing | inner/outer token sets | fiber loop vs lifted-base loop | strongest current symbolic read |
| `Axis 4` | clockwise vs counterclockwise spin | `FeTi` vs `TeFi` runtime family | `U o E o U o E` vs `E o U o E o U` | symbolic spin assignment open |
| `Axis 5` | S-curve/lobe/weighting | rotation-class vs dephasing-class tokens | `{Ti,Te}` vs `{Fi,Fe}`; broader FGA/FSA candidate | symbolic overlay open |
| `Axis 6` | up/down reading | judging-first vs perceiving-first | `b6=-b0 b3`; operator-first vs terrain-first | strong symbolic alignment |

Six-line scaffold:

| Line | Axis |
|---|---|
| line 1 | `Axis 6` |
| line 2 | `Axis 5` |
| line 3 | `Axis 3` |
| line 4 | `Axis 4` |
| line 5 | `Axis 1` |
| line 6 | `Axis 2` |

`Axis 0` is the external drive through the six-line space.

## Axis-specific live alternatives

### Axis0 alternatives

```text
b0 = sign(r_z)
local entropy S(rho_bar(eta))
coherent-information shell sum Phi0
Xi_ref
Xi_shell
Xi_hist
```

### Axis3 alternatives

```text
inner/outer fiber-base loop    <- strongest current taijitu read
L/R Weyl chirality             <- geometry layer
Type1/Type2 topology inversion <- older/candidate
IN/OUT flux                    <- Packet F / screenshot candidate
```

### Axis4 alternatives

```text
clockwise/counterclockwise visual spin
FeTi vs TeFi runtime family
U o E o U o E vs E o U o E o U
semigroup commutator [L_R,L_C]
Carnot/Szilard forward/reverse direction
```

### Axis5 alternatives

```text
dephasing vs rotation                       <- current four-token packet
finite-gradient algebra vs finite-spectral algebra <- stronger Packet-F distinction
gradient/GKSL semigroup vs spectral/Hamiltonian group
hot/cold                                    <- Carnot metaphor, not fully formalized
line/wave                                   <- open; not formalized in checked screenshots
```

### Axis6 alternatives

```text
judging-first vs perceiving-first
operator-first vs terrain-first
left pre-composition vs right post-composition
A rho vs rho A
UP/DOWN symbolic reading
b6 = -b0 b3 dependency
```

## Type1 / Type2 stage tables

Critical read rule: `Pattern` is the paired stage word; `Result` is the active loop-selected component. Do not encode an active engine loop as carrying the whole pattern word. Example: Type1 outer at `WINlose` reads `WIN`; a loop in `loseLOSE` may read `lose` or `LOSE` depending on placement.

The two Carnot-style directed loop orders are:

```text
Se -> Ne -> Ni -> Si
Se -> Si -> Ni -> Ne
```

These orders are thermodynamic/engine order, not just symbolic ordering.

Type1 = left / IN / `H_L=+H0`.

| Topology | Terrain | Loop | Order family | Stage token | Axis6 | Signed op | Result | Pattern |
|---|---|---|---|---|---|---|---|---|
| `Se` | `Se-in` | outer / major | deductive | `TiSe` | UP | `Ti↑` | `LOSE` | `LOSEwin` |
| `Ne` | `Ne-in` | outer / major | deductive | `NeTi` | DOWN | `Ti↓` | `WIN` | `WINlose` |
| `Ni` | `Ni-in` | outer / major | deductive | `NiFe` | DOWN | `Fe↓` | `LOSE` | `loseLOSE` |
| `Si` | `Si-in` | outer / major | deductive | `FeSi` | UP | `Fe↑` | `WIN` | `winWIN` |
| `Se` | `Se-in` | inner / minor | inductive | `SeFi` | DOWN | `Fi↓` | `win` | `LOSEwin` |
| `Si` | `Si-in` | inner / minor | inductive | `SiTe` | DOWN | `Te↓` | `win` | `winWIN` |
| `Ni` | `Ni-in` | inner / minor | inductive | `TeNi` | UP | `Te↑` | `lose` | `loseLOSE` |
| `Ne` | `Ne-in` | inner / minor | inductive | `FiNe` | UP | `Fi↑` | `lose` | `WINlose` |

Type2 = right / OUT / `H_R=-H0`.

| Topology | Terrain | Loop | Order family | Stage token | Axis6 | Signed op | Result | Pattern |
|---|---|---|---|---|---|---|---|---|
| `Se` | `Se-out` | outer / major | inductive | `FiSe` | UP | `Fi↑` | `WIN` | `loseWIN` |
| `Si` | `Si-out` | outer / major | inductive | `TeSi` | UP | `Te↑` | `WIN` | `WINwin` |
| `Ni` | `Ni-out` | outer / major | inductive | `NiTe` | DOWN | `Te↓` | `LOSE` | `LOSElose` |
| `Ne` | `Ne-out` | outer / major | inductive | `NeFi` | DOWN | `Fi↓` | `LOSE` | `winLOSE` |
| `Se` | `Se-out` | inner / minor | deductive | `SeTi` | DOWN | `Ti↓` | `lose` | `loseWIN` |
| `Ne` | `Ne-out` | inner / minor | deductive | `TiNe` | UP | `Ti↑` | `win` | `winLOSE` |
| `Ni` | `Ni-out` | inner / minor | deductive | `FeNi` | UP | `Fe↑` | `lose` | `LOSElose` |
| `Si` | `Si-out` | inner / minor | deductive | `SiFe` | DOWN | `Fe↓` | `win` | `WINwin` |

## Next sim-tool target implied by this fold

The useful bounded carrier for testing tools is:

```text
finite nested Hopf-Weyl spinor network
```

Minimum contents:

```text
small graph nodes with psi_L, psi_R in S^3
density reductions rho_L, rho_R
left/right Weyl Hamiltonian signs
inner/fiber and outer/base loop placements
eight terrain laws
four current operators plus candidate backlog hooks
Axis6 signed precedence
Axis0 cut/readout candidate
negative controls: chirality erase, commuting-control, label shuffle, carrier quotient erase
```

Tool roles:

| Tool family | Natural job |
|---|---|
| `geomstats` / `Manifolds.jl` | Hopf/Bloch/manifold distances and geodesic checks |
| `sympy` / `Symbolics` | exact commutators, identities, symbolic channel checks |
| `clifford` / `torch_ga` | spinor/geometric-product candidate couplings |
| `e3nn` / `e3nn_jax` | equivariant update checks |
| `PyG` | spinor-network message passing |
| `ITensors` / `quimb` | cut/shell contraction and tensor-network readouts |
| `GUDHI` / `TopoNetX` / `XGI` | topology, filtration, incidence, hypergraph structure |
| `z3` / `cvc5` | order impossibility and legal/illegal controls |

## Closeout reading

This fold should be read before broad claims that mention:

- Axis 0-6;
- taijitu / I Ching / yin-yang mapping;
- terrain/operator schedules;
- signed operators;
- 64 engine states;
- Carnot/Szilard axis-wired probes;
- nested Hopf / Weyl QIT engine carriers.

It should be paired with [[projects/codex-ratchet/dual-carnot-szilard-qit-engine-witness-2026-06-09]] for the immediate dual-stack sim target and [[projects/codex-ratchet/two-engine-winlose-carnot-szilard-pattern-2026-06-09]] for the paired Type1/Type2 WIN/LOSE pattern, Carnot loop orders, and downstream/emergent I Ching comparison discipline.
