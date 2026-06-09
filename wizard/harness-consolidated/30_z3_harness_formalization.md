last_updated: 2026-04-18

# z3 Harness Formalization (L-proof)

The MMM harness is a constraint-admissibility system. Constraint-admissibility systems are z3/cvc5's domain. This file names the formalization: the harness's own admissibility predicates become machine-checkable SMT constraints, and structural violations surface as UNSAT.

---

## The Observation

Every harness layer is already a constraint system:

- **L1 (status ladder)** — strict ordering: `exists < runs < passes local rerun < canonical by process`. Inflation = claim L while only evidence for L' < L without cited L evidence.
- **L-bound (bounded work)** — predicate: work `W` stayed within Scope iff In-scope(W) ∧ ¬Out-of-scope(W) ∧ bound-exit-cited(W).
- **L5 (closeout)** — predicate: closeout admissible iff all required fields for the role block are present.
- **Pre-emit audit (17_)** — six-axis predicate: sentence admissible iff probe-cited ∧ constraint-cited ∧ quotient-named ∧ status-labeled ∧ divergence-preserved ∧ ¬banned-construction.
- **Coupling-program gates (06_)** — strict partial order on steps 1–6 with per-step admission criterion; UNSAT if step N admitted without cited result file for step N-1.

Per `07_z3_unsat_primacy.md`, z3 UNSAT is the primary proof form in this project. Applied to the harness itself: an inadmissible claim surfaces as UNSAT under the harness constraint set. The UNSAT trace is the proof that the claim is structurally impossible under the harness, not merely disallowed.

---

## The Formalization Layer (L-proof)

L-proof sits alongside the other layers:

```
L0  ambient topology                   [pre-instruction]
L1  root constraints (axiom)           [doctrine]
L2  harness grammar                    [grammar templates]
L3  project dictionary                 [noun grounding]
L4  role boot templates                [role differentiation]
L5  closeout templates                 [session-boundary shape]
L6  probe corpora (25_, 26_)           [measurement]
L-bound  bounded-work block            [anti-skip-ahead]
L-meta   edit protocol                 [differential]
L-proof  z3 encodings                  [machine-checkable admissibility]  ← this file
```

L-proof is not a replacement for L0–L5; it is a decidability layer on top of them. A sentence that passes L-proof has a machine-checkable witness that the harness admits it. A sentence that fails L-proof has a UNSAT trace naming which axis it violated.

---

## Encoding Targets

Five encodings exhaust the current harness's machine-checkable surface. Each is a separate work unit (see `28_bounded_work.md`); only the first is shipped in the initial deliverable.

| # | Encoding | Input representation | UNSAT signal | Status |
|---|---|---|---|---|
| 1 | Status-ladder non-inflation | claimed label + evidence booleans | claim > evidence → UNSAT | shipped 2026-04-18; 3/3 tests |
| 2 | Pre-emit six-axis audit | sentence feature record | any axis false under predicate → UNSAT | shipped 2026-04-18; 5/5 tests |
| 3 | Bounded-work unit | (Scope, In-scope, Out-of-scope, action taken) | action ∉ In-scope ∨ action ∈ Out-of-scope → UNSAT | shipped 2026-04-18; 5/5 tests |
| 4 | Coupling-program gate ordering | claimed step + cited-evidence per step | gate admitted without predecessors cited → UNSAT | shipped 2026-04-18; 5/5 tests |
| 5 | Closeout block completeness | role + field-present booleans | required field missing for role → UNSAT | shipped 2026-04-18; 6/6 tests |
| F | Contract fuzzer (C1–C4) | boolean cube of each encoding | C1/C2/C3/C4 violation → fuzz FAIL | shipped 2026-04-18; 0 violations |
| X | cvc5 dual-solver cube cross-check | full input cube per encoding (2816 points) | z3/cvc5 disagreement on any cube point → X FAIL | shipped 2026-04-18, cube-extended post-audit; 0 disagreements |
| M | MD monotone conjecture | pre/post `(D_corr, D_drift, D_compl)` ∈ [0,1]³ | pure-addition with MD drop → UNSAT (holds) | shipped 2026-04-18; Conj-A UNSAT, B+C SAT |

Each encoding is small (< 150 lines z3). Running them is fast (< 1s per claim). The cost is in the input representation — reducing a natural-language claim to the structured form the encoding consumes.

Total L-proof coverage as of Round D-prime close (post-three-audit-rounds tightening 2026-04-18): **5 admissibility encodings + 1 fuzzer + 1 dual-solver cube cross-check (2816 points) + 1 MD-monotone probe + 1 metamorphic self-test (M1+M2 invariants) + 1 closeout shape-conformance probe (markdown↔record literal agreement) live; 10/10 aggregator suites green under `harness_precommit.py` (~10.3s). Session dogfood for the audit-response unit cited separately: 5 positive SAT + 1 adversarial UNSAT.**

