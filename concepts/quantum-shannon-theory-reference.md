---
title: Quantum Shannon Theory Reference
created: 2026-04-09
updated: 2026-05-21
type: concept
tags: [reference, quantum, formal, mathematics, entropy]
sources:
  - https://arxiv.org/abs/quant-ph/0209124v3
  - https://arxiv.org/abs/1511.06071v2
  - https://arxiv.org/abs/1308.4283v3
framing: late_stage_reference_snapshot
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Quantum Shannon Theory

Quantum Shannon theory generalizes classical information theory to quantum systems. Where Shannon theory studies bits through noisy channels, quantum Shannon theory studies qubits through quantum channels — completely positive trace-preserving (CPTP) maps. Key quantities: coherent information, quantum capacity, entanglement-assisted capacity, and the structure of quantum codes.

Authority boundary: this page supplies late-stage channel/reference language. It does not promote local entropy values, bipartite cut witnesses, Axis 0 gradients, or Phi0/seam claims into channel capacity or bridge status.

## Core Quantities

### Von Neumann Entropy

S(ρ) = -Tr[ρ log ρ]

The quantum analog of Shannon entropy. For a pure state |ψ⟩, S = 0. For a maximally mixed state in d dimensions, S = log d. Satisfies subadditivity: S(AB) ≤ S(A) + S(B), with equality iff ρ_AB = ρ_A ⊗ ρ_B.

### Coherent Information

I_c(A⟩B) = S(B) - S(AB)

Measures how much quantum information flows from A to B through a channel. Unlike mutual information (which is symmetric), coherent information is asymmetric — it tracks the quantum capacity direction. Positive coherent information is a useful witness for unassisted quantum transmission, not a complete iff criterion for every channel or regularized-capacity setting.

### Quantum Mutual Information

I(A:B) = S(A) + S(B) - S(AB)

Total correlations (classical + quantum) between A and B. I(A:B) = 0 iff ρ_AB = ρ_A ⊗ ρ_B. Upper bounded by 2·min{S(A), S(B)}.

### Quantum Discord

D(A:B) = I(A:B) - J(A:B)

where J(A:B) is the classical correlation (maximum over measurements on B). Discord = 0 iff all correlations are classical. Discord > 0 means the system has quantum correlations even when entanglement = 0.

## Quantum Channel Capacity

### Holevo-Schumacher-Westmoreland Theorem

The classical capacity of a quantum channel N is:

C(N) = lim_{n→∞} (1/n) max_{ρ^{(n)}} [S(N(ρ^{(n)})) - Σ_i p_i S(N(ρ_i^{(n)}))]

where the max is over ensembles {p_i, ρ_i}. This is the regularized Holevo quantity.

### Quantum Capacity (LSD Theorem)

The quantum capacity of channel N is:

Q(N) = lim_{n→∞} (1/n) max_ρ I_c(ρ, N^{⊗n})

The regularization is necessary because coherent information is not generally additive; superadditivity and superactivation phenomena make single-letter capacity claims unsafe.

### Entanglement-Assisted Capacity

C_E(N) = max_ρ I(ρ, N)

No regularization needed — mutual information is additive. The quantum and classical capacities with entanglement assistance are directly computable.

## Cut States and Entropy Kernels

For a bipartite system AB with a cut between A and B:

### Reduced States

ρ_A = Tr_B[ρ_AB] — partial trace over B gives the marginal state of A. This is the quantum analog of marginal probability distributions.

### Entropy Kernel

The entropy kernel K(ρ_AB) is the collection of entropy quantities (S(A), S(B), S(AB), I(A:B), I_c(A⟩B), I_c(B⟩A)) considered as a function of the bipartite state. Different states with the same kernel are "entropically equivalent" — distinguishable only by higher-order information.

### Strong Subadditivity

S(ABC) + S(B) ≤ S(AB) + S(BC)

The most important inequality in quantum information. Equivalent to the monotonicity of relative entropy under CPTP maps. Constrains the feasible region of entropy vectors.

## Relevance to This System

### Connection to Axis 0

The cited system language defines Axis 0 as ∇_η I_c(ρ(η)) — the gradient field of coherent information across shell parameters. This makes Axis 0 a candidate vector on a capacity-related surface, not a scalar summary. The capacity theorem says that Q(N) is controlled by coherent information under regularization, so Axis 0 is best read as a directional bridge candidate for channel-preserving structure rather than as a standalone doctrine object.

The repo's own build order matters here: Axis 0 is a late bridge claim, not a primitive. Quantum Shannon language is most useful after local state/operator/channel objects are already admitted.

### Connection to Phi0

The Phi0 seam quantity concerns the boundary between quantum-preserving and classically-degraded transmission across a cut. For the specified state/cut, the sign of coherent information is a diagnostic for unassisted quantum transmission; it is not a complete channel-capacity verdict. When I_c <= 0, the channel may still carry classical correlation or assisted resources. That makes coherent information a sharper seam-side diagnostic than generic entropy alone, but still a receipt-bound witness.

### Connection to the constraint cascade

Quantum Shannon theory gives a disciplined CS-native vocabulary for why some families are retained and others excluded under composition:
- channel claims should respect CPTP composability
- cut-based quantities should survive partial trace and data processing in the expected direction
- directionality matters because coherent information is asymmetric
- regularization/additivity pathologies warn against collapsing local witnesses into global capacity claims too early

