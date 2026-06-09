---
title: Lego Sim Contract
created: 2026-04-07
updated: 2026-05-21
type: summary
tags: [reference, research, system, simulation, planning]
sources:
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/LEGO_SIM_CONTRACT.md
  - raw/articles/new-docs/archive_old/LEGO_SIM_CONTRACT.md
  - raw/articles/new-docs/LEGO_SIM_CONTRACT.md
framing: historical_contract_mirror
historical_archive_sources:
  - raw/articles/new-docs/archive_old/LEGO_SIM_CONTRACT.md
  - raw/articles/new-docs/LEGO_SIM_CONTRACT.md
spec_mirror: specs/codex-ratchet/lego-sim-contract-current
---

# LEGO Sim Contract

## Spec mirror
Current process-contract routing belongs in [[specs/codex-ratchet/lego-sim-contract-current|Lego Sim Contract Current Mirror]].

This concept page is a stale mirror of the lego/sim contract. Use it for language and genealogy, not current sim authority, until it is refreshed against the live repo source.

The raw article sources in the frontmatter are historical/archive sources. The live repo contract in `system_v5/docs/LEGO_SIM_CONTRACT.md` outranks them for current sim work.

## Overview
Defines what every small sim (lego sim) must declare, use, emit, and satisfy before it can count as a real building block in the pre-Axis ladder. The system should be built from small sims as legos -- only works if each sim is explicit, rich, and honest enough to be composed upward.

The current active companions for this contract are [[lego-build-catalog]] and [[actual-lego-registry]], which split the lego program into a grouped controller ledger and an exhaustive row-level registry.

## Core Rule
A small sim is not automatically a valid lego. A sim counts as a real lego only if it: declares its role, declares its tier, uses required tools, emits required artifacts, includes required negatives, states promotion status, and can be consumed by higher sims without smuggling hidden assumptions. If these are missing, the sim is diagnostic_only.

## Required Fields

### Identity
sim_id, name, version, tier

### Purpose and Scope
purpose, scientific_question, sim_class (constraint_probe, carrier_probe, geometry_probe, transport_search, chiral_search, negative_probe, placement_probe)

### Constraint and Structure
root_constraints_in_force, carrier_layer, geometry_layer, bridge_layer, cut_layer, law_or_candidate_tested, branch_status_before_run, allowed_claims, promotion_blockers

### Tooling
required_tools, actual_tools_used, proof_surfaces_used, graph_surfaces_used, topology_surfaces_used

### Inputs
required_inputs, data_or_artifact_dependencies

### Negatives
required_negatives, negatives_run, kill_conditions

### Outputs
required_artifacts, artifacts_emitted, witness_trace_id, result_summary

### Evaluation
pass_rule, fail_rule, promotion_status, eligible_consumers, blocked_consumers

## Tier Definitions
- 0: root constraints
- 1: finite carrier
- 2: geometry
- 3: transport
- 4: differential / chirality / flux
- 5: negatives
- 6: placement / pre-entropy
- 7: AXIS-ENTRY (embargoed until Tiers 3-6 justify it)

## Promotion Discipline
diagnostic_only results cannot support geometry claims. Missing artifact = promotion blocked. No sim may claim results above its declared resolution level.

## Related pages
- [[current-architecture-core]]
- [[ladders-fences-admission-reference]]
- [[current-preaxis-status-and-ordering-note]]
- [[boot-prompt-templates]]
