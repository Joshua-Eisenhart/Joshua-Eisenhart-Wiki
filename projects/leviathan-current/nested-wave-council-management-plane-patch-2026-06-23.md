---
title: Nested Wave Council Management Plane Patch
created: 2026-06-23
updated: 2026-06-23
type: patch-note
status: patch_preserved_not_applied
source_repo: /Users/joshuaeisenhart/GitHub/lev
codex_memory_packet: /Users/joshuaeisenhart/wiki/codex-memory/context_packets/2026-06-23-lev-nested-wave-council-management-patch/README.md
patch_file: /Users/joshuaeisenhart/wiki/codex-memory/context_packets/2026-06-23-lev-nested-wave-council-management-patch/lev-nested-wave-council-management-selected.patch
patch_sha256: 5527cbac266b31f34cb39033d7312b83dab7175ab7fda27c0b72a83e1b2a9d82
claim_ceiling: conceptual and code patch preservation; not merged Lev canon
---

# Nested Wave Council Management Plane Patch

## One-sentence frame

Lev should treat Wizard-style runs as sequenced waves where each wave is a nested set of councils, while a parallel management plane handles resources, context loading, laggards, rerouting, gates, receipts, and failure routing.

## Corrected hierarchy

```text
Run / Wizard
  -> Waves
      -> Councils
          -> subcouncils / teams
              -> agents
                  -> skills + MMMs + tools + source packs
```

The earlier error was calling too many council functions "waves." Axiom digging, constraint digging, gate digging, premortem, source lock, evidence binding, and Ponytail/Krypton checks are usually councils or subcouncils. A wave is the larger coordinated phase containing them.

## Management plane

The work plane needs a sidecar management plane:

```text
Operations Council
  - Run Conductor
  - Resource Manager
  - Laggard Monitor

Context Council
  - Skill Loader
  - MMM Loader
  - Source Pack Loader
  - Object Card Guard

Gate / Receipt Council
  - GateOps
  - Receipt Manager
  - Evidence Binder
  - Claim Ceiling Watcher

Reroute Council
  - Failure Packet Router
  - Provider Rerouter
  - Repair Dispatcher
  - Human Escalation Router
```

These agents are not random problem solvers. They manage execution reality: quota, model choice, stalled branches, missing context, failed gates, source refs, receipts, and requeue routing.

## Gate relationship

```text
failed gate
  -> FailurePacket
  -> GateToWaveRoute
  -> repair council / repair wave
  -> evidence-bound retry
  -> host gate / receipt
```

Useful examples:

```text
object_binding failed       -> object/source binding council
evidence_manifest failed    -> evidence/source-pack council
falsifier failed            -> premortem/falsifier council
overclaim failed            -> Ponytail/Krypton claim-narrowing council
scope failed                -> scoping/decision council
feasibility failed          -> resource/tool/provider repair council
progress failed             -> follow-up / next-ratchet council
basin drift detected        -> attractor-basin / constraint council
```

## Preserved patch bundle

The selected patch is preserved in Codex memory, not applied here as canon:

```text
/Users/joshuaeisenhart/wiki/codex-memory/context_packets/2026-06-23-lev-nested-wave-council-management-patch/
```

Patch integrity:

```text
sha256  5527cbac266b31f34cb39033d7312b83dab7175ab7fda27c0b72a83e1b2a9d82  lev-nested-wave-council-management-selected.patch
```

## Claim ceiling

This is a patch candidate and architecture memory. It does not prove full Lev functionality, full nested council runtime, full skill/MMM loading, or production host admission. It preserves the upgrade direction so it can be reviewed, split, tested, and promoted deliberately.
