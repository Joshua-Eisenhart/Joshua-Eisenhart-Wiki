---
title: Leviathan Current Worker Swarm Plan 2026-06-17
created: 2026-06-17
type: worker-swarm-plan
status: active wave 1
claim_ceiling: routing plan; worker outputs require controller verification
---

# Leviathan Current Worker Swarm Plan 2026-06-17

## User objective

Build a markdown wiki that can process the whole current Leviathan / LevOS estate, explain what it is, find Josh / Joshua Eisenhart's contributions, preserve JP Smith's implementation/developer lane, and assess where Leviathan is doing well, failing, promising, and research-connected.

## Active source roots

- Current repo: `/Users/joshuaeisenhart/GitHub/leviathan`
- Wiki project: `/Users/joshuaeisenhart/wiki/projects/leviathan-current`
- Existing LevOS prior notes: `/Users/joshuaeisenhart/wiki/projects/levos`
- Codex Ratchet/current wiki context: `/Users/joshuaeisenhart/wiki/projects/codex-ratchet` and `/Users/joshuaeisenhart/wiki/concepts`, but only as comparator/provenance context unless explicitly matched.

## Shared worker rules

- Do not edit the Leviathan repo.
- Write only assigned markdown files under `projects/leviathan-current/`.
- Cite exact source paths read.
- Mark support level for every major claim: `observed file`, `inferred from docs`, `roadmap/design intent`, `chat/provenance candidate`, `legacy`, `not checked`, or `open`.
- Do not treat chat transcripts as repo truth.
- Do not treat Codex Ratchet claims as Leviathan implementation claims.
- Redact secrets if encountered; write `[REDACTED]`, not values.
- Preserve live contradictions instead of smoothing them.

## Model-routing preference

For future pressure/synthesis lanes, try OpenRouter Fusion and GLM 5.2 before Opus 4.8 when available. Treat those outputs as pressure/advisory until controller-verified against repo/wiki artifacts.

## Wave 1 workers

1. **authority-docs-worker**
   - Reads current authority docs and high-signal specs.
   - Owns: `what-is-leviathan.md`, `current-state-and-roadmap.md`, `architecture-planes-and-ownership.md`, `contract-surface-map.md`.

2. **runtime-map-worker**
   - Reads package manifests and selected core module entrypoints.
   - Owns: `runtime-module-map-start.md`, `flowmind-control-plane-start.md`, `event-graph-orchestration-start.md`.

3. **contribution-signal-worker**
   - Searches repo/wiki for Josh/Joshua/Codex Ratchet/root constraints/finitude/noncommutation/ratchet/locality/provenance signals.
   - Owns: `josh-contribution-signal-index-2026-06-17.md`.

4. **chat-provenance-worker**
   - Uses `source-inventory-2026-06-17.json` chat/transcript candidates as queue; classifies source types and first tranche candidates without claiming full transcript read.
   - Owns: `chat-provenance-queue-2026-06-17.md`.

5. **research-map-worker**
   - Inventories research-connected docs/folders and maps likely external research domains without overclaiming.
   - Owns: `research-connection-map-start.md`.

6. **assessment-falsifier-worker**
   - Independently reviews current docs/inventory for what seems strong, failing, promising, and unverified.
   - Owns: `doing-well-failing-promising-start.md`.

## Controller verification after wave

- Re-read all owned output files.
- Check exact paths exist.
- Run wiki probe.
- Patch index/front door if needed.
- Mark Packet 1 complete only if authority-doc pages exist and cite sources.
