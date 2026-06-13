# FEP and Entropic Gravity: Gradient Flow on Information Functionals

Date: 2026-06-12
Status: research corpus, not admitted sim evidence
Provenance: recall-based items marked [recall]; repo-cited items cite committed
  artifact paths; owner-voice items cite source paths.

---

## Scope and ceiling

This note covers: (1) the Free Energy Principle's finite/computable core;
(2) the standard entropic-gravity results; (3) the honest relation between the
two as gradient-flow-on-information-functional families; (4) repo relevance for
the Axis-0 contender registry, the basin-cycle packet, and the S8 table.

Nothing here authorizes sim execution, bridge claims, physics admission, or
Axis-0 closure. All repo-side promotions remain at the status recorded in the
cited committed artifacts.

---

## 1. Free Energy Principle — finite/computable core

### 1.1 Variational free energy on a finite state space

The variational free energy is defined as:

```
F = E_q[-ln P(y,x)] - H[q(x)]
```

where `q(x)` is the recognition density over hidden states `x`, `P(y,x)` is
the generative density, and `H` is Shannon entropy. Two equivalent
decompositions:

```
F = D_KL[q(x) || P(x|y)] + (-ln P(y))    (KL + surprise)
F = D_KL[q(x) || P(x)] - E_q[ln P(y|x)]  (complexity - accuracy)
```

Since `KL >= 0`, free energy upper-bounds surprise `-ln P(y)`. Minimizing `F`
over `q` is approximate Bayesian inference.

On a finite state space, both `q` and `P` are finite probability distributions
(or, in the quantum extension, density matrices). All expectations and KL
divergences are finite sums or traces. Gradient descent on `F` with respect to
internal state parameters `mu` is:

```
dmu/dt = -dF/dmu
```

This is an ordinary gradient flow on a finite-dimensional parameter space.
A corresponding repo sim in `system_v4/probes/sim_fep_deep_active_inference_gradient_flow.py`
implements Gaussian KL free energy with pytorch autograd; the positive test
requires monotone decrease and convergence to the sensory state `s`; the
negative test requires that ascent (wrong sign) increases `F`.

### 1.2 Expected free energy (policy selection)

For policy selection over future time horizons, the expected free energy `G`
decomposes as:

```
G(pi) = -E_Q(s|pi)[H[P(o|s)]] + D_KL[Q(o|pi) || P(o)]
       = epistemic value (information gain) + pragmatic value (preference)
```

This is distinct from the variational `F`. Policy selection uses `G`; inference
uses `F`. The two-objective structure is the computable version: on a finite
observation and state space, both are finite sums.

### 1.3 Markov blanket partition

Friston's partition (from Pearl 1988 Bayesian nets) divides states into:

```
external (eta)  — hidden causes
sensory  (s)    — read by internal, affected by external
active   (a)    — written by internal, affects external
internal (mu)   — the agent's internal dynamics
```

Blanket = sensory + active. Given the blanket, internal and external states are
conditionally independent: `P(mu,eta | s,a) = P(mu|s,a) P(eta|s,a)`.

The conditional independence claim is testable on any finite precision matrix.
A repo sim in `system_v4/probes/sim_holodeck_deep_coupling_to_fep_markov_blanket.py`
verifies it via Schur-complement conditional covariance on a pytorch
4x4 precision matrix; the negative test confirms that a nonzero direct
`mu-eta` coupling breaks the blanket property continuously.

The harness framing aligns: internal states are `INDISTINGUISHABLE` from
external except through the blanket; direct `mu-eta` coupling is `EXCLUDED` by
the blanket construction.

### 1.4 NESS connection [recall]

Under Langevin dynamics `dx/dt = f(x) + omega`, at a nonequilibrium steady
state (NESS) the Helmholtz decomposition separates `f(x)` into a dissipative
(curl-free) gradient part `-(Q+Gamma) nabla ln p*(x)` and a solenoidal
(divergence-free) part circulating on iso-probability surfaces. Systems that
persist at NESS look as if they minimize surprisal `-ln p*(x)`. This is the
physics backing for the FEP's "systems that exist minimize free energy" claim.

Source in wiki: `~/wiki/raw/articles/new-docs/references/FEP_AND_ACTIVE_INFERENCE_REFERENCE.md`
(lines 96-109).

---

## 2. Negatives — what FEP does NOT establish

These are the load-bearing criticisms. They matter for repo-side FEP use.

### 2.1 Tautology / unfalsifiability (strongest)

