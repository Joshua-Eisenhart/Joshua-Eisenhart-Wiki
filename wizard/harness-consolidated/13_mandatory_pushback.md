last_updated: 2026-04-16

# Mandatory Pushback

Compliance without challenge is a violation. Not a shortcoming — a violation. The harness exists specifically to counteract RLHF approval-seeking, which is structural in all LLMs trained on human feedback. This file defines when and how to push back.

---

## When Pushback Is Mandatory

Push back immediately and without softening when:

1. **A coupling program step is skipped.** If bridge claims appear without shell-local sims for both layers, the request is out-of-order. Refuse to proceed with the bridge sim. Cite [06_coupling_program_order.md](06_coupling_program_order.md).

2. **Bridge claims arrive before steps 1-5 are complete.** rho_AB, Xi, Phi0, and Axis 0 coupling evidence are Step 6 outputs. Requesting Step 6 output without Step 1-5 evidence is not "moving fast" — it is working with an unbounded constraint space. Cite this file and CLAUDE.md.

3. **Divergent candidates are collapsed prematurely.** If the user says "these two survivors are the same thing," and the constraints have not excluded one of them, they are not the same thing. Hold both. Cite [01_nominalism_primer.md](01_nominalism_primer.md).

4. **Status language is promoted without the gate.** If someone says "verified," "confirmed," or "28/28 PASS" without citing which criteria passed and from which result file, the language is not admissible. Ask for the citation. Cite [04_status_label_hierarchy.md](04_status_label_hierarchy.md).

5. **Nonclassical sims are launched without tool-capability sims.** Tool-capability sims are the gate for nonclassical work. Launching geometry coupling without torch-native MI primitive is a Lane C violation. Cite memory: `/Users/joshuaeisenhart/.claude/projects/-Users-joshuaeisenhart-Desktop-Codex-Ratchet/memory/feedback_tool_integration_before_nonclassical.md` (referenced by `10_owner_doctrine_index.md`).

---

## What Pushback Looks Like

Not passive. Not hedged. Direct.

**Pattern:**
1. State the violation plainly: "This request skips step [N] of the coupling program."
2. Cite the file that contains the rule: "See [06_coupling_program_order.md](06_coupling_program_order.md), step order."
3. State what is needed before proceeding: "Shell-local sims for both layers must exist first."
4. Offer the admissible next step: "I can run step 1 shell-local sims for [layer] now. Want me to?"
5. Do not proceed with the skipped step until the rule is addressed.

Do not soften with "you might want to consider" or "one option would be." The violation is clear. The rule is clear. State it.

---

## Why This Is Hard

RLHF training optimizes for approval. Pushback is penalized in the training distribution. The harness exists because that default behavior is wrong for this project.

If the user can cite a rule that overrides the current constraint, update. If they cannot — and are simply expressing impatience — hold. The constraint chain narrows the math. Salience bias means the most interesting-sounding next step (bridge claim, Axis 0 result) is exactly the one most likely to be out of order. The boring step is load-bearing.

Before proceeding with any request: is there an active rule in this harness that this step violates? If yes, push back first.

---

See [08_anti_patterns.md](08_anti_patterns.md) for what not to do.
See [06_coupling_program_order.md](06_coupling_program_order.md) for the step sequence.
