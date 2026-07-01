# Constraint-Core Formalization — Self-Contained Bundle

**This bundle is fully self-contained.** A fresh AI thread or reader with NO prior context and NO
access to the source repos can work from it alone. Everything needed is here.

Exported: 2026-07-01. Status: **scratch_diagnostic / synced-not-canon** — exploration feeding the
ratchet, NOT admitted canon. `promotion_allowed = false` on every result.

---

## 0. What this project is (read first)

The owner (Joshua Eisenhart) is building a constraint-based "theory of everything" that unifies math,
physics, biology, and consciousness on a **nominalist, constraint-first foundation**. Core ideas:

- **Root axiom:** `a = a iff a ~ b` — identity is emergent from distinguishability under a probe, not
  primitive. This yields an **entropic monism**.
- **A monotone generative ratchet:** all of mathematics must be *earned step by step*; nothing is
  admitted (made "canon") until the constraints and kill-tests leave no weaker surviving alternative.
  "The ratchet itself is what earns things being canon." LLMs tend to make things canon prematurely —
  so results here are explicitly fenced as scratch/exploration.
- **Two main constraints:** non-commutation (N01) and finitude (F01), plus bracketing
  non-associativity (T01). Reduces most mathematics to what runs on a Turing machine, with an
  "oracle" dual (deduction iff induction, reason iff perception).
- **The QIT engines:** the concrete object. Density matrices on C^2 (qubits) evolving under
  constraint-locked GKSL/CPTP dynamics. Structures analogous to Carnot/Szilard engines but in a
  different math base. Personality types, I-Ching, and taijitu are *witness overlays*, not inputs.

## 1. The geometric constraint manifold and its 7 axes

The manifold has 7 degrees of freedom (Axis-0..Axis-6) that must NOT be collapsed. The engines run on
this manifold. The axes (as earned in this work):

- **Axis-6**: composition order (operator-first vs terrain-first) — the signed Axis-6.
- **Axis-5**: dephasing/projection vs unitary rotation.
- **Axis-3**: fiber/inner loop vs base/outer loop.
- **Axis-4**: deduction (UEUE) vs induction (EUEU) — composition-order family.
- **Axis-1**: unitary vs dissipative (coherent vs CPTP dynamics). Split {Se,Ni} | {Ne,Si}.
- **Axis-2**: direct vs conjugated frame (lab vs co-rotating). Split {Se,Ne} | {Ni,Si}.
- **Axis-0**: the perceiving axis (intuition/sensing, N/S). Split {Ne,Ni} | {Se,Si}. **The hard one.**

The build order is 6 → 5 → 3 → 4 → 1 → 2 → 0; Axis-0 is where most models stall.

## 2. The KEY RESULTS of this bundle (what was earned)

The central achievement is the **resolution of the Axis-0 stall**, in five linked steps:

1. **Axis-0 = Axis-1 XOR Axis-2** (spec §7m). The perceiving split is the *parity* of the dynamics
   and frame axes. XOR is not linearly separable → no single scalar readout can ever realize it,
   which is exactly why 14 prior single-cut readouts all failed. `axis0_xor_sim.py`.
2. **The two-sector theorem** (§7n). Axis-1 is an ENTROPY charge (eigenvalue sector); Axis-2 is a
   PHASE/GAUGE charge (eigenvector sector, invisible to every entropy functional, proven to 2e-15).
   The parity needs both sectors, multiplied. `axis0_sector_sim.py`.
3. **The gauge-breaking law** (§7o). The frame bit becomes physically readable in LINEAR proportion
   to symmetry-breaking dissipation δ (a2-physicality = 0.0787·δ, R²=1.0000). This makes "Axis-0 is a
   late object" quantitative and ties it to the co-ratchet (entropy must be earned first).
   `axis0_gauge_breaking_sim.py`.
4. **Maximal terrain differentiation** (§7p). All 8 terrains distinct under a 14-feature dynamical
   fingerprint (mean dist 5.5); bottleneck = the two projective Si terrains (nearly sheet-symmetric).
   `terrain_differentiation_sim.py`, `terrain_fingerprints.json`.
