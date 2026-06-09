---
title: Shell-Local to Shell-Coupled Research Program
created: 2026-04-08
updated: 2026-04-16
type: concept
tags: [simulation, planning, system, architecture, constraints, topology]
sources:
  - raw/articles/new-docs/CODEX_AUDIT_2026_04_08.md
framing: historical_worker_result_snapshot
---

# Shell-Local to Shell-Coupled Research Program

The next sim program: stop treating proposed layers as a fixed stack. Treat them as candidate constraint shells and test which objects are genuinely local versus only emerging under coupling.

## Conceptual Roles (not the same kind of thing)

These are different roles, not interchangeable terms:
- **Shell**: a candidate constraint surface (simultaneous, not sequential)
- **Lego**: a primitive object family (state, operator, probe, observable, entropy-like quantity)
- **Operator**: a channel/unitary acting on states within a shell
- **Probe**: a measurement/observation extracting information from a shell
- **Entropy**: a quantity that may be well-defined, trivial, or absent depending on shell + coupling

## Key Framing

Each candidate shell may admit some observables, probes, operators, and gradients while others may be trivial, absent, or only become meaningful under coupling or full nesting.

Not "each layer has an entropy." Instead: "which entropy-like quantities are genuinely local to a shell, which only emerge under coupling, and which are topology-sensitive?"

For geometry-stack claims specifically, the ratchet test is order-sensitivity/non-commutativity: commuting pairs are negative controls, while shell order matters only when swapping composition changes the admissible witness set.

## 5-Stage Program

### 1. Shell-Local Lego Sims
For each candidate shell, test which primitive objects are well-defined in isolation:
- State families
- Operators
- Probes
- Observables
- Entropy-like quantities

### 2. Pairwise Coupling Sims
Test which pairs of shell-local structures:
- Remain compatible
- Interact nontrivially
- Activate new quantities when coupled

### 3. Small Multi-Shell Coexistence Sims
Test which triples (and small N) of shells:
- Can coexist simultaneously
- Constrain each other
- Kill or create new observables

### 4. Topology-Variant Reruns
Rerun coupling/coexistence sims across different topology classes:
- Hopf tori
- Different fiber bundle structures
- Different carrier geometries
- Different geometry-depth / G-structure survivals

Identify: topology-stable vs topology-sensitive vs topology-emergent quantities.

### 5. Emergence Tests
Which entropy gradients, probes, and operators are:
- **Genuinely shell-local**: defined and meaningful in isolation
- **Coupling-dependent**: only discriminating when multiple shells active
- **Topology-sensitive**: depend on carrier geometry
- **Late-emergent**: only appear at full manifold depth (rho\_AB, xi, Phi0, Axis 0)

## Bridge Claims Come Last

Only after stages 1-5 produce results:
- rho\_AB (bipartite structure)
- xi (bridge object)
- Phi0 (seam quantity)
- Axis 0 (gradient field)

These are late objects, not primitives.

## Connection to Existing Work

- [[migration-registry]]: 28 families = shell-local legos (mostly stage 1)
- [[battery-index]]: negative tests = coupling failure modes (stage 2 boundary)
- [[pytorch-ratchet-build-plan]]: phases 4-6 = stages 3-5
- [[enforcement-and-process-rules]]: Rule 4 (build from foundations) + Rule 11 (presume less, test more)

## Program Status (2026-04-15, updated)

The large closure table below should be read with caution. It appears to summarize a worker/refinery wave of recent coupling-program pages, but it presently outruns the stricter evidentiary standard you stated here in chat: Claude has not yet run a proper non-classical sim campaign. So this table is useful as a lane map and hypothesis inventory, but should not be treated as settled canon by process.

**Recent coupling programs summarized here should therefore be read as high-entropy candidate/result synthesis unless and until their non-classical lane and controller-grade verification are independently re-established.**

Additional fence:
- this table is useful for routing and inventory
- it is not permission to treat the summarized shell/support/bridge relations as already admitted
- support-first doctrine still applies: `runs on`, coexistence, emergence, and bridge claims remain earned sim questions even when a worker/reporting surface summarizes them confidently

