# Hardening changelog — 2026-07-01 (external audit pass, claude.ai session)
All changes below are audit-inserted; sync knowingly. Sims' mathematical
content untouched except H-3 (path containment only).

H-1  ADDED    CLAUDE.md — agent contract (hard rules, withdrawn-claims list,
              honest-failure guards, V/W anti-conflation, open-decision fence).
H-2  FIXED    spec_and_reports/ORIENTATION.md had diverged from root
              ORIENTATION.md (two different orientations = agent trap).
              Replaced with a pointer stub; root is canonical.
H-3  FIXED    manifold_build_ladder.py wrote 4 JSONs into the caller's CWD.
              Now writes to sims_and_scripts/out/ (path containment only; no
              math change; verified identical stdout).
H-4  ADDED    run_all.py — deterministic harness: 20 sims, per-sim headline
              invariants with explicit tolerances, honest-failure guards
              (Axis-0 doctrine must stay False; 11/64 collapse must stay 11),
              withdrawn-claim guards ("no linear law" string asserted), JAX
              graceful skip, exit 0/1, writes run_all_report.json.
H-5  ADDED    requirements.txt (numpy/scipy/sympy required, jax optional,
              matplotlib deliberately excluded).
H-6  EDITED   spec §7g: inline AUDIT FLAG on the two-64s tension marked
              PENDING OWNER DECISION (guards against silent harmonization).
H-7  ADDED    spec_and_reports/PURE_MATH_CORE.md — the de-jargoned P1–P11
              proposition ledger from the audit session (referenced by
              CLAUDE.md as the fast label-free entry point).

H-8  ADOPTED  spec v29 (adds §7v, the χ₂ open-path instrument) from the other
              thread's lineage; re-applied H-6 (the two-64s flag, absent in
              that lineage).
H-9  EDITED   spec §7v: AUDIT FLAG with the fourth audit's grade correction —
              (i) V-vs-V* is the K-mirror pair, not the a2 pair (χ₂ responds
              to all three pairs; not charge-specific); (ii) the terrain-level
              decisive test fails (2/8 / 6/8, ε-contaminated phases). §7m
              remains admissible-candidate.
H-10 ADDED    sims_and_scripts/chi2_decisive_test_sim.py — instrument +
              charge-specificity tests + the §7m decisive test, deterministic.
H-11 ADDED    run_all.py entry for H-10 (guards the 2/8 / 6/8 result and the
              non-specificity finding against silent "fixes").
H-12 EDITED   CLAUDE.md: §7m status guard and χ₂ overclaim guard added to the
              withdrawn/hardened-claims list; open-items list updated to the
              sharpened form (ε-even a2-specific functional).

# Fourth pass — 2026-07-01 (this thread: fable-v2 merge + §7w resolution)
Base = fable's v2 zip (H-8..H-12: adopts §7v, adds the fourth-audit grade
correction and chi2_decisive_test_sim.py). This pass merged that base with the
other thread's §7v instrument and then RESOLVED the sharpened open item.
Version-label correction (per reviewer): the earlier M-1 note in the prior
bundle mislabelled the merge as spec v28->v29 / rosetta v11->v12; the saved
artifacts were spec v30 / rosetta v13. This pass produces spec (fable-v2 base
+ §7w) and rosetta with a fourth audit-log entry.

