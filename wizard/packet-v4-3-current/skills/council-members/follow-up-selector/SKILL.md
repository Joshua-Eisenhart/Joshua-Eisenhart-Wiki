# Follow-Up Selector Skill v4.3

authority_status: canonical-skill

The Follow-Up Council selects and edits next-move categories.

Allowed actions on options:

- keep
- merge
- kill
- rewrite

Do not duplicate Follow-Up Options. Explain selection logic; let the options section show the prompts/actions.

## Method

1. Read the compiled answer and the strategy carry-forward.
2. Generate possible next-move categories, not final prose first.
3. Apply one action to each candidate: keep, merge, kill, or rewrite.
4. Preserve only options with distinct payoff and use condition.
5. Reject options that are only receipt inspection, route bookkeeping, or generic “audit more” unless diagnostics are the actual user need.

## Output Boundary

The Follow-Up Council reports why a next-move type is useful. It does not repeat the final Follow-Up Options section. If its text could be copied into the options section without change, it failed.

## Return Fields

- option action: keep, merge, kill, or rewrite;
- selected next-move category;
- context preserved;
- rejected option and reason;
- final option patch.

Also include the common child receipt fields required by `WIZARD_v4_3.md`.
