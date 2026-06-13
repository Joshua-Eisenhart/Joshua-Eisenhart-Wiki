# Ratchet Order - Standard Math

Status: standing research queue, not populated in this kickoff.

Expected scope: ordering/canonicalization mathematics, alias classes,
noncommutation/order witnesses, and finite order-row invariants used by future
ratchet-order discriminators.

Do not sample this placeholder into MMM heads.

## Wave 2 source-backed context

This note is standard-math context only. It does not assert that Ratchet order
identity has been proven; it records the ordinary mathematical neighborhoods in
which such a claim would need witnesses.

### Order structures and quotients

- **Finite monoid / semigroup actions.** A finite operation library can be
  modeled as transformations acting on a finite carrier. Orbits, stabilizers,
  congruences, and quotients are the standard vocabulary for "same reachable
  class" versus "same named step." For Ratchet use, a monoid-action row is only
  an alias/control row unless it also preserves the ordered transition witness.
  Sources: GAP monoid action manual,
  https://webusers.imj-prg.fr/~jean.michel/gap3/htm/chap079.htm; Lawson,
  *Inverse Semigroups: The Theory of Partial Symmetries*, DOI
  `10.1142/3645`.
- **Inverse-semigroup / partial-symmetry refinement.** Gemini cross-check
  flagged inverse semigroups as a better standard context when operations are
  partial, non-invertible, or idempotent-rich. Treat this as an alternative
  modeling lens, not evidence that Ratchet transitions form an inverse
  semigroup. Sources: Lawson, DOI `10.1142/3645`; Lawson, "Introduction to
  inverse semigroups," arXiv `2304.13580`,
  https://arxiv.org/abs/2304.13580.
- **Lattices and quotient towers.** Candidate constraint sets, refinement
  levels, and survivor sets can be organized as partially ordered structures.
  A quotient tower should specify the equivalence relation at each level and
  the map between adjacent levels; otherwise it is just a naming stack. Source:
  Birkhoff, *Lattice Theory*, AMS Colloquium Publications 25, DOI
  `10.1090/coll/025`, https://pubs.ams.org/ebooks/coll/025/.

### Path-dependence and constraint satisfaction context

- **CSP local consistency is pruning, not global identity.** Arc consistency,
  path consistency, and stronger local consistency methods remove locally
  unsupported assignments. They do not by themselves prove that all admissible
  pruning orders produce the same canonical survivor, unless the algorithm and
  fixpoint theorem being used state that property for the exact operator class.
  Sources: Apt, *Principles of Constraint Programming*, Cambridge University
  Press, ISBN `9780521825832`,
  https://assets.cambridge.org/97805218/25832/sample/9780521825832ws.pdf;
  Dechter, *Constraint Processing*, Morgan Kaufmann, ISBN `9781558608900`,
  ACM entry https://dl.acm.org/doi/10.5555/861888.
- **Algorithm order vs mathematical path dependence.** A solver may visit arcs,
  variables, or constraints in different queue orders while still computing the
  same least/greatest fixpoint for a monotone finite-domain operator. Ratchet
  path-dependence needs a stronger witness: two admissible ordered histories
  that remain distinct after the declared alias/quotient maps.
- **Sheaf/global-section analogy is a guardrail.** Sheaf language can describe
  when locally compatible data fail to glue into a global section, but importing
  it into Ratchet requires an explicit cover, restriction maps, and obstruction
  criterion. Source: Abramsky and Brandenburger, "The Sheaf-Theoretic Structure
  of Non-Locality and Contextuality," arXiv `1102.0264`,
  https://arxiv.org/abs/1102.0264.

### Bracketing and associativity context

- **Mac Lane coherence kills purely formal bracketing differences.** In a
  monoidal category satisfying the pentagon and triangle coherence conditions,
  formal composites built only from associators and unitors agree. A Ratchet
  bracketing witness must therefore show extra structure outside the purely
  coherent formal rebracketing fragment, or show that the relevant coherence
  hypotheses do not apply. Sources: Mac Lane, *Categories for the Working
  Mathematician*, 2nd ed., ISBN `9780387984032`; MIT tensor category notes,
  https://ocw.mit.edu/courses/18-769-topics-in-lie-theory-tensor-categories-spring-2009/ecf8da86e596bf0132023c7dff5732b4_MIT18_769S09_lec03.pdf;
  nLab overview,
  https://ncatlab.org/nlab/show/coherence+and+strictification+for+monoidal+categories.
- **Associator rows need source/target typing.** A bracketing row is not
  meaningful unless the carrier, product/tensor operation, unit convention,
  associator map, and allowed composites are fixed. "Different parentheses"
  alone is not evidence of distinct Ratchet order identity.

### Rewrite and normal-form context

- **Confluence plus termination supports unique normal forms.** In term
  rewriting, termination and confluence are the standard sufficient conditions
  for existence and uniqueness of normal forms. Newman's lemma gives the
  classic route from termination plus local confluence to confluence. Sources:
  Baader and Nipkow, *Term Rewriting and All That*, Cambridge University Press,
  ISBN `9780521779203`, TUM page https://www21.in.tum.de/~nipkow/TRaAT/;
  Knuth and Bendix, "Simple Word Problems in Universal Algebras,"
  https://www.cs.tufts.edu/~nr/cs257/archive/don-knuth/knuth-bendix.pdf.
- **Completion is conditional.** Knuth-Bendix completion is a way to attempt a
  terminating confluent rewrite system for equations under a reduction order.
  Failure, nontermination, or nonconfluence are ordinary outcomes and should be
  negative controls for any claimed canonical Ratchet order form.