**Forty coupling programs summarized as apparently closed on a worker/reporting surface (not yet accepted here as final doctrine, final bridge closure, or final support-order law):**

In the table below, field values such as `valid`, `confirmed`, `worker-reported r=1.0`, `20/20`, and `worker-reported z3 UNSAT` are worker-reported packet strings. They are preserved as reservoir/context, not accepted repo proof.

| Program | Emergence Observable | Worker-reported bridge field, not accepted proof | Commit |
|---|---|---|---|
| MERA×Weyl×Hopf | Q₂ = I_c × H_chirality × Hol_phase | ρ_ABC worker-reported valid; Xi co-varies Q₂; Axis 0 gradient worker-reported | 9182b039 |
| Gerbe×Dirac×MERA | Q₃ = gap_shift × I_c_gradient × DD_class | ρ_GDM worker-reported valid; I_c co-varies Q₃; Axis 0 gradient worker-reported | ef6b6b07 |
| MERA×Clifford×Weyl | Q_MCW = I_c × H_clifford × H_chirality | ρ_MCW worker-reported valid; Clifford constraint: only XX/YY/ZI/IZ generators chirality-admissible | 0b524113f |
| Holographic×Clifford×Weyl | Q_HCW = I_c × H_clifford × H_chirality | ρ_HCW worker-reported valid; worker-reported Pearson r=0.978 (I_c vs Q_HCW); DPI gradient worker-reported | 90bdbe457 |
| SpectralTriple×Weyl×MERA | Q_STW = I_c × H_chirality × spectral_gap | ρ_STW worker-reported valid (64×64); worker-reported r(Q_STW,gap)>0.99; worker-reported Axis 0 gradient 20/20 seeds; topology: flat/ring/star worker-reported | b3dd36613 |
| Contact×Symplectic×MERA | Q_CSM = I_c × H_contact × H_symp | ρ_CSM worker-reported valid (64×64, torch.kron); worker-reported r>0.99; worker-reported Axis 0 20/20 seeds; H_contact=0 for degenerate form | d28c67c46 |
| Symplectic×Hopf×MERA | Q_SHM = I(A:B) × H_symp × H_hopf | ρ_SHM worker-reported valid; worker-reported r>0.99; worker-reported Axis 0 20/20 seeds; I(A:B)=MI (non-negative); H_hopf=log(2)/2 from π/2 holonomy | 2710e32ad |
| Gerbe×SpectralTriple×Clifford | Q_GSC = MI × H_gerbe × H_st | ρ_GSC worker-reported valid; worker-reported r=1.0 (Q linear in MI); local unitaries enforce MI monotone; chirality-admissible XX generator | a93e4f5e8 |
| Weyl×Gerbe×Hopf | Q_WGH = MI × H_weyl × H_gerbe × H_hopf | ρ_WGH worker-reported valid; worker-reported r=1.0; worker-reported Axis 0 20/20; 4-factor product; z3+sympy 4-factor zero | f3dbb7c5f |
| Dirac×Symplectic×Weyl | Q_DSW = MI × H_dirac × H_symp × H_weyl | ρ_DSW worker-reported valid; worker-reported r=1.0; MI starts 2log(2) for Bell; worker-reported z3 UNSAT H_weyl=0 | a930463ca |
| Holographic×Gerbe×Hopf | Q_HGH = MI × H_holo × H_gerbe × H_hopf | ρ_HGH worker-reported valid; worker-reported r=1.0; T2 AdS>T1>T3 hyperbolic; dQ/dMI>0 via autograd | 3cad05f22 |
| Contact×Clifford×MERA | Q_CCM = MI × H_contact × H_clifford | ρ_CCM worker-reported valid; worker-reported r=1.0; clifford+pytorch+z3+sympy load_bearing (4 tools); Cl(3,0) e12 chirality-admissible | e10141b63 |
| SpectralTriple×Contact×Gerbe | Q_SCG = MI × H_st × H_contact × H_gerbe | ρ_SCG worker-reported valid; worker-reported r=1.0; worker-reported 20/20 Axis 0; H_contact=log(17); H_gerbe seed-controlled | 70f41c656 |
| Dirac×Hopf×Clifford | Q_DHC = MI × H_dirac × H_hopf × H_clifford | ρ_DHC worker-reported valid; worker-reported r=1.0; worker-reported 20/20 Axis 0; `.grades()` is method not attr (bug fixed) | 73e38bda8 |
| Symplectic×SpectralTriple×MERA | Q_SSM = MI × H_symp × H_st | ρ_SSM worker-reported valid; worker-reported r=1.0; E1-E4 zero; pytorch autograd in Step 4; T1/T2/T3 pass | e2b9010c5 |
| Weyl×Contact×Dirac | Q_WCD = MI × H_weyl × H_contact × H_dirac | ρ_WCD worker-reported valid; worker-reported r=1.0; worker-reported 20/20 Axis 0; clifford+pytorch+z3+sympy load_bearing (4 tools) | fb9cee414 |
| Hopf×Symplectic×Clifford | Q_HSC = MI × H_hopf × H_symp × H_clifford | ρ_HSC worker-reported valid; worker-reported r>0.99; T1/T2/T3 lens space; H_hopf topology-variant (π/2, log2, π/3) | 3216c87b9 |
| Gerbe×Weyl×SpectralTriple | Q_GWS = MI × H_gerbe × H_weyl × H_st | ρ_GWS worker-reported valid; worker-reported r=1.0; H_weyl seed-independent; T2 S²: weight=1+1/π | 8e83348c9 |
| **QUINTUPLE** Weyl×Hopf×Gerbe×Dirac×MERA | Q_WHGDM = MI × H_weyl × H_hopf × H_gerbe × H_dirac | Zero in ALL 30 sub-4-shell combos; ≠0 only in full 5; N=5 product form worker-reported | 97fdc870 |
| Contact×SpectralTriple×Hopf | Q_CSH = MI × H_contact × H_st × H_hopf | ρ_CSH worker-reported valid; worker-reported r=1.0; worker-reported 20/20 Axis 0; float64 required (float32 causes hermitian test fail) | 62d03ae22 |
| Clifford×Gerbe×Symplectic | Q_CGS = MI × H_clifford × H_gerbe × H_symp | ρ_CGS worker-reported valid; worker-reported r=1.0; worker-reported 20/20 Axis 0; H_clifford=0.5 fallback (Cl(3,0) rotor if available); float64 required | 2a7705cd9 |
| Gerbe×Clifford×Contact | Q_GCC = MI × H_gerbe × H_clifford × H_contact | ρ_GCC worker-reported valid; worker-reported r=1.0; worker-reported 20/20 Axis 0; H_clifford=0.5 fallback; float64 required | 11af54818 |
| Weyl×Symplectic×MERA | Q_WSM = MI × H_weyl × H_symp × H_mera | ρ_WSM worker-reported valid; worker-reported r=1.0; worker-reported 20/20 Axis 0; H_weyl/H_mera=log(2); toponetx load_bearing in topology step | 98f4af019 |
| Hopf×Dirac×Contact | Q_HDC = MI × H_hopf × H_dirac × H_contact | ρ_HDC worker-reported valid; worker-reported r=1.0; worker-reported 20/20 Axis 0; H_hopf topology-sensitive (T1/T2/T3); H_dirac spectral gap seed=0 | 93488def8 |
| SpectralTriple×Symplectic×Hopf | Q_SSH = MI × H_st × H_symp × H_hopf | ρ_SSH worker-reported valid; worker-reported r=1.0; worker-reported 20/20 Axis 0; H_hopf topology-sensitive; Q_T2>Q_T1>Q_T3 ordering | 0518e2e65 |
| Dirac×Gerbe×MERA | Q_DGM = MI × H_dirac × H_gerbe × H_mera | ρ_DGM worker-reported valid; worker-reported r=1.0; worker-reported 20/20 Axis 0; H_dirac=0.337 (seed=0 gap); T2>T1>T3 DPI ordering | 89fbe7edb |
| Clifford×Weyl×Contact | Q_CWC = MI × H_clifford × H_weyl × H_contact | ρ_CWC worker-reported valid; worker-reported r=1.0; worker-reported 20/20 Axis 0; clifford load_bearing if importable; H_weyl topology-stable | adf121804 |
| Hopf×Symplectic×Gerbe | Q_HSG = MI × H_hopf × H_symp × H_gerbe | ρ_HSG worker-reported valid; worker-reported r=1.0; worker-reported 20/20 Axis 0; H_hopf topology-sensitive T3<T1<T2; H_symp/H_gerbe stable | 23663fee3 |
| SpectralTriple×Gerbe×Clifford | Q_SGC = MI × H_st × H_gerbe × H_clifford | ρ_SGC worker-reported valid; worker-reported r=1.0; worker-reported 20/20 Axis 0; clifford load_bearing in all 5 steps; H_clifford varies with θ | eaa2ff710 |
| Dirac×Contact×MERA | Q_DCM = MI × H_dirac × H_contact × H_mera | ρ_DCM worker-reported valid; worker-reported r=1.0; worker-reported 20/20 Axis 0; H_dirac spectral gap seed=0; all H topology-stable | 9144294b3 |
| Holographic×Dirac×SpectralTriple | Q_HDS = MI × H_holo × H_dirac × H_st | ρ_HDS worker-reported valid; worker-reported r=1.0; worker-reported 20/20 Axis 0; gap-fill: covers Dirac×Holo, Holo×ST, Dirac×ST pairs | c84419d04 |
| Holographic×Contact×Symplectic | Q_HCS = MI × H_holo × H_contact × H_symp | ρ_HCS worker-reported valid; worker-reported r=1.0; worker-reported 20/20 Axis 0; gap-fill: covers Holo×Contact, Holo×Symplectic pairs | e1455399e |
| Holographic×MERA×Clifford | Q_HMC = MI × H_holo × H_mera × H_clifford | ρ_HMC worker-reported valid; worker-reported r=1.0; worker-reported 20/20 Axis 0; gap-fill: covers MERA×Holo pair; H_clifford=e12 bivector (index [4] not [3]) | df2284322 |
| Weyl×Holographic×Symplectic | Q_WHS = MI × H_weyl × H_holo × H_symp | ρ_WHS worker-reported valid; worker-reported r=1.0; worker-reported 20/20 Axis 0; all H topology-stable; Q_WHS=0.167 at seed=0 | 139339bc3 |
| Contact×Holographic×Weyl | Q_CHW = MI × H_contact × H_holo × H_weyl | ρ_CHW worker-reported valid; worker-reported r=1.0; worker-reported 20/20 Axis 0; Q_T3<Q_T1<Q_T2 DPI ordering; rustworkx+xgi+toponetx supportive | eef9b0047 |
| Symplectic×Holographic×Dirac | Q_SHD = MI × H_symp × H_holo × H_dirac | ρ_SHD worker-reported valid; worker-reported r=1.0; worker-reported 20/20 Axis 0; DPI ordering Q_T3<Q_T1<Q_T2 | e863b5a3a |
| Hopf×Contact×Gerbe | Q_HCG = MI × H_hopf × H_contact × H_gerbe | ρ_HCG worker-reported valid; worker-reported r=1.0; worker-reported 20/20 Axis 0; Q_T3<Q_T1<Q_T2 topology-sensitive H_hopf | 7ab7aaa73 |
| SpectralTriple×Dirac×Symplectic | Q_SDS = MI × H_st × H_dirac × H_symp | ρ_SDS worker-reported valid; worker-reported r=1.0; worker-reported 20/20 Axis 0; all H topology-stable; H_st=gap(seed=1)≈0.025 | 1b54176d2 |
| Weyl×Dirac×MERA | Q_WDM = MI × H_weyl × H_dirac × H_mera | ρ_WDM worker-reported valid; worker-reported r=1.0; worker-reported 20/20 Axis 0; all H topology-stable; H_weyl=H_mera=log(2) | 2640fa35a |
| Clifford×Holographic×Dirac | Q_CHD = MI × H_clifford × H_holo × H_dirac | ρ_CHD worker-reported valid; worker-reported r=1.0; worker-reported 20/20 Axis 0; H_clifford=0.383 (Cl(3,0) e12 θ=π/4); all topology-stable | eaf279233 |
| Symplectic×SpectralTriple×Weyl | Q_SSW = MI × H_symp × H_st × H_weyl | ρ_SSW worker-reported valid; worker-reported r=1.0; worker-reported 20/20 Axis 0; all H topology-stable; autograd dQ/dMI worker-reported | 1252ac950 |

