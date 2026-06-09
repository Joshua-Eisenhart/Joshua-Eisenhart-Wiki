last_updated: 2026-04-18
version: 1.0

# Project Dictionary — L3 Vocabulary Layer

Versioned constraint set of admitted project-specific terms. Each entry is grounded through probe + admissibility + quotient structure (see `16_dictionary.md` for the base method). If a term cannot be grounded this way, it is unsafe shorthand.

Base vocabulary layer: `16_dictionary.md` + `03_language_discipline.md`.  
Clause rewrites: `20_phrasebook.md`.  
This file is the project-specific extension of that base.

---

## Sim / Classification Terms

**lego**  
An atomic, independently testable math object. A lego is admissible when it survives shell-local probes in isolation, independent of any other lego. Not a metaphor — a modular unit whose boundaries hold under independence probes in M. A lego that requires another object to be defined is not atomic; split it.

**lego stage**  
The gate requiring all relevant lego rows in `system_v5/docs/17_actual_lego_registry.md` to carry at least one sim before coupling work opens. The lego stage is not negotiable by partial counts or "strong locals."

**coupling program**  
A sequence of six steps (shell-local → pairwise → multi-shell → topology-variant → emergence → bridge). A coupling program is admitted only when Steps 1–5 have closed; Step 6 (bridge/axis/engine) is excluded until then. Not a metaphor for "sim that touches two objects."

**canonical**  
Status label. Earned when: passes local rerun AND starts from SIM_TEMPLATE AND TOOL_MANIFEST has non-empty reasons for all tried tools AND TOOL_INTEGRATION_DEPTH has at least one `load_bearing` non-baseline tool AND classification field is set. Never set canonical from a single criteria; all must hold.

**classical_baseline**  
Classification for sims using numpy-era computation or no load-bearing non-baseline tool. A classical_baseline is not excluded — it is admissible as exploratory terrain. It is excluded from the canonical lane only.

**tool manifest**  
The TOOL_MANIFEST + TOOL_INTEGRATION_DEPTH fields in every sim. A sim without non-empty reasons for each tried tool is excluded from canonical classification regardless of other criteria. The manifest is a probe receipt, not documentation.

**load_bearing**  
Tool integration depth: the sim's conclusion materially depends on this tool. A tool is load_bearing when removing it changes the result, not just the code. `supportive` means useful but not decisive. `decorative` means present only at import level.

**stage gate**  
A hard ordering constraint. Stage gates are not processual checkpoints that can be softened — they are constraints that exclude downstream work while upstream work is open. Bypassing a stage gate is not a judgment call.

---

## Geometry / Structure Terms

**shell**  
A geometry layer with its own local support surface. A shell must be earned in its lane before it is imported into coupling sims. Shells are not nested Matryoshka dolls that stack automatically; they run simultaneously when co-active, and each must survive shell-local probes before coexistence is tested.

**manifold support**  
The local surface on which a shell's geometry is defined. Must be admitted before any operator or probe that presupposes it. Not silently imported.

**axis**  
A hypothesis space label, not a proven structure. Each axis names a candidate math cluster being tested. The axis label does not fix the math; surviving candidate maths within an axis become admissible under coupling constraint tests. Axes 0–6 are distinct hypothesis spaces for the individual engine.

Axes 7–12 are the proposed candidate math for the multi-instance interaction space — the geometry of how multiple engine instances couple and interact. "Instance" here is scale-neutral: AI agents, actual people, social groupings, and QIT engine instances are all admissible instance types once they reach agent-like coupling behavior. Not the MMM (language control plane) and not the Leviathan framework (social architecture) — three different aspects of the same multi-instance scale. Axes 7–12 are the math dimension; still open, no QIT-native contract yet.

**engine**  
A full Axis 0–6 structure. Not admissible as a claim until all lego stages, coupling programs, and coexistence tests for the relevant axes survive. Emergent when present — not assumed.

At scale, a QIT engine configuration surfaces agent-like coupling behavior — the engine becomes an instance that other engines interact with. Multi-engine configurations are admissible as "personalities" (distinct Axis 0–6 configurations coupling through Axes 7–12 candidate geometry). The individual/multi-instance boundary is probe-relative, not primitive.

**ratchet**  
The asymmetric directed constraint process. A ratchet step is admitted when a constraint is added that excludes previously surviving candidates without re-admitting excluded ones. Not a metaphor. The constraint chain is the ratchet; the irreversibility is structural, not narrative.

---

## Engine / Substrate Terms

**QIT**  
Quantum Information Theory. Treated here as the oracle side of the Turing machine analogy. QIT engines are not proven; they are candidate math streams. Super-sim convergence, if it arrives, must emerge from independent sims, not from framing.

**FEP**  
Free Energy Principle. Treated as literal physics mirror under this framing (predictive coding + allostasis). Not a metaphor for "the system tries to minimize surprisal." Specific FEP claims about error signals, generative models (a Bayesian technical term, not a banned verb), and action-perception loops must survive independent probes before admission into coupling work.

**holodeck**  
The projective co-generative system (project → sense → error-correct → hash). Co-generative with the engines, not downstream from them. Has its own lego catalogue; sims it independently.

---

## Harness / Process Terms

**harness**  
The full constraint infrastructure for shaping LLM completion topology. The harness is not a checklist; it is a constraint manifold on the LLM output space. Manifold-level harness files shape what completions are probable; instructions-on-manifold files issue rules that the training gradient fights. See `21_mimetic_meme_manifold.md`.

