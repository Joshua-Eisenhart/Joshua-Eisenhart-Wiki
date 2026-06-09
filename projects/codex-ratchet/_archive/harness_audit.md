# Wiki Harness Audit Report
**Date:** 2026-04-16  
**Auditor:** Claude Haiku (fresh audit, non-author)  
**Target:** `/Users/joshuaeisenhart/wiki/harness/`

---

## OVERALL RESULT: PASS

All 12 required checks passed. Harness documentation is complete, internally consistent, and correctly structured.

---

## File Inventory & Word Counts

| File | Words | Limit | Status |
|------|-------|-------|--------|
| 00_READ_FIRST.md | 299 | ≤300 | ✓ |
| 01_nominalism_primer.md | 326 | ≤500 | ✓ |
| 02_constraint_admissibility_primer.md | 342 | ≤500 | ✓ |
| 03_language_discipline.md | 438 | ≤500 | ✓ |
| 04_status_label_hierarchy.md | 283 | ≤500 | ✓ |
| 05_four_sim_kinds.md | 404 | ≤500 | ✓ |
| 06_coupling_program_order.md | 323 | ≤500 | ✓ |
| 07_z3_unsat_primacy.md | 374 | ≤500 | ✓ |
| 08_anti_patterns.md | 467 | ≤500 | ✓ |
| 09_perspectival_rotation.md | 406 | ≤500 | ✓ |
| 10_owner_doctrine_index.md | 468 | ≤500 | ✓ |
| README.md | 485 | ≤500 | ✓ |

---

## Detailed Check Results

### Check 1: All 12 Required Files Exist
**Status:** ✓ PASS  
All 12 files present and readable.

### Check 2: Word Count Limits
**Status:** ✓ PASS
- 00_READ_FIRST.md: 299 words ≤ 300 words (limit)
- All primers (01–07): 283–438 words, all ≤ 500 words
- All remaining files (08–11): 406–485 words, all ≤ 500 words

### Check 3: Language Discipline Rewrite Pairs (03)
**Status:** ✓ PASS  
**Found:** 10 bad→good rewrite pairs in 03_language_discipline.md table:
1. "The rule creates a phase transition" → good rewrite
2. "This proves the operator is fundamental" → good rewrite
3. "The geometry determines Axis 0" → good rewrite
4. "The measurement causes the collapse" → good rewrite
5. "This confirms the hypothesis" → good rewrite
6. "The correct density matrix is" → good rewrite
7. "The law forces the result" → good rewrite
8. "This discovers the true structure" → good rewrite
9. "The constraint generates candidates" → good rewrite
10. "The shell creates the next layer" → good rewrite

Requirement: ≥ 10 pairs. ✓ Met.

### Check 4: Status Label Table Alignment (04 vs CLAUDE.md Authority)
**Status:** ✓ PASS  
04_status_label_hierarchy.md table exactly matches authority in /Users/joshuaeisenhart/Desktop/Codex\ Ratchet/.claude/worktrees/harness-audit/CLAUDE.md:

| Label | Meaning (Match) |
|-------|---|
| `exists` | File is present in repo ✓ |
| `runs` | Executes without error (exit 0) ✓ |
| `passes local rerun` | Fresh run confirms all tests pass ✓ |
| `canonical by process` | passes local rerun + SIM_TEMPLATE + tool manifest + non-empty reasons + classification field ✓ |

All definitions identical.

### Check 5: HARD GATE Statement in 05
**Status:** ✓ PASS  
**Found in 05_four_sim_kinds.md:**
```
**Nonclassical is HARD BLOCKED until both conditions hold:**
1. Tool-capability sims exist and pass locally for each intended tool
2. At least one tool-lego-integration sim exists and passes for a relevant admissibility claim
```
Gate explicitly stated. ✓

### Check 6: Coupling Program Order Steps (06)
**Status:** ✓ PASS  
All 6 mandatory steps listed and correctly ordered in 06_coupling_program_order.md:
1. Shell-local Lego Sims ✓
2. Pairwise Coupling Sims ✓
3. Multi-shell Coexistence ✓
4. Topology-Variant Reruns ✓
5. Emergence Tests ✓
6. Bridge Claims Only ✓

Hard gate enforcement stated: "Do not make bridge claims before evidence from steps 1–5 exists." ✓

### Check 7: Banned Verbs (Grep Analysis)
**Status:** ✓ PASS  
**Banned verbs:** causes, creates, drives, produces, generates, makes, forces, determines  
**Search result:** Zero instances outside of 03_language_discipline.md intentional examples.

Banned verbs correctly appear ONLY in 03_language_discipline.md as:
- Bulleted list under "## Banned Verbs"
- Rewrite table (bad→good examples)
- Guidance section ("Inspect sentences with 'causes,' 'creates,' 'drives.'")
- Final paragraph discussing rationalist language problem

Zero violations. ✓

