---
title: Deep Research External Source Cluster — 2026-06-08
created: 2026-06-08
updated: 2026-06-08
type: source-cluster-router
framing: scratch
project: codex-ratchet
claim_ceiling: source-processing router only; no source claim, project claim, M(C), QIT-engine, Axis0, gravity, physics, Standard Model/GR, consciousness, or bridge admission
sources:
  - projects/codex-ratchet/source-intake/deep-research-source-queue-2026-06-08.json
  - projects/codex-ratchet/source-intake/deep-research-source-queue-2026-06-08.md
  - projects/codex-ratchet/source-intake/deep-research-source-accessibility-phase1-2026-06-08.json
  - projects/codex-ratchet/source-intake/deep-research-source-accessibility-phase1-2026-06-08.md
  - projects/codex-ratchet/source-intake/raw-source-paste-redacted-2026-06-08-session-20260607_193523_228c20-msg-96486.txt
---

# Deep Research External Source Cluster — 2026-06-08

## Purpose

This page is a cluster router for the large pasted external source list from the collapsed Hermes session. It keeps the list usable without pretending the sources have already been read into doctrine.

Two bad outcomes this page blocks:
- treating 151 pasted anchors as processed research because they are now in the wiki;
- turning every link into a shallow page before deciding its role.

## Boundary

This is source processing only. It does not admit any physics, QIT-engine, `M(C)`, Axis0, gravity, consciousness, emotion, AI-alignment, or bridge claim.

The safe status is:

```text
source anchor -> accessibility/excerpt receipt -> bounded extraction -> candidate support/falsifier/graveyard row
```

No row may jump directly from source anchor to project claim.

## Intake state

From the sanitized queue:

- Total parsed tokens: 151
- Remote URLs: 150
- Local files: 1
- URLs with redacted signed/query strings: 23
- Durable queue: [[projects/codex-ratchet/source-intake/deep-research-source-queue-2026-06-08]]
- Phase-1 accessibility receipt: [[projects/codex-ratchet/source-intake/deep-research-source-accessibility-phase1-2026-06-08]]

The original signed/query payloads are not persisted in wiki text. Hashes are preserved in the JSON queue for dedupe/provenance only.

## Phase-1 accessibility result

The bounded phase-1 pass processed 14 high-priority/paper-like rows after a broader Python extraction attempt timed out. It used `curl --max-time` plus Poppler (`pdfinfo`/`pdftotext`) so individual sources could not stall the session.

Observed result:

- `pdf_extracted`: 10
- `html_or_other_downloaded`: 3
- `missing`: 1

The missing local file is:

- `src-002` — `/Users/joshuaeisenhart/Downloads/A_Cognitive_Architecture_for_the_Implementation_of.pdf`

## Processing lanes

| Lane | Rows / sources | Current status | Claim ceiling | Next bounded move |
|---|---|---|---|---|
| Emotion / Lövheim / cognitive architecture | `src-001` CEUR Lövheim tweet emotion paper; `src-003` Wikiversity Lövheim cube page; `src-002` local cognitive-architecture PDF path | CEUR PDF extracted; Wikiversity page downloaded; local PDF missing | emotion-model reference only; no architecture or affective-engine claim | Find/recover the missing local PDF or replace it with a stable source; then extract a small emotion-model support ledger. |
| QIT / observers / categorical/formal support | `src-015` It-from-Qubit Simons proposal; `src-029` Orús tensor-network introduction; `src-035` multiverse/quantum mechanics paper; `src-087` Selby diagrammatic notation; `src-148` Observers Are All You Need | PDFs extracted in phase 1 | external formal pressure/support only; no `M(C)` or QIT-engine admission | Sort each source as donor, analogy, falsifier, or graveyard row before citing it in a synthesis page. |
| Physics / entropy / origin-life support | `src-009` Feynman physical-law PDF page returned a browser/challenge page; `src-076` Haldane Origin of Life PDF extracted | one extracted PDF, one challenged/HTML row | support/falsifier only; no physics or cosmology admission | Re-probe Feynman from a stable mirror or local copy; treat Haldane as historical origin-life/entropy support only. |
| AI / prediction / world-model support | `src-017` Bayesian Prediction for Artificial Intelligence; `src-004` ScienceDirect signed/source page; assorted later AI/agent links remain queued | one arXiv PDF extracted; ScienceDirect row downloaded as HTML/source landing page, not clean PDF text | AI/world-model support only; no implementation or alignment claim | Build a small AI/prediction source ledger only after extracting stable text from the ScienceDirect/cognitive-architecture sources. |
| Wide cultural/sociotechnical context | `src-062`, `src-063` Astrosociology journal PDFs and many queued non-paper web links | two PDFs extracted, most wider links unprocessed | context/graveyard/support only; not project evidence | Defer unless a later prompt asks for sociotechnical context or a specific source row. |

## Stop conditions

- Do not preserve or print signed query strings.
- Do not cite a queued source as if extracted.
- Do not create one page per URL until a lane has a target use.
- Do not let external theory/source language override the project front door: root distinguishability -> finite `M(C)` -> carrier/readout -> geometry/axes/readouts.
- Do not promote paper agreement into proof, simulation evidence, or owner doctrine.

## Immediate next extraction order

1. Recover or replace the missing cognitive-architecture PDF (`src-002`).
2. Create a small emotion/Lövheim support ledger from `src-001` and `src-003`, explicitly bounded as affect-model support.
3. Classify the QIT/formal PDFs as donor / analogy / falsifier / graveyard rows, not as admissions.
4. Re-probe `src-009` Feynman from a stable source if physical-law support is needed.
5. Leave wide sociotechnical/context rows queued unless they become task-relevant.

## Related pages

- [[projects/codex-ratchet/read-first]]
- [[projects/codex-ratchet/actual-physics-docs-processing-map-2026-06-06]]
- [[projects/codex-ratchet/physics-model-curated-core-source-list-2026-06-06]]
- [[projects/codex-ratchet/current-toe-contender-graveyard-workspace-2026-06-07]]
- [[CLAIM_CEILING_POLICY]]
