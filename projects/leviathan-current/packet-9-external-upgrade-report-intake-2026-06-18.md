---
title: Packet 9 External Upgrade Report Intake
created: 2026-06-18
updated: 2026-06-18
type: packet-receipt
status: active
source_snapshot: c90ec8499c83db3d17f6132ec734698a8de2dbce
claim_ceiling: stale external report intake and routing; not source proof; not wiki canon; not an overlay package
---

# Packet 9 External Upgrade Report Intake

## Source

Attachment:

```text
/Users/joshuaeisenhart/.codex/attachments/8611a21b-5b44-4abc-9e11-6706ae6518e6/pasted-text.txt
```

Attachment title:

```text
Leviathan OS Wiki Upgrade Research and Packaging Report
```

This report is useful as advisory pressure, but it is stale relative to the current `projects/leviathan-current/` wiki state.

## Intake Verdict

Do **not** merge or apply the report as-is.

Treat it as:

```text
external advisory / packaging idea / stale source map
```

Do not treat it as:

```text
current Leviathan wiki truth
current runtime evidence
current architecture authority
ready overlay zip
public documentation canon
```

## Bounded Intake Pack

```yaml
purpose: preserve useful packaging and information-architecture ideas from a stale external report without letting stale repo-state claims overwrite Packet 7/8 evidence
role: audit_reader
frame: external advisory report, current wiki outranks it for local state and Packet 7/8 proof truth
read_order:
  - projects/leviathan-current/read-first
  - projects/leviathan-current/README
  - projects/leviathan-current/index
  - projects/leviathan-current/proof-audit-roadmap-vs-mvp-2026-06-18
  - projects/leviathan-current/packet-8-wizard-mass-swarm-receipt-2026-06-18
  - attachment pasted-text.txt
do_not_read:
  - turn citation handles as portable evidence
  - attachment as destination-wiki audit
  - attachment as current Leviathan runtime proof
questions:
  - Which ideas survive as future packaging ideas?
  - Which claims are stale or contradicted by current wiki evidence?
  - What should be blocked from canon?
required_output: accepted/rejected/needs-verification table plus follow-up queue
promotion_rule: promote only ideas that match current local wiki evidence or are explicitly labeled future packaging work
target_codex_surface: projects/leviathan-current packet receipts and future packaging backlog
minimal_test: wiki_probe.py clean after adding this intake page
```

## Why It Is Stale

| Report claim / posture | Current local status | Intake decision |
|---|---|---|
| Leviathan has a clearly articulated three-plane model: FlowMind, Graph, Event Bus. | Current technical wiki pages use the four-plane architecture boundary: FlowMind, Orchestration, Graph, Event Bus. The README three-plane framing is public simplification, not technical canon. | Demote. Useful only as public-framing history. |
| Destination wiki repo could not be inspected publicly. | The local wiki exists and has been repeatedly probed with `wiki_probe.py`; current pages and Packet 7/8 receipts are available locally. | Reject as current blocker. |
| Build a fresh overlay zip to merge into a future wiki zip. | Could be a future packaging path, but current work is already inside `/Users/joshuaeisenhart/wiki/projects/leviathan-current/`. | Keep as future packaging idea only. |
| Use Codex-Ratchet as secondary engineering evidence for Leviathan docs. | This is dangerous unless heavily filtered. Codex Ratchet and Leviathan are related but distinct; current wiki keeps their boundary explicit. | Keep only with strict boundary and privacy filtering. |
| Public claims come from Leviathan unless an engineering detail exists only in Codex-Ratchet. | Directionally useful, but current wiki also requires command receipts for runtime/proof claims. | Accept with stronger proof-ceiling language. |
| Public docs should not mirror repository structure one-for-one. | Matches current wiki direction: concept atlas, read-order, evidence frontier, proof receipts, and source maps are separate. | Accept. |
| External `turn...` citations support claims. | Those handles are not portable local evidence. | Reject as load-bearing citations. Replace with local file paths or current web/source reads if reused. |
| OpenAI/Codex worktree guidance supports the packaging plan. | Not verified in this intake. OpenAI product guidance is drift-prone and must be checked against official docs before use. | Needs fresh official-source verification before citation. |
| No Packet 7/8 proof state is incorporated. | Packet 7 and Packet 8 now control the `ROADMAP.md` vs `mvp.md` split and blocker details. | Report is stale for runtime state. |

