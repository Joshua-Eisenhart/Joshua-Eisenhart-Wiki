---
title: Migration Registry
created: 2026-04-08
updated: 2026-05-21
type: concept
tags: [simulation, planning, implementation, system]
sources:
  - raw/articles/new-docs/MIGRATION_REGISTRY.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/MIGRATION_REGISTRY.md
spec_mirrors:
  - /Users/joshuaeisenhart/wiki/specs/codex-ratchet/lego-sim-contract-current.md
  - /Users/joshuaeisenhart/wiki/specs/codex-ratchet/sim-estate-integration-status.md
  - /Users/joshuaeisenhart/wiki/specs/codex-ratchet/tool-function-receipt-status.md
framing: historical_migration_snapshot
---

# Migration Registry

Bounded registry snapshot tracker for the 28 irreducible families' PyTorch migration. Cross-referenced in April against probe files in `system_v4/probes/`.

Status boundary: this is an April registry snapshot, not current migration or promotion truth. The counts below should not be used as live result counts or current torch/tool admission. Use [[specs/codex-ratchet/lego-sim-contract-current|lego-sim-contract-current]], [[specs/codex-ratchet/sim-estate-integration-status|sim-estate-integration-status]], and [[specs/codex-ratchet/tool-function-receipt-status|tool-function-receipt-status]] for current contract/status routing.

## Summary (audited 2026-04-10; wording refreshed 2026-04-11)

- **Total families**: 28
- **Torch modules on disk**: 2026-04-10 audit snapshot recorded ~30+ sim_torch_*.py files, treated as exploratory rather than promoted
- **Formally registered**: 0 in the 2026-04-10 registry snapshot — this is a registry-status statement, not a claim that no torch-side work exists
- **Baseline files exist**: 24 full, 2 partial, 2 missing
- **Template compliance**: 41.0% of result JSONs have all three required fields

## Critical Gaps

1. **2 families have NO baseline**: z\_measurement (#12), chiral\_overlap (#26) — need new baseline sims.
2. **2 families have PARTIAL baselines**: purification (#2, no standalone `purify(rho)`), unitary\_rotation (#11, no standalone rotation-as-channel).
3. **Zero families promoted** past NOT\_STARTED in the 2026-04-10 registry snapshot despite exploratory torch code existing on disk.
4. **Phase 7 "PASS" is stale** in the 2026-04-10 audit snapshot: covers C1/C3/C4 only. C2\_graph\_topology: 11/28 non-null, 17/28 null, 0/28 NOT_TESTED.

## Family Registry (selected)

| # | Family | Baseline | Negative Battery | Status |
|---|--------|----------|------------------|--------|
| 1 | density\_matrix | YES | negative\_density\_matrices | NOT\_STARTED |
| 3-10 | channels (z/x dephasing, depolarizing, etc.) | YES | negative\_channels | NOT\_STARTED |
| 13-15 | gates (CNOT, CZ, SWAP) | YES | negative\_entanglement | NOT\_STARTED |
| 25 | hopf\_connection | YES | negative\_geometry | NOT\_STARTED |
| 27-28 | mutual\_information, quantum\_discord | YES | negative\_entropy\_boundaries | NOT\_STARTED |

## Promotion Status Definitions

- **NOT\_STARTED** — no torch module exists (or exists but unvalidated)
- **BASELINE\_ONLY** — numpy baseline passes, no torch code
- **TORCH\_DRAFT** — torch written, not tested against baseline
- **TORCH\_TESTED** — torch matches baseline + negative battery confirmed
- **CANONICAL** — integrated into constraint graph, ready for Phase 4+

## Negative Battery Coverage

All 5 negative battery files exist and cover all 28 families:
- `sim_negative_density_matrices.py` — families #1, 2, 20, 21, 24
- `sim_negative_channels.py` — families #3-12, 16, 17
- `sim_negative_entanglement.py` — families #13-15, 18, 19
- `sim_negative_entropy_boundaries.py` — families #22, 23, 27, 28
- `sim_negative_geometry.py` — families #25, 26

## Related Pages

- [[pytorch-ratchet-build-plan]] — Phase 3 migration plan
- [[battery-index]] — negative battery catalog
- [[enforcement-and-process-rules]] — two-lane quality policy (Rule 5)
- [[specs/codex-ratchet/lego-sim-contract-current]]
- [[specs/codex-ratchet/sim-estate-integration-status]]
- [[aligned-sim-backlog-and-build-order]] — build ordering
