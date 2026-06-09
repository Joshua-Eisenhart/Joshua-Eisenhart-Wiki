---
title: LLM Controller Contract Current Mirror
created: 2026-05-21
updated: 2026-05-21
type: contract-mirror
framing: current_snapshot
tags: [specs, codex-ratchet, controller, evidence, status-labels]
sources:
  - /Users/joshuaeisenhart/Codex-Ratchet/system_v5/docs/LLM_CONTROLLER_CONTRACT.md
  - /Users/joshuaeisenhart/Codex-Ratchet/system_v5/docs/ENFORCEMENT_AND_PROCESS_RULES.md
---

# LLM Controller Contract Current Mirror

This is a spec-side mirror of the live repo LLM controller contract. It is a routing and salience surface, not the authority itself.

Authoritative source: `system_v5/docs/LLM_CONTROLLER_CONTRACT.md`.

## Core Failure Mode

The named controller failure is narrative substitution for gate obedience: a plausible story feels like the rule, but the rule requires a cited gate criterion and a cited result file from the current session.

If the file cannot be cited, the gate is not satisfied. The controller should report the blocked gate and the evidence needed.

## Required Status Labels

Use only these public repo truth labels:

| label | meaning | proof |
|---|---|---|
| `exists` | file or result present | `ls` or `git status` evidence |
| `runs` | file executes without error | local rerun exit code `0` |
| `passes local rerun` | expected tests pass | fresh run output confirms it |
| `canonical by process` | local rerun plus template/tool/depth requirements | SIM_TEMPLATE, tool manifest, `classification`, and pass evidence |

Do not collapse these labels into `verified`, `canonical`, or broad completion language.

## Evidence Table Rule

Before making broad repo-state claims, fill a claim/evidence/verification table with:

- claim;
- source file;
- result path;
- exact criteria checked;
- status label.

A pass on one criterion cannot imply a pass on all criteria.

## Hard Build Guardrail

The controller must preserve the same hard stage order as [[specs/codex-ratchet/enforcement-process-rules-current|Enforcement Process Rules Current Mirror]]:

- tool sims first;
- micro tool/function probes before tool-lego or tool-tool coupling;
- lego sims across the registry;
- classical baselines as baseline/control evidence only;
- coupling/coexistence only after parent evidence, except explicit bounded no-promotion exceptions;
- bridge/axis/engine work late and gated.

## Sim-Mode Full Wizard Parallelism

For sim/proof/tool-stage work, Full Wizard is the default admission and parallelization mechanism. It is invalid to narrow to one tool or one packet before real parallel preflight has checked other independent tool surfaces, unless the user explicitly asked for that one named tool.

Accepted sim-mode closeout must distinguish:

- authored or queued packet;
- runner-executed result;
- receipt-backed ledger update;
- blocked or deferred tool surfaces;
- follow-up options that were actually made, scouted, and audited.

## Evidence Tracks Never Merge

Foundation migration, seam proof depth, and stack/nesting sims do not aggregate. A breakthrough in one track does not close another track, and none of them overrides the hard stage gate.

## Hard Stops

- No registry/doc status edits before the code/result gate is satisfied and cited.
- No broad coupling/coexistence/topology/emergence/bridge/axis queueing merely because exploratory coupling exists.
- No debugging stacked uncertainty: if a compound packet fails and a participating tool function lacks a useful-lego receipt, decompose first.
- No `canonical` claim without SIM_TEMPLATE, non-empty tool manifest reasons, `classification`, and fresh local pass evidence.
- No absolute repo-state claim without current-session file or command evidence.

## Worker Contract

Agents get bounded tasks and explicit deliverables. They may write, repair, audit, and enqueue bounded probes, but executable evidence comes from Python runner outputs and result JSONs. Controller consolidation must verify worker claims against result files.

Micro tool-stage worker prompts must name the exact tool/function/API surface, lego target, one allowed variable of uncertainty, out-of-scope claims, and ledger loopback.

## Block K Closeout

Every controller session ends with Block K from `~/wiki/harness/24_closeout_templates.md`. Missing fields make closeout incomplete, not finished.

Block K must carry gates cited, admission decisions, narrative substitutions intercepted, worker claims verified/not verified, status-label changes, and blocked actions.

## Claim Ceiling

This mirror supports controller discipline and wiki routing. It does not validate any worker claim, sim result, or repo status by itself.

Concept mirror: [[llm-controller-contract]].