5. **Operator-geometry fusion** (§7q) and **the 16 engine stages** (§7r). "The surface IS the
   operator": for projective/depolarizing terrains the generator literally equals its operator algebra
   (residual 0.00-0.12, the GR-ether case); source-locked terrains carry irreducible surplus geometry
   (0.67, frame-independent). The 16 stages (8 terrains × 2 native operators, signed Axis-6) are all
   distinct + order-sensitive (N01), splitting 8 fused / 8 source-surplus — the same 8/8 split
   coincides across §7o, §7p, §7q. `operator_geometry_fusion_sim.py`, `sixteen_stage_engine_sim.py`.

## 3. SIM HYGIENE — the discipline (important for any continuation)

**Sims are PURE MATH with NO jargon.** Structural indices only: `eps ∈ {±1}` (sheet sign),
`a1 ∈ {0,1}` (dynamics bit), `a2 ∈ {0,1}` (frame bit), `t0..t7` (terrains), `Ti/Te/Fi/Fe` (operator
channels). NO personality names, NO "intuition/sensing", NO terrain names appear in the computation.

**All labels live in `rosetta_layer.json`**, tagged by earned status:
- **earned**: the structure realizes it exactly (a1→Axis-1, a2→Axis-2, p→Axis-0; the 8 terrain names).
- **witness**: usable symbolic crosswalk, must NOT replace the math (Jungian functions, taijitu yin/yang).
- **candidate**: suggested, not closed, never a design input (Carnot/Szilard, I-Ching).

If you continue this work: keep this separation. Structure first, labels second, only where earned.

## 4. The terrain / operator dictionary (the rosetta)

8 terrains (index : name : Axis-1,Axis-2 bits : native operators):
  t0 Funnel (Se-in)   dissip,direct    Ti,Fi      t4 Cannon (Se-out)  dissip,direct   Ti,Fi
  t1 Vortex (Ne-in)   unitary,direct   Ti,Fi      t5 Spiral (Ne-out)  unitary,direct  Ti,Fi
  t2 Pit (Ni-in)      dissip,conjug    Te,Fe      t6 Source (Ni-out)  dissip,conjug   Te,Fe
  t3 Hill (Si-in)     unitary,conjug   Te,Fe      t7 Citadel (Si-out) unitary,conjug  Te,Fe

4 operators: Ti = z-dephasing, Te = x-dephasing, Fi = x-rotation, Fe = z-rotation.
Native law: direct terrains {Se,Ne} admit Ti+Fi; conjugated {Ni,Si} admit Te+Fe. (See rosetta_layer.json.)

## 5. How to run everything

All `*_sim.py` files are standalone and reproduce their key numbers. Requirements: `numpy`, `scipy`
(and `matplotlib` only if you regenerate figures). `flux_nesting_ablation_jax.py` and
`manifold_build_ladder.py` use `jax`. Run any sim with `python <name>.py`.

The authoritative document is **CONSTRAINT_CORE_FORMAL_SPEC.md** (sections §0-§10, with the geometric
manifold arc in §7-§7r). Two reader's guides: `geometric_manifold_consolidated.md` and
`constraint_core_methods_report.md` (tools/process/thinking/suggestions).

## 6. What is still OPEN (honest edges)

- Axis-0's continuous Ξ bridge (bipartite ρ_AB → Φ_0) is still open: the parity is now understood
  (§7m-§7o) but the two-sector INSTRUMENT (entropy meter + relational phase meter) is not fully built.
  The phase-charge readout χ_2 remains the specific open piece (closed-loop holonomy provably fails).
- Source-locked terrains carry irreducible geometry beyond the operator algebra (§7q) — a genuine
  surplus degree of freedom.
- The real Julia/JAX/PyTorch engines (in the owner's repos) have not been run here; the per-stage
  fingerprints (`sixteen_stage_engine.json`, `terrain_fingerprints.json`) are the validation targets.
- Connected-but-fenced lanes: holodeck/FEP memory model, entropic-monism cosmology (dark energy/matter)
  with dynamic shells. Not expanded here; each has its own claim ceiling.

## 7. File manifest

See folder structure below. `spec_and_reports/` = the spec + reader's guides + rosetta;
`figures/` = all PNGs; `sims_and_scripts/` = all standalone Python sims; `data_json/` = all result
data; `inputs/` = the owner's original Personality theory spreadsheet.

---
*Provenance: Claude Science session 2026-07-01. All results scratch_diagnostic; the ratchet earns canon.*
