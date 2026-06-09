# Harness-Consolidated Nominalist Steering Audit

Scope read:

- Markdown surface: every non-archive `.md` file under `/Users/joshuaeisenhart/wiki/wizard/harness-consolidated/`, 53 files, 4,814 lines.
- Probe surface: every `.py` file under `/Users/joshuaeisenhart/wiki/wizard/harness-consolidated/probes/`, 15 files, 2,876 lines.
- Comparison surface: `/Users/joshuaeisenhart/wiki/hermes-current/active-intentions.md`, plus the active v4.3 object-preservation pointer/spec/validator enough to check awareness.

High-level finding:

The harness is not empty or merely decorative. It has strong, repeated steering against primitive identity/equality, status inflation, causal verbs, construction/proof language, skip-ahead coupling, and unbounded closeout. Its strongest operational layer is the pre-emit/status/bounded-work/closeout/Z3 cluster.

It is also stale in important ways. The consolidated harness does not appear to know about the v4.3 object-preservation preflight guard. Several sim/tool files still encode the old PyTorch-as-ratchet framing, while the current repo authority says JAX and Julia are primary nonclassical engines and PyTorch is sidelined except as legacy/comparison/helper evidence. The harness is also much stronger against primitive identity and causal wording than against primitive geometry, time, probability, and support/carrier/coexistence smuggling.

2026-06-04 carrier caveat: PEPS3D/CTMRG references below are stale relative to the 2026-06-03 session handoff. CTMRG/PEPS3D is retired as a load-bearing carrier. Current carrier routing is ITensors-MPS, exact dense/TensorKit, QuantumClifford, and spinor-native trajectories, with JAX and Julia primary in parallel. This dated note fences the stale harness-doctrine references without rewriting the whole audit.

## 1. LOAD-BEARING STEERING RULES

