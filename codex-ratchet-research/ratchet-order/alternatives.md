# Ratchet Order - Alternatives

Status: standing research queue, not populated in this kickoff.

Future work should read the round-2 breadth discriminator and then pin finite
round-3 candidate ids, canonical alias form, expected teeth, and cost guards.

## Wave 2 alternative rows

These are candidate alternative framings for future Ratchet-order tests. Each
row should remain pre-admission until a finite carrier, equivalence relation,
and ordered witness are pinned.

| Alternative | What it canonicalizes | Useful test shape | Bounded source anchor | Kill / defer condition |
| --- | --- | --- | --- | --- |
| Finite transformation monoid action | Reachability under named operations on a finite carrier | Enumerate generated transformations; compare ordered words by resulting transformation plus recorded word | GAP monoid actions, https://webusers.imj-prg.fr/~jean.michel/gap3/htm/chap079.htm | Defer if the carrier or operation generators are not finite and explicit. |
| Inverse-semigroup partial symmetry | Partial maps, idempotents, restriction domains, local inverses | Track domain/range idempotents and partial composition; compare order words after restriction data is preserved | Lawson, DOI `10.1142/3645`; arXiv `2304.13580`, https://arxiv.org/abs/2304.13580 | Kill as overfit if all operations are total transformations and no partiality matters. |
| Lattice / closure-operator tower | Constraint-set refinement and survivor levels | Define meet/join or closure operator; test whether histories converge to same closure element | Birkhoff, DOI `10.1090/coll/025`, https://pubs.ams.org/ebooks/coll/025/ | Kill path-dependence if the same monotone finite closure operator yields the same least fixpoint and histories leave no extra witness. |
| Quotient tower with typed maps | Alias classes across successive abstraction levels | For each level, record equivalence relation, quotient map, and whether order word is preserved or forgotten | Standard quotient/lattice context: Birkhoff DOI `10.1090/coll/025` | Defer if the tower names levels but omits the equivalence relation. |
| Rewrite system / normal form | Canonical representative for expressions or histories | Orient equations, run critical-pair/confluence checks, compare normal forms | Knuth-Bendix PDF, https://www.cs.tufts.edu/~nr/cs257/archive/don-knuth/knuth-bendix.pdf; Baader/Nipkow, https://www21.in.tum.de/~nipkow/TRaAT/ | Kill noncanonical claims if termination and confluence are proven for the exact rewrite relation. |
| Church-Rosser / diamond control | Joinability of diverging reductions | Construct two histories from common source; test whether they join under allowed reductions | Baader/Nipkow, ISBN `9780521779203`; Newman/confluence standard context | Defer if the allowed reductions differ between branches. |
| Mac Lane coherence control | Pure formal rebracketing under associator/unit constraints | Encode only structural associators/unitors; check whether all diagrams commute under coherence assumptions | MIT notes, https://ocw.mit.edu/courses/18-769-topics-in-lie-theory-tensor-categories-spring-2009/ecf8da86e596bf0132023c7dff5732b4_MIT18_769S09_lec03.pdf | Kill a bracketing claim if it is only formal parenthesization inside coherent monoidal structure. |
| CSP propagation fixpoint | Queue-order-insensitive local consistency closure | Run different propagation schedules; compare final domains and retained history witnesses | Apt ISBN `9780521825832`; Dechter ISBN `9781558608900` | Kill mathematical path-dependence if only queue schedule differs and final closure plus history quotient is identical. |
| Sheaf/global-section obstruction | Local-to-global compatibility failure | Define cover, local sections, restrictions, and obstruction test; compare histories as sections only after typing | Abramsky-Brandenburger arXiv `1102.0264`, https://arxiv.org/abs/1102.0264 | Defer if "local/global" is metaphorical and no cover/restriction data is specified. |

## Canonicalization guard

Preferred finite row schema for future packets:

```text
candidate_id:
carrier:
generators_or_constraints:
ordered_word_a:
ordered_word_b:
alias_relation:
quotient_level:
canonical_form_rule:
observable_difference:
kill_condition:
source_anchor:
```

This schema is intentionally conservative: it separates a name, a carrier, a
canonicalization rule, and a surviving observable. A row that cannot fill these
fields should remain a scout row, not an MMM claim.
