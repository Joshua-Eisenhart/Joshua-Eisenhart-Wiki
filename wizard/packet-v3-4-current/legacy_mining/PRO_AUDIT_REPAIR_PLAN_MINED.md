

# Source: MMM_V2_8_CANONICAL_CORE_SUMMARY.md

# MMM v2.8 Canonical Core Summary

## Current canon

1. Positive MMM boots first.
2. Negative / banned / contrast material never boots.
3. Main agent loads big/main MMM, not all voice mini-MMMs.
4. Subagents load assigned mini-MMM before task card.
5. Subsubagents load inherited positive context plus exact child mini-MMM.
6. Wizard requires real multi-wave subagent execution.
7. A visible voice/lane/check/council/composition has not run unless a real subagent ran it or it is marked blocked/deferred.
8. Visible routes require spawned / blocked / deferred truth.
9. Controller synthesis is not execution.
10. Voices run in voice waves, not ordinary follow-up.
11. LLM Council has its own wave, with nested rounds/subagents when runtime supports it.
12. Audit, Hygiene, and Security are checks/guards/waves, not voices and not lanes.
13. Lanes and compositions emerge from audits of voices, LLM Council, general output, route registry, and acceptance gates.
14. Follow-up generation uses three waves: Make/Assembly, Run/Scout, Audit/Improve.
15. Final Follow-up is the audited useful subset unless the user asks for full candidate bank.
16. Output must reduce cognitive load, not become a worker log.
17. Header/footer should expose useful route truth cleanly.
18. FULL docs must be genuinely full; smaller docs derive from full.
19. MMMs need positive nouns, people, schools, systems, methods, operators, math/geometry, and salience-driver phrase clusters.
20. Rules are default/general and later tuned per runtime/model.

## Hierarchy

1. User-stated canon.
2. Positive MMM boot law.
3. Real subagent-wave truth.
4. Main-agent big MMM / subagent mini-MMM separation.
5. General Wizard format and cognitive-load reduction.
6. Legacy docs mined only for useful parts.
7. Runtime adapters marked as tunable adapters, not canon.



# Source: MMM_V2_8_DOC_STRUCTURE_PATCH_PLAN.md

# MMM v2.8 Doc Structure Patch Plan

## Patch posture

Patch into v2.9. Do not redesign.

## 1. Rename / promote FULL guide

- Promote `current/WIZARD_GENERAL_FULL_GUIDE_v2_8.md` to `universal_core/WIZARD_UNIVERSAL_CORE_FULL_v2_9.md`.
- Retire or delete tiny `WIZARD_GENERAL_FULL_REFERENCE_v2_8.md`.
- Add a validation check: FULL docs must be materially larger than STANDARD/COMPACT/ULTRA.

## 2. Add universal_core/

Create:
- `WIZARD_UNIVERSAL_CORE_FULL_v2_9.md`
- `WIZARD_UNIVERSAL_CORE_STANDARD_v2_9.md`
- `WIZARD_UNIVERSAL_CORE_COMPACT_v2_9.md`
- `WIZARD_UNIVERSAL_CORE_ULTRA_v2_9.md`
- `WIZARD_HEADER_FOOTER_TEMPLATES_v2_9.md`
- `WIZARD_FOLLOWUP_SYSTEM_v2_9.md`
- `WIZARD_ROUTE_REGISTRY_v2_9.md/json`
- `WIZARD_ACCEPTANCE_GATES_v2_9.md/json`

## 3. Keep MMM as the universal salience layer

Create:
- `mmm/main/`
- `mmm/mini/`

Main agent boots main MMM only.
Subagents boot assigned mini-MMM only.

## 4. Add runtime adapters, not canon

Create:
- `runtime_adapters/README_ADAPTERS_NOT_CANON.md`
- `CLAUDE_ADAPTER_NOT_CANON.md`
- `CODEX_ADAPTER_NOT_CANON.md`
- `GEMINI_ADAPTER_NOT_CANON.md`
- `HERMES_ADAPTER_NOT_CANON.md`

