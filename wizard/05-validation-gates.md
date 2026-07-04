---
title: Wizard Validation Gates
created: 2026-04-28
updated: 2026-04-28
type: concept
tags: [wizard, validation, receipt, route-truth, mmm, audit]
framing: current
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Wizard Validation Gates

Validation keeps the Wizard from becoming a costume for controller narration. It checks whether routes ran, whether MMMs shaped output, and whether follow-ups came from receipts.

## Receipt Gate

Every spawned route needs a receipt with:

- unit id
- route category
- loaded sources
- what ran
- result
- evidence path or quoted summary
- open issues
- status label

Blocked and deferred routes need a smaller receipt naming the blocker or deferral reason.

## Fake-Plurality Gate

Do not count a route as plural merely because one controller wrote several headings. Plurality requires separate receipts or an explicit statement that the result was controller-local.

## Boot-Contamination Gate

Positive boot prompts should not name negative/reference-only subtrees, banned-token lists, or "do not say" blocks unless the task is a validator. Positive boot should load shaped language. Validator files can hold excluded forms, but those files should not leak into normal boot.

## MMM Leakage Gate

Reject or downgrade MMM rows when:

- category id and folder disagree
- audit/security/council/synthesis are labeled as voices or lanes
- rows use uniform `100` weight without probe evidence
- `gloss` is empty or generic
- provenance is a bulk shipping stamp rather than a source path plus admission run
- row kind is wrong
- aligned rows lack drift contrast
- sentence stems are missing

## Follow-Up Gate

A follow-up menu passes only when it includes real route language, stable selectors, payoff, and blocker/deferral notes. A full Wizard run must consider all voices, lanes, checks, routes, and compositions before pruning visible choices.

It fails when the visible menu is mostly route bookkeeping, receipt inspection, contradiction listing, or orchestration debugging. Those options belong in full-bank or diagnostic mode unless the user asked for them.

## Voice Preservation Gate

A Full Wizard output fails when voices ran but the visible answer compresses them into one generic paragraph. Each visible voice must provide a distinct useful contribution:

- Hume: evidence and uncertainty.
- Zhuangzi: alternate readings and exclusion conditions.
- Feynman: observable check.
- Orwell: plain wording.
- Popper: falsifier or failure condition.
- Pushback: overclaim correction.
- Factory: bottleneck or handoff.
- Strategy: sequence or retreat condition.
- Systems: feedback loop or second-order effect.

The gate passes only when at least one sentence per visible voice would be lost if that voice were removed. Labels alone do not count.

## Wiki Gate

Any durable wiki edit must update:

- the page itself
- [[index]] when a new public page is added
- [SCHEMA.md](../SCHEMA.md) when a new public folder or tag appears
- [[log]] with the action and status

The current Wizard reference status is `exists`. Promotion requires a fresh run that uses these pages, emits receipts, validates links/frontmatter, and logs the result.

## Full-Format Gate

The Wizard format itself is testable. A full Wizard output fails the gate when:

- it gives a short status summary instead of the full section order
- it omits V1-V9, L10-L14, G15-G18, or C19-C22 when the task is Wizard tuning
- it calls local receipt scaffolding a live model behavior test
- it hides the wave registry or turns it into the whole answer
- it uses a follow-up menu with labels but no route language
- it includes raw advisory transcripts as boot-visible packet material

A full Wizard output passes when:

- the header names workstream, route truth, and result
- the main answer gives the bottom line and status boundary
- Popper classifies the central claim
- the wave registry states what ran, blocked, or deferred
- voices, lanes, council, hygiene, security, and audit all appear when relevant
- the follow-up bank uses stable selectors and full route language
- evidence paths are present but not allowed to dominate the answer

## Behavior Gate

Static validation is not enough for MMM claims. To prove that an MMM shapes output, run the same task under at least three regimes:

1. no MMM
2. main MMM only
3. assigned mini-MMM plus main MMM

The task must not telegraph the expected voice. The audit compares vocabulary, structure, decision route, and failure modes. A mini-MMM passes only when the loaded output is distinguishable in the intended direction without importing banned or cosplay vocabulary.

For Hume, the output should show evidence-scoped human judgment, not academic Hume terms. For Zhuangzi, the output should preserve live readings and exclusion tests, not classical motifs. For QIT build mode, the output should move toward an artifact, gate, or status decision, not merely describe philosophy.

## Proof And Graph Gate

Proof and graph tools can validate local structure. They do not validate the whole philosophy. The output must state the claim ceiling.

Examples:

- A Z3 gate can prove a status-ladder constraint.
- A cvc5 gate can cross-check a symbolic case.
- A graph gate can prove a DAG or ordering property.
- A pytest gate can prove the runner’s contract.

None of those alone proves a QIT engine. They support the next rung in the status ladder.
