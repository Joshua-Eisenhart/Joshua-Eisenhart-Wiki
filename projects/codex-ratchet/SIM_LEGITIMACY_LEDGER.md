# Sim legitimacy ledger — line-item, 2026-07-01
# What is earned/verified vs what needs work. Grades are honest, not promotional.
# Verified this pass: full harness 22 pass / 0 fail / 2 skip GREEN; engines lane
# cross-validated (numpy RK4 oracle vs JAX exact-superoperator-expm agree 1e-6 on
# all 16 stages; torch passes; Julia authored, not yet run).

TIERS
  A = EXACT / SYMBOLIC IDENTITY (machine precision or provable; strongest)
  B = DYNAMICAL / FINITE-EXHAUSTIVE (solid numerical result, not symbolic)
  C = SCOPED / CANDIDATE (correct within stated limits; claim wording matters)
  D = STAND-IN / OPEN / HYGIENE DEBT (needs work)

================================================================================
LEGIT — TIER A (exact, verified)
================================================================================
1.  constraint_core_audit.py            C1-C3 -> H=C^2 realization; sigma_pm, density,
                                        Weyl laws r'=+/-2 n x r, 8 CPTP generators,
                                        b6=-b0*b3 (0/8), entropy peak S=ln2 at eta=pi/4.
                                        All PASS at 1e-16. [one CONVENTION flag: r_y sign]
2.  constraint_core_symbolic.py         T01 (1Q/2Q), N01 spine ranks, Hopf flux integral,
                                        b6 law symbolic. Exact.
3.  nonunitality_theorem_sim.py         8/8 fusion bit = 1[||L(I)||!=0]. Operators unital
                                        (=0); source-locked terrains ||L(I)||=sqrt2 exact;
                                        basis-independent. Replaces a falsified metric test.
4.  axis0_xor_sim.py                    Axis-0 = Axis-1 XOR Axis-2, exact vs repo operator
                                        table. (LOO demoted earlier — correctly.)
5.  axis0_sector_sim.py                 Two-sector: entropy blind to frame (symbolic identity,
                                        unitary similarity preserves spectrum); eigenvector
                                        move 0.67. Gauge-invariance of closed loop exact.
6.  audit_response_w_covariance_sim.py  W=(sx+sz)/sqrt2 maps Ti<->Te, Fi<->Fe EXACTLY
                                        (3.4e-33 / 4.5e-17). Native-operator law as W-covariance.
7.  axis2_two_layer_sim.py              Axis-2 = V (continuous, K=H0) x W (discrete Z2).
                                        Eigenvalue move ~9e-16, eigenvector move 1.99. Exact.
8.  eps_even_a2_specificity_sim.py      eps-symmetrization exact (mirror pairs |diff|=0);
                                        a2 exact at operator layer (||W.Ti.W-Te||=9e-16),
                                        no-go at terrain layer (residual 2.05). Resolves the
                                        last terrain-a2 open item as a LAYER statement.
9.  engines/oracle_targets.py           numpy RK4 float64 oracle -> the 16-stage contract.
                                        16 stages, min pairwise 0.0276, 16/16 order gaps>0,
                                        nonunital bits [1,0,1,0,1,0,1,0]. Verified this pass.
10. engines/jax_engine.py               Pure-functional JAX kernel, exact superoperator expm,
                                        vmap+jit, float64. Agrees with numpy RK4 oracle to
                                        1e-6 on all 16 stages -> genuine two-METHOD cross-check
                                        (integration vs matrix-exp), not a re-run. Verified.
11. engines/validate_engines.py         Cross-substrate contract checker. Recomputes invariants
                                        substrate-side (not trusted from file). GREEN on jax+torch.

================================================================================
LEGIT — TIER B (dynamical / finite-exhaustive; solid, not symbolic)
================================================================================
12. axis0_spinor_720_sim.py             360deg->-psi, 720deg->+psi exact SU(2); measurement
                                        decays the lifted phase. The spinor-level tense carrier.
13. engine_64_schedule_sim.py           64=2x8x4; order-blind -> 11/64 collapse, N01
                                        order-sensitive -> 64/64. Unique processing = N01.
14. sixteen_stage_engine_sim.py         16 = 8 terrains x 2 native operators, all distinct
                                        (mean 4.6), 16/16 order-sensitive, 8-fused/8-surplus.
15. terrain_differentiation_sim.py      All 8 terrains distinct, 14-feature fingerprint,
                                        min 0.35 (t3-t7 projective Si bottleneck).
16. terrain_sourcelock_axis0_sim.py     8 GKSL generators pinned to scratch fixed points;
                                        5 functionals all track Axis-1 (the honest negative).
17. operator_geometry_fusion_sim.py     Containment split: projective/depol 0.00-0.12 (fused),
                                        source-locked 0.67 in every frame (surplus geometry).
18. engine_type_access_sim.py           Engine type = Weyl chirality; access violation flips
                                        8/8; two 8-sets pole-mirror. Dynamical 14/16 + exact 8.
19. access_law_decoupling_sim.py        Sign follows terrain 14/16, drive 2/16; Ti/Te pinching
                                        stages negate exactly (0), Fi/Fe rotation stages don't.
20. nested_basin_sim.py                 Ne/Ni converge, Se/Si bounded; sub-basin separation
                                        Pit 0.445 vs Hill 0.005; commuting control ~2e-17.
21. flux_nesting_ablation_jax.py        Flux requires nesting: Phi(eta_i,eta_j)=2pi(cos-cos);
                                        A=0 ablation -> holonomy vanishes. [SKIP in harness:
                                        needs jax; runs in jaxcarrier env — verified earlier.]
