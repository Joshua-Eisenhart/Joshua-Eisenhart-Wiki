---
title: Wizard v4.1 Hermes Adapter
type: runtime_adapter
packet: v4.1
runtime: hermes
framing: standalone
---

# Hermes Adapter

This adapter binds the universal Wizard to Hermes-style memory, carry-forward, and durable process surfaces.

These are Hermes-specific runtime rules. They are not universal Wizard requirements.

## Role

Hermes is useful for:

- memory retrieval;
- long-horizon continuity;
- carry-forward packets;
- contradiction tracking;
- source-and-lift receipts;
- preserving decisions across sessions.

## Main Thread Use

When Hermes memory is available, the main thread may request:

- relevant prior decisions;
- current standing constraints;
- known failure patterns;
- open blockers;
- prior receipts.

Hermes material is source input. It is not execution proof.

## Hermes Receipt

A Hermes receipt should name:

- memory surface queried;
- source slice returned;
- confidence or freshness;
- contradiction or drift signal;
- evidence boundary;
- what the memory does not prove.

## Admission

Hermes memory can influence salience and context.

It can prove that a prior note exists.

It cannot prove that current work executed unless paired with a current execution receipt.

## Carry-Forward

At closeout, Hermes may receive:

- accepted decision;
- blocked route;
- deferred route;
- artifact surface;
- next bounded prompt;
- evidence boundary.

Do not write vague summaries. Write only bounded, reusable carry-forward state.
