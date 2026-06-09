---
title: Wizard v4.0 Claude Adapter
type: runtime_adapter
packet: v4.0
runtime: claude
framing: standalone
---

# Claude Adapter

This adapter binds the universal Wizard to Claude-style workflows.

These are Claude-specific runtime rules. They are not universal Wizard requirements.

## Main Thread

The main Claude thread loads:

1. `mmm/FULL_MMM_v4_0.md`;
2. boot/core docs;
3. user task and source material;
4. this adapter when using Claude workers or Claude Code.

The main thread owns synthesis and visible claims.

## Claude Workers

Use separate Claude workers or tool tasks when a visible member needs real independent work.

Each worker should receive:

- shared task summary;
- exact mini-MMM slice;
- route/member task card;
- source slice;
- receipt schema.

## Claude Code

When Claude Code has file or tool access, it may produce execution receipts.

When it does not have file or tool access, it returns semantic analysis, critique, or proposed patches only.

Do not count semantic prose as execution.

## Expert And Failure Lenses

Claude is useful for:

- premortem and postmortem narrative pressure;
- expert critique;
- outside evaluator framing;
- wording and synthesis;
- long-context source comparison.

These still need receipts if the output claims a member ran.

## Output

Keep the answer readable.

Show what changed the decision, what is blocked, and the best next prompts. Keep raw transcripts hidden unless requested.
