# Clarification Interview Guide

Load this file only when Step 4 requires user input.

## Priority

Ask about unresolved items in this order:

1. Contradictions that prevent a consistent interpretation
2. Missing decisions that block downstream planning
3. Ambiguities affecting goals, scope, users, workflows, inputs, outputs, or acceptance
4. Assumptions that could materially change the solution
5. Out-of-scope candidates requiring confirmation
6. Lower-impact details and preferences

Defer questions that do not affect the current batch or its readiness.

## Formulate Questions

For each question:

- Ask about one decision unless related decisions must be resolved together.
- Explain enough context for the user to understand why the answer matters.
- Use requester terminology.
- Avoid unexplained jargon and leading language.
- Offer concrete options only when they represent real alternatives, and allow another answer.
- Do not ask for information already established by the sources, conversation, or prior responses.

When evidence implies but does not state a requirement:

1. State the current interpretation.
2. Identify the supporting evidence.
3. Ask the user to confirm or correct it.

Example:

> The raw requirement appears to imply that only administrators can approve requests. Should this be a confirmed access rule, or may other roles approve them?

## Choose the Interview Mode

Ask one question at a time when the next question depends on the answer, the issue is high impact, or interpretations differ materially.

Use a small grouped set when questions are independent, the user is preparing for a requester meeting, or the user requests a questionnaire. Group by theme and place the highest-impact questions first.

Use only relevant themes:

- Goal and success criteria
- Users, roles, and permissions
- Inputs, formats, validation, and examples
- Outputs and user-visible behavior
- Main and alternative workflows
- Scope boundaries and exclusions
- Domain terminology
- Edge cases and failure handling
- Constraints, dependencies, and integrations
- Security, privacy, safety, and data retention
- Acceptance expectations
- Deployment and operations

## Process Each Response

After every response:

1. Update the requirement-state classification.
2. Convert resolved items into confirmed requirements or clarified decisions when supported.
3. Preserve unresolved items.
4. Record new uncertainty introduced by the answer.
5. Ask the next highest-impact question.

Do not interpret beyond what the user explicitly confirmed. When an answer remains unclear, summarize the current interpretation and request confirmation.

## Stop

Stop when:

- Readiness can be determined reliably.
- No unresolved item materially affects scope, behavior, acceptance, risk, architecture, or backlog structure.
- Remaining questions are optional preferences.
- The user asks to stop or requests the current handoff.

Do not continue only to populate every handoff section. Preserve unresolved essentials under **Open Questions** and lower readiness accordingly.
