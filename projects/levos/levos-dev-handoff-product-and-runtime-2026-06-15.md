---
title: LevOS Developer Handoff — Product and Runtime Frame 2026-06-15
created: 2026-06-15
updated: 2026-06-15
type: handoff
status: sendable framing draft / not repo contract
claim_ceiling: product and architecture framing; not implementation proof, not market validation, not maintainer acceptance
sources:
  - projects/levos/levos-gpt-webui-idea-ledger-2026-06-15.md
  - projects/levos/levos-gpt-webui-representation-audit-2026-06-15.md
  - /Users/joshuaeisenhart/Desktop/levos_v10.zip
tags:
  - levos
  - developer-handoff
  - product
  - sales
  - runtime
  - openhr
  - openfinance
  - ai-alignment
---

# LevOS Developer Handoff — Product and Runtime Frame 2026-06-15

## One-sentence pitch

LevOS is the governed AI operating system that gives small companies and decentralized communities megacorp-grade intelligence, memory, HR, finance, audit, training, and coordination — under their own control, without turning workers or organizations into surveillance objects.

## Short sales pitch

LevOS turns intent into action, action into receipts, receipts into memory, memory into a graph, and the graph into cheaper, safer intelligence.

It is not just an LLM wrapper, HR app, finance app, RAG app, workflow builder, or employee monitoring tool. It is a governed run fabric for people, companies, agents, and communities.

Companies get:

- a shared company brain;
- lower AI cost through routing, memory, and context reuse;
- safer agent execution through policy gates and human approvals;
- durable decision and work memory;
- OpenHR career development and skill proofs;
- OpenFinance peer repair of bottlenecks;
- P2P audit and mentoring networks;
- cross-company proof sharing without raw-data surrender.

The promise:

```text
frontier intelligence under your control, at non-frontier cost
```

## What LevOS is at the runtime level

LevOS should be understood as a semantic-control operating system for nested organizational dictionaries and proof graphs.

A company, family, guild, coop, or community is:

```text
versioned dictionary + typed graph + policy gates + proof receipts + human/agent runtime
```

The Lev-native ownership map remains:

```text
FlowMind        -> control, policy, semantic target declarations
Orchestration   -> scheduling, fanout, retries, lifecycle traversal
Exec            -> provider/runtime dispatch and backpressure
Graph           -> state, knowledge, projections, lineage, graph operations
Event Bus       -> causality/audit spine and replay
Semantic Control -> admit/rework/reject candidate effects through proof/eval/receipt
AgentPing       -> human approval/escalation/progress surface
AgentLease      -> scoped authority, privacy, sensitive-material access, PII, files, browser, finance views
Memory          -> durable context across episodic/semantic/procedural/temporal/working layers
World-Model     -> admissibility/materiality/surprise gating so compute scales with meaningful change
```

## Why this matters for AI alignment

AI naturally compresses. It wants one model, one context, one score, one identity graph, one optimization target. Used badly, it becomes a central-planning engine that collapses human local knowledge, hidden talent, divergent groups, private context, and plural futures into one legible control surface.

LevOS should align AI by changing the substrate:

```text
model output is not truth
model output is a proposal / observation / candidate action
candidate actions need evidence, policy, leases, human approval when needed, receipts, and semantic admission
```

The alignment target is not one global humanity-vector. It is many human and organizational carriers preserving sovereignty while finding temporary shared action-vectors through proofs and translation.

Good line:

```text
LevOS aligns AI with humanity by making AI serve decentralized human potential instead of centralized human control.
```

## The deep product primitive: definitions

Every organization is a dictionary with enforcement.

An org controls perception by controlling definitions:

- what counts as work;
- what counts as value;
- what counts as skill;
- what counts as failure;
- what counts as trust;
- what counts as money;
- what counts as contribution;
- what counts as authority;
- what counts as done;
- who counts as qualified;
- what counts as proof.

LevOS should make those dictionaries explicit, versioned, auditable, forkable, and interoperable.

```text
wiki    = human-readable dictionary
graph   = machine-readable dictionary
receipt = proof a definition was applied
gate    = rule for admitting a new definition or graph claim
veto    = right to reject a dictionary update
fork    = right to exit or branch a dictionary
```

Leviathan power is definition power. LevOS decentralizes that power.

## Core technical object model

```ts
type ContextId = string;
type SubjectId = string;
type ClaimId = string;
type ProofId = string;
type ReceiptId = string;
```

### Dictionary

```ts
type Dictionary = {
  id: string;
  ownerId: SubjectId;
  scope: "person" | "family" | "team" | "company" | "guild" | "community" | "network";
  version: string;
  terms: TermDef[];
  roles: RoleDef[];
  metrics: MetricDef[];
  policies: PolicyDef[];
  proofRules: ProofRule[];
};

type TermDef = {
  term: string;
  context: ContextId;
  definition: string;
  evidenceRequired: ProofRule[];
  visibility: "private" | "team" | "company" | "network" | "public";
  parentTerms?: string[];
  conflictsWith?: string[];
};
```

