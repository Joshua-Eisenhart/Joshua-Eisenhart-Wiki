# Hermes subagent stress + adaptive-routing plan — 2026-04-21

Purpose: hold the current plan for stress-testing the Hermes answer surface and keeping worker routing adaptive as LLMs, launchers, and tool surfaces shift.

Status: active current plan note.

## Bottom line
- Hermes should treat `model family`, `audit family`, and `launcher/runtime path` as separate questions.
- The main stable worker families currently worth stress-testing are:
  - Claude / Sonnet-high
  - Codex / gpt-5.4-high
  - Gemini
- The main strong audit families currently worth using are:
  - Opus high
  - Codex high
- Hermes should not get stuck looping on a broken launcher just because that launcher exists.
- `pi-mono` is not a proved backup route right now.
- `omc`, `omx`, `tmux`, and `mngr` should only stay in the active stack if they earn distinct value beyond the direct worker paths.

## Checked context this plan is using
- Claude-led lane/voice packs are currently producing the cleanest main answer surface when Opus audits them.
- Codex and Opus both work well as audit lanes.
- Hermes already has a wiki offload path and a growing skills layer.
- Hermes already has a self-evolution path that should use real traces instead of taste-only edits.
- The user wants plurality preserved: many narratives, many paths, and many live workers should stay alive until bounded work excludes them.
- Voice use should not collapse into one `🦉 Hume` summary. A voice may be called more than once in the body when the reasoning job genuinely recurs.

## Design rules

### 1. Separate three different things
1. model family
2. launcher/runtime path
3. answer-surface role

Examples:
- Claude can be the worker family even if `tmux` is not the launcher used on that run.
- Codex can be an audit family even if OMX is not part of the main delivery path.
- A runtime path can be blocked while the model family is still available through another route.

### 2. Runtime registry, not launcher faith
Every bounded run should classify each candidate path as one of:
- `live`
- `blocked`
- `untried this pass`
- `diagnostic only`

Do not retry a blocked path repeatedly in the same pass unless a concrete repair changed something.
Do not present a launcher as important just because it exists.

### 3. Adaptive routing rule
Preferred routing policy:
1. choose the strongest direct worker path already proved for the task class
2. choose an audit family independent enough to catch collapse
3. only fall back to alternate launchers if the direct path is blocked or lacks a needed capability
4. if a path fails, mark the reason and route around it for the rest of that pass
5. record the failure shape so a later hygiene/evolution pass can decide whether it deserves repair

### 3.5 Iterative council loop
A packet may run a bounded back-and-forth when the first audit says key voices should answer again.

Rules:
1. first worker pass
2. first audit
3. recall only the key voices or models that matter
4. second audit
5. stop, or at most one more bounded round

Do not erase the first-round receipts.
Later-round workers may read selected earlier voice receipts when cross-voice feedback is the point.
If another round would mostly repeat the same shape, stop.

### 3.6 Stochastic exploration rule
Default paths are useful, but bounded randomness is also useful.

Use it like this:
- Sonnet may stay the main worker by default
- Codex or Gemini may be sampled sometimes as worker paths
- Opus may stay the main audit path by default
- Codex may sometimes audit instead
- every sampled path must be recorded in the packet report
- randomness should serve coverage, drift detection, or anti-collapse testing, not decoration

### 3.65 Background-remediation rule
If a sampled lane is slow, hanging, or repeatedly failing:
1. stop waiting on it in the foreground packet
2. mark it `blocked`, `diagnostic only`, or `background remediation`
3. route around it with a live alternate path immediately
4. if the issue still looks worth understanding, push the failing lane into a background remediation runner
5. process the background result only when it finishes; do not stall the main packet on it

This keeps stress-testing alive without letting one sticky failure consume the whole controller.

### 3.7 Usefulness gate for launchers
Do not keep a launcher in the active stack just because it exists.
A launcher should earn its keep through one of:
- unique capability
- better reliability
- better throughput
- better ergonomics for a real packet

