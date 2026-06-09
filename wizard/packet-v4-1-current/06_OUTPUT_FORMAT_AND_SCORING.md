---
title: Wizard v4.1 Output Format and Scoring
type: output_contract
packet: v4.1
framing: standalone
---

# Output Format And Scoring v4.1

The visible answer should be readable, structured, and useful.

It should not look like a raw log.

The visible answer should reduce cognitive load. It should feel pleasant to the eye and mind: short sections, useful labels, a little visual character, and no route machinery unless it helps the user decide.

## Cognitive Load Budget

Default visible output should fit this shape:

- one clear answer;
- one short context-aware voice block for Strategy, Systems, and Factory when the run is about the Wizard or a broad work system;
- three short council result blocks;
- one compiled move;
- three to four follow-up options;
- one footer.

Avoid:

- raw worker logs;
- long route inventories;
- duplicate caveats;
- more than four visible follow-up options;
- asking the user for a prompt when source context is enough.

## Beauty And Readability Gate

Wizard output is a user interface, not a receipt dump. A technically accurate
answer still fails if the user has to parse it like a log.

Before sending, apply this visible-surface filter:

- `## ✨ Answer` starts with the accepted outcome in one or two plain
  paragraphs. It does not open with paths, route counts, stale queue inventory,
  or command results.
- File paths are used only when they are the artifact the user should care
  about. Do not stack three or more file links in the opening answer unless the
  task is specifically a file audit.
- Council sections show the council wisdom first. Route truth supports the
  council; it is not the council.
- Repeated `Aggregate:`, `Blocked/deferred:`, `parents`, `children`,
  `obligation`, and runtime details are compressed into one `Proof:` line per
  council or the footer.
- The `Members:` line names conceptual members that ran, not controller
  plumbing. Prefer `Strategy 3/5, Systems 3/5, Factory 3/5` over
  `Decision parent 1/1, child count 3/5 obligation`.
- Follow-up options are pleasant prompt cards, never fenced prompt/code boxes.
  Use a normal quoted prompt sentence plus `Why this helps`, `Use when`, and
  `Stop if`.
- Diagnostics that mostly serve route-truth accounting belong in the footer,
  capped at two compact lines.

If a draft looks like a CI log, worker log, receipt inventory, or contract
audit, rewrite it into this order: outcome, council wisdom, compiled move,
pleasant next prompts, footer truth.

## Ambient Start Output

When the Wizard runs without an initial prompt, include a short source-scan line:

```text
Source scan: repo docs, active packet, and current verification artifacts.
```

Then proceed normally. Do not make the user supply a prompt just to start.

## Header

Use this header for visible Wizard runs:

```text
🧙 Wizard v4.1 | {FULL|PARTIAL|BLOCKED} | waves:{completed/3}[ partial-coverage] | parents:{completed/required} | children:{completed/obligation}[ blocked|deferred|not-run] | [tools:{completed} | ]score:{0-100} | runtimes:{names}
```

The first line of every visible Wizard operational answer must be this v4.1 scored header when any Decision, Failure, or Follow-Up council wave ran, or when the user is evaluating Wizard runtime/route truth.

Examples:

```text
🧙 Wizard v4.1 | FULL | waves:3/3 | parents:12/12 | children:9/9 | score:94 | runtimes:codex,claude,tools
🧙 Wizard v4.1 | PARTIAL | waves:3/3 partial-coverage | parents:18/32 | children:0/1 blocked | tools:1 | score:72 | runtimes:codex-native,tools
🧙 Wizard v4.1 | PARTIAL | waves:2/3 | parents:7/10 | children:2/6 blocked | score:63 | runtimes:codex
🧙 Wizard v4.1 | BLOCKED | waves:1/3 | parents:2/9 | children:0/9 not-run | score:31 | runtimes:self
```

Do not print `FULL` unless the full-run minimum passes.

Do not print `COMPACT` in v4.1. Compact mode is not specified yet.

Wizard-relevant work done without a proper Decision/Failure/Follow-Up run is not valid work product. Do not close it as successful ordinary output. If only boot, preflight, source scan, tool inspection, or implementation work ran, emit a `BLOCKED` or `PARTIAL` v4.1 header that names the missing council, parent, and child obligations, then retry the smallest missing route when safe.

A follow-up option is the next Wizard input. Do not say "no fresh three-council run header" because a chosen follow-up was "only option execution." The chosen option must boot v4.1, run Decision, Failure, and Follow-Up on the option plus prior prework, then compile the next move and next follow-up options.