MP-1 RESTORED  chi2_openpath_readout_sim.py + chi2_openpath_readout.png (the §7v
               instrument; fable's v2 kept only the decisive-test sim). Added a
               correction header: property D is demonstrated on the K-mirror
               pair (V vs V*), not the a2 pair; math unchanged.
MP-2 ADDED     spec §7w — the terrain-level a2 item RESOLVED as a layer
               statement (no-go with a located home): eps-symmetrization is
               achievable but the eps-even functional reads a1 not a2; a2 is
               exact at the operator layer (||W.Ti.W-Te||=9e-16) and does not
               descend to terrain generators (residual ~2.05).
MP-3 ADDED     sims_and_scripts/eps_even_a2_specificity_sim.py (the no-go,
               deterministic) + eps_even_a2_specificity.png.
MP-4 EDITED    spec §7n bridge-status reconciled: chi2 = earned sector meter,
               not a2-specific; parity reads end-to-end at the operator layer.
MP-5 EDITED    PURE_MATH_CORE P10 -> earned-as-sector-meter + a2 layer no-go;
               rosetta row + open queue updated; CLAUDE.md fence: terrain-a2
               and charge-specific-chi2 items moved from "open construction" to
               "resolved no-go (§7w)"; P9 admissibility named as the open item.
MP-6 ADDED     run_all.py guards for the instrument sim and the eps-even no-go.
MP-7 ADDED     rosetta _audit_log_2026-07-01_fourth (fourth audit + §7w).
Honest-failure and withdrawn-claim guards from H-4/H-11 all still hold.


# Unified bundle — 2026-07-01 (reference docs added)
UB-1 ADDED  reference_docs/ — key source material from the repos, so the bundle
            is self-contained for a fresh thread with no repo access:
            - engine_math/ (engine-math-reference, igt-pattern-explicit-math,
              TERRAIN_LAW_LEDGER, QIT four-operator signed math, 64-schedule atlas)
            - science_method/ (recursive-science-methodology, leviathan-science-
              method-qit-engine-crosswalk, leviathan-v3.2 raw source) — the
              bidirectional engine<->science-process mapping; deductive=inductive
              reversed = the spec's UEUE/EUEU loop (§7l) / N01 order-sensitivity.
            - holodeck/ (doctrine, projective memory model, QIT-FEP-Leviathan
              integration, prediction-first processing) — the perception/memory lane.
            reference_docs/README.md maps each file to the spec sections it sources.
            These are SOURCE/SUPPORT tier (candidate/witness per their own front-
            matter), not audited spec claims.
UB-2 EDITED ORIENTATION.md LAYOUT section: added reference_docs/ + the hardening
            infra files (CLAUDE.md, run_all.py, requirements.txt, CHANGELOG).
Harness unchanged: 21 pass / 0 fail / 2 skip (jax) -> GREEN.

H-13 FIXED    run_all.py signed-zero brittleness: chi2_openpath check expected
              "closed=+0.0000" but numpy builds differ on signed zero of
              -arg(); check is now value-based (|closed| <= 1e-9).
H-14 ADDED    engines/ lane: oracle_targets.py (numpy contract ->
              targets.json), jax_engine.py, torch_engine.py, julia_engine.jl,
              validate_engines.py, README_LAPTOP.md. Verified here: oracle +
              JAX + torch agree to 1e-6 on all 16 stages (three independent
              numerical routes). Julia authored, first run pending on laptop.
H-15 FINDING  (P12) 16/16 N01 order sensitivity is load-bearing on the
              coherent axis: with H0 on the z-axis the four Fe stages commute
              EXACTLY with their terrains (phase covariance) -> 12/16. The
              bundle contained two axis conventions across sims; they are not
              interchangeable. Guarded by axis_loadbearing_n01_sim.py (H-16).
H-16 ADDED    sims_and_scripts/axis_loadbearing_n01_sim.py + run_all entry.
H-17 EDITED   CLAUDE.md: engines lane in the map; P12 axis rule added.
H-18 NOTE     torch installs with a transient "Bus error" message in this
              sandbox but imports and runs correctly (2.12.1); harmless.


# Upgrade pass — 2026-07-01 (O1 derived + laptop package + engines in harness)
UP-1 DERIVED  O1 (was the top open item): "exactly 2 native operators per terrain"
              is now DERIVED from C2, not labelled. admissibility_two_operator_sim.py.
              Same-basis (D,H) pairs commute exactly (order-gap 0) -> C2 forbids;
              2 cross-basis survivors are Axis-2 (W) conjugates; terrain frame sign
              selects one. Added to run_all.py SUITE (23rd sim). PASS.
UP-2 WIRED    engines/ cross-substrate lane into run_all.py: run_engines_lane() runs
              the numpy RK4 oracle, any importable substrate engine (jax/torch), then
              validate_engines.py; asserts GREEN. Verified PASS with jax present
              (oracle vs jax agree), SKIP when no substrate engine importable.
UP-3 ADDED    LAPTOP_RUN.sh -- one-command setup+verify for a local laptop: makes a
              .venv, installs numpy/scipy/sympy (+ jax/torch unless --fast), runs the
              full harness incl. engines lane, and runs the Julia route if julia is on
              PATH. Exit 0 = GREEN. Added LAPTOP_README.md.
UP-4 EDITED   CLAUDE.md: P9/O1 marked CLOSED; fixed a stale "≈2.05" residual to the
              real per-pair values 2.112 / 1.990. MODEL_LAYER_LEDGER 5.6 -> EARNED.
Harness now: 23 pass / 0 fail / N skip -> GREEN (engines lane PASS when jax/torch present).


# O3 done — 3-qubit contract (2026-07-01)
UP-5 SCALED   O3 (was open): the 16-stage engine contract lifted to 3 qubits (C^8).
              engines/oracle_targets_3q.py (numpy RK4), jax_engine_3q.py (exact 64x64
              superoperator expm), validate_engines_3q.py. Readout = 63-dim Pauli-
              expectation vector. GENUINELY 3q: ZZ chain coupling makes evolution
              non-factorizing (max negativity 0.038>0); 16 stages distinct (min pairwise
              0.174); 8/8 fusion + 16/16 order gaps preserved. Oracle vs JAX agree ~1e-12
              on all 16 stages in 63-dim space. Wired into run_all engines lane
              (reports "1q GREEN; 3q GREEN"). Julia/torch 3q engines: next (schema mirrors
              the 1q ones).
UP-6 NORMALIZED  wiki layout: all 25 sims consolidated under sims_and_scripts/, engines/
              lane pushed (was absent on wiki), 20 flat root duplicates removed. Public
              repo now mirrors the zip layout.


# Full-usage pass — 2026-07-01 (3 substrates verified in-house + info-processing)
UP-7 VERIFIED  PyTorch run IN-HOUSE for the first time (torch 2.12.1, CPU, complex128):
               both 1q and 3q torch engines execute here and validate against the numpy
               oracle. No "Bus error" -> D2 was fable's environment, not the code. Three
               independent routes now confirmed at BOTH scales: numpy RK4 oracle, JAX exact
               expm, PyTorch matrix_exp. 3q agreement ~1e-12 across all 16 stages (63-dim
               Pauli). Julia remains the 4th route (laptop-only; no runtime in sandbox).
UP-8 ADDED     torch_engine_3q.py (3q PyTorch route). validate_engines_3q now GREEN on jax+torch.
UP-9 NEW SIM   info_processing_sim.py -- DOES the engine process information? Each stage as a
               CPTP channel on a message qubit entangled with a reference. Result: all 16 are
               open-system processors (I_coh<0); entropy injection spans 0.006..0.991 bits
               (distinct info work); the Choi matrix separates all 16 (min 0.277); scalar
               entropy metrics collapse 5 Weyl-mirror pairs (two-sector signature at the info
               layer). figures/info_processing.png. Added to harness (now 25 pass).


# Memory layer — 2026-07-01 (spinor + holodeck precursor)
UP-10 NEW SIM  memory_sim.py -- does the engine STORE/RECALL? Three mechanisms:
               (1) memory cells: only projective-Si terrains t3/t7 retain a written z-bit
               (margin 0.71/0.53 after 8 holds); dissipative/depolarizing erase to ~0.
               (2) spinor phase memory: 360deg->sign -1, 720deg->+1, invisible at rho level.
               (3) memory<->computation tradeoff: bit margin 0.00 (tau=1) -> 0.43 (tau=0.02);
               compute hard=forget, compute gently=remember. figures/memory.png. Added to
               harness (26 pass). Model ledger Layer 12; O6 holodeck now PARTIAL (precursor built).


# Learning layer — 2026-07-01 (holodeck prediction-first / active inference)
UP-11 NEW SIM  holodeck_sim.py -- prediction-first active-inference loop in PURE QIT (free
               energy = Umegaki relative entropy, no classical math). (1) prediction loop
               minimizes F 2.62->0 monotone; (2) stationary learning cuts surprise 99%
               (belief stored in Hill projective cell); (3) single-cell capacity boundary:
               learns k=1, fails k>=2 (~0.4 bits residual); (4) 3-qubit register learns
               k=2,3,4 to <0.05 bits -> independent derived reason for the 3-qubit floor.
               figures/holodeck.png. Added to harness (27 pass). Layer 13; O6 now MOSTLY DONE.


# Leviathan bridge — 2026-07-01 (world-engine output interface, stub)
UP-12 NEW SIM  lev_bridge_sim.py + QIT_LEV_BRIDGE_SPEC.md -- the engine as a signal source a
               Leviathan graph consumes. Defines the per-tick stream contract {belief_bloch,
               surprise_bits, fe_gradient} and the LevBridge adapter (.tick/.subscribe). Proven:
               surprise is near-zero on a stable world, spikes 1.50 on a regime shift, decays as
               the engine relearns -- a usable control signal for Lev attention/action. Pure QIT.
               Deliberately NOT coupled to live Lev internals yet (foundations-up). Added to
               harness (28 pass). Layer 14; O6 bridge stub done, live wiring + action edge ahead.


# Action half / closed loop — 2026-07-01 (running world-engine)
UP-13 NEW SIM  agent_loop_sim.py -- the CLOSED active-inference loop. Adds the ACTION half:
               pick the action minimizing EXPECTED free energy G = risk - epistemic_value
               (pure QIT). Perception+action closed: from a world opposite the goal (goal_dist
               1.37) the agent drives it to preference (goal_dist <0.01, world_z +0.85) and holds
               it -- it ACTS to make the world match its model. figures/agent_loop.png. Added to
               harness (29 pass). Layer 13.5. Reverse edge Layer 14 deferred, done engine-side.


# Julia substrate live in-house — 2026-07-02 (4th route; a real finding)
UP-14 VERIFIED Installed the Julia 1.10.5 runtime IN THE SANDBOX and ran julia_engine.jl +
               julia_engine_3q.jl (the 4th independent route, the user's aligned choice).
               FINDING (CLAUDE.md rule 1): first run DISAGREED with the oracle (1q min-dist
               0.096) -- Julia is column-major, so reshape(transpose(rho),4) mismatched numpy's
               column-stacking vec. Fixed to reshape(rho,4)/reshape(v,2,2). After the fix all
               four substrates agree: 1q min-dist 0.0276, 3q worst pvec dev 9.89e-13 on C^8.
               Made the Julia engines DEPENDENCY-FREE (hand-rolled JSON, no registry / no ] add).
               Wired both into run_all engines lane (reports "...+julia GREEN" when julia is on
               PATH). Julia runtime archived as an artifact so it survives workspace sweeps.


# Formal proof lane — 2026-07-02 (laws FORCED, not fitted; aligned tools installed)
UP-15 TOOLS    Read the 3-engine dependency contract and installed the aligned Python-lane
               tools it names: z3-solver + cvc5 (SMT proof pair), qutip (QIT library), plus
               quimb/cotengra/diffrax/optax/sympy/mpmath. Julia package registry remains
               blocked by sandbox TLS interception (pkg.julialang.org connects but the
               re-signed cert is unparseable by Julia's downloader) -> Julia engine stays
               dependency-free (LinearAlgebra); the strict-carrier Julia packages are a
               laptop-side TODO.
UP-16 NEW SIM  axis_laws_dual_proof.py -- the axis laws are FORCED (SMT), proven in Z3 AND
               cvc5 with agreement, WITH an erased control that flips the verdict (drop the Ni
               constraint -> XOR uniqueness breaks). Proves: (1) Axis-0=Axis-1 XOR Axis-2 is the
               UNIQUE boolean law and IS xor; (2) b6=-b0*b3 uniquely bilinear, no linear law
               fits. Satisfies the contract's "z3 & cvc5 agree with erased controls that flip".
UP-17 NEW SIM  terrain_qutip_crosscheck.py -- QuTiP (standard Lindblad) reproduces the hand-
               rolled terrain superoperators to 2.2e-16 across all 8 terrains, confirms all 8
               CPTP (Choi PSD) and the nonunitality bits. 5th independent route at operator level.
               Both sims self-skip if tools absent (portable). Layer 15; harness 30 pass (constraintcore).


# Proof lane extended — 2026-07-02 (three more manifold laws forced)
UP-18 NEW SIM  manifold_laws_smt_proof.py -- (1) 8-of-16 access law FORCED by the sheet law
               (Z3: any non-8/8 split UNSAT); (2) pole-mirror pairing (0,4)(2,6) forced by
               zero-sum AND cross-sheet -- with the logged FINDING that zero-sum ALONE is
               degenerate (2 matchings zero-sum; near-equal |fixed_z|); (3) two-sector theorem
               as a SYMBOLIC IDENTITY (sympy): eigs(rho(theta,phi))={p,1-p} for all angles,
               dS/dtheta=0 exactly -> entropy identically blind to Axis-2. Self-skips if
               z3/sympy absent. Layer 15.7-15.9; harness 31 pass (constraintcore).


# Physics bridges — 2026-07-02 (established physics on the info<->physics seam)
UP-19 NEW SIM  physics_bridge_sim.py -- the engine reproduces two pieces of confirmed physics
               (NOT a ToE validation). (1) Landauer: dissipative terrains erase a bit; pure
               limit saturates the bound (S:1->0, purity->1, bath >= kT ln2 = 2.87e-21 J@300K);
               coherent drive only makes erasure partial. (2) Einselection: Ti z-dephasing
               selects {|0>,|1>}, Te selects {|+>,|->}; pointer states ARE the purity-1 channel
               fixed points -- "an attractor basin that selects for itself" as decoherence
               physics. figures/physics_bridge.png. Self-skips if qutip absent. Layer 16.


# Fluctuation theorems — 2026-07-02 (nonequilibrium generalization of the Szilard bound)
UP-20 NEW SIM  fluctuation_theorem_sim.py -- the engine's unitary drive obeys Jarzynski
               (<e^-bW>=e^-bdF, 3e-14 at every drive speed) AND Crooks (P_F/P_R=e^{b(W-dF)}
               across all work bins). 2nd law <W>>=dF holds; dissipated work drops as drive
               slows. Genuine dF=-0.793 (nontrivial). FINDING: first Crooks pass failed at the
               tails -- a reverse-protocol bug, not physics; fixed time-reversed drive recovered
               the exact law. numpy-only. Layer 16.3; harness 33 pass (constraintcore).


# Quantum speed limit — 2026-07-02 (the model's two axioms as a physical bound)
UP-21 NEW SIM  quantum_speed_limit_sim.py -- the engine's drive obeys the QSL, tying FINITUDE
               and NONCOMMUTATION to dynamics. (1) t_orth=(pi/2)/dE saturates the Levitin-
               Toffoli bound (ratio 0.999) at every energy; larger dE = faster. (2) [H,rho]!=0
               <=> dE>0 <=> evolution (three equivalent); commuting H never moves; full
               orthogonality needs the state balanced across eigenstates (tilted H precesses
               part-way). numpy-only. Layer 16.4; harness 34 pass (constraintcore).


# Holographic bound + decoherence scaling — 2026-07-02 (finitude & the classical boundary)
UP-22 NEW SIM  holographic_bound_sim.py -- FINITUDE as the holographic/Bekenstein bound:
               S(rho)<=log2(dim) (maximally-mixed saturates); Page-curve area law S(A)<=
               min(|A|,|B|) on n=6 qubits (smaller boundary caps shared info). numpy-only. L16.5.
UP-23 NEW SIM  decoherence_scaling_sim.py -- HOW FAST einselection wins: GHZ decoherence rate
               ~2n (independent baths, linear) / ~2n^2 (collective, superdecoherence, exact).
               The quantum->classical boundary is a scaling law. numpy+scipy. L16.6.
               Harness 36 pass (constraintcore).