## 5. Add legacy mining quarantine

Create:
- `legacy_mining/README_LEGACY_NOT_CANON.md`
- `EXTRACTED_USEFUL_PATTERNS.md`
- `REJECTED_LEGACY_PATTERNS.md`

## 6. Enrich definitions after deep research

Definitions FULL should gain:
- nearest neighbors
- non-job
- salience drivers
- associated people/schools/systems/methods
- math/operator/geometry associations
- legacy mined notes

## 7. Enrich MMMs after deep research

Do not make final lexical changes until Deep Research provides expansion candidates.

## 8. Preserve negative quarantine

Keep:
- `reference_only_negative/README_NEGATIVE_REFERENCE_ONLY_v2_9.md`

Ensure no boot file references it.



# Source: MMM_V2_8_FULLNESS_GAP_REPORT.md

# MMM v2.8 Fullness Gap Report

## Doc size scan

```json
{
  "NEW_THREAD_POSITIVE_MMM_BOOT_PROMPT_v2_8.md": {
    "chars": 427,
    "lines": 17
  },
  "README_BOOT_ORDER_v2_8.md": {
    "chars": 732,
    "lines": 25
  },
  "SUBAGENT_POSITIVE_MINI_MMM_BOOT_PROMPT_v2_8.md": {
    "chars": 407,
    "lines": 20
  },
  "SUBSUBAGENT_POSITIVE_MINI_MMM_BOOT_PROMPT_v2_8.md": {
    "chars": 462,
    "lines": 23
  },
  "WIZARD_ACCEPTANCE_GATES_v2_8.md": {
    "chars": 4723,
    "lines": 121
  },
  "WIZARD_EMOJI_MAP_v2_8.md": {
    "chars": 427,
    "lines": 7
  },
  "WIZARD_FOLLOWUP_FORMAT_v2_8.md": {
    "chars": 3796,
    "lines": 94
  },
  "WIZARD_GENERAL_COMPACT_v2_8.md": {
    "chars": 492,
    "lines": 16
  },
  "WIZARD_GENERAL_FULL_GUIDE_v2_8.md": {
    "chars": 48809,
    "lines": 1318
  },
  "WIZARD_GENERAL_FULL_REFERENCE_v2_8.md": {
    "chars": 537,
    "lines": 13
  },
  "WIZARD_GENERAL_STANDARD_v2_8.md": {
    "chars": 1629,
    "lines": 67
  },
  "WIZARD_GENERAL_ULTRA_v2_8.md": {
    "chars": 274,
    "lines": 8
  },
  "WIZARD_HEADER_FOOTER_TEMPLATES_v2_8.md": {
    "chars": 187,
    "lines": 8
  },
  "WIZARD_ROUTE_REGISTRY_v2_8.md": {
    "chars": 2978,
    "lines": 34
  },
  "WIZARD_SOURCE_EXTRACTION_HERMES_CLAUDE_CODEX_v2_8.md": {
    "chars": 11322,
    "lines": 289
  }
}
```

## Main finding

The actual full guide exists and is large: `current/WIZARD_GENERAL_FULL_GUIDE_v2_8.md` has 48809 chars. But the file named `WIZARD_GENERAL_FULL_REFERENCE_v2_8.md` has only 537 chars. This naming mismatch is the main fullness failure.

## Definitions

Full definitions have 21822 chars. This is useful, but v2.9 should add richer debugging fields:

- nearest neighbors
- non-job
- receipt requirement
- salience drivers
- associated people
- associated schools / traditions
- associated systems / methods
- math / operator / geometry associations
- legacy mined notes

## Tier separation

The tier separation exists, but the v2.9 validation should explicitly check:
- FULL > STANDARD > COMPACT > ULTRA by content richness
- FULL is source of truth for debugging
- COMPACT/ULTRA are not the only usable docs
- FULL mini-MMMs are rich enough for short-lived workers



