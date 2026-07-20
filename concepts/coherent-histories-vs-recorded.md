---
title: Coherent histories vs recorded histories
created: 2026-07-19
updated: 2026-07-19
type: concept
tags: [quantum, physics, mathematics, proof]
sources:
  - owner-pack-167_3 (audit/FEYNMAN_DIRAC_HISTORY_RECONCILIATION_20260716.md, desktop/FEYNMAN_DIRAC_COHERENT_HISTORY_TASK_CARD.md)
  - owner-pack-170-axis0-history-gate-delta (contracts/AXIS0_COHERENT_HISTORY_GATE.md, audit/167_5_DIRECTIONAL_WITNESS_AUDIT.md)
  - owner-pack-171-feynman-dirac-nested-history-delta (math/FEYNMAN_DIRAC_NESTED_WELD.md, contracts/FD_NESTED_HISTORY_CONTRACT.md, audit/GITHUB_FD_EVIDENCE_AUDIT.md)
  - owner-pack-RATCHET_188 (active/history_geometry.py)
framing: current
status: research-note
---

# Coherent histories vs recorded histories

## The core distinction

167.3 diagnoses the project's inherited Feynman-labelled scout as an **incoherent branch sum**, not Feynman's actual move. The old formula sums Kraus operators without cross terms:

Z_Kraus = Σ_h Tr[E K_h ρ K_h†]

with no h≠h' terms. That is a legitimate quantum-instrument/process calculation for a regime where a path record already exists, but it is "not yet Feynman's load-bearing move" (`audit/FEYNMAN_DIRAC_HISTORY_RECONCILIATION_20260716.md`, §2).

Feynman's rule instead adds complex history amplitudes coherently, before the Born rule is applied. The finite Ratchet-compatible form given in 167.3 is:

C_y = Σ_{h∈H_y} A_h, p(y) = Tr(E_y C_y ρ C_y†)

Expanding gives p(y) = Σ_{h,h'∈H_y} Tr(E_y A_h ρ A_h'†), so interference is exactly the off-diagonal h≠h' content (same file, §2). The old Kraus-history scout is recovered as "a controlled decohered limit when path records make those off-diagonal terms vanish" — i.e. recorded histories are a limiting case of coherent histories, not a separate object. See [[concepts/literal-entropic-gcm]] for the same construction placed inside the owner's wider noncausal cosmology.

171's weld restates this with explicit bracketing `b` and a class operator C_y^(λ) = Σ_{(h,b)∈H_r(y)} A_{h,b}^(λ), and is explicit that "no partial trace, dephasing, measurement, or branch normalization may occur inside a route later called coherent" (`math/FEYNMAN_DIRAC_NESTED_WELD.md`, §3).

## The Kraus-mixture control

Across all four packs, the Kraus/recorded formula is kept — but demoted to a **comparator lane**, never the completed mechanism:

- p_recorded(y) = Σ_h Tr(E_y A_h ρ A_h†), "appropriate only after an explicit record/cut destroys or makes unavailable the cross terms" (`FEYNMAN_DIRAC_NESTED_WELD.md`, §3; near-identical statement in `contracts/FD_NESTED_HISTORY_CONTRACT.md`, Gate 2).
- The GitHub audit confirms the actual repo code implements exactly this recorded sum (`acc = acc + k @ rho @ torch.conj(k).T`, i.e. Σ_h K_h ρ K_h†) with no cross terms, and reclassifies it: "a good decohered / which-history / instrument control, but cannot be the load-bearing Feynman operation" (`audit/GITHUB_FD_EVIDENCE_AUDIT.md`, §1). The audit's disposition table files it explicitly as `Kraus histories -> recorded/decohered comparator`.

So "control" here means: the Kraus sum is the null/baseline lane a coherent-history claim must beat and must reduce to when a record exists — not an independent physical claim.

## The bracketing registry

167.3 introduces explicit bracket memory on top of ordering. A history is `(h,b)` where `b` is its explicit parse tree of composition, required whenever composition is not already earned associative:

A_(ab)c ≠ A_a(bc) "must be retained until a quotient or factor witness earns their equivalence" (`FEYNMAN_DIRAC_HISTORY_RECONCILIATION_20260716.md`, §3, "Nonassociativity and bracket memory").

