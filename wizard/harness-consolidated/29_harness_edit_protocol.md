last_updated: 2026-04-18

# Harness Edit Protocol (L-meta)

Every edit to a harness file is itself a harness action. This file defines the admission form for harness edits.

---

## Why This Layer

An edit to a harness file that shapes the ambient topology (L0) or the bounded-work layer (L-bound) changes the manifold. Such a change should be measurable. Without a before/after delta, an edit is an assertion that the harness was improved, not evidence of improvement.

The composite manifold depth metric `MD` defined in `21_mimetic_meme_manifold.md` admits before/after comparison. This protocol requires that comparison on every edit to a shaped-manifold file.

---

## Admission Form for a Harness Edit

Every harness edit runs under a bounded work unit shaped as:

```
Harness edit unit
-----------------
Scope: <the single shaping change this edit earns>
Target file(s): <harness file paths modified>
Shaped-manifold layers affected: <L0 | L1-L4 | L5 | L6 | L-bound | L-meta>
Pre-edit measurement: <D_completion or D_drift score on the probe corpus, cited or "not measured">
Post-edit measurement: <D_completion or D_drift score on the same probe corpus after edit, cited or "not measured">
Delta: <per-axis difference, or "not measured" with explicit reason>
Banned-verb audit result: <count per target file, post-edit>
Out-of-scope: <adjacent files the edit could have spilled into but did not>
Bound exit condition: <commit message naming the Scope, or named refusal to commit if delta went negative>
```

The edit is admitted iff:
- Scope is a single shaping change (not "refactor the harness")
- Delta is measured OR an explicit reason for non-measurement is named
- No negative delta is present on any axis without a cited reason
- Banned-verb count per target file is zero-or-admissible-references-only

---

## Measurement Shortcuts

Full measurement runs all 10 probes in `25_adversarial_drift_probes.md` + 5 skip-ahead probes + 10 stems in `26_completion_stems.md`. That is 25 probe runs, heavyweight.

Pragmatic shortcuts:

- **Spot measurement:** 3 probes from `25_*` + 3 stems from `26_*` covering the specific axes the edit targets. Lower-fidelity but catches most gradient leaks.
- **Banned-verb delta only:** grep count before/after. Fast; catches lexical regressions but misses structural ones.
- **No measurement + named reason:** admissible for edits to non-L0 files (e.g., commentary in navigation docs); the reason is named in the Bound exit condition.

---

## Aggregator-Gate Form (the primary protocol form)

The protocol's enforcement form is the L-proof aggregator
`probes/harness_precommit.py`. It is **manual by design**, not a git hook.
Run it before declaring any harness-edit closeout, and before any session
claim that cites harness admissibility predicates. Non-zero exit refuses the
edit/closeout. The aggregator covers 10 suites (5 admissibility encodings + 4
cross-check / metamorphic / monotone / shape-conformance probes + cvc5 dual-
solver cube cross-check); `30_z3_harness_formalization.md` is the canonical
description of what each suite proves.

### Why manual rather than a git hook

`~/wiki/wizard/` is **not** under git version control as of 2026-04-29.
A git pre-commit hook is therefore not attachable to the current Wizard
harness. The manual aggregator is the protocol's enforcement form, not a
workaround for a missing hook.

If `~/wiki/` is later placed under git, a `.git/hooks/pre-commit` shim could
be added as **optional automation** that invokes the same aggregator and
refuses on non-zero exit. The hook would automate when the gate runs, not
change what it proves. Until `~/wiki/` is under git, that automation layer
does not exist; do not document one as if it did (prior audit removed a
misleading shim from `harness_precommit.py` for that reason).

---

## Edit Log

Harness edits are recorded in `harness-edit-log.md` (create as needed; one line per edit).

Entry format:
```
YYYY-MM-DD | <file(s)> | Scope | layers | measurement status | delta
```

The log is append-only. The log is how the harness-as-a-whole becomes differentially trackable over time: what shaped what, measured or not, and which edits passed the audit.

