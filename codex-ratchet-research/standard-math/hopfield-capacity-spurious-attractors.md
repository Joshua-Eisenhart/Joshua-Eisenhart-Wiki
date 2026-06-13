# Hopfield Network Capacity and Spurious Attractor Theory

Source status: standard-math corpus, recall-based from published literature.
Items marked [recall] have not been web-verified this session; treat as
provisional until a live search confirms them. No promotion to repo evidence.
Ceiling: research-corpus input only.

---

## 1. Core Finite/Computable Definitions

**Hopfield network (classical, discrete-time).** N binary neurons, states
`s_i in {-1,+1}`. Weight matrix W is N×N, real, symmetric, zero diagonal
(`W_ii = 0`). Synchronous update: every neuron updates simultaneously,
`s_i(t+1) = sgn(sum_j W_ij s_j(t))`. Asynchronous update: one neuron updates
per step, chosen uniformly or in a fixed sweep order.

**Hebbian (outer-product) learning rule.** Given P stored patterns
`xi^mu in {-1,+1}^N`, `mu = 1..P`:

```
W_ij = (1/N) * sum_{mu=1}^{P} xi_i^mu * xi_j^mu    (i != j),  W_ii = 0
```

This is the construction whose capacity is ~0.138N (see section 3).

**Energy function (Lyapunov function for asynchronous update):**

```
E(s) = -(1/2) * sum_{i,j} W_ij s_i s_j  +  sum_i theta_i s_i
```

where `theta_i` are thresholds (often zero). With zero thresholds and symmetric
W with zero diagonal, E is well-defined.

**Continuous-time Hopfield network.** Replace binary states with real-valued
activations `u_i(t)`, `V_i = g(u_i)` where g is a sigmoidal. The energy is

```
E = -(1/2) sum_{i,j} T_ij V_i V_j + sum_i (1/R_i) int_0^{V_i} g^{-1}(s) ds
  - sum_i I_i V_i
```

where `T_ij` = connection conductances, `R_i` = resistances, `I_i` = input
currents. The Lyapunov argument carries over when T is symmetric, `T_ii = 0`.

**Computable objects for a sim.** On a finite carrier of N neurons:
- energy landscape: `E(s)` for all `2^N` states (feasible for N <= ~25);
- local minima: enumerate by gradient descent from all initial states;
- basin of each minimum: set of states that converge to it under the chosen
  update rule;
- crosstalk noise term: `(1/N) sum_{nu != mu} (xi^nu · s)(xi_i^nu)`, which
  is the interference between stored patterns during retrieval.

---

## 2. The 0.138N Capacity Result and Hypotheses

**The number.** With the Hebbian rule and P random, unbiased (`<xi_i> = 0`),
i.i.d. patterns, as N grows with P/N -> alpha:

- For alpha < 0.138: nearly all stored patterns are stable fixed points with
  high probability (the system recovers correctly from small initial
  corruptions).
- At alpha = 0.138 (approximately 0.1380...): the memory capacity threshold.
  Above this, retrieval quality drops sharply and a first-order phase
  transition occurs in the fraction of correctly recalled bits.

The rigorous derivation is due to Amit, Gutfreund, and Sompolinsky (1985,
1987) [recall] via the replica method from statistical physics, and the result
is corroborated by independent signal-to-noise ratio calculations.

**Hypotheses — where the result holds:**
1. Patterns are random, i.i.d., unbiased (`<xi_i> = 0`). Biased patterns
   (e.g., sparse or heavily correlated) shift the capacity.
2. N is large (thermodynamic limit). For small N the result is a guideline,
   not a precise threshold. A network with N=12 (as in `basin3_julia.jl`)
   is deep in the small-N regime; the 0.138N bound gives P_max ~ 1.6, so
   storing even 2 patterns is operating near or over the finite-N analog of
   the bound.
3. Synchronous or asynchronous update rule with Hebbian weights. Other learning
   rules (e.g., pseudoinverse/perceptron rule) change the capacity; the
   pseudoinverse rule achieves P/N -> 1 for orthogonal patterns [recall].
4. Binary (`{-1,+1}`) or graded neurons with the energy above. Quaternion-
   valued neurons or complex weights alter the analysis.
