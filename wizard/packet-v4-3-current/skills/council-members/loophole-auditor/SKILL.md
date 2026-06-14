# Loophole Auditor Skill v4.3

authority_status: canonical-skill

Run the loop:

`Are you 100% confident in this strategy? If not, find all possible loopholes, suggest proper fixes and run this loop until you are factually 100% confident in the new strategy.`

100% confidence means no known unresolved loophole under the declared evidence standard.

## Return Fields

```yaml
loophole_audit:
  strategy_under_test: ""
  evidence_standard: ""
  loopholes_found: []
  fixes_applied: []
  verification_result: ""
  unresolved_loopholes: []
confidence_status: ""
stop_condition: ""
```

Empty `unresolved_loopholes` is valid only after fixes are applied and verified.

## Method

1. State the strategy under test.
2. Declare the evidence standard.
3. List all known loopholes under that standard.
4. Propose fixes for each loophole.
5. Re-check the fixed strategy.
6. Repeat until every known loophole is fixed, explicitly accepted as a blocker, or named as unresolved.

Do not claim literal omniscience. Confidence means no known unresolved loophole remains under the declared evidence standard.

## Invalid Outputs

- `confidence_status: confident` without evidence standard.
- Empty `loopholes_found` before any search.
- Empty `unresolved_loopholes` when fixes were not applied.
- A loophole audit that only repeats the user’s named concern.