# Source: MMM_V2_8_LEGACY_MINING_REPORT.md

# MMM v2.8 Legacy Mining Report

## Status

The uploaded HERMES / SOUL / SUBAGENT_BOOT / AGENTS / CLAUDE docs are **not canon**. They are old broken predecessor systems. v2.9 should mine them, not obey them.

## Metrics

{
  "HERMES(3).md": {
    "exists": true,
    "chars": 36158,
    "lines": 485,
    "subagent_mentions": 22,
    "wave_mentions": 13,
    "followup_mentions": 55,
    "receipt_mentions": 36,
    "mmm_mentions": 16
  },
  "SOUL(3).md": {
    "exists": true,
    "chars": 15331,
    "lines": 273,
    "subagent_mentions": 1,
    "wave_mentions": 0,
    "followup_mentions": 5,
    "receipt_mentions": 7,
    "mmm_mentions": 0
  },
  "SUBAGENT_BOOT(3).md": {
    "exists": true,
    "chars": 8206,
    "lines": 171,
    "subagent_mentions": 16,
    "wave_mentions": 0,
    "followup_mentions": 2,
    "receipt_mentions": 9,
    "mmm_mentions": 9
  },
  "AGENTS(3).md": {
    "exists": true,
    "chars": 33401,
    "lines": 500,
    "subagent_mentions": 5,
    "wave_mentions": 36,
    "followup_mentions": 42,
    "receipt_mentions": 51,
    "mmm_mentions": 16
  },
  "CLAUDE(3).md": {
    "exists": true,
    "chars": 30011,
    "lines": 427,
    "subagent_mentions": 9,
    "wave_mentions": 0,
    "followup_mentions": 15,
    "receipt_mentions": 25,
    "mmm_mentions": 0
  }
}

## Useful mined patterns

### HERMES

Useful:
- visible scaffold discipline
- Results as compact receipt summary
- follow-up as future-choice menu
- footer/header rail concept
- cognitive-load compression
- separation of body, Results, Follow-up, Hygiene/Security, Footer

Reject:
- any system-specific literal scaffold that conflicts with universal core
- any old route semantics that treat visible routes as menu theater
- any rule that lets controller-local reasoning count as workerized plurality

### SOUL

Useful:
- Hume as bridge voice
- Zhuangzi as anti-collapse
- Feynman as operation/testability
- Orwell as anti-fog
- Popper as falsifier
- Factory / Strategy distinction
- pushback as earned disagreement

Reject:
- voice-as-style framing
- any voice output without subagent receipt
- old emoji mismatches

### SUBAGENT_BOOT

Useful:
- salience-before-rules
- mini-MMM before task card
- task card minimum fields
- receipt discipline
- bounded subsubagent use

Reject:
- treating boot docs as complete doctrine
- any unclear status between controller-local and spawned worker

### AGENTS / Codex

Useful:
- no fake plurality
- spawned / blocked / deferred truth
- worker budget accounting
- wave registry
- mini-MMM law
- direct/narrow exception
- route registry fields

Reject:
- Codex-specific capacity/config as universal canon
- any Codex-only paths or runtime assumptions in universal core

### CLAUDE

Useful:
- anti-collapse doctrine
- body-before-follow-up
- subagent execution model
- LLM Council concept
- audit integration
- follow-up field structure
- strong pushback and no placation

Reject:
- treating Claude model routing as universal
- forcing every interactive answer into full Claude-style menu
- any old follow-up rule that makes special waves ordinary menu items

## Adapter extraction target

v2.9 should include:
- `runtime_adapters/CLAUDE_ADAPTER_NOT_CANON.md`
- `runtime_adapters/CODEX_ADAPTER_NOT_CANON.md`
- `runtime_adapters/GEMINI_ADAPTER_NOT_CANON.md`
- `runtime_adapters/HERMES_ADAPTER_NOT_CANON.md`