So this page is useful not because it proves the surviving families are final, but because it supplies the correct language for admissible channel-side bookkeeping once local objects exist.

### Connection to shell-local -> coupling -> bridge order

The shell-local program says: build local legos first, then pairwise coupling, then coexistence, then topology variants, then emergence, then bridge claims. Quantum Shannon quantities mostly live at the coupling/bridge side of that ladder:
- reduced states require a nontrivial cut
- coherent information requires directed bipartite bookkeeping
- capacities summarize repeated channel use, not merely local state existence

So this reference is strongest as a late-stage interpretation/control page, not as a justification for skipping earlier geometry and channel-admission work.

### Connection to controller semantics

There is also a direct CS reading. The controller has to distinguish:
- local object existence
- runnable channel packet
- rerun-backed cut behavior
- stronger bridge/capacity interpretations

Quantum Shannon theory helps keep those levels separate. A local entropy value is not yet a channel-capacity claim. A single bipartite cut witness is not yet a global rate theorem. A suggestive coherent-information gradient is not yet canonical Axis 0. This is exactly the kind of status separation the controller contract is trying to preserve.

### Connection to discord

Standard QIT fact: discord can be nonzero for separable states. If a repo result claims this in a specific cut or shell, cite the result path separately. Discord tracks nonclassical correlation structure in the entropy kernel even when entanglement measures vanish, which is useful for distinguishing "classical-looking" from genuinely classical cut behavior.

## Key Results

1. **No-cloning**: unknown quantum states cannot be copied. Capacity comparisons require the relevant definitions and assistance regime; do not use no-cloning alone as a proof of a universal capacity inequality.
2. **Additivity failures**: Hastings disproved additivity of minimum output entropy/Holevo capacity; quantum-capacity superactivation is a separate phenomenon, associated with results such as Smith-Yard. These pathologies make capacity computation hard.
3. **Quantum data processing**: S(ρ||σ) is monotone under CPTP maps. This is the quantum generalization of data processing inequality.
4. **Holographic entropy adjacency**: Ryu-Takayanagi and entanglement-wedge language are adjacent support for entropy/geometry analogies, not core quantum Shannon capacity theorems on this page.

## Open Questions

- Does the system's coherent-information gradient candidate (Axis 0) acquire a Berry-like holonomy when shell parameters trace a closed loop?
- Is quantum-capacity additivity failure related in any principled way to substrate-sensitive or topology-sensitive behavior in the current sims?
- Can the entropy kernel of the surviving families be characterized as a constrained polytope or cone, and what boundaries are actually load-bearing rather than decorative summaries?
- Which quantities in the current repo are genuinely channel-side objects versus local entropy summaries being over-read as channel objects?
- What is the minimal shell-local and pairwise evidence required before any Axis 0 or Phi0 claim should be promoted beyond `runs` or `passes local rerun`?

## 2026-04-10 arXiv source additions

These additions are support surfaces for the quantum Shannon lane, not proof that the repo's current capacity language is canonical.

### quant-ph/0209124v3 — Simple construction of quantum universal variable-length source coding
- Gives a clean quantum source-coding construction with vanishing error and coding-rate overflow probability.
- Useful for bounded compression, variable-length coding, and entropy-rate routing.
- Best fit pages: [[compression-to-density-matrix-map]], [[quantum-information-measures]], [[quantum-shannon-theory-reference]].

### 1511.06071v2 — Channel Simulation and Coded Source Compression
- Connects coded source compression with channel simulation in the quantum setting.
- Useful where the wiki needs a bridge between compression and channel-side resource accounting.
- Best fit pages: [[quantum-shannon-theory-reference]], [[compression-to-density-matrix-map]], [[cptp-maps-and-channels]].

### 1308.4283v3 — Entanglement-assisted zero-error source-channel coding
- Studies zero-error source-channel coding with entanglement assistance.
- Useful for exact-coding / zero-error boundaries and entanglement-assisted routing.
- Best fit pages: [[quantum-shannon-theory-reference]], [[entanglement-theory]], [[quantum-information-measures]].

## Related Pages

- [[current-research-overlays]] — research-routing hub for this late-stage channel lane
- [[quantum-information-measures]] — entropy, mutual information, Holevo bound
- [[entanglement-theory]] — separability, concurrence, negativity
- [[cptp-maps-and-channels]] — complete positivity, Kraus form, Lindblad dynamics
- [[constraint-on-distinguishability]] — trace distance, fidelity, data processing
- [[shell-local-to-coupled-program]] — local to bridge build order
- [[llm-controller-contract]] — guarded promotion and truth labels
- [[controller-state-transition-model]] — bounded evidence progression across surfaces
- [[codex-ratchet-cs-bounded-system-framing]] — controller-native queue/truth framing
- [[pytorch-ratchet-build-plan]] — Axis 0 formal math
- [[entropy-sweep-protocol]] — which entropy families are admissible
- [[distance-metrics-state-space]] — Bures distance, fidelity, QFI
- [[topic-map]] — broader navigation spine

## Sources

- Wilde. "Quantum Information Theory." Cambridge University Press, 2nd ed., 2017.
- Watrous. "The Theory of Quantum Information." Cambridge University Press, 2018.
- Preskill. "Quantum Information and Computation." Caltech lecture notes.
- Hayden, Winter. "Counterexamples to the Maximal p-Norm Multiplicativity Conjecture." Comm. Math. Phys. 284, 263 (2008).