## Accepted Ideas

The report contributes useful future-facing ideas if they stay below canon:

- **Task-first information architecture**: do not expose repo structure as the main reader path.
- **Overlay/package discipline**: future exports should be reviewable, validateable, and mergeable rather than blind dumps.
- **Privacy filtering**: do not publish local paths, local-message integrations, secrets, private env paths, or operator logs as public docs.
- **Frontmatter/metadata discipline**: useful as a future docs-build concern, provided it does not force this personal wiki into a heavy site generator.
- **Command catalog idea**: useful only after current command surfaces are verified from Leviathan source or proof receipts.
- **Accessibility/SEO checklist**: useful for a future public docs site, not required for every internal wiki page.

## Rejected Or Blocked Ideas

- Do not replace the current wiki with the proposed `docs/` overlay tree.
- Do not collapse current architecture back to the report's three-plane framing.
- Do not treat Codex-Ratchet scripts, tests, bots, or runtime paths as Leviathan public docs without source-by-source privacy review.
- Do not import the report's citations as evidence.
- Do not describe Packet 7/8 runtime state as merely "not inspected" or "phase-one blueprint only."
- Do not let "overlay zip" become a current workflow unless Josh explicitly asks for a packaged public docs export.

## Current Authority Above This Report

Read these first:

1. [[projects/leviathan-current/read-first]]
2. [[projects/leviathan-current/README]]
3. [[projects/leviathan-current/index]]
4. [[projects/leviathan-current/deep-audit-current-snapshot-2026-06-18]]
5. [[projects/leviathan-current/evidence-frontier-and-blockers-dashboard-2026-06-18]]
6. [[projects/leviathan-current/proof-audit-roadmap-vs-mvp-2026-06-18]]
7. [[projects/leviathan-current/packet-8-wizard-mass-swarm-receipt-2026-06-18]]

## Future Use Queue

1. **Packaging Scout**
   - Prompt: Convert this report's overlay-zip idea into a future-only packaging plan for the current local wiki, using existing `wiki_probe.py` and current Packet 7/8 claim ceilings.
   - Stop condition: if the plan starts replacing current project pages or publishing private/operator material.

2. **Public Docs Filter**
   - Prompt: Build a public/private filter table for Leviathan wiki pages: public-safe, internal-only, provenance-only, and blocked/private.
   - Stop condition: if it treats Codex-Ratchet internal artifacts as Leviathan product evidence.

3. **Citation Repair**
   - Prompt: Replace the report's non-portable `turn...` citations with local file paths, current GitHub/raw URLs, or command receipts.
   - Stop condition: if a citation cannot be verified from a current source.

4. **Architecture Language Cleanup**
   - Prompt: Audit all pages for three-plane versus four-plane wording and preserve the distinction: three-plane public simplification, four-plane technical boundary.
   - Stop condition: if a page is intentionally quoting older/public framing.

## Blocked Helper Note

The bounded-Hermes-intake skill requested:

```bash
python3 scripts/codex_skill_agent_inventory.py --out /tmp/codex_skill_agent_inventory.json
```

In this checkout, that helper path is absent. This intake therefore used exact file reads and `wiki_probe.py` instead of claiming the inventory helper passed.

## Verification

Wiki probe:

```bash
python3 /Users/joshuaeisenhart/wiki/tools/wiki_probe.py --wiki-root /Users/joshuaeisenhart/wiki --output /tmp/leviathan-current-wiki-probe-packet9-20260618.json
```

Result:

```text
page_count: 440
index_header_count: 440
indexed_link_count: 530
missing_pages: []
orphans: []
broken_links: []
stubs: []
malformed_wikilinks: []
stale_namespace_wikilinks: []
```
