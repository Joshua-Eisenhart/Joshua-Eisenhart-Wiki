# Current AI Agent Harness Research — 2026-06-15

```yaml
status: research_front_door
created: 2026-06-15
scope: current harness / agent-runtime / memory / benchmark research
claim_ceiling: source-grounded synthesis, not exhaustive literature review
source_seed: user screenshot IMG_6209.png + web extraction + local search
local_corpus_synthesis: projects/ai-agent-harnesses/wiki-harness-corpus-processed-2026-06-15.md
```

## Processed local wiki corpus

The local wiki harness corpus has now been processed into:

`projects/ai-agent-harnesses/wiki-harness-corpus-processed-2026-06-15.md`

That companion file covers conceptual harness docs, Wizard runtime/conformance docs, Claude/Hermes restart-memory docs, and Codex-Ratchet steward/archive harness docs. Use this file for the current external-paper front door; use the companion for local wiki doctrine.

## ClaimGate product boundary checkpoint

`projects/ai-agent-harnesses/claimgate-standalone-product-boundary-2026-06-20.md`

This companion note captures the June 20 ClaimGate standalone packaging
decision: Wizard/Ratchet/Hermes/Leviathan are source mines, not product
dependencies; live model pools are required but provider identities are
per-run capabilities; and deterministic hard-wall gates remain the only
promotion path.

Current June 20 checkpoint: `10c611f` repairs the Harness Author Lev FlowMind
export after mass testing showed the previous `slots:` sketch parsed as
`format: unknown` with `nodeCount: 0`. The v23 zip
`ClaimGate_CoreLevOS_COMPLETE_SINGLE_ZIP_v23_lev_native_harness_author.zip`
clean-extracted and passed `npm run product:verify` with 410 entries under the
500-entry cap. The v19 solution contributed a useful product primitive:
Axiom Digger -> Constraint Digger -> Gate Digger -> proposal-only Lev-shaped
Project Harness export. This is now runnable as `claimgate harness-author ...`,
`npm run harness:demo`, `npm run harness:compile-demo`, tested by
`tests/harness-author-tests.js`, and exposed in the web UI. When local
Leviathan is installed, the generated FlowMind graph now passes
`lev exec --flow ... --dry-run` with `format: graph`, `entry: ingest`, and
`nodeCount: 8`. Its ceiling remains explicit: it emits proposals and
runner-parseable scaffolds, but does not prove that a live Lev core/eval
runtime consumed the generated eval pack or that generated gates can promote
themselves.

The full product still keeps the hard ClaimGate gate as the only promotion
path. The post-fix `product:run` attempted the 27-seat 3x3x3 TeamHarness
topology, accepted 13 typed live seats across 3 providers and 7 models, and
recorded 14 failed/blocked/malformed seats literally. The post-fix `self:run`
attempted the same topology, accepted 14 typed live seats across 3 providers
and 7 models, and passed the honesty audit with
`admitted_on_synthesized_evidence: 0`. The live provider pool accepted 9 lanes
across OpenRouter, xAI, Google API, and Codex-native, while `gemini-cli-default`
failed with `exit_1`. The web UI keeps the original GitHub-native
trust-product direction:
"Can this work count?", with TeamHarness/Live Swarm, Source Truth, and Harness
Author tabs that surface current receipts without upgrading advisory or source
mining work into promotion evidence. The source ledger still reports
`properly_integrated_count: 0`: Wizard v4.3 is `adapter_partial`, the v19
Harness Author intake is `adapter_partial`, oh-my-openagent v4.12.0 is
`pattern_extracted`, the 0xRicker X post is `unresolved_source`, and the
YouTube marketing video is `not_processed`. The marketing lane is explicit but
not video-grounded yet: campaign brief -> variants -> metrics envelope ->
hard-wall verdict.

## Bottom line

The current research trend is clear:

> Agent performance is increasingly treated as a **model + harness** property, not a model-only property.

The strongest current papers point to the same architecture:

```text
LLM proposes / reasons
runtime harness mediates observation, memory, tools, action realization, validation, and trajectory control
execution traces feed harness improvement
regression tests + cross-audits decide whether a harness change survives
```

For our purposes, the useful phrase is:

```text
harness = executable runtime boundary around the model
```

Not just a prompt. Not just skills. Not just MCP. The harness is the runtime layer that decides what the model can observe, remember, attempt, execute, verify, and repeat.

## Screenshot seed / local-note status

The screenshot showed a set of note filenames being created:

- `breakthrough-synthesis.md`
- `breakthrough-deterministic-intervention-runtime.md`
- `breakthrough-skill-mcp-benchmarking.md`
- `breakthrough-topological-memory-read-model.md`
- `arxiv-2605.12061-sage-graph-memory-insights.md`
- `arxiv-2605.14355-herculean-financial-agent-benchmark-insights.md`
- `arxiv-2605.15701-h-mem-hybrid-memory-insights.md`
- `arxiv-2605.17734-hasp-skill-programs-insights.md`
- `arxiv-2605.20025-autoresearchclaw-insights.md`
- `arxiv-2605.22166-life-harness-insights.md`