5. Zero diagonal (W_ii = 0). If self-coupling is permitted, additional fixed
   points appear.
6. Symmetric weights. Without symmetry, the Lyapunov argument fails and
   cycles can appear.

**Practical cap for correct retrieval (not just fixed-point stability).** The
~0.138N result is for fixed-point stability of stored patterns. For good
basin-of-attraction retrieval (large basins, high per-bit accuracy from a
30%-corrupted start), the empirical cap is lower, roughly 0.05N to 0.10N
[recall]. The sharper threshold for "large error-correcting basins" is a
separate finite-N question.

**What 0.138N does NOT guarantee.** It does not say anything about:
- the size or shape of the basins (only existence of fixed points);
- the number or density of spurious attractors;
- retrieval from a corrupted start outside the basin;
- any quantum, complex, or quaternion generalization.

---

## 3. Spurious Attractor Structure

**Three attractor families in classical Hopfield networks.**

*(a) Stored patterns and their negatives.* The P stored patterns `xi^mu` and
their bit-flips `-xi^mu` are each fixed points of the synchronous update under
the Hebbian rule. These are the "intended" attractors. Their basins are the
semantically useful part of the network.

*(b) Mixture states.* For any odd subset of stored patterns
`{xi^{mu_1}, ..., xi^{mu_{2k+1}}}`, the element-wise majority vote

```
xi^mix_i = sgn( xi_i^{mu_1} + ... + xi_i^{mu_{2k+1}} )
```

is a spurious fixed point. The three-pattern mixture (`xi^{mu_1} + xi^{mu_2}
+ xi^{mu_3}` majority) is the smallest non-trivial case. These states are
admixtures of stored patterns and have no semantic content; they are fixed
points by symmetry of the energy landscape under bit-flip of the Hebbian sum.
[recall, standard result]

*(c) Spin-glass states.* For alpha close to or above the capacity threshold,
many energy minima emerge that are not near any stored pattern. These are
called "spin-glass" states or "glassy" states by analogy with disordered
magnetic systems. Their number grows rapidly with N; the spin-glass phase
dominates above the capacity. They fragment the landscape into many shallow
minima with no interpretable content.

**Why the absence of spurious attractors on a small carrier is suspicious.**
On a small carrier (N=4, 8, or 12), only a tiny number of states exist
(`2^4 = 16`, `2^8 = 256`, `2^12 = 4096`). Any decent implementation of the
Hebbian rule with P >= 2 stored patterns will produce mixture and near-mixture
states as additional energy minima. If a finite Hopfield sim with P >= 3
stored patterns and N ~ 10 reports zero spurious attractors:
- Either the search was limited (only started from the stored patterns, not
  from corrupted or random seeds);
- Or the weights were not Hebbian but a specially constructed rule that avoids
  spurious states;
- Or the attractor predicate is too coarse (e.g., "close to a stored pattern"
  rather than "is an energy minimum");
- Or the result is fabricated.

A sim with N=4 and P=3 stored chiral quaternion-family patterns that reports
a clean partition with exactly 3 basins and no spurious attractors should be
treated as having an insufficiently sensitive spurious-attractor probe.

**Density of spurious attractors at capacity.** The number of spurious local
minima grows exponentially with N at the spin-glass transition. Below capacity,
mixture states make up the bulk of spurious attractors; above capacity, glassy
states dominate. In neither regime does a well-implemented sim produce zero
spurious attractors for P >= 2 and N >= 10. [recall]

---

## 4. Energy and Lyapunov Conditions: When Monotonicity Holds

**Asynchronous update, symmetric weights.** Under asynchronous single-neuron
update (one neuron flips according to majority rule), the Hopfield energy E(s)
is non-increasing. Proof: when neuron i updates from `s_i` to `s_i'`:

```
delta_E = E(s') - E(s) = -(s_i' - s_i) * (sum_j W_ij s_j)
```

Since `s_i' = sgn(sum_j W_ij s_j)`, the update decreases E or leaves it
unchanged. This holds if and only if W is symmetric and W_ii = 0.

**The symmetry requirement is strict.** If W is asymmetric, delta_E has no
definite sign. The system can cycle. No Lyapunov argument is available in
general for asymmetric weights; cycles of period 2 (or longer) can occur.

