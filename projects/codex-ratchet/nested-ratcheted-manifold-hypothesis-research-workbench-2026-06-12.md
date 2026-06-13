# Nested ratcheted manifold hypothesis — research workbench

Status: **hypothesis / research workbench, not canon**.  
Written: 2026-06-12, after owner correction that the whole sim plan must state the actual nested geometry, every qubit rung, the G2/Spin exceptional structures, and the way every layer changes under nesting.  
Claim ceiling: `proposal_to_test`, `promotion_allowed=false`, `formal_admission_allowed=false`.  
Do not cite this page as admitted `M(C)`, final manifold, QIT engine, runtime flux, Axis0, bridge, physics, or canon.

## Why this page exists

The prior answers kept collapsing the object into either:

- a flat list of geometry words;
- a mostly-1Q plan;
- a status ledger;
- or a generic qubit-ladder queue.

That is not enough. The object to test is a **nested finite survivor tower**: all subsystem states through the chosen qubit ceiling, all partial-trace compatibilities, and all induced geometry recomputed after every ratchet constraint.

This page preserves the explicit proposed object so it can be researched, corrected, and then tested. It is intentionally **not canon yet**.

## Sources / anchors checked while writing

Repo anchors:

- `/Users/joshuaeisenhart/Codex-Ratchet/system_v6/receipts/ratchet_geometry_order_hypothesis_20260612.md`
- `/Users/joshuaeisenhart/Codex-Ratchet/system_v6/receipts/ratcheting_geometry_order_20260612.md`
- `/Users/joshuaeisenhart/Codex-Ratchet/system_v6/receipts/gcm_layer_stack_reference_20260612.md`
- `/Users/joshuaeisenhart/Codex-Ratchet/system_v6/receipts/geometry_sim_program_canonical_20260610.md`

Wiki anchors:

- [[projects/codex-ratchet/read-first]]
- [[projects/codex-ratchet/geometry-sim-program-canonical-2026-06-10]]
- [[projects/codex-ratchet/s1-qubit-ladder-f01-n01-t01-2026-06-10]]
- [[projects/codex-ratchet/octonion-g2-sedenion-carrier-geometry-audit-2026-06-08]]
- [[projects/codex-ratchet/nesting-law-audited-2026-06-10]]
- [[constraint-manifold-architecture]]

Research anchors seeded by web search, not yet fully ingested:

- Hopf fibration / nested tori: Hopf fibration references including David Lyons, “An Elementary Introduction to the Hopf Fibration”; standard Hopf bundle facts `S^1 -> S^3 -> S^2` and stereographic nested tori.
- Berry connection / curvature: Berry connection and curvature references for `A=-i psi^dagger d psi`, holonomy, and curvature as geometric phase data.
- Density-state geometry: Bengtsson and Zyczkowski, *Geometry of Quantum States*; density matrices / Bloch ball / Bures / Fubini-Study literature.
- G2 / Spin(7): Karigiannis, “Some Notes on G2 and Spin(7) Geometry”; G2 as octonion automorphism / 3-form stabilizer; Spin(7) Cayley 4-form.
- Clifford and qubits: Clifford-algebra / algebraic-spinor QI references, including arXiv `2005.04231` as a starting search anchor.
- QCA / runtime flux candidate: Gross, Nesme, Vogts, Werner, “Index theory of one dimensional quantum walks and cellular automata” / GNVW index as net quantum-information flow.

These research anchors are **to be verified and quoted in a later research tranche**. They are not enough by themselves to promote the model.

---

# 1. The proposed final nested object

For a finite qubit ceiling `N` — currently at least `N=8` unless a later test demands more — define every nonempty subsystem:

\[
A\subseteq [N]=\{1,2,\ldots,N\},\qquad A\ne\emptyset.
\]

Subsystem Hilbert space:

\[
H_A=(\mathbb C^2)^{\otimes |A|}.
\]

Density-state space:

\[
D_A=\{\rho_A\in \operatorname{Herm}(H_A):\rho_A\ge0,\operatorname{Tr}\rho_A=1\}.
\]

Finite survivor set after all ratchet constraints on subsystem `A`:

\[
X_A^{\max}\subset D_A.
\]

The proposed fully nested object is:

\[
\boxed{
\mathcal X_{\le N}^{\max}
=
\left\{
(\rho_A,\mathcal G_A)_{\emptyset\ne A\subseteq[N]}:
\rho_A\in X_A^{\max},
\operatorname{Tr}_{A\setminus B}(\rho_A)\sim_B \rho_B
\text{ for every }B\subset A,
\mathcal G_A=\operatorname{InducedGeometry}(X_A^{\max})
\right\}.
}
\]

Here:

- `A` is any subsystem, not only the first `n` qubits;
- `B subset A` is any smaller subsystem;
- `Tr_{A\setminus B}` is partial trace;
- `~_B` is equality under the active probe quotient for subsystem `B`;
- `G_A` is the geometry induced on the survivor set after ratcheting, not copied from the free space.

If exact equality is available, replace:

\[
\operatorname{Tr}_{A\setminus B}(\rho_A)\sim_B\rho_B
\]

with:

\[
\operatorname{Tr}_{A\setminus B}(\rho_A)=\rho_B.
\]

This is a **finite stratified inverse-limit-like tower**, not one ordinary smooth manifold.

---

# 2. Qubit rung table

For `n=|A|`:

\[
H_n=(\mathbb C^2)^{\otimes n},\qquad N_n=2^n.
\]

| rung | Hilbert space | dimension | pure sphere | projective space | density real dimension | Clifford algebra |
|---:|---|---:|---|---|---:|---|
| 1Q | `C^2` | 2 | `S^3` | `CP^1` | 3 | `Cl(2) ~= M_2(C)` |
| 2Q | `(C^2)^2` | 4 | `S^7` | `CP^3` | 15 | `Cl(4) ~= M_4(C)` |
| 3Q | `(C^2)^3` | 8 | `S^15` | `CP^7` | 63 | `Cl(6) ~= M_8(C)` |
| 4Q | `(C^2)^4` | 16 | `S^31` | `CP^15` | 255 | `Cl(8) ~= M_16(C)` |
| 5Q | `(C^2)^5` | 32 | `S^63` | `CP^31` | 1023 | `Cl(10) ~= M_32(C)` |
| 6Q | `(C^2)^6` | 64 | `S^127` | `CP^63` | 4095 | `Cl(12) ~= M_64(C)` |
| 7Q | `(C^2)^7` | 128 | `S^255` | `CP^127` | 16383 | `Cl(14) ~= M_128(C)` |
| 8Q | `(C^2)^8` | 256 | `S^511` | `CP^255` | 65535 | `Cl(16) ~= M_256(C)` |

The ladder rule is sequential:

```text
1Q -> 2Q -> 3Q -> 4Q -> 5Q -> 6Q -> 7Q -> 8Q -> maybe more
```

No rung skip. Existing feedstock does not skip attachment.

---

# 3. Ratchet rule inside every subsystem

For each subsystem `A`, start with finite candidates:

\[
X_{A,0}\subset D_A.
\]

Apply constraints one by one:

\[
X_{A,k+1}=\{\rho\in X_{A,k}: C_{A,k+1}(\rho,\mathcal G_{A,k})=1\}.
\]

Then recompute:

\[
\mathcal G_{A,k+1}=\operatorname{InducedGeometry}(X_{A,k+1}).
\]

The final survivor set is:

\[
X_A^{\max}=X_{A,K_A}.
\]

The important correction is that every later constraint acts on the geometry already altered by prior constraints:

```text
constraint -> smaller/altered survivor set -> recomputed geometry -> next constraint
```

Not:

```text
free geometry + many labels
```

---

# 4. The layer stack and how each layer changes under nesting

Each row below must become a testable sim surface. None is canon yet.

## 4.1 Spinor/projective layer

For subsystem `A`, `n=|A|`:

\[
\psi_A\in H_A,
\qquad
\|\psi_A\|=1.
\]

Pure-state sphere:

\[
S(H_A)=S^{2^{n+1}-1}.
\]

Projective quotient:

\[
\mathbb P(H_A)=S^{2^{n+1}-1}/U(1)=\mathbb{CP}^{2^n-1}.
\]

