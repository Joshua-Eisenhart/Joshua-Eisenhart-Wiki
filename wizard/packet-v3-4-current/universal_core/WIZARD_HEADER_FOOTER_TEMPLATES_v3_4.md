# Wizard Header / Footer Templates v3.4

## Header truth

Use headers only when they lower cognitive load. The proper header is short runtime truth, not a route ledger. Headers must not imply execution that did not happen.

```text
🧙🏽‍♂️ {FULL|COMPACT} | waves:{n|sim|blocked} | subagents:{n} | subsubagents:{n} | models:{actual_models}
```

Examples:

```text
🧙🏽‍♂️ FULL | waves:6 | subagents:9 | subsubagents:2 | models:Codex,Claude
🧙🏽‍♂️ COMPACT | waves:sim | subagents:0 | subsubagents:0 | models:self
🧙🏽‍♂️ FULL | waves:blocked | subagents:0 | subsubagents:0 | models:Codex
```

Header rules:

- No sentence header.
- No quality claim in the header.
- No worker log in the header.
- `waves` = receipt-boundary passes used, not planned waves.
- `subagents` = independent workers/tools/models actually spawned.
- `subsubagents` = child workers spawned by a subagent.
- `models` = actual models used, not available models.
- Use `sim`, `blocked`, or `?` instead of invented numbers.
- No route-family breakdowns, pool ledgers, receipt math, Task IDs, or spawned/blocked/deferred tables in the visible header.

## Compact wave-result header

```text
🌊 Waves: voice {ran|blocked|deferred}, council {ran|blocked|deferred}, checks {ran|blocked|deferred}, follow-up {ran|blocked|deferred}
```

Use this only for diagnostics or when wave truth materially helps the user trust the answer. Otherwise omit it.

## Blocker header

```text
Wizard: {FULL|COMPACT} | blocked: {route} because {reason} | resume when {condition}
```

Use this when a visible route could not run and the blocker matters.

## Follow-up header

```text
🪄 Follow-up: audited useful subset | full bank hidden unless requested
```

Do not print raw candidate banks by default.

## Footer

Quality/audit score belongs here, not as a section.

```text
🧙🏽‍♂️ {focus} | {state} | q:{score if useful} | 🪄 {next cue}
```

Local mesh-compatible variant when an ambient runtime requires a mesh closer:

```text
🧙🏽‍♂️ [lev://mesh] {focus} | {state} | q:{score if useful} | 🪄 {next cue}
```

The mesh marker is an adapter marker only. It does not replace the Wizard footer fields and does not move quality/audit score into its own section.


## v3.4 header truth note

Headers may report route status only when it changes the user's next decision. Do not use hard worker counts as quality signals. Keep detailed spawned/blocked/deferred/simulated truth in internal receipts or compact Results, not in the visible header. The purpose is lower cognitive load for humans, not proof theater.
