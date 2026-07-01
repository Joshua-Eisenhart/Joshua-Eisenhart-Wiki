# Constraint-Core Formalization — Self-Contained Bundle

Read this first. This bundle is a complete, zero-context snapshot of a formalization of
Joshua Eisenhart's constraint-based theory. A fresh thread with no repo access and no prior
conversation can work from it alone.

STATUS: synced-not-canon. Every result is scratch_diagnostic (promotion_allowed=false). The
ratchet earns canon separately; nothing here is asserted as final.

================================================================================
1. WHAT THE PROJECT IS
================================================================================
A theory-of-everything built as a monotone GENERATIVE RATCHET on the weakest structures:
each layer must be earned from the one below before the next is taken. Foundations:
  - Root axiom: a = a  iff  a ~ b   (identity is emergent from distinguishability).
  - Dual constraints: FINITUDE and NON-COMMUTATION (nonassociativity enters at the octonion
    layer). Equivalent framings: deduction iff induction; Turing machine iff oracle;
    reason iff perception.
  - ENTROPIC MONISM: entropy and operators are not separate from the geometry; they
    co-ratchet on the same manifold (a Hamiltonian/Hilbert-space-like duality).
Substrate discipline: sims are PURE MATH (numpy/scipy, jax for two). No classical
probability smuggled in. Named structure (Jungian functions, terrains, physics vocabulary)
lives ONLY in the rosetta layer (rosetta_layer.json), never in the sim math.

================================================================================
2. THE GEOMETRIC CONSTRAINT MANIFOLD
================================================================================
A 7-axis manifold (Axes 0-6), built layer by layer in the order 6-5-3-4-1-2-0.
The degrees of freedom must NOT collapse. Key objects:
  - 8 TERRAINS: source-locked GKSL generators on C^2, indices t0..t7 in the sim; names in
    rosetta (t0 Funnel, t1 Vortex, t2 Pit, t3 Hill, t4 Cannon, t5 Spiral, t6 Source,
    t7 Citadel). 4 dissipative + 4 unitary-dominant.
  - 4 OPERATORS: Ti (z-dephasing), Te (x-dephasing), Fi (x-rotation), Fe (z-rotation).
  - 16 STAGES = 8 terrains x 2 native operators. 64 addresses = 16 x 4 sub-stages.
  - 2 ENGINE TYPES = the 2 Weyl chiralities (eps=+/-1); each person is ONE engine and
    accesses 8 of the 16 stages.

================================================================================
3. THE FIVE-PLUS AXIS-0 RESULTS (the hard gate, in order)
================================================================================
Axis-0 is where most attempts stall. The chain (each has a sim + a figure):
  §7m  XOR:            Axis-0 = Axis-1 XOR Axis-2 (exact). Not linearly separable ->
                       14 single readouts all failed. [axis0_xor_sim.py]
  §7n  Two sectors:    Axis-1 = entropy charge (eigenvalues); Axis-2 = phase charge
                       (eigenvectors, invisible to entropy). [axis0_sector_sim.py]
  §7o  Gauge degen.:   exact gauge degeneracy at delta=0 (two unitary objects = identical
                       channel). NOTE: an earlier "linear law R^2=1" was WITHDRAWN as a
                       parametrization artifact; the GKSL rebuild gives a saturating, not
                       linear, response. [axis0_gauge_breaking_sim.py v3]
  §7p  Differentiation: all 8 terrains distinct under a 14-feature fingerprint; bottleneck
                       t3/t7 (projective Si pair). [terrain_differentiation_sim.py]
  §7q  Fusion:         two-tier. THEOREM (upgraded): the 8/8 fusion split = 1[||L(I)||!=0]
                       (non-unitality). Operators are unital; source-locked terrains carry
                       ||L(I)||=sqrt2. [operator_geometry_fusion_sim.py, nonunitality_theorem_sim.py]
  §7r  16 stages:      all distinct + order-sensitive (N01, 16/16); 8 fused / 8 source-surplus.
                       [sixteen_stage_engine_sim.py]
  §7s  Access law:     eight-of-sixteen. Chirality lives in the terrain (14/16 vs 2/16
                       decoupled). Two-tier: EXACT conjugation identity on 8 dephasing
                       stages, dynamical 14/16 on rotation stages (failures t3/t7:Fe).
                       [engine_type_access_sim.py, access_law_decoupling_sim.py]
  §7t  Native law:     EARNED. The Hadamard involution W=(sx+sz)/sqrt2 maps Ti<->Te, Fi<->Fe
                       exactly. [audit_response_w_covariance_sim.py]
  §7u  Axis-2 2-layer: the W-vs-V fork resolved. Axis-2 = (V continuous frame, connection
                       K=H0) x (W discrete direct/conjugated involution). Compose via K->WKW.
                       No spec repair. [axis2_two_layer_sim.py]

================================================================================
4. SIM HYGIENE + ROSETTA (read before touching the math)
================================================================================
Sims contain ONLY structural indices (eps, a1, a2, t0..t7, Ti/Te/Fi/Fe). All interpretive
labels are quarantined in rosetta_layer.json with an earned/witness/candidate tier:
  earned    - verified against the operator table (axis math, terrain names, W-covariance,
              non-unitality, engine-type access).
  witness   - Jungian functions, taijitu yin-yang (recorded, not design inputs).
  candidate - Carnot/Szilard, I-Ching (only the 2^6=64 count is grounded; never forced).
The rosetta also carries the AUDIT LOG: three external-thread audits that reproduced the
work and forced corrections (the §7o withdrawal, the §7q null reframing, the §7q->theorem
upgrade). That log is the ratchet working across instances.

================================================================================
5. HOW TO RUN
================================================================================
Each file in sims_and_scripts/ is standalone: `python <name>.py` prints its headline numbers.
Dependencies: numpy, scipy (all); jax (flux_nesting_ablation_jax.py only). No repo needed.
The full formal spec is spec_and_reports/CONSTRAINT_CORE_FORMAL_SPEC.md (v28).

================================================================================
6. WHAT IS STILL OPEN (short, honest ledger)
================================================================================
  1. chi_2: the open-path eigenvector-sector (phase-charge) readout for the Xi bridge.
     The one genuinely open item at the current layer. Closed-loop holonomy proven
     insufficient (gauge-invariant); needs a relational open-path instrument.
  2. Terrain-level a2 bit: W-covariance is exact at the OPERATOR level but NOT at the
     terrain level (generator-map residuals 1.4-2.0). The direct/conjugated assignment on
     terrains still rests on the source table alone.
  3. Run the owner's real Julia/JAX/PyTorch engines; the per-stage fingerprints
     (sixteen_stage_engine.json, terrain_fingerprints.json) are the validation targets.
  4. Connected-but-fenced lanes: holodeck/FEP memory, entropic-monism cosmology (dark
     sector). Recorded, deliberately not expanded.

================================================================================
7. LAYOUT
================================================================================
  ORIENTATION.md            - this file
  spec_and_reports/         - the full spec (v28), consolidated guide, methods report
  figures/                  - all result figures (PNG)
  sims_and_scripts/         - standalone pure-math sims
  data_json/                - per-result data + rosetta_layer.json
  inputs/                   - the Personality spreadsheet (drift-prone; left unexpanded)