| # | File + line range | Rule in one sentence | What it prevents | Operational? |
|---|---|---|---|---|
| 1 | `SALIENCE_LOADER.md:8-18` | Start every session from the axiom that objects do not exist as primitives and only distinction under a finite measurement can be used. | Primitive object identity, bare equality, entity-first reasoning. | yes |
| 2 | `SALIENCE_LOADER.md:20-28` | Every admissible statement must identify a measurement/salience model `M`, an admissibility test under constraints `C`, and a quotient/survivor shape. | Untethered claims, true/correct language, objects treated as prior to probes. | yes |
| 3 | `SALIENCE_LOADER.md:30-44` | Use the explicit status ladder and preferred claim grammar instead of truth/proof/solution language. | Status inflation and completion-like claims without receipts. | yes |
| 4 | `SALIENCE_LOADER.md:46-65` | Forbid primitive identity/causality/correctness and run a pre-emit check before output. | Causal-default wording, equality smuggling, smooth prose that erases constraints. | yes |
| 5 | `SALIENCE_PREAMBLE.md:15-51` | Inject root axiom, status ladder, claim pattern, and manifold-support wording before agent work. | Subagents starting from ordinary object/causal ontology. | yes |
| 6 | `00_READ_FIRST.md:50-61` | A statement is admissible only when it names observation/operator, constraint, witness/bound, and status label. | Unsupported claims entering the harness as facts. | yes |
| 7 | `READ_POLICY.md:5-15` | Always load salience, core, language, phrase, bounded-work, and status files before using the harness. | Agents reading isolated files and losing root steering. | yes |
| 8 | `BOOT.md:12-48` | Select a boot tier by task risk and include the required harness files for that tier. | Overloading small tasks or under-priming high-risk tasks. | yes |
| 9 | `01_nominalism_primer.md:25-41` | Convert "does this exist?" into "what distinction survives which observation or intervention?" | Object-first ontology and existence-as-default reasoning. | no |
| 10 | `02_constraint_admissibility_primer.md:5-26` | Treat constraints as eliminators and impossibility as stronger evidence than constructive success. | Construction-first or causal-production framing. | no |
| 11 | `02_constraint_admissibility_primer.md:35-51` | Sim output tests a constraint boundary and is not truth unless the impossible alternative is eliminated. | Simulation success promoted into proof/truth. | yes |
| 12 | `03_language_discipline.md:17-46` | Prefer survival/admissibility/divergence verbs and ban proves/causes/builds/optimizes verb frames. | Causal and constructive grammar smuggled into reports. | yes |
| 13 | `03_language_discipline.md:49-75` | Rewrite primitive claims into observation/operator/constraint/status forms and check each sentence before emission. | Smooth prose that hides missing witnesses or status. | yes |
| 14 | `04_status_label_hierarchy.md:7-24` | Use only `possible`, `not eliminated`, `survives constraints`, and `admitted`, and never infer upward. | "Validated", "verified", "true", "all pass" drift. | yes |
| 15 | `04_status_label_hierarchy.md:26-38` | If result criteria are absent, stop rather than assigning status. | Completion-like claims from missing evidence. | yes |
| 16 | `05_four_sim_kinds.md:7-35` | Classify sims as classical baseline, nonclassical operator/interface, scaffold, or meta-sim. | Classical/scaffold results being mistaken for nonclassical evidence. | yes |
| 17 | `05_four_sim_kinds.md:37-49` | Block nonclassical claims until tool capability and integration are shown. | Backend label overclaim and interface-only nonclassical claims. | yes |
| 18 | `06_coupling_program_order.md:7-12` | Enforce the sequence from isolated shell operations through cross-shell coupling before bridge/axis claims. | Skip-ahead from local sim to bridge/manifold conclusion. | yes |
| 19 | `06_coupling_program_order.md:44-59` | A coupling claim must cite the result for each prior stage or report the missing gate. | Uncited bridge/coupling promotion. | yes |
| 20 | `07_z3_unsat_primacy.md:5-19` | Prefer UNSAT impossibility results over SAT examples for harness steering. | Example-finding being treated as structural proof. | yes |
| 21 | `07_z3_unsat_primacy.md:40-47` | Do not claim a Z3 result is load-bearing unless it is integrated into sim/admission logic. | Decorative formal methods labels. | yes |
| 22 | `08_anti_patterns.md:9-55` | Name and reject accuracy, process, language, and operational anti-patterns. | Common drift patterns such as result laundering, status inflation, and hidden skips. | yes |
| 23 | `09_perspectival_rotation.md:43-49` | Keep divergent narratives as candidates, translate them to local observables, and let constraints eliminate. | Single-narrative smoothing and premature unification. | no |
| 24 | `12_f01_n01_nominalist_axioms.md:9-36` | Reduce harness rules to bounded finite observation (`F01`) and order-sensitive noncommutation (`N01`). | Unbounded exploration, order-insensitive summaries, and convention mistaken for evidence. | yes |
| 25 | `12_f01_n01_nominalist_axioms.md:40-47` | Do not couple shells until each shell has a bounded local witness. | Cross-stage coupling before local evidence. | yes |
| 26 | `13_mandatory_pushback.md:9-37` | Push back when the user requests skipped steps, stronger status, premature nonclassical launch, or broad queued work. | Compliance-driven overclaiming and skipping gates. | yes |
| 27 | `13_mandatory_pushback.md:44-47` | Obedience is not alignment when the request contradicts ordering constraints. | RLHF-style agreement with invalid route shape. | no |
| 28 | `15_root_axiom_card.md:5-16` | Identity is probe-relative and statements must name the probe relation, negative contrast, and status. | Bare sameness/equality and absent negative controls. | yes |
| 29 | `16_dictionary.md:7-20` | Expand harness nouns into observation, constraint, witness, and status before using shorthand. | Shorthand becoming unearned ontology. | yes |
| 30 | `17_pre_emit_audit.md:11-22` | Each sentence must pass six axes: measurement, constraints, quotient, status, divergence, and no banned construction verbs. | Primitive identity, status inflation, smoothing, and constructive/causal verbs. | yes |
| 31 | `17_pre_emit_audit.md:26-49` | Use canonical grammar for claims, status, negative claims, and disagreements; fail if any sentence needs smoothing. | Human-friendly prose that hides missing receipts. | yes |
| 32 | `17_pre_emit_audit.md:75-91` | Treat primitive claims, causal verbs, missing status, missing divergence, and normalized disagreements as failures. | Ontology drift after drafting. | yes |
| 33 | `18_red_team_probes.md:7-19` | Before output, ask whether the statement names `M`, `C`, status, eliminated alternatives, and avoids shorthand. | Final-answer drift that survived first drafting. | yes |
| 34 | `19_grammar.md:7-35` | Use canonical statement shapes and demote any sentence that cannot instantiate them. | Object-first, winner/loser, and final-answer grammar. | yes |
| 35 | `20_phrasebook.md:7-38` | Replace existence/identity/causality/proof phrases with probe/admissibility/divergence/status phrases. | Default ontology and causal/truth phrasing. | yes |
| 36 | `21_mimetic_meme_manifold.md:82-125` | Score language through correction, drift, completion, and gap probes before treating it as harness-steering language. | Untested style being mistaken for actual steering. | yes |
| 37 | `21_mimetic_meme_manifold.md:174-187` | Prefer constructors that preserve existing harness meaning and make drift measurable. | New language patches that feel aligned but do not steer. | yes |
| 38 | `22_project_dictionary.md:16-39` | Force sim terms to retain classification, result, witness, and elimination boundaries. | Sim output being treated as general proof. | yes |
| 39 | `22_project_dictionary.md:44-61` | Treat geometry/manifold/axis/engine/ratchet terms as support or stage labels, not primitive objects. | Geometry and axis labels promoted before support evidence. | yes |
| 40 | `22_project_dictionary.md:91-101` | Define probe family, constraint, survivor, and admitted as distinct terms. | Candidate/survivor/admission collapse. | yes |
| 41 | `22_project_dictionary.md:132-158` | Preserve status labels and ban terms such as verified, validated, true, optimal, and solution. | Status and truth inflation. | yes |
| 42 | `23_role_boot_templates.md:13-23` | Bind each agent role to a primary failure mode and mandatory harness files. | Generic agents applying the wrong steering layer. | yes |
| 43 | `23_role_boot_templates.md:26-106` | Give sim worker, controller, Hermes, and batch runner role blocks with explicit forbidden claims. | Role-specific drift, especially sim promotion and queue/status errors. | yes |
| 44 | `24_closeout_templates.md:19-47` | Require closeout blocks for task, scope, files, commands, strongest/weakest result, status, boundary, and next safe move. | "I did X, therefore Y is done" closeouts. | yes |
| 45 | `24_closeout_templates.md:75-97` | Closeout must preserve branch status, dead routes, and authority order rather than narrating progress. | Graveyard erasure and forward-plan laundering. | yes |
| 46 | `25_adversarial_drift_probes.md:11-19` | Test harness language with adversarial probes and score drift before accepting updates. | Unmeasured steering claims. | yes |
| 47 | `25_adversarial_drift_probes.md:198-213` | Mark output failed when it starts from object/cause, inflates status, skips gates, or lacks pushback. | Agent answers that sound aligned but still drift. | yes |
| 48 | `26_completion_stems.md:5-17` | Use completion stems as a language-drift probe, not as doctrine. | Mistaking generated completions for harness truth. | yes |
| 49 | `26_completion_stems.md:105-124` | Score completions on nominalist framing, status discipline, gate ordering, pushback, and branch preservation. | Low-energy default completions entering boot. | yes |
| 50 | `27_ambient_topology.md:56-74` | Treat language, templates, failure cases, and probes as support topology and test whether a rule changes output. | Instructions-only edits with no steering effect. | yes |
| 51 | `28_bounded_work.md:32-44` | Every work unit must specify object, allowed move, forbidden move, exit condition, and required status. | Skip-ahead and unbounded task expansion. | yes |
| 52 | `28_bounded_work.md:102-123` | A unit is valid only if it has a local observable, forbidden downstream move, exit condition, and admission-pool interpretation. | Ordered-pipeline fantasies and downstream promotion. | yes |
| 53 | `29_harness_edit_protocol.md:17-40` | Harness edits must be bounded work units with target drift, allowed edits, forbidden edits, and exit conditions. | Broad harness rewrites that dilute steering. | yes |
| 54 | `29_harness_edit_protocol.md:55-64` | Aggregator success is the primary formal edit gate and manual green checks are only support. | Self-certified harness improvements. | yes |
| 55 | `29_harness_edit_protocol.md:115-155` | External-audit-first edits must make the outside criticism load-bearing before changing doctrine. | Editing to satisfy vibes rather than witnessed failures. | yes |
| 56 | `30_z3_harness_formalization.md:44-59` | Formalize status, pre-emit, bounded work, coupling order, and closeout as first-order encodings. | Principle-only harness claims. | yes |
| 57 | `30_z3_harness_formalization.md:85-94` | Favor UNSAT counterexample elimination over SAT witness search. | Positive examples as proof of discipline. | yes |
| 58 | `30_z3_harness_formalization.md:98-143` | State explicitly what the formalization does not prove. | Aggregator success inflated into full harness admission. | yes |
| 59 | `31_admission_surface.md:140-158` | Admission-surface results witness only encoded predicates, not semantic truth or full nominalism. | "Green suite means correct harness" drift. | yes |
| 60 | `32_mmm_word_ratchet.md:27-64` | Admit words only if they respect no primitive identity/story-causality and give a contamination audit. | Word-level ontology drift in boot packets. | yes |
| 61 | `32_mmm_word_ratchet.md:282-291` | New mini-MMM language must be extracted through intended steering, drift risk, test stems, fingerprint shift, and provenance. | Unchecked language imports. | yes |
| 62 | `34_mmm_research_reservoir_map.md:9-22` | External research is a reservoir, never authority, and must be filtered through the root constraints. | Importing outside ontology as doctrine. | yes |
| 63 | `34_mmm_research_reservoir_map.md:87-112` | Audit research language for hidden identity before using it. | Equivalence/object smuggling from external traditions. | yes |
| 64 | `34_mmm_research_reservoir_map.md:349-380` | Copy no outside framework directly; extract only output-changing steering candidates and test them. | Mimetic imitation and decorative citations. | yes |