171 makes this a gate requirement rather than a suggestion: every surviving history must carry "explicit bracketing if composition has not earned associativity" plus "a provenance hash of the complete compatible nest from which it was derived" (`FD_NESTED_HISTORY_CONTRACT.md`, Gate 1). The task card operationalizes it as a second-stage fixture: after the ordered/associative case passes, add "an explicitly bracketed composition fixture using the Julia-owned algebra table," preserving `(ab)c` and `a(bc)` as distinct histories "when their associator is nonzero," with Julia arbitrating semantics (`desktop/FEYNMAN_DIRAC_COHERENT_HISTORY_TASK_CARD.md`, "Bracket extension"). No single file in this set uses the literal words "bracketing registry" as a named object-noun; the object that plays that role is the per-history `(h,b)` pair plus its provenance hash, tracked across the tournament stages (FD0–FD7 in 167.3 §5) so that a given calculation is always tagged by which lane it is running in: coherent-unresolved, recorded/decohered, phase-scrambled, classical-mixture, single-path, or commuting-order (`FEYNMAN_DIRAC_COHERENT_HISTORY_TASK_CARD.md`, "Required lanes"; restated as the 8-lane comparator set in `170.../contracts/AXIS0_COHERENT_HISTORY_GATE.md`, "Finite coherent histories").

## Interference witnesses

Named explicitly across sources:

- **W_int = p_coh − Σ_h p_h**, the interference witness proper, reported alongside the full off-diagonal history Gram matrix G_hh' = Tr(E A_h ρ A_h'†) (`FEYNMAN_DIRAC_COHERENT_HISTORY_TASK_CARD.md`, "Required lanes"). The pass condition requires W_int nonzero in the coherent lane and vanishing (within tolerance) for recorded, classical-mixture, and commuting controls.
- 171's contract requires the same Gram block G_hh' be serialized and states a program that "only serializes a scalar `path_count`, `Z_path`, or endpoint state fails this gate" (`FD_NESTED_HISTORY_CONTRACT.md`, Gate 2).
- 170's gate adds an unprojected response vector R_δ(t) = (ΔV, ΔS, ΔG, ΔQ, ΔNest, ΔCoh, ΔRecord, ΔIncoming) for a related directional-witness program, with `Δcoh` as one tracked component (`contracts/AXIS0_COHERENT_HISTORY_GATE.md`, "Response is observed, then classified").
- The 167.5 audit (adjacent, not itself a §4 doc) reports a concrete `interference_frobenius`-style finite ingredient: row amplitudes summed into a 2×4 matrix before density is taken, called "a useful finite coherent-recombination ingredient, not merely a recorded-count mixture," but explicitly "not yet a complete finite Feynman–Dirac mechanism" — no class-operator completeness proof, no common carrier across bracketed histories (`audit/167_5_DIRECTIONAL_WITNESS_AUDIT.md`, Finding 1).

## The history eraser (RATCHET_188, `active/history_geometry.py`)

The `history_gram` function builds the finite coherent-history object directly: for each of the `2^n` bit-string histories over `nesting.edge_order`, it computes a phase-weighted branch amplitude `amplitude = exp(iφ)/√(len(histories))` applied to `history_path_state(...)`, stacks the branches into `branch_matrix`, and forms the **Gram/coherence matrix** `gram = branch_matrix.conj().T @ branch_matrix` (lines 36–49). This is the coherent-history object: its off-diagonal entries are the interference content, reported as `interference_frobenius = ||gram - diag(diag(gram))||`.

The eraser is the `erase_interference` flag on `history_gram`/`history_metric`: when `True`, it replaces the Gram matrix with only its diagonal, `gram = normalize_density(np.diag(np.diag(gram)))` (line 51) — i.e. it deletes the cross-history terms while keeping the per-history diagonal (the "which-history record"). `run_history_layer` then runs both `full` (coherent) and `erased` variants per nesting and checks that erasure actually changes the induced information geometry: `metric_change = ||full_metric - erased_metric||` and `coherence_removed`, gated by the check `erasing_interference_changes_metric` (lines 105–135). A companion check, `renesting_changes_history_geometry`, tests that changing the nesting topology (not just erasing records) also moves the induced metric — keeping "which regime" and "which geometry" as separately falsifiable axes.

The doc `WHAT_ACTUALLY_RATCHETED_186.md` describes this construction in prose: "The diagonal deletion removes interference and changes the BKM metric. The full coherent history state is retained. This does not prove a continuum Feynman path integral; it executes eight finite compatible paths for each three-edge nesting" (lines 86–89). The layer-depth ledger table names the object as "coherent history Gram state `G_hh'=<A_h ψ|A_h' ψ>`" with the entropy-side witnesses being "history entropy, record entropy, coherence and BKM," under the operational rule "amplitudes persist until record resolution," tested on "eight coherent histories plus erasures" (`EVERY_LAYER_EXPLICIT_MATH_AND_RUNTIME_188.md`, row 9). See [[concepts/entropic-geometry-one-object]] for the BKM-metric-as-Hessian law this Gram state feeds into.

Note the divergence in claim strength: 167.3/171/170 describe an unbuilt target contract (Gates 1–6, tournament FD0–FD7) for a Feynman–Dirac mechanism on the literal nested manifold. `history_geometry.py` (RATCHET_188) is a later, narrower, actually-executed instance of the same coherent-vs-erased pattern — a Gram-matrix coherent sum with a diagonal-deletion eraser and an entropy/metric response — but it is scoped to one nesting-family fixture, not the full bracketed/Dirac-carrier tournament those contracts specify. Whether 188's object satisfies 171's Gate 1–4 requirements (provenance hash, Dirac-carrier Clifford checks, geometry/flux/entropy separation) is not addressed in any of the read files.

## The gate contract

`170.../contracts/AXIS0_COHERENT_HISTORY_GATE.md` and `171.../contracts/FD_NESTED_HISTORY_CONTRACT.md` both govern admissibility, at different scopes:

- **AXIS0_COHERENT_HISTORY_GATE.md** blocks any implementation of the wider directional/Axis-0 candidate until two prerequisite receipts are sealed (`PASS_THREE_RUNTIME_CALIBRATION`, `SEALED_MULTI_LINEAGE_RATCHET_RECEIPT`); absent either, the required return is `HOLD_PREREQUISITE`. It requires eight comparator lanes (finite possibilistic extension, classical mixture, recorded/incoherent, coherent pre-readout sum, phase scramble, single-history deletion, order/bracket permutation, forward-shadow) and a mandatory deletion-witness table (perturbation-use, scenario-relabel, JK scramble, phase-scramble/recorded-history, etc.).
- **FD_NESTED_HISTORY_CONTRACT.md** is narrower and specifically Feynman–Dirac: Gate 0 (prerequisites), Gate 1 (complete-history semantics with provenance hash), Gate 2 (coherent-vs-recorded serialization of C_y, I_coherent, I_recorded, and the Gram block G_hh'), Gate 3 (Dirac/chiral carrier: D†=D, Γ²=I, {Γ,D}=0, no partial Clifford-relation credit), Gate 4 (geometry/flux/entropy kept as separate serialized fields, never renamed into one another), Gate 5 (target-blind evaluator — no `terrain`/`Feynman`/`Dirac`/`Hopf`/`spinor` labels fed as score features), Gate 6 (no premature partial-trace factorization by default). Verdicts are restricted to `PASS_COMPONENT`, `HOLD`, `FAIL`, `BLOCKED` — explicitly never `PASS_PHYSICS`, `Axis0 derived`, or `terrain architecture confirmed`.

Both contracts converge on the same claim ceiling: passing establishes a bounded mechanism-compatibility result on a finite fixture, never Axis 0, gravity, retrocausality, or the owner's literal ring-checkerboard/nested-Hopf cosmology (`AXIS0_COHERENT_HISTORY_GATE.md`, "Claim ceiling"; `PRIMARY_SOURCES_AND_BOUNDARIES.md`, "What this package intentionally does not infer").

## Open / unresolved

- No file in this set names an object called "bracketing registry" verbatim; the role is filled by the per-history `(h,b)` tuple plus provenance hash and the lane tags (coherent/recorded/scrambled/mixture/etc.), tracked as required serialization fields rather than as a single named registry structure.
- Whether `history_geometry.py` (RATCHET_188) satisfies the FD_NESTED_HISTORY_CONTRACT gates (Dirac-carrier Clifford checks, target-blind evaluator, provenance hash per history) is not stated anywhere in the read set — 188 is a later executed layer, not audited against the 171 contract in these files.
- 167.5's directional-witness audit found that its own "Axis-0" gates (`dynamic_damping_control_reconverges`, `dynamic_spreading_control_amplifies`) still returned `true` under a mutation that erased all state vectors, and that a declared perturbation (`compression_perturbation_outer_z2`) was unused by the runtime — a live warning, cited by 170's contract itself, that a coherent/incoherent-looking pass can be schedule-classification rather than dynamics (`167_5_DIRECTIONAL_WITNESS_AUDIT.md`, §5–6).
- The phase-functional question (which Θ[h] — turn/checkerboard, connection/holonomy, local-additive, spectral/Dirac, bracket-cocycle — is load-bearing) is explicitly left as an open competed tournament (FD3 in 167.3 §5; the table in `FEYNMAN_DIRAC_NESTED_WELD.md` §5), not resolved by any source read here.
- Sources disagree on how far along the ladder the project actually is: 167.3/171 describe FD0–FD7 and Gates 0–6 as not-yet-built target contracts; the GitHub audit finds only recorded-history code in the repo; the 188 pack shows an executed (but narrower) coherent-Gram-plus-eraser fixture. No file reconciles whether 188 counts as satisfying any specific FD stage or gate number.
