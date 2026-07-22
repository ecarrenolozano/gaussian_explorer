# Readiness Scoring

Load this file only when assigning handoff readiness.

## Criteria

Score each criterion from 1 to 5:

1. User or stakeholder goal
2. Target users or roles
3. Main input and output expectations
4. Main workflow and expected behavior
5. Scope boundaries
6. Important constraints and dependencies
7. Major edge cases or invalid states
8. Acceptance-level expectations

Treat criteria 1-5 as essential.

## Scale

- **1 - Undefined:** No reliable information.
- **2 - Weak:** Partial information with substantial ambiguity.
- **3 - Partial:** Core meaning is understandable, but important details remain unresolved.
- **4 - Clear:** Sufficient for downstream planning, with minor uncertainty.
- **5 - Explicit:** Complete, confirmed, and supported by clear evidence.

Calculate the arithmetic mean of all eight scores. Use the unrounded mean for thresholds and report the average to one decimal place.

A **blocking contradiction** is a conflict that prevents a consistent interpretation of the goal, users, scope, behavior, or acceptance expectations.

## Status Rules

Apply these rules in order:

1. Select **Not ready** if the average is below 3.0, any essential criterion is below 3, a blocking contradiction remains, or downstream work would require inventing core behavior.
2. Otherwise, select **Ready** only if the average is greater than 4.5, no essential criterion is below 4, and no unresolved contradiction materially affects the requirement.
3. Select **Partially ready** for every remaining case where the core requirement can be documented without inventing it.

When conditions appear to conflict, select the least-ready status.

## Required Output

Record:

- Each criterion and score
- Overall average to one decimal place
- Selected status
- Blocking issues, if any
- Whether downstream user-story generation should proceed