## 2. STALE OR REDUNDANT

- `README.md:5-9` and `README_CONSOLIDATED_BY_WIZARD.md:15-23` still describe the harness as a support copy for older Wizard routing, including v3.4-era language. That provenance is useful, but it is not current runtime authority.

- `README.md:59` says Codex runtime authority lives in `CLAUDE.md` plus system docs. Current repo authority says `AGENTS.md` and `CODEX.md` are Codex authority, while `CLAUDE.md` is reference doctrine only. This should be corrected or fenced as historical.

- `21_claude_working_memory.md:15-25` references old Wizard paths and a Claude-specific read order. It is useful provenance for Claude lanes but stale as a Codex harness boot rule.

- `10_owner_doctrine_index.md:22-57` points into `.claude/projects/...` memory and old tool/sim framing. It should remain a provenance index, not a current authority surface.

- `11_pytorch_as_ratchet.md:3-47`, `05_four_sim_kinds.md:37-49`, `10_owner_doctrine_index.md:49-53`, `23_role_boot_templates.md:26-44`, and `z3_sim_tool_manifest_completeness.py:1-46` preserve the old PyTorch/tool framing. Current repo authority says JAX and Julia are primary for nonclassical execution; PyTorch is sidelined except as legacy evidence, explicit comparison/mirror output, or bounded helper with a real ablation.