**Synchronous update caveat: 2-cycles.** Under synchronous update (all
neurons flip simultaneously), the energy is NOT guaranteed to be
monotone. The system can enter limit cycles of period 2: a state s and its
successor s' can form a two-cycle `s -> s' -> s -> ...`. These are not fixed
points and do not correspond to stored patterns. The Lyapunov guarantee for
synchronous Hopfield is a weaker object: E(s(t+2)) <= E(s(t)), i.e., energy
decreases over pairs of steps, not over individual steps. Cycles of period > 2
can also occur for synchronous update with particular weight matrices. [recall]

This is a load-bearing caveat for any Codex-Ratchet basin sim using synchronous
update: the monotone energy must be measured over two-step pairs, not single
steps, to remain honest. A sim that checks `E(t+1) < E(t)` under synchronous
update and calls it Lyapunov-certified is overclaiming.

**Graded/continuous-time case.** For the continuous-time ODE with symmetric
T_ij, `dE/dt <= 0` follows from the chain rule and the monotone sigmoidal
activation [recall]. Limit cycles are precluded for strictly monotone g and
symmetric T. This is the regime where the Hopfield 1984 tank circuit paper
proves convergence.

**Bipartite and constrained symmetric cases.** When the weight matrix has
block-off-diagonal structure (bipartite graph), additional monotone energy
functionals exist and the system can be mapped to a min-cut problem. This is
the basis for the Hopfield-Tank TSP solver variant.

**What the energy function does NOT certify:**
- Basin size or shape;
- Distance from the stored-pattern to the energy minimum;
- Absence of spurious attractors (the energy still decreases into them);
- Retrieval quality from corrupted starts (only that the update terminates).

---

## 5. Negatives: What the Formalism Cannot Do

**No. 1: Capacity bound does not transfer to non-i.i.d. or non-binary patterns.**
The 0.138N result is proved for i.i.d. uniform `{-1,+1}` patterns. Quaternion
patterns, complex-valued patterns, sparse patterns, or structured patterns
require separate analysis. The bound can be much lower (correlated patterns
saturate capacity quickly) or higher (orthogonal patterns under the
pseudoinverse rule). No direct analogue of 0.138N exists for arbitrary
quaternion-Hopfield constructions without a separate derivation.

**No. 2: Lyapunov guarantee fails for asymmetric or complex weights.**
If the Hermitian condition `W = W^dagger` is used for complex/quaternion
weights but the product rule is noncommutative (as in the chiral quaternion
Hopfield of `basin3_julia.jl`), the energy proof requires that the Hebbian
update produces a self-adjoint weight under the chosen product structure.
For quaternion weights assembled as `W_ij = sum_mu q_L_i^mu * conj(q_L_j^mu)`
with Hamilton product, self-adjointness under Hamilton product is not the same
as standard Hermitian conjugation; the energy monotonicity argument needs
re-verification for the specific update rule.

**No. 3: Finite size destroys thermodynamic guarantees.**
The replica method and phase-transition language (memory phase, spin-glass
phase, ferromagnetic phase) apply in the thermodynamic limit N -> infinity.
For N=4 or N=12, the "0.138N" is a sub-1 or sub-2 number, meaning the
theoretical P_max is less than 1 or 2 patterns. Operating at P=3 or P=8
patterns on N=12 neurons is firmly in the overloaded regime from the
thermodynamic perspective; the stored patterns are not guaranteed to be
stable fixed points at all. The network may still function as a multistable
device, but it is not operating in the regime where the classical capacity
theorem applies.

**No. 4: Energy minima do not equal stored memories.**
The Hebbian construction guarantees that stored patterns are energy minima
(for low enough P/N). It does not guarantee that every energy minimum is a
stored pattern, nor that the stored-pattern minima are the deepest minima.
Spurious attractors can be deeper (lower energy) than the stored-pattern
attractors in an overloaded network.

**No. 5: Basin volume cannot be inferred from fixed-point stability.**
A pattern being a stable fixed point (eigenvalue of the update-linearization
negative) says nothing about the basin radius or volume. Stability is a local
property; basins can be arbitrarily small, irregular, or fractal. The classic
Hopfield analysis does not bound basin size.

**No. 6: Synchronous update can produce oscillations that look like retrieval.**
A 2-cycle between two states close to a stored pattern is not retrieval.
Without checking that the trajectory terminates at a fixed point (not a
cycle), a sim that reports "converged" based on proximity to a stored pattern
is overclaiming.

**No. 7: The Lyapunov argument does not extend to CPTP quantum dynamics in
general.** A quantum channel `E(rho)` does not generally decrease any fixed
scalar functional analogous to the classical energy. For specific channel
families (e.g., projective measurements, depolarizing noise toward a target
state) specific functionals do decrease, but this must be proved case-by-case.
The classical Lyapunov proof does not transfer automatically to the quantum
setting.

---

## 6. Quantum Hopfield Proposals

### 6.1 What "quantum Hopfield" has meant in the literature

Several distinct proposals use the name; they are not equivalent.

**(a) Quantum associative memory (Ventura-Martinez, 1999-2000).** [recall]
Replaces classical bit patterns with quantum superpositions. The key idea:
store P patterns as superpositions in a Hilbert space of dimension 2^N (the
full quantum register). The capacity claim: a quantum associative memory can
store exponentially many patterns (P ~ 2^N) in the superposition, versus
the ~0.138N classical bound. The catch: retrieval requires phase-sensitive
operations and the stored superposition state. Noisy or partial queries do not
generally collapse to the intended pattern; they collapse to a mixture. The
exponential capacity is real but the retrieval model differs fundamentally from
classical pattern completion.

**(b) Hopfield network with quantum tunneling (Serafini et al., Rotondo et al.).** [recall]
Replaces the thermal annealing of classical Hopfield with quantum fluctuations
(transverse fields, tunneling terms). The energy landscape is the same Hebbian
landscape; quantum tunneling helps escape shallow spurious attractors and reach
deeper minima. Theoretical claim: quantum effects can improve retrieval for
some parameter regimes. Status: established in simplified models (e.g.,
transverse-field Ising at low temperature), but demonstrations of practical
advantage over simulated annealing are limited. The capacity bound in the
quantum-tunneling variant remains close to the classical one when temperature
is matched; the advantage is in escape from metastable states, not in raising
capacity.

**(c) Quantum dot / Ising model implementations.** Physical implementations
where spins are qubits and coupling Hamiltonians realize the Hopfield energy as
the system Hamiltonian. Thermal/dissipative evolution drives the system to the
ground state. Genuine implementations at small scale (N ~ 10-20 spins) are
physically realized; large-scale implementations face decoherence. The energy
in this framework is the quantum Hamiltonian H; basins correspond to low-energy
subspaces.

**(d) Modern quantum Hopfield networks (Barra et al., Ramsauer et al., Krotov-
Hopfield).** The dense associative memory / modern Hopfield network (Krotov-
Hopfield 2016, Ramsauer et al. 2020 [recall]) is a classical but high-capacity
variant using polynomial or exponential interaction terms. The "Hopfield
Networks is All You Need" paper (Ramsauer 2020) shows the continuous-time
modern Hopfield update rule is equivalent to the attention mechanism in
transformers. Capacity scales as 2^(alpha N) rather than 0.138N when
interaction order increases. This is a classical, not quantum, result; it
is sometimes confused with quantum Hopfield but has no quantum operations.
It IS relevant because: (i) the high-capacity regime suppresses spurious
attractors relative to the standard Hebbian rule; (ii) the equivalence to
softmax attention provides a formal bridge between associative memory and
information-theoretic channel operations.

**(e) Quantum Hopfield as a CPTP channel.** This is the framework most directly
relevant to Codex-Ratchet's surface doctrine. A retrieval step is a CPTP
map `E_theta: rho -> rho'` parameterized by a target state `|xi><xi|` (stored
pattern) and a mixing/damping parameter. The simplest family:

```
E_theta(rho) = (1 - alpha) * rho + alpha * |xi><xi|
```

This is a convex mixture channel. It is CPTP (trivially, as a convex
combination of identity and a preparation channel). The fixed point is
|xi><xi|. The "energy" analog is the fidelity `F(rho, |xi><xi|) = <xi|rho|xi>`,
which is non-decreasing under E_theta. The spurious attractors analog: if
multiple target patterns are superimposed in the channel (mixed target), the
fixed point is a mixture density matrix, not a pure stored pattern.

The Lyapunov statement for the CPTP channel framework:

```
F(E_theta(rho), sigma_target) >= F(rho, sigma_target)
```

holds for the specific damping-to-target channel. It does NOT hold for general
CPTP channels. The contractivity of the trace distance under CPTP maps gives
`||E(rho) - E(sigma)||_1 <= ||rho - sigma||_1`, but this does not by itself
bound the energy/fidelity in a Hopfield-like direction.

### 6.2 What is genuinely established vs speculative

**Genuinely established:**
- CPTP channels provide a well-defined quantum generalization of update steps.
- Specific families (preparation mixtures, amplitude damping) have monotone
  fidelity functionals.
- Quantum tunneling can improve escape from shallow spurious attractors in
  the transverse-field Ising model.
- Modern classical Hopfield (Ramsauer 2020) capacity scaling and transformer
  equivalence are mathematically established.