Any system with a Markov blanket at NESS can be redescribed as minimizing
variational free energy. If it applies to all persistent systems, it predicts
nothing specific. Friston's response: FEP is a mathematical framework
(analogous to the principle of stationary action), not a falsifiable theory;
specific models derived from it are falsifiable.

Source: `FEP_AND_ACTIVE_INFERENCE_REFERENCE.md` (lines 175-196):
"Any system with a Markov blanket at NESS can be described as minimizing free
energy. If it applies to everything, it predicts nothing specific."

Repo implication: FEP-adjacent sims must name the finite observables, controls,
and falsifiers that go beyond the tautology shell. The cited sim
`sim_fep_deep_active_inference_gradient_flow.py` earns its canonical label
because the negative test (ascent increases `F`) falsifies the wrong-sign
candidate and the fixed-point zero-gradient test falsifies non-convergence.
That is the pattern.

### 2.2 Technical errors in blanket definitions (Biehl, Pollock, Kanai 2021)

Definitions of "Markov blanket" across Friston's papers are not equivalent.
Crucial equation rewriting steps are "not generally correct without additional
previously unstated assumptions." The free energy lemma is "proved by
counterexample to be wrong when taken at face value."

Source: `FEP_AND_ACTIVE_INFERENCE_REFERENCE.md` (lines 182-185).

Repo implication: any blanket-based sim must state which blanket definition
it uses (statistical / conditional independence / precision-matrix structural
zero) and keep to that definition throughout. The precision-matrix version used
in the Holodeck-FEP coupling sim is clean because it is testable directly.

### 2.3 Statistical blanket vs physical boundary (Bruineberg et al.)

The step from a statistical Markov blanket to a physical system boundary
involves an unjustified metaphysical leap. A Markov blanket is statistical;
treating it as a physical boundary conflates map and territory.

Source: `FEP_AND_ACTIVE_INFERENCE_REFERENCE.md` (lines 186-190).

Repo implication: the harness's nominalist constraint — probe families `M`
define the equivalence, not primitive identity — blocks the statistical-to-
physical collapse directly. A Markov blanket in this system is a structural
zero in a precision or coupling matrix, not a claim about what objects are.

### 2.4 Blanket decomposition failure conditions [recall]

The blanket partition fails or degrades when:
- direct `mu-eta` coupling is nonzero (the negative control in the Holodeck sim
  demonstrates this is a monotone degradation, not a step change);
- the state space has cycles that route information through non-blanket paths;
- the system is far from NESS with strong transient correlations.

None of these are exotic failure modes; they are routine situations for
non-equilibrium or strongly-coupled systems.

---

## 3. Entropic gravity — standard results

### 3.1 The thermodynamic-gradient family [recall]

The family of entropic-gravity or thermodynamic-gravity proposals includes at
least three distinct levels:

(a) **Black hole thermodynamics** (Bekenstein 1972, Hawking 1974-1975):
Black holes carry entropy `S_BH = A / (4 G hbar)` proportional to horizon area
`A`. They satisfy a set of laws formally analogous to the laws of
thermodynamics. This is an established result with experimental support
(Hawking radiation as a theoretical prediction, Bekenstein bound as a
computable constraint). Source in wiki raw: `density_matrices_across_fields.md`
cites `S_BH = A / (4 G_N hbar)` as exact under AdS/CFT.

(b) **Jacobson 1995 derivation** [recall-tagged, primary source not on file]:
Ted Jacobson showed in 1995 (Phys Rev Lett 75:1260) that the Einstein field
equations can be derived from the proportionality of entropy to horizon area
plus the thermodynamic identity `delta Q = T dS` applied to local Rindler
horizons seen by accelerating observers. This is a standard result in the
thermodynamics-of-spacetime program. It says GR arises as a thermodynamic
equation of state, not as a fundamental geometric law. The Raychaudhuri equation
and the Clausius relation are the key ingredients; no quantum gravity is needed.
[recall-flagged: this entry is from knowledge, not from a file on disk in this
repo/wiki. The stochastic-thermodynamics reference cites `1210.5071v1`
(stochastic thermodynamics and reversible dynamical systems) which in its
reference list includes Verlinde's 2011 JHEP paper; Jacobson's 1995 paper is
in the same tradition but not in a local file.]

(c) **Verlinde 2011 (entropic gravity)**: Gravity as an entropic force. The
gravitational force on a test mass near a holographic screen emerges from the
entropy gradient associated with the mass's displacement. Formally: the force is
`F = T (dS/dx)` where the entropy gradient is evaluated on the screen.