---

## Input Representation Problem

z3 cannot read prose. The harness claims live in prose. The bridge between prose and z3 is a structured record per claim:

```
{
  "claim_kind": "status_label" | "work_unit" | "gate_admission" | "closeout" | "sentence_audit",
  "fields": {...}
}
```

The bridge can be:
- **manual** — the author fills the record before submitting the claim (highest fidelity; lowest throughput)
- **LLM-extracted** — a separate LLM pass extracts the record from the prose (recursive; the extraction itself needs L-proof eventually)
- **grammar-template-matched** — if the claim is cast in the `19_grammar.md` pattern, the record fields line up by position (medium fidelity; high throughput)

First deliverable uses the manual form. The extraction problem is a separate work unit.

---

## Why UNSAT, Not SAT

`07_z3_unsat_primacy.md` states this in the math domain; it transfers directly:

- SAT = "a model exists where the claim could hold." A harness check that returns SAT only shows the claim is *not ruled out* — it does not prove admissibility. The claim could still fail at a probe the encoding did not capture.
- UNSAT = "no model exists where the claim holds under these constraints." UNSAT is a structural impossibility proof within the encoded constraint system.

So L-proof is primarily a refusal tool: it proves certain claims are inadmissible. Passing L-proof (SAT) is necessary but not sufficient; failing L-proof (UNSAT) is sufficient for refusal.

This matches the existing harness posture: exclusion is prior to construction.

---

## Scope Limits of the L-Proof Layer (audit-response 2026-04-18)

L-proof is bounded. The encodings cover what the encodings cover; they do not prove the
whole harness. This section names what L-proof does **not** cover so that SAT from the
aggregator is not read as a universal admissibility certificate.

**Representation scope.**
Each predicate consumes a structured record of booleans (and, for status-ladder + gate, a
small integer claim). The record is authored manually by the operator — Phase 4 extractor
is deferred. This means every L-proof verdict is downstream of a human reduction from
prose to record; the reduction itself is not proved.

**Cube-size scope.**
The fuzzer and cvc5 cube cross-check both exhaust the boolean cube per encoding. This is
tractable today — 2816 total cube points — because feature counts are small (4–10 booleans
per encoding). Any future encoding whose record exceeds ~20 booleans will blow out of
full-cube coverage and require sampled or symbolic reasoning instead. That transition is
not in L-proof's current surface.

