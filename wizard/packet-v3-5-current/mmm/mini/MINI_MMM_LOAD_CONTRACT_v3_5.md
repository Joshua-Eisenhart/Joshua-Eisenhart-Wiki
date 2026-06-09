---
title: Mini-MMM Load Contract v3.5
type: mini_mmm_load_contract
packet: v3.5
framing: current
---

# Mini-MMM Load Contract v3.5

Subagents and subsubagents load mini-MMMs. The main thread loads the full MMM.

## Subagent Load Order

1. Shared positive task summary.
2. Exact route/member mini-MMM, or the matching member slice from `MEMBER_MINI_MMM_REGISTRY_v3_5.md`.
3. Assigned route definition.
4. Task card.
5. Source slice or tool surface.
6. Receipt format.

## Subsubagent Load Order

1. Parent route summary.
2. Exact child route/member mini-MMM, or the matching member slice from `MEMBER_MINI_MMM_REGISTRY_v3_5.md`.
3. Child route definition.
4. Child task card.
5. Source slice or tool surface.
6. Receipt format.

## Load Rules

- Load only the mini-MMM for the assigned route/member.
- A composition or council role may load the mini-MMMs for its selected member set.
- Do not load the full MMM into child workers by default.
- Do not load archive, negative, banned, contrast, or reference-only MMM material into worker boot.
- If no exact mini-MMM exists, load the nearest member-family slice and mark the route `mini_mmm_family_fallback`.
- A visible member counts as run only when its worker loaded the matching mini-MMM or explicitly declared the fallback.
