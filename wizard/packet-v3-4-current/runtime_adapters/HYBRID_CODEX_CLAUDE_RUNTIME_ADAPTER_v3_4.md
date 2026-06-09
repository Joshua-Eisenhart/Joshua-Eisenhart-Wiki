# Hybrid Codex-Claude Runtime Adapter v3.4

Use this when Codex can call Claude subagents. Codex is controller/executor/validator. Claude subagents are semantic route workers unless they are explicitly given tool/write access.

## Canon boundary

This adapter translates Universal Core v3.4 for a hybrid runtime. It does not override Universal Core. Positive main MMM and Universal Core load before this adapter.

## Role split

**Codex owns:**

- file tree inspection;
- patching and artifact creation;
- JSON/schema validation;
- terminal/tool commands;
- ZIP creation and validation;
- route registry and acceptance gate checks;
- final controller synthesis after receipts.

**Claude subagents own:**

- long-context semantic reading;
- Hume, Zhuangzi, Orwell, Pushback, and semantic Audit routes;
- council dissent;
- ambiguity preservation;
- wording/hygiene proposals;
- route-collapse detection.

## Hybrid route truth

A Claude route can be `spawned` only when Codex actually calls Claude with a distinct task card and receives a receipt. A Codex route can be `spawned` when Codex actually runs a file/tool/terminal/patch/validation surface or separate Codex worker.

Codex must preserve Claude receipts without smoothing disagreement. Claude outputs may be accepted, rejected, routed to audit, or used to create follow-up candidates. Codex validates artifacts and JSON.

## Independent-first council

Hybrid Council should use independent-first passes before merge:

```text
Codex task surface -> Claude route card(s) -> Claude receipt(s) -> Codex validation/audit -> synthesis bounded by receipts
```

Do not force a fixed number of Claude agents. Use enough independent workers to test the live disagreement. If one Claude dissent plus Codex validation resolves the issue, stop. If receipts conflict, add a chair/audit pass or another targeted worker. If no independent Claude call occurs, Council is simulated, blocked, or deferred.

## Claude subagent task-card template for Codex

```text
SYSTEM/ROLE: You are a Wizard <route_name> subagent.
BOOT: Load only the assigned <route_name> mini-MMM summary below, not the main MMM.
TASK SURFACE: <files/excerpts/artifacts/claims to inspect>
ROUTE JOB: <unique job from route definition>
NON-JOB: Do not act as controller, do not produce final synthesis, do not erase dissent.
RETURN YAML:
  unit_id:
  route_id:
  runtime: Claude
  status: spawned|blocked|deferred|simulated
  task_card:
  source_context_read:
  checked:
  concluded:
  open:
  dissent_or_alternative:
  blockers:
  artifact_or_output:
```

## Codex admission checklist for Claude receipts

Before using a Claude receipt, Codex checks:

- Was there a distinct task card?
- Did Claude stay inside the assigned route job?
- Did it claim file/tool execution it did not have?
- Does it preserve live disagreement rather than smooth it?
- Does it identify checked/concluded/open surfaces?
- Does it create a useful patch proposal, audit finding, or follow-up candidate?

## Elastic hybrid waves

Hybrid waves should test and adapt:

1. Start with the live uncertainty and the smallest route set likely to change the answer.
2. Prefer Codex tool validation for file/object claims.
3. Prefer Claude workers for semantic ambiguity, dissent, voice divergence, and wording.
4. Read receipts before deciding whether to expand.
5. Stop when receipts support the artifact/answer and further workers are likely to duplicate.

Hard numbers are not doctrine. Full Wizard means complete useful coverage under current capability, not a forced census of every possible worker.