- Spurious attractors (mixture states) exist in quantum associative memory
  just as in the classical case; in fact the full-superposition storage
  approach has a superposition-state spurious attractor problem that is harder
  to analyze than the classical case. [recall]

**Speculative or unproven:**
- That exponential quantum capacity (via superposition storage) is
  operationally useful for pattern completion under realistic decoherence.
- That a finite spinor-network Hopfield model has better capacity than 0.138N
  without a proof for the specific carrier and rule.
- That the CPTP-channel Lyapunov property generalizes beyond simple mixing
  channels to entangled-pattern or noncommutative-weight families.
- That eliminating spurious attractors on a small finite carrier (as in
  `spinor_network_surface_v1`) constitutes a meaningful capacity improvement
  rather than an artifact of the small N / small P regime.
- Any connection between quantum Hopfield retrieval and the physical Hopf
  fibration structure used in this repo's spinor-network carriers.

---

## 7. Computable Finite Checks

These are procedures a finite sim can actually run (ceiling: numerical evidence
only, not thermodynamic-limit theorems).

**Check 1: weight matrix symmetry and diagonal.**
Assert `|W - W^T|_max < eps` and `|diag(W)|_max < eps`. For quaternion/complex
W, check `|W - W^dagger|_max < eps`. This is necessary (not sufficient) for
the Lyapunov argument.

**Check 2: Lyapunov monotonicity under asynchronous update.**
For a sample of initial states, run asynchronous update and verify
`E(s(t+1)) <= E(s(t)) + eps` at each step. Report any violation; even one
is informative (it signals symmetry-breaking or implementation error).
For synchronous update, check `E(s(t+2)) <= E(s(t))` instead.

**Check 3: Basin enumeration by exhaustive seed sweep.**
For N <= 20, start from all 2^N states (or a dense random grid for larger N)
and record terminal fixed points. Count the number of distinct attractors.
Expected: at least the P stored patterns plus several spurious states for
P >= 2. Report count(spurious) explicitly; a zero count for P >= 2 demands
explanation.

**Check 4: Spurious-attractor identification.**
Label each terminal state: "stored pattern match" (Hamming distance d(s, xi^mu)
< threshold for some mu), "bit-flip match" (d(s, -xi^mu) < threshold), "mixture
state" (majority-vote test against all odd-sized subsets), or "unknown/glassy."
For N <= 20, the mixture-state check is computable. Report distribution.

**Check 5: Basin size estimation.**
For each attractor A_k, count the number of initial states that converge to it
(basin volume under the uniform measure on {-1,+1}^N). The stored patterns
should have the largest basins for P well below capacity. Report basin size
distribution; near-capacity operation makes stored-pattern basins shrink and
spurious-attractor basins grow.

**Check 6: Pattern stability sanity test.**
For each stored pattern xi^mu, verify that xi^mu is itself a fixed point:
`update(xi^mu) == xi^mu`. For asynchronous update, test one-step stability
for each neuron individually. If any stored pattern is not a fixed point, the
implementation or parameter choice is wrong.

