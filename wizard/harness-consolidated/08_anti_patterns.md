last_updated: 2026-04-17

# Anti-Patterns for LLM Workers

Exact list of failure modes to avoid when executing work in this harness. Each one represents a broken path through the constraint chain.

## Accuracy Anti-Patterns

**"ALL PASS" when some tests are skipped or use weaker criteria**
- Never collapse mixed-depth results into a single pass claim. Specify which criteria (for example F01/N01 checks, tool-depth, or probe-family checks) actually passed.

**Reporting agent output as verified without checking the result JSON**
- Agent completion claims are premises, not conclusions. Read the actual result file. Verify exit code, test counts, and tool integration depth before trusting a summary.

**Treating "exists" as "canonical"**
- File present ≠ runs ≠ passes local rerun ≠ canonical by process. Never promote without the full chain.

**Reusing labels across different axes/layers**
- Status labels apply to a single constraint axis. Do not reuse across topological layers, shell ontologies, or coupling measurements. Each axis has its own label chain.

## Process Anti-Patterns

**Editing a registry/status doc before code/result gate is satisfied**
- Docs are read-only until sim output proves them. Stale docs corrupt the entire chain.

**Launching coupling sims before shell-local sims exist for both layers**
- The program order is mandatory: shell-local lego sims must be complete, pairwise coupling sims second, multi-shell tests third, only then bridge claims. Skipping a layer breaks the evidence chain.

**Treating entropy as sufficient evidence for shell membership**
- Coupling behavior fixes shell membership more strongly than entropy shape alone. A state may have high-entropy signatures without surviving the coupling tests that define its layer.

## Language Anti-Patterns

**RLHF-style agreement ("you're right!", reflexive validation)**
- Do not validate based on training-model agreeability. Use constraint-admitted / excluded framing tied to an actual lego or test.

**Using causal language below the owner-dialog level**
- Use survival/exclusion wording from [03_language_discipline.md](03_language_discipline.md) and [09_perspectival_rotation.md](09_perspectival_rotation.md), not construction language.

**Collapsing "forward evolution" with "backward admissibility"**
- A state that survives (backward) is not the same as a state that evolves to something (forward). Keep these distinct in every claim. The manifest distinguishes them.

**Framing results as discovering pre-existing truth vs survival**
- "Wasn't excluded by z3" not "This is the correct answer." Use exclusion/survival language, not discovery.

## Operational Anti-Patterns

**Declaring many tools imported but none load-bearing**
- A sim cannot be canonical with all tools decorative. One tool outside the baseline must be truly load-bearing. Document which tool carries the weight.

**Presume-heavy design**
- Explore what the math allows, not just what the engine proposes. Test all rotation axes, dephasing bases, channel types — not preferred variants only.

**Collapsing multiple surviving candidates prematurely**
- A family that survives two independent coupling sims is still a candidate. Hold divergence until later constraints force collapse.

## Cross-Reference
- See [09_perspectival_rotation.md](09_perspectival_rotation.md) for nominalist reframing discipline  
- See [10_owner_doctrine_index.md](10_owner_doctrine_index.md) for backing memory files on language and salience