**Worker-reported pairwise coverage: 45/45 pairs covered** (all C(10,2) unique shell pairs appear at least once across the 40 programs. Gap-filled 2026-04-15: MERA×Holo, Dirac×Holo, Holo×ST, Dirac×ST, Holo×Contact, Holo×Symplectic.)

**Worker-reported invariants across all forty programs:**
- All emergence observables = 0 for every single shell and every pairwise combination
- All emergence observables ≠ 0 only in the full shell combination
- Axis 0 gradient dI_c/dlayer < 0 is worker-reported in all three Step 6 bridge-claim rows
- Topology-agnostic: DPI holds on flat torus, sphere, twist (topology variant step)
- worker-reported z3 UNSAT is the worker-reported proof form in the Step 6 packet rows; current repo acceptance remains separate

| Stage | Status on this page | Key evidence |
|---|---|---|
| 1. Shell-local lego sims | worker-reported complete | 150+ worker-cited candidate canonical sims across L1-L5, G-tower, TN, Clifford, symplectic |
| 2. Pairwise coupling sims | worker-reported complete | layer_coupling_matrix worker-cited canonical (13/13); SU3×Sp6 pairwise; spectral-triple×Weyl |
| 3. Multi-shell coexistence | worker-reported complete | triple coexistence catalog done; layer triple catalog complete; **Hopf+Weyl+torus triple coexistence 19/19** (f2568ce6): 270 joint-admissible states < 288 pairwise min — each shell strictly restrictive; η=π/4 is max-coexistence point |
| 4. Topology-variant reruns | worker-reported complete | Hopf tori, spinor torus MPS (14/14), Berry phase on S² (15/15); **sim_hopf_weyl_torus_topology_variant** (12/12, c6fec9d9): ratio=7.41 (flat:2000 vs round:270). Holonomy shell = topology-sensitive; Weyl-L = topology-stable. worker-reported z3 UNSAT: round-torus coexistence structurally impossible on T². |
| 5. Emergence tests | worker-reported complete | Arrow-of-time asymmetry L1->L3 (15/15 UNSAT); I_c sign emergence worker-reported; **sim_hopf_weyl_emergence_quantities** (7/7, 2973f61d): Q1 = P_L(Hol psi) - Hol P_L(psi) has reported norm 0.791 in joint shell, exactly 0 for each shell alone; topological chirality charge Q2 != 0 only when holonomy mixes grades; joint entropy sub-additive (S(joint)=0.289 < S(Hopf)+S(Weyl)=1.076); Q1 antisymmetric CW/CCW; topology-sensitive (zero on flat torus). |

