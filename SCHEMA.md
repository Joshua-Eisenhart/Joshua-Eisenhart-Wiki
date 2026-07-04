---
status: superseded
superseded_by: "inventory: classified STALE in wf8_wiki_inventory.md (2026-07-02)"
---

# Wiki Schema

## Domain
Leviathan System — a persistent knowledge base for the Leviathan project: architecture, probes, simulations, invariants, runtime behavior, operational decisions, and supporting research.

## Published Folder Structure

### Governance and harness (read-first surfaces)
- `harness/` = cross-agent nominalist constraint-admissibility harness for LLM workers. Priming, grammar, boot-order. See `harness/SALIENCE_LOADER.md`.
- `wizard/` = cross-agent Wizard/MMM wave-execution reference. Universal contract for boot law, route truth, wave receipts, follow-up construction, MMM reservoirs, and runtime adapter derivation. Runtime-specific Claude/Codex/Hermes files derive from it; they do not live inside it.
- `hermes-current/` = Hermes low-entropy working/context spine: identity, intentions, plans, environment, authority rules, and Hermes-side routing. See `hermes-current/read-first.md`.
- `projects/` = project-local context and front doors. `projects/<name>/read-first.md` where present.

### Knowledge field
- `entities/` = named actors, systems, or first-class surfaces
- `concepts/` = topics, methods, references, and synthesis pages. Frontmatter `framing:` declares whether a page is current / mixed / legacy / legacy_rationalist_leak. Frontmatter `priming: false` marks non-priming pages; readers should not draw first-pass framing from them.
- `comparisons/` = side-by-side analyses
- `queries/` = substantial filed answers and research queues

### Operational
- `audits/` = audit runs
- `tools/` = tool notes
- `claude-memory/` = rolling agent memory
- `config/` = config files
- `log.md` = wiki operations log

### Source and history
- `raw/` = immutable source material only
- `_archive/` = retired or superseded material (includes stabilization snapshots)

### Support folders
- `concepts/_archive/` = retired or superseded published pages kept for provenance
- `concepts/_meta/` = internal navigation or maintenance pages that are not counted as public pages unless explicitly promoted into a published folder

### Top-level routing artifacts
- `index.md` = browse-time index of public pages; section order implies browse-time routing
- `lev_reorientation_guide.md` / `lev_reorientation_guide_v2.md` = sibling long-form harness artifacts (T3 and T4 voice); comparative reference for Leviathan OS work

### Authority rule
- For Hermes-side routing, defer to `hermes-current/current-vs-legacy.md`.
- For cross-agent priming and doctrine, start with `harness/SALIENCE_LOADER.md` and `harness/00_READ_FIRST.md`.
- `projects/<name>/read-first.md` may add project-local entry/ranking rules.

## Conventions
- File names: lowercase, hyphens, no spaces (example: `transport-gate.md`)
- Every published page starts with YAML frontmatter
- Use `[[wikilinks]]` to connect pages; aim for at least 2 outbound links on substantive pages
- When updating a page, always bump the `updated` date
- Every new public page must be added to `index.md` under the correct section
- Every action must be appended to `log.md`
- Never modify files in `raw/`; they are immutable source material
- Keep pages scannable; split pages over about 200 lines
- If a numbered batch page and a clean slug page cover the same public topic, keep the clean slug public and move the numbered twin to `_archive/`

## Frontmatter
```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [from taxonomy below]
sources: [raw/articles/source-name.md]
framing: current | mixed | legacy
contradictions: [page-name]
---
```

`framing` and `contradictions` are optional, but when used they should follow the values above.

## Tag Taxonomy
All tags used on pages must come from this list.

- system
- architecture
- runtime
- probe
- simulation
- invariant
- graph
- geometry
- transport
- audit
- log
- reference
- decision
- entity
- concept
- comparison
- query
- source
- research
- validation
- anomaly
- planning
- implementation
- topology
- constraints
- visualization
- tooling
- digest
- mathematics
- quantum
- formal
- status
- compression
- corrections
- harness
- wizard
- wave
- mmm
- subagent
- adapter
- receipt
- boot-law
- route-truth
- followup
- language
- session
- mapping
- canonical
- equivalence
- entropy
- workflow
- foundation
- algebra
- multi-agent
- metadata
- ingest
- intake
- coverage
- bibliography
- coordination
- thermodynamics
- qit
- ai
- alignment
- maintenance
- wiki
- controller
- queue
- spine
- chirality
- glossary
- leviathan
- engines
- developer
- systems
- operators
- channels
- bridge
- computer-science
- loops
- manifesto
- translation
- legacy
- cosmology
- governance
- holodeck
- proof
- fep
- memory
- science
- method
- recursion
- recall
- perception
- personality
- world-engine
- nominalism
- navigation
- physics
- manifold
- parity
- handoff
- automation

### Added from active published pages 2026-04-24
- a2-layer
- arxiv
- axioms
- axis0
- binary-operator
- candidate
- cartan
- clifford
- constraint-geometry
- constraint-ratchet
- coupling
- current
- degrees-of-freedom
- distinguishability
- doctrine
- e6
- e7
- e8
- emergence
- eml
- exceptional
- external-math
- f4
- formal-methods
- framing
- g-tower
- g2
- genealogy
- group-theory
- historical-context
- hopf
- iching
- igt
- integration
- intent
- jordan-peterson
- lawful-cycles
- lie-groups
- mera
- mutual-information
- n-shell
- non-commutative
- packets
- pattern
- philosophy
- prediction-first
- process
- product-form
- provenance
- quantum-information-theory
- ratchet
- recovery
- results
- rosetta
- routing
- spinors
- stub
- symbolic
- symbolic-regression
- sympy
- template
- tensor-network
- weyl
- world-model
- xgi
- z2
- z3

## Page Thresholds
- Create a page when an entity or concept appears in 2 or more sources, or is central to one source
- Add to an existing page when a source mentions something already covered
- Do not create pages for passing mentions or minor details
- Split a page when it exceeds about 200 lines
- Archive a page when it is fully superseded; move it to `_archive/` and remove it from the public index

## Entity Pages
One page per notable entity. Include:
- Overview or what it is
- Key facts and dates
- Relationships to other entities or concepts via `[[wikilinks]]`
- Source references

## Concept Pages
One page per concept or topic. Include:
- Definition or explanation
- Current state of knowledge
- Open questions or debates
- Related concepts via `[[wikilinks]]`

## Comparison Pages
Side-by-side analyses. Include:
- What is being compared and why
- Dimensions of comparison
- Verdict or synthesis
- Sources

## Query Pages
Use for substantial answers worth filing back into the wiki. Include:
- The question
- Synthesis
- Follow-up questions or next actions
- Sources

## Update Policy
When new information conflicts with existing content:
1. Check dates; newer sources generally supersede older ones.
2. If genuinely contradictory, keep both claims with dates and sources.
3. Mark contradictions in frontmatter with `contradictions: [page-name]`.
4. Flag the contradiction in the next lint or audit pass.
