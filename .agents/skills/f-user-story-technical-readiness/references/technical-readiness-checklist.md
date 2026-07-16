# Technical Readiness Checklist

Apply only relevant checks.

## arc42 Evidence

- The story is covered by the relevant goals, constraints, context, solution strategy, building blocks, runtime behavior, deployment, cross-cutting concepts, quality scenarios, risks, and decisions.
- Unrelated arc42 sections may be brief or explicitly not applicable.
- Open architecture questions that affect implementation are visible and routed.

## C4 and Ownership Path

- The story maps to the correct software system.
- The owning container is explicit.
- Affected components or data models are explicit when needed.
- Referenced container, component, and data documents exist.
- The architecture responsibility matches the story outcome.
- The implementation mapping is `confirmed`, `proposed`, `planned`, or explicitly `not-mapped`.
- A proposed or not-mapped location does not hide a blocking design decision.

## Interfaces and Data

- Providers, consumers, protocols, data formats, validation, errors, and compatibility expectations are sufficiently defined.
- Data ownership, lifecycle, consistency, migration, retention, access, and recovery concerns are sufficiently defined.

## Runtime and Internal Design

- Important success, failure, asynchronous, retry, and recovery flows are sufficiently defined.
- Significant component responsibilities are cohesive and non-overlapping.
- Selective code-level design exists when state, lifecycle, concurrency, domain relationships, collaboration, or risk makes it necessary.
- Missing design is routed to Skill E instead of invented here.

## Quality and Cross-Cutting Concepts

- Relevant quality scenarios have measurable or reviewable outcomes.
- Security, privacy, configuration, secrets, logging, monitoring, error handling, performance, scalability, and testing concepts are sufficient for planning when applicable.
- Architecture decisions and risks that constrain the story are explicit.

## Deployment and Operations

- Runtime and deployment paths are clear where they affect implementation.
- Environment, configuration, secret ownership, observability, scaling, recovery, and external dependencies are understood enough to plan work.

## Verification

- Acceptance behavior can be verified.
- Required developer, integration, end-to-end, regression, performance, security, migration, or recovery evidence can be planned.
- Environments, test data, or external systems are available or explicitly blocked.

## Technical Uncertainty

- Unknowns are classified as ordinary implementation detail, architecture work, product clarification, or bounded spike.
- External dependencies have owners and expected evidence.
- No unresolved question is hidden behind optimistic assumptions.