Adapters can tune the general system locally, but cannot override:
- positive MMM first
- negative never boots
- real subagent wave truth
- spawned / blocked / deferred
- main MMM vs mini-MMM separation



# Source: MMM_V2_8_MMM_SALIENCE_GAP_REPORT.md

# MMM v2.8 MMM Salience Gap Report

## Marker scan in main full MMM

```json
{
  "hume": 33,
  "popper": 1,
  "feynman": 1,
  "zhuangzi": 37,
  "orwell": 1,
  "wiener": 0,
  "beer": 0,
  "meadows": 0,
  "toyota": 0,
  "kanban": 146,
  "z3": 2,
  "smt": 1,
  "sat": 7,
  "unsat": 4,
  "operator": 3,
  "manifold": 0,
  "tensor": 1,
  "measurement": 3,
  "distinguishability": 0,
  "ooda": 0,
  "clausewitz": 0,
  "sunzi": 0,
  "owasp": 0,
  "least privilege": 24,
  "cybernetics": 0,
  "daoism": 0,
  "confucian": 0,
  "quine": 0,
  "peirce": 0,
  "mach": 1,
  "bacon": 0,
  "ockham": 0,
  "bayes": 0,
  "control theory": 0
}
```

## Main finding

The main full MMM has a large lexical reservoir, but the positive noun/person/school/system/math salience is uneven.

Strong or present:
- Hume
- Zhuangzi
- kanban
- least privilege
- SAT / UNSAT
- some Z3 / SMT

Weak or missing:
- Norbert Wiener
- Stafford Beer
- Donella Meadows
- Toyota as named system source
- cybernetics as named school
- Daoism / Confucianism as explicit terms
- OODA / Boyd
- Clausewitz / Sunzi
- OWASP
- distinguishability
- manifold
- density matrix / CPTP / operator language is too thin

## v2.9 expansion target

Do not generate final lexical MMMs in this pass. Deep Research should produce positive salience candidates for:

- people
- schools
- systems
- methods
- operators
- math/geometry objects
- phrase clusters
- nouns / verbs / adjectives
- source-adjacent couplings and triplets

## Route-specific salience needs

- Hume: Hume, common life, testimony, proportioned belief, modest judgment, empiricism.
- Popper: conjecture, refutation, severe test, counterinstance, critical rationalism.
- Feynman: apparatus, measurement, physical intuition, not fooling yourself.
- Zhuangzi: Daoism, wandering, perspective, transformation, non-forcing.
- Orwell: plain English, concrete nouns, active verbs, euphemism, dead metaphor.
- Systems: Wiener, Beer, Meadows, feedback, stocks/flows, delays, emergence.
- Factory: Toyota, TPS, kanban, jidoka, andon, takt, pull, reliability, incident review.
- Strategy: Boyd/OODA, campaign, tempo, reserve, decisive point, retreat.
- Audit/Hygiene/Security: provenance, receipt, traceability, readability, OWASP, least privilege.
- LLM Council: model variance, independent assessment, dissent preservation, peer review.
- Formal methods: Z3, SMT, model checking, invariant, witness, counterexample, finite model, equivalence class, distinguishability.



# Source: MMM_V2_8_PRO_AUDIT_REPORT.md

# MMM v2.8 Pro Audit Report

## Result

**v2.8 is the strongest packet so far, but it should not be treated as final.** It has the right architecture in pieces: positive-only boot, route registry, acceptance gates, mixed-model wave proof artifacts, mini-MMM categories, and a real long-form Wizard guide. The main repair is structural and documentary: the actual full guide is buried as `WIZARD_GENERAL_FULL_GUIDE_v2_8.md`, while `WIZARD_GENERAL_FULL_REFERENCE_v2_8.md` is only 537 chars. That mismatch will cause agents to load the wrong “full” file.

## High-confidence passes

