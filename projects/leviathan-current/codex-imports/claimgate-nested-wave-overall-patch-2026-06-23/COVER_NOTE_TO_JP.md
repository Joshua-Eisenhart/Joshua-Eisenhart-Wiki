# Cover Note To JP: ClaimGate / Nested Wave Patch

JP,

This is a review packet, not a pushed branch. The goal is to preserve and share the current ClaimGate/Lev patch direction without smearing it into Lev canon prematurely.

The core correction is architectural:

```text
Waves are nested sets of councils.
Many things that sound like waves are actually councils or subcouncils.
The work plane needs a parallel management plane that handles resources,
context loading, laggards, rerouting, gates, receipts, and failure packets.
```

The patch adds/prototypes the ClaimGate-side loop and repair machinery around this shape:

- ClaimGate council-wave loop contracts and tests.
- Required cognitive bindings for council members: skills, MMMs, source refs, input/output contracts, gate contracts, and requeue policy.
- Failure packets and repair-wave/repair-dispatch planning.
- ClaimGate steering hardening and host-consumption boundaries.
- CDO/triple50 integration hooks for council-wave execution.
- Sparse OpenRouter flow/profile surfaces for bounded outside-model lanes.

What this is not claiming:

- Not full Lev runtime completion.
- Not production admission.
- Not full nested-council runtime proof.
- Not proof that every spawned agent actually loads skills/MMMs yet.
- Not a second proof brain outside Lev.

Suggested review posture: treat this as a patch candidate and split it into smaller PRs if useful:

1. ClaimGate loop/contracts.
2. Cognitive member manifest gate.
3. Repair dispatch / failure packet routing.
4. Management-plane contracts.
5. CDO/triple50 integration.

The important design principle is: councils and agents may generate and repair, but ClaimGate/Lev gates decide what advances.
