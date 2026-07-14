# Story Writing Rules

Load this file only during Steps 3 and 4.

## Source Contract

Use the clarified handoff for batch-specific requirements and `project_context.md` for project-level scope, terminology, actors, and approved decisions.

Use these handoff sections when present:

- Confirmed Requirements
- Clarified Decisions
- Explicit Assumptions
- Open Questions
- Scope Boundaries
- Inputs and Outputs
- User Workflows
- Edge Cases and Error Handling
- Non-Functional Requirements
- Acceptance Notes

If the handoff conflicts with an approved project-context decision, do not choose silently. Report the conflict and return it to clarification.

Carry forward only assumptions explicitly recorded in the handoff. Treat newly discovered uncertainty as an open question, not an assumption.

## Candidate Outcomes

Extract candidate outcomes before writing stories. For each outcome, identify:

- Actor or role
- Capability or observable behavior
- User or business value
- Trigger and expected result
- Scope boundary
- Supporting source requirement
- Material constraints and open questions

Do not infer a benefit merely to complete the format. Defer the outcome when actor, capability, or value cannot be supported.

## Story Form

Use:

> As a `<role>`,  
> I need `<capability>`,  
> so that `<value>`.

Write a concise title that states the user outcome. Use the requester’s terminology unless it is ambiguous or inconsistent with approved project terminology.

## Splitting Rules

Create a separate story when there is a distinct:

- Actor
- User outcome or value
- Independently deliverable workflow
- Acceptance boundary
- Materially different failure behavior

Keep positive, negative, and boundary scenarios in one story when they describe the same user outcome.

Do not split by technical layer such as interface, API, service, database, infrastructure, or test implementation. Do not combine unrelated batches into one story unless the user explicitly requests consolidation and traceability remains clear.

## Partially Ready Batches

Generate a story only when its actor, core behavior, value, and scope are supported. Include material unresolved details under **Open questions**. Defer a candidate when an open question changes its core behavior or acceptance boundary.

## Duplicate Prevention

Compare candidate outcomes with active existing stories. Do not create a new story when an existing story expresses the same actor, capability, value, and scope. Add traceability only when the existing story legitimately covers the new source batch and the user requested consolidation; otherwise report the overlap.