**Bridge-gate note:** this worker/result surface reports a step-6-ready picture, but that should still be treated here as high-entropy candidate/result synthesis rather than as final accepted gate closure.

## What This Changes

Prior state: most sims were shell-local (stage 1). Coupling sims were sparse.

Current state on this page: all 5 stages are summarized as worker-reported complete. That is useful for routing, but this page should still be read as candidate/result synthesis until the stricter non-classical verification lane is independently re-established.

Interpretation fence:
- do not read the worker-reported completion rows here as a proof that the support order is settled
- do not let this page outrank narrower truth-audit, artifact, or controller-status surfaces
- use this page to see which hypotheses and reported packets exist, then route down to the narrower evidence pages before promotion

**Open bridge work (step 6):**
- Canonical Ξ bridge sim (z3/cvc5 UNSAT as primary proof form)
- A|B cut specification candidate canonical sim
- Shell/history unification proof

**Previously noted**: SHELL\_COUPLING\_PROGRAM.md referenced in LLM\_CONTROLLER\_CONTRACT.md does not exist as a standalone file. That gap remains. The worker/reporting surface described the sims as complete; repo acceptance remains unproven here.

## Related Pages

- [[constraint-surface-and-process]] — constraint manifold theory
- [[formal-constraints-and-geometry]] — strict split between constraints, manifold, and carrier
- [[aligned-sim-backlog-and-build-order]] — build ordering
- [[codex-audit-controller-contract]] — controller contract for running this program
