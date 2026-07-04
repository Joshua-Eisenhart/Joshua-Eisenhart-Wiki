---
title: Zip Agent Protocol
created: 2026-07-02
target_path: /Users/joshuaeisenhart/wiki/projects/leviathan-current/ZIP_AGENT_PROTOCOL_2026-07-02.md
status: fallback-written-from-codex-ratchet-sandbox
claim_ceiling: protocol formalization from local legacy/current docs; not a new runtime implementation
tags: [zip-agent, mesh, lev, codex-ratchet, gateable-work-packet]
---

# Zip Agent Protocol - 2026-07-02

This page revives the older ZIP-agent primitive as the mesh work-packet unit between code-based and LLM-based systems. A Zip Agent is a self-contained, content-addressed artifact bundle that can be loaded by a code runner or an LLM worker, run without interactive chat state, and returned as a full artifact bundle with receipts, not just prose.

The requested wiki path is outside the writable sandbox for this run, so this fallback file is the authored spec.

## Source Receipts

Sharpest original statements found:

> "ZIPs are treated as deterministic, chatless subagents."

Source: `READ ONLY Legacy core_docs/a2_runtime_state archived old state/A2_WORKING_UPGRADE_CONTEXT_v1.md`

> "ZIPs are immutable."
> "Each ZIP is a complete world-state snapshot."
> "ZIPs can be dropped into a fresh thread and used immediately."

Source: `READ ONLY Legacy core_docs/a2_runtime_state archived old state/A2_WORKING_UPGRADE_CONTEXT_v1.md`

> "Constantly bringing everything back to a zip that can be loaded into any llm and run."

Source: `READ ONLY Legacy core_docs/ultra high entropy docs/txt/GPT 12_29 pro plan vs browser crashes.md.txt`

> "Purpose: \"ZIPs are deterministic, chatless subagents\"; \"ZIPs are atomic (never split)\"; \"ZIP ingestion is a single-line deterministic action\"."

Source: `READ ONLY Legacy core_docs/upgrade docs/DIRECTED_EXTRACTION_ANSWERS_v2.md`

> "ZIP never splits; docs inside ZIP shard."

Source: `READ ONLY Legacy core_docs/upgrade docs/DIRECTED_EXTRACTION_ANSWERS_v2.md`

> "Keeping them separated--via the zipped sub-agent protocols you mentioned--lets the system refine entropy step-by-step rather than mixing levels."

Source: `READ ONLY Legacy core_docs/a2_feed_high entropy doc/branchthread extract chat gpt.txt`

The most formal old skeleton appears in `system_v4/a1_state/A1_GRAPH_PROJECTION.json`: `ZIP_HEADER.json`, `MANIFEST.json`, `HASHES.sha256`, eight zip-type enums, monotone sequence replay, gap parking, deterministic-output rule, and reject tags.

## Current Cross-Links

- Mesh protocol: `/Users/joshuaeisenhart/wiki/projects/leviathan-current/MESH_NODE_PROTOCOL_V0_2026-07-02.md`
- Gate doctrine: `/Users/joshuaeisenhart/wiki/projects/leviathan-current/GATE_DOCTRINE_ADMISSIBILITY_NOT_QUALITY.md`
- Constraint-core tier state: `/Users/joshuaeisenhart/wiki/projects/constraint-core/RATCHET_STATE_BY_TIER_2026-07-02.md`
- Constraint-core lineage: `/Users/joshuaeisenhart/wiki/projects/constraint-core/LINEAGE_AND_VERDICTS_2026-07-02.md`
- Eval-pack outbox: `/Users/joshuaeisenhart/wiki/projects/leviathan-current/lev-eval-packs-outbox-20260702.zip`
- Bootpack extraction: in progress; strongest extracted skeleton is in `system_v4/a1_state/A1_GRAPH_PROJECTION.json` under `zip_protocol_v2_contract`.

## Definition

A Zip Agent is a deterministic, chatless, substrate-independent work packet.

It is "agent" because it carries everything needed to perform a bounded task: instructions, forms, schemas, references, nested sub-agent packets, tests/falsifiers, return contract, and claim ceiling. It is "zip" because the whole unit is atomic, content-addressed, sharded internally, and returned as an artifact bundle.

