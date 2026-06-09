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

Examples:

```text
🧙 Wizard v4.1 | FULL | waves:3/3 | parents:12/12 | children:9/9 | score:94 | runtimes:codex,claude,tools
🧙 Wizard v4.1 | PARTIAL | waves:3/3 partial-coverage | parents:18/32 | children:0/1 blocked | tools:1 | score:72 | runtimes:codex-native,tools
🧙 Wizard v4.1 | PARTIAL | waves:2/3 | parents:7/10 | children:2/6 blocked | score:63 | runtimes:codex
🧙 Wizard v4.1 | BLOCKED | waves:1/3 | parents:2/9 | children:0/0 | score:31 | runtimes:self
```

Do not print `FULL` unless the full-run minimum passes.

Do not print `COMPACT` in v4.0. Compact mode is not specified yet.

If no councils actually ran, do not use a Wizard run header. Use ordinary answer formatting and state the limitation in `## 🧙 Footer`.

## v4.1 Route-Truth Reconciliation Gate

Before emitting the visible header, footer, or follow-up options, reconcile four count families separately:

- waves: completed sequential receipt-boundary passes;
- parents: completed accepted parent subagents against required selected members;
- children: completed accepted child/subsubagent receipts against the current child route obligation;
- tools: completed tool or harness checks.

Do not count a tool check as a child/subsubagent receipt. If a conformance harness, command, or local checker ran, report it under `tools:{n}` or in verification, never under `children`.

If all three waves crossed their sequential barriers but member coverage was incomplete, write `waves:3/3 partial-coverage`. Plain `waves:3/3` is reserved for complete selected-member coverage.

If children/subsubagents were attempted but did not complete, write a child status marker: `blocked`, `deferred`, or `not-run`. The footer must use the same truth as the header. It cannot say "no children were proven" while the header says `children:1/1`.

If the runtime supports parent-launched child/subsubagent routes and a visible three-council run required them, do not write `children:0/0 not-run`. Show the obligation, for example `children:0/3 not-run`.

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
- it lacks a concise MMM proof line showing full-MMM and mini-MMM receipt evidence;
- the footer is not the final top-level section or does not begin with `🧙 Time/value:`;
- the compiled move omits owner/lane, stop/failure condition, artifact/output surface, or status;
- follow-up options are not copy-pasteable prompts with payoff, use condition, and stop/block condition;
- the header hides route obligations or contradicts the footer;
- the visible `score:{n}` does not match the computed conformance score;
- it relies on `from the prior run` council or receipt counts in a current Wizard header;
- verification counts are stale, naked, or not command-tied.

This gate repairs the answer. It should not appear as a visible audit section unless the user explicitly asks for diagnostics.

## Council Results

Each council section should explain what the council changed for the user. It is not a worker ledger.

Use short result sentences first. Put proof/counts after the result, not before it.

For a visible full run, name the member families that actually ran: divergent voices, Six Thinking Hats, premortem/failure lenses, expert.what_experts_say, lanes, compositions, and guards. Do not hide this as a raw count; show the human meaning of the council and then the proof/counts.

```text
🧭 Decision: The smallest useful move is ...
Why it matters: ...
Proof: 12/12 parent members accepted, 1/1 child/tool checks accepted. Blocked: none. Rerouted: none.
```

```text
🛡️ Failure: Outcome is harden_then_execute because ...
What changed: ...
Proof: 9/9 parent members accepted, 1/1 child/tool checks accepted. Blocked: none.
```

```text
🧭 Follow-Up: Best next prompts are ...
Why they are useful: ...
Proof: 11/11 parent members accepted, 1/1 child/tool checks accepted. Accepted options: 4.
```

Council result sections must not start with `Ran:`, `Blocked:`, `Rerouted:`, `Run truth:`, `Receipts:`, receipt inventory, or parent/child inventory. Those details are allowed only after the human result.

The visible council subsections must preserve the canonical council identities:

- `### 🧠 Decision`
- `### 🛡️ Failure`
- `### 🧭 Follow-Up`

Do not replace them with route labels such as `### 🧪 Proof`, `### 🛡️ Premortem`, or `### 🧭 Scout`. Route labels belong inside results, follow-up options, or execution reports.

## Recommended Visible Shape

```markdown
🧙 Wizard v4.1 | FULL | waves:3/3 | parents:32/32 | children:3/3 | score:94 | runtimes:codex,claude,tools

## ✨ Answer
The best bounded move is ...

## 🧩 Context-Aware Voices
♟️ Strategy:
🔁 Systems:
🏭 Factory:

## 🏛️ Council Results
Three LLM councils ran as sequential write barriers: Decision chose the move, Failure tested it, and Follow-Up compiled usable next prompts.

### 🧠 Decision
Members:
Result:
Why it matters:
Proof:

### 🛡️ Failure
Members:
Result:
What changed:
Proof:

### 🧭 Follow-Up
Members:
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
   First step:
   Pre-checked:
   Use this when:
   Do not use if:

2. 🔁 Alternative: "..."
   Why this helps:
   First step:
   Pre-checked:
   Use this when:
   Do not use if:

3. 🧪 Proof: "..."
   Why this helps:
   First step:
   Pre-checked:
   Use this when:
   Do not use if:

4. 🧩 All of the Above: "..."
   Why this helps:
   First step:
   Pre-checked:
   Use this when:
   Do not use if:

## 🧙 Footer
🧙 Time/value: {worth_it|marginal|not_worth_it} | time:{short|medium|long} | value:{low|medium|high} | reason:{one plain sentence}
Status:
Proof:
MMM proof:
Verification:
Limit:
Next retry if needed:
Source scan: only when the run had no initial prompt.
```

The footer is mandatory for every visible Wizard output. It must be the final top-level section, must be led by `## 🧙 Footer`, and its first nonblank line must be `🧙 Time/value:`. The time/value line states whether the output's expected value is commensurate with the reader's time cost.

## Score

Score out of 100:

- 20 points: main full MMM loaded before runtime rules.
- 20 points: three council waves completed in sequence.
- 20 points: required parent members completed with exact mini-MMM load receipts.
- 15 points: child/subsubagent or tool child receipts completed where supported.
- 15 points: compile gate passed for accepted options.
- 10 points: visible output is readable, not a worker log, and includes blockers.

Automatic caps:

- Cap at 40 if main full MMM was not loaded.
- Cap at 50 if any council is missing.
- Cap at 60 if no parent workers actually ran.
- Cap at 70 if no child/tool child was attempted despite runtime support.
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
