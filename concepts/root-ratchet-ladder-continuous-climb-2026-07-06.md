# The root ratchet ladder: one continuous climb from static field to the terrains (2026-07-06 synthesis)

Provenance: consolidates the ratchet-mechanics work of the 2026-07-06 session into one climb. Ceiling: all sims cited are `scratch_diagnostic, promotion_allowed=false` mechanism illustrations under the entropic-monism fence -- measured, not canon, not derivations. Companion to [[root-ratchet-mechanics-and-rolling-entangled-dice-2026-07-06]] (the root-vs-downstream doctrine) and [[entangled-dice-universe-creation-2026-07-06]] (the cosmology statement).

## What this page adds

The root ratchet is no longer a set of separate claims -- it is a single climbing process with a chain of forced teeth, each opening the demand the next one closes. This page states that ladder once, rung by rung, with the receipt for each. Nothing here is asserted; each rung says what was measured and what remains owed.

## The one mechanism (the same rules at every rung)

```text
DEMAND      a pair the room asserts distinguishable (trace distance > THETA=0.25)
            that the acquired bases do NOT resolve -- a=a iff a~b speaking:
            two things the room says are different the carrier cannot yet tell apart
MSS         admit ONLY the weakest structure that closes >=1 open demand;
            larger leaps inadmissible; the pawl holds when nothing is forced
PAWL LOCK   each closed demand records its EXACT witness (provenance) in an
            append-only ledger; a re-encounter must reuse it -- no lateral swap
DRIVE       the entropy gradient (available minus resolved distinguishability),
            intrinsic to a growing possibility space; memory-bearing so it ratchets
MEASURE     quantum distinguishability only (trace distance / Helstrom).
            NEVER bits, log2, vectors, or counting of microstates
```

Measure is separated from verdict throughout (Lev mesh-package discipline): instruments emit numbers, a separate policy eval decides on the controls flipping. A gate the instrument does not contain cannot be tuned -- the structural fix for the four gate-tuning audits earlier in the project.

## The ladder, rung by rung

### Rung 0 -- cosmogenesis: the first tooth (MSS in a static field)

`cosmogenesis_ratchet_first_tooth_sim.py`. In a static pre-ratchet possibility field there is no carried difference between frames (measured: static field carries ~0; a persistent carrier carries ~0.94) -- time IS a carried difference. MSS forces the weakest structure that keeps a difference alive: a norm-preserving (division) spinor carrier (a lossy map annihilates the difference to ~1e-9; the norm-preserving one persists at 1.0). Its expansion is entangled (concurrence 0 -> 1, dark-energy-first) and chiral (mirror carrier = opposite-sign holonomy; F01+N01 forced). The entropy gradient is intrinsic -- it opens with the carrier and stops opening when growth is frozen. All controls flip. This is "the rolling entangled dice / expanding chiral fuzz ball" as the ratchet's first tooth.

### Rung 1 -- the bridge tooth: carrier -> the 8 terrains

`bridge_tooth_carrier_to_terrains_sim.py`. The bare carrier has no attractor -- unitary evolution preserves trace distance, so a state and a perturbed copy stay distinguishable forever (measured: td 0.224 -> 0.261, demand OPEN). The room now demands persistence-under-perturbation: the pair must converge. The MSS-weakest structure that closes it is a single GKSL dissipator with a fixed point -- a terrain generator (a terrain closes it: td -> 0.002). Why eight: the 8 terrains are pairwise-distinct CHANNELS (min channel distance 0.195; their fixed points can coincide -- depol -> I/2 -- so channel, not fixed point, is the honest distinguishing observable). Chirality carries forward from Rung 0: the eps=+1 and eps=-1 sheets have opposite chirality (product -1), inherited handedness, not injected. Uses the real terrain generators (`engines/oracle_targets.py`). This closes the continuity gap between the origin and the geometric constraint manifold.

