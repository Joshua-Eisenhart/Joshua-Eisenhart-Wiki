# S10 G2 - Standard Math

Status: populated by corpus wave 2 child lane on 2026-06-11. This is a
standard-math and local-ceiling register only. It does not build a packet,
promote a G2 object, or move a repo queue.

## Boundary

Use these notes as labels, source pointers, and future discriminator material.
Do not sample them as a proof that any Codex Ratchet row has earned compact
G2, split G2(2), triality, a physical object, a bridge, or a complete null-row
classification.

## Real forms and models

- Complex type `G2` is rank 2 and dimension 14. The finite-dimensional real
  simple Lie algebras of this complex type have compact and split real forms;
  Draper surveys both real forms and relates Lie algebra, octonion, 3-form, and
  spinorial models. Source: Cristina Draper, "Notes on G2: The Lie algebra and
  the Lie group", arXiv:1704.07819, https://arxiv.org/abs/1704.07819.
- Compact `G2` can be treated as an automorphism group of the real division
  octonions, equivalently as the stabilizer of the positive 3-form on the
  seven-dimensional imaginary octonions. Source: John Baez, "The Octonions",
  Bull. Amer. Math. Soc. 39 (2002), arXiv:math/0105155,
  https://arxiv.org/abs/math/0105155.
- The split real form is associated with split octonions and the split stable
  3-form. Local rows must state metric/signature conventions before using the
  label `G2(2)` or `G_{2(2)}`. Source: Draper, arXiv:1704.07819; Asok-Hoyois-
  Wendt, "Generically split octonion algebras and A1-homotopy theory",
  https://hoyois.app.uni-regensburg.de/papers/octonionbundles.pdf.
- Real-form labels are not interchangeable with finite Chevalley group labels:
  the split real form often written `G2(2)` or `G_{2(2)}` is not the finite
  group `G2(2)`. Local source: `system_v6/receipts/s10_g2_family_mine_20260610.md`.

## Parabolic and Levi material for null rows

- General parabolic theory supplies a Levi quotient/factor only under the
  hypotheses of the chosen reductive/parabolic setting. For standard parabolic
  subgroups, the Levi factor is read from the retained simple roots inside the
  Dynkin diagram; this is a structural theorem, not a license to infer a closed
  embedded factor from a computed stabilizer complement. Source: Brian Conrad,
  "Standard parabolic subgroups: theory and examples",
  https://virtualmath1.stanford.edu/~conrad/249BW16Page/handouts/stdpar.pdf.
- For S10 null rows, the useful standard-math label is therefore
  `nilradical plus Levi quotient` unless a packet explicitly constructs and
  verifies an embedded Levi factor. Local source:
  `system_v6/sims/geo_s10_intertwiner_depth_v0/audit_verdict.md`.
- Current local null-row evidence computes an 8-dimensional split null
  stabilizer with 5-dimensional nilradical and 3-dimensional Levi quotient.
  The audit explicitly blocks the stronger phrase "explicit closed Levi factor"
  until a later packet supplies it. Local source:
  `system_v6/sims/geo_s10_intertwiner_depth_v0/audit_verdict.md`.

## Triality and D4/G2 relationships

- Triality is a special feature of type `D4` / `Spin(8)`: it permutes the three
  eight-dimensional representations. It is not a generic property of G2 rows.
  Source: Baez, "The Octonions", arXiv:math/0105155.
- The standard bridge from D4 triality to G2 is a fixed-point/folding story: G2
  appears in relation to automorphisms of Spin(8)/D4 and octonion
  automorphisms, but a local packet must say which realization it is using.
  Source: McRae, "Exploring Triality Explicitly: Convenient bases for SO(8),
  Spin(1,7), and G2", arXiv:2502.14016, https://arxiv.org/abs/2502.14016.
- Local S10 audit now supports one explicit Chevalley-basis realization of
  D4 representation intertwiners, still at `scratch_diagnostic` ceiling. That
  closes only the local diagram-level caveat for that realization; it does not
  classify all triality intertwiners. Local source:
  `system_v6/sims/geo_s10_intertwiner_depth_v0/audit_verdict.md`.

## Root, Weyl, and branch combinatorics

- The G2 root system has 12 roots, 6 positive roots, Weyl group order 12, and
  two root lengths. These are standard root-system labels, not evidence that a
  local row has installed octonion structure constants. Source: PAWS 2024
  root-system notes, https://swc-math.github.io/aws/2025/PAWSEmory/2024PAWSEmoryNotes.pdf.
- The local branch labels `7`, `14`, and `27` can be used as representation-
  or projector-row labels only when their projector/action ranks are computed.
  The ratchet audit accepts these as bounded algebraic-ratchet rows, not as a
  crowned G2 theorem. Local source:
  `system_v6/sims/ratchet_g2_family_v0/audit_verdict.md`.

## 480-table combinatorics context

- The Fano plane has seven points and seven three-point lines, with each pair
  of points on a unique line. This is the standard finite incidence substrate
  used by octonion multiplication mnemonics. Source: Bruno Sevennec, "Octonion
  multiplication and Heawood's map", arXiv:1106.6015,
  https://arxiv.org/abs/1106.6015.
- The local S10 receipt treats the "480 orientations" as multiplication-table
  variants from 30 labelled Fano triad arrangements times 16 sign/orientation
  choices. The external pointer for the exact 480 count is MathOverflow, so use
  it as a counting pointer to verify by enumerator, not as a promoted theorem.
  Source: https://mathoverflow.net/questions/131167/octonions-and-the-fano-plane;
  local source: `system_v6/receipts/s10_g2_family_mine_20260610.md`.
- The 480 context is admissible only as table/enumerator work: record Fano
  lines, sign choices, structure-constant hash, 3-form hash, metric signature,
  and orbit/class key. Do not create 480 independent "G2 objects" by label.

## Source list

- Baez, "The Octonions", arXiv:math/0105155, https://arxiv.org/abs/math/0105155.
- Draper, "Notes on G2", arXiv:1704.07819, https://arxiv.org/abs/1704.07819.
- Salamon-Walpuski, "Notes on the octonions", arXiv:1005.2820,
  https://arxiv.org/abs/1005.2820.
- Sevennec, "Octonion multiplication and Heawood's map", arXiv:1106.6015,
  https://arxiv.org/abs/1106.6015.
- Conrad, "Standard parabolic subgroups", Stanford notes,
  https://virtualmath1.stanford.edu/~conrad/249BW16Page/handouts/stdpar.pdf.
- McRae, "Exploring Triality Explicitly", arXiv:2502.14016,
  https://arxiv.org/abs/2502.14016.
- PAWS root-system notes,
  https://swc-math.github.io/aws/2025/PAWSEmory/2024PAWSEmoryNotes.pdf.
- Local receipt/audit paths named inline above.
