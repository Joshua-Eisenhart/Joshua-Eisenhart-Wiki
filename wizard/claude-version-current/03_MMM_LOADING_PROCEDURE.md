---
title: Claude Code Wizard — MMM Loading Procedure
type: loading_procedure
runtime: claude_code
created: 2026-06-13
updated: 2026-06-13
---

# MMM Loading Procedure

Per PANEL REVISION 4: specify a token-budget + eviction protocol, not only a Read order. Note that "exact Read order" is a target the runtime may not follow literally.

---

## MMM sizes (as of 2026-06-13)

| File | Lines | Estimated tokens | Role |
|---|---|---|---|
| `../packet-v4-3-current/mmm/FULL_MMM_v4_3.md` | ~36,826 | ~28,000–32,000 | Full positive reservoir; too large for most context budgets |
| `../packet-v4-3-current/mmm/COMPACT_MMM_v4_3.md` | ~4,699 | ~3,500–4,500 | Compact positive reservoir; **COMPACT-first default** |
| `../packet-v4-3-current/mmm/mini/<role>/` | ~200–800 each | ~150–600 each | Per-role mini-MMMs; load assigned mini + required_mini_mmms only |
| `../packet-v4-3-current/mmm/mini/MEMBER_MINI_MMM_REGISTRY_v4_3.md` | small | ~400–600 | Registry of available mini-MMMs; load to pick, not to run all |

Claude context windows compact automatically. A 36k-line file loaded early will be evicted before later tool results arrive. The procedure below accounts for this.

---

## Token-budget rule

Assign a token budget before loading any MMM. The exact figure depends on the model and task, but a working default:

```
total_context_budget: (model context limit) - (task prompt) - (expected tool results) - (output reserve)
mmm_budget: min(total_context_budget * 0.20, 5000 tokens)
```

If `mmm_budget < 800 tokens`, skip the MMM and proceed with inline notes only — a too-small MMM window degrades more than it helps.

---

## COMPACT-first default

Load COMPACT MMM unless the budget explicitly allows FULL. Never load both in the same context window.

```
if mmm_budget >= 3500:
    load COMPACT_MMM_v4_3.md
    # do not also load FULL_MMM_v4_3.md
elif mmm_budget >= 800:
    load the first N lines of COMPACT_MMM_v4_3.md until budget is consumed
else:
    skip MMM; use inline notes
```

Load FULL MMM only when:
- The budget explicitly allows (rare: task is purely MMM-alignment work, no large tool results expected), AND
- The controller has confirmed the full file will not be evicted before use.

In practice, FULL MMM fits only in sessions where the MMM itself is the primary workload. Default to COMPACT.

---

## Eviction protocol — which slices drop first

Claude compacts context from the oldest/least-recently-attended material. The MMM is loaded early in the prompt, making it the first candidate for eviction when context fills.

Priority-preserve order (preserve these last):
1. Current task prompt and live receipts — never evict.
2. `00_READ_FIRST.md` and `01_RUNTIME_CONTRACT.md` — authority + compile gate.
3. Assigned mini-MMM and `required_mini_mmms` — role-specific salience for the active lane.
4. COMPACT MMM — positive reservoir for the main agent.

Drop first (earliest to be lost to context compaction):
1. FULL MMM (if it was ever loaded) — too large to protect.
2. Mini-MMMs for roles NOT currently active.
3. Prior session context and handoff notes (after key facts extracted).
4. Provenance / historical packet notes.

Implication: if tool results are large, the MMM may be partially or fully evicted before the synthesis step. The controller must re-inject key MMM phrases inline in the task card rather than assuming the model retained the full reservoir.

---

## Read target order (target, not a guarantee)

This is the intended order. The runtime (context compaction, token limits) may not preserve all of it:

1. `../packet-v4-3-current/README.md` — v4.3 packet front door.
2. `../packet-v4-3-current/mmm/COMPACT_MMM_v4_3.md` — COMPACT-first; skip or truncate if budget is tight.
3. `../packet-v4-3-current/mmm/mini/MEMBER_MINI_MMM_REGISTRY_v4_3.md` — identify which mini-MMMs are assigned to active lanes; do not load all.
4. Assigned mini-MMM(s) for the current lane/voice.
5. `../packet-v4-3-current/WIZARD_v4_3.md` — council topology and runtime rules.
6. This folder's `00_READ_FIRST.md` + `01_RUNTIME_CONTRACT.md` + `02_TOOL_ADVANTAGE_MAP.md`.
7. Task card and live receipts.

"Exact Read order" means the controller issues Reads in this sequence. It does not mean the model's effective attention over the loaded content follows this sequence — context compaction may reorder salience. This is a target, not a guarantee.

---

## Child-Agent prompt template

When the main controller spawns a child `Agent` for a council voice, sim-runner, auditor, or scout, the child does NOT receive the main agent's full MMM. The child receives:

1. A task card (goal, scope, out_of_scope, acceptance, key_paths, read_first, deliverable, closeout_check).
2. The COMPACT MMM embedded inline (verbatim or summarized — choose based on child's budget).
3. The assigned mini-MMM for the child's role (verbatim).
4. The `required_mini_mmms` list with reasons.

### Template

```yaml
# Child Agent Task Card — Claude Wizard v4.3

runtime: claude_code
action_class: spawn_subagent
parent_controller: <session/task id>

## Task card

goal: <one sentence; what the child must decide or produce>
scope: <what is in scope>
out_of_scope: <what must not be touched or claimed>
acceptance: <the checkable criterion for done>
key_paths: <files to read; receipts to return>
read_first:
  - <path 1>
  - <path 2>
deliverable: <artifact path or structured receipt the parent will read>
closeout_check: <what the parent will verify to confirm the child's claim>

## MMM — COMPACT (embedded)

# [Paste verbatim content of COMPACT_MMM_v4_3.md here, or summarize if budget is tight]
# Budget rule: if embedding would exceed child token budget, include only the first 100 lines
# of COMPACT plus the saliency patch (lines 1–30 of the compact file).

## Assigned mini-MMM

role: <voice name | lane name | audit type>
# [Paste verbatim content of the assigned mini-MMM here]

## Required mini-MMMs

required_mini_mmms:
  - path: <../packet-v4-3-current/mmm/mini/<role>/<file>>
    why: <one sentence — what failure mode this mini-MMM prevents for this child>
  - path: <...>
    why: <...>

## Hard constraints (child must not violate these)

- Do NOT run git commands.
- Do NOT write to any file outside the declared deliverable path.
- Do NOT claim a route ran without a receipt.
- Do NOT promote a claim beyond what the receipt supports.
- Return honest status labels: exists < runs < passes local rerun < canonical by process.
- Bottom-line-first in the final message.
- The builder does not audit its own work; if an audit is part of this task, state explicitly that this child IS or IS NOT the audit context.
```

---

## Mini-MMM selection rules

- Each active council voice gets its own assigned mini-MMM from `../packet-v4-3-current/mmm/mini/<compact|full>/voices/md/`.
- A lane-level task (controller_acts, compositions, system_routes) gets the matching mini from the lane category.
- The `required_mini_mmms` list names additional mini-MMMs the child should load because the task crosses multiple failure modes (e.g., a Failure voice may also need a checks_guard mini if the task is a boundary check).
- The reason for each required mini-MMM must be stated. "It might be useful" is not a reason. Name the specific failure mode the mini-MMM guards against for this task.

---

## What this procedure does not cover

- FULL MMM loading in live multi-tool sessions: avoid unless the session is dedicated MMM-alignment work.
- Mini-MMM registry maintenance: the registry lives at `../packet-v4-3-current/mmm/mini/MEMBER_MINI_MMM_REGISTRY_v4_3.md`; updates to it require the maintenance governor.
- Context compaction internals: Claude's compaction algorithm is not directly inspectable. The eviction protocol above is a design target, not a verifiable guarantee.