- `01_nominalism_primer.md:11-17` says "Statistics IS causality." That conflicts with the active intention that probability and causality must not be smuggled in as primitive ontology, and that causal language is downstream and conditional.

- `09_perspectival_rotation.md:35-39` uses "same invariant" and "THE SAME THING" as explanatory language. That is rhetorically useful but risky under the current no-primitive-identity requirement.

- `00_READ_FIRST.md:13-44` defines a boot order through file `30`, while files `31` through `34` now exist and include admission/word-ratchet/research-reservoir material. The front-door boot is stale relative to the consolidated directory.

- `BOOT.md:4` says it supersedes `READ_POLICY.md`, but `00_READ_FIRST.md:40-44`, `README.md:13-24`, and `SALIENCE_LOADER.md:66-70` still route through `READ_POLICY.md`. The two surfaces overlap and should either be merged or clearly separated.

- Several formalization/status lines have stale suite counts: `21_mimetic_meme_manifold.md:68`, `30_z3_harness_formalization.md:61`, `30_z3_harness_formalization.md:173-180`, `31_admission_surface.md:9-10`, `31_admission_surface.md:140-158`, and `audit_response_closeout_2026_04_18.md:20-22`. The actual `harness_precommit.py:47-59` suite list has 11 suites.

- `dogfood_session_2026_04_18.py:1-19` explicitly marks itself as historical and superseded as a current closure proof. It still runs, but should not be cited as current harness health except as provenance.