### Check 8: Markdown Cross-References
**Status:** ✓ PASS  
All internal markdown links verified:
- 00_READ_FIRST.md → references 01–10: all exist ✓
- 01_nominalism_primer.md → references 02: exists ✓
- 02_constraint_admissibility_primer.md → references 03: exists ✓
- 03_language_discipline.md → references 01, 02: exist ✓
- 04_status_label_hierarchy.md → references 05, 06: exist ✓
- 05_four_sim_kinds.md → references 04, 06, 07: exist ✓
- 06_coupling_program_order.md → references 05, 07, repo file: exist ✓
- 07_z3_unsat_primacy.md → references 04, 05, 06, repo file: exist ✓
- 08_anti_patterns.md → references 03, 09, 10: exist ✓
- 09_perspectival_rotation.md → references 08: exists ✓
- 10_owner_doctrine_index.md → references 08, 09, README: exist ✓
- README.md → references 08, 09, 10: exist ✓

All relative path links resolve. ✓

### Check 9: Absolute Paths in 10_owner_doctrine_index.md
**Status:** ✓ PASS  
All 21 absolute paths verified to exist:

**Foundational Doctrine (11 files):**
- `/Users/joshuaeisenhart/.claude/projects/-Users-joshuaeisenhart-Desktop-Codex-Ratchet/memory/user_nominalist_system.md` ✓
- `/Users/joshuaeisenhart/.claude/projects/-Users-joshuaeisenhart-Desktop-Codex-Ratchet/memory/user_one_thing_many_perspectives.md` ✓
- `/Users/joshuaeisenhart/.claude/projects/-Users-joshuaeisenhart-Desktop-Codex-Ratchet/memory/user_empathy_origin.md` ✓
- `/Users/joshuaeisenhart/.claude/projects/-Users-joshuaeisenhart-Desktop-Codex-Ratchet/memory/user_teleological_selection_cosmology.md` ✓
- `/Users/joshuaeisenhart/.claude/projects/-Users-joshuaeisenhart-Desktop-Codex-Ratchet/memory/user_entropic_monism_doctrine.md` ✓
- `/Users/joshuaeisenhart/.claude/projects/-Users-joshuaeisenhart-Desktop-Codex-Ratchet/memory/user_causality_fep_doctrine.md` ✓
- `/Users/joshuaeisenhart/.claude/projects/-Users-joshuaeisenhart-Desktop-Codex-Ratchet/memory/user_self_similar_legacy_doctrine.md` ✓
- `/Users/joshuaeisenhart/.claude/projects/-Users-joshuaeisenhart-Desktop-Codex-Ratchet/memory/user_qit_turing_oracle_doctrine.md` ✓
- `/Users/joshuaeisenhart/.claude/projects/-Users-joshuaeisenhart-Desktop-Codex-Ratchet/memory/user_compression_is_rosetta_convergence.md` ✓
- `/Users/joshuaeisenhart/.claude/projects/-Users-joshuaeisenhart-Desktop-Codex-Ratchet/memory/user_four_sim_kinds_tool_lego_integration_doctrine.md` ✓
- `/Users/joshuaeisenhart/.claude/projects/-Users-joshuaeisenhart-Desktop-Codex-Ratchet/memory/user_geometry_stack_ratchet_doctrine.md` ✓

**Critical Feedback (10 files):**
- `/Users/joshuaeisenhart/.claude/projects/-Users-joshuaeisenhart-Desktop-Codex-Ratchet/memory/feedback_language_is_rationalist.md` ✓
- `/Users/joshuaeisenhart/.claude/projects/-Users-joshuaeisenhart-Desktop-Codex-Ratchet/memory/feedback_multiple_divergent_narratives.md` ✓
- `/Users/joshuaeisenhart/.claude/projects/-Users-joshuaeisenhart-Desktop-Codex-Ratchet/memory/feedback_anti_salience_doctrine.md` ✓
- `/Users/joshuaeisenhart/.claude/projects/-Users-joshuaeisenhart-Desktop-Codex-Ratchet/memory/feedback_root_constraints_create_process.md` ✓
- `/Users/joshuaeisenhart/.claude/projects/-Users-joshuaeisenhart-Desktop-Codex-Ratchet/memory/feedback_constraint_manifold_simultaneous.md` ✓
- `/Users/joshuaeisenhart/.claude/projects/-Users-joshuaeisenhart-Desktop-Codex-Ratchet/memory/feedback_pytorch_is_ratchet.md` ✓
- `/Users/joshuaeisenhart/.claude/projects/-Users-joshuaeisenhart-Desktop-Codex-Ratchet/memory/feedback_classical_unblocked_nonclassical_gated.md` ✓
- `/Users/joshuaeisenhart/.claude/projects/-Users-joshuaeisenhart-Desktop-Codex-Ratchet/memory/feedback_tool_integration_before_nonclassical.md` ✓
- `/Users/joshuaeisenhart/.claude/projects/-Users-joshuaeisenhart-Desktop-Codex-Ratchet/memory/feedback_selective_divergence_patient_convergence.md` ✓
- `/Users/joshuaeisenhart/.claude/projects/-Users-joshuaeisenhart-Desktop-Codex-Ratchet/memory/feedback_just_do_it.md` ✓

