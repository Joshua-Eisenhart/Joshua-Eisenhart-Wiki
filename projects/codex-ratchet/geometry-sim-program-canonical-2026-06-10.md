# Canonical geometry sim program — anti-collapse wiki copy

Status: project-level routing / anti-collapse note.  
Written: 2026-06-09 local time, from the 2026-06-10 repo receipt and this session's owner correction.  
Repo anchors: `/Users/joshuaeisenhart/Codex-Ratchet/system_v6/receipts/geometry_sim_program_canonical_20260610.md` (`3e3611879`, roadmap), `/Users/joshuaeisenhart/Codex-Ratchet/system_v6/receipts/nesting_law_audited_20260610.md` (`6499eb470`, audited nesting-law companion), S1 foundation commits through `c52187331`, S1 exact deepening commits `6ed5e961e` and `6489a6929`, and S2 spec-prep gate `555ab9c2c`.  
Claim ceiling: `scratch_diagnostic`, `promotion_allowed=false`, `formal_admission_allowed=false` for every sim until a later gate explicitly changes that.

Purpose: preserve the full geometry-first program so future agents and sims do not collapse the model back into project labels, packet inventory, Jungian/function words, or generic systems jargon. The word **geometric** means actual geometry.

Related project notes:
- [[projects/codex-ratchet/read-first]]
- [[constraint-manifold-architecture]]
- [[projects/codex-ratchet/qit-axes-terrain-operator-fold-2026-06-09]]
- [[projects/codex-ratchet/octonion-g2-sedenion-carrier-geometry-audit-2026-06-08]]
- [[projects/codex-ratchet/ring-checkerboard-three-presentations-sim-engine-runbook-2026-06-09]]
- [[projects/codex-ratchet/nesting-law-audited-2026-06-10]]
- [[projects/codex-ratchet/s1-qubit-ladder-f01-n01-t01-2026-06-10]]

## Non-negotiable correction

Do not put systems vocabulary into the math.

Use standard mathematical objects and formulas first. If project labels are needed, attach them outside the formulas, after the geometry has been stated.

Bad pattern:

```text
Sim the terrain/Jung/engine labels.
```

Good pattern:

```text
Sim the spinor, Hopf map, connection, curvature, torus foliation,
channel generator, fixed point, basin, order gap, associator, and group action.
```

## Current status

At the time this page was first written, the committed repo receipt was a **roadmap**, not a completed geometry sim result. The live repo has since advanced through the S1 foundation closeout.

Current honest status, patched 2026-06-10 after live repo verification and later S1 exact-deepening commits:

```text
canonical geometry roadmap: committed
nesting-law audited companion: committed
S1 foundation family: closed as committed scratch-diagnostic evidence
Bloch/root admissibility discriminator: hardened, twice-audited, committed scratch diagnostic
S1 positive spinor-Hopf free-mode sim: hardened, re-audited, committed scratch diagnostic
S1 quaternion model: hardened, re-audited, committed scratch diagnostic
S1 negative models: hardened, re-audited, committed scratch diagnostic
S1 finite-phase lens tower: hardened, re-audited, committed scratch diagnostic
S1 1Q exact closure: committed scratch diagnostic at 6489a6929
S1 3Q minimum floor: committed scratch diagnostic at 6ed5e961e
S1 2Q boundary/control: live/untracked at this wiki patch, not closed here
S1 4Q-8Q ladder: not built here
S2 connection/flux/foliation spec prep: committed at 555ab9c2c, runtime gated behind S1 ladder closure
current ceiling for all of the above: promotion_allowed=false, formal_admission_allowed=false
```

This page exists so future workers cannot collapse either way: the broad S1 family is no longer merely in flight, and 1Q/3Q exact deepening has landed, but the S1 qubit ladder is not closed through the selected target. This is still not formal carrier admission, final `M(C)`, physics, QIT-engine, or geometry-complete doctrine.

## S1 qubit-ladder gate before S2 runtime

S2 connection / curvature / foliation uses the 1Q Hopf geometry:

```math
A=d\phi+\cos(2\eta)d\chi
```

```math
F=dA=-2\sin(2\eta)d\eta\wedge d\chi
```

But later QIT-engine / chirality / memory / runtime flux requires the qubit ladder not to collapse into a single 3Q note. Load [[projects/codex-ratchet/s1-qubit-ladder-f01-n01-t01-2026-06-10]] before reopening S2 runtime.

Every rung must carry:

```text
F01_finitude_receipt
N01_noncommutation_receipt
T01_bracketing_receipt
```

Do not replace noncommutation with anticommutation. Anticommutation is a sharpened Clifford special case; root order pressure is `AB != BA`. Do not fake nonassociativity inside qubit matrix multiplication; the matrix associator control is zero, while schedule/channel/quotient bracketing and octonion extension are separate tests.

## Bloch sphere / Bloch ball status

The Bloch sphere and Bloch ball are not the full foundation carrier.

They survive as density/channel quotient geometry:

\[
S^3/S^1\cong S^2
\]

and:

\[
D(\mathbb C^2)\cong B^3
\]

The quotient is:

\[
\rho=\psi\psi^\dagger
\]

and:

\[
(e^{i\alpha}\psi)(e^{i\alpha}\psi)^\dagger=\psi\psi^\dagger.
\]

So the quotient kills the global spinor phase. Any sim using only \(\rho\) must explicitly report what it erases:

- fiber phase;
- lifted path data;
- \(720^\circ\) spinor return;
- some holonomy conventions;
- some chirality/lift information;
- any three-slot bracketing signal that disappears after density quotient.

Correct role:

```text
S^3 = spinor/Hopf carrier candidate
S^2 = projective/Bloch quotient
B^3 = mixed-state channel domain
```

Do not promote \(S^2\) or \(B^3\) as the full root-surviving carrier without a discriminator that proves the erased distinctions are irrelevant.

## The stacking law

Every layer has four different sim modes. These are different sims.

### 1. Free mode

