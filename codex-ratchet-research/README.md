# Codex Ratchet Research Corpus

Status: architecture scaffold and kickoff surface.

This corpus is the research layer for the alternatives program. It gathers
standard mathematical treatments, bounded alternative families, and designed
negative controls before any future card or blind sheet tries to use them.

## Authority And Flow

The knowledge stack has three tiers:

1. Wiki research corpus: broad source-grounded notes, literature structure,
   standard facts, alternative-space bounds, and first-class negatives.
2. Distillates: bounded extractions in the MMM register that a future card or
   blind sheet may draw from.
3. MMM heads: small salience heads only. They do not ingest the corpus.

Pollution rule: corpus material never flows directly into MMMs. Only a
distillate may be sampled into an MMM head, and the distillate must keep the
nominalist/empiricist register: names are labels for tested distinctions,
identity is probe-relative, exclusions are preferred over reified
constructions, and unsupported abstractions are not promoted.

## Directory Contract

Each layer directory holds exactly these recurring files:

- `standard-math.md`: the literature treatment of the mathematical objects
  used by that layer.
- `alternatives.md`: the registry's finite alternative spaces researched with
  definitions, known results, and classification theorems that bound the space.
- `negatives.md`: designed-fail controls and kill tests. Negative results are
  first-class evidence, not cleanup.
- `distillate.md`: bounded extraction for future cards/blind sheets, written
  in the MMM register.

## Layer Directories

- `s2-connections`: connection, flux, foliation, gauge convention, and lifted
  holonomy alternatives for the S2 Hopf-torus layer.
- `s3-probes`: density and observable probe-family alternatives, including
  POVM alias handling.
- `s4-operators`: operator/channel alphabet alternatives, with CPTP, affine
  Bloch-map, unital/non-unital, and Choi-boundary controls.
- `s5-flows`: terrain flow alternatives, affine ball dynamics, and
  generator-level flow controls.
- `s67-topologies`: support graphs, covers, lens actions, and finite topology
  alternatives.
- `s9-transport`: connection and transport alternatives, including same-Chern
  different-holonomy families and path-ordered loop tests.
- `s10-g2`: G2-related alternatives and future discriminator rows.
- `ratchet-order`: ratchet-order alternatives and ordering/canonicalization
  controls.

## Research Register

Write corpus files as research notes with explicit bounded claims:

- cite the object being classified or controlled;
- distinguish equality, gauge equivalence, convention equivalence, and
  co-survival;
- keep classification theorems attached to their hypotheses;
- state what a theorem forbids before stating what it permits;
- preserve designed-fail controls as reusable test material;
- mark repo-registry candidates separately from standard literature facts.

Write distillates as future-work extraction:

- use tested labels rather than reified objects;
- say "this row excludes..." before "this object is...";
- prefer "under this probe/canonicalizer" to global identity language;
- keep promotion blocked unless a future receipt supplies the gate.

## Standing Queue

Kickoff priority is `s2-connections`, `s4-operators`, `s5-flows`, and
`s9-transport` because the round-3 registry marks them as heavy or closest
neighbors. Remaining standing queue: `s3-probes`, `s67-topologies`, `s10-g2`,
and `ratchet-order`.