If it does not, classify it as secondary, diagnostic only, or blocked.

Important nuance:
- `not currently useful` is not always the same as `useless`
- a path may be underintegrated rather than inherently weak
- if a launcher has plausible unique value, give it one bounded integration packet before demoting it hard
- if that bounded packet still does not show distinct value, stop centering it

### 4. Stress-test packets
Stress tests should be bounded packets, not one giant blended run.
Useful packets:
1. body-voice fidelity
2. follow-up integrity
3. council/pushback survival
4. cross-model divergence preservation
5. runtime health / launcher routing
6. wiki offload + retrieval continuity
7. skill loading + skill usefulness
8. trace capture for self-evolution

### 5. Hygiene scope rule
Runtime-health checks belong in hygiene only when:
- the output is explicitly about routing/runtime health, or
- a blocked path materially changes the answer surface, or
- a real red flag should change what the user does next

Do not force a full runtime inventory into every output.

### 6. Wiki rule
The wiki should hold:
- current routing policy
- current stress-test plan
- checked vs open path status
- normalization targets for what should move into skills
- trace-backed lessons that are too detailed for injected memory

The wiki should not become a raw dump of every run.
Use it as the long-form control surface and continuity spine.

### 7. Skill + evolution rule
After a meaningful stress-test pass:
1. capture the traces/artifacts
2. decide what belongs in wiki vs skill vs memory
3. patch the affected skill if the failure mode is procedural
4. use self-evolution only against real trace/rubric pairs
5. rerun one bounded packet to verify the patch actually helped

### 8. Plurality / Zhuangzi rule
- Keep multiple live narratives until bounded work excludes them.
- Do not flatten `Claude main / Gemini side-run / Codex audit / Opus audit` into one permanent hierarchy too early.
- If two or more readings still survive, keep them visible.
- The same voice may recur more than once in the body if it is doing different jobs at different moments.
- A council is not a list of labels; it is preserved difference under bounded synthesis.

## Current practical direction
- Main worker default: Claude / Sonnet-high
- Main audit default: Opus high
- Side audit / adversarial audit: Codex high
- Parallel alternative worker: Gemini
- Bounded stochastic exploration is allowed:
  - Sonnet remains the clear default worker
  - Codex or Gemini may be sampled sometimes as workers
  - Opus remains the clear default auditor
  - Codex may sometimes audit instead
- Launchers like `omc`, `omx`, `tmux`, `mngr` stay secondary until they prove distinct routing value
- `pi-mono` remains non-routable until a real backup path is proved

## Latest bounded packet
- Packet: `wizard_loop_002`
- Artifacts: `/tmp/subagent-format-harness/packets/wizard_loop_002/`
- What happened:
  - sampled Gemini worker succeeded
  - parallel default Sonnet worker succeeded
  - sampled Codex audit path hung / produced no audit artifact
  - the controller routed around it immediately with a Sonnet fallback audit
  - Hume / Popper / Zhuangzi recall then ran
  - Opus closed the packet with `final_opus.md`
- Main lesson:
  - adaptive routing worked when the packet stopped waiting on the broken sampled audit lane and substituted a useful live path
  - plural synthesis remained partial but honest

## Next bounded moves
1. use the stress-test rubric note for the answer surface:
   - `[[hermes-answer-surface-stress-rubric-2026-04-21]]`
   - body voice
   - council survival
   - pushback honesty
   - follow-up quality
   - hygiene separation
   - routing adaptability
2. patch the harness so each run records a runtime registry:
   - live / blocked / untried / diagnostic only
3. run one bounded cross-model packet:
   - Sonnet worker
   - Gemini worker
   - Opus audit
   - Codex audit
4. offload the resulting lessons into:
   - this wiki note
   - the affected skills
   - self-evolution inputs if the traces are rich enough

Related notes:
- [[active-plans]]
- [[skills-and-agent-rules]]
- [[hermes-memory-offload]]
- [[handoffs/hermes-runtime-subagent-handoff-2026-04-20]]

Write mode: controller-maintained.