**Logic scope.**
All encodings sit in `QF_LIA` (quantifier-free linear integer arithmetic) + propositional
logic, or in `QF_LRA` (for the MD monotone probe). No quantifier alternation, no arrays,
no uninterpreted functions. Harness rules that would require those (e.g. "for every probe
M in corpus, there exists a surviving candidate") are not encodable in the current
fragment.

**Axis-coverage scope.**
Five rule surfaces are encoded (status-ladder, pre-emit, bounded-work, gate-ordering,
closeout). The harness has more rules than that — see `31_admission_surface.md` for the
catalog of rules that are not yet encodable. L-proof SAT on a record says only that the
record passes the five encoded predicates, not that every harness rule approves.

**Solver-agreement scope.**
z3 + cvc5 agreement on the full cube is a strong empirical witness. It is not a proof.
Both solvers could share a common soundness bug. The ratchet is dual-solver disagreement
surfaces immediately, but shared blind spots remain possible.

**Session-claim scope.**
The dogfood record is one session's claim. It uses the same predicates as the aggregator
but against session-specific input records. It is cited separately from the aggregator in
every closeout because a session claim is not a regenerating invariant.

**Meta-scope.**
This entire doc is prose. The prose itself is not L-proof-verified. The predicates are
verified; the prose around them is subject to the regular pre-emit six-axis audit, not to
a higher-order proof.

---

## Phase 1 Deliverable (Closed 2026-04-18)

All five encodings now live under `~/wiki/wizard/harness-consolidated/probes/`:

- `z3_status_ladder_admissibility.py` — 3/3 tests
- `z3_pre_emit_six_axis.py` — 5/5 tests
- `z3_bounded_work_unit.py` — 5/5 tests
- `z3_coupling_gate_ordering.py` — 5/5 tests
- `z3_closeout_completeness.py` — 6/6 tests

Phase 1 bound-exit: 24/24 tests passing across 5 encodings; z3 v4.16.0 in codex-ratchet env.

---

## Phase 2+3+5+6+7 Deliverable (Closed 2026-04-18, tightened after audit)

Next-wave artifacts now live under `~/wiki/wizard/harness-consolidated/probes/`:

- `z3_fuzz_contract.py` — Phase 2 contract fuzzer over the boolean cube of all 5 encodings.
  Checks C1 (non-triviality), C2 (monotone evidence), C3 (bad-flag sensitivity), C4 (universal
  inflation). 0 violations across all 5 encodings on the full cube.
- `cvc5_cross_check.py` — Phase 3 dual-solver agreement. Re-implements each predicate in cvc5
  and replays **every input cube point** (2816 points total: 64 status-ladder + 512 pre-emit +
  64 bounded-work + 384 gate-ordering + 1792 closeout). 0 z3/cvc5 disagreements. This is a
  strictly stronger contract than sampled test-list agreement and raises the refusal from
  "z3 says no" to "two orthogonal SMT encodings agree on no model over the full cube"
  per `07_z3_unsat_primacy.md`.
- `harness_precommit.py` — Phase 5 L-proof aggregator. Runs 5 encoding suites + contract
  fuzzer + cvc5 cube cross-check + MD monotone probe + metamorphic self-test (Round C) +
  closeout shape-conformance (Round D-prime). **10/10 green, ~10.3s wall-clock.**
  **Not a git pre-commit hook** — the current Wizard harness tree at `~/wiki/wizard/` is not
  under git version control. The aggregator is a harness-edit gate: run manually before declaring
  any harness-edit closeout per `29_harness_edit_protocol.md`, and before any session claim
  that cites harness admissibility predicates.
- `z3_md_monotone.py` — Phase 6 probe of the MD composite metric monotone conjecture.
  Conj-A (pure-addition monotone) → UNSAT (structural). Conj-B (mixed-edit monotone) → SAT
  with explicit counterexample. Conj-C (correction-weight boundary witness) → SAT. Outcome:
  MD is monotone only under pure-addition edits; mixed edits can degrade MD because the
  weights (0.4 / 0.3 / 0.3) are unequal. Harness cannot coast on any single axis.
- `dogfood_session_2026_04_18.py` — Phase 7 dogfood. The session's own claim is decomposed
  into 5 positive records + 1 adversarial record and fed through the predicates.
  Positive outcome: 5/5 SAT. Adversarial record (gate-ordering claim=step6 with step-1
  evidence only) → UNSAT as required. Without the adversarial record the dogfood would be
  vacuous on the gate axis (positive defaults to claim=1 which is trivially admissible);
  the adversarial UNSAT shows the encoding actually refuses session-level overclaims.

### Exit citations (split per audit 2026-04-18, refreshed Round D-prime)

- **Phases 1, 2, 3, 5, 6 (regenerating invariants):** `harness_precommit.py` rc=0 over
  10 suites, ~10.3s. Suites covered: 5 z3 unit encodings + contract fuzzer + cvc5 cube
  cross-check (2816 points) + MD monotone probe + metamorphic self-test (Round C) +
  closeout shape-conformance (Round D-prime).
- **Phase 7 (point-in-time session claim, audit-response unit):**
  `dogfood_audit_response_2026_04_18.py` rc=0 — 5 positive records SAT + 1 adversarial
  record UNSAT. Cited separately because a session claim is not a regenerating
  invariant. The older `dogfood_session_2026_04_18.py` is preserved as a frozen
  artifact for the original Phase 2+3+5+6+7 unit (do not read it as current state).

**Phase 4 (partial — extractor) shipped Round D-prime:**

- `closeout_doc_extractor.py` — markdown closeout doc → boolean role record. Returns
  `extra_top_level_headings` so shape divergences (Round D + D-prime failure modes)
  are caught structurally, not by re-reading the doc.
- `z3_closeout_shape_conformance.py` — z3 predicate over the extracted record:
  SAT iff all required fields' headings present + non-empty AND no forward-plan AND
  zero extras. Probe has 5 tests (2 positive + 3 adversarial), all green.
- Full Phase 4 (prose-content fidelity, not just heading shape) remains deferred —
  see `31_admission_surface.md` Class III.1.

**Still deferred (each requires separate admission):**

- **Phase 4 — full** — prose-content extractor (Class III.1 in admission surface)
- **Phase 8** — external publication write-up

---

## Cross-references

- `07_z3_unsat_primacy.md` — doctrine this file extends to the harness itself
- `21_mimetic_meme_manifold.md` — MMM layers formalized here
- `04_status_label_hierarchy.md` — status ladder encoded in demo
- `28_bounded_work.md` — bounded-work encoding target (future)
- `17_pre_emit_audit.md` — six-axis encoding target (future)
- `ENFORCEMENT_AND_PROCESS_RULES.md` — Rule 12 (structural anti-salience) this formalizes
