# Hermes answer-surface stress rubric — 2026-04-21

Purpose: evaluate whether a bounded Hermes output packet is staying plural, adaptive, readable, and operational as models, launchers, and skills shift.

Status: active stress-test rubric note.

## Use this for
- bounded formatting/output stress tests
- cross-model worker comparisons
- audit-loop evaluation
- deciding whether a launcher or skill still earns a place in the active stack
- deciding what to offload into wiki, skills, or self-evolution inputs

## Packet shape
A good packet is small and explicit.

Recommended packet fields:
- task
- worker family or families
- audit family or families
- launcher/runtime path per family
- runtime registry
- receipts
- synthesis
- wiki/skill follow-through

## Core scoring dimensions

### 1. Body voice fidelity
Questions:
- Does the main body visibly use more than one voice?
- Does `🦉 Hume` stay grounded instead of swallowing the whole reply?
- Do other voices do real work in the prose itself?
- Can a voice recur more than once when the reasoning job genuinely recurs?

Pass signs:
- at least 3 distinct reasoning jobs are visible in the body
- voice labels could not be swapped without changing the reasoning
- semantic emojis appear in the body where the voice is load-bearing

Fail signs:
- everything collapses into one summary voice
- voices appear only in follow-up or labels
- repeated voice calls add no new job

### 2. Council survival
Questions:
- Are multiple narratives still visible after synthesis?
- Did the synthesis preserve surviving disagreement rather than smoothing it away?
- Is there a visible council or equivalent receipt block when needed?

Pass signs:
- at least one surviving tension is explicitly preserved when evidence does not close it
- council receipts stay separate enough to compare
- the answer names what the council agreed on and what it did not

Fail signs:
- one model/voice story eats the others without evidence
- council is decorative rather than load-bearing
- plurality is present in the workers but erased in the answer

### 3. Pushback honesty
Questions:
- Did any voice or auditor clearly push back where the prior surface or current plan failed?
- Was that pushback specific enough to change the next move?

Pass signs:
- at least one explicit pressure-test or pushback survives when the packet warrants it
- the falsifier or failure mode is concrete

Fail signs:
- politeness hides a real failure
- "audit" language appears without naming what failed
- pushback is absent where a real contradiction or weak assumption existed

### 4. Follow-up quality
Questions:
- Does each visible lane/voice change what the user can do next?
- Are the two all-of-the-above bundles explicit and materially different?
- Are hollow slots removed or marked as suppressed?
- In tuning / stress / wizard mode, does the visible route field stay broad enough to continue the real work instead of collapsing into one narrow story?

Pass signs:
- every option names a real next move
- removal test shows most slots are load-bearing
- boot path or blocked state is visible when needed
- main route field includes the broad visible lane set or explicitly explains why a lane was not run

Fail signs:
- count-shaped menu with hollow slots
- decorative options with no execution mapping
- all-of-the-above bundles differ only cosmetically
- the follow-up block is too narrow to continue the broader campaign

### 5. Hygiene and security separation
Questions:
- Is hygiene/security separate from the main follow-up block?
- Does it surface only when relevant, except in explicit tuning mode?
- Are real red flags named plainly?

Pass signs:
- clear separate block
- real blocked or risky surfaces are named directly
- no unnecessary runtime inventory flood in normal outputs

Fail signs:
- safety gets buried in creative prose
- hygiene/security leaks into every answer without reason
- blocked paths are silently omitted rather than marked

### 6. Routing adaptability
Questions:
- Does the packet treat model family, launcher path, and answer role as separate things?
- Does it route around blocked launchers instead of looping on them?
- Does it keep alternative live paths visible where warranted?
- Does it use background remediation for sticky failures instead of stalling the foreground packet?
- Does it emit both a runtime registry and a lane-resolution artifact so omissions are explicit rather than silent?

Pass signs:
- runtime registry used: `live`, `blocked`, `untried this pass`, `diagnostic only`
- blocked or hanging launchers are not repeatedly retried in the same pass
- direct worker path and audit path are chosen on usefulness, not mythology
- slow failing lanes can be pushed to background remediation while the main packet continues
- `lane_resolution.json` or equivalent explicitly says which visible lanes ran, which were blocked, and which stayed controller-local with explanation

Fail signs:
- one broken launcher consumes the whole pass
- launcher existence is mistaken for importance
- hierarchy is frozen before bounded comparison excludes alternatives
- the controller waits on a lane that should have been backgrounded or bypassed
- visible lanes disappear without an explicit lane-resolution record

### 7. Stochastic exploration usefulness
Questions:
- Was any randomness bounded and useful?
- Did random worker/audit selection increase coverage or drift detection?
- Did the run stay legible even with some randomness?

Pass signs:
- default path remains clear
- alternate model/audit sampling is bounded and explained
- randomness helps catch stale assumptions or collapse

Fail signs:
- randomization is decorative noise
- the packet becomes unreproducible or opaque
- default path disappears into roulette

### 8. Wiki + skill + evolution follow-through
Questions:
- Were real lessons captured into the wiki?
- Was a relevant skill patched if the failure mode was procedural?
- Were traces preserved for self-evolution if rich enough?

Pass signs:
- long-form lesson lands in the wiki
- procedural fix lands in a skill when needed
- trace/rubric pair exists for later self-evolution

Fail signs:
- everything stays trapped in chat
- memory carries what should be in wiki or skill
- self-evolution is discussed but no trace/rubric pair is captured

## Iterative council loop rubric
Use when the first audit says the answer still collapsed too much or missed a real challenge.

Allowed loop shape:
1. first worker pass
2. first audit
3. recall key voices or models
4. second audit
5. stop or one final bounded round

Rules:
- cap at 2-3 rounds unless the user explicitly asks for more
- each extra round must name why it exists
- later rounds may feed one voice's reply into another voice if that comparison is the point
- preserve first-round receipts; do not overwrite them
- stop when another round would mostly repeat the same shape

## Launcher usefulness gate
A launcher stays in the active stack only if it earns one of:
- unique capability
- materially better reliability
- materially better throughput
- materially better ergonomics for a real packet

Otherwise classify it as:
- `diagnostic only`
- `secondary`
- or `blocked`

Important nuance:
- underintegrated is not the same as useless
- if a launcher has plausible unique value, give it one bounded integration packet before hard demotion
- if that packet still does not show distinct value, stop centering it

Do not repair a launcher only because it exists.

## Suggested score labels
- `strong`
- `usable with gaps`
- `rough but informative`
- `blocked for this packet`

## Minimal packet report
For each packet, record:
- worker family used
- audit family used
- runtime registry snapshot
- strongest surviving narrative
- strongest surviving pushback
- what changed after audit or council loop
- what landed in wiki/skills

Related notes:
- [[hermes-subagent-stress-and-adaptive-routing-plan-2026-04-21]]
- [[active-plans]]
- [[skills-and-agent-rules]]

Write mode: controller-maintained.
