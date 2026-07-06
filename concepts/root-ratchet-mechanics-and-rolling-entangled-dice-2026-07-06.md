# Root ratchet mechanics and the rolling entangled dice (current synthesis)

Provenance: consolidates the owner's root-ratchet synthesis package `CR_root_ratchet_current_project_FULL_v2_20260706` (2026-07-06) with the measured sim receipts produced this session. Ceiling: **doctrine-router + scratch_diagnostic receipts** — the doctrine (root vs downstream, faces of one basin) is owner synthesis, NOT canon promotion; the sims cited are `scratch_diagnostic, promotion_allowed=false` mechanism illustrations, not derivations. Where a claim is measured it says "measured (sim ...)"; where it is doctrine it says "doctrine".

## Why this page exists

The owner's `ROOT_RATCHET_CURRENT_SYNTHESIS.md` states the reason directly: to "consolidate the current root object so later Lev, holodeck, FEP, IGT, physics, and product metrics do not get mistaken for the root." Downstream faces kept being taken for the foundation. This page fixes the distinction and links each root claim to whatever receipt currently exists.

## The one root object

```text
root = MSS
     + F01 (finitude)
     + N01 (noncommutation)
     + probe-relative identity  (a = a iff a ~ b)
     + Axis-0 drive / entropy-gradient (intrinsic, not injected)
     + dual-ratcheting QIT entropic-geometric constraint manifold
```

Everything below is a **face that measures whether the root works**, never the root itself:

```text
downstream faces: QIT engines - FEP/active inference - IGT/perception-strategy
                  - holodeck/object formation - Leviathan/mesh world model
                  - physics/TOE readouts - cosmology/sequential inheritance
```

Rule (owner, `FACES_OF_THE_ATTRACTOR_BASIN.md` / `DOWNSTREAM_METRICS_NOT_ROOT.md`): *"Do not let the downstream faces replace the root. They measure whether the root works. They do not define the root."*

## Axis-0: drive early, readout late

The recurring failure was building Axis-0 only as the late Phi_0 / coherent-information readout (the *rolled* die) and never as the early drive (the *rolling* die). Both objects are real:

| Object | When | What | Belongs |
|---|---|---|---|
| Axis-0-as-drive | early, root-side | rolling process; entropy-/possibility-gradient | near MSS + the first live ratchet |
| Axis-0-as-readout | late, cut-dependent | Phi_0 / coherent information after Xi | after geometry/history become a density/cut object |

"If Axis-0 is placed only late, the model loses its motor" (owner, `AXIS0_DRIVE_VS_READOUT.md`).

## MSS is the admissibility constraint, not a preference - measured

MSS admits **only the weakest structure that (a) survives and (b) still evolves**; larger leaps are inadmissible; the pawl holds when no admissible step is forced. This runs, with the verdict derived from the demand structure rather than a picked climb count:

- `foundational_ratchet_entropy_gradient_sim.py` (scratch_diagnostic): a **demand** = a pair the room asserts distinguishable (trace distance > theta) that acquired bases don't resolve; a step is admissible only if it closes >=1 demand; the **pawl is proven** (every non-climb shows candidate bases rejected-unforced); co-ratchet one-for-one; Axis-0 acts the moment a demand exists. Measure is quantum distinguishability (trace distance/Helstrom) - **no bits, no vectors**. Honest remainder (measured): a dim-2 carrier **saturates** after 2 forced teeth - the gap widens but no new demand opens, because 3 noncommuting qubit bases resolve every new pair. That is the F01 3-qubit-floor, reached by the mechanism, not assumed.

> Open pawl question carried from the 2026-07-04 summary (section 8): minimality alone does **not** lock - plural minima allow lateral swaps; the lock also needs **witness identity** (remembering the exact admitted witness/provenance) + append-only memory. The current sim's pawl = MSS-admissibility; the witness-identity/memory clause is not yet in it. This is the next hardening of the pawl.

## Cosmogenesis = the ratchet's first tooth (MSS in a static field) - measured mechanism illustration

The owner's `ROLLING_ENTANGLED_DICE_CREATION_MODEL.md` gives the sequence: static pre-ratchet possibility field -> finite entangled/chiral live support -> rolling entangled dice -> expanding chiral fuzz ball -> spacetime. The **same** demand/MSS/entropy-gradient rules, run in a static field, reproduce it:

- `cosmogenesis_ratchet_first_tooth_sim.py` (scratch_diagnostic): time = a carried difference between frames (static field carries ~0; a persistent carrier carries ~0.94); **MSS forces the norm-preserving (division) carrier** - a lossy map annihilates the difference back to static, a norm-preserving spinor persists; the carrier's expansion is **entangled** (concurrence 0->1, dark-energy-first) and **chiral** (mirror carrier = opposite-sign holonomy; F01+N01 forced); the **entropy gradient is intrinsic** - it opens with the carrier and stops opening when growth is frozen (Feynman knife). All controls flip.

Discipline note (respecting [[entangled-dice-universe-creation-2026-07-06]]): the sim does **not** mechanize the dice *metaphor*. It tests whether the *ratchet mechanism* reproduces the persistence criterion. The classical Cartesian/checkerboard picture stays a fence; only the distinguishability + norm-preserving math is in the sim. Owner doctrine under test (entropic-monism fence): a mechanism illustration, not a derivation of the cosmological constant or actual early-universe dynamics.

## Dual-ratcheting manifold - the loop

```text
geometry            -> constrains possible operators/readouts
operators/readouts  -> create entropy/memory demands
demands             -> force new admissible geometry
new geometry        -> changes possible operators/readouts
```

Geometry and entropy "seem separate and are one": measured at qubit fixed points, the entropy face (Hessian of relative entropy) equals the geometry face (BKM information metric), separation UNSAT (`surface_identity_sim.py`). This is the established Tomita-Takesaki / Connes-Rovelli thermal-time program **used**, not claimed as new.

## Downstream success metrics (this session) - explicitly not root

The objective-validity work built this session is downstream-by-design: it measures whether the engines earn objecthood, and is kept structurally separate from the root so its gates cannot be tuned:

- **Re-identification under probe rotation** (`engine_reidentification_objective_sim.py`): identity is the survivor of probe rotation (a=a iff a~b operational). 11/16 stages re-identify from never-seen probes; the 5 misses are the depol eps-degenerate pairs + the Fe proj-commuting pair the engine math predicts. Control (shuffled stages -> chance) flips.
- **External dynamics-ID** (`engine_dynamics_id_arbiter_sim.py`): PySINDy (off-the-shelf, zero theory input) reconstructs 7/8 terrain flows at held-out R^2 0.93-1.00; shuffled-time control detonates; t3 (projective) is the one terrain not polynomial-identifiable.
- **Object-formation scorecard** (`engine_object_formation_scorecard_sim.py`): composes the two above into an adapted formation-loss surface under the Lev mesh-package **measurement/verdict separation** - instruments emit numbers, a separate policy eval decides on controls flipping. This discipline is the structural fix for gate-tuning: a gate the instrument does not contain cannot be relaxed.

Owner framing (`DOWNSTREAM_METRICS_NOT_ROOT.md`): "Use downstream metrics to test success. Do not mistake them for root mechanics."

## Current receipts at a glance

| Root claim | Receipt | Status |
|---|---|---|
| MSS forces weakest admissible structure; pawl proven | foundational_ratchet sim | measured, scratch |
| Cosmogenesis = ratchet's first tooth | cosmogenesis_ratchet_first_tooth sim | measured, scratch |
| Entropy gradient intrinsic (drive early) | both sims (freeze halts gap) | measured, scratch |
| Geometry face = entropy face | surface_identity sim | measured, scratch |
| dim-2 saturation -> 3-qubit floor | foundational_ratchet honest remainder | measured, scratch |
| Witness-identity pawl lock | - | owed (2026-07-04 section 8) |
| Xi bridge geometry->rho_AB | - | biggest open gap |

Full harness at time of writing: 82 pass / 0 fail / 0 skip GREEN. All sims `scratch_diagnostic, promotion_allowed=false`.

## See also

- [[entangled-dice-universe-creation-2026-07-06]] - the cosmology statement (proposal-facing; metaphor fence)
- [[least-presumption-mss-third-root-2026-07-04]] - MSS as the third root
- [[geometry-entropy-dual-ratchet-verdict-2026-07-04]] - the dual-ratchet verdict
- [[igt-discovery-and-two-engines-2026-07-04]] - IGT as a downstream face
- [[iff-chain-identity-duality-2026-07-03]] - a=a iff a~b worn many ways
