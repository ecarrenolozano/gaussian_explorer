# Technical Status and Routing

Load during Step 5.

## Per-Story Status

Assign one primary status that identifies the first required action:

- **implementation-ready:** no blocking technical uncertainty remains; dependencies and verification evidence are sufficient for an implementation issue.
- **needs-requirement-clarification:** implementation depends on missing or conflicting product behavior, business rules, ownership, constraints, or acceptance outcomes.
- **needs-story-revision:** source evidence is sufficient, but story wording, scope, splitting, acceptance criteria, priority, lineage, or traceability must change.
- **needs-architecture-change:** a system-wide, cross-story, interface, data-ownership, deployment, trust-boundary, or consequential technical decision must be changed or recorded by architecture.
- **needs-technical-spike:** feasibility or a consequential technical choice cannot be resolved responsibly from available evidence and needs bounded investigation.
- **blocked-external:** a known external dependency, environment, vendor, policy, hardware, approval, or prerequisite prevents implementation.
- **blocked-state:** malformed, stale, missing, duplicated, or contradictory artifact state prevents reliable assessment.

When multiple findings apply, choose the earliest owning stage in this order: `blocked-state`, requirement clarification, story revision, architecture change, technical spike, external blocker, implementation ready. Record secondary findings separately.

## Routing

- `needs-requirement-clarification` -> `b-requirements-clarifier`, then regenerate/review downstream artifacts.
- `needs-story-revision` -> `c-create-user-stories`, then `d-user-story-product-readiness`; assess architecture impact before returning here.
- `needs-architecture-change` -> `e-architecture-and-design`, then return here after architecture approval.
- `needs-technical-spike` -> prepare a spike candidate; `g-create-repository-issues` publishes it after approval.
- `blocked-external` -> named owner or dependency; reassess when resolved.
- `blocked-state` -> the skill that owns the inconsistent artifact.
- `implementation-ready` -> eligible for technical approval and later publication by `g-create-repository-issues`.

Do not edit or split stories, write ADRs, redesign architecture, or create issues in this skill.

## Review Assessment

For the reviewed set, assign:

- **technical-ready:** every reviewed story is `implementation-ready`.
- **partially-ready:** at least one story is `implementation-ready`, at least one is not, and eligible stories can proceed without depending on non-ready stories.
- **changes-required:** no artifact-state blockage exists, but the set is not safely publishable in whole or in an independent subset.
- **blocked:** upstream state prevents reliable review.

Publication eligibility is per story. `implementation-ready` does not itself equal human approval.