- `ASSESSMENT.md`, `AUDIT.md`, `PROBES.md`, `PUSHBACK.md`, `SPAWN.md`, and `TRANSLATION.md` are compact routers that mostly point to deeper files. They are redundant but may still be useful as low-cost entrypoints.

- `dictionary_v0.md:1-53` is provisional and placeholder-heavy. It should not be treated as a steering rule when `16_dictionary.md` and `22_project_dictionary.md` exist.

- Direct `python3 probes/cvc5_cross_check.py` fails in the system Python because `cvc5` is not installed there. It passes with the repo interpreter used by `harness_precommit.py`. The docs should be explicit about the required interpreter if direct probe invocation remains expected.

## 3. GAPS - MISSING STEERING

### Gap 1: Primitive geometry, time, and probability are weaker guards than primitive identity

What is missing: The harness strongly blocks primitive identity, equality, causality, construction, proof, and status inflation. It does not equally mechanize "no primitive geometry", "no primitive time", or "no primitive probability". Geometry appears in `22_project_dictionary.md:44-61` as a term to ground, but it is not a pre-emit axis. Probability appears positively in `32_mmm_word_ratchet.md:37` and `34_mmm_research_reservoir_map.md:199-218`; that material is useful only if it is explicitly treated as non-primitive, downstream, and support-conditioned.

Where it should go:

- Add a seventh/eighth pre-emit axis to `17_pre_emit_audit.md` for geometry/time/probability smuggling.
- Add rewrite rows to `19_grammar.md` and `20_phrasebook.md`.
- Add drift-word entries to `32_mmm_word_ratchet.md`.
- Add a formal/string probe beside `z3_pre_emit_six_axis.py`, or extend it if the encoding stays boolean.

### Gap 2: Causal language is banned, but downstream conditional causality is not specified

What is missing: The harness bans causal verbs and primitive causal statements, but it does not give a narrow admissible form for downstream causal language. Active intentions require causal language to be conditional and downstream, not absent by taboo alone.

Where it should go:

- Add a "conditional causal claim" grammar to `03_language_discipline.md` and `19_grammar.md`.
- Add examples to `20_phrasebook.md`, e.g. "under receipt R and carrier C, intervention I changes observable O relative to negative control N; no broader causal ontology is claimed."
- Extend `17_pre_emit_audit.md` with a causal-ceiling check: any causal word must cite downstream receipt, carrier/support, negative control, and blocked overclaim.

### Gap 3: Support-first/manifold-first is not first-class enough

What is missing: The current harness has support language, especially `22_project_dictionary.md:47-49`, but it lacks a universal rule that "runs-on", support, carrier, coexistence, and manifold support are sim questions earned before later operators. The old coupling ladder is useful but too tool/stage-shaped and not enough carrier/support-shaped.

Where it should go:

- Add a new support-first preflight, either as `35_support_first_preflight.md` or as a section in `28_bounded_work.md`.
- Update `23_role_boot_templates.md` so sim workers and controllers must name carrier/support/coexistence before later operators.
- Update `17_pre_emit_audit.md` to fail later-operator claims that lack support/carrier/coexistence receipts.
- Add a support-first Z3/string probe or extend `z3_coupling_gate_ordering.py`.

### Gap 4: Fail-closed exists for status, but recon/admission separation is not explicit enough

What is missing: The closeout and status layers preserve branch status and prevent forward-plan laundering, but they do not consistently require a separate "recon only" vs "admission decision" field. Active intentions specifically say to keep recon separate from admission.

Where it should go:

- Add explicit `recon_artifacts` and `admission_decisions` fields to `24_closeout_templates.md`.
- Add role-specific instructions in `23_role_boot_templates.md` for scout/recon workers.
- Add a closeout-shape probe ensuring recon files are not cited as admission unless an admission field is present.

### Gap 5: Sim steering is stale relative to current repo authority

What is missing: The sim harness still mostly talks in old PyTorch/tool capability terms. Current repo authority requires new nonclassical manifold work to start from explicit finite F01/N01 carrier/probe/operator/path sets, JAX- or Julia-native spinor state or explicit carrier tensor, finite PEPS3D carrier anchor from the first admitted carrier step, negative/control condition, receipt path or blocked-reason artifact, and blocked downstream consumers. The harness does not encode that current shape.

Where it should go:

- Replace or heavily amend `11_pytorch_as_ratchet.md`.
- Update `05_four_sim_kinds.md` and the sim-worker block in `23_role_boot_templates.md`.
- Update `22_project_dictionary.md:55-58` to reflect current JAX/Julia/PyTorch boundaries.
- Extend `z3_sim_tool_manifest_completeness.py` or add a new sim contract probe for F01/N01, JAX/Julia carrier, PEPS3D anchor, negative controls, source hash/staleness, and blocked consumers.

### Gap 6: v4.3 object-preservation guard is absent from harness-consolidated

What is missing: A search for `v4.3`, `object preservation`, `preflight guard`, and `repo validator` in `harness-consolidated` found no hits. Active wiki and repo surfaces say the v4.3 object-preservation guard is an additive preflight before v4.2 when novel objects, salience drift, proxy drift, or shell-model work are in play. The active spec requires a primary object card, typed lateral mappings, root/extended constraint separation, wildcard/fixation-breaker, and evidence spine.

Where it should go:

- Add a pointer in `00_READ_FIRST.md`, `README.md`, and `READ_POLICY.md`.
- Add a role block to `23_role_boot_templates.md` for object-preservation preflight.
- Add a short new harness file that points to the repo-held authority without inventing `packet-v4-3-current`.
- Add a probe that validates the presence of a v4.3 object card for applicable tasks, or points to `scripts/wizard_v4_3_object_preservation.py`.

### Gap 7: Negative controls and graveyard honesty are present but not central

What is missing: Negative contrast appears in `15_root_axiom_card.md:13-16`, and closeout preserves weak/dead branches in `24_closeout_templates.md:75-97`, but "negative-control-heavy" and "graveyard-honest" are not universal sim/report fields.

Where it should go:

- Add required `negative_controls`, `graveyard_companions`, and `killed_or_blocked_candidates` fields to sim and closeout templates.
- Add drift probes to `25_adversarial_drift_probes.md` that fail when only positive/survivor evidence is reported.
- Extend `z3_closeout_completeness.py` or add a sim-result-shape probe.

### Gap 8: Object/proxy preservation is not connected to the word-ratchet layer

What is missing: `32_mmm_word_ratchet.md` and `34_mmm_research_reservoir_map.md` do strong word-level steering, but they do not include the v4.3 distinction among adapter, probe, analogy, and proxy, nor the rule that proxies cannot become primary objects.

Where it should go:

- Add v4.3 mapping-type terms to `32_mmm_word_ratchet.md`.
- Add external-research extraction rules to `34_mmm_research_reservoir_map.md` requiring object-preservation checks when importing analogy-rich sources.

### Gap 9: Formal probes do not cover the newest active-intention requirements

What is missing: The Z3/probe suite covers status, pre-emit, bounded work, coupling order, closeout, fuzzing, CVC5 cross-check, MD monotonicity, metamorphic invariants, and tool-manifest completeness. It does not check primitive geometry/time/probability, support-first ordering, v4.3 object preservation, graveyard honesty, current JAX/Julia/PEPS3D carrier requirements, or actual file/receipt existence.

Where it should go:

- Add new probes rather than overloading the existing five-predicate L-proof framing.
- Update `harness_precommit.py` suite names and docs after adding them.

### Gap 10: Current-vs-legacy authority boundary is not prominent enough

What is missing: The consolidated harness contains valuable legacy language, but it does not consistently mark which surfaces are current steering, which are support/provenance, and which are stale relative to AGENTS/CODEX. This is risky because the harness is itself designed to be boot-loaded by agents.

Where it should go:

- Add a short current-authority banner to `README.md` and `00_READ_FIRST.md`.
- Mark `10_owner_doctrine_index.md`, `11_pytorch_as_ratchet.md`, `21_claude_working_memory.md`, `dictionary_v0.md`, and the April closeout as reference/provenance unless updated.

## 4. Z3 PROBES STATUS

Command used for direct status: `python3 <file>` from `/Users/joshuaeisenhart/wiki/wizard/harness-consolidated`.

System `python3` was `/usr/local/bin/python3` version `3.13.2`. The repo interpreter used by `harness_precommit.py` is `/Users/joshuaeisenhart/.local/share/codex-ratchet/envs/main/bin/python3` version `3.13.6`.

| Probe file | Can it run with direct `python3 <file>`? | What it checks | Still relevant? |
|---|---|---|---|
| `probes/closeout_doc_extractor.py` | yes, rc=0 | Parses a closeout markdown file, extracts role blocks, and reports unexpected headings. | yes, as a closeout-shape helper; it does not itself check ontology. |
| `probes/cvc5_cross_check.py` | no under system `python3`; fails `ModuleNotFoundError: No module named 'cvc5'` | Re-encodes five Z3 predicates in cvc5 and exhaustively compares the finite Boolean cube. | yes, but dependency/interpreter docs are stale. It passes under the repo interpreter with 2,816 cube points and 0 disagreements. |
| `probes/dogfood_audit_response_2026_04_18.py` | yes, rc=0 | Checks the audit-response closeout against six expected SAT/UNSAT outcomes. | limited; useful point-in-time dogfood evidence, not current harness admission. |
| `probes/dogfood_session_2026_04_18.py` | yes, rc=0 | Historical dogfood for the original L-proof closure packet. | stale/provenance only; the file itself says it is superseded as current closure proof. |
| `probes/harness_precommit.py` | yes, rc=0 | Runs the aggregate suite using the repo interpreter: status, pre-emit, bounded work, coupling gate, closeout, sim tool-manifest, fuzz, cvc5, MD, metamorphic, and closeout shape. | yes, current useful aggregate gate, but its hardcoded interpreter and suite count should be documented in markdown. |
| `probes/z3_bounded_work_unit.py` | yes, rc=0 | Encodes bounded work as object/scope, in-scope move, out-of-scope move, bound exit, and status field. | yes, highly relevant to anti-skip steering. |
| `probes/z3_closeout_completeness.py` | yes, rc=0 | Encodes required closeout fields and blocks forward-plan-only completion. | yes, relevant; should be extended for recon/admission and graveyard fields. |
| `probes/z3_closeout_shape_conformance.py` | yes, rc=0 | Checks exact markdown heading shape for role closeouts and rejects extra headings/missing required headings. | yes, relevant to receipt hygiene. |
| `probes/z3_coupling_gate_ordering.py` | yes, rc=0 | Encodes ordered gate evidence for isolated shells through bridge claims and checks malformed examples. | yes, but should be updated with current support/carrier and JAX/Julia/PEPS3D sim gates. |
| `probes/z3_fuzz_contract.py` | yes, rc=0 | Fuzzes status, pre-emit, bounded-work, coupling, and closeout contracts over Boolean cubes. | yes, useful meta-check for encodings. |
| `probes/z3_md_monotone.py` | yes, rc=0 | Checks monotonicity conditions for the memetic divergence score under added aligned or drift markers. | yes for harness-language edits; not a direct ontology guard. |
| `probes/z3_metamorphic_self_test.py` | yes, rc=0 | Runs tactic-variant and metamorphic checks so the Z3 encodings are not accidentally trivial. | yes, useful proof-hygiene meta-layer. |
| `probes/z3_pre_emit_six_axis.py` | yes, rc=0 | Encodes the six-axis pre-emit sentence gate: measurement, constraints, quotient, status, divergence, and banned construction verbs. | yes, highly relevant; it needs extension for geometry/time/probability/support/proxy smuggling. |
| `probes/z3_sim_tool_manifest_completeness.py` | yes, rc=0 | Encodes canonical sim metadata: classification, tool manifest, load-bearing tool, non-numeric tool when nonclassical, baseline divergence, and canonical result path. | partly; useful shape check but stale relative to current JAX/Julia primary engines, PyTorch sidelining, PEPS3D-first carrier, and v4.3 object preservation. |
| `probes/z3_status_ladder_admissibility.py` | yes, rc=0 | Encodes the four-label status ladder and forbids upward inference. | yes, highly relevant. |