**MMM / mimetic meme manifold**  
The language/context control plane. Operates at any scale — individual LLM instance, fleet of agents, human social grouping. It reshapes what completions are probable by shaping the surrounding context/vocabulary, not by issuing instructions. The wiki harness is an MMM implementation for individual LLM instances.

Do not conflate with Axes 7–12. The MMM is the *language* dimension of any level; Axes 7–12 are the *geometric/mathematical* description of how multiple instances couple. Both operate at the multi-instance scale but are different aspects of it.

**Leviathan**  
The Leviathan company framework was built as a human social OS: shared community governance, Development Mirrors for people, membership language control, delegated proxy voting. In 2026-04-18 session it was recognized that the same architecture transfers directly to agent collectives (fleet governance, agent role differentiation, language manifold control). This is a transfer insight, not a claim that Leviathan was always about AI.

**probe family M**  
Finite resolution surface that licenses distinctions. Two objects are identical under M if no probe in M distinguishes them. Changing M changes identity. Never use identity claims without naming the active M.

**constraint set C**  
The active exclusion set. C excludes incompatible configurations; survivors remain provisional. UNSAT under C is the clean formal certificate. Empirical exclusion (failed probe) is weaker than formal exclusion.

**survivor**  
A candidate that passed all probes in M under constraint set C. A survivor is not confirmed; it is not excluded. Surviving alternatives must be listed.

**admitted / excluded**  
Primary vocabulary for constraint outcomes. Admitted = not yet excluded under C. Excluded = ruled out by probe or formal UNSAT. These are not binary final states — they are relative to the active C and M.

---

## Failure Mode Terms

Named failure modes surfaced by the harness audit. Each names a specific intercept target, not a personality criticism.

**narrative substitution**  
The generalized controller failure: a plausible story extracted from the rules, then obeyed in place of the rules. The story is indistinguishable from the rules under surface probe M_language; it is distinguishable under M_gate (does the cited result file exist?). Intercept: cite the specific gate criterion and the result file. If neither can be cited, the narrative is substituting for the gate.

**gate intercept**  
The procedure of pausing on a proposed action, naming the required gate criterion, and citing the result file that satisfies it. A gate intercept fires when the action feels like the obvious next step given the research narrative. Its output is either a cited file path (action admitted) or a block report (action excluded).

**gradient failure**  
A role-specific drift pattern driven by training-gradient pull. Each role has a distinct gradient failure surface: sim-worker promotes status labels; controller substitutes narrative for gates; Hermes executes on setup-only prompts; batch-runner treats queue entry as execution permission. Named in `23_role_boot_templates.md`. Not a moral failing — the completion probability under the training manifold.

**stage inflation**  
A downstream-stage claim admitted on upstream evidence. Example: claiming bridge/axis work is admitted because several lego sims survived. The inflation is the gap between what was tested and what is claimed. Intercept by step number: Step N status can only be admitted from Step N evidence, not Step N−1 evidence.

**label inflation**  
A status label applied in excess of the earned criteria. Example: writing `canonical` on a sim that passes local rerun but has no load_bearing non-baseline tool. Every label up the ladder has a specific admission criterion; stopping short of all criteria excludes the higher label regardless of how close the gap is.

**bounded exploration vs broad promotion**  
Two distinct activities at the coupling stage. Bounded exploration: pairwise/coexistence sims running off already-strong shell-local parents for feedback, with claims kept narrow. Broad promotion: widening coupling/coexistence/topology/emergence work into general stage-advancement claims. Bounded exploration is admitted during the lego stage; broad promotion is excluded until the lego stage closes across the registry.

**fleet**  
Multiple agent instances orchestrated through a controller (Hermes) and a runner (batch-runner). At fleet scale, L4 role-differentiated boot templates shape each instance; Axes 7–12 candidate math describes inter-instance coupling; the Leviathan framework provides the social architecture for role and authority differentiation. Fleet is the operational term; its formal analog is the multi-instance scale across all three aspects.

---

## Status Labels (ladder)

All four; never collapse or skip:

| Label | Meaning |
|---|---|
| `exists` | File is present in repo |
| `runs` | Executes without error (exit 0) |
| `passes local rerun` | Fresh run confirms all tests survive |
| `canonical by process` | passes local rerun + SIM_TEMPLATE + tool manifest with non-empty reasons + at least one load_bearing non-baseline tool + classification field set |

Never imply a higher label from a lower one. Never write "verified," "confirmed," or "all pass" without naming which criteria were checked and citing the result file path.

---

## Banned Project-Level Terms

Never use in sim code, result JSON, or worker prose:

- `proves` — use `survived constraints tested`
- `confirms` — use `survived probe M under C`
- `the correct X` — use `the admissible X under current C`
- `verified` — cite the status label and result path instead
- `all pass` — list which criteria C1/C2/... were actually checked
- `done` without result path — cite the file and status label
- `causes` / `creates` / `drives` / `produces` — see `03_language_discipline.md`

---

## See Also

- `03_language_discipline.md` — banned/preferred verbs, rewrite table
- `16_dictionary.md` — base noun grounding (probe, admissibility, candidate, etc.)
- `20_phrasebook.md` — clause rewrites
- `21_mimetic_meme_manifold.md` — manifold depth map and construction rule
- `19_grammar.md` — sentence patterns
- `SALIENCE_PREAMBLE.md` — injection-time manifold blocks
