# Status and Routing

## Behavior result

Use one:

- `met`;
- `not-met`;
- `blocked`;
- `not-executed`.

## Stakeholder disposition

Use one:

- `accepted`;
- `rejected`;
- `accepted-by-explicit-waiver`;
- `pending`.

A waiver must record the exact deviation, impact, mitigation, owner, approver, date, and review condition when applicable.

## Routing

- implementation violates approved behavior -> implementation, then Skill I retesting;
- implementation plan must change -> Skill H;
- automated evidence missing -> Skill I;
- story or acceptance criterion defective -> Skill C, then Skill D;
- requirement missing or new behavior requested -> Skill B;
- architecture prevents required behavior -> Skill E, then downstream reassessment.
