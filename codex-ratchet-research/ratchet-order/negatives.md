# Ratchet Order - Negatives

Status: standing research queue, not populated in this kickoff.

Expected negative controls: same unordered support without same order,
composition equality claims without noncommutation checks, and alias inflation
from convention-equivalent but order-distinct rows.

## Wave 2 negative controls

Use these as "what would forbid the claim" checks. They are not failures of the
research program; they are the conditions under which order/path language must
be narrowed or removed.

### Associativity, bracketing, and coherence

- **Pure associativity is not a Ratchet witness.** If the only difference is
  `((a*b)*c)` versus `(a*(b*c))` inside an ordinary associative operation, the
  bracketing difference is killed.
- **Mac Lane coherence kills formal-only bracketing claims.** If the row lives
  entirely inside a monoidal category's structural associators and unitors and
  the pentagon/triangle hypotheses hold, the standard result is that formal
  diagrams commute. A surviving Ratchet claim needs a non-formal observable or
  a justified failure of the coherence hypotheses. Sources: Mac Lane,
  *Categories for the Working Mathematician*, ISBN `9780387984032`; MIT notes,
  https://ocw.mit.edu/courses/18-769-topics-in-lie-theory-tensor-categories-spring-2009/ecf8da86e596bf0132023c7dff5732b4_MIT18_769S09_lec03.pdf.
- **Strictification is an alias trap.** If a weak associative structure can be
  strictified without changing the relevant semantics, then "different
  parentheses" may be notation rather than identity. Do not promote unless the
  strictification/quotient explicitly preserves a measured distinction.

### Confluence, termination, and normal forms

- **Confluent terminating rewrite systems kill path-specific normal forms.** If
  the exact Ratchet expression/history rewrite relation is terminating and
  confluent, normal forms are unique; order identity should be stated at the
  normal-form level, not as path dependence. Sources: Baader/Nipkow,
  https://www21.in.tum.de/~nipkow/TRaAT/; Knuth-Bendix PDF,
  https://www.cs.tufts.edu/~nr/cs257/archive/don-knuth/knuth-bendix.pdf.
- **Local confluence plus termination is enough in the classic Newman's-lemma
  setting.** Do not keep a path-dependence claim alive merely because only
  local forks were inspected; if termination is proven and critical local forks
  are joinable, global confluence may follow under the standard hypotheses.
- **Completion success is a negative control.** If Knuth-Bendix completion
  succeeds for the declared equations and reduction order, and both histories
  reduce to the same normal form, the candidate is an alias/canonicalization
  row, not a live order-distinction row.

### Constraint propagation and fixpoint traps

- **Queue-order dependence is not automatically mathematical path dependence.**
  Many CSP propagation algorithms use work queues whose processing order can
  vary while the intended local-consistency closure remains the same. A
  Ratchet claim needs either distinct final closures or a declared history
  witness that survives the quotient. Sources: Apt, ISBN `9780521825832`,
  https://assets.cambridge.org/97805218/25832/sample/9780521825832ws.pdf;
  Dechter, ISBN `9781558608900`, https://dl.acm.org/doi/10.5555/861888.
- **Monotone finite closure can erase order.** If the operator is monotone over
  a finite lattice and the test only asks for the least fixpoint, different
  iteration orders may be implementation detail. Source context: Birkhoff,
  DOI `10.1090/coll/025`.
- **Local consistency is incomplete.** Failure of arc/path consistency to decide
  a CSP is not evidence that Ratchet order exists; it may only mean the chosen
  local method is too weak.

### Alias traps

- **Same unordered support is not same ordered word.** If a quotient forgets
  order, it cannot be used to prove ordered identity. Conversely, if all
  downstream observables also forget order, it cannot prove ordered difference.
- **Convention-equivalent labels are not distinct objects.** Renaming basis,
  generator labels, sign conventions, or presentation syntax must be quotient
  tested before being counted as a separate Ratchet row.
- **Source/target mismatch invalidates composition evidence.** A composed row
  is void if the codomain of one step is not the domain of the next under the
  declared typing discipline.
- **Sheaf language must not be metaphor-only.** "Local obstruction" language is
  killed unless the packet defines a cover, local sections, restriction maps,
  and global-section criterion. Source: Abramsky-Brandenburger arXiv
  `1102.0264`, https://arxiv.org/abs/1102.0264.