All 21 paths exist. ✓

### Check 10: No Content Redundancy Between Primers
**Status:** ✓ PASS  
Each primer covers distinct, complementary territory:

- **01_nominalism_primer.md:** Nominalist metaphysics; forms are material; statistics IS causality; LLM rationalist bias is architectural inheritance, not fixable, only visible
- **02_constraint_admissibility_primer.md:** How constraints work mechanically; elimination vs generation; forward vs backward reasoning; test ≠ truth
- **03_language_discipline.md:** Vocabulary discipline enforcement; banned/preferred verbs; rationalist language as epistemological lever
- **04_status_label_hierarchy.md:** Four-label system; no upward inference rule; banned vague synonyms
- **05_four_sim_kinds.md:** Sim taxonomy; classical baseline vs nonclassical vs tool-capability vs tool-lego-integration; hard block on nonclassical
- **06_coupling_program_order.md:** Six-step mandatory sequence with hard gates; shell-local first, bridge claims last
- **07_z3_unsat_primacy.md:** Asymmetry between SAT (existence, weaker) and UNSAT (impossibility, stronger); load-bearing proof form

No two primers overlap in their core claim. ✓

### Check 11: No LLM-Voice Tics
**Status:** ✓ PASS  
Grep for ["Let me", "I'll", "Certainly", "Great question"]: Zero hits.

Files use imperative/declarative forms throughout:
- Direct commands: "Do not skip steps," "Use survival/exclusion wording"
- Third-person claims: "This lego survives," "Constraints eliminate"
- No hedging, no agreement-seeking, no conversational softening

✓

### Check 12: Written for LLM Workers, Not Human Learners
**Status:** ✓ PASS  
Tone and framing analysis:

**Audience signals (LLM worker orientation):**
- 01: "When your first instinct says..." — directly addresses LLM introspection requirement
- 02: "Never write: 'This is THE density matrix,'" — command to worker, not explanation for learner
- 03: "**You do not have that license.**" — confrontational; assumes worker understands the problem
- 04: "LLM agents collapse truth distinctions" — problem framing for LLM, not pedagogy
- 05: "The real backlog is the integration matrix" — operational framing for worker
- 06: "Do not skip steps" — enforcement, not learning scaffolding
- 07: "Quantum mechanics speaks in negation" — technical authority claim, assumes worker can handle abstraction
- 08: "Exact list of failure modes to avoid when executing work" — operational checklist for worker
- 09: "The LLM failure mode:" — directly names and addresses LLM problem
- README: "Onboarding materials for LLM workers" — explicitly labels audience

**Absent pedagogical throat-clearing:**
- No "Let me explain," "This might seem confusing," "You might be wondering"
- No step-by-step walkthroughs for human learners
- No analogies to build intuition
- No Socratic questioning

All files are operational documents for LLM execution, not educational texts for human onboarding. ✓

---

## Raw Grep Results

### Banned Verbs Search
```
Search for: causes, creates, drives, produces, generates, makes, forces, determines
Result: Found ONLY in 03_language_discipline.md as intentional documentation/examples
Violations outside 03: 0
```

### Word Count Command Output
```
00_READ_FIRST.md:                    299 words
01_nominalism_primer.md:             326 words
02_constraint_admissibility_primer.md: 342 words
03_language_discipline.md:           438 words
04_status_label_hierarchy.md:        283 words
05_four_sim_kinds.md:                404 words
06_coupling_program_order.md:        323 words
07_z3_unsat_primacy.md:              374 words
08_anti_patterns.md:                 467 words
09_perspectival_rotation.md:         406 words
10_owner_doctrine_index.md:          468 words
README.md:                           485 words
```

### Markdown Link Verification
```
All relative references verified to point to existing files within harness/
All absolute references in 10_owner_doctrine_index.md verified to existing memory files
Zero broken links detected
```

---

## Summary

| Check | Result | Evidence |
|-------|--------|----------|
| 1. Files exist | PASS | All 12 present |
| 2. Word counts | PASS | All within limits |
| 3. Rewrite pairs (03) | PASS | 10 pairs found |
| 4. Status labels (04) | PASS | Matches CLAUDE.md exactly |
| 5. HARD GATE (05) | PASS | Explicitly stated |
| 6. Six steps (06) | PASS | All listed, correct order |
| 7. Banned verbs | PASS | 0 violations; 0 instances outside 03 examples |
| 8. Cross-references | PASS | All .md links resolve |
| 9. Absolute paths (10) | PASS | All 21 memory files exist |
| 10. No redundancy | PASS | Each primer distinct |
| 11. No LLM tics | PASS | Zero instances detected |
| 12. LLM worker voice | PASS | Operatinal, not pedagogical |

**FINAL VERDICT: PASS** — Harness documentation is complete, correct, and internally consistent.

