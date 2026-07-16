# CURRENT — v7 Campaign Restart Context (2026-06-14)

> **UPDATE 2026-07-10.** The estate moved to **Ratchet v0.3** (gradient drive; no-gradient-no-tooth),
> stamped **146/0/0** on the sim-stack rerun. The first receipt packet went through the full
> build -> audit-kill -> repair -> reopen loop. The `bundle_docs/` mirrors here were re-synced
> 2026-07-10 from `system_v7/constraint_core/docs/` (bare FORCED language superseded by scoped
> FORCED-WITHIN-GRAMMAR / CONSTRUCTIBLE-NOT-FORCED placements). Claim ceiling: scratch_diagnostic,
> promotion_allowed=false.

> **PURPOSE.** Boot a fresh thread (any LLM) into the v7 sim campaign. Read this + the §1 cited
> artifacts and you are current. This is the FRONT DOOR; it POINTS to canonical sources, it does
> not duplicate them (duplication drifts from reality). Status discipline: `exists < runs < passes
> local rerun < canonical by process`. Trust result-JSON over verdict prose. Nothing here is admitted
> above `scratch_diagnostic` / `passes local rerun` unless its cited artifact says so.

## 0. Operating doctrine (compressed)

- **ROOT.** One primitive = **constraint on distinguishability**; `a = a iff a ~ b` (identity is *earned*
  by probe-indistinguishability, not primitive). `F01` (finite simultaneous-distinguishability surface) +
  `N01` (**weak** noncommutation / order) operationalize it. **Finitude** load-bearing. **EXCLUSION-FIRST**:
  constraints *eliminate what cannot persist; they do not generate*. UNSAT is the primary proof form.
- **THREE root expressions** (never collapse): quotient `S/~_M` (elements) / noncommutation (order) /
  nonassociativity (grouping).
- **MSS — Minimal Survivable / Least-Admissible Evolvable Structure** (an admission META-GATE, *not* a root
  axiom, *not* ontology): admit only the **weakest** structure that survives the active constraints **and
  still evolves** (distinguishes / composes / continues / is killable). **Plural**: keep `Min(Surv(C))` — keep
  *incomparable* survivor branches live until a sim/proof kills one (anti-collapse at the base). No metric /
  time / cause / probability / identity / complex-Hilbert / geometry / spinor / manifold as a PRIMITIVE
  unless a prior admissible closure **forces** it (the "installed not forced" discriminator). Not Occam:
  Occam can pick a *dead* minimal thing; MSS requires *evolvable* survival.
