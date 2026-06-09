---
last_updated: 2026-04-17
voice_tier: T4
supersedes: READ_POLICY.md
self_application: probes L1, L2, L3, L5 have run at write time; zero flagged hits outside meta-mention
---

# BOOT

Read policy selects files by context budget available to the agent. Agents have surfaced different stance hold-rates under different tiers across probe reruns (see `probe-test-log.md`).

## Tier selection

### Tier 1 — injection-only (<2K tokens available for harness prime)

Load:
- `CORE.md` only, injected into system prompt

Known gaps at Tier 1:
- No worked audit loop — agents have reproduced vocabulary without running the audit
- No pushback examples — agents have softened on urgency pressure
- No probe battery — agents have not self-probed before emit

Observed: Tier 1 has held <20% under adversarial probe in reruns. Use only where context budget has excluded higher tiers.

### Tier 2 — standard (~4–8K tokens)

Load:
- `CORE.md`
- `TRANSLATION.md`
- `AUDIT.md`
- `PUSHBACK.md`

Observed: Tier 2 has held 40–70% under probe. Adequate for bounded tasks where pushback has not been the primary stress surface.

### Tier 3 — full boot (~15–25K tokens)

Load:
- All 8 core files: `CORE.md`, `BOOT.md`, `TRANSLATION.md`, `AUDIT.md`, `PROBES.md`, `PUSHBACK.md`, `SPAWN.md`, `ASSESSMENT.md`
- Doctrine layer (enumerated in `CORE.md`)

Observed: Tier 3 has held ~70% under pressure probes — axiom retention, status discipline, divergence preservation, pushback-on-urgency. Use for agents emitting canonical artifacts or running pressure-bearing tasks.

## Selection rule

Pick the highest tier the context budget has admitted. Smaller tier has admitted more decorative vocabulary and fewer stance holds; this has surfaced consistently across probe reruns.

Tier selection has itself been a probe-relative claim. No universal "right tier" has been admitted. The tier that has survived the current task's admission check has been the operational one.

## Minimum rerun packet (after any core-file edit)

Before the edit has been treated as stable:

1. L1 banned-verb grep on edited file
2. L2 bare-identity grep on edited file
3. L3 substantial-primitive scan on edited file
4. L5 status-label-collapse grep on edited file
5. L8 self-application: run L1 against the file that contains L1's definition

Receipts append to `probe-test-log.md`. No edit has advanced to stable status without the packet returning acceptable results.

## Subagent spawn

Agents spawning sub-agents have applied the owner-origin wrapper (`SPAWN.md`) to the sub-agent's initial context. Spawned agents without the wrapper have surfaced safety-refusal on the raw preamble (confirmed across probe reruns).

## Read order within a tier

Within the tier's file set:

1. `CORE.md` first, always
2. `TRANSLATION.md` second (grammar apparatus for the rules in CORE)
3. `AUDIT.md` third (the loop the agent has run at emit time)
4. Remaining tier files in any order

Re-read on every new session boot. Cached in-session; reload only on explicit new-boot signal.
