# Wizard Header / Footer Templates v3.3

## Header truth

Use headers only when they lower cognitive load. Headers must not imply execution that did not happen.

```text
Wizard: FULL | route truth: spawned {n}, blocked {n}, deferred {n} | council: {spawned|blocked|deferred} | follow-up: audited subset
```

For Full Wizard or debugging/tuning output, the header must expose worker topology:

```text
Wizard: {FULL|COMPACT} | subagents: spawned {n} / blocked {n} / deferred {n} | subsubagents: spawned {n} / blocked {n} / deferred {n} | waves: worker {n} / controller {n} / not-run {n}
Routes: voices {spawned}/{blocked}/{deferred}; lanes {spawned}/{blocked}/{deferred|future-only}; council {status}; checks {spawned}/{blocked}/{deferred}; compositions {spawned}/{blocked}/{deferred|future-only}; follow-up scout {spawned|blocked|deferred|not-run}
```

If a route family was named but no worker ran, mark it `future-only` or `not-run`. Do not hide it inside the spawned count.

If model/subagent counts are known from receipts:

```text
Subagents: codex 5.5 high {n}, opus high {n}, sonnet high {n}
```

Do not print internal transport labels in normal output.

## Compact wave-result header

```text
🌊 Wave Results: voices spawned {n} / blocked {n} / deferred {n}; council {status}; checks {status}; follow-up {audited|future-only}
```

Use this only when the wave truth materially helps the user trust the answer. Otherwise omit it.

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