Local search across the expected surfaces (`~/wiki`, `~/Codex-Ratchet`, `~/Desktop`, `~/Documents`, `~/Downloads`) did **not** find those exact files. Current status: visible in screenshot as intended/generated notes, but not located on disk in the expected places.

## Core papers / sources extracted

| ID / source | Title | Date | Harness relevance | Use for us |
|---|---:|---:|---|---|
| arXiv:2605.22166 | **Adapting the Interface, Not the Model: Runtime Harness Adaptation for Deterministic LLM Agents** / Life-Harness | May 2026 | Runtime harness adaptation across environment contracts, procedural skills, action realization, trajectory regulation. Reports 116/126 settings improved and 88.5% average relative improvement. | Strongest direct support for: fix the runtime interface, not only prompts/model weights. |
| arXiv:2606.09498 | **Self-Harness: Harnesses That Improve Themselves** | Jun 2026 | Weakness mining → harness proposal → regression validation. Reports Terminal-Bench 2.0 gains across MiniMax, Qwen, GLM. | Best current source for harness self-improvement loop; must pair with strict validation. |
| arXiv:2606.05922 | **Evolving Agents in the Dark: Retrospective Harness Optimization via Self-Preference** / RHO | Jun 2026 | Harness optimization from past rollouts without external labels. Coreset selection, re-solving, self-validation/self-consistency, candidate harness updates. | Useful for trace-mining and failure-derived harness tuning, but self-preference cannot be final authority. |
| arXiv:2605.17734 | **Harnessing LLM Agents with Skill Programs** / HASP | May 2026 | Converts textual skills into executable Program Functions that trigger and intervene in the agent loop. | Strong support for: skills must become executable guardrails, not passive text. |
| arXiv:2605.18747 | **Code as Agent Harness** | May 2026 | Survey framing code as operational substrate for reasoning, acting, environment modeling, verification, shared state, multi-agent coordination. | Good high-level taxonomy; supports code-mediated, verifiable, stateful harness design. |
| arXiv:2602.22480 | **VeRO: A Harness for Agents to Optimize Agents** | Feb/Jun 2026, ICML 2026 | Versioning, Rewards, Observations for agent-harness optimization and agent-on-agent improvement. | Useful infrastructure pattern: version every harness edit, capture observations, evaluate before acceptance. |
| arXiv:2605.12061 | **SAGE: Self-Evolving Agentic Graph-Memory Engine** | May 2026 | Reader/writer graph-memory engine; memory evolves from feedback. | Memory substrate for harness: graph memory, feedback-improved retrieval, evidence chains. |
| arXiv:2606.06036 | **Memory is Reconstructed, Not Retrieved: Graph Memory for LLM Agents** / MRAgent | Jun 2026, ICML 2026 | Active memory reconstruction over cue-tag-content graph; retrieval adapts during reasoning. | Supports dynamic memory access rather than static top-k recall. |
| arXiv:2604.12285 | **GAM: Hierarchical Graph-based Agentic Memory** | Apr 2026 | Event progression graph + topic associative network; consolidation on semantic shifts. | Good pattern for thread restart and wiki/memory synchronization: separate active event graph from stable knowledge. |
| arXiv:2605.15701 | **H-Mem: Hybrid Memory Mechanism** | May 2026 | Temporal/semantic tree plus knowledge graph for evolving agent memory. | Useful secondary memory design; tree+graph hybrid. |
| arXiv:2605.20025 | **AutoResearchClaw** | May 2026 | Multi-agent debate, self-healing executor, pivot/refine loop, verifiable result reporting, cross-run evolution, HITL modes. | Good research-harness pattern: failures become information; results must be execution-grounded. |
| arXiv:2605.14355 | **Herculean: Agentic Benchmark for Financial Intelligence** | May 2026 | MCP-based skill environments for professional workflows; agents struggle with hedging/auditing due to state consistency and structured verification. | Benchmark/positioning evidence for skill environments + workflow reliability; not a core implementation dependency. |
| Harness Bench / arXiv:2605.27922 | **Harness Bench** | May 2026 | Measures model-harness configuration effects over 106 sandboxed tasks, 5,194 trajectories. | Current benchmark lead for measuring harness effect directly. Needs deeper extraction later. |
| LangChain blog | **Improving Deep Agents with harness engineering** | Feb 2026 | Trace-driven harness engineering; prompt/tools/middleware knobs; Terminal-Bench improvement. | Practical engineering corroboration; blog, not primary paper. |

## What the field says now

### 1. Harnesses are no longer wrappers; they are runtime systems

Life-Harness, Code-as-Harness, Self-Harness, RHO, and VeRO all converge on this:

```text
model behavior = model weights + runtime harness + environment contract + memory + tool/action realization + trajectory control
```

So a harness has to own:

- observation shaping
- tool schemas
- action validation
- memory retrieval / reconstruction
- skill intervention
- trajectory loop control
- state persistence
- trace capture
- regression testing
- versioning / rollback

### 2. Text skills are too weak unless executable

HASP is the clearest source here. Textual skills are advisory. Program Functions are executable interventions.

For our systems this means:

```text
SKILL.md is not enough.
The harness needs executable skill gates / action modifiers / state checks.
```

### 3. Harness improvement is becoming trace-driven

Self-Harness, RHO, VeRO, and LangChain's harness-engineering blog all use the same loop:

```text
collect traces
mine failures
propose minimal harness edits
validate against held-out / regression tasks
accept only non-regressing edits
```

This is the right maintenance loop for Wizard/Hermes/Claude/Codex-style systems.

### 4. Memory is part of the harness, not an optional add-on

SAGE, MRAgent, GAM, and H-Mem point away from flat retrieval. Current direction:

```text
memory as graph / tree / event progression / active reconstruction
```

Important split:

- **active event memory**: current thread, volatile, high update rate
- **consolidated doctrine memory**: slower, stable, promoted only after semantic shift / audit
- **associative graph memory**: reconnects partial cues to evidence chains

This maps directly to wiki + session memory + durable memory synchronization.

### 5. Benchmarks are shifting from answer quality to workflow execution

Herculean, Harness Bench, VeRO-Bench, Terminal-Bench, τ-bench, AgentBench, SWE-bench, and MCP Atlas all stress the same issue:

```text
Can the agent execute a workflow reliably under tools, state, constraints, and verification?
```

Static QA is no longer enough.

## Architecture implication for our harness work

The right harness shape is:

```text
1. Active contract
   - current project / role / authority / allowed actions

2. Memory layer
   - active event graph
   - stable wiki/doctrine layer
   - associative retrieval / reconstruction

3. Skill layer
   - text skills become executable interventions where possible

4. Action realization layer
   - model proposes structured action
   - harness validates and executes or blocks

5. Trajectory regulator
   - loop detection
   - fake-progress detection
   - failed-gate repetition detection
   - reroute / pause / audit switch

6. Trace miner / self-improvement loop
   - mine failures
   - propose minimal harness edits
   - validate against regression suite
   - accept only non-regressing edits
```

## Research gaps to pursue next

1. **Runtime-truth validation**
   - How to prove a real route ran, not just that a receipt shape exists?
   - Most current papers still rely heavily on trace/eval outcomes, not unforgeable runtime proof.

2. **Harness edit safety**
   - Self-Harness and RHO improve harnesses, but the hard question is regression-free improvement under partial feedback.
   - VeRO helps with versioning/rewards/observations, but semantic regression remains open.

3. **Cross-model harness transfer vs model-specific harnesses**
   - Life-Harness reports transfer across 17 models from Qwen3-4B trajectories.
   - Self-Harness emphasizes model-specific weaknesses.
   - This is a live tension: universal environment-side structure vs model-specific adaptation.

4. **Memory consolidation truth**
   - SAGE/MRAgent/GAM/H-Mem all improve memory, but the question is what promotes from event memory into doctrine.
   - Need promotion gates, not just retrieval accuracy.

5. **Execution rails vs output rails**
   - Guardrail industry sources now emphasize execution rails: validate tool arguments/actions before execution.
   - This is central for destructive tools, repo writes, git, cron, and agent spawning.

6. **Benchmarking harness+model pairs**
   - Harness Bench and local harness-bench efforts explicitly measure model/harness combinations.
   - This should be tracked because it directly tests the claim that harnesses can matter as much as model choice.

## Immediate next extraction targets

Need deeper extraction, not just abstracts:

1. `arXiv:2606.09498` Self-Harness — proposal validation details + regression testing setup.
2. `arXiv:2606.05922` RHO — self-preference failure modes; whether it has anti-collapse/anti-regression controls.
3. `arXiv:2605.18747` Code as Agent Harness — taxonomy table + open challenges.
4. `arXiv:2605.22166` Life-Harness — exact four-layer implementation inventory.
5. `arXiv:2605.27922` Harness Bench — methodology, task categories, how model-harness effects are isolated.
6. `arXiv:2605.17734` HASP — Program Function trigger/intervention mechanics.

## Working synthesis

The current harness frontier is not "better prompting."

It is:

```text
turning agent scaffolding into executable, versioned, trace-mined, regression-tested runtime infrastructure.
```

The strongest pattern for us is:

```text
Life-Harness gives the runtime-interface frame.
HASP gives executable skills.
Code-as-Harness gives code/state/verifiability taxonomy.
VeRO gives versioning/rewards/observations for optimization.
Self-Harness and RHO give failure-mining harness evolution.
SAGE/MRAgent/GAM/H-Mem give memory architecture.
Harness Bench / Herculean give benchmark pressure.
```

## Source status

- Screenshot-local notes: exact filenames visible but not found on disk in expected local locations.
- Web extraction: completed for core arXiv set listed above.
- This doc: restart/front-door note for continued harness research.