Selector-only inputs such as `4`, `1-4`, `all`, and `All of the Above` are not the whole scope. They are pointers to the prior next-input handoff. The Wizard must join the selected option with current thread state, source context, packet docs, MMM surfaces, prior prework, and relevant artifacts before it drafts an answer. A repair-only or test-only report is valid only when it is explicitly shown as a blocked/partial Wizard run with the missing council, parent, and child obligations named.

The Wizard is general-purpose. Follow-up prework may inspect docs, run tests, map refactors, reproduce bugs, scout research sources, draft implementation handoffs, or use adapter-specific tools. For Codex Ratchet sim work, follow-up prework may run cheap local sims when the strict sim profile passes. Show those sim receipts as preworked evidence for the next Wizard loop, not as a replacement for the next loop or as queue/readiness proof.

## v4.1 Route-Truth Reconciliation Gate

Before emitting the visible header, footer, or follow-up options, reconcile four count families separately:

- waves: completed sequential receipt-boundary passes;
- parents: completed accepted parent subagents against required selected members;
- children: completed accepted child/subsubagent receipts against the current child route obligation;
- tools: completed tool or harness checks.

Do not count a tool check as a child/subsubagent receipt. If a conformance harness, command, or local checker ran, report it under `tools:{n}` or in verification, never under `children`.

Do not advertise a runtime in `runtimes:{names}` unless an accepted receipt or completed tool check proves that runtime. Model names and reasoning levels belong in child `variant_signature` and `rerouter_ledger` fields, not in the header runtime list unless the runtime itself was used and receipt-backed.

If all three waves crossed their sequential barriers but member coverage was incomplete, write `waves:3/3 partial-coverage`. Plain `waves:3/3` is reserved for complete selected-member coverage.

If children/subsubagents were attempted but did not complete, write a child status marker: `blocked`, `deferred`, or `not-run`. The footer must use the same truth as the header. It cannot say "no children were proven" while the header says `children:1/1`.

If the runtime supports parent-launched child/subsubagent routes and a visible three-council run required them, do not write `children:0/0 not-run`. Show the obligation, for example `children:0/3 not-run`.

Before any visible header counts Claude Bridge children from more than one
parent, run or inspect the fanout receipt summary helper and reconcile the
summary against the per-parent obligation. A fanout batch with global timeout,
budget failures, not-launched children, or weak/no-delta receipts is `PARTIAL`
until the failed children are rerun or explicitly marked blocked.

Quality drift beats raw completion. A large child batch can finish and still be
partial when the child receipts are shape-identical, do not change the parent,
or lack artifact-facing deltas.

Loop output must show loop state without becoming a loop log. The footer may
name `loop:{n}/{cap}`, `new_findings:{n}`, `resolved:{n}`, and
`done_status:{done|continue|cap_reached|blocked}`. The answer body should
describe the accepted move, not enumerate every receipt.

For loop closeout, do not write `done` unless the compile gate records the done
predicate: configured consecutive empty-new-finding loops observed, no
unresolved load-bearing findings, and audit fixed point. Otherwise say
`continue`, `cap_reached`, or `blocked`.

For loop iterations after the first, `cross_loop` must cite at least one prior
finding id under supersedes, kills, extends, resolved, or unchanged. If it does
not, the output is a non-advancing re-prompt and the score is capped at 70.

For loop iterations after the first, `cross_loop.dispositions` must cover every
prior load-bearing open finding under exactly one disposition: supersedes,
kills, extends, resolved, or unchanged. Missing prior ids, duplicate prior ids,
or dispositions without rationale and artifact/clause references forbid `done`
and cap score at 75.

If runtime has no spawn surface for a substantive Wizard route, the header must
be `BLOCKED` with the missed parent/child obligation. `FULL` is forbidden.

If any required child model family is blocked without a smaller-retry or
accepted degraded-family receipt, `FULL` is forbidden and the missing family
must be named in the footer.

The FULL/PARTIAL label must be computed from
`manager.resource_pressure.model_family_statuses` and
`degraded_alt_child_families`, not from a footer note.

If `post_follow_up_compile_gate.terminal_status` is not `passed`, visible
follow-up options cannot be labeled `ready_for_execution`.

