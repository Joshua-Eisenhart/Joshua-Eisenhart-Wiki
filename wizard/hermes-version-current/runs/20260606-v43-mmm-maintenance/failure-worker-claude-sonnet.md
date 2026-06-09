# Failure Worker — Claude Sonnet High

```text
modelUsage: {'claude-haiku-4-5-20251001': {'inputTokens': 1074, 'outputTokens': 20, 'cacheReadInputTokens': 0, 'cacheCreationInputTokens': 0, 'webSearchRequests': 0, 'costUSD': 0.0011740000000000001, 'contextWindow': 200000, 'maxOutputTokens': 32000}, 'claude-sonnet-4-6': {'inputTokens': 3, 'outputTokens': 3871, 'cacheReadInputTokens': 16298, 'cacheCreationInputTokens': 16630, 'webSearchRequests': 0, 'costUSD': 0.12532590000000002, 'contextWindow': 200000, 'maxOutputTokens': 32000}}
session_id: 88bec708-1dc6-4697-8729-3105dcc11619
subtype: success
```

I don't have filesystem tools in this interface — only MCP connectors. Working from the decision summary provided inline.

```yaml
council: Failure Council
subcouncils_covered:
  - failure.premortem
  - failure.falsifier_route_truth
  - failure.regression_safety

mmm_l0_ref: voice-mini-mmm-saliency-calibration/references/wizard-3x3-mmm-saliency-alignment.md
mmm_council_ref: Failure Council
mmm_subcouncil_refs: failure.premortem + failure.falsifier_route_truth + failure.regression_safety

saliency_preload_before_rules: true
which_loaded_slice_changed_output:
  - L0 salience: strongest-falsifier-first rule surfaced Codex Ratchet RED before route claim
  - premortem slice: forced stop-condition check on Codex Ratchet before clean-call was made
  - falsifier_route_truth slice: blocked native delegate_task route; required external fallback receipt

target_claims:
  - id: TC-1
    claim: "v4.3 is the current runtime ('it's 4.3')"
    status: open
    note: v4.3 is formally guard/preflight, not replacement runtime; v4.2 council topology may still be active
  - id: TC-2
    claim: "On-demand template + finite cron + receipt-backed Wizard is correct config"
    status: survived
    evidence: packet validator ok=true post-carrier-patch; wiki probe clean; PEPS3D fields removed
  - id: TC-3
    claim: "Native delegate_task subagents viable"
    status: killed
    evidence: xAI key invalid; route blocked; no receipt returned
  - id: TC-4
    claim: "External Claude Code Sonnet is viable fallback decision worker"
    status: survived
    evidence: ran and returned receipt with modelUsage
  - id: TC-5
    claim: "Codex Ratchet runner is clean/callable"
    status: killed
    evidence: runner RED; must not be called clean; no receipt path available

strongest_falsifiers:
  - rank: 1
    claim_ref: TC-5
    falsifier: Codex Ratchet runner is RED — any route or report calling it clean has no receipt and fails route-truth
    decisive_check: inspect runner status directly before any invocation; absence of GREEN receipt = blocked
  - rank: 2
    claim_ref: TC-1
    falsifier: v4.3 is architecturally a guard/preflight; v4.2 council topology is not confirmed retired
    decisive_check: read v4.3 spec for runtime vs preflight designation; check whether v4.2 council paths are still wired
  - rank: 3
    claim_ref: TC-3
    falsifier: xAI key invalid blocks all native delegate_task subagent spawns; no internal fallback exists
    decisive_check: key validation at spawn time; if blocked, external Claude Code Sonnet is the only receipt-producing route

premortem_findings_mapped:
  likely_failure: >
    v4.3 labeled as runtime while still operating as guard/preflight;
    future turns may treat v4.2 council paths as retired when they are not — silent topology lie
  hidden_assumption: xAI key valid for native delegate_task subagents (falsified; key invalid)
  warning: >
    SALIENCY_TRANCHE_01_CANDIDATE not deduplicated against FULL/COMPACT/mini registry;
    risk of premature canonical promotion before conformance passes
  hardening:
    - Dedup SALIENCY_TRANCHE_01_CANDIDATE before any canonical promotion
    - Patch v4.3 MMM preload into control/template before cron creation
    - Create finite cron after template (default 8 ticks × 45m cadence, matching historical autoloop)
  stop_condition: >
    Do not call Codex Ratchet runner under any route until runner returns GREEN with receipt;
    do not promote SALIENCY_TRANCHE_01_CANDIDATE to canonical until conformance passes

route_truth:
  - route: native delegate_task subagents
    status: BLOCKED
    reason: xAI key invalid
    receipt: none
  - route: external Claude Code Sonnet decision worker
    status: OPEN (viable)
    receipt: returned; contains modelUsage
  - route: Codex Ratchet runner
    status: BLOCKED
    reason: runner RED
    receipt: none

hardened_route:
  primary: external Claude Code Sonnet decision worker (receipt-backed)
  sequence:
    - step: 1
      action: patch v4.3 MMM preload into control/template
      gate: packet validator ok=true (already confirmed post-carrier-patch)
    - step: 2
      action: create finite cron after template (8 ticks, 45m interval)
      gate: cron count=0 confirmed before creation; cron count=1 after
    - step: 3
      action: dedup SALIENCY_TRANCHE_01_CANDIDATE against FULL/COMPACT/mini registry
      gate: conformance pass required before canonical promotion
  blocked_until_green:
    - Codex Ratchet runner (runner RED)
    - native delegate_task subagents (xAI key invalid)

kill_or_open_status:
  - TC-1: open   # v4.3 runtime vs preflight unresolved; needs spec read
  - TC-2: survived # config validated by observable evidence
  - TC-3: killed  # xAI key invalid; route confirmed blocked
  - TC-4: survived # external Sonnet receipt with modelUsage confirmed
  - TC-5: killed  # Codex Ratchet RED; no clean-call permissible

evidence_boundary:
  observed:
    - wiki probe clean; page_count=438
    - cron count=0
    - v4.3 packet validator ok=true (post-carrier-patch)
    - PEPS3D fields removed from packet positive
    - xAI key invalid (native subagent spawn failed)
    - External Claude Code Sonnet returned receipt with modelUsage
    - Codex Ratchet runner status=RED
  not_yet_checked:
    - v4.3 spec: runtime vs preflight designation (TC-1 open pending this)
    - v4.2 council topology: still wired or retired?
    - SALIENCY_TRANCHE_01_CANDIDATE: dedup against FULL/COMPACT/mini registry (conformance unrun)
  canonical_hold: >
    No claim promoted to canonical until TC-1 resolved by spec read
    and SALIENCY_TRANCHE_01_CANDIDATE passes conformance check
```

