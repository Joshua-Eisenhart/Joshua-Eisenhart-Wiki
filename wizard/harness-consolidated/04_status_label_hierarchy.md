last_updated: 2026-04-17

# Status Label Hierarchy

LLM agents collapse truth distinctions. This page codifies the only four labels in use and enforces no upward inference.

## The Four Labels

Use ONLY these four labels. Never imply a higher label from a lower one.

| Label | Meaning |
|---|---|
| `exists` | File is present in repo |
| `runs` | Executes without error (exit 0) |
| `passes local rerun` | Fresh run confirms all tests pass |
| `canonical by process` | passes local rerun + SIM_TEMPLATE + tool manifest + non-empty reasons + classification field |

## The Hard Rule

**Never infer a higher label from a lower one.**

- "exists" does NOT imply "runs"
- "runs" does NOT imply "passes local rerun"
- "passes local rerun" does NOT imply "canonical by process"

## Banned Phrases

These vague synonyms obscure which criteria were checked. Do not use:
- "verified" — cite which run and which criteria
- "confirmed" — same; always name the evidence file
- "ALL PASS" or "28/28 PASS" — specify which criteria (for example F01-boundedness, N01-ordering, tool-depth, or probe-family checks) on which families
- "passes" alone — always say "passes local rerun" or "canonical by process"
- "works" or "valid" — meaningless without context
- "correct" or "true" — use "survived [constraint class]" or "indistinguishable [under probes]"

## When to Stop

If you cannot cite the specific result file and the specific criteria tested, you cannot claim a status label. Return to lower label or admit uncertainty.

## Cross-references

- See [05_four_sim_kinds.md](05_four_sim_kinds.md) for how each kind of sim earns which label
- See [06_coupling_program_order.md](06_coupling_program_order.md) for when bridge claims can be made
- See LLM_CONTROLLER_CONTRACT.md (repo) for the Claim → Evidence → Verification table pattern