It is not a conversation transcript, a loose prompt, a one-off JSON result, or a trust transfer. The receiving node still verifies through its own gates.

## Anatomy

Minimum Zip Agent layout:

```text
ZIP_HEADER.json
MANIFEST.json
HASHES.sha256
FORMS/
PROMPTS/
REFERENCES/
SUBAGENTS/
SCRIPTS/
SCHEMAS/
TESTS/
RECEIPTS/
RETURN_CONTRACT.json
CLAIM_CEILING.md
README.md
```

`ZIP_HEADER.json` declares protocol version, zip type, source layer, target layer, run id, sequence, created time, compiler version, parent packet hash when nested, and manifest hash.

`MANIFEST.json` lists every member with relative path, byte size, sha256, role, required/optional status, and execution substrate hints.

`HASHES.sha256` is the simple line-oriented integrity surface for all members.

`FORMS/` carries structured inputs, expected observations, adapter forms, gate forms, and witness forms.

`PROMPTS/` carries LLM-readable task prompts. These are packet-local and must not depend on prior chat state.

`REFERENCES/` carries bounded source slices. References can include pointers to external content, but any load-bearing source used by the executor must be content-addressed or quoted into a bounded reference file.

`SUBAGENTS/` carries zips-in-zips. A child packet has its own header, manifest, hashes, return contract, claim ceiling, and receipts. Parent prompts may launch child packets, but parent synthesis cannot count a child as complete until the child return bundle validates.

`SCRIPTS/` carries deterministic code runners, validators, adapters, or replay scripts.

`SCHEMAS/` carries JSON Schema, Zod, TypeScript, Python dataclass, or equivalent shape contracts for input and return artifacts.

`TESTS/` carries positive checks, negative controls, mutation probes, and hostile fixtures.

`RECEIPTS/` starts empty or contains prior source receipts. Returned packets append execution receipts here.

`RETURN_CONTRACT.json` declares exactly what must come back: files, schemas, receipt paths, pass/block vocabulary, content addresses, and allowed claim rungs.

`CLAIM_CEILING.md` states the maximum claim the packet can earn, such as `exists`, `runs`, `passes fresh local rerun`, `mutation-proven load-bearing`, or `admitted by declared gate`.

## Load-Bearing Property 1: Chatless

CHATLESS means execution cannot depend on hidden conversational memory, interactive clarification, or state not present in the packet.

Required consequences:

- A fresh thread can load the packet and run it.
- A code runner can validate and execute the packet without an LLM.
- An LLM can read the packet and return the required schema without back-and-forth.
- A replay runner can compare outputs against the same manifest and inputs.
- Any missing source, ambiguous task, or schema mismatch blocks or parks the packet instead of being repaired from memory.

Why it matters: chatless packets are gateable. Interactive chat drifts; packet contents can be hashed, replayed, diffed, rejected, signed, and re-run.

## Load-Bearing Property 2: Substrate-Independent

SUBSTRATE-INDEPENDENT means the same packet has a dual execution contract:

1. Code path: deterministic runner consumes `ZIP_HEADER.json`, `MANIFEST.json`, `SCHEMAS/`, `SCRIPTS/`, `TESTS/`, and source files; emits machine receipts and a return bundle.
2. LLM path: LLM worker consumes `PROMPTS/`, `FORMS/`, `REFERENCES/`, `SCHEMAS/`, `CLAIM_CEILING.md`, and `RETURN_CONTRACT.json`; emits schema-conforming artifacts and a return bundle.

The paths must converge on the same return schema and claim ladder, but they do not need identical internal reasoning. Code can be the executor and LLM the proposer, or LLM can be the bounded worker and code the validator. Either way, admission belongs to deterministic gates.

Dual execution contract:

```json
{
  "input": "same manifest and source addresses",
  "code_executor_must": ["validate shape", "run scripts/tests", "emit receipts", "block on missing data"],
  "llm_executor_must": ["use only packet-local context", "fill declared forms", "cite packet sources", "emit return schema"],
  "both_must": ["preserve content addresses", "state claim ceiling", "return a bundle", "never self-promote"]
}
```