Every visible loop answer after loop 1 must include a compact
`wizard_loop_state` YAML block or artifact reference with `cross_loop`,
`done_predicate`, and current unresolved count. Prose-only loop state fails
self-repair.

The `wizard_loop_state` block is the operative loop state. Prose may summarize
it, but prose must not duplicate, override, or contradict the YAML state.
If prose says `done`, `ready`, `resolved`, or `FULL` while the operative YAML
state or accepted receipts say `continue`, `blocked`, `unresolved`, `PARTIAL`,
or missing coverage, visible self-repair fails. The renderer must reconcile the
YAML and prose before output; it cannot hide the contradiction in the footer.
Visible prose must use the canonical loop status token from
`wizard_loop_state.done_predicate.terminal_status`; do not invent completion
synonyms such as closed, green, shipped, ratcheted, finished, or clean outside
the operative block. If human-readable prose needs to mention status, write
`done_status:<token>` and keep the token identical to YAML.

When the cross-loop ledger is large, the visible answer may cite
`cross_loop.dispositions_ref` and show only `disposition_summary`. It may not
truncate the only copy of the disposition list.

If `manager.resource_pressure.model_family_statuses[family]` is absent for a
required family in a substantive Codex-adapter run, treat that family as
`BLOCKED` for the header computation until an accepted smaller-retry or
degraded-family receipt names the reason and substitute signal.
Whether a run is substantive Codex-adapter work is computed from receipts, not
renderer discretion. Accepted Wizard route receipts involving Codex-native,
Claude Bridge, Opus, Sonnet, Haiku, Gemini, or OMX/tmux activate model-family
accounting unless an accepted atomic/low-decomposition override says otherwise.
Tool and harness checks remain separate proof surfaces; they do not activate
or satisfy model-family accounting by themselves.

Visible verification counts must be current and tied to the exact command or harness that produced them:

```text
- `python3 -m pytest system_v5/tests/test_wizard_v4_conformance.py -q` -> 41 passed
```

Do not write naked stale summaries like `35 passed` or `48 passed` unless the exact command and fresh result are also shown.

## Visible Output Self-Repair Gate

Before sending, the main thread privately checks the drafted answer. If it fails, rewrite the answer and send only the repaired version.

The answer fails this gate when:

- it uses bold pseudo-headings such as `**Main Answer**`, `**Council Results**`, `**Follow-Up**`, or `**Verification**` instead of real Markdown sections;
- it lacks the required visible sections: `## ✨ Answer`, `## 🏛️ Council Results`, `## ✅ Compiled Move`, `## 🧭 Follow-Up Options`, and final `## 🧙 Footer`;
- it replaces the three council identities with option/route labels such as Proof, Premortem, Scout, Make, Run, Audit, Direct, or All of the Above;
- the `### 🛡️ Failure` section's first `Members:` line does not include
  `Premortem` with a compact passed or blocked ratio;
- it treats follow-up option execution as outside the Wizard loop;
- it lacks a concise MMM proof line showing full-MMM and mini-MMM receipt evidence;
- the footer is not the final top-level section or does not begin with `🧙 Time/value:`;
- the compiled move omits owner/lane, stop/failure condition, artifact/output surface, or status;
- follow-up options are not readable prompt cards with payoff, use condition, and stop/block condition;
- the header hides route obligations or contradicts the footer;
- the header advertises unproven runtime/model breadth;
- any Decision, Failure, or Follow-Up council wave ran and the first line is not the Wizard v4.1 scored header;
- the `## ✨ Answer` section opens with route bookkeeping such as `I ran`, `Option`, `Parent receipt`, `Child receipt`, `Parents:`, `Children:`, `Tools:`, `Route truth:`, or `Truth boundary:` instead of the accepted move/outcome in plain language;
- the visible `score:{n}` does not match the computed conformance score;
- it relies on `from the prior run` council or receipt counts in a current Wizard header;
- verification counts are stale, naked, or not command-tied;
- it treats a selector-only input as the whole scope instead of joining the prior handoff, current thread state, repo/source docs, packet docs, MMM surfaces, and artifacts;
- it answers a Wizard-relevant input as only a repair/test pass without route-truth status;
- it omits route-truth status for Wizard-relevant output when no council waves ran;
- it closes Wizard-relevant work as useful or accepted when no proper Decision/Failure/Follow-Up run happened;
- it says no further action is authorized, waits for the next explicit input, or otherwise idles when Ambient Start Mode has enough source context to infer a bounded move.
- the visible answer reads like a worker log: repeated aggregate counts,
  route-obligation prose in every council, dense file/path lists in the opening
  answer, or follow-up options wrapped as fenced boxes instead of readable
  prompt cards;