- Positive main-agent boot is clean: boot files checked did not reference negative/reference material.
- `reference_only_negative/` exists and is outside the boot path.
- Mini-MMM tiers exist across voices, lanes, checks/guards, system routes, compositions, and controller acts.
- v2.8 includes route registry and acceptance gates.
- v2.8 contains runtime proof artifacts under `runs/wizard_full_expanded_latest/`.
- Mixed-model run proof exists: `external_mixed_model_wave_summary.json` reports 10 valid live waves and attempted Sonnet, Opus, Codex, and Gemini routes.
- Voice mini-MMM load proof exists: `external_repair_load_proof_summary.json` reports 9/9 voice subagents loaded full voice mini-MMM files.
- Negative/reference material is not part of the checked boot files.

## Critical gaps

1. **Full reference naming is dangerous.** `WIZARD_GENERAL_FULL_REFERENCE_v2_8.md` is tiny, while `WIZARD_GENERAL_FULL_GUIDE_v2_8.md` is the actual full guide.
2. **Legacy source status is not clean enough.** The packet includes `WIZARD_SOURCE_EXTRACTION_HERMES_CLAUDE_CODEX_v2_8.md`, but v2.9 should explicitly mark old HERMES/SOUL/AGENTS/CLAUDE docs as legacy mining sources, not canon.
3. **Main MMM noun/salience field still has gaps.** Some salience anchors exist, but people/schools/systems/math/operator language is uneven. Marker scan found zero or near-zero counts for Wiener, Beer, Meadows, Toyota, cybernetics, Daoism, Confucian, OODA, Clausewitz, Sunzi, distinguishability, and manifold.
4. **Definitions are improved but not rich enough for debugging smaller versions.** Full definitions are ~21822 chars, but v2.9 should add nearest neighbors, salience drivers, associated people/schools/systems/methods, and math/operator associations per route.
5. **Follow-up logic should explicitly say lanes/compositions emerge from prior wave audits.** v2.8 is close, but v2.9 should make this canonical.
6. **Runtime adapters are not clearly separated.** v2.9 should add non-canon runtime adapters for Claude/Codex/Gemini/Hermes instead of blending old source material into universal core.

## Audit answers

1. Universal core / MMM / adapters / legacy / negative separation: **PARTIAL**. Structure exists but should be clearer.
2. Main boot positive-only: **PASS**.
3. Mini-MMMs assigned to subagents: **PASS with wording patch needed**.
4. FULL docs actually full: **PARTIAL** due full-guide vs full-reference mismatch.
5. Definitions rich enough: **PARTIAL**.
6. Subagents required for visible routes: **PASS in direction**, strengthen in current universal core.
7. Voices separated from ordinary Follow-up: **PASS in direction**, reinforce.
8. LLM Council own wave/nested rounds: **PASS in direction**, enrich nested-round wording.
9. Audit/Hygiene/Security as checks/guards/waves: **PASS**.
10. Follow-up Make full candidate bank: **PASS in direction**.
11. Follow-up Run/Scout prework: **PASS in direction**.
12. Follow-up Audit/Improve final prompts: **PASS in direction**.
13. Header wave/subagent truth: **PASS in run output, needs standard template**.
14. Footer cognitive-load reduction: **PARTIAL**.
15. Runtime adapters non-canon: **PARTIAL**.
16. Legacy docs quarantined: **PARTIAL**.
17. Negative reference-only: **PASS**.
18. Main/mini-MMM noun salience: **PARTIAL / needs expansion**.
19. FULL mini-MMMs rich enough: **PARTIAL**.
20. COMPACT/ULTRA useful: **PASS with ongoing behavior testing needed**.

## Recommendation

Do not rebuild immediately. Run targeted deep research for salience expansion, then build v2.9 with a clean folder separation:

- `universal_core/`
- `mmm/`
- `definitions/`
- `boot_rules/`
- `runtime_adapters/`
- `legacy_mining/`
- `reference_only_negative/`
- `archive/`
- `audit/`
