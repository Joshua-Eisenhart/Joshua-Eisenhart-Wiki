---
title: Research Ratchet Wiki Update Intake
created: 2026-06-21
updated: 2026-06-21
type: intake-receipt
status: installed_with_cautions
claim_ceiling: wiki/source update receipt; not runtime integration; not Lev merge; not sim admission
source_zip: /Users/joshuaeisenhart/Downloads/research_ratchet_wiki_update_20260621.zip
followup_source_zip: /Users/joshuaeisenhart/Downloads/research_ratchet_full_wiki_ingest_pack_20260621.zip
---

# Research Ratchet Wiki Update Intake

## Source

Installed from local bundle:

```text
/Users/joshuaeisenhart/Downloads/research_ratchet_wiki_update_20260621.zip
```

The bundle was treated as a wiki/source pack, not a product release and not a
runtime proof.

A later full processing bundle was digested as source/reference material:

```text
/Users/joshuaeisenhart/Downloads/research_ratchet_full_wiki_ingest_pack_20260621.zip
```

That full bundle integrity-checked clean and contained deeper research notes,
source extracts, and Lev patch sketches. Its `wiki_update/` pages were not copied
over the current wiki because the current wiki pages already include safer
claim-ceiling and path-repair edits.

## Installed pages

Concept pages:

- [[concepts/world-engine-graph-patch-algebra]]
- [[concepts/spinor-memory]]
- [[concepts/attractor-basin-digger]]
- [[concepts/admissibility-geometry-and-gates]]

Project pages:

- [[projects/research-ratchet/README]]
- [[projects/research-ratchet/missing-primitives-and-open-questions-2026-06-21]]
- [[projects/research-ratchet/cold-start-packet-current-2026-06-21]]
- [[projects/research-ratchet/next-10-ratchet-clicks-2026-06-21]]
- [[projects/codex-ratchet/spinor-memory-sim-integration-2026-06-21]]
- [[projects/leviathan-current/research-ratchet-deep-patch-plan-2026-06-21]]

## Route correction

The source bundle used `projects/leviathan/` for the Leviathan patch page. The
wiki's current Leviathan namespace is `projects/leviathan-current/`, so the page
was installed there and the Research Ratchet front-door link was retargeted.

## Accepted frame

The useful abstraction is:

```text
event-sourced admissibility geometry over a world-model graph
```

Use this as a bridge across:

```text
WorldModelGraph
GraphPatch
GateOperator
ReceiptEventLog
SpinorMemory
AttractorBasinDigger
ColdStartPacket
ClaimGate authority chain
Leviathan Effect/Eval/Ledger spine
Codex-Ratchet sim/proof discipline
```

## Cautions

- Do not call this runtime integrated.
- Do not call the Leviathan patch merged.
- Do not claim Spinor Memory is proof authority.
- Do not claim Attractor Basin Digger is admission authority.
- Do not copy the bundled `sources/` tree into the wiki or product by default; it
  contains older uploaded ZIPs and is evidence/source material only.
- Repair Lev target paths before any repo patch. The source sketch names
  `core/graph-state`, `core/eval`, and `core/effect` as package roots. A fresh
  upstream path check on 2026-06-21 at
  `cc0e6fe537a6549df6c0172c4963f3dcfa36fa5f` found current surfaces under
  `core/context-graph`, `core/domain/src`, `core/eval/src/proof`,
  `core/effect/src`, `core/flowmind`, `core/orchestration/src/handlers`, and
  related bench/test surfaces.
- Translate `GraphPatch` into the existing Lev `GraphOperation[]` /
  compositor vocabulary before calling it a runtime primitive.
- Rewrite the FlowMind sketch from `flow_id` / `slots` into the current
  `name` / `entry` / `nodes` flow schema before treating it as executable.

## Local checks

The bundle zip was integrity-checked before installation. The wiki should be
probed again after this intake to confirm no broken links were introduced.
