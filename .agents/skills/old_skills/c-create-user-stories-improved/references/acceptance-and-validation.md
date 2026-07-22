# Acceptance Criteria, Quality, Identifiers, and Priority

Load this file only during Steps 5 and 6.

## Acceptance Scenarios

Write at least one primary Given/When/Then scenario for each story.

Each scenario must be:

- observable from the user or system boundary;
- unambiguous and testable;
- focused on one outcome;
- supported by the clarified handoff;
- free of implementation prescriptions.

Use additional scenarios for supported alternate, negative, permission, validation, boundary, or failure behavior. Do not invent edge cases solely to make the story appear complete.

Use this structure:

```markdown
**Scenario: <observable outcome>**

Given <starting state or context>
When <user action or event>
Then <observable result>
```

Use `And` only when it adds another condition or result to the same scenario. Avoid phrases such as `works correctly`, `behaves properly`, or `looks good`.

## Story Validation

Before assigning an identifier, confirm that the story:

- traces to at least one valid eligible batch;
- has an evidence-supported actor, capability, and value;
- describes a user-visible outcome rather than a technical task;
- has clear scope and no unsupported assumptions;
- does not duplicate an active existing story;
- has testable scenarios covering the primary outcome;
- preserves material constraints and open questions;
- is small and bounded enough for downstream planning.

Use INVEST as a quality heuristic:

- Independent
- Negotiable
- Valuable
- Estimable
- Small
- Testable

INVEST does not override evidence. A well-formed but unsupported story must not be persisted.

Revise a candidate when wording or splitting is the issue. Defer it when source evidence is insufficient or an unresolved decision changes core behavior. Do not assign an identifier to a deferred candidate.

## Duplicate Handling

Compare actor, capability, value, acceptance behavior, and scope with active existing stories.

When an existing story already represents the same material outcome:

- do not create a duplicate;
- add the new source batch to the existing story metadata and visible source details;
- append the missing traceability relationship;
- include the existing identifier in the new batch registry marker;
- create a new draft document version because persistent content changed.

Do not merge stories whose actors, outcomes, scope, or acceptance boundaries materially differ.

## Feature Groups

Group stories by a user-facing capability or domain concept supported by project terminology. Do not use a technical component or implementation layer as the feature name unless it is itself user-facing.

## Priority

Assign exactly one priority using available evidence:

- **MVP:** Required for the smallest complete, usable end-to-end outcome.
- **Post-MVP:** Valuable but not required for initial usability.
- **Deferred:** Optional, speculative, blocked, or dependent on unresolved decisions.
- **Unconfirmed:** Available evidence does not support a priority decision.

Do not infer priority from document order, perceived effort, or personal preference.

## Story Identifiers

Use `US-XXXX`, where `XXXX` is a four-digit sequence.

1. Scan existing story metadata and headings.
2. Stop on malformed or duplicate identifiers.
3. Use `US-0001` when none exist.
4. Otherwise increment the highest numeric value.
5. Assign identifiers only after validation.
6. Never reuse, renumber, or silently repair an identifier.

Use this metadata comment immediately below each story heading:

```html
<!-- story-id: US-0001 | source-batch: PRDB-001 | priority: MVP | lifecycle: active -->
```

Use comma-separated source-batch identifiers only when one story legitimately traces to multiple batches. Allowed lifecycle values are `active` and `deprecated`.


## Interaction-State Validation

When the source describes configurable or reactive behavior, verify scenarios for supported state transitions, including:

- enabled versus disabled modes;
- initial versus fitted/effective values;
- fixed versus optimized parameters;
- refit or live-update behavior after a setting changes;
- stale-result indication;
- reset or restore behavior.

Do not require all scenarios universally. Include them when the handoff or project context supports the behavior.

## Coverage Validation

Before assigning identifiers, verify that every source statement has a provisional coverage disposition and that the candidate story does not absorb unrelated NFRs, decisions, or implementation tasks.