- council `Members:` lines name plumbing such as `Decision parent`,
  `Follow-Up parent`, or `child count obligation` instead of meaningful member
  families and compact ratios;
- `Blocked/deferred` appears before the council result, or appears repeatedly
  in multiple council sections when one footer truth line would suffice;
- the `## ✨ Answer` section contains more route bookkeeping than user-facing
  decision content;
- the first paragraph contains `parents`, `children`, `receipts`,
  `route truth`, `blocked/deferred`, or command output unless the user asked
  for diagnostics;
- any council `Result:` line starts with counts, blockers, runtime names, or
  receipt references instead of council judgment;
- the same blocker or caveat appears in more than one council section when one
  footer truth line would preserve it;
- any normal council section exceeds four short content lines after its
  heading;
- `Proof:` contains individual receipt ids, paths, or worker logs instead of
  aggregate accepted/blocked truth;
- follow-up options are fenced code blocks or raw prompt dumps without payoff,
  pre-check, use condition, and stop condition;
- footer route-truth diagnostics exceed two compact lines unless the user
  asked for route diagnostics;
- the answer reads chronologically, such as "I inspected, then I ran, then I
  found," instead of decision-first;
- file paths appear in the opening answer when the artifact itself is not the
  user-facing deliverable;
- `FULL`, `ready`, or `done` appears before route truth and compile-gate status
  have been reconciled;
- follow-up options lack an `All of the Above` option when multiple useful
  options are shown.
- loop output says `done` without a compile-gate done predicate;
- loop output lacks a `cross_loop` relationship after loop 1;
- a premortem route says the skill loaded when it only invoked the method and
  did not read `skills/premortem/SKILL.md`.
- prose claims a loop is done, ready, resolved, or full while the operative
  `wizard_loop_state`, manager resource-pressure fields, or receipts say
  continue, blocked, unresolved, partial, or missing family coverage;
- prose uses completion synonyms outside the canonical
  `done_status:<terminal_status>` token;
- a required model-family key is absent from
  `manager.resource_pressure.model_family_statuses` during a substantive
  Codex-adapter run.
- a loop after the first lacks prior finding ids in `cross_loop`;
- `FULL` appears when the runtime had no spawn surface for required
  parent/child work;
- a follow-up option says `ready_for_execution` while the post-Follow-Up
  compile gate is missing or blocked.
- a loop after the first fails to cover every prior load-bearing open finding
  under exactly one `cross_loop` disposition;
- a `cross_loop` disposition lacks rationale, artifact/clause reference, or a
  real delta for `extends`;
- a loop fixed point uses sibling audits with no independence vector;
- a loop fixed point uses only timestamp or model-label differences as its
  independence vector;
- premortem skill body read provenance comes from a different worker than the
  premortem synthesis without marking the route `degraded_local`;
- premortem skill body read provenance names an unversioned or stale skill path
  without packet/source digest or adapter-delta mirror proof;
- loop state appears only as prose when `loop_iteration > 1`.

This gate repairs the answer. It should not appear as a visible audit section unless the user explicitly asks for diagnostics.

## Council Results

Each council section must begin with a compact `Members:` line so the user can
see the actual council composition and route-truth ratios immediately. This
comes before the result sentence, proof, counts, or commentary.

Use this order for every visible council section:

1. `Members:` named members with compact `passed/total-ran-agents` ratios.
2. `Result:` what the council changed.
3. `Why it matters:` or `What changed:` when useful.
4. `Proof:` aggregate parent/child/tool truth.

Do not move `Members:` to the end. If the named members and ratios are not
visible before the result, the output fails self-repair.

For a visible full run, name the three nested parent councils in each wave:
Decision `Voices`, `Six Hats`, `Experts`; Failure `Premortem`, `Falsifiers`,
`Loophole Auditor`; Follow-Up `Prompt Voices`, `Lanes`, `Compile Gate`. Do not hide
this as a raw count; show the human meaning of the council and then the
proof/counts. Individual voices, hats, lanes, and compile-gate fields should
appear as child/subsubagent proof under their council parent, not as parent
council seats.