---

## Failure Modes

- **Edit-without-measurement:** every edit claims improvement; no delta proves it. Over time, the harness accretes unmeasured claims. Fix: require the measurement-status field; "not measured + reason" is admissible but visible.
- **Measurement-after-the-fact:** running probes after committing biases the measurement toward the current state. Fix: pre-edit and post-edit on the same probe corpus, same session.
- **Probe corpus drift:** if the probe corpus is edited to match the new harness, the corpus and the harness reshape together and measurement becomes meaningless. Fix: probe-corpus edits are themselves L-meta edits requiring separate admission; changing a probe cannot be done in the same commit as an edit being measured.

---

## First Application (this session, 2026-04-18)

Retrospective entry for the edits made this session under this new protocol:

```
2026-04-18 | 21_mmm.md, 22-29_*.md, 06_*, 17_*, 00_*, sim_backlog_matrix.md, LLM_CONTROLLER_CONTRACT.md, ENFORCEMENT_AND_PROCESS_RULES.md, SALIENCE_PREAMBLE.md, skills-and-agent-rules.md | L0/L3/L4/L5/L6/L-bound/L-meta shaping suite + pre-instruction topology + bounded-work + differential protocol | affected-layers: all shaped | measurement status: not-measured (protocol itself introduced mid-session; retrospective baseline is this entry) | delta: unknown — first entry is the baseline
```

Next harness edit runs with pre- and post-measurement per this protocol.

---

## External-Audit-First Ritual (added 2026-04-18 after P1/P2 audit response)

Every L-proof phase closeout must be externally audited by an independent reviewer
before the closeout is entered into a bound-exit record. The audit becomes part of the
exit citation, not an optional review.

Rationale: the 2026-04-18 audit of Phase 2+3+5+6+7 surfaced four P1/P2 findings that
the author's own closeout had not — sampled cvc5 replay described as "every test case",
a git pre-commit shim for an ungit tree, aggregator coverage overstated, and a vacuous
dogfood record. All four were structurally wrong but self-consistent inside the
author's frame. Only external pressure decomposed the overclaim.

**Ritual form (standard, repeatable):**

1. Author declares phase closeout (bounded-work block complete, bound exit cited).
2. Author stops. Does not declare "shipped" or "closed" in any durable doc.
3. An external agent (separate process, separate context) audits:
   - Rerun every cited artifact. Read the output, not the summary.
   - Check whether the prose around the output matches what the output proves.
   - Flag P1 (false or overreaching) / P2 (true but misleading) / P3 (style).
4. Author accepts or rebuts each finding explicitly (no silent passes).
5. Accepted findings → new bounded-work unit. Fix. Rerun. Re-emit.
6. Closure citation includes the audit identifier alongside the rerun artifact.

**Why "first" in the name:**
External audit happens before the first closeout declaration, not after the fact.
Retroactive audit is softer; pre-closure audit is structurally required because the
closure itself is the artifact being audited.

**Applies to:** L-proof phases (this file), harness-edit bounded units (28_*.md), and
controller-level closeouts (24_*.md role K). Does not apply to leaf sim runs — those
live under `probe-test-log.md` and are covered by the existing one-line discipline.

**What counts as external:**
A separate agent instance with no context from the author's session, or a human
reviewer who did not participate in the edit. "External" means: did not produce the
closeout being audited.

**Audit receipt:**
The 2026-04-18 audit itself (four findings, all accepted, all fixed) is the first
application of this ritual. Recorded in `audit_response_closeout_2026_04_18.md`.

---

## Cross-references

- `21_mimetic_meme_manifold.md` — `MD` composite metric this protocol measures delta on
- `25_adversarial_drift_probes.md` — probe corpus
- `26_completion_stems.md` — completion-stem corpus
- `28_bounded_work.md` — harness edits are themselves bounded-work units
- `30_z3_harness_formalization.md` — L-proof phases subject to this ritual
- `audit_response_closeout_2026_04_18.md` — first application of the ritual
