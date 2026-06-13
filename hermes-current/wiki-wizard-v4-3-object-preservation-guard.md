# Wiki Wizard v4.3 Object-Preservation Guard

Purpose: route Hermes to the current Wizard v4.3 object-preservation guard and keep its authority/runtime boundaries straight.

Status: active Hermes routing note. Pointer only — not the authority surface and not a runtime.

Use this when:
- a task mentions Wizard v4.3, object-preservation, primary object cards, or salience/proxy drift
- Claude or Codex says v4.3 is "wired in" and the wiki/harness needs to know what that means
- deciding where v4.3 authority lives vs. where v4.2 runtime authority lives

## What v4.3 is

Wizard v4.3 is the **current-task object-preservation gate in front of v4.2 councils**. The current binding is **v4.3-gated v4.2**: v4.3 preserves the primary object so councils cannot drop it or promote a proxy/analogy/metric into canon mid-run; v4.2 supplies the council/runtime/output machinery.

Core shape:
- a primary object card with a stable object statement + `object_statement_sha256` hash;
- typed lateral mappings (`adapter`, `probe`, `analogy`, `proxy`) where only `adapter`/`probe` may ever promote to claim-bearing;
- separated root vs extended constraints;
- wildcard / fixation-breaker lanes;
- an `evidence_spine` (source-math locks, sim/audit receipts when relevant, Claude pattern cards as reference-only, claim ceiling, blocked consumers).

For the Codex Ratchet shell model, the preserved object is the finite **retrocausal possibility field** — not Axis0, FEP, scalar entropy, PEPS3D, or a Wolfram analogy. Those are adapters/probes/proxies, never the object.

## Where authority actually lives (repo, not wiki)

The live v4.3 authority surfaces are repo-held under `/Users/joshuaeisenhart/Codex-Ratchet`, gated by that repo's `AGENTS.md`:
- spec: `system_v5/docs/WIZARD_V4_3_PRIMARY_OBJECT_PRESERVATION_SPEC_20260526.md`
- validator: `scripts/wizard_v4_3_object_preservation.py`
- tests: `system_v5/tests/test_wizard_v4_3_object_preservation.py`
- repo Claude skill: `.claude/skills/wizard-v43/SKILL.md` (repo-relative)
- Codex skill: `~/.codex/skills/three-council-wizard-v4-3/SKILL.md`

Verification path (pytest hangs in that repo state; use the CLI directly):
```bash
python3 scripts/wizard_v4_3_object_preservation.py example --out /tmp/wiz_v43_packet.json
python3 scripts/wizard_v4_3_object_preservation.py validate --input /tmp/wiz_v43_packet.json   # expect ok: true
python3 scripts/wizard_v4_3_object_preservation.py selftest --out /tmp/wiz_v43_selftest.json
```

## Boundaries this note enforces

- There is **no** `packet-v4-3-current` directory under `~/wiki/wizard/` and there should not be one unless a validated packet is explicitly created. The wiki's current Wizard packet stays v4.2.
- Hermes owns a validated v4.3 object-preservation packet at `wizard/hermes-version-current/packets/hermes_v4_3_retrocausal_object_card.json`. Full harness doc: `wizard/hermes-version-current/15_HERMES_WIZARD_V4_3_OBJECT_PRESERVATION.md`.
- Claude material (skills, workflow scripts, agents) is **reference-only** and may be mined as pattern cards. It never becomes the primary object, a completed council, or a completion claim.
- This is a routing note. It does not authorize wiki page creation, truth-label promotion, or repo-state claims. The repo `AGENTS.md` + spec + validator are the authority.
- Do not call a v4.2 route `FULL` just because the v4.3 preflight passed; v4.2 keeps its own route-truth gates.

## Relationship to the wiki Wizard surface

- Wiki Wizard runtime: still v4.2 (`wizard/packet-v4-2-current/`); see [[wiki-wizard-v4-2-autoloop-control]].
- Current-vs-legacy ranking: see [[current-vs-legacy]].
- For Codex Ratchet repo status, prefer the project surface over scattered concept notes; see [[projects/codex-ratchet/STATUS]].

Related notes:
- [[read-first]]
- [[active-plans]]
- [[wiki-wizard-v4-2-autoloop-control]]
- [[current-vs-legacy]]

Write mode: controller-maintained routing note.
