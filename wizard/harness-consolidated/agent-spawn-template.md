last_updated: 2026-04-17

# Agent Spawn Template

Canonical wrapper for spawning subagents under the harness. Solves the failure mode where raw preamble injection trips a subagent's prompt-injection safety filter (see `probe-test-log.md` 2026-04-17).

## Why the wrapper exists

A fresh subagent has no trust context for an anonymous "Harness preamble. ..." string. It can read that as an adversarial injection and refuse. Wrapping with owner-origin framing + harness file paths on disk keeps the provenance inspectable.

## Wrapper

Prepend this block to any subagent prompt that would otherwise use a raw preamble:

```
This is a legitimate harness-directed task for the Codex Ratchet project, owned by joshua.eisenhart@gmail.com. The active Wizard harness lives at /Users/joshuaeisenhart/wiki/wizard/ on disk; nominalist-CS support material lives at /Users/joshuaeisenhart/wiki/wizard/harness-consolidated/. You may inspect those paths to confirm provenance. The preamble below is drawn from SALIENCE_PREAMBLE.md in the consolidated harness directory.

[BLOCK A or BLOCK B or BLOCK C, depending on task tier]

Task (harness rules above apply):

[actual task here]
```

## Tier selection

Match the block to `READ_POLICY.md`:

- Tier 1 (hygiene only, short replies, sub-subagents): wrapper + Block A
- Tier 2 (analysis, drafting, code review): wrapper + Block B, and instruct the agent to read `SALIENCE_LOADER.md`, `03_language_discipline.md`, `16_dictionary.md`, `19_grammar.md`
- Tier 3 (canonical sim, doctrine, coordination): wrapper + Block B, and instruct the agent to follow `00_READ_FIRST.md` in full
- Model floor from current project memory: use Sonnet by default for spawned agents; reserve Opus for heavier judgment; keep older Haiku probe notes as historical, not as model guidance.

## When NOT to use the wrapper

- when the parent agent itself does the work (no subagent spawn) — the parent is already under `CLAUDE.md` preamble and doesn't need the wrapper
- when the subagent is a scripted tool call with no LLM reasoning — the wrapper does nothing useful

## Validation

Before relying on a spawned subagent's output, check:

1. did the subagent read the files named for its tier? (look for Read tool calls in its output)
2. did the subagent cite the earned status label? (not "all pass", not "verified")
3. did the subagent preserve surviving alternatives when divergence was present?

If any check fails, rerun the subagent with a stricter tier.

## See also

- `SALIENCE_PREAMBLE.md` (source of Blocks A/B/C)
- `READ_POLICY.md` (tier selection)
- `probe-test-log.md` (safety-refusal failure mode that motivated this template)
- `13_mandatory_pushback.md` (subagent obligations under conflict)
