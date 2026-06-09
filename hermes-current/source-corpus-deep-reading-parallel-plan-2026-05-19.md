# Source Corpus Deep Reading Parallel Plan — 2026-05-19

Purpose: plan the long-running, parallel document-processing campaign for the READ ONLY source corpora so the wiki becomes educational and concept-rich rather than only repo-spec-like.

Status: active planning/control note.

## Correction being preserved

The wiki should not reduce large source works, old threads, books, and high-entropy reference docs into tiny spec-like markdown summaries.

Large source corpora such as Dark Empress, old threads, READ ONLY Reference Docs, and Legacy core_docs need actual reading and extraction:

- themes
- concepts
- arguments
- examples
- tensions and contradictions
- owner-kernel vs generated elaboration
- glossary / vocabulary
- research connections
- tool/math/CS connections
- candidate wiki pages
- executive summaries at several scales

Repo-specific application should be one downstream section, not the whole meaning of a page.

## Source roots

Primary source roots:

1. `/Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/READ ONLY Reference Docs`
   - observed 2026-05-19 inventory: 76 files, about 8.3 MB
   - mix: markdown, text, images
   - notable large files include `grok unified phuysics nov 29th.txt`, `Leviathan v3.2 word.txt`, bootpacks, holodeck docs, Weyl/axis/math materials

2. `/Users/joshuaeisenhart/Desktop/Codex Ratchet/READ ONLY Legacy core_docs`
   - observed 2026-05-19 inventory: 285 files, about 30.7 MB
   - mix: markdown, text, PDFs, DOCX, Pages, Python, JSON, CSV
   - notable large files include `grok rosetta stone.pdf`, `gemini axiom thread. from leviathan. saved. .pdf`, `gemini toe summary volume 1-23.pdf`, high-entropy GPT/Gemini/Grok thread dumps, sim/result artifacts, and refined Ratchet Fuel docs

Important: these roots are READ ONLY source corpora. Do not rewrite originals. Produce derived wiki notes, raw wrappers/extracted text, ledgers, and summaries elsewhere.

## Why this is a large parallel task

This is not a single cleanup pass. It is a multi-day / multi-agent reading campaign.

The work is well-suited to LLMs because much of it is:

- summarizing long docs
- extracting themes from old threads
- distinguishing author prompts from assistant/generated continuations
- making executive summaries
- clustering repeated ideas across many files
- turning high-entropy source material into lower-entropy educational wiki pages

But it requires real reading. Filename scans are not enough.

## Worker shape for Sonnet-high day

When Claude Code / Sonnet high is available, use high parallelism. Each worker gets one bounded source packet and returns a receipt, not direct uncontrolled wiki edits unless explicitly assigned.

Recommended parent lanes:

1. Corpus inventory and clustering parent
   - assigns child workers by folder/source type
   - produces a source map and recommended packet order

2. Dark Empress / book-scale source parent
   - goal: recover major themes from the full work, not a tiny digest
   - outputs: chapter/section map, major themes, recurrent metaphors, system ideas, unresolved tensions, candidate public pages

3. READ ONLY Reference Docs parent
   - splits docs into math/geometry, bootpacks, axis/Weyl, symbolic/IGT, old physics threads, holodeck/runtime, JP/graph/tooling
   - outputs cluster summaries and candidate wiki pages

4. Legacy core_docs parent
   - splits a1 refined Ratchet Fuel, a2 high entropy feeds, ultra-high entropy PDFs/TXT, sim/result artifacts, QIT/runtime docs
   - outputs cluster summaries, provenance fences, concept/research extraction candidates

5. Research integration parent
   - for each extracted theme, names outside fields and papers/books to integrate later
   - outputs educational research lanes, not just citation lists

6. Wiki synthesis parent
   - converts accepted summaries into wiki page plans:
     - concept pages
     - source pages
     - comparison pages
     - educational tool pages
     - research primers
     - project application pages

## Child receipt format

Each child worker should return a durable receipt with:

- source path(s) read
- source type: book / thread / spec / bootpack / result artifact / code / mixed
- amount actually read: full / sampled / headings-only / blocked
- owner-kernel passages or ideas
- generated/assistant elaboration passages or ideas
- executive summary, 1 paragraph
- structured summary, 1-3 pages
- major themes
- important concepts not yet in wiki
- research/tool connections
- Codex Ratchet / Leviathan application, clearly marked downstream
- risks: drift, stale claims, generated speculation, contradiction, unsafe promotion
- recommended wiki outputs
- confidence / open questions

## Summary layers to produce

For large sources, do not stop at one markdown file. Produce layered outputs:

1. Source card
   - short orientation, provenance, role, caveats

2. Executive summary
   - readable overview for humans

3. Theme map
   - major ideas and recurring motifs

4. Concept extraction ledger
   - candidate wiki concepts with one-sentence why

5. Research bridge map
   - outside fields/papers/books/tools to connect

6. Project application note
   - how this may matter for Codex Ratchet / Leviathan, fenced as application

7. Wiki page queue
   - exact pages to create or deepen

## Anti-collapse rules

- Do not reduce a 600-page book to one tiny summary unless that summary is explicitly only the source card.
- Do not flatten old threads into repo specs.
- Do not let current repo authority erase source genealogy.
- Do not let high-entropy generated elaboration outrank owner-side kernels.
- Do not promote source resonance into proof or sim status.
- Do not create dozens of pages before a controller accepts the cluster map.
- Preserve contradictions and alternatives where source work has not resolved them.

## First day target when Sonnet high is available

A good first large parallel day should aim for:

1. full corpus inventory with packet assignments
2. 8-20 source-packet receipts, depending on available worker budget
3. one deep book/thread receipt for Dark Empress or a similarly large source
4. one READ ONLY Reference Docs cluster map
5. one Legacy core_docs cluster map
6. one accepted wiki synthesis queue
7. no direct promotion into doctrine without controller review

## Immediate next controller step

Before launching workers tomorrow:

1. create a manifest of all source files with sizes, extensions, and rough token estimates
2. choose packet boundaries under safe worker context limits
3. assign each packet a role and receipt template
4. launch Sonnet-high workers in parallel
5. reconcile receipts into wiki source ledgers and educational concept/research/tool queues

2026-05-19 refinement: [[model-family-reality-cluster-audit-2026-05-19]] is now the controller audit for the user-named all-model family cluster. Packet B (`grok unified phuysics nov 29th.txt`) has now been extracted at [[packet-b-grok-unified-physics-extraction-2026-05-19]], with visible contradiction markers preserved. The Holodeck source packet has now been extracted at [[holodeck-source-packet-extraction-2026-05-19]], with owner-kernel vs generated-elaboration separation and no new Holodeck concept sprawl. Next packet should be Leviathan v3.2 for the broad all-model lane, or Packet C (`grok eisenhart model .txt`) if the controller wants one more ToE/physics formula/claim extraction before widening into Leviathan, Dark Empress, Grandmaster, personality/IGT, or QIT/math carriers.

Packet-source receipt requirements used for Packet B and future source packets:
- source path and amount actually read;
- owner-confirmed kernels;
- owner-flagged uncertainties/contradictions;
- generated/assistant elaboration;
- formula and diagram candidates;
- outside research claims needing verification;
- wiki destination decision: deepen existing page, source-only note, result/router pointer, or no promotion.

Related notes:
- [[wiki-ingest-queue-and-priorities]]
- [[whole-wiki-mmm-source-research-campaign-2026-05-18]]
- [[read-only-source-doc-processing-ledger-2026-05-18]]

Write mode: controller-maintained.
