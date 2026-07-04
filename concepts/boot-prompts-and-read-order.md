---
title: Boot Prompts And Read Order
created: 2026-04-07
updated: 2026-04-08
type: summary
tags: [reference, research, system]
sources:
  - raw/articles/new-docs/archive_hermes_overlaps/BOOT_PROMPTS_AND_READ_ORDER.md
framing: legacy
priming: false
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Boot Prompts And Read Order

## Purpose
Concrete prompt templates and read orders for booting a new thread without collapsing layers. Superseded by [[boot-prompt-templates]] (the active operational version) but preserves the read-order logic and framing-specific templates.

## Default Read Order
For a fresh thread:
1. SYSTEM_CONTEXT_HANDOFF__CURRENT.md
2. CONSTRAINT_SURFACE_AND_PROCESS.md
3. OWNER_THESIS_AND_COSMOLOGY.md
4. NOMINALISM_IN_THIS_SYSTEM.md
5. relevant reference doc(s)
6. relevant audit doc(s)
7. only then write or edit

If the task is narrow, read only the minimal subset needed.

## Boot Prompt Templates (Legacy)

### Governing-doc rewrite
"Read SYSTEM_CONTEXT_HANDOFF__CURRENT.md first. Then read the governing docs for the task. Preserve the distinction between governing constraints, candidate thesis, and reference support. Do not introduce new ontology. Make only the requested rewrite."

### Reference doc writing
"Write a new reference doc that uses exact established terminology only. Include exact fit, mismatch notes, and system-side mapping. Do not collapse the support tradition into the system ontology."

### Audit pass
"Audit the folder by role, not by filename alone. Separate governing docs, reference docs, audit docs, handoff docs, and archive residue. Identify overlap, residual ladder language, and any unsupported overclaiming."

### Claude Code run
"Update only the files explicitly named in the task. Keep changes minimal and local. If a document is a candidate thesis, label it that way. If a governing doc, keep it non-derivative and explicit."

## Read-Order Rule
Driven by the task's layer:
- governing change -> handoff + governing docs first
- support writing -> reference docs first, then mapping
- audit -> handoff + audit docs first
- consolidation -> all role docs, then overlap review

Never start with the broadest umbrella doc unless the task is specifically architectural.

## Related pages
- [[boot-prompt-templates]]
- [[agent-workflow-and-boot-architecture]]
- [[system-context-handoff-current]]