## Composition With MeshSignedBundleV0

MeshSignedBundleV0 is the signature layer over the Zip Agent, not a replacement for it.

Zip Agent owns packet anatomy, execution contract, nested sub-agent structure, internal hashes, and return schema.

MeshSignedBundleV0 should own signer identity, public-key or host-key binding, signature over canonical manifest bytes, optional transparency log reference, and receiving-node verification metadata.

This matches current mesh doctrine: sovereign machines exchange content-addressed artifacts; receiving nodes verify through their own gates; peer witness is not authority transfer.

Recommended layering:

```text
MeshSignedBundleV0
  signed_manifest_hash
  signer_ref
  signature
  signature_scope
  transparency_or_receipt_ref
  payload: ZipAgentV0.zip
```

Unsigned Zip Agents can exist as local scratch packets. Cross-node packets should be signed or host-anchored when they can affect admission, graph residency, or upstream patch flow.

## Composition With Evaluator Packs

A Lev evaluator/witness pack is a resident Zip Agent when it has:

- manifest or eval yaml;
- prompts or observation instructions;
- schemas and fixtures;
- companion sensor/script;
- gate policy;
- tests and negative controls;
- receipt/claim ceiling.

The current CR sim evaluator packs already match the pattern: external sims emit provider evidence; packs consume lane records; deterministic sensors compute measurements; gate policies decide; tests include pass and hostile false-green cases. The gap is packaging discipline: the pack directory is zip-agent-shaped, but it is not always returned as a full return zip with receipts.

## Current Instantiation Map

| OG property | Current instance | Gap |
|---|---|---|
| Atomic carrier, never split | `ZIP_JOB` concept in `A1_GRAPH_PROJECTION.json`; current patch/eval outbox zips | Current dispatch often returns JSON lines or patch files, not a full return bundle. |
| Self-describing manifest | Eval packs use `*.eval.yaml`, policies, fixtures, tests; old skeleton uses `ZIP_HEADER.json` and `MANIFEST.json` | No single cross-surface Zip Agent manifest schema yet. |
| Internal sharding | Old rule: zip never splits; docs inside shard | Current packs use dirs/fixtures, but shard roles are implicit. |
| Chatless fresh-thread load | `codex exec --sandbox read-only` style dispatch; prompt file -> structured JSON; Wizard packet validation | LLM outputs can still rely on prompt wording and stdout unless wrapped in a return bundle. |
| Sub-agent nesting | Wizard subagent/subsubagent packet practices and mini-MMM route packets | Nested packet return validation is weaker than the old zips-in-zips idea. |
| Deterministic ingestion action | Old "single-line deterministic action"; current adapters validate provider evidence | Current ingestion is per-surface, not one Zip Agent loader. |
| Return results/failure as packet | Old `SIM_RESULTS_ZIP` / `SIM_FAILURE_ZIP`; Mesh returns findings/patches/receipts | Current return path is mostly JSON, patches, or markdown receipts, not a full artifact bundle. |
| Claim ceiling | Current Gate Doctrine and Mesh Node Protocol status ladders | Many artifacts carry ceilings, but enforcement is uneven outside gate-owned packs. |
| Content addressing | Mesh Node Protocol, provider evidence content addresses, `HASHES.sha256` skeleton | Need canonical zip-level address plus per-member addresses. |
| Code/LLM duality | FlowMind/exec/eval packs: declarations, prompts, schemas, companion sensors | Need an explicit dual execution contract per packet. |
| Signature/host anchor | MeshSignedBundleV0 concept; host-signature repair pressure in Lev ClaimGate | Signature layer not yet consistently bound to every cross-node work packet. |

Instantiations mapped: 11. Gaps: 11.

## Current Instances In Plain Terms

`codex-exec dispatch`: prompt file plus bounded context asks a model to return structured JSON. This is chatless in spirit, but usually stdout/JSON-only on return. Add manifest, content addresses, and return-zip discipline.

`lev evaluator/witness packs`: self-contained load-and-run directories with manifest, fixture, sensor, policy, and tests. A pack is already a resident Zip Agent when it can validate and emit receipts locally.