### The pawl -- why teeth stay held (witness identity + append-only memory)

`pawl_witness_identity_memory_sim.py`. Minimality alone does NOT lock (2026-07-04 correction sec.8): when a demand has several equal-cost witnesses, an MSS-alone pawl slides among them (measured: 12 lateral swaps accepted) -- the tooth is not actually held. The witness-identity + append-only-memory pawl requires the SAME remembered witness on re-encounter (0 swaps). And the drive must be memory-bearing to ratchet not random-walk (sec.10): memory drive climbs (9 retained teeth, gap 0.316); memory-erased drive random-walks and stalls (5 teeth, 0.059) -- the memoryless-drive kill control the owner's real climb engine also passes.

### The floor -- why the climb needs >=3 qubits

`ratchet_three_qubit_floor_sim.py`. On a single qubit the ratchet saturates: 3 Pauli bases tomographically span the qubit, so growth opens no new demand (measured: 0 teeth-before-saturation, 0 open demands at the last shell). On 2 and 3 qubits a handful of single-qubit bases resolves a vanishing fraction of the exponentially many distinguishable pairs (full tomography needs 4^n-1 axes: 3 / 15 / 63), so demands keep forcing (12 teeth; 69 and 161 open demands still open). The floor is real for the mechanism reason, not a fit -- this is WHY the owner needs at least 3 qubits for many things to run.

### The whole thing as one climb

`unified_ratchet_witness_memory_3q_sim.py`. The three pieces above run as ONE ratchet: the foundational demand/MSS/gradient mechanism + the witness-memory pawl + the 3-qubit carrier. On 3 qubits it banks a retained ladder of 3 teeth (7 acquired bases, 0 lateral swaps). Three controls flip: ladder-vs-flat (memory banks 3, memoryless twin banks 0), pawl-lock (witness-memory 0 swaps, minimality-only twin 39), Feynman freeze (0 retained teeth after growth frozen -- the drive IS the gradient). It locks by remembered witness, is driven by the intrinsic gradient, and keeps forcing teeth past dim-2.

## The climb at a glance

| Rung | Tooth | Demand it closes | Receipt | Status |
|---|---|---|---|---|
| 0 | norm-preserving chiral spinor | carry a difference between static frames | cosmogenesis_ratchet_first_tooth | measured, scratch |
| 1 | GKSL terrain dissipator (x8) | persistence under perturbation (attractor) | bridge_tooth_carrier_to_terrains | measured, scratch |
| pawl | witness identity + append-only memory | hold a tooth against lateral swap | pawl_witness_identity_memory | measured, scratch |
| floor | >=3 qubits | keep demands opening past tomographic saturation | ratchet_three_qubit_floor | measured, scratch |
| all | one climb | the above as a single ratchet | unified_ratchet_witness_memory_3q | measured, scratch |

Full harness at time of writing: 86 pass / 0 fail / 0 skip GREEN. All sims `scratch_diagnostic, promotion_allowed=false`.

## What is still owed (honest remainder)

```text
- the NEXT tooth after the terrains: terrains -> axes -> the composed engine loop
  (the 16 stages), as a continuation of this same forced climb
- the Xi bridge: geometry/history -> rho_AB (the late Axis-0 readout object), the
  biggest open structural gap
- run the unified ratchet WITH the terrain tooth in one script (currently Rung 1 and
  the unified 3q climb are separate sims)
- Type 2 (right Weyl, flux OUT) mirror engine as the eps=-1 sheet's own climb
```

## See also

- [[root-ratchet-mechanics-and-rolling-entangled-dice-2026-07-06]] -- root vs downstream doctrine
- [[entangled-dice-universe-creation-2026-07-06]] -- the cosmology statement (metaphor fence)
- [[least-presumption-mss-third-root-2026-07-04]] -- MSS as the third root
- [[geometry-entropy-dual-ratchet-verdict-2026-07-04]] -- the dual-ratchet verdict