When a parent member represents nested children, the visible council result
should show the child impact, not the raw child log. Good examples:
`Six Hats 6/6, impact: Black killed broad launch; Green added smaller probe`.
`Lanes 5/5, impact: Back set stop condition; Direct became accepted move`.

The `Members:` line is not a substitute for the council result. It is the
visible route-truth proof that named members actually ran. Use each member's
accepted-child ratio in `member passed/total-ran-agents` form, for example
`Systems 4/4`, `Factory 3/4`, `Premortem 4/5 after reroute`, `Six Hats 6/6`,
`Lanes 5/5`. The denominator is the number of agents/children actually
attempted for that member, plus accepted reroutes when they replace a failed
core child. The numerator is accepted useful receipts only. Do not count tool
checks, controller synthesis, pending starts, or timed-out children as passed
agents.

If a council section names members but omits the ratios, the output fails
self-repair. If a member is important to the result and has `0/N`, mark the run
`PARTIAL` or `BLOCKED` and explain the reroute/stop boundary.

Keep each council section compact. In normal visible output, use at most four
short lines after the heading:

```text
Members: Strategy 3/5, Systems 3/5, Factory 3/5.
Result: ...
Why it matters: ...
Proof: ...
```

Do not repeat the same child-coverage caveat in all three councils. State the
local implication once where it changes the council result, then put global
route truth in the footer.

```text
Members: Feynman 5/5, Factory 5/5, Strategy 5/5, Systems 5/5, Six Hats 6/6, Experts 5/5.
Result: The smallest useful move is ...
Why it matters: ...
Proof: 12/12 parent members accepted, 60/60 child receipts accepted across Codex-native, Opus, Sonnet, Haiku, and Gemini-attempt/degraded coverage. Tool checks reported separately. Blocked: none. Rerouted: none.
```

```text
Members: Premortem 5/5, Falsifiers 5/5, Loophole Auditor 6/6.
Result: Outcome is harden_then_execute because ...
What changed: ...
Proof: 9/9 parent members accepted, 45/45 child receipts accepted across Codex-native, Opus, Sonnet, Haiku, and Gemini-attempt/degraded coverage. Tool checks reported separately. Blocked: none.
```

Failure Council requires `Premortem` in this line. If premortem did not run,
show the blocked ratio and mark the run partial or blocked; do not silently
replace it with Black Hat, Popper, Pushback, postmortem, calibration, expert
critique, or receipt audit.

```text
Members: Orwell 5/5, Strategy 5/5, Factory 5/5, Six Hats 6/6, Lanes 5/5, Experts 5/5.
Result: Best next prompts are ...
Why they are useful: ...
Proof: 11/11 parent members accepted, 55/55 child receipts accepted across Codex-native, Opus, Sonnet, Haiku, and Gemini-attempt/degraded coverage. Tool checks reported separately. Accepted options: 4.
```

Council result sections must not start with raw route bookkeeping such as
`Blocked:`, `Rerouted:`, `Run truth:`, `Receipts:`, receipt inventory, or
parent/child inventory. `Members:` is the required first line because it is
human council composition plus compact route truth, not a raw log.

The visible council subsections must preserve the canonical council identities:

- `### 🧠 Decision`
- `### 🛡️ Failure`
- `### 🧭 Follow-Up`

Do not replace them with route labels such as `### 🧪 Proof`, `### 🛡️ Premortem`, or `### 🧭 Scout`. Route labels belong inside results, follow-up options, or execution reports.

## Recommended Visible Shape

🧙 Wizard v4.1 | FULL | waves:3/3 | parents:9/9 | children:49/49 | score:94 | runtimes:codex,claude,gemini,tools

## ✨ Answer
The best bounded move is ...

## 🧩 Context-Aware Voices
♟️ Strategy:
🔁 Systems:
🏭 Factory:

## 🏛️ Council Results
Wizard Harness council results: Three LLM councils ran as sequential write barriers: Decision chose the move, Failure tested it, and Follow-Up compiled usable next prompts.

### 🧠 Decision
Members: Feynman 5/5, Factory 5/5, Strategy 5/5, Systems 5/5, Six Hats 6/6, Experts 5/5.
Result:
Why it matters:
Proof:

### 🛡️ Failure
Members: Premortem 6/6, Falsifiers 5/5, Loophole Auditor 6/6.
Result:
What changed:
Proof:

### 🧭 Follow-Up
Members: Orwell 5/5, Strategy 5/5, Factory 5/5, Six Hats 6/6, Lanes 5/5, Experts 5/5.
Result:
Accepted options:
Proof:

## ✅ Compiled Move
- Target:
- Immediate action:
- Owner/lane:
- Success check:
- Stop condition:
- Artifact/output:
- Status:

## 🧭 Follow-Up Options
1. 🧰 Direct: "..."
   Why this helps:
   Pre-checked:
   Use this when:
   Stop if:

2. 🔁 Alternative: "..."
   Why this helps:
   Pre-checked:
   Use this when:
   Stop if:

3. 🧪 Proof: "..."
   Why this helps:
   Pre-checked:
   Use this when:
   Stop if:

4. 🧩 All of the Above: "..."
   Why this helps:
   Pre-checked:
   Use this when:
   Stop if:

## 🧙 Footer
🧙 Time/value: {worth_it|marginal|not_worth_it} | time:{short|medium|long} | value:{low|medium|high} | reason:{one plain sentence}
Status:
Proof:
MMM proof:
Verification:
Limit:
Next retry if needed:
Source scan: only when the run had no initial prompt.

The footer is mandatory for every visible Wizard output. It must be the final top-level section, must be led by `## 🧙 Footer`, and its first nonblank line must be `🧙 Time/value:`. The time/value line states whether the output's expected value is commensurate with the reader's time cost.

## Score

Score out of 100:

- 20 points: main full MMM loaded before runtime rules.
- 20 points: three council waves completed in sequence.
- 20 points: required parent members completed with exact mini-MMM load receipts.
- 15 points: child/subsubagent receipts completed where supported, with tool
  and harness checks scored separately under verification.
- 15 points: compile gate passed for accepted options.
- 10 points: visible output is readable, not a worker log, and includes blockers.

Automatic caps:

- Cap at 40 if main full MMM was not loaded.
- Cap at 50 if any council is missing.
- Cap at 60 if no parent workers actually ran.
- Cap at 70 if no child/subsubagent was attempted despite runtime support.
- Cap at 70 if child lanes were marked blocked because there was "no exact
  implementation task" or "nothing useful for a child to do." Those are not
  valid blockers; use a model/reasoning variant, falsifier, scout, salience
  check, receipt audit, or follow-up improver.
- Cap at 75 if a substantive Codex-adapter run with available child runtimes
  lacks the Codex-native/Opus/Sonnet/Haiku/Gemini child model matrix.
- Cap at 75 if any counted parent in a substantive Codex-adapter run has fewer
  than five accepted child/subsubagent receipts and no explicit
  atomic/low-decomposition override.
- Cap at 80 if any counted parent has more than ten child/subsubagent receipts
  without a stress-test label and receipt-shape/divergence audit.
- Cap at 80 if follow-up options fail compile gate.
- Cap at 85 if output lacks council notation.
- Cap at 85 if output hides the three LLM councils or omits Strategy, Systems, and Factory context voices for a Wizard/system run.
- Cap at 85 if output lacks a footer.
- Cap at 85 if the footer is not the final section or lacks a leading `🧙 Time/value:` signal.
- Cap at 85 if follow-up options lack a human-readable `All of the Above` option.
- Cap at 85 if council sections read like a worker log instead of result-first synthesis.
- Cap at 85 if visible follow-up options were not pre-run/audited/improved.
- Cap at 85 if tools are counted as children or if the footer contradicts the header route truth.
- Cap at 85 if `waves:3/3` hides partial parent/member coverage.
- Cap at 85 if `children:0/0 not-run` hides a required child/subsubagent route obligation.
- Cap at 85 if verification counts are stale or not command-tied.
- Cap at 85 if the answer uses pseudo-headings instead of the required Markdown sections.
- Cap at 85 if the answer replaces Decision/Failure/Follow-Up with option or lane labels.
- Cap at 85 if the answer does not surface full-MMM and mini-MMM proof.
- Cap at 85 if MMM proof counts contradict header parent counts.
- Cap at 85 if the header score does not match computed conformance.
- Cap at 85 if a current Wizard header relies on prior-run council receipts.

## Retry Decision

- `score >= 90`: full accepted.
- `75 <= score < 90`: usable partial; show blockers and one retry prompt.
- `50 <= score < 75`: retry missing route(s) before presenting as useful unless user asked for diagnostics.
- `score < 50`: blocked/failed run; rerun the smallest missing route or report the blocker.

If the system can safely retry, it should retry before final output.