`data-only carriers`: `packet.json` plus scripts, such as Wizard v4.3 object-preservation packets, are thin Zip Agents. They have the form and validator; add manifest, hashes, return bundle, and nested child packet convention.

`constraint_core bundle exchange`: scratch/hypothetical zip lineage and two-lane status surfaces already preserve no-promotion ceilings. These are Zip Agent candidates when each bundle contains harness, receipts, source addresses, and return contract.

`outbound kit`: patch/eval outbox zips already function as cross-node artifact carriers. Add the standard header/manifest/return-contract and receiver-return bundle.

`MeshSignedBundleV0`: the signed zip-agent envelope. It should sign the canonical manifest and bind signer/host/receipt metadata while leaving admission to receiver gates.

## Revival Plan

1. Define `ZipAgentV0` manifest schema with `ZIP_HEADER.json`, `MANIFEST.json`, `RETURN_CONTRACT.json`, `CLAIM_CEILING.md`, member roles, hashes, and nested packet refs.
2. Add a loader/validator that can run `zip-agent validate <zip>` and return deterministic reject tags: missing manifest, hash mismatch, schema mismatch, undeclared reference, stale source, bad sequence, unsupported zip type, missing return contract, overclaim ceiling, unsigned-cross-node packet.
3. Wrap current `codex exec` prompt dispatches in ZipAgentV0: prompt and forms in, return bundle out. Keep stdout as a convenience projection only.
4. Treat evaluator packs as resident Zip Agents: add generated `ZIP_HEADER.json`, `MANIFEST.json`, and `RETURN_CONTRACT.json` to shipped packs or package them during export.
5. Require return-zip discipline for cross-node packets: receiver returns `RETURN_HEADER.json`, receipts, changed artifacts, rejected cases, findings, and a manifest of outputs.
6. Layer MeshSignedBundleV0 over cross-node Zip Agents once the manifest is canonical.
7. Keep claim ceilings as required fields. A packet can propose, measure, witness, or gate, but it cannot silently promote itself.

## Return-Zip Assessment

The old form is stronger than current practice in one way: it makes the return an artifact estate, not an answer.

Current dispatchers often return JSON lines, markdown receipts, or patch files. That is efficient, but it loses the old invariants: full replay context, output hashes, rejected cases, child receipts, and return contract compliance in one atomic object.

Recommended compromise: keep streaming JSONL for progress, but require terminal `RETURN_ZIP` for any packet that can affect admission, graph residency, cross-node exchange, or claim language. The JSONL stream is telemetry; the return zip is the admissible artifact.

## Compact JSON

{"og_docs_found":["READ ONLY Legacy core_docs/a2_runtime_state archived old state/A2_WORKING_UPGRADE_CONTEXT_v1.md","READ ONLY Legacy core_docs/upgrade docs/DIRECTED_EXTRACTION_ANSWERS_v2.md","READ ONLY Legacy core_docs/upgrade docs/DIRECTED_EXTRACTION_AUDIT_AND_QUESTIONS.md","READ ONLY Legacy core_docs/ultra high entropy docs/txt/GPT 12_29 pro plan vs browser crashes.md.txt","READ ONLY Legacy core_docs/a2_feed_high entropy doc/branchthread extract chat gpt.txt","system_v4/a1_state/A1_GRAPH_PROJECTION.json","/Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/READ ONLY Reference Docs/Older Legacy/BOOTPACKS/BOOTPACK_THREAD_B_v3.9.13.md","/Users/joshuaeisenhart/wiki/projects/leviathan-current/MESH_NODE_PROTOCOL_V0_2026-07-02.md","/Users/joshuaeisenhart/wiki/projects/leviathan-current/GATE_DOCTRINE_ADMISSIBILITY_NOT_QUALITY.md","/Users/joshuaeisenhart/wiki/projects/constraint-core/RATCHET_STATE_BY_TIER_2026-07-02.md","/Users/joshuaeisenhart/lev-main/docs/design/proposal-flowmind-ratchet.md"],"sharpest_quote":"ZIPs are treated as deterministic, chatless subagents.","instantiations_mapped":11,"gaps":11,"spec":"./ZIP_AGENT_SPEC_FALLBACK.md"}
