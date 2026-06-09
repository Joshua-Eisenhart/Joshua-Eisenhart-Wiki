last_updated: 2026-04-18

# Admission-Surface Audit — What L-Proof Does Not Yet Cover

Catalog of harness rules and failure classes that are **not** currently encodable as SMT
predicates in the L-proof layer. Written 2026-04-18 as Phase 6 of the audit-response
bounded-work unit.

`harness_precommit.py` rc=0 certifies nine suites pass. It does not certify that every
harness rule is checked. This file names the gap so that L-proof closures cannot silently
stand in for whole-harness admission.

Categorization:
- **Class I** — out of SMT expressive range (would need quantifiers, arrays, or UF that
  the current QF_LIA/QF_LRA fragment cannot represent).
- **Class II** — in range, but no encoding written yet (tractable next-phase work).
- **Class III** — fundamentally cannot be SMT-encoded (depends on reading live file
  contents, runtime behavior, or natural-language semantics).

---

## Class I — expressive-range gaps

### I.1 Universal survivor quantification
Rule surface: `21_mimetic_meme_manifold.md` and the general nominalist frame require that
any claim over a probe family `M` references a surviving candidate set. Encoding requires
quantifier alternation: `∀ M ∈ corpus. ∃ s ∈ S. admissible(s, M)`. QF_LIA cannot express
this; would need universally-quantified SMT (or a finite-corpus unrolling for a concrete
`M`).

Workaround in current encoding: pre-emit axis 5 (`divergence_preserved`) is a single
boolean that a survivor set was named. The boolean does not check that the named set is
consistent with any specific probe corpus.

### I.2 Banned-verb substring search
Rule surface: `03_language_discipline.md` banned-verb list ("causes", "creates",
"drives", "produces", "generates", "makes", "forces", "determines"). Current encoding:
pre-emit axis 6 (`banned_construction_absent`) is a single boolean set by the author.
Actual substring checking requires string theory (CVC4/cvc5 or Z3 string solver) or a
pre-processing pass outside the SMT layer.

### I.3 Status-label inference across sentences
Rule surface: `ENFORCEMENT_AND_PROCESS_RULES.md` Rule 12 (structural anti-salience) plus
`04_status_label_hierarchy.md` require that no sentence IMPLIES a higher status than
preceding sentences cited. This is a temporal/discourse constraint over a document, not a
single-sentence predicate. Would need a sequence encoding (array of sentence records).

---

## Class II — in-range, not yet encoded

### II.1 Ritual-compliance check
Rule surface: `29_harness_edit_protocol.md` external-audit-first ritual. A closeout is
admissible iff an external-audit identifier is cited. Encoding shape:
`admissible_closeout(cited_audit_id, audit_identifier_exists_in_corpus)`. Tractable as a
boolean + set-membership test; not yet implemented.

### II.2 Tool-manifest completeness
Rule surface: `CLAUDE.md` sim requirements state `TOOL_MANIFEST` must have `tried`,
`used`, non-empty `reason` for every tool, and `TOOL_INTEGRATION_DEPTH` must label at
least one tool `load_bearing`. Trivially boolean-encodable; not wired in because current
encodings target harness-edit claims, not sim claims.

### II.3 Coupling-program numbered-step exclusivity — **ENCODED 2026-04-18**
Rule surface: `06_coupling_program_order.md` steps 1–6. Original gap: gate-ordering
encoding checked "step N requires steps ≤ N evidence" but did not check "claimed step
must exist and be numeric 1–6". A malformed claim (step=0 or step=7) passed as UNSAT
for the wrong reason.

**Status:** encoded in `probes/z3_coupling_gate_ordering.py` via `check_with_reason()`
which returns one of `ADMITTED` / `INADMISSIBLE` / `MALFORMED`. The `malformed_predicate`
explicitly checks `claim < 1 ∨ claim > 6` and short-circuits before consulting the
ordering predicate. Three new tests cover claim=0, claim=7, claim=-1; all return
`(unsat, MALFORMED)`. Backward-compatible `check()` still returns sat/unsat for
existing callers.

### II.4 Three-lanes-never-merge predicate
Rule surface: `CLAUDE.md` three-lanes discipline (Foundation migration / Seam proof
depth / Stack coexistence). A claim that collapses progress across lanes is
inadmissible. Encoding: assign each claim a lane tag, refuse claims that cite evidence
from a different lane. Not yet encoded.

### II.5 Read-only file protection
Rule surface: memory entry `feedback_respect_read_only_labels.md` — READ ONLY labels
are authoritative. Encoding: predicate takes (path, action) and UNSATs if action ∈
{move, rename, modify} and path matches the read-only pattern. Trivially boolean; not
yet encoded because "action on path" is usually not expressed as an admissibility
record.

### II.6 Closeout-doc shape conformance — **ENCODED 2026-04-18**
Rule surface: `24_closeout_templates.md` defines exactly N fields per role block
(K=7, S=9, H=7, R=7) and forbids a forward-plan field. Original gap: the operator
could author a markdown closeout doc whose literal `##`-heading shape diverged from
the spec while the dogfood-asserted boolean record matched it. Round D caught a
literal `## Forward plan` heading despite `forward_plan_present=False` in the
record. Round D-prime caught two extra `##`-level appendices beyond Block K's
seven fields.

**Status:** encoded in two parts:
- `probes/closeout_doc_extractor.py` parses a markdown doc into a boolean record
  matching `ROLE_FIELDS[role]` plus `forward_plan_present` plus
  `extra_top_level_headings` (list).
- `probes/z3_closeout_shape_conformance.py` runs `shape_conformance_predicate`
  over the extracted record: SAT iff all required fields' headings present AND
  no forward-plan heading AND zero extras. The shape predicate runs against the
  literal markdown form, so authoring a closeout doc whose markdown shape and
  boolean record disagree is now structurally impossible at the L-proof layer.

The probe is wired into `harness_precommit.py` aggregator (10/10 suites
post-Round-D-prime).

## Class III — fundamentally outside SMT

### III.1 Prose fidelity
Whether a prose paragraph actually says what its extracted record claims it says is a
natural-language semantic check. No finite SMT encoding captures it. Phase 4 extractor
(deferred) is the bridge — it performs the reduction — but the extractor's own fidelity
is not SMT-verifiable either.

### III.2 Runtime behavior
Whether a cited artifact actually exists on disk, ran on the current machine, produced
rc=0 in this session, and printed the text cited — all require IO, not SMT. The current
aggregator does this imperatively in Python (`subprocess.run`); that's not L-proof, it's
an orchestrator around L-proof.

### III.3 Semantic equivalence of paraphrases
"All five encodings pass local rerun" and "The L-proof suite is green" may be the same
claim, or not. Deciding equivalence requires NL understanding. Current harness expects
the author to pick one canonical wording and submit it; paraphrases are out-of-scope.

### III.4 Intent alignment
Whether a harness edit actually makes the manifold "deeper" in the intended sense is
ultimately a judgment about the author's goal. The MD metric (`21_mmm.md`) is a
quantitative proxy; L-proof can verify that MD_post > MD_pre under specific conditions
(see `z3_md_monotone.py`) but cannot verify that the intended notion of "better" is
what MD measures.

---

## What SAT from the aggregator *does* say

After this audit the aggregator SAT claim decomposes to:

    harness_precommit.py rc=0 witnesses:
      - 5 admissibility predicates hold on all 2816 cube points,
      - z3 and cvc5 agree on all 2816 cube points,
      - C1–C4 contract fuzzer violations = 0,
      - MD monotone probe verdicts are {UNSAT, SAT, SAT} as expected,
      - metamorphic tactic-variance + all-false invariants hold.

It does **not** witness:
      - every harness rule is encoded (Class II inventory),
      - encodings can express quantified / string / discourse rules (Class I),
      - prose matches records, files exist, intent is aligned (Class III).

A closeout that cites `harness_precommit.py rc=0` as the sole exit is still a scoped
claim. The scope is the nine suites. This file is the registry of what lies outside
them.

---

## Cross-references

- `30_z3_harness_formalization.md` — the L-proof layer this file bounds
- `29_harness_edit_protocol.md` — external-audit-first ritual that found the need for this catalog
- `audit_response_closeout_2026_04_18.md` — closeout under which this file was written
- `ENFORCEMENT_AND_PROCESS_RULES.md` — Rule 12 (Class I.3 target)
- `03_language_discipline.md` — banned-verb source (Class I.2)