## 5. RECOMMENDED ACTIONS

1. Add a v4.3 object-preservation pointer to the harness front doors: `00_READ_FIRST.md`, `README.md`, `READ_POLICY.md`, and `23_role_boot_templates.md`. Keep it pointer-only to the repo-held spec/validator; do not invent a `packet-v4-3-current`.

2. Replace the stale PyTorch-as-ratchet steering with current engine boundaries: JAX and Julia primary, PyTorch only legacy/comparison/helper with ablation. Start with `11_pytorch_as_ratchet.md`, `05_four_sim_kinds.md`, `22_project_dictionary.md`, and the sim-worker block in `23_role_boot_templates.md`.

3. Extend the pre-emit gate for primitive geometry, time, probability, and support/proxy smuggling. Update `17_pre_emit_audit.md`, `19_grammar.md`, `20_phrasebook.md`, and `z3_pre_emit_six_axis.py` or a sibling probe.

4. Add a support-first/manifold-first preflight requiring `runs_on`, `support`, `carrier`, and `coexistence` before bridge/operator/axis/manifold claims. Put it in `28_bounded_work.md` or a new `35_support_first_preflight.md`, and wire it into role templates.

5. Update sim contract steering for current nonclassical work: F01/N01, JAX/Julia carrier, finite PEPS3D anchor from the first admitted carrier step, negative controls, graveyard companions, source hash/staleness, receipt path, and blocked downstream consumers.

6. Add explicit recon/admission separation to closeout: separate `recon_artifacts` from `admission_decisions`, and make the closeout probes fail if a recon result is used as admission without an admission field.

7. Add negative-control and graveyard-honesty fields to sim and closeout templates, then add adversarial drift probes that fail on positive-only reports.

8. Reconcile boot surfaces: decide whether `BOOT.md` or `READ_POLICY.md` is the current selection authority, update `00_READ_FIRST.md` to include files `31` through `34`, and mark router files as routers rather than doctrine.

9. Fix suite-count drift in markdown to match `harness_precommit.py:47-59`, and document that direct `cvc5_cross_check.py` requires the repo interpreter or a system Python with `cvc5`.

10. Add a current-authority banner distinguishing current steering from provenance/reference files, especially around `CLAUDE.md`, old `.claude` memory indexes, April dogfood files, `dictionary_v0.md`, and old Wizard v3.4/v3-era language.