The layer alone, checked against known exact invariants.

Example:

\[
\psi\in S^3,
\qquad
\|\psi\|=1.
\]

### 2. Restricted / stacked mode

The layer confined by lower geometry. The sim asks whether an operation preserves the lower structure, moves within it, moves to another leaf, or leaves it.

Example:

\[
\Phi(T_\eta)\subseteq T_\eta?
\]

\[
\Phi(T_\eta)\subseteq T_{\eta'}?
\]

or:

\[
\Phi(T_\eta)\not\subseteq \bigcup_\eta T_\eta.
\]

For shell coordinate:

\[
z=\cos(2\eta),
\]

leakage is:

\[
\frac{dz}{dt}.
\]

### 3. Quotiented mode

The layer viewed through lower quotients. The sim asks which distinctions survive.

Example:

\[
\psi\neq\psi'
\]

but:

\[
\psi\psi^\dagger=\psi'{\psi'}^\dagger.
\]

For nonassociativity:

\[
((ab)c)\Psi-a(bc)\Psi
\]

may be visible before density quotient and erased after density quotient.

### 4. Ratcheted mode

Owner correction, 2026-06-10: as the ratchet runs, the actual geometry becomes more constrained and altered; it has to align to the constraints, and the surviving path is narrow and specific.

Mathematically, ratcheted mode is sequential constraint application with induced-geometry recomputation at every step:

\[
G_{t+1}=\{x\in G_t:C_{t+1}(x)\}.
\]

But the sim must not stop at membership. It must recompute the geometry induced on the survivor set:

\[
g_{t+1}=g_t|_{G_{t+1}},
\]

\[
A_{t+1}=A_t|_{G_{t+1}},
\]

\[
F_{t+1}=dA_{t+1},
\]

and, when the survivor set has positive ambient measure, the conditioned measure:

\[
\mu_{t+1}(E)=\frac{\mu_t(E\cap G_{t+1})}{\mu_t(G_{t+1})}
\]

when \(\mu_t(G_{t+1})>0\). If \(G_{t+1}\) is lower-dimensional or measure-zero in the ambient geometry, such as a shell \(T_\eta\subset S^3\), the sim must use the induced / disintegrated / coarea surface measure instead of this conditioning formula. Every ratcheted-mode receipt must say which case it is in.

Each constraint acts on the altered output of the previous step, not on the original free geometry:

\[
C_{t+1}:G_t\to\{0,1\},
\qquad
G_t\neq G_0\ \text{in general}.
\]

The three computed signatures are:

1. Narrowing:

\[
\mu(G_{t+1})\leq\mu(G_t).
\]

Record ledger:

\[
R_{t+1}=R_t\cup(G_t\setminus G_{t+1}).
\]

2. Alteration:

\[
I_k(G_{t+1})\neq I_k(G_t)
\]

for induced invariants such as metric distances, holonomy, flux, measure, fixed points, or basins.

3. Path specificity:

\[
\text{specificity}_t=\frac{\#\{\text{branches/orders/pins that survive coherently}\}}{\#\{\text{branches/orders/pins attempted}\}}.
\]

Low specificity means the path is narrow. Order sensitivity here is noncommutation acting at the geometry level:

\[
C_i(C_j(G))\not\cong C_j(C_i(G))
\]

under the active equivalence/probe family.

Ratchet sims begin only after the relevant free-mode stages survive audit.

No sim is complete until it says which of these four modes it ran.

## Cross-cutting order and bracketing tests

Order/bracket pressure is not a fifth mode. It is a test family that can run inside free, restricted, quotiented, or ratcheted mode.

### Binary order

Root binary order:

\[
AB\neq BA.
\]

Measured on a state or object:

\[
\Delta_{A,B}(x)=A(Bx)-B(Ax).
\]

### Nontrivial anticommutation

Anticommutation alone:

\[
AB+BA=0
\]

is not always enough to imply noncommutation. Edge case:

\[
AB=BA=0
\]

satisfies both commuting and anticommuting conditions.

So the sharpened binary rung must require nontrivial anticommutation:

\[
AB+BA=0,
\qquad
AB\neq0.
\]

For Clifford generators:

\[
\gamma_i\gamma_j+\gamma_j\gamma_i=2\delta_{ij},
\]

and for \(i\neq j\):

\[
\gamma_i\gamma_j=-\gamma_j\gamma_i,
\qquad
\gamma_i\gamma_j\neq0.
\]

### Ternary order

Root ternary bracket order:

\[
[a,b,c]=(ab)c-a(bc).
\]

Nonassociativity:

\[
[a,b,c]\neq0.
\]

### Alternativity as the real sharpened ternary rung

The sharpened ternary structure on the octonion path is not global anti-associativity. It is alternativity: the associator is alternating / totally antisymmetric.

Repeated slots vanish:

\[
[a,a,b]=0,
\qquad
[a,b,a]=0,
\qquad
[b,a,a]=0.
\]

Swapping slots flips sign:

\[
[a,b,c]=-[b,a,c]=-[a,c,b].
\]

This is the precise signed ternary structure that octonions have.

### Anti-associativity is a separate designed-to-fail branch

A global anti-associative law such as:

\[
(ab)c=-a(bc)
\]

is not the octonion path. Any unital algebra fails immediately:

\[
(1\cdot1)\cdot1=1\neq-1=-1\cdot(1\cdot1).
\]

It also conflicts with alternativity on repeated slots. Alternativity gives:

\[
(aa)b=a(ab),
\]

while anti-associativity would require:

\[
(aa)b=-a(ab).
\]

Thus anti-associativity belongs, if anywhere, as a unit-free exotic branch or a designed-to-fail control row, not as the main ternary ratchet.

Correct ladder:

```text
root binary: AB != BA
sharpened binary: AB + BA = 0 and AB != 0 -> Clifford-style anticommutation
root ternary: [a,b,c] != 0
sharpened ternary on the octonion path: alternating associator / alternativity
anti-associativity: separate exotic branch or kill-control row
```

## Nesting taxonomy additions

The earlier list of nesting types was still incomplete. Add these two kinds explicitly.

### Refinement / limit nesting

A finite sequence approximates or converges toward a limiting geometry:

\[
G_N\to G.
\]

Examples:

\[
T_\eta^{N,N}\to T_\eta,
\]

with the double-cover quotient handled, and finite phase quotients such as:

\[
S^3/\mathbb Z_N=L(N,1)
\]

as a finite-phase quotient family that must be compared against:

\[
S^3/S^1\cong\mathbb{CP}^1.
\]

This is the finitude-root nesting type: finite presentations must show convergence or controlled non-convergence to the claimed invariant.

### Group-action / orbit nesting

A group action:

\[
G\curvearrowright X
\]

creates orbits and stabilizers:

\[
Gx\cong G/G_x.
\]

Examples:

\[
S^2\cong SU(2)/U(1),
\]

\[
G_2/SU(3)\cong S^6,
\]

\[
Spin(7)/G_2\cong S^7.
\]

This is distinct from bundle nesting. A sim must say whether it is testing a bundle, a quotient, a refinement limit, or a group orbit/stabilizer relation.

---

# Full geometry and math stack

## 1. Complex two-spinor space

\[
\mathbb C^2
\]

A two-component spinor:

\[
\psi=
\begin{pmatrix}
z_1\\
z_2
\end{pmatrix},
\qquad
z_1,z_2\in\mathbb C.
\]

Normalize:

\[
|z_1|^2+|z_2|^2=1.
\]

Therefore:

\[
\psi\in S^3\subset\mathbb C^2.
\]

Coordinate form:

\[
\psi(\phi,\chi,\eta)=
\begin{pmatrix}
e^{i(\phi+\chi)}\cos\eta\\
e^{i(\phi-\chi)}\sin\eta
\end{pmatrix},
\qquad
\phi,\chi\in S^1,
\qquad
0\leq\eta\leq\frac{\pi}{2}.
\]

Free-mode checks:

\[
\|\psi\|^2=1.
\]

Haar sampling: draw two complex Gaussians and normalize.

## 2. Round \(S^3\) geometry

\[
S^3=\{(z_1,z_2)\in\mathbb C^2: |z_1|^2+|z_2|^2=1\}.
\]

Identifications:

\[
S^3\cong SU(2)\cong\{\text{unit quaternions}\}.
\]

Metric in \((\phi,\chi,\eta)\):

\[
ds^2=d\eta^2+d\phi^2+d\chi^2+2\cos(2\eta)d\phi d\chi.
\]

Volume:

\[
\operatorname{Vol}(S^3)=2\pi^2.
\]

Do not confuse the real \(S^3\) geodesic distance with Fubini--Study distance on the base quotient.

## 3. Hopf map \(S^3\to S^2\)

For:

\[
\psi=(z_1,z_2),
\]

set:

\[
x=2\operatorname{Re}(z_1\bar z_2),
\]

\[
y=2\operatorname{Im}(z_1\bar z_2),
\]

\[
z=|z_1|^2-|z_2|^2.
\]

Then:

\[
x^2+y^2+z^2=1.
\]

So:

\[
\pi:S^3\to S^2.
\]

In \((\phi,\chi,\eta)\):

\[
x=\sin(2\eta)\cos(2\chi),
\]

\[
y=\sin(2\eta)\sin(2\chi),
\]

\[
z=\cos(2\eta).
\]

Free-mode checks:

\[
\pi(e^{i\alpha}\psi)=\pi(\psi),
\]

surjectivity / covering of \(S^2\), and uniform Haar pushforward.

## 4. Hopf fibers and linking

Each fiber is:

\[
\pi^{-1}(p)\cong S^1.
\]

Thus:

\[
S^1\hookrightarrow S^3\xrightarrow{\pi}S^2.
\]

A fiber loop:

\[
\gamma_f(u)=\psi(\phi_0+u,\chi_0,\eta_0).
\]

Base point remains fixed:

\[
\pi(\gamma_f(u))=\pi(\gamma_f(0)).
\]

Distinct Hopf fibers have linking number:

\[
\operatorname{Lk}=1.
\]

A Stage-1 sim must compute linking numerically, not merely state it.

## 5. Density quotient

\[
\rho=\psi\psi^\dagger.
\]

Explicitly:

\[
\rho=
\begin{pmatrix}
\cos^2\eta & e^{2i\chi}\cos\eta\sin\eta\\
e^{-2i\chi}\cos\eta\sin\eta & \sin^2\eta
\end{pmatrix}.
\]

The phase \(\phi\) is erased.

\[
\psi\sim e^{i\alpha}\psi.
\]

\[
S^3/S^1\cong\mathbb{CP}^1\cong S^2.
\]

Keystone identity to sim:

\[
\text{Bloch}(\psi\psi^\dagger)=\pi(\psi).
\]

## 6. Bloch sphere

Pure density matrices:

\[
\rho=\frac12(I+x\sigma_x+y\sigma_y+z\sigma_z),
\]

with:

\[
x^2+y^2+z^2=1.
\]

This is \(S^2\), but it is already a quotient of \(S^3\).

## 7. Bloch ball / full density space

\[
D(\mathbb C^2)=\{\rho: \rho^\dagger=\rho,\ \rho\geq0,\ \operatorname{Tr}\rho=1\}.
\]

Bloch form:

\[
\rho=\frac12(I+x\sigma_x+y\sigma_y+z\sigma_z),
\]

with:

\[
x^2+y^2+z^2\leq1.
\]

So:

\[
D(\mathbb C^2)\cong B^3.
\]

Eigenvalues:

\[
\lambda_\pm=\frac12(1\pm\|r\|).
\]

Purity:

\[
\operatorname{Tr}(\rho^2)=\frac12(1+\|r\|^2).
\]

Entropy:

\[
S(\rho)=-\lambda_+\ln\lambda_+-\lambda_-\ln\lambda_-.
\]

Dissipative flows leave the pure sphere and move inside this ball. That is why \(B^3\) is necessary even though it is not the full carrier.

## 8. Probe / measurement geometry

For unit vector \(n\):

\[
O_n=n\cdot\sigma.
\]

Expectation:

\[
\operatorname{Tr}(\rho\,n\cdot\sigma)=n\cdot r.
\]

Level sets:

\[
n\cdot r=c.
\]

These are plane slices of the Bloch ball.

Born probabilities:

\[
p_\pm=\frac12(1\pm n\cdot r).
\]

Projectors:

\[
P_\pm=\frac12(I\pm n\cdot\sigma).
\]

Measurement update:

\[
\rho\mapsto\frac{P_\pm\rho P_\pm}{p_\pm}.
\]

Probe equivalence:

\[
\rho\sim\rho'
\iff
\operatorname{Tr}(M_i\rho)=\operatorname{Tr}(M_i\rho')
\quad\forall i.
\]

## 9. Metrics and distances

Fubini--Study metric on the base:

\[
ds^2_{FS}=\frac14(d\theta^2+\sin^2\theta\,d\alpha^2).
\]

Trace distance:

\[
D(\rho,\sigma)=\frac12\|\rho-\sigma\|_1.
\]

Fidelity:

\[
F(\rho,\sigma)=\left(\operatorname{Tr}\sqrt{\sqrt\rho\,\sigma\,\sqrt\rho}\right)^2.
\]

CPTP contraction:

\[
\|\Phi(\rho)-\Phi(\sigma)\|_1\leq\|\rho-\sigma\|_1.
\]

This contraction is real distinguishability-loss math. It should not be replaced by metaphor.

## 10. Measures

Haar sampling on \(S^3\): draw complex Gaussian pair \((g_1,g_2)\), then normalize:

\[
\psi=\frac{(g_1,g_2)}{\sqrt{|g_1|^2+|g_2|^2}}.
\]

Pushforward under Hopf map gives uniform measure on \(S^2\).

Volumes:

\[
\operatorname{Vol}(S^3)=2\pi^2,
\qquad
\operatorname{Area}(S^2)=4\pi.
\]

## 11. Hopf connection

\[
A=-i\psi^\dagger d\psi.
\]

In coordinates:

\[
A=d\phi+\cos(2\eta)d\chi.
\]

Horizontal condition:

\[
A(\dot\gamma)=0.
\]

Thus:

\[
d\phi=-\cos(2\eta)d\chi.
\]

Horizontal/base loop:

\[
\gamma_b(u)=\psi(\phi_0-\cos(2\eta_0)u,\chi_0+u,\eta_0).
\]

## 12. Curvature / flux

Flux is curvature:

\[
F=dA.
\]

Since:

\[
A=d\phi+\cos(2\eta)d\chi,
\]

then:

\[
F=d(\cos(2\eta))\wedge d\chi,
\]

\[
F=-2\sin(2\eta)d\eta\wedge d\chi.
\]

Also:

\[
dF=0.
\]

## 13. Holonomy / Berry phase convention pin

For a fixed shell \(\eta\):

\[
h(\eta)=\oint A.
\]

One convention gives:

\[
h(\eta)=-2\pi\cos(2\eta).
\]

The Berry phase law for a closed base loop is:

\[
\gamma=-\frac12\Omega,
\]

where \(\Omega\) is the solid angle enclosed on \(S^2\). For a latitude:

\[
\gamma=-\pi(1-\cos(2\eta)).
\]

These differ by gauge/orientation/reference convention. Every sim must pin which one it reports before comparing engines.

## 14. Total flux / Chern-like integral

Over:

\[
0\leq\eta\leq\frac\pi2,
\qquad
0\leq\chi<2\pi,
\]

\[
\int F=-4\pi.
\]

Thus:

\[
\frac{|\int F|}{4\pi}=1.
\]

Orientation may flip the sign, not the magnitude.

## 15. Hopf tori and the double-cover tripwire

For:

\[
0<\eta<\frac\pi2,
\]

\[
T_\eta=\{\psi(\phi,\chi,\eta):\phi,\chi\in S^1\}.
\]

Then:

\[
T_\eta\cong S^1\times S^1\subset S^3.
\]

Radii:

\[
r_1=\cos\eta,
\qquad
r_2=\sin\eta.
\]

True embedded area:

\[
\operatorname{Area}(T_\eta)=2\pi^2\sin(2\eta).
\]

Clifford torus:

\[
\eta=\frac\pi4.
\]

Critical identification:

\[
\psi(\phi+\pi,\chi+\pi,\eta)=\psi(\phi,\chi,\eta).
\]

So the \((\phi,\chi)\) chart is a 2-to-1 cover of the embedded torus. The naive chart area is:

\[
4\pi^2\sin(2\eta),
\]

but the true embedded area is:

\[
2\pi^2\sin(2\eta).
\]

Any discrete torus sim must handle:

\[
(a,b)\sim(a+N/2,b+N/2)
\]

for even \(N\). An \(N\times N\) chart grid has only:

\[
N^2/2
\]

physical spinor points. Ignoring this double-counts area, volume, and vertex count.

## 16. Nested Hopf tori

Choose:

\[
0<\eta_1<\eta_2<\cdots<\eta_n<\frac\pi2.
\]

Then:

\[
\{T_{\eta_k}\}_{k=1}^n
\]

is the nested torus stack.

Each shell has:

\[
h(\eta_k)=-2\pi\cos(2\eta_k).
\]

Adjacent flux:

\[
\Phi_{k,k+1}=2\pi(\cos(2\eta_k)-\cos(2\eta_{k+1})).
\]

A nested-torus sim must check torus area, holonomy curve, inter-shell flux, and the double-cover quotient.

## 17. \(SU(2)\to SO(3)\) double cover

For:

\[
U\in SU(2),
\]

\[
U(n\cdot\sigma)U^\dagger=(Rn)\cdot\sigma
\]

for:

\[
R\in SO(3).
\]

The map:

\[
SU(2)\to SO(3)
\]

is two-to-one:

\[
U\sim -U.
\]

A \(360^\circ\) rotation sends:

\[
\psi\mapsto-\psi.
\]

A \(720^\circ\) rotation returns:

\[
\psi\mapsto\psi.
\]

## 18. Antiunitary mirror / time reversal

Let:

\[
K=\text{complex conjugation},
\qquad
T=\sigma_yK.
\]

Then:

\[
T\rho T^{-1}=\sigma_y\bar\rho\sigma_y.
\]

On Bloch coordinates:

\[
r\mapsto-r.
\]

Conjugation by \(\sigma_y\) alone gives:

\[
\sigma_y\sigma_x\sigma_y=-\sigma_x,
\]

\[
\sigma_y\sigma_y\sigma_y=\sigma_y,
\]

\[
\sigma_y\sigma_z\sigma_y=-\sigma_z.
\]

Therefore:

\[
\sigma_yH\sigma_y=-H
\]

only when \(H\) has no \(\sigma_y\) component. For:

\[
H_0=\frac{\sigma_x+\sigma_y+\sigma_z}{\sqrt3},
\]

an exact sign flip fails because of the \(\sigma_y\) component. This must be an explicit convention/control check.

## 19. Channel space

A quantum channel:

\[
\Phi(\rho)=\sum_iK_i\rho K_i^\dagger,
\]

with:

\[
\sum_iK_i^\dagger K_i=I.
\]

On Bloch coordinates, a qubit channel is affine:

\[
r\mapsto Mr+c.
\]

It maps the Bloch ball to an ellipsoid inside the ball.

Lindblad flow:

\[
\frac{d\rho}{dt}=-i[H,\rho]+\sum_j\left(L_j\rho L_j^\dagger-\frac12\{L_j^\dagger L_j,\rho\}\right).
\]

## 20. Fixed points and basins

Fixed point:

\[
\Phi_t(\rho_*)=\rho_*
\]

or infinitesimally:

\[
X(\rho_*)=0.
\]

Basin:

\[
B(\rho_*)=\{\rho: \lim_{t\to\infty}\Phi_t(\rho)=\rho_*\}.
\]

Every terrain/channel sim should report fixed points and basins, not just a single trajectory.

## 21. Pauli algebra

\[
[\sigma_i,\sigma_j]=2i\epsilon_{ijk}\sigma_k.
\]

\[
\{\sigma_i,\sigma_j\}=2\delta_{ij}I.
\]

\[
\operatorname{Tr}(\sigma_i\sigma_j)=2\delta_{ij}.
\]

## 22. Four base channel maps

### \(D_z\)

\[
D_z(\rho)=(1-q_1)\rho+q_1(P_0\rho P_0+P_1\rho P_1),
\]

\[
P_0=\frac12(I+\sigma_z),
\qquad
P_1=\frac12(I-\sigma_z).
\]

Bloch action:

\[
(x,y,z)\mapsto((1-q_1)x,(1-q_1)y,z).
\]

### \(D_x\)

\[
D_x(\rho)=(1-q_2)\rho+q_2(Q_+\rho Q_+ + Q_-\rho Q_-),
\]

\[
Q_+=\frac12(I+\sigma_x),
\qquad
Q_-=\frac12(I-\sigma_x).
\]

Bloch action:

\[
(x,y,z)\mapsto(x,(1-q_2)y,(1-q_2)z).
\]

### \(R_x\)

\[
R_x(\rho)=U_x(\theta)\rho U_x(\theta)^\dagger,
\]

\[
U_x(\theta)=e^{-i\theta\sigma_x/2}.
\]

Bloch action:

\[
(x,y,z)\mapsto(x, y\cos\theta-z\sin\theta, z\cos\theta+y\sin\theta).
\]

### \(R_z\)

\[
R_z(\rho)=U_z(\varphi)\rho U_z(\varphi)^\dagger,
\]

\[
U_z(\varphi)=e^{-i\varphi\sigma_z/2}.
\]

Bloch action:

\[
(x,y,z)\mapsto(x\cos\varphi-y\sin\varphi, x\sin\varphi+y\cos\varphi, z).
\]

## 23. Eight generator families

Use:

\[
D[L](\rho)=L\rho L^\dagger-\frac12(L^\dagger L\rho+\rho L^\dagger L).
\]

Let:

\[
H_L=+H_0,
\qquad
H_R=-H_0.
\]

### 23.1 Left dissipative open flow

\[
X_{1,L}(\rho)=\lambda_L\sum_jD[L_{j,L}](\rho)-i\epsilon_L[H_L,\rho].
\]

### 23.2 Right dissipative open flow

\[
X_{1,R}(\rho)=\lambda_R\sum_jD[L_{j,R}](\rho)-i\epsilon_R[H_R,\rho].
\]

### 23.3 Left Hamiltonian circulation

\[
X_{2,L}(\rho)=-i[H_L,\rho].
\]

Weak version:

\[
X_{2,L}(\rho)=-i[H_L,\rho]+\epsilon\sum_kD[L_k](\rho).
\]

### 23.4 Right Hamiltonian circulation

\[
X_{2,R}(\rho)=-i[H_R,\rho].
\]

Weak version:

\[
X_{2,R}(\rho)=-i[H_R,\rho]+\epsilon\sum_kD[L_k](\rho).
\]

### 23.5 Left lowering / attractor flow

\[
X_{3,L}(\rho)=\gamma_LD[\sigma_-](\rho)-i\epsilon_L[H_L,\rho],
\]

\[
\sigma_-=
\begin{pmatrix}
0&0\\
1&0
\end{pmatrix}.
\]

### 23.6 Right raising / source flow

\[
X_{3,R}(\rho)=\gamma_RD[\sigma_+](\rho)-i\epsilon_R[H_R,\rho],
\]

\[
\sigma_+=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix}.
\]

### 23.7 Left projector-retention flow

\[
X_{4,L}(\rho)=-i[\omega_Lm_L\cdot\sigma,\rho]+\kappa_L(P_+^L\rho P_+^L+P_-^L\rho P_-^L-\rho).
\]

### 23.8 Right projector-retention flow

\[
X_{4,R}(\rho)=-i[\omega_Rm_R\cdot\sigma,\rho]+\kappa_R(P_+^R\rho P_+^R+P_-^R\rho P_-^R-\rho).
\]

No non-math labels belong inside these formulas.

## 24. Flows from generators

For each generator:

\[
\Phi_t=e^{tX}.
\]

Then:

\[
\rho(t)=\Phi_t(\rho_0).
\]

Every flow must check:

\[
\operatorname{Tr}\rho(t)=1,
\]

\[
\rho(t)\geq0,
\]

\[
\rho(t)^\dagger=\rho(t).
\]

## 25. Sixteen placements

There are:

\[
2\text{ sheets}\times2\text{ loop fields}\times4\text{ generator families}=16
\]

objects:

\[
(X_{a,s},Y_\ell),
\]

where:

\[
a\in\{1,2,3,4\},
\quad
s\in\{L,R\},
\quad
\ell\in\{f,b\}.
\]

This is a real mathematical layer. A generator alone is not the same as the generator placed on a fiber or base loop.

## 26. Terrain/operator order maps

For operator \(O\) and flow \(\Phi_T\):

\[
O_T^+(\rho)=\Phi_T(O(\rho)),
\]

\[
O_T^-(\rho)=O(\Phi_T(\rho)).
\]

Order gap:

\[
\Delta_{T,O}(\rho)=O_T^+(\rho)-O_T^-(\rho).
\]

Measure:

\[
\|\Delta_{T,O}(\rho)\|_1.
\]

There are:

\[
8\times4\times2=64
\]

composite cells.

## 27. Stacked preservation / leakage tests

For any flow \(\Phi\):

\[
\Phi(T_\eta)\subseteq T_\eta?
\]

\[
\Phi(T_\eta)\subseteq T_{\eta'}?
\]

or does it leave the torus foliation?

Since:

\[
z=\cos(2\eta),
\]

shell leakage can be measured by:

\[
\frac{dz}{dt}.
\]

Examples that must be tested, not assumed:

- \(R_z\) preserves \(z\), so it preserves Hopf shells.
- \(R_x\) generally changes \(z\), so it crosses shells.
- Dephasing can move pure states into \(B^3\) and destroy pure-torus structure.
- Dissipative generators require the Bloch ball, not just \(S^2\).

## 28. Two-site systems

\[
\mathbb C^2\otimes\mathbb C^2.
\]

Joint state:

\[
\rho_{AB}.
\]

Partial traces:

\[
\rho_A=\operatorname{Tr}_B(\rho_{AB}),
\qquad
\rho_B=\operatorname{Tr}_A(\rho_{AB}).
\]

Entanglement entropy:

\[
S(\rho_A).
\]

Conditional entropy:

\[
S(A|B)=S(AB)-S(B).
\]

Mutual information:

\[
I(A:B)=S(A)+S(B)-S(AB).
\]

Coherent information:

\[
I_c=-S(A|B).
\]

## 29. Three-spinor floor

\[
(\mathbb C^2)^{\otimes3}.
\]

\[
\dim_\mathbb C=8.
\]

State:

\[
\Psi\in(\mathbb C^2)^{\otimes3}.
\]

Density:

\[
\rho_\Psi=\Psi\Psi^\dagger.
\]

This is the minimum floor for a three-slot bracket:

\[
((ab)c)\Psi
\]

versus:

\[
(a(bc))\Psi.
\]

## 30. Clifford algebra \(Cl(6)\)

Generators:

\[
\gamma_1,\ldots,\gamma_6,
\]

with:

\[
\gamma_i\gamma_j+\gamma_j\gamma_i=2\delta_{ij}.
\]

Complex form:

\[
Cl_6(\mathbb C)\cong M_8(\mathbb C).
\]

This matches:

\[
(\mathbb C^2)^{\otimes3}\cong\mathbb C^8.
\]

## 31. Weyl chirality in four-spinor language

Four-component spinor:

\[
\Psi=
\begin{pmatrix}
\psi_L\\
\psi_R
\end{pmatrix}.
\]

Chirality matrix:

\[
\gamma^5=\operatorname{diag}(-1,-1,+1,+1).
\]

Projectors:

\[
P_L=\frac12(I-\gamma^5),
\qquad
P_R=\frac12(I+\gamma^5).
\]

## 32. Division algebra ladder

\[
\mathbb R,
\quad
\mathbb C,
\quad
\mathbb H,
\quad
\mathbb O.
\]

Dimensions:

\[
1,2,4,8.
\]

Imaginary-unit counts:

\[
0,1,3,7.
\]

Associative:

\[
\mathbb R,\mathbb C,\mathbb H.
\]

Nonassociative but alternative:

\[
\mathbb O.
\]

Unit quaternions:

\[
\{q\in\mathbb H:|q|=1\}\cong S^3.
\]

## 33. Full normed-division Hopf fibration ladder

The four rungs are:

\[
S^0\hookrightarrow S^1\to S^1,
\]

\[
S^1\hookrightarrow S^3\to S^2,
\]

\[
S^3\hookrightarrow S^7\to S^4,
\]

\[
S^7\hookrightarrow S^{15}\to S^8.
\]

These correspond to:

\[
\mathbb R,
\mathbb C,
\mathbb H,
\mathbb O.
\]

Base dimensions:

\[
1,2,4,8.
\]

Fiber dimensions:

\[
0,1,3,7.
\]

Adams termination: no fifth normed-division Hopf fibration. Sedenion zero divisors break the norm law.

## 34. Octonion multiplication / Fano plane

Octonion units:

\[
e_i,
\quad
i=1,\ldots,7.
\]

Multiplication:

\[
e_ie_j=-\delta_{ij}+\sum_k f_{ijk}e_k,
\]

where:

\[
f_{ijk}=\pm1
\]

on oriented lines of the Fano plane.

Associator:

\[
[a,b,c]=(ab)c-a(bc).
\]

Alternativity:

\[
[a,a,b]=0,
\qquad
[a,b,b]=0.
\]

Ordered triples of distinct imaginary units:

\[
7\cdot6\cdot5=210.
\]

Fano-line associative triples:

\[
42.
\]

Nonzero associator triples:

\[
168.
\]

and:

\[
168=|PSL(2,7)|.
\]

Table orientation/convention must be pinned. A valid basis-orientation difference is not automatically a math disagreement.

## 35. \(G_2\)

\[
G_2=\operatorname{Aut}(\mathbb O).
\]

Imaginary octonions:

\[
\operatorname{Im}\mathbb O\cong\mathbb R^7.
\]

Octonion 3-form:

\[
\varphi(x,y,z)=\langle xy,z\rangle.
\]

Then:

\[
G_2=\{g\in GL(7,\mathbb R):g^*\varphi=\varphi\}.
\]

Dimension:

\[
\dim G_2=14.
\]

This is likely but not forced from names. It must survive variant controls.

## 36. \(SU(3)\subset G_2\)

Fix:

\[
u\in S^6\subset\operatorname{Im}\mathbb O.
\]

Then:

\[
\operatorname{Stab}_{G_2}(u)\cong SU(3).
\]

So:

\[
SU(3)\subset G_2,
\]

and:

\[
G_2/SU(3)\cong S^6.
\]

Dimension check:

\[
14-8=6.
\]

## 37. Exceptional Jordan algebra

The missing rung between octonion/\(G_2\) and higher exceptional geometry is:

\[
J_3(\mathbb O),
\]

the algebra of \(3\times3\) Hermitian octonionic matrices.

Dimension:

\[
\dim J_3(\mathbb O)=27.
\]

Automorphism group:

\[
F_4=\operatorname{Aut}(J_3(\mathbb O)).
\]

Dimension:

\[
\dim F_4=52.
\]

Octonionic projective plane:

\[
\mathbb OP^2=F_4/Spin(9).
\]

This must remain in the tower. Do not drop it when summarizing octonion/\(G_2\) work.

## 38. \(Spin(7)\)

\[
Spin(7)\subset SO(8).
\]

It preserves the Cayley 4-form:

\[
\Omega.
\]

A \(Spin(7)\)-structure:

\[
(M^8,\Omega).
\]

Stabilizer relation:

\[
G_2\subset Spin(7).
\]

Coset:

\[
Spin(7)/G_2\cong S^7.
\]

Dimension check:

\[
21-14=7.
\]

## 39. \(Spin(8)\) triality

\[
Spin(8)
\]

has three eight-dimensional representations:

\[
8_v,
\quad
8_s,
\quad
8_c.
\]

Triality permutes them.

## 40. Split octonions / split \(G_2\)

Split octonions:

\[
\mathbb O_s.
\]

They have indefinite norm.

Automorphism group:

\[
G_{2(2)}.
\]

Geometry:

\[
(\mathbb R^{3,4},\varphi_{\text{split}}).
\]

This branch remains open until compact-vs-split controls decide it.

## 41. Sedenions / zero-divisor boundary

\[
\mathbb S=\mathbb O\oplus\mathbb O.
\]

Dimension:

\[
\dim_\mathbb R\mathbb S=16.
\]

Zero divisors exist:

\[
x\neq0,
\qquad
y\neq0,
\qquad
xy=0.
\]

The finite incidence structure is:

\[
PG(3,2),
\]

with:

\[
15\text{ points},
\qquad
35\text{ lines},
\qquad
15\text{ planes}.
\]

This is boundary/control geometry, not carrier promotion.

## 42. Ring/checkerboard discretization of Hopf tori

A discrete torus sample must be:

\[
T_\eta^{N_\phi,N_\chi}=\left\{\psi\left(\frac{2\pi a}{N_\phi},\frac{2\pi b}{N_\chi},\eta\right)\right\}.
\]

with:

\[
a=0,\ldots,N_\phi-1,
\qquad
b=0,\ldots,N_\chi-1.
\]

Graph:

\[
\mathbb Z_{N_\phi}\times\mathbb Z_{N_\chi}.
\]

Parity:

\[
\kappa(a,b)=a+b\pmod2.
\]

But the physical spinor identification is:

\[
(a,b)\sim(a+N/2,b+N/2)
\]

for even \(N\). A ring/checkerboard sim that ignores this is not a valid Hopf-torus discretization.

Refinement:

\[
2\to4\to8\to16\to32\to64
\]

must converge to continuous invariants: area, holonomy, flux, and quotient counts.

## 43. Engine/path geometry — deferred, not deleted

The engine/dynamics layer must wait until the lower geometry is real. When it returns, it must be stated as maps and path identifications, not as readout words.

Example path/order maps:

\[
\Phi_D=U\circ E\circ U\circ E,
\]

\[
\Phi_I=E\circ U\circ E\circ U.
\]

Order gap:

\[
\Delta_{D,I}(x)=\Phi_D(x)-\Phi_I(x),
\]

or quotient-aware:

\[
\Phi_D(x)\not\sim\Phi_I(x).
\]

Möbius-like identification, if claimed, must be literal:

\[
(\theta,s)\sim(\theta+2\pi,-s).
\]

This layer is deferred behind the geometry-first stages. Deferred does not mean erased.

## 44. Constraint manifold over the stack

Let \(\mathcal A_t\) be the ambient stacked geometry at time \(t\), containing whichever of the above layers are active and earned.

Constraints:

\[
C_i(x)=0
\]

or:

\[
C_i(x)\geq0.
\]

Admissible object:

\[
M(C,t)=\{x\in\mathcal A_t:C_i(x)\text{ holds for all active }i\}/\sim_P.
\]

Probe quotient:

\[
x\sim_Py
\iff
p_j(x)=p_j(y)
\quad\forall j.
\]

Time maps:

\[
f_t:M(C,t)\to M(C,t+1).
\]

Those maps must explicitly state their effect on:

\[
S^3,
\quad
S^2,
\quad
T_\eta,
\quad
A,
\quad
F,
\quad
\rho,
\quad
X,
\quad
O,
\quad
\Delta.
\]

Do not say the full geometric constraint manifold is built until this constrained stacked object exists.

---

# Sim dependency order

## Stage 1 — spinor / Hopf foundation

1. \(\mathbb C^2\) normalized spinors.
2. \(S^3\) metric and volume.
3. \(SU(2)\) / unit quaternion structure.
4. \(SU(2)\to SO(3)\) double cover.
5. Hopf map \(S^3\to S^2\).
6. \(S^1\) fibers.
7. fiber linking number \(1\).
8. density quotient identity.
9. \(S^2\) base and Haar pushforward.

## Stage 2 — connection / flux / foliation

1. Hopf connection \(A\).
2. curvature \(F=dA\).
3. holonomy convention pin.
4. Berry half-solid-angle convention pin.
5. Stokes consistency.
6. total Chern-like integral.
7. Hopf tori \(T_\eta\).
8. double-cover correction.
9. nested Hopf tori.

## Stage 3 — density / probes / metrics

1. Bloch ball.
2. entropy and purity.
3. expectation planes.
4. Born probabilities.
5. measurement update.
6. probe equivalence quotient.
7. trace distance.
8. fidelity.
9. CPTP contraction.

## Stage 4 — channel and operator geometry

1. channel space.
2. Pauli algebra.
3. \(D_z\).
4. \(D_x\).
5. \(R_x\).
6. \(R_z\).
7. fixed axes.
8. ellipsoid images.

## Stage 5 — generators / flows / basins

1. eight generator families.
2. finite-time flows.
3. CPTP / trace / positivity checks.
4. fixed points.
5. basins.
6. unital vs non-unital behavior.

## Stage 6 — stacked action

1. generator action on Hopf tori.
2. shell leakage.
3. action on \(A\).
4. action on \(F\).
5. action on holonomy.
6. sixteen placements.
7. terrain/operator order gaps.
8. sixty-four composite cells.
9. loop-order maps, if the map definitions are explicit.

## Stage 7 — finite discretization

1. torus grids.
2. double-cover quotient on grids.
3. checkerboard parity.
4. refinement convergence.
5. convergence to continuous area, holonomy, and flux.

## Stage 8 — two-site / three-site / Clifford floor

1. \((\mathbb C^2)^{\otimes2}\).
2. partial trace.
3. entanglement entropy.
4. conditional entropy.
5. coherent information.
6. \((\mathbb C^2)^{\otimes3}\).
7. \(Cl(6)\).
8. Weyl/chirality projectors.

## Stage 9 — division algebra / nonassociative tower

1. \(\mathbb R\).
2. \(\mathbb C\).
3. \(\mathbb H\).
4. \(\mathbb O\).
5. four Hopf fibrations.
6. Adams termination.
7. octonion/Fano multiplication.
8. associator.
9. alternativity.
10. sedenion zero-divisor kill.

## Stage 10 — exceptional structure tower

1. \(G_2=\operatorname{Aut}(\mathbb O)\).
2. \(SU(3)\subset G_2\).
3. \(J_3(\mathbb O)\).
4. \(F_4\).
5. \(\mathbb OP^2\).
6. \(Spin(7)\).
7. \(Spin(8)\) triality.
8. split \(G_{2(2)}\).
9. sedenion / \(PG(3,2)\) boundary.

## Stage 11 — constrained manifold

1. ambient stacked geometry \(\mathcal A_t\).
2. active constraints \(C_i\).
3. admissible subset.
4. probe quotient.
5. time maps.
6. explicit effects on the lower geometry.
7. no promotion until the constrained stacked object exists.

---

# Anti-collapse rules for future sims

A sim must not collapse layers by name similarity.

## Required declarations

Every sim must declare:

1. the exact mathematical object;
2. whether it is free, restricted/stacked, or quotiented;
3. which lower geometry it depends on;
4. which lower geometry it preserves, moves within, leaves, or erases;
5. exact invariants checked;
6. exact controls that can fail;
7. what distinctions are killed by quotienting;
8. whether it is a geometry sim or only a diagnostic/claim packet.

## Forbidden collapses

Do not collapse:

- \(S^3\) into \(S^2\);
- spinor phase into density matrix;
- Hopf torus chart count into physical torus count;
- holonomy convention into Berry convention without a pin;
- \(B^3\) channel geometry into the full carrier;
- a ring/checkerboard graph into Hopf-torus geometry unless it handles the torus quotient and convergence;
- octonion table convention differences into factual contradictions without a basis/orientation check;
- \(G_2\) into a final answer without compact/split/reduction controls;
- sedenions into carrier promotion despite zero divisors;
- deferred engine maps into geometry completion.

## Safe status language

Use:

```text
roadmap committed
free-mode sim exists / does not exist
artifact observed
validator green
scratch diagnostic
not admitted
not promoted
in flight
mixed-version
quotient erases X
stacked flow preserves/moves/leaves Y
```

Do not use compact closure slogans such as:

```text
canonical-geometry-built
full-manifold-complete
bloch-sphere-root-carrier
ring-checkerboard-proves-nested-tori
g2-forced
sedenion-carrier-admitted
engine-geometry-complete
```

These hyphenated forms are intentionally not the exact slogans future scans should treat as claims.

## Current reset sentence

Use this sentence until the Stage-1 geometry sim actually lands and is verified:

```text
The canonical geometry program is now recorded, but the free-mode geometry stages are not completed; older packets are useful scratch diagnostics, not substitutes for simming the known geometry in order.
```