22. axis_loadbearing_n01_sim.py  [NEW]  P12: z-axis -> Fe commutes (gap 2e-16, 16/16->12/16);
                                        (1,1,1)/sqrt3 -> gap 0.144. The coherent axis is
                                        load-bearing, not a convention. Verified this pass.

================================================================================
LEGIT BUT SCOPED — TIER C (correct within limits; watch the claim)
================================================================================
23. chi2_openpath_readout_sim.py        EARNED as an eigenvector-SECTOR meter (open-path nonzero,
                                        closed=0, gauge-invariant, tracks eigenvectors). SCOPED:
                                        NOT a2-specific — reads all 3 frame ops; the demo used
                                        the K-mirror pair. Header corrected. Do not call it "an
                                        a2 meter".
24. chi2_decisive_test_sim.py           Correct NEGATIVE result: chi2 discriminates a2/eps/K
                                        (0.94/1.13/1.51), entropy blind; terrain decisive test
                                        2/8-6/8. This is the fourth-audit finding, reproduced.
25. three_qubit_octonion_fep.py         Cayley-Dickson ladder, Cl(0,6)->C^8=3 qubits, pure-QIT
                                        free energy (no classical prob). Solid AS A CARRIER
                                        ARGUMENT; the FEP->Axis0/consciousness/gravity ceiling is
                                        explicitly NOT crossed (candidate lane).
26. manifold_build_ladder.py            L1-L5 layer ladder + co-ratchet (entropy IS a modular
                                        Hamiltonian; DPI monotone). Correct; [SKIP in harness:
                                        long-running. Also the axis-0 GATE row is honest: Axis-0
                                        is a late object, terrain-local functionals don't split it.]
27. axis0_gauge_breaking_sim.py         SCOPED. The headline "a2-physicality = k*delta, k~0.0787,
                                        R^2=1" is WITHDRAWN — the delta-dissipation is a single
                                        Kraus step, affine in delta by construction, so R^2=1 is an
                                        algebraic identity, not a law. What SURVIVES and passes: the
                                        delta=0 gauge degeneracy (the two unitary objects are the
                                        IDENTICAL channel, 2.6e-16) and the qualitative co-ratchet
                                        link (parity readable only once the entropy sector is on).
                                        Runs GREEN in harness against the survived claims, not the
                                        withdrawn one. Do not cite the linear law.

================================================================================
NEEDS WORK — TIER D
================================================================================
D1. engines/julia_engine.jl             AUTHORED but NEVER RUN (no Julia runtime in sandbox).
                                        The 3rd independent substrate. Run on laptop:
                                        `julia julia_engine.jl && python validate_engines.py`.
                                        If it disagrees, that is a FINDING — report numbers.
D2. engines/torch_engine.py             Runs and PASSES, but on this laptop torch installs with
                                        a transient "Bus error" message (harmless per fable).
                                        Re-verify on your machine; confirm complex128 path.
D3. P9 admissibility (NO SIM YET)       WHY exactly 2 native operators per terrain, from C1-C3.
                                        The one genuinely open derivation at the current layer.
                                        Currently the 2-operator law is a rosetta LABELLING, not
                                        derived. This is the top open item.
D4. Sim-hygiene debt (jargon in code)   Terrain names still appear (mostly comments, some var
                                        names like X_Ni) in: manifold_build_ladder (10),
                                        constraint_core_audit (6), terrain_sourcelock (6),
                                        operator_geometry_fusion (5), sixteen_stage_engine (5),
                                        nested_basin (2), engine_64 (1), three_qubit (1). Rule is
                                        math stays pure; names live in rosetta. Low-risk (mostly
                                        comments) but should be swept for full compliance.
D5. Scale-up to 3-qubit / Cl(0,6)       engines/ superoperator design generalizes 4->64 but the
                                        16-stage contract has only been RUN at 1 qubit. The
                                        3-qubit rung (three_qubit sim exists in principle) has no
                                        cross-substrate contract yet. Bloch readout must become a
                                        Pauli-expectation vector.
D6. Two-64s tension (OWNER DECISION)    §7g: 64 = 2x8x4 (all combos) vs 16 native stages x 4
                                        sub-stages (48 combos inadmissible). Flagged, unresolved.
                                        Not a sim bug — a modelling choice only you can make.
D7. Real engine fingerprints            sixteen_stage_engine.json / terrain_fingerprints.json are
                                        VALIDATION TARGETS for your real Julia/JAX/PyTorch engines
                                        (the repo ones). The engines/ lane is the first bridge to
                                        those; full reproduction against your production engines is
                                        still ahead.
D8. Fenced lanes (recorded, not built)  holodeck/FEP memory model and entropic-monism cosmology
                                        are connected but deliberately not expanded into audited
                                        sims. Reference docs shipped; no sims.

================================================================================
BOTTOM LINE
================================================================================
- All 24 sims_and_scripts/ files are line-itemed above (Tier A: items 1-8 + engines
  items 9-11 are the engines/ lane; Tier B: 12-22; Tier C: 23-27). 22/24 run GREEN in
  the harness; the 2 skips (flux_nesting_ablation_jax, manifold_build_ladder) are jax/
  long-run and were verified out-of-harness. Every A/B sim is a real, reproduced result.
- The engines/ lane is the real advance: the 16-stage contract now runs on a
  pure-functional JAX kernel that AGREES with the numpy oracle by an independent
  method (exact expm vs RK4). That is "engines running, unique computation per
  stage" on an aligned substrate — no longer numpy stand-in only.
- The single genuinely open derivation is P9 (why 2 operators per terrain).
- The rest of "needs work" is: run Julia (D1), sweep jargon from code (D4),
  and scale the contract to 3 qubits (D5). None of these are refutations of
  what is earned; they are the next rungs.