**Check 7: Corrupted-start retrieval accuracy.**
For each stored pattern, generate a corrupted version (flip 10-30% of bits),
run update until convergence, measure Hamming distance to the nearest stored
pattern. Report the overlap `m^mu = (1/N) sum_i xi_i^mu s_i`. For P well below
0.138N, expect m close to 1. For P above 0.138N, expect m to degrade.

**Check 8: SMT formalization of finite properties.**
For N <= ~15, the following can be stated as finite Boolean queries:
- "there exists a state s such that E(update(s)) > E(s) + eps" (Lyapunov
  violation certificate);
- "the stored pattern xi^1 is a fixed point of the update rule";
- "the state s* is not a fixed point but the transition graph has no outgoing
  edge from s*" (trapping without being a fixed point, for stochastic variants).
Z3/CVC5 can check these for small N over bit-vector or integer representations.

**Check 9: For quantum/CPTP variant.**
Given a channel E_theta defined by Kraus operators {K_i}:
- Verify `sum_i K_i^dagger K_i = I` (trace preservation) to numerical tolerance;
- Verify Choi matrix `C = sum_i |K_i><K_i|` is positive semidefinite;
- Verify non-increase of fidelity to target: `F(E_theta(rho), sigma_target)`
  vs `F(rho, sigma_target)` on a sample of rho;
- Verify spurious-state existence: start from an equal mixture of two stored
  patterns `rho = (|xi^1><xi^1| + |xi^2><xi^2|) / 2` and check whether the
  channel drives it to xi^1, xi^2, or a stable mixture. The stable mixture
  is the quantum analog of a mixture spurious attractor.

---

## 8. Repo Relevance

Read-first docs consulted:
- `system_v6/receipts/owner_doctrine_spinor_network_surface_20260611.md`
- `system_v6/receipts/spinor_network_surface_estate_20260611.md`
- `system_v6/sims/spinor_network_surface_v1/audit_verdict.md`
- `system_v5/julia_carrier/basin3_julia.jl` (first 80 lines)
- `wiki/codex-ratchet-research/basins/standard-math.md`
- `wiki/codex-ratchet-research/basins/negatives.md`
- `wiki/codex-ratchet-research/basins/alternatives.md`

### How this note bears on specific packets

**`spinor_network_surface_v1` (and v0, v2).**

The owner doctrine (`owner_doctrine_spinor_network_surface_20260611.md:16-21`)
requires: "finite spinor set, Hermitian coupling matrix, dissipative retrieval
dynamics, stored patterns, energy/entropy landscape, basins, spurious
attractors." The standard-math content above names exactly what that list
requires before each element can be claimed.

The v1 audit verdict (`audit_verdict.md:90-91`) reports 6 spurious pair-mixture
attractors over 6/6 equal pair mixtures, and notes the search is exhaustive
only for that declared seed family. The standard-math section on mixture states
above explains why pair mixtures are the right first target: for P stored
patterns, the odd-subset majority states are the dominant spurious family in
the Hebbian model. However, the pair-mixture equal-mix is only the P=2 odd
subset case (the trivial mixture). For P=3 or more patterns, three-pattern
mixture states and glassy states should also appear. The v1 search is honest
within its scope but should be enlarged in v2 to cover three-pattern mixtures
and random initial states beyond the stored/corrupt family.

The Lyapunov check in v1 (`audit_verdict.md:80-81`) uses
`V(rho) = 1 - max terminal fidelity`, verifying that it increases for the
non-Hermitian control. This is honest. The standard-math content above
clarifies that this is a fidelity-to-target functional, not the full Hopfield
energy, and that monotonicity holds only for specific channel families. V2
should: (a) state which channel family is being used, (b) verify the Kraus
completeness condition (which the v1 audit found was not persisted in the
results ledger), and (c) test the non-Hermitian control by checking that V
INCREASES rather than merely fluctuates.

**`basin3_julia.jl` (N=12 quaternion Hopfield).**

