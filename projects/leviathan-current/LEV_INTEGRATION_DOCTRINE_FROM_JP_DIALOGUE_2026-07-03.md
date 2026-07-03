---
title: Lev integration doctrine — hardened by the JP dialogue
created: 2026-07-03
type: project-doctrine
status: distilled from live JP pushback 2026-07-03; each item survived adversarial questioning
tags: [leviathan, integration, gates, engines, mmm, claim-types, doctrine]
---

# Lev integration doctrine — what the JP dialogue settled (2026-07-03)

JP's pushback was the best adversarial review the integration story has had.
Every item below survived it or was corrected by it. This doc supersedes
looser statements in earlier integration docs where they conflict.

## 1. The claim-type split (the core rule)

Every claim entering lev is one of two kinds, and they are gated differently:

- CLASS 1 — computable referent: the truth-maker is bytes/execution/math
  ("tests pass", "latency = X", "quotient_class_count = 5"). Gate = independent
  recomputation from the referenced raw inputs. LLM reports in this class are
  never trusted; they are re-derived.
- CLASS 2 — semantic referent: meaning, quality, sentiment, persona fit.
  NO recomputation exists. A second LLM call is a second WITNESS, not
  verification. These NEVER gate on truth — only on process (ran, valid
  schema, fresh) — and enter as advisory. What CAN be gated: the statistics
  of the witnesses (agreement rate, stability under paraphrase, calibration
  against downstream outcomes over time). Measure the judges, never call the
  judgment verified.
- The working move on Class 2: DECOMPOSE first. Most "subjective" evals are
  majority Class-1 in disguise (standards-adherence = boundaries + lint +
  coverage + a semantic residue). Shrink opinion's territory; gate the rest.

## 2. Engines stay domain-side; lev depends on contracts, not engines

- Pure lev (no quantitative domain) needs NO sim engine. jax: no seat.
  julia: no seat. Verified against every plausible seat.
- The rule: each evidence domain brings its own recompute machinery
  (SDLC: compilers/tests/AST; physics: numpy/jax/torch/julia; video: ffprobe).
  Lev's invariant job: require multi-leg independently-computed evidence and
  check the legs agree. Engine-agnostic forever.
- torch is the ONLY engine with a potential native lev seat (trainable
  perception/routing on lev's own streams, feeding the existing G3 port) —
  and that seat is UNEARNED: the first predictor lost to a flat baseline
  (receipt on record). No trained component enters lev without beating a
  dumb baseline in a measured comparison; when one does, it enters as
  advisory-with-receipts, never as a gate.

## 3. Parity is not proof (the airbag concession)

- Cross-engine agreement = reproducibility engineering. It gates the
  ARITHMETIC layer only (was the finite calculation executed faithfully).
  The julia vec/unvec incident proves the failure-containment layer works —
  like a crash test: it does not prove the theory, and must never be
  presented as "proof it's working."
- The proof ladder: engine parity < dual-solver SMT on finite statements
  (real proofs, load-bearing today, no floats) < Lean-style formalization
  (roadmap, not done). Claims are split into logic (SMT), arithmetic
  (parity), interpretation (claim ceilings) — three instruments, never
  conflated.
- Dual implementation: ONE spec, two independent translations. Neither must
  be perfect — independence, not perfection, is the requirement; the system
  detects imperfection rather than assuming its absence. Divergence between
  translators is also a spec-ambiguity detector. Cost honesty: the second
  leg is the admission toll for the permanent record; exploration/purgatory
  work runs single-leg.

## 4. What a sim is (the one-line answers that landed)

- A sim = an executable claim about a mathematical model, with negative
  controls that prove the claim could have failed, emitting a result JSON
  that is the evidence object gates consume. "pytest where the thing under
  test is a theory."
- The LLM/state rule: LLM output is never a state transition; only a gate
  verdict is. World state = (M dictionary, W graph, L ledger, PARK set);
  every tick is (state, event) -> (state', receipts); given L, every tick
  replays.

## 5. Ratchet organs vs ratchet properties (the convergence claim, precise)

- Lev already has the ORGANS: ClaimGate, retries, schemas, content
  addresses, witness receipts, discharge-to-graph. (Independently evolved;
  homologous with the bootpack proto-gates — provenance receipts: bootpack
  rules 38/43/78/82/89.)
- What turns organs into a RATCHET, currently missing in lev: (1) kills
  provably permanent (no silent readmission), (2) retries with lineage
  (reworked attempt = new token, not same bytes), (3) an objective progress
  measure (park loops cannot stall forever), (4) state advances ONLY on
  audited receipts. These four are formalized in the ratchet_formal_gates
  program (R5/R6 etc.) and are the natural next lev kernel upgrades —
  runtime-level, zero engines required.

## 6. MMM v1 (the avatar concept, de-mystified for build)

- The MMM is DATA: typed entries {term, sense, scope, version,
  provenance_ref}, content-addressed, admitted through a gate
  (candidate -> park -> confirm -> admitted). Not a model.
- Four carriers of the same object, deployed in cost order: (1) context
  pack on fable (RAG) — works today, zero training; (2) conformance eval —
  outputs checked against entries, violations typed; (3) fine-tuned nano
  model — later, only after a benchmark shows it beats RAG-on-fable;
  (4) frontier LLM = a giant unscoped MMM (the literal reading of
  "LLMs are MMMs").
- The two touches per tick: resolve (inject org referents before inference)
  and conformance (check output against the same entries after). The
  ratchet: every human correction becomes a candidate entry; the dictionary
  is never done.

## 7. Product frame

Lev = CONSTRAINT ENGINEERING as a category. Businesses buy constrained
agents: gated outputs, a graph that holds only what survived checking,
terminating retries, receipts for everything, an MMM overlay so agents
speak the org's language. "Everyone else sells a model and hopes; lev sells
the constraint system that makes any model's output trustworthy."

## 8. One-week shippables identified (2026-07-03)

1. MMM v1 (schema + admission + resolve + conformance; dogfood on lev's own
   jargon; with/without demo).
2. Honesty gate for coding agents (claimed test results re-run by companion;
   mismatch blocks the REPORT).
3. Generic reconciliation pack (two refs + claimed number -> compare).
4. Sequential-shift sensor pointed at a real ops stream (pack exists).

## 9. How to talk to JP (method, learned)

- Material walkthroughs in his format (input/output, tick-by-tick state per
  component), never concept prose. No cross-domain analogies unless his own
  stack contains the instance. Concede first when he's right — the two
  biggest doctrine sharpenings in this doc came from conceding fast
  (recompute-of-meaning does not exist; parity is not proof) and then
  drawing the honest line.