Pure density:

\[
\rho_{\psi_A}=|\psi_A\rangle\langle\psi_A|.
\]

Nesting change: a larger pure state may project by partial trace to a mixed smaller state, so the lower subsystem may lose its pure spinor lift unless a purification is recorded.

## 4.2 Local Weyl-spinor layer

Each single-qubit factor `i` has:

\[
H_i=\mathbb C^2,
\qquad
\psi_i=\begin{pmatrix}z_{i0}\\z_{i1}\end{pmatrix},
\qquad
|z_{i0}|^2+|z_{i1}|^2=1.
\]

So:

\[
\psi_i\in S_i^3\subset\mathbb C^2.
\]

Product-state skeleton:

\[
\psi_A=\bigotimes_{i\in A}\psi_i.
\]

Entangled states do not factor this way, but local one-qubit reductions remain:

\[
\rho_i=\operatorname{Tr}_{A\setminus\{i\}}\rho_A.
\]

Nesting change: local Weyl spinors survive directly for product/pure local states; for entangled states they are replaced by local marginal density data plus possible purification data.

## 4.3 Local Hopf fibration layer

For each qubit `i`:

\[
S_i^1\hookrightarrow S_i^3\to S_i^2.
\]

Hopf coordinates:

\[
\psi_i(\phi_i,\chi_i,\eta_i)=
\begin{pmatrix}
e^{i(\phi_i+\chi_i)}\cos\eta_i\\
e^{i(\phi_i-\chi_i)}\sin\eta_i
\end{pmatrix}.
\]

Hopf map:

\[
x_i=\sin(2\eta_i)\cos(2\chi_i),
\]

\[
y_i=\sin(2\eta_i)\sin(2\chi_i),
\]

\[
z_i=\cos(2\eta_i).
\]

For `n` qubits, the local product skeleton is:

\[
(S^1)^n\hookrightarrow(S^3)^n\to(S^2)^n.
\]

Modulo one global phase:

\[
(S^1)^n/S^1\cong T^{n-1}.
\]

Nesting change: local phase fibers exist before density quotient; they may be erased by `rho=|psi><psi|`, by partial trace, or by mixing.

## 4.4 Nested Hopf tori and higher-qubit strata

For local qubit `i`, fixed `eta_i` gives:

\[
T_{\eta_i}^{(i)}=\{\psi_i(\phi_i,\chi_i,\eta_i):\phi_i,\chi_i\in S^1\}.
\]

\[
T_{\eta_i}^{(i)}\cong S^1\times S^1.
\]

For product-like local factors:

\[
T_{\vec\eta}^A=\prod_{i\in A}T_{\eta_i}^{(i)},
\qquad
\vec\eta=(\eta_i)_{i\in A}.
\]

\[
T_{\vec\eta}^A\cong(S^1\times S^1)^n.
\]

Double-cover guard for each local torus chart:

\[
(\phi_i,\chi_i)\sim(\phi_i+\pi,\chi_i+\pi).
\]

For entangled states, product Hopf tori are not enough. Replace or supplement them with Schmidt/marginal strata. For a cut `B|A\B`:

\[
|\psi_A\rangle=\sum_j\sqrt{\lambda_j}e^{i\theta_j}|u_j\rangle_B|v_j\rangle_{A\setminus B}.
\]

Fixed Schmidt spectrum:

\[
\vec\lambda=(\lambda_1,\ldots,\lambda_r)
\]

defines a stratum:

\[
\Sigma^{B|A\setminus B}_{\vec\lambda}.
\]

Nesting change: literal local Hopf tori become cut-dependent entanglement strata once higher-qubit entanglement is present. A sim must say which one it is using.

## 4.5 Density/probe quotient layer

Density space:

\[
D_A=\{\rho_A\ge0,\operatorname{Tr}\rho_A=1\}.
\]

Spectral form:

\[
\rho_A=\sum_{j=1}^{2^n}p_j|e_j\rangle\langle e_j|,
\qquad
p_j\ge0,
\qquad
\sum_jp_j=1.
\]

Pauli strings:

\[
P_\alpha=\sigma_{\alpha_1}\otimes\cdots\otimes\sigma_{\alpha_n},
\qquad
\alpha_i\in\{0,x,y,z\}.
\]

Readout:

\[
r_\alpha(\rho_A)=\operatorname{Tr}(P_\alpha\rho_A).
\]

Expansion:

\[
\rho_A=\frac1{2^n}\sum_\alpha r_\alpha(\rho_A)P_\alpha.
\]

Probe quotient:

\[
\rho_A\sim_A\rho_A'
\iff
r_\alpha(\rho_A)=r_\alpha(\rho_A')
\text{ for every active probe }P_\alpha.
\]

Nesting change: probe quotient can identify distinct states and can erase phase/path/holonomy/bracketing data. Every quotient row must state what it forgets.

## 4.6 Metric layer

Pure-state Fubini-Study distance:

\[
d_{FS}([\psi],[\phi])=\arccos|\langle\psi,\phi\rangle|.
\]

Trace distance:

\[
d_1(\rho,\sigma)=\frac12\|\rho-\sigma\|_1.
\]

Fidelity:

\[
F(\rho,\sigma)=\left(\operatorname{Tr}\sqrt{\sqrt\rho\sigma\sqrt\rho}\right)^2.
\]

Bures distance:

\[
d_B(\rho,\sigma)=\sqrt{2(1-\sqrt{F(\rho,\sigma)})}.
\]

Nesting change: metric geometry must be recomputed on `X_A^max`; nearest-neighbor graphs, clusters, distances, and strata may change after every constraint.

## 4.7 Connection / curvature / flux layer

Local Hopf connection for each qubit `i`:

\[
A_i=-i\psi_i^\dagger d\psi_i
=d\phi_i+\cos(2\eta_i)d\chi_i.
\]

Curvature:

\[
F_i=dA_i=-2\sin(2\eta_i)d\eta_i\wedge d\chi_i.
\]

Holonomy:

\[
h_i(\eta_i)=\oint A_i=-2\pi\cos(2\eta_i).
\]

Strip flux:

\[
\Phi_i(\eta_a,\eta_b)=\int_{\Sigma_{ab}}F_i=h_i(\eta_b)-h_i(\eta_a).
\]

Global projective connection for pure `n`-qubit states:

\[
A_A=-i\psi_A^\dagger d\psi_A,
\qquad
F_A=dA_A
\]

on:

\[
S^{2^{n+1}-1}\to\mathbb{CP}^{2^n-1}.
\]

Mixed-state phase geometry is separate and may require Uhlmann/Bures data.

Nesting change: flux appears early as Hopf curvature; stage/runtime/QIT flux is later and depends on maps/cuts/runners. Do not blur these.

## 4.8 Cut layer

For every `B subset A`:

\[
\rho_B=\operatorname{Tr}_{A\setminus B}\rho_A.
\]

Unordered bipartitions for `n=|A|`:

\[
2^{n-1}-1.
\]

Counts:

```text
1Q: 0
2Q: 1
3Q: 3
4Q: 7
5Q: 15
6Q: 31
7Q: 63
8Q: 127
```

Nesting change: cuts enforce compatibility between higher and lower subsystem states.

## 4.9 Entanglement and entropy layer

For 2Q pure states, Schmidt form:

\[
|\psi\rangle_{AB}=\cos\alpha|00\rangle+e^{i\beta}\sin\alpha|11\rangle.
\]

Concurrence:

\[
C=\sin(2\alpha).
\]

Negativity:

\[
\mathcal N=\frac12\sin(2\alpha).
\]

For general cuts:

\[
S(\rho)=-\operatorname{Tr}(\rho\log\rho).
\]

\[
I(B:C)=S(\rho_B)+S(\rho_C)-S(\rho_{BC}).
\]

\[
S(B|C)=S(\rho_{BC})-S(\rho_C).
\]

\[
I_c(B\rangle C)=S(\rho_C)-S(\rho_{BC}).
\]

\[
\mathcal N(\rho_{BC})=\frac{\|\rho_{BC}^{T_C}\|_1-1}{2}.
\]

3Q monogamy witness:

\[
C^2_{A|BC}=C^2_{AB}+C^2_{AC}+\tau_A.
\]

Nesting change: entropy forms become available only when the necessary cuts/state structure exist. 1Q degeneracy is expected; 2Q unlocks bipartite quantities; 3Q+ unlocks monogamy/multipartite rows.

## 4.10 Channel and flow layer

Local channels on qubit `i`:

\[
D_{z,i}^{\lambda}(\rho)=\frac{1+\lambda}{2}\rho+\frac{1-\lambda}{2}\sigma_{z,i}\rho\sigma_{z,i}.
\]

\[
D_{x,i}^{\lambda}(\rho)=\frac{1+\lambda}{2}\rho+\frac{1-\lambda}{2}\sigma_{x,i}\rho\sigma_{x,i}.
\]

\[
R_{x,i}^{\theta}(\rho)=e^{-i\theta\sigma_{x,i}/2}\rho e^{i\theta\sigma_{x,i}/2}.
\]

\[
R_{z,i}^{\theta}(\rho)=e^{-i\theta\sigma_{z,i}/2}\rho e^{i\theta\sigma_{z,i}/2}.
\]

For block `B`:

\[
O_B=O\otimes I_{A\setminus B}.
\]

Lindblad dissipator:

\[
\mathcal D[L](\rho)=L\rho L^\dagger-\frac12(L^\dagger L\rho+\rho L^\dagger L).
\]

Generator:

\[
\mathcal L(\rho)=-i[H,\rho]+\sum_j\gamma_j\mathcal D[L_j](\rho).
\]

Flow:

\[
\Phi(t)=e^{t\mathcal L}.
\]

Four flow families to instantiate explicitly:

\[
\Phi_E(t),\quad \Phi_C(t),\quad \Phi_K(t),\quad \Phi_P(t).
\]

Nesting change: channels/flows may preserve a survivor set, move within it, move to another stratum/fiber, leave it, or erase a pure lift.

## 4.11 Sixteen ordered-map layer

For every valid block `B subset A`, test these ordered maps:

\[
\Phi_E^B\circ D_z^B,
\quad
D_z^B\circ\Phi_E^B,
\]

\[
\Phi_E^B\circ R_x^B,
\quad
R_x^B\circ\Phi_E^B,
\]

\[
\Phi_C^B\circ D_z^B,
\quad
D_z^B\circ\Phi_C^B,
\]

\[
\Phi_C^B\circ R_x^B,
\quad
R_x^B\circ\Phi_C^B,
\]

\[
\Phi_K^B\circ D_x^B,
\quad
D_x^B\circ\Phi_K^B,
\]

\[
\Phi_K^B\circ R_z^B,
\quad
R_z^B\circ\Phi_K^B,
\]

\[
\Phi_P^B\circ D_x^B,
\quad
D_x^B\circ\Phi_P^B,
\]

\[
\Phi_P^B\circ R_z^B,
\quad
R_z^B\circ\Phi_P^B.
\]

Order defect:

\[
\Delta_{\Phi,O}(\rho)=\Phi(O(\rho))-O(\Phi(\rho)).
\]

Witness:

\[
g_{\Phi,O}(\rho)=\|\Delta_{\Phi,O}(\rho)\|_1.
\]

Nesting change: order becomes a measured geometric constraint; where the gap is zero, order is free under the declared probes; where nonzero or mortal, the ordering matters.

## 4.12 Flux-fate layer

For each ordered map `M`:

If:

\[
M(\rho_\psi)=\rho_{\psi'}
\]

then local Hopf flux shift is:

\[
\Delta h_i=h_i(\eta_i')-h_i(\eta_i).
\]

If:

\[
M(\rho_\psi)=\rho_{mixed}
\]

then:

```text
pure Hopf lift erased
geometric Hopf flux undefined on image
```

Then compute instead:

\[
\operatorname{rank}(M(\rho_\psi)),
\qquad
S(M(\rho_\psi)),
\qquad
\operatorname{Tr}(M(\rho_\psi)^2).
\]

Nesting change: the map either transports/changes flux, or destroys the pure lift that made Hopf flux defined.

## 4.13 Finite runner / locality layer

Local torus grid:

\[
\phi_a=\frac{2\pi a}{N},
\qquad
\chi_b=\frac{2\pi b}{N}.
\]

\[
\psi_{a,b,\eta}=\psi(\phi_a,\chi_b,\eta).
\]

Double-cover:

\[
(a,b)\sim(a+N/2,b+N/2)
\]

for even `N`.

Checkerboard parity:

\[
\kappa(a,b)=a+b\pmod2.
\]

Two-phase update:

\[
U_{AB}=U_BU_A.
\]

Paired update:

\[
U_{AABB}=U_BU_BU_AU_A.
\]

Higher-rung QCA candidate:

\[
\alpha:\mathcal A\to\mathcal A.
\]

Potential chiral index:

\[
\operatorname{ind}(\alpha).
\]

Nesting change: continuous/projective geometry gains finite local dynamics; QCA/GNVW-style flux must be earned here, not imported from Hopf curvature alone.

## 4.14 Clifford / chirality / Weyl layer

At subsystem `A`, `n=|A|`:

\[
Cl(2n)
\]

with generators:

\[
\gamma_1,\ldots,\gamma_{2n},
\qquad
\gamma_i\gamma_j+\gamma_j\gamma_i=2\delta_{ij}I.
\]

Complex representation:

\[
Cl(2n)\cong M_{2^n}(\mathbb C).
\]

Chirality:

\[
\Gamma_A=i^n\gamma_1\gamma_2\cdots\gamma_{2n}.
\]

\[
\Gamma_A^2=I.
\]

Projectors:

\[
P_L^A=\frac12(I-\Gamma_A),
\qquad
P_R^A=\frac12(I+\Gamma_A).
\]

Chiral components:

\[
\rho_L=P_L^A\rho_A P_L^A,
\qquad
\rho_R=P_R^A\rho_A P_R^A.
\]

Nesting change: higher qubit rungs gain explicit left/right chiral decomposition. At 3Q, `Cl(6) ~= M_8(C)` is the first full `C^8` floor.

## 4.15 G2 / octonion layer

Octonions:

\[
\mathbb O.
\]

Imaginary octonions:

\[
\operatorname{Im}\mathbb O\cong\mathbb R^7.
\]

A convention-pinned standard `G2` 3-form is:

\[
\varphi=e^{123}+e^{145}+e^{167}+e^{246}-e^{257}-e^{347}-e^{356}.
\]

Then:

\[
G_2=\{g\in GL(7,\mathbb R):g^*\varphi=\varphi\}.
\]

Equivalently:

\[
G_2=\operatorname{Aut}(\mathbb O).
\]

The 3-form defines a cross product by:

\[
g_\varphi(x\times y,z)=\varphi(x,y,z).
\]

Octonion associator:

\[
[a,b,c]=(ab)c-a(bc).
\]

Alternativity:

\[
[a,a,b]=0,
\qquad
[a,b,b]=0.
\]

To attach this to the survivor tower, choose an explicit seven-dimensional real readout/observable space:

\[
W_A\subset \operatorname{span}_{\mathbb R}\{P_\alpha\}
\]

with:

\[
\dim W_A=7.
\]

Then attach:

\[
(W_A,\varphi_A),
\qquad
\varphi_A\in\Lambda^3 W_A^*.
\]

G2-compatibility condition:

\[
g^*\varphi_A=\varphi_A.
\]

Nesting change: adding G2 imposes a 7D 3-form/cross-product/associator compatibility constraint. It is not a label; it needs `W_A`, `phi_A`, and tests.

## 4.16 SU(3) inside G2

Choose a unit vector:

\[
u\in S^6\subset\operatorname{Im}\mathbb O.
\]

Then:

\[
\operatorname{Stab}_{G_2}(u)\cong SU(3).
\]

and:

\[
G_2/SU(3)\cong S^6.
\]

Splitting:

\[
\operatorname{Im}\mathbb O=\mathbb R u\oplus u^\perp,
\qquad
u^\perp\cong\mathbb R^6\cong\mathbb C^3.
\]

Nesting change: selecting `u` reduces symmetry from `G2` to `SU(3)` and creates an almost-complex 6D complement. This should be tested as a stabilizer reduction.

## 4.17 Spin(7) layer

Extend:

\[
\mathbb R^7\to\mathbb R^8=\mathbb R t\oplus\mathbb R^7.
\]

Cayley 4-form:

\[
\Omega=dt\wedge\varphi+*\varphi.
\]

Then:

\[
Spin(7)=\{g\in GL(8,\mathbb R):g^*\Omega=\Omega\}.
\]

and:

\[
Spin(7)/G_2\cong S^7.
\]

Nesting change: a 7D G2 structure extends to an 8D Spin(7) structure only if the added dimension and Cayley form are explicitly realized.

## 4.18 Spin(8) triality layer

Spin(8) has three 8D representations:

\[
8_v,
\qquad
8_s,
\qquad
8_c.
\]

Triality permutes:

\[
8_v,8_s,8_c.
\]

A test must provide actual maps:

\[
T_{v\to s}:8_v\to8_s,
\quad
T_{s\to c}:8_s\to8_c,
\quad
T_{c\to v}:8_c\to8_v.
\]

Nesting change: vector-like, left-spinor-like, and right-spinor-like roles can be compared or permuted only if their representations are explicitly constructed.

## 4.19 F4 / exceptional Jordan layer

Exceptional Jordan algebra:

\[
J_3(\mathbb O)=\{3\times3\text{ Hermitian octonionic matrices}\}.
\]

Real dimension:

\[
\dim_\mathbb R J_3(\mathbb O)=27.
\]

Jordan product:

\[
A\circ B=\frac12(AB+BA).
\]

Automorphism group:

\[
F_4=\operatorname{Aut}(J_3(\mathbb O)).
\]

Octonionic projective plane:

\[
\mathbb OP^2=F_4/Spin(9).
\]

Nesting change: this is a late compatibility test requiring a 27D Jordan target/source. It must not replace lower Hilbert/density/cut/Clifford layers.

## 4.20 Split G2 and sedenion boundary controls

Split octonions:

\[
\mathbb O_s.
\]

Split real form:

\[
G_{2(2)}.
\]

Sedenions:

\[
\mathbb S.
\]

Zero-divisor boundary:

\[
ab=0,
\qquad
a\ne0,
\qquad
b\ne0.
\]

Nesting change: compact G2, split G2, and sedenion zero-divisor behavior are branch/control surfaces. Sedenions are graveyard/boundary unless later constraints say otherwise.

---

# 5. How layers nest and change each other

| Added layer | Adds | Changes previous geometry by |
|---|---|---|
| phase quotient | `psi ~ e^{i theta} psi` | erases global phase; creates projective state and pure density |
| pure density | `rho=|psi><psi|` | keeps projective state; loses raw spinor phase |
| Pauli probes | `r_alpha=Tr(P_alpha rho)` | collapses states into probe-equivalence classes |
| local Hopf | `S^1 -> S^3 -> S^2` | creates local phase fibers and shell coordinate `eta` |
| Hopf tori | `T_eta subset S^3` | stratifies local geometry by shell/leaf |
| connection | `A=-i psi^dagger d psi` | gives phase fiber measurable twist |
| curvature | `F=dA` | makes geometric flux available |
| strip flux | `int F = h_j-h_i` | gives shell pairs flux relation |
| mixing | rank > 1 density | may erase pure Hopf lift |
| cuts | `rho_B=Tr_{A\B} rho_A` | forces higher/lower subsystem compatibility |
| Schmidt strata | fixed `lambda` | replaces simple tori with entanglement strata |
| entropy | `S,I,I_c,N` | becomes available only where cuts exist |
| channels | dephase/rotate maps | move, contract, mix, or preserve states |
| flows | `e^{tL}` | adds time evolution and attractor/basin rows |
| 16 ordered maps | `Phi o O`, `O o Phi` | makes order a measured geometric constraint |
| flux fate | `Delta h` or lift erasure | says whether a map transports flux or destroys the lift |
| runner | finite local update | turns survivor geometry into finite local dynamics |
| Clifford | `Cl(2n)` | adds gamma/chirality structure |
| Weyl chirality | `P_L,P_R` | splits states into left/right components |
| G2 | `phi in Lambda^3(R^7)^*` | imposes 7D cross-product/associator compatibility |
| SU(3) inside G2 | stabilizer of `u in S^6` | selects direction and reduces symmetry |
| Spin(7) | `Omega=dt wedge phi + *phi` | extends G2 7D structure to 8D |
| Spin(8) | triality `8_v,8_s,8_c` | compares vector/left/right spinor roles |
| F4 | `J_3(O)` | tests 27D exceptional Jordan compatibility |

---

# 6. Research backing still needed

This page should be processed as a research task before any canon promotion. Minimum research rows:

1. Hopf bundle / nested torus row
   - verify formulas for Hopf coordinates, double cover, torus area, connection, curvature, holonomy convention.
   - sources to ingest: Hopf fibration references, Lyons, geometry/topology textbooks, Berry phase references.

2. Density and quantum-state geometry row
   - verify `D(H_n)`, Bloch special case, Bures/Fubini-Study/trace distance, fidelity, pure/mixed boundary.
   - sources to ingest: Bengtsson-Zyczkowski, Nielsen-Chuang, Petz/Sudar mixed-state geometry sources.

3. Multi-qubit cut/entropy row
   - verify bipartition counts, Schmidt strata, concurrence, negativity, monogamy limits, coherent information.
   - sources to ingest: standard QI texts and entanglement reviews.

4. Clifford/chirality row
   - verify `Cl(2n) ~= M_{2^n}(C)`, gamma anticommutation, chirality operator, left/right projectors, relation to qubit representation.
   - sources to ingest: Clifford/QI papers and standard Clifford algebra references.

5. G2/Spin/F4 row
   - verify 3-form convention, `G2=Aut(O)`, `G2/SU(3)=S^6`, Cayley form, `Spin(7)/G2=S^7`, Spin(8) triality, `J3(O)`, `F4`, split form, sedenion zero-divisor controls.
   - sources to ingest: Karigiannis G2/Spin(7) notes, Baez octonions, Bryant/Joyce/Berger-holonomy references, Harvey-Lawson calibrations, octonion/Jordan references.

6. QCA/GNVW runtime-flux row
   - verify GNVW index conditions and whether the finite runner can be cast as a 1D QCA with a computable index.
   - sources to ingest: Gross-Nesme-Vogts-Werner index theory and follow-up QCA literature.

7. Nesting law row
   - verify inverse-limit / marginal problem / quantum marginal compatibility framing.
   - sources to ingest: quantum marginal problem, N-representability, projective/inverse systems where relevant.

8. Ratchet-order row
   - verify pairwise commutator/mortality/order-matrix method, not as standard theorem but as finite test protocol.
   - sources to ingest: repo receipts plus external mathematics for noncommuting maps, BCH, order effects, categorical/coherence guardrails if needed.

---

# 7. Next wiki processing steps

Do not promote this page. Process it in tranches:

```text
Tranche 1: source-backed Hopf/density/cut/Clifford/G2 bibliography.
Tranche 2: convert each layer above into a row ledger with source anchors.
Tranche 3: mark each row as standard math / project hypothesis / repo-tested / open.
Tranche 4: derive build cards from only the rows with enough math support.
Tranche 5: test the nested object one rung at a time through 8Q(+).
```

The page should stay labeled:

```text
hypothesis / research workbench / not canon
```

until those tranches land.

---

# 8. Error-correction guard

Reject any future plan that cannot answer all of these explicitly:

```text
Where are Weyl spinors?
Where are nested Hopf tori?
Where is A?
Where is F=dA?
Where is h(eta)?
Where are the cuts for every subsystem?
Where are the Pauli-string quotients?
Where are the 16 ordered maps?
Where is the flux-fate row?
Where is Cl(2n)?
Where are P_L and P_R?
Where is G2 as a 3-form stabilizer, not a name?
Where are SU(3), Spin(7), Spin(8), F4, split G2, and sedenion controls?
How does each layer change the induced geometry when nested?
What external research backs each row?
What repo evidence, if any, has tested it?
```

If the answer is “implied,” the plan fails.
