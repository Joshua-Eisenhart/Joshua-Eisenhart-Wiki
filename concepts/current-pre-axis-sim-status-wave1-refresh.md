---
title: Current Pre-Axis Sim Status Wave1 Refresh
created: 2026-04-07
updated: 2026-05-21
type: summary
tags: [reference, research, simulation, status]
sources:
  - raw/articles/new-docs/archive_old/CURRENT_PRE_AXIS_SIM_STATUS__WAVE1_REFRESH.md
spec_mirrors:
  - /Users/joshuaeisenhart/wiki/specs/codex-ratchet/sim-estate-integration-status.md
  - /Users/joshuaeisenhart/wiki/specs/codex-ratchet/formal-scout-readiness-status.md
  - /Users/joshuaeisenhart/wiki/specs/codex-ratchet/lego-sim-contract-current.md
framing: historical_preaxis_snapshot
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Current Pre-Axis Status Wave 1 Refresh

## Overview
Short refresh note dated 2026-04-04. Does NOT claim closure. Supplements [[current-pre-axis-sim-status-keep-open-diagnostic-broken]] with post-wave-1 status.

Status boundary: this is a 2026-04-04 refresh note, not current live status. The open/closed language below belongs to that wave unless a current spec mirror or fresh repo receipt says otherwise.

Artifact availability note: this page cites April result names such as `edge_state_writeback_results.json` and `operator_basis_search_results.json`. Those exact filenames were not present in the current checkout during the 2026-05-21 wiki audit, so restore or locate archival receipts before citing them as evidence.

## 2026-04-04 Wave 1 Recorded Facts
- Edge writeback: source snapshot reported artifact confirmation (`edge_state_writeback_results.json`: 8 hits, 0 misses, 50% admissibility written); current checkout receipt was not linked/found in the 2026-05-21 audit.
- Type2 Weyl inversion: remains open (type2.fully_matches=false in operator_basis_search_results.json)
- Xi bridge: remains open as dedicated sim layer
- C1 currently fails as a witness -- MI, concurrence, and negativity do not produce non-classical binding
- Tiers 0-2 still lack a final owner law, but lower-tier transport/chirality signals are mechanically active and tier 2 has an admitted local carrier

## What This Note Does NOT Claim
No Axis-entry closure, no Tier 5 closure, no C1 closure, no Type2 Weyl inversion resolution, no claim that pointwise and history-window families should be merged.

## Related pages
- [[current-pre-axis-sim-status-keep-open-diagnostic-broken]]
- [[current-preaxis-status-and-ordering-note]]
- [[current-pre-axis-wave2-validation-note]]
