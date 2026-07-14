# Readiness and Approval

## Assessments

Use the least-ready applicable assessment.

### `ready-for-deployment`

Use only when all applicable preparation is complete, no blocking risk remains, and the plan is actionable by an authorized execution process.

### `ready-with-accepted-risks`

Use only when every remaining material risk records:

- description and expected impact;
- mitigation or contingency;
- owner;
- authorized approver;
- acceptance date;
- review or expiration condition when applicable.

### `not-ready`

Use when known defects, rejected acceptance, unsafe migration or recovery, or unacceptable risk prevents deployment.

### `blocked`

Use when required artifact, environment, access, information, evidence, owner, or decision is unavailable or inconsistent.

## Human approval

Record approval only when the user explicitly approves the exact current deployment-plan version for the named environment.

Record:

- plan version;
- release candidate;
- target environment;
- assessment;
- decision;
- approver;
- date;
- comments;
- accepted-risk references.

Approval authorizes the plan for execution by the designated process. It does not mean deployment occurred.

A change to the plan, artifact, environment, migration, rollback approach, or material risk resets the decision to pending.