Verlinde's proposal is explicitly catalogued in the repo/wiki and described
relative to the owner's model:

> "Verlinde's claim that gravity is an entropic force — not fundamental but
> emergent from information/entropy gradients — is structurally aligned. But
> his formulation assumes classical thermodynamics, holographic screens, and
> temperature as primitives."
>
> Source: `~/wiki/raw/articles/system-v5-reference-docs/MODEL_CONTEXT copy.md`
> (lines 113-117), classification `llm-elaboration` (assistant consolidation,
> not owner voice).

The Verlinde formulation also appears in the legacy genealogy table:
`~/wiki/raw/articles/new-docs/LEGACY_CONTEXT_AND_GENEALOGY.md` line 48:
`| Entropic gravity | Verlinde | Gravity as emergent from entropy | Classical thermodynamic framing |`

And in `DR_entropic_monism_hopf.md` (legacy deep research result):
> "Entropic-gravity proposals (notably Erik Verlinde) treat gravitational
> dynamics as emergent from information/entropy considerations, explicitly tying
> 'space emergence' to information associated with matter configurations...
> conceptually adjacent to your 'distance from mutual information' axiom, though
> your proposal is more microscopic/operational (graph + quantum channels) than
> Verlinde's macroscopic thermodynamic argument."

### 3.2 What is established vs speculative [recall + source-flagged]

Established (standard textbook/literature):
- Black hole entropy is proportional to horizon area (Bekenstein-Hawking).
- The Clausius relation applied to local Rindler horizons gives Einstein's
  equations (Jacobson). [recall]
- The Raychaudhuri equation gives the rate of change of the expansion of a
  congruence of null geodesics; combined with the proportionality of entropy to
  area, it produces the thermodynamic form of the Einstein equations. [recall]
- Mutual information / entanglement entropy is related to bulk geometry in
  AdS/CFT (Ryu-Takayanagi formula, 2006). [recall; mentioned in DR_entropic_monism_hopf.md]

Speculative (not derivation-complete):
- Verlinde's entropic-force proposal recovers Newton's law and, in his 2016
  extension, claims dark matter can be explained as an entropic effect. The
  2016 extension is contested. [recall]
- Deriving the inverse-square law from an entropy gradient requires assuming
  a holographic screen with specific area scaling. The assumption is not
  independently derived.
- Connecting entropic gravity to Newtonian dynamics via the Unruh temperature
  requires the proportionality of acceleration to local temperature to already
  hold; this is a premise, not a conclusion.

