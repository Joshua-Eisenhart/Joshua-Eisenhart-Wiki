---
title: Mini-MMM Load Contract v4.1
type: mini_mmm_load_contract
packet: v4.1
framing: standalone
---

# Mini-MMM Load Contract v4.1

Subagents and subsubagents load mini-MMMs. The main thread loads the full MMM.

Main thread rule: the main/leader thread loads the main full MMM for full runs
and may load the compact main MMM only for constrained compact runs.

Worker rule: parent and child workers do not load the main full MMM or compact
main MMM by default. `compact` for a worker means the compact member mini-MMM
under `mmm/mini/compact/...`, not `mmm/main/compact/...`. Voice and non-voice
workers both prefer exact route/member mini-MMMs. If no exact mini-MMM exists,
use the sparse registry slice plus definition row, then nearest family fallback
marked `mini_mmm_family_fallback`; if none exists, block the route.

## Subagent Load Order

1. Shared positive task summary.
2. Exact route/member mini-MMM slice from `MEMBER_MINI_MMM_REGISTRY_v4_1.md`
   or exact `mmm/mini/{full,compact}/...` file when one exists.
3. Route-bound council-member skill when the member is skill-backed.
4. Assigned route definition.
5. Task card.
6. Source slice or tool surface.
7. Receipt format from `../../schemas/RECEIPT_SCHEMA_v4_1.md`.

## Subsubagent Load Order

1. Parent route summary.
2. Exact child route/member mini-MMM slice from
   `MEMBER_MINI_MMM_REGISTRY_v4_1.md` or exact
   `mmm/mini/{full,compact}/...` file when one exists.
3. Route-bound council-member skill when the member is skill-backed.
4. Child route definition.
5. Child task card.
6. Source slice or tool surface.
7. Receipt format from `../../schemas/RECEIPT_SCHEMA_v4_1.md`.

## Load Rules

- Load only the mini-MMM for the assigned route/member.
- A composition or council role may load the mini-MMMs for its selected member set.
- Do not load the full MMM into child workers by default.
- Non-voice workers use exact compact or full member mini-MMMs when present.
  They do not load the compact main MMM as a general salience base.
- Voice workers use exact voice mini-MMMs. This preserves Hume, Zhuangzi,
  Feynman, Orwell, Popper, Pushback, Factory, Strategy, and Systems as
  distinct voices.
- If no exact child mini-MMM exists, use sparse registry slice plus definition
  row. If that is insufficient, use nearest member-family fallback and mark
  `mini_mmm_family_fallback`. If no family fallback exists, block the child.
- Do not load archive, negative, banned, contrast, or reference-only MMM material into worker boot.
- If no exact mini-MMM exists, load the nearest member-family slice and mark the route `mini_mmm_family_fallback`.
- A visible member counts as run only when its worker loaded the matching mini-MMM or explicitly declared the fallback.
- A worker that did not load its assigned mini-MMM cannot be counted as that visible voice, lane, guard, or council member.
