---
title: Research Ratchet wiki update manifest — 2026-06-21
created: 2026-06-21
updated: 2026-06-21
type: manifest
status: update-manifest
claim_ceiling: update manifest only
tags: [research-ratchet, wiki-update, spinor-memory, attractor-basin, leviathan]
---

# Research Ratchet wiki update manifest — 2026-06-21

## Added pages

- [[projects/research-ratchet/read-first-2026-06-21]]
- [[projects/research-ratchet/world-model-graph-patch-2026-06-21]]
- [[projects/research-ratchet/spinor-memory-and-attractor-basin-digger-2026-06-21]]
- [[projects/research-ratchet/leviathan-deep-patch-plan-2026-06-21]]
- [[projects/research-ratchet/codex-sim-basin-dynamics-plan-2026-06-21]]
- [[projects/research-ratchet/claimgate-authority-state-machine-2026-06-21]]
- [[concepts/spinor-memory]]
- [[concepts/attractor-basin-digger]]

## Consolidated thesis

The deep patch is not just a memory feature. It is a **world-model graph-patch harness**:

```text
proposal graph patch
  -> authority/admission gate
  -> ACT / ObservedEffect
  -> Eval measurements
  -> receipt / proof refs
  -> accepted successor graph state
  -> SpinorMemory orientation update
  -> AttractorBasinMap update
  -> ColdStartPacket
```

## Key design rulings

1. Spinor Memory is JSON-first oriented project-state memory in v0.
2. Attractor Basin Digger is a basin-stability classifier, not an authority engine.
3. Gates are typed operators.
4. Proposals are graph patches.
5. Receipts are state-transition seals.
6. Codex sims are basin/operator probes.
7. ClaimGate remains authority spine.
8. Leviathan owns runtime/effect/eval/ledger integration.
9. Wiki pages are routers/overlays unless repo receipts promote them.
10. Topic map/index should be updated only by a separate navigation-edit pass if desired; this pass avoids destructive replacement of long navigation pages.

## Local verification

Two source packages were executed locally before this consolidation:

```text
research-ratchet-spinor-memory-v0: npm test -> passed
ClaimGate v41 enforcing trust root + spinor memory: npm test -> passed
```