The repo's own risk audit for the physics docs names the open status explicitly:
"no proof of Axis0, no proof of gravity, no proof of physics or manifold, exact
Xi_shell open, exact Phi0 projection open, inverse-square shell law only a
modeling target."
Source: `~/wiki/concepts/axis0-physics-source-teeth-map.md` (section "Gravity
audit status/risk list").

### 3.3 Negatives for entropic gravity [recall]

- The Verlinde proposal has not produced a complete derivation of GR from
  entropy gradients at the level of rigor of Jacobson's 1995 derivation.
- The holographic screen assumption bakes in an areal scaling that begs the
  question about geometry.
- Classical temperature and thermodynamic equilibrium are assumed as primitives;
  the machinery breaks down for non-equilibrium processes without an extension.
- The Rindler-horizon / Unruh-temperature argument is local; extending it to
  global gravitational potentials requires additional steps that have not been
  cleanly established.
- Dark matter as an entropic effect (Verlinde 2016) is observationally contested;
  galaxy cluster data (e.g., Bullet Cluster) is difficult to explain without
  localized matter. [recall]

---

## 4. Honest relation: shared mechanics, different basis

The owner's doctrine receipt at `system_v6/receipts/owner_doctrine_carnot_szilard_connection_20260612.md`
(commit `24d03db89`) establishes the "same mechanics, different basis" pattern
for Carnot (thermodynamic) and Szilard (informational) engines.

The same pattern applies to FEP and entropic gravity. Both are members of a
broader family: **gradient flow on information functionals**.

| Mechanic | FEP basis | Entropic gravity basis |
|---|---|---|
| The functional | variational free energy `F = KL[q||P(x|y)] + surprise` | entropy `S` as a function of horizon area / information configuration |
| The gradient | `dF/dmu` over internal-state parameter space | `dS/dx` over displacement toward/away from a holographic screen |
| The flow | `dmu/dt = -dF/dmu` (perception minimizes `F`) | `F = T dS/dx` (force from entropy gradient, Verlinde) |
| The fixed point | `q = P(x|y)` (true posterior) | equilibrium configuration where entropy is stationary |
| The legality fence | below-Landauer / unpaid-erasure UNSAT | Clausius inequality / second law |
| Source convention | Friston (2005-2019), Bayesian inference, NESS | Bekenstein-Hawking, Jacobson 1995, Verlinde 2011 |
| Classical residue to strip | continuous time, classical probability, fixed generative model | classical thermodynamics, temperature as primitive, holographic screen as assumed |

The shared mechanics column is the owner's pattern: the underlying dynamical
structure (cycle/flow, per-step ledger, legality fence, fixed point) repeats
across different basis geometries. This is a candidate alignment, not a proof.

**What is NOT established by noting the shared family:**
- FEP and entropic gravity are not the same theory.
- Deriving GR from FEP, or FEP from entropic-gravity mechanics, would require
  additional steps that are not currently earned.
- The tautology critique for FEP applies here: the shared-mechanics observation
  can be made for any gradient flow; naming the family does not give empirical
  content.
- No Axis-0 admission, bridge claim, or physics result follows from this note.

**What IS computable across the family:**
- In the FEP setting, the gradient `dF/dmu` is exactly computable on a finite
  state space with a finite precision matrix. The monotone-decrease positive test
  and the ascent negative test are load-bearing controls. [evidenced by committed
  sim in system_v4/probes/sim_fep_deep_active_inference_gradient_flow.py]
- In the entropic-gravity setting on a discrete carrier, the entropy gradient
  `dS/dx` over the discrete state transitions is also computable. The repo's
  Axis-0 contender candidate `A0.CP.3_entropy_gradient_sign` is exactly this:
  per cell, the signed change in a committed entropy/readout scalar under each
  outgoing generator update.
- The Szilard / basin-cycle connection is the nearest committed evidence: the
  `carnot_szilard_basin_cycle_v0` packet earns that the per-cycle typed ledger
  closes (defect 0), the Basin-Landauer floor holds (relaxation merging `m`
  states dissipates >= ln(m)), and the stroke-to-stroke structure map is emitted.
  Source: `system_v6/receipts/owner_doctrine_carnot_szilard_connection_20260612.md`
  (adjudication entry v0).

---

## 5. Repo relevance

### 5.1 Axis-0 contender registry

The `axis0_contender_probe_registry_20260612.md` (commit `fcf1b385`) registers
11 candidates. Of these, `A0.CP.3_entropy_gradient_sign` is the entry closest
to the entropic-gravity family: it asks for the signed entropy gradient per cell
over directed outgoing generator updates. It is classified `co-survivor-open`,
`heavy-local`, adapter required — meaning it cannot be tested in the current
light-symbolic phase until a source-backed 33-cell adapter for the entropy kind
exists.

The alias rule is explicit: two entropy readouts alias only if the 33-cell sign
vector and exact rank partition match under monotone reparameterization. Equal
total entropy or equal monotonicity of total entropy is NOT alias.

`A0.CP.7_lyapunov_descent_direction` is the entry closest to the FEP family:
it asks for the sign of descent in a finite Lyapunov functional over the carrier.
It is also `co-survivor-open`, `heavy-local`. The registry warns that a probe
reading stability/damping only is classified `wrong_distinction` unless it
matches the positive/negative feedback doctrine.

Both CP.3 and CP.7 require a source-backed 33-cell adapter before the heavy
battery can run.

### 5.2 Basin-cycle packet

`carnot_szilard_basin_cycle_v0` (adjudicated 2026-06-12, commit `24d03db89`)
earns the Szilard/Carnot connection at scratch-ceiling. The relevant mechanics
in the FEP/gravity vein: the Basin-Landauer floor (`relaxation merging m states
dissipates >= ln m`) is the legality fence for the basin basis, exactly
analogous to the Landauer floor in Szilard and the Carnot limit in Carnot.

This is the only committed packet that provides a structural bridge across the
three bases. Its scope fences are explicit: `heat/work variables, bath-gating,
and any physics reading — the connection is typed-counting mechanics, earned
exactly that far.`

### 5.3 S8 table

`s8_local_information_table_v0` (commit `859df13e3`, GENUINE-WITH-CAVEATS)
closes the S8-local `S(A|B)`, `I(A:B)`, `I_c` gap identified in the S8
adjudication. It computes these quantities for the three-spinor/Clifford floor
`(C^2)^x3` with 66 identity-channel rows over fixed state fixtures and
bipartitions.

The FEP connection: conditional entropy `S(A|B) = S(AB) - S(B)` and coherent
information `I_c = S(B) - S(AB)` are the quantities that govern whether
information is preserved or erased across a quantum channel. This is the
quantum-information-theoretic version of the FEP's "surprise = -ln P(y)"
evaluated per subsystem. A negative conditional entropy `S(A|B) < 0` signals
quantum correlations (entanglement) that have no classical FEP analogue.

The S8 table is a scratch-diagnostic carrier result, not an Axis-0 probe, not
a basin-cycle result, and not a physics claim. Its relevance here is that it
provides the exact fixed-state information quantities needed to build a
source-backed 33-cell adapter for `A0.CP.3_entropy_gradient_sign`.

---

## 6. Source inventory

### On-disk in repo/wiki (read):
- `~/wiki/raw/articles/new-docs/references/FEP_AND_ACTIVE_INFERENCE_REFERENCE.md`
  — formal FEP reference including critiques; provenance: llm-elaboration
  (assistant-assembled reference doc, April 2026).
- `~/wiki/concepts/stochastic-thermodynamics-reference.md`
  — NESS, Jarzynski, Crooks, Landauer, quantum extensions; the FEP/NESS
  analogy is flagged as "formal analogy/support bridge to stochastic-thermodynamic
  NESS language, not as a settled literal identity claim."
- `~/wiki/raw/articles/system-v5-reference-docs/MODEL_CONTEXT copy.md`
  — owner model vs Verlinde: `llm-elaboration` (system-v5 context doc).
- `~/wiki/raw/articles/new-docs/LEGACY_CONTEXT_AND_GENEALOGY.md`
  — genealogy table with `| Entropic gravity | Verlinde | ... |`
- `~/Codex-Ratchet/READ ONLY Legacy core_docs/deep_research_results/DR_entropic_monism_hopf.md`
  — old deep-research result, FEP + Verlinde adjacency noted; ceiling:
  research-history, not current admission.
- `~/Codex-Ratchet/system_v6/receipts/owner_doctrine_carnot_szilard_connection_20260612.md`
  — committed owner doctrine, same-mechanics pattern; `owner-source`.
- `~/Codex-Ratchet/system_v6/receipts/axis0_contender_probe_registry_20260612.md`
  — committed registry; `owner-source` (owner-gated receipt).
- `~/wiki/codex-ratchet-research/basins/standard-math.md`
  — basin/Conley standard math; `llm-elaboration` (corpus note).
- `~/Codex-Ratchet/system_v4/probes/sim_fep_deep_active_inference_gradient_flow.py`
  — committed sim, canonical, pytorch load-bearing.
- `~/Codex-Ratchet/system_v4/probes/sim_holodeck_deep_coupling_to_fep_markov_blanket.py`
  — committed sim, canonical, pytorch load-bearing.

### [recall]-tagged entries (knowledge, no on-disk file verified):
- Jacobson (1995) derivation of Einstein equations from Clausius + area entropy.
- Verlinde (2011) entropic force: `F = T dS/dx`.
- Raychaudhuri equation as an ingredient in the Jacobson derivation.
- Ryu-Takayanagi formula relating entanglement entropy to bulk area in AdS/CFT.
- Verlinde (2016) dark-matter extension and observational contestation.
- Bullet Cluster gravitational lensing evidence against purely entropic dark matter.

---

## 7. Promotion boundary

This note is admissible as research-corpus input for:
- Designing source-backed 33-cell adapters for CP.3 (entropy gradient) and CP.7
  (Lyapunov descent) in the axis-0 contender sweep.
- Grounding the "legality fence" row in future basin-cycle packets using the
  Landauer / Clausius family analogy.
- Informing FEP-adjacent controls: the tautology critique maps directly onto
  the harness requirement that a sim must have a falsifying negative test, not
  just a positive that shows free-energy descent.

This note does NOT authorize:
- Axis-0 admission.
- Bridge, physics, or manifold promotion.
- "THE Axis-0 readout is an entropy gradient."
- Any gravity, dark energy, or physics result.
- Promotion of any FEP sim beyond its current status label.
- Treating the "shared mechanics" column as a proof that FEP = entropic gravity.
