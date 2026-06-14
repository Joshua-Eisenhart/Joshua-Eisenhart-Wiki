last_updated: 2026-04-17

# LLM Worker Harness — Read First

Front door for Codex Ratchet / Leviathan harness work.

## Mandatory first read

**`SALIENCE_LOADER.md`** — one page. Read top to bottom before anything else below. This is the priming layer; everything else is the working surface.

For tier selection by task type (hygiene / analysis / canonical), see **`READ_POLICY.md`**. For subagent-spawning framing that prevents safety-refusal of raw preamble injection, see **`agent-spawn-template.md`**.

## Boot order (after loader)

1. `15_root_axiom_card.md` — identity is probe-relative, not primitive
2. `01_nominalism_primer.md`
3. `02_constraint_admissibility_primer.md`
4. `03_language_discipline.md` — verb discipline
5. `16_dictionary.md` — noun grounding
6. `19_grammar.md` — sentence patterns
7. `20_phrasebook.md` — clause rewrites
8. `04_status_label_hierarchy.md`
9. `05_four_sim_kinds.md`
10. `06_coupling_program_order.md`
11. `07_z3_unsat_primacy.md`
12. `08_anti_patterns.md`
13. `09_perspectival_rotation.md`
14. `10_owner_doctrine_index.md`
15. `11_pytorch_as_ratchet.md`
16. `12_f01_n01_nominalist_axioms.md`
17. `13_mandatory_pushback.md`
18. `14_leviathan_os_constraint_map.md`
19. `17_pre_emit_audit.md`
20. `18_red_team_probes.md`
21. `21_mimetic_meme_manifold.md` — manifold depth map + self-application probes + construction rule
22. `22_project_dictionary.md` — L3 project-specific noun grounding (lego, shell, axis, engine, coupling program, MMM, Leviathan, ratchet)
23. `23_role_boot_templates.md` — L4 role-differentiated boot blocks (sim-worker / controller / Hermes / batch-runner)
24. `24_closeout_templates.md` — L5 closeout blocks (S / K / H / R) — the last-message shape that carries manifold between sessions
25. `25_adversarial_drift_probes.md` — probe family `M_drift`; ten rationalist-framed probes with scoring rubric for session `D_drift`
26. `26_completion_stems.md` — completion-stem corpus for session `D_completion`; ten stems with both training-manifold and shaped-manifold completions
27. `27_ambient_topology.md` — L0 layer; pre-instruction language biasing doctrine; admission criteria for L0 vs. instructions-on-manifold
28. `28_bounded_work.md` — L-bound layer; the work-unit block that refuses skip-ahead by declaring Scope + Out-of-scope + Bound exit
29. `29_harness_edit_protocol.md` — L-meta; every harness edit is a bounded-work unit with pre/post `MD` measurement or named reason for non-measurement
30. `30_z3_harness_formalization.md` — L-proof; z3/SMT encoding of harness admissibility predicates; structural violations surface as UNSAT; first encoding at `probes/z3_status_ladder_admissibility.py`
31. `31_admission_surface.md` — catalog of rules not yet encodable in L-proof
32. `32_mmm_word_ratchet.md` — word/phraselet admission protocol for the MMM language reservoir
33. `33_mmm_language_fingerprint.md` — measured first-pass distribution of current wiki/harness language
34. `34_mmm_research_reservoir_map.md` — source/research lanes for enriching language without imitation

## v4.3 current Wizard core (updated — 2026-06-13)

The proper shared Wizard v4.3 packet now lives in the wiki at `~/wiki/wizard/packet-v4-3-current/`. This harness-consolidated folder remains nominalist-CS doctrine/priming support, not the runtime packet itself.

For object-preservation work, use the shared v4.3 core plus the active LLM adaptation. Repo validators remain concrete implementation/check surfaces when a task invokes that guard:
- shared core: `~/wiki/wizard/packet-v4-3-current/`
- Hermes adaptation: `~/wiki/wizard/hermes-version-current/`
- Claude adaptation: `~/wiki/wizard/claude-version-current/`
- validator implementation surface when needed: `scripts/wizard_v4_3_object_preservation.py`

Do not boot directly from v4.2 as current law; older packets are source/provenance to be lifted through v4.3 and the active LLM adaptation.

## Injection layer (not read — pasted)

`SALIENCE_PREAMBLE.md` holds short preamble blocks (60 / 140 word) for prepending to spawned-agent system prompts. Use when you launch a subagent that cannot be trusted to perform the full read.

## Core rules (admissibility form)

This file is navigation; the manifold that shapes completions lives in the files above. The rules below name the admissibility conditions for substantive output:

- identity / equality admitted only under a cited probe family `M`
- constraints narrow by exclusion; survivors remain provisional
- status labels stay distinct: `exists < runs < passes local rerun < canonical by process`; no label is inferred from a lower one
- substantive claims are cast in the pattern from `19_grammar.md`; verbs survive the audit in `03_language_discipline.md`
- divergence is preserved until exclusion narrows the candidate set by cited evidence
- `17_pre_emit_audit.md` is run against every substantive sentence; `25_adversarial_drift_probes.md` is run against sessions suspected of drift; `26_completion_stems.md` is run after harness edits

If a request conflicts with the harness, the conflict is named rather than smoothed. Smoothing reads as silent refusal of the audit and is itself out of admissible space.
