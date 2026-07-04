---
title: Hermes
created: 2026-04-10
updated: 2026-07-03
type: entity
tags: [entity, workflow, multi-agent, tooling, architecture]
sources:
  - raw/articles/new-docs/AGENT_WORKFLOW_AND_BOOT_ARCHITECTURE.md
  - raw/articles/new-docs/archive_old/HERMES_STACK_AND_ADDONS_PLAN.md
  - raw/articles/new-docs/archive_old/BOUNDED_HERMES_INGESTION_PROTOCOL.md
framing: current
status: current stub
---

# Hermes

## Overview
Hermes is the controller-side agent surface and current low-entropy wiki spine. It owns bounded planning, ingestion, audit, and routing work rather than scientific closure or broad unbounded execution.

## Key facts
- Hermes is described as the A2 high-entropy ingestion and audit layer.
- Hermes launches and audits worker terminals under explicit boot roles.
- Hermes is supposed to work through bounded packs, not whole-corpus freeform digestion.
- `hermes-current/` is the safer entry surface for substantive wiki work.
- CocoIndex is used as retrieval, not authority.

## Relationships
- Operational workflow: [[agent-workflow-and-boot-architecture]]
- Current front door: [[hermes-current/read-first]]
- Memory offload: [[hermes-current/hermes-memory-offload]]
- Retrieval layer: [[hermes-current/cocoindex-wiki-mcp-memory-layer]]
- Bounded ingestion rules: [[bounded-hermes-ingestion-protocol]]
- Stack planning: [[hermes-stack-and-addons-plan]]
- Repo and ecosystem map: [[hermes-repos-and-ecosystem-classification]]
- Worker prompt surface: [[boot-prompt-templates]]
- Controller rules: [[llm-controller-contract]]

## Notes
Use this page when the question is about who Hermes is in the system. Use the linked concept pages when the question is about procedures, prompts, or ecosystem planning.