---

🧙🏽‍♂️ **[lev://mesh]** task-card | 🧨 pressure-mapped | receipt-bounded 🔒

---

**Voices**

🧨 **Popper** — TC-1 (`"it's 4.3"`) is the live risk. Target claim: v4.3 is full runtime. Strongest falsifier: v4.3 spec designates it guard/preflight; v4.2 council topology not confirmed retired. Decisive check: read v4.3 spec for runtime/preflight boundary. Status: `open`.

🦉 **Hume** — Three things were directly observed: Codex Ratchet RED, packet validator ok=true post-patch, xAI key invalid. Everything else is provisional until the v4.3 spec and SALIENCY dedup are run.

🔬 **Feynman** — Procedure: read v4.3 spec → find runtime/preflight designation field → if `preflight_only=true`, TC-1 is killed; if `runtime=true`, TC-1 survived. Pass/fail: presence or absence of that field is the decisive observable.

✂️ **Orwell** — "Surface future work as v4.4 maintenance/object-preservation" is fog. Replace with: "write a note that v4.3 is guard/preflight until spec confirms otherwise."

---

**Lanes**

➡️ **Direct** — `spawn_worker`: read v4.3 spec file, find runtime vs preflight designation, close TC-1 as killed or survived.

🔀 **Alternative** — `controller_local`: skip TC-1 resolution for now; treat v4.3 as guard/preflight conservatively and proceed with hardened_route sequence (step 1 → 2 → 3). Lower risk; defers the spec read.

🏛️ **Systems** — `controller_local`: the xAI key failure + Codex Ratchet RED + TC-1 ambiguity are three simultaneous blocked surfaces — the system is operating on one receipt-producing route (external Sonnet). Single route = single point of failure. Name this as a structural risk.

🧹 **Repo hygiene** — `spawn_worker`: run SALIENCY_TRANCHE_01_CANDIDATE dedup against FULL/COMPACT/mini registry; conformance check before canonical promotion gate.

---

**All compositions**

🔗 **All-A — Close TC-1 + Harden Route**: Read v4.3 spec (➡️ Direct) + dedup SALIENCY candidate (🧹) + confirm Codex Ratchet RED in writing so it can't be called clean (🧨). Three bounded workers; receipt required for each.

🔗 **All-B — Conservative Advance**: Skip TC-1 spec read; treat v4.3 as preflight conservatively (🔀); execute hardened_route steps 1–3 in sequence using external Sonnet as sole receipt-producing route (🏭). Faster; leaves TC-1 open.

🔗 **All-C — Structural Risk First**: Name the single-route structural risk (🏛️); design a second receipt-producing route before advancing steps (🧭 strategy: what's the retreat condition if external Sonnet is blocked?); then proceed with All-A.