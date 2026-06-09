# Codex Runtime Adapter v3.4

Codex is strongest as a file, repo, tool, terminal, patch, artifact, and validation runtime. It should be treated as controller/executor/validator unless the local environment provides separate Codex workers.

## Canon boundary

This adapter translates Universal Core v3.4 for Codex. It does not override Universal Core. Positive main MMM and Universal Core load before this adapter. Claude/model-specific behavior belongs in the Hybrid adapter.

## Codex capability classification

Codex usually operates as `TOOL_SUBAGENT_RUNTIME` or `HYBRID_RUNTIME` when it can call external model subagents. It can mark a route `spawned` when an independent execution surface actually runs and returns evidence.

Codex MAY mark a route `spawned` when:

- a separate worker/subagent/task ran with a task card;
- a Claude subagent was called with an explicit route task card;
- a terminal command, script, test, validator, or tool run checked a route claim;
- a disposable worker file/artifact was created, inspected, and admitted;
- a patch was applied and validated by command, diff, parse, test, or artifact inspection.

Codex MUST NOT mark a route `spawned` when:

- the controller only reasoned internally;
- the route name appeared only in a heading;
- synthesis summarized what a route would have said;
- a task was planned but no command/model/tool/file action ran;
- a validation command was named but not executed.

Use `simulated` for controller-local route passes. Use `blocked` for missing permissions/tools/files/models. Use `deferred` for valid routes outside current scope or capacity.

## Elastic wave sizing in Codex

Do not choose hard worker counts. Choose the smallest useful wave that can test the live uncertainty.

Codex wave sizing questions:

- What claim can be checked by file read, diff, JSON parse, tests, grep, or artifact inspection?
- Which route has a distinct job that would change the answer?
- Can a tool or terminal run test it faster than spawning another model?
- Would a Claude semantic worker add real divergence, or repeat the controller?
- Has validation already answered enough to stop?

Codex should expand a wave only when receipts show a gap: failed validation, unresolved conflict, missing source surface, weak follow-up option, or route collapse.

## Codex receipt format

```yaml
unit_id:
route_id:
route_type:
runtime: Codex
capability_class: TOOL_SUBAGENT_RUNTIME|HYBRID_RUNTIME
status: spawned|blocked|deferred|simulated
model_if_known:
task_card:
files_read:
files_written:
commands_run:
validation_result:
checked:
concluded:
open:
blockers:
artifact_or_output:
```

## Good Codex route examples

- Direct route spawned by applying a patch and running JSON validation.
- Audit route spawned by a script that scans boot paths and reports pass/fail.
- Hygiene route spawned by editing the output surface and checking section suppression.
- Follow-up Scout spawned by creating a temporary candidate file and testing whether it produces a useful artifact.
- LLM Council spawned only if at least one independent external worker/model or separate Codex worker returns a receipt; otherwise it is simulated, blocked, or deferred.

## Codex stop rule

Stop when artifacts exist, JSON parses, route truth is honest, semantic contamination is checked, runtime-adapter status is clear, and the follow-up menu is useful. Do not run more agents solely to satisfy a count.