### Claim / proof / receipt

```ts
type Claim = {
  id: ClaimId;
  subjectId: SubjectId;
  context: ContextId;
  predicate: string;
  value: unknown;
  visibility: Visibility;
  evidenceRefs: ProofId[];
  status: "draft" | "proposed" | "admitted" | "rejected" | "parked" | "expired" | "disputed";
  createdBy: SubjectId;
  expiresAt?: string;
};

type Proof = {
  id: ProofId;
  claimId: ClaimId;
  proofType:
    | "human_attestation"
    | "peer_audit"
    | "document"
    | "work_artifact"
    | "financial_view"
    | "llm_eval"
    | "test_result"
    | "zk_proof"
    | "signature";
  issuerId: SubjectId;
  artifactRefs: string[];
  confidence?: number;
  limitations?: string[];
};

type Receipt = {
  id: ReceiptId;
  claimId: ClaimId;
  action: "admit" | "reject" | "park" | "revoke" | "appeal" | "expire";
  reason: string;
  proofRefs: ProofId[];
  decidedBy: SubjectId | "semantic_control";
  timestamp: string;
};
```

### Visibility

```ts
type Visibility =
  | "private"
  | "draft"
  | "team"
  | "company"
  | "peer_circle"
  | "network_proof"
  | "public";
```

Rule:

```text
share proofs by default; share raw data only by explicit lease and context
```

## Product law: company brain, not company panopticon

LevOS should remember work, not spy on private cognition.

Private-by-default:

- personal notes;
- draft prompts;
- career fears;
- outside job interest;
- exploratory thinking;
- raw sensitive material.

Shareable after promotion/admission:

- decision receipts;
- work artifacts;
- customer-impacting claims;
- project state;
- approved skill claims;
- audit results;
- scoped finance views.

Staff-facing promise:

```text
LevOS protects and amplifies your work. It does not imprison your mind.
```

## OpenHR

OpenHR is employee-aligned career intelligence, not normal HR surveillance.

Graph split:

```text
Personal Career Graph -> worker-owned, private by default
Company Work Graph    -> company-owned work state and receipts
OpenHR Market Graph   -> federated selective-proof market across companies
```

Worker benefits:

- skill discovery;
- career pathing;
- promotion packet creation;
- internal mobility;
- training paths;
- market options kept open;
- proof of contribution;
- protection against credit theft or manager memory drift.

Company benefits:

- better retention;
- better talent allocation;
- lower hiring cost;
- faster onboarding;
- better training ROI;
- less hidden skill waste.

Best line:

```text
OpenHR keeps your options open — including inside your current company.
```

## OpenFinance

OpenFinance is selective vulnerability coordination, not open-all-books transparency.

The primitive is the five-family repair circle:

```text
Five families rotate through one house at a time.
They clean, repair, organize, teach, and maintain together.
All five houses become cleaner and more stable with less isolated effort.
```

The SME version:

```text
Five companies rotate through one company's bottleneck at a time:
books, cashflow, hiring, sales, onboarding, AI workflow, compliance, training.
```

Rule:

```text
Expose weakness only to the circle that can repair it.
Expose proof outward only after repair.
```

OpenFinance graph objects:

```ts
type NeedClaim = {
  subjectId: SubjectId;
  context: ContextId;
  needType:
    | "cashflow"
    | "bookkeeping"
    | "tools"
    | "labor"
    | "training"
    | "process"
    | "sales"
    | "maintenance"
    | "audit"
    | "mentoring";
  description: string;
  visibility: "private" | "peer_circle" | "network_proof";
  evidenceRefs: ProofId[];
  requestedHelp: string[];
};

type CapacityClaim = {
  subjectId: SubjectId;
  context: ContextId;
  capacityType:
    | "cash"
    | "skill"
    | "tools"
    | "space"
    | "labor"
    | "mentor_time"
    | "audit_capacity";
  availability: string;
  proofRefs: ProofId[];
};

type RepairSession = {
  id: string;
  circleId: string;
  targetId: SubjectId;
  needRefs: ClaimId[];
  helperRefs: SubjectId[];
  workDoneRefs: ProofId[];
  beforeAfterRefs: ProofId[];
  followupDate: string;
};
```

Best line:

```text
OpenFinance is how weakness becomes a shared work queue instead of a private failure.
```

## P2P audit and mentoring

Equivalent peers audit equivalent peers:

```text
workers audit workers
managers audit managers
CFOs audit CFOs
founders audit founders
bosses mentor bosses
companies audit companies
communities audit communities
```

Loop:

```text
weakness exposed -> peer audit -> mentor/training assigned -> repair work -> receipt -> graph update
```

This gives decentralized systems one of the powers of centralized systems — institutional learning — without central ownership of all raw data.

## SME and community network thesis

Megacorps win because they internalize capacity:

```text
HR + finance + legal + procurement + analytics + AI + training + institutional memory + management layers
```

SMEs and communities can compete if LevOS lets them federate capacity:

```text
local sovereignty
+ shared proof graph
+ shared AI context
+ peer auditing
+ OpenHR
+ OpenFinance
+ mentoring/training
+ business/community mesh
= decentralized megacorp capability
```

Best line:

```text
LevOS gives small companies a megacorp-grade brain without forcing them to become a megacorp.
```

Civilization line:

```text
LevOS lets decentralized communities coordinate like empires without becoming empires.
```

## Frontier intelligence without frontier costs

The intelligence is not only the model. It is:

```text
model + context graph + memory + tools + evals + receipts + policy + human approval + routing
```

LevOS should route cognition:

```text
local/small models -> extraction, classification, summaries, routine drafting
mid models         -> normal analysis and workflow help
frontier models    -> rare high-risk, high-surprise, high-leverage decisions
sim/proof engines  -> verification, counterexamples, formal checks
humans/peers       -> approval, audit, veto, repair
```

Cost principle:

```text
compute scales with material surprise, not with chat volume or a polling clock
```

## Codex Ratchet / spinor freedom link

The public vector is the institution's view. It is a quotient readout, not the person/company/community.

Freedom-preserving LevOS should treat each person/org/community as a local carrier with private graph, path history, hidden phase, local dictionary, and contextual claims. Public scores, credentials, roles, and KPIs are only quotient readouts.

Rule:

```text
never confuse the quotient with the carrier
```

This is why Codex Ratchet matters: it supplies the discipline that blocks premature quotient-collapse, false merges, and public-vector tyranny.

## Wizard's role

Wizard should become a LevOS council/policy/skill layer.

```text
Wizard thinks and guards.
LevOS runs and records.
Codex Ratchet tests and adjudicates.
Leviathan governs human coordination.
```

Wizard contributes:

- parent/child role separation;
- councils;
- anti-collapse audit;
- strict gate + wide explorer;
- simulation-run discipline;
- fresh-audit separation;
- follow-up and context-handling discipline.

LevOS contributes:

- real runtime;
- graph state;
- permissions/leases;
- human approvals;
- provider execution;
- receipts;
- productizable surfaces.

## MVP wedge

Do not start with the whole civilization product. Start with a concrete business wedge:

### MVP 1 — AI Gateway + Company Second Brain

- staff use LLMs through LevOS;
- private drafts remain private;
- promoted work becomes candidate company memory;
- important actions get receipts;
- model routing controls cost;
- company graph stores decisions/artifacts.

### MVP 2 — Dictionary + Semantic Control

- explicit company terms/roles/metrics/policies;
- claim/proof/receipt graph operations;
- admit/reject/park workflow;
- no LLM output becomes truth without admission.

### MVP 3 — OpenHR

- worker career graph;
- skill claims;
- promotion packets;
- internal mobility;
- employee-controlled visibility.

### MVP 4 — OpenFinance

- peer-circle need/capacity graph;
- selective finance/resource views;
- repair sessions;
- before/after receipts.

### MVP 5 — Cross-company network

- portable credentials;
- vendor proofs;
- peer audit;
- boss-to-boss mentoring;
- company-to-company repair graph.

## Non-negotiable invariants

1. No global human score.
2. No raw surveillance by default.
3. No semantic merge without context.
4. Any live distinguishing witness blocks merge.
5. Private drafts are not company memory.
6. LLM outputs are proposals, not truth.
7. Proofs travel farther than raw data.
8. Weakness exposure is scoped to repair circles.
9. Workers control personal career graph visibility.
10. Companies own company memory but not worker interiority.
11. Peer audit is role-equivalent wherever possible.
12. Every admitted claim has receipt/provenance.

## Best taglines

```text
Frontier intelligence, under your control.
```

```text
The company brain that safely runs AI work.
```

```text
Megacorp intelligence for small companies.
```

```text
A company brain, not a company panopticon.
```

```text
OpenFinance lets small groups pool truth before they pool money.
```

```text
LevOS decentralizes definition power.
```

```text
LevOS performs coordination without collapse.
```

## One paragraph sendable pitch

LevOS is the governed AI operating system for companies and communities. It gives every organization a shared brain: a graph of people, work, documents, decisions, finances, skills, audits, AI interactions, and receipts. Unlike normal AI tools, LevOS does not just answer prompts. It routes intent, assembles context, chooses the right model, gates sensitive actions, asks humans for approval, records proof, updates memory, and makes the result replayable. For SMEs, this creates megacorp-grade intelligence without megacorp overhead. For workers, it creates a private career graph and proof of contribution without turning work into surveillance. For networks of companies, it creates OpenHR, OpenFinance, peer audit, mentoring, and selective proof-sharing so decentralized businesses and communities can coordinate like empires without becoming centralized empires. The promise is simple: frontier intelligence, under your control, at non-frontier cost.