This packet operates at M in {2,3,4,8} stored quaternion-spinor patterns on
N=12 neurons. From section 3 above: at M=2 with N=12, P/N = 0.17, which
already exceeds the classical 0.138N capacity for i.i.d. binary patterns. At
M=8 with N=12, P/N = 0.67, which is deep in the spin-glass/overloaded regime.
The claim ceiling (`exploration_probe`) is appropriate. The L/R chiral
quaternion weight structure does not have a known capacity bound; operating
at these P/N ratios means mixture states and glassy states are expected. The
fact that `basin3` reports a "candidate_distinct" measured result (not
hardcoded) is honest. Any future promotion from this carrier needs a separate
capacity argument for the quaternion case or must operate at P/N << 0.138
with an appropriate quaternion-weight analysis.

**`npc2_connection_geometry_julia.jl`.**

Uses Hopfield bond matrix `W_ij = sum_mu xi_i^mu * conj(xi_j^mu)` (standard
Hebbian outer product in complex/Hopf coordinates). The failing `n01_noncommutation`
row (`npc2_connection_geometry_julia_results.json`) is consistent with the
standard-math fact that the classical Hebbian rule does not produce a
noncommutative coupling; noncommutativity must come from the per-site
carrier structure (quaternion or spinor product), not from the weight matrix
itself.

**The 0.138N result as a guard on future surface claims.**

The owner doctrine calls for "finite spinor set + Hermitian coupling +
dissipative retrieval" as the native basin object. Before any claim of capacity
enhancement or reduced spurious-attractor density from the spinor/chiral
structure, a concrete counter to the following must be in the packet:

1. Measure P/N for the carrier and state whether it is above or below the
   classical 0.138N threshold (even as a finite-N estimate).
2. Run a full exhaustive fixed-point enumeration over all initial states
   (feasible for N=4 surface), classify each attractor as stored, bit-flip,
   mixture, or unknown.
3. Check Lyapunov monotonicity under the specific update rule used (not just
   assumed from the classical symmetric case).
4. For the CPTP-channel retrieval framework, verify Kraus completeness and
   Choi positivity and persist the ledger.

Until these checks are in the packet, the basin claim rests on the small seed
set, not on a comprehensive attractor structure.

**Quantum Hopfield: no repo packet claims the quantum capacity enhancement.**

As of the estate sweep (`spinor_network_surface_estate_20260611.md:gap 1-4`),
no completed strict quantum-Hopfield carrier was found. The quantum Hopfield
capacity claim (exponential in N via superposition storage) is NOT claimed in
any current packet and should remain fenced until a packet demonstrates it on
a specific carrier with the retrieval procedure described in section 6.1(a)
above. The relevant caution: exponential capacity requires coherent superposition
storage and retrieval, not just a CPTP damping channel toward a classical
pattern state.

---

## Source Anchors (recall-based unless otherwise noted)

- J. J. Hopfield, "Neural networks and physical systems with emergent collective
  computational abilities," PNAS 79(8):2554-2558, 1982. [recall]
- J. J. Hopfield, "Neurons with graded response have collective computational
  properties like those of two-state neurons," PNAS 81(10):3088-3092, 1984.
  [recall]
- D. J. Amit, H. Gutfreund, H. Sompolinsky, "Storing Infinite Numbers of
  Patterns in a Spin-Glass Model of Neural Networks," Physical Review Letters
  55(14):1530-1533, 1985. [recall]
- D. J. Amit, H. Gutfreund, H. Sompolinsky, "Statistical mechanics of neural
  networks near saturation," Annals of Physics 173(1):30-67, 1987. [recall]
- D. Ventura, T. Martinez, "Quantum associative memory," Information Sciences
  124(1-4):273-296, 2000. [recall]
- D. Krotov, J. J. Hopfield, "Dense Associative Memory for Pattern Recognition,"
  NeurIPS 2016. [recall]
- H. Ramsauer et al., "Hopfield Networks is All You Need," ICLR 2021. [recall]
- A. Barra et al., "Equilibrium statistical mechanics of bipartite spin systems,"
  J. Phys. A: Math. Theor. 44(24):245002, 2011. [recall]
- P. Rotondo et al., "Counting the learnable functions of geometrically
  structured data," Physical Review Research 2(2):023139, 2020. [recall]
  (quantum-fluctuation-enhanced retrieval)
- Scholarpedia, "Hopfield network," http://www.scholarpedia.org/article/Hopfield_network.
  [recall]
