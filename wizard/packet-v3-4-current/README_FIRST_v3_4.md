# MMM Wizard Clean System Packet v3.4

This is the runtime-adaptable v3.4 packet. It uses only FULL and COMPACT sizes, adds runtime adapters as translation layers, hardens main boot MMM semantic contamination, and adds elastic wave/subagent sizing.

## Boot order

1. Load positive main MMM for the main agent.
2. Load the selected universal core.
3. Load route registry and acceptance gates.
4. Load a runtime adapter only when the local system needs one.
5. Load the task surface.

Main agent loads `mmm/main/...` only. Main agent does not load all voice mini-MMMs or preload all mini-MMMs. Subagents load only their assigned `mmm/mini/...` route. Subagents do not load the main MMM. Subsubagents load inherited positive parent context plus exact child mini-MMM.

Excluded diagnostic/provenance material never boots.

## Core files

- FULL core: `universal_core/WIZARD_UNIVERSAL_CORE_FULL_v3_4.md`
- COMPACT core: `universal_core/WIZARD_UNIVERSAL_CORE_COMPACT_v3_4.md`
- Route registry: `universal_core/WIZARD_ROUTE_REGISTRY_v3_4.md`
- Follow-up system: `universal_core/WIZARD_FOLLOWUP_SYSTEM_v3_4.md`
- Acceptance gates: `universal_core/WIZARD_ACCEPTANCE_GATES_v3_4.md`

## Runtime adapters

Runtime adapters are allowed in v3.4 because this is a deployment upgrade. They are not higher canon than the Universal Core.

- Codex: `runtime_adapters/CODEX_RUNTIME_ADAPTER_v3_4.md`
- Claude: `runtime_adapters/CLAUDE_RUNTIME_ADAPTER_v3_4.md`
- Hybrid Codex-Claude: `runtime_adapters/HYBRID_CODEX_CLAUDE_RUNTIME_ADAPTER_v3_4.md`

Use the Hybrid adapter when Codex can call Claude subagents. Codex should remain controller/executor/validator. Claude subagents should be semantic route workers unless explicitly granted tool/write access.

## Runtime capability and route truth

v3.4 classifies runtimes before execution:

- TRUE_SUBAGENT_RUNTIME
- TOOL_SUBAGENT_RUNTIME
- SIMULATED_ROUTE_RUNTIME
- HYBRID_RUNTIME

Visible routes use one of four statuses: `spawned`, `blocked`, `deferred`, or `simulated`. Simulated means controller-local approximation and never counts as spawned execution.

## Elastic waves, not hard counts

Waves and subagents are sized by evidence need, route value, runtime capacity, marginal payoff, and stop evidence. Do not force hard numbers such as "always run N agents" or "Full Wizard must execute every route." Full Wizard uses the full route system as a candidate bank, then runs/scouts the useful subset and marks the rest honestly.

## Source hierarchy

1. Current user-stated canon for v3.4 runtime adaptability.
2. Current user-stated canon in the v3.3 build request.
3. v3.3 packet as structural base.
4. v2.8 packet as reservoir.
5. v2.8 Pro audit as repair plan.
6. Deep research report as positive salience mining.
7. Legacy docs as mining sources only.
8. v3.0/v3.2 as rejected-pattern examples only.

## What changed from v3.3

- Added Runtime Capability Negotiation to Universal FULL and COMPACT.
- Added `simulated` status for honest weak-runtime/controller-local route passes.
- Added elastic wave/subagent sizing doctrine to prevent hard-count fixation.
- Added Codex, Claude, and Hybrid Codex-Claude runtime adapters.
- Hardened boot MMMs against quarantined diagnostic/failure salience.
- Added semantic boot contamination and runtime adaptability validation reports.

## Salience boundary

The main MMM is positive/control/operation/evidence oriented. Diagnostic security/audit vocabulary is retained only in checks/guards and quarantined material, not in boot salience.
