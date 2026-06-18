# Current vs Legacy

Purpose: explain how to rank and use different wiki surfaces safely.

Status: active Hermes working-spine provenance note.

Use this when:
- deciding what is authoritative
- reconciling conflicting notes
- deciding whether older material should steer present work

Current truth:
- `hermes-current/` is Hermes's living control surface for present framing, intentions, plans, and operating rules.
- `wizard/` is the current Wizard harness surface; `wizard/harness-consolidated/` is the current nominalist-CS doctrine/priming support copy. The old `harness/` root path is not assumed live unless restored by a later explicit migration.
- Wizard runtime version: the wiki Wizard home is `wizard/`. The shared current v4.3 core now lives at `wizard/packet-v4-3-current/`, and each LLM/system can have a native sibling adaptation such as `wizard/hermes-version-current/` or `wizard/claude-version-current/`. `wizard/packet-v4-2-current/` and earlier packets are legacy/provenance/source material only, to be lifted through v4.3 and the active LLM adaptation before use. Hermes's adopted always-on behavior lives in its adapter plus the `hermes-wizard` skill; Claude/Codex adapters are separate and must be tooled to their own systems. The active v4.3 MMM boot surfaces live under `wizard/packet-v4-3-current/mmm/`.
- `projects/` contains project-specific current context when a project has an explicit living surface there.
- `concepts/` is a large knowledge field and concept corpus; it may contain valuable harness-like material, but not every concept note is a front-door authority note.
- `raw/` contains intake/source materials and should not be treated as normalized guidance by default.
- `archive/` contains older settled or retired material.
- Legacy sources such as Dark Empress, Grandmaster, and Leviathan v3.2 remain important historical/provenance surfaces, but they should not automatically outrank the active Hermes spine or the harness.
- Older or higher-entropy docs can still carry strong candidate ideas, useful genealogy, or better formulations of a local issue; age alone does not make them worthless.
- Prefer wiki pages and routes that keep provenance/framing explicit: newer/current-docs-aligned versus older/legacy/inconsistent should stay visibly distinguished rather than smoothed together.
- The main ranking question is refinement/evidence level, not a hard canon/non-canon split.
- The whole wiki is a mixed corpus / KB / memory field, not one authority surface. Broad retrieval is good, but admission is per document: classify role, provenance, current-vs-legacy status, and evidence support before using a note as authority.

Authority rule:
- For Hermes-side behavior and framing, prefer `hermes-current/` notes.
- For cross-agent priming/doctrine, prefer `wizard/harness-consolidated/`; for Wizard runtime behavior, prefer `wizard/` and `wizard/hermes-version-current/`.
- Use project-specific current notes next when relevant.
- Use concept notes for deeper reference and mappings.
- Use legacy material comparatively and explicitly, especially when preserving provenance or unresolved differences.
- For Codex Ratchet questions, prefer `projects/codex-ratchet/*.md` over scattered `concepts/` notes. For Leviathan OS questions, prefer `projects/leviathan-current/read-first.md` and the live GitHub website/raw sources at `https://github.com/lev-os/leviathan`; if that route is insufficient, use a clean fresh clone with SHA/clean-status evidence. The old `~/GitHub/leviathan` checkout was deleted on 2026-06-18 and should be treated as historical only.

When conflict appears:
1. Do not smooth the conflict away casually.
2. Identify which note is current and which is legacy/supporting.
3. Separate stronger proven/current claims from legacy or higher-entropy candidate ideas rather than discarding either by reflex.
4. Escalate to a current note if the distinction needs to guide future work.

Do not:
- treat age alone as authority
- treat age alone as demotion if the older note still preserves a useful candidate structure
- treat rich concept notes as automatically current policy
- silently rewrite legacy material into present truth

Related notes:
- [[read-first]]
- [[about-me-and-how-to-work-with-me]]
- [[hermes-memory-offload]]

Write mode: human-owned / controller-maintained with care.