- **BASE ORDER (corrected this session).** constraint-on-distinguishability → finite support `S` → probe
  family `P` → **probe-relative quotient `S/~_P`** inside `M(C) = (S, C, P, ~_P, Adm_C, composition/
  bracketing, readouts, controls, receipts)` → state functional `ω` → probe/update algebra → density matrix
  `ρ` **only if forced** (`ω(A)=Tr(ρA)` via GNS once the algebra is earned) → … → **spinors/quaternions =
  CLOSURE WITNESSES** (forced by sign/phase/lift/double-cover/holonomy/chirality closure, not primitive) →
  finite admissibility object `M(C)` is **EARLY**; *smooth geometric* manifold is **LATE**.
  - **LIVE FORK (do not collapse).** Reading A: the density-matrix quotient is the floor (today's GOLD sim).
    Reading B: the **bare** distinguishability quotient is weaker-and-surviving, and complex/Hilbert/`ρ` is
    *installed*. "**Is the complex/`ρ` carrier forced or installed?**" is the testable rung *below* today's
    floor (same discriminator that excluded quaternions). If B holds, GOLD is L2, not L1.
- **QUBIT-LADDER VALIDITY.** 1q runs and *should*, but is **not valid alone**; validity needs the ladder run
  to a declared useful depth **+ one beyond**. (gate: `scripts/validate_qubit_ladder_depth.py`)
- **MODEL FLEET.** codex2 = most solid (builder/arbiter); **Claude = orchestrator** (sole CR controller);
  grok / gemini / OpenRouter = **FINDERS** (advisory). **NO single-model trust** — validity needs a
  **multi-model cross-audit**. **Hallucination is a FEATURE** (variation) *given strict gates* (selection).
- **WIZARD = strict GATE + wide EXPLORER simultaneously** (the ratchet). **A** = defense-lawyer/retooler
  (old *slightly-bad* sims = feedstock; retool+rename to clean pure-math). **B** = prosecutor (assume every
  submission is an attempted **hack**). The gate is **adversarial**, and lexically strict (pure-math names;
  sim name must correlate with its actual math).
- **GATES are based on properly-defined axioms/constraints.** Target = the b_kernel **definedness fence**:
  admit only `L0` (19-lexeme allow-list) + admitted-term registry; reject bare `DERIVED_ONLY`; route
  `OVERLAY`/`JARGON`. (the current `validate_math_only_packet.py` is still a *blacklist* — see §2.)
- **MAINTENANCE.** The wizard maintains **git + wiki by default** (commit stable work, keep synced,
  restart-ready). **NEVER rebase.** Surgical explicit-pathspec commits only. **HERMES is INDEPENDENT**
  (audit-only; must not touch the CR repo/processes/commits unless the owner explicitly grants sim-control).

## 1. Canonical artifacts (read these; do not trust this summary)

**REPO `~/Codex-Ratchet`**
- Doctrine/foundations: `system_v6/foundations/fresh_llm_simulation_target_spec_20260615.md` (give-this-to-a-fresh-LLM sim target spec: axioms, constraints, variants, A/B gate/explorer, first sim queue); `root_axioms_v0_1_DRAFT.md`; `v7_gate_grounding_law_DRAFT_20260614.md`; `manifold_layer_order_and_completeness_contract_20260614.md` (14-box contract + canonical layer order); `manifold_layer_ledger_20260614.md`.
- Admission kernel (the law in code): `system_v4/skills/b_kernel.py` (7-stage UNDEFINED_TERM_FENCE) + `system_v4/skills/a1_brain.py` (`L0_LEXEME_SET`[19] / `DERIVED_ONLY_TERMS` / `OVERLAY_TERMS` / `JARGON_TERMS`)
- Gate stack: `scripts/validate_{v7_admission, math_only_packet, name_math_correlation, qubit_ladder_depth, smt_not_tautology, two_tier_authority, result_integrity, three_engine_sim_result, canon_firewall}.py`
- v7 sims: `system_v7/sims/{distinguishability_quotient_floor_v0` (GOLD 1q, passes-local-rerun), `finite_probe_quotient_inverse_limit_tower_1q_through_4q` (first nesting tower, passes-local-rerun), `axis0_terrain_engine_leap_v0` (BAD-twin negative fixture), `mixed_radix_endofunction_scc_terminal_quotient_under_z2_involution_v0` (REJECTED caught-hack fixture)}`
- Receipts: `system_v6/receipts/{v7_gate_grounding_fresh_audit, finite_probe_quotient_inverse_limit_tower_adjudication, first_reclamation_caught_hack_adjudication}_20260614.md`
- Commits (main): `a04d27773` caught-hack fixture · `b82e34a66` box-viii multi-model · `b859976e7` layer contract+ledger · `ae0af33c9` tower+ladder gate · `5b5883489` grounding law

**WIKI `~/wiki`**
- `projects/codex-ratchet/read-first.md` (front door) · this restart doc · `nested-ratcheted-manifold-hypothesis-research-workbench-2026-06-12.md` (the nesting-law workbench: §3 ratchet rule, §5 layer-modification table, §8 guard) · `concepts/geometry-stack-ratchet-doctrine.md`
- `claude-memory/sessions/` (per-thread logs) · `claude-memory/INDEX.md`

**CLAUDE MEMORY `~/.claude/projects/-Users-joshuaeisenhart-Codex-Ratchet/memory/`** (auto-loads each Claude thread)
- `MEMORY.md` index → `feedback_hallucination_is_feature_with_strict_gates`, `feedback_wizard_maintains_git_and_wiki_by_default`, `project_mss_and_corrected_base_order`, `project_v7_campaign_state_and_restart`, `reference_fleet_model_roster_verified_20260613`, `project_v6_dropped_the_admission_kernel`.

## 2. Current state (honest labels)

- **Layer ledger: NO layer is DONE.** L1 probe-quotient floor (GOLD) = `passes local rerun`, **1q-only → not valid-alone**. Tower L1→3 (+4q one-beyond) = `passes local rerun`. **Lego stage INCOMPLETE → no coupling / bridge / axis work licensed.**
- **Gate stack: built + axiom-grounded, but has KNOWN bypasses** the caught-hack proved: (1) the jargon scan misses `spec.json` *values* (jargon hides there); (2) `name↔math` MATH_VOCAB too shallow (only `quotient` checked — misnomers pass); (3) `name↔math` misses the nested `rungs` dict (fails laddered sims on present-but-undetected dims); (4) ground-constant-fold SMT slips `validate_smt_not_tautology.py`. → **mass-reclamation is BLOCKED until these are hardened.**
- **First reclamation = REJECTED caught-hack** (cosmetic relabel: jargon moved into `spec.json`, `load_bearing` inflated, engine-independence faked, object misnamed). The **multi-model cross-audit caught it; grok alone returned NO BYPASS**. The A/B mechanism is validated; the gate needs hardening.
- **Hermes interference (2026-06-14) resolved at source** — Hermes is now hands-off (canceled its CR tasks, hard-boundaried its skill). Its leftover working-tree edits to `AGENTS.md` / `CODEX.md` / `system_v5/codex_skills/*` / wizard schemas/tests are **untouched** (owner's call to keep/revert/leave).

## 3. Open tasks (priority order; tracked in the Claude task list)

1. **Harden the jargon / name↔math gates** — scan `spec.json` values; deepen MATH_VOCAB (catch misnomers); read nested `rungs`; catch ground-fold SMT. (The `mixed_radix` REJECTED fixture is the regression test.) *Blocks mass-reclamation.*
2. **Register** `name_math` + `qubit_ladder` into `validate_v7_admission.py` (serialize; was contaminated once).
3. **Ground the definedness fence** — invert `validate_math_only_packet.py` blacklist → `L0`+registry allow-list, **scoped to inputs/definitions not output keys**; prerequisite: build the **admitted-math-term registry** (L0=19 is too small alone).
4. **Formalize MSS** into `root_axioms` + a completeness-contract box (plural survivors, ρ-if-forced, Readings A/B held).
5. **Build the base sim** — `S/~_P` floor in `M(C)` *below* GOLD, with the **strength-preorder operationalized** (the real research nub) and the **forced-or-installed** discriminator (controls incl. commuting-update / probe-erase / label-shuffle / classical-baseline / overbuilt-carrier-ablation / density-matrix installed-vs-forced).
6. **Harden the tower to DONE** (correct the 4q forecast overclaim; add W4/boundary states; adversarial boundary-state injection; cross-engine partial-trace source audit).
7. **Mass-reclamation wave** (retool slightly-bad v6 → clean v7) — *only after* tasks 1–3.

## 4. Open forks (held — owner decides; do NOT collapse)

- Reading A vs B (density-matrix floor vs bare quotient; forced-or-installed).
- Root-sentence wording: relation-as-primitive (`v0`) vs constraint-as-primitive-with-`~_M`-as-local-form (`v0.1`).
- `load_bearing` definition: solver must *reason* vs authoritative-decision-procedure suffices.
- The **strength-preorder `A ⪯ B`** needs an operational/computable definition (`A` is a coarsening of / embeds in `B`?) — the base-sim research nub.
- MSS canonical name: "Least-Admissible Evolvable Structure" vs "Minimal Survivable Structure".
- Hermes leftover working-tree edits — keep / revert / leave.
- **Layer count/order is OPEN** (do not collapse): the committed contract's 15-numbered+6-gated vs the nesting-law spec's ~23 vs a finder-proposed 18-layer scaffold. Alternate counts, DAGs, partial orders all live.

## 4a. Candidate refinements (finder-sourced — UNVERIFIED, earn via sim before adopting)

Banked from a multi-model finder pass (GPT-webui), cross-audited; candidate-strength only, NOT canon:
- **Per-layer entropy-RESIDUAL as the lift-justification** (sharpens box xiii / the entropy co-ratchet): for each layer `L_k` with projection `π_k: L_k → L_{k-1}`, define residual `R_k = info in L_k not visible in π_k(L_k)`; **admit `L_k` only if `R_k` is load-bearing under active probes** (the lower layer must *lose* a distinction the constraints still need). Entropy = the ratchet PRESSURE that justifies lifting.
- **Five entropy forms** across the tower (entropy is not only at ρ): capacity (`log|S|`) / quotient (`log|S/~_P|`) / state (`S(ρ)`) / fiber-residual (`H(lift) − H(base)`) / cut-correlation (`I(A:B)`, Schmidt, `Φ0`).
- **Engines operationalize MSS** (vertical manifold × horizontal tri-engine grid; engines are the execution tribunal, NOT a layer): Julia = *is it defined?* (catches overdefinition) / JAX = *is it deformably stable?* (catches fake stability) / PyTorch = *does it dynamically carry?* (catches sterile formalism). Tri-engine gate = agreement OR explained divergence, **Julia Canon authoritative** (not co-equal senses).
- Rejected at root: Bekenstein/boundary-capacity framing (smuggled late physics; `log|S|` finitude is the legitimate capacity bound).
- **Geometric-ratchet LIFT CRITERION (the manifold = "presume less, lift only on failure"):** a layer `L_{k+1}` is admitted ONLY with a **failure-receipt** showing the weaker `L_k` cannot carry a required distinction/entropy/order/continuation; then admit the **weakest** stronger lift that fixes it. Standing test per layer: *"can a weaker object do the same job?"* — yes → demote; no → minimal lift + receipt. The weak-to-strong ladder (bare distinguishability → probe quotient → finite ordered update / QCA → GNVW/cut-entropy → state functional → density/operator if forced → projective/Hopf if phase/path erased → Weyl/spinor if sign/orientation load-bearing → Clifford/G-structure if closure demands → tensor/cut → Xi/rho_AB/Phi0 → smooth manifold/metric/time only as approximation). Canonical phrase: **"the manifold is the accumulated geometry of minimal survivors — the memory of what weak structure could not avoid becoming."** (geometric counterpart of the entropy-residual lift-rule; to fold into the ratchet definition doc + completeness-contract nesting box.)

## 5. How to restart (the discipline)

- **Fresh Claude thread:** `MEMORY.md` auto-loads and points here → read this + §1 artifacts → current.
- **Fresh non-Claude thread (codex/gpt/grok/gemini):** this wiki doc is the hub; read it + the §1 repo artifacts.
- **After each significant turn (standing maintenance):** update this doc (§2 state, §3 tasks, §4 forks), update Claude memory, append the `claude-memory/sessions/` log, and commit — wiki + repo, surgical, never rebase. "High maintenance of all" = this doc, the memory, and the repo stay synced and never drift from on-disk reality (verified by a fresh-context audit, not trusted).
