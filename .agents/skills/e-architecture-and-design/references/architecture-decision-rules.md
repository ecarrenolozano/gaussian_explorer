# Architecture Decision Record Rules

Load during Step 6.

Create an architecture decision record only when a decision:

- is difficult or expensive to reverse;
- affects multiple major applications, services, teams, or stories;
- changes data ownership, deployment, trust boundaries, interoperability, or a major dependency;
- resolves an important quality trade-off; or
- establishes a long-lived technical constraint.

Do not create architecture decision records for routine implementation details, minor library choices, or product decisions.

## File Naming

Use `architecture-decision-NNN-short-title.md`. Determine the next number by scanning existing architecture decision files and incrementing the highest value. Start at `architecture-decision-001`. Never reuse or renumber an existing decision number.

The number is only a document sequence. It must not become a source-code, module, package, service, or deployment identifier.

## Status

Use one status: `proposed`, `accepted`, `superseded`, or `rejected`.

- New decisions remain `proposed` until explicit architecture approval accepts them.
- On approval, update all decisions required by the approved architecture to `accepted` as part of the same consistent change.
- Do not rewrite an accepted record to change its decision. Create a new record and mark the older record `superseded`.
- A required blocking decision cannot remain unresolved when architecture is assessed as ready.

## Content

Use `templates/architecture-decision.md`. Record context, decision, alternatives, rationale, consequences, validation, related stories, related architecture areas, and follow-up work.

When evidence is insufficient for a consequential decision, record the open question and mark the architecture as blocked. Do not disguise uncertainty as an accepted decision. A technical investigation may be recommended, but issue creation belongs downstream.
