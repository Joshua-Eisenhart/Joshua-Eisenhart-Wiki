# Skills Manifest v4.2

authority_status: canonical-skill

Packet-local skills are callable by parent or child routes. They do not replace the three councils.

## Required Skills

### `premortem`

Path: `skills/premortem/SKILL.md`

Used by `failure.premortem`.

Wizard variant returns structured receipt evidence only. It must not create reports, transcripts, HTML, docs, browser actions, or web pages.

### `claude-bridge`

Path: `skills/claude-bridge/SKILL.md`

Used when Claude external worker capacity is available. It is a child execution surface, not a council replacement.

### `claude-pattern-intake`

Path: `skills/claude-pattern-intake/SKILL.md`

Used when Claude agents, skills, workflows, or Claude Code outputs should update Wizard/Codex behavior. Claude output is source material only; the skill ports mechanics through Wizard authority, receipt, and conformance rules.

### `source-math-lock`

Path: `skills/source-math-lock/SKILL.md`

Used before downstream workers reuse source-doc math, atlas rows, terrain/operator words, Axis-6 conventions, proof assumptions, or workflow-stage formulas. It emits a locked artifact plus source hashes and independent recomputation checks.

### `sim-audit-spine`

Path: `skills/sim-audit-spine/SKILL.md`

Used for Codex Ratchet sim, proof, result, terrain/operator, queue, and workflow claims. It keeps state archaeology, builders, mechanical gates, fabrication audits, SMT proof flips, and final claim ceilings separate.

## Council-Member Skills

### `loophole-auditor`

Path: `skills/council-members/loophole-auditor/SKILL.md`

Used by `failure.loophole_auditor`.

### `factory-handoff`

Path: `skills/council-members/factory-handoff/SKILL.md`

Used by Factory child roles and management handoff checks.

### `follow-up-selector`

Path: `skills/council-members/follow-up-selector/SKILL.md`

Used by `follow_up.next_move_selector`.

### `strategy-loop`

Path: `skills/council-members/strategy-loop/SKILL.md`

Used by Strategy children and loop repair.

### `systems-strategy`

Path: `skills/council-members/systems-strategy/SKILL.md`

Used by Systems children and context/strategy checks.

### `collapse-auditor`

Path: `skills/council-members/collapse-auditor/SKILL.md`

Used after multi-voice, multi-worker, source-lock, sim/proof, or workflow runs when apparent agreement may be decorative plurality or shared-premise correlated error.

## Rule

Every skill-backed child still loads compact MMM plus the relevant skill mini-MMM. A skill call without MMM salience and child receipt proof is not counted.
