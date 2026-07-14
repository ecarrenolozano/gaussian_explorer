# Workflow State Detection

## State Vocabulary

Assign one state per stage:

- `not-started`: no meaningful stage evidence exists;
- `in-progress`: draft or partial artifacts exist without the required completion evidence;
- `awaiting-approval`: the artifact is reviewable but the owning human approval is absent;
- `completed`: required evidence exists and matches current upstream versions;
- `blocked`: a prerequisite, decision, environment, tool, or owner is missing;
- `stale`: the stage was completed for an older upstream version or different artifact;
- `inconsistent`: identifiers, versions, mappings, or status evidence contradict each other;
- `not-applicable`: explicitly justified as unnecessary for the selected scope.

Do not equate `completed` with a file merely existing.

## Stage Evidence

### A — Project Context

Inspect `sdlc_docs/00_project_context/project_context.md` or the canonical path declared by Skill A. Determine whether required context sections and its approval gate are complete. Missing or unapproved context normally blocks downstream product work.

### B — Requirements Clarification

Inspect `sdlc_docs/01_requirements/00_raw_ideas.md` for requirement batches such as `PRDB-XXX`. Use the batch's processing and readiness state. A batch may be ready, partially ready, not ready, or still being clarified; do not collapse these into one project-wide status.

### C — User Stories

Inspect:

- `sdlc_docs/01_requirements/01_user_stories.md`
- `sdlc_docs/01_requirements/02_traceability_matrix.md`

Confirm the current story version, active story identifiers, source-batch mappings, and document status. Draft stories mean Skill C has produced work but product approval is not yet complete.

### D — Product Readiness

Inspect `sdlc_docs/01_requirements/03_user_story_product_readiness.md`. Completion requires approval for the exact current user-story version and full active-story scope. Diagnostic or subset reviews do not complete the gate.

### E — Architecture and Design

Inspect:

- `sdlc_docs/02_architecture/00_architecture_overview.md`
- `sdlc_docs/02_architecture/01_story_architecture_map.md`
- relevant component documents and architecture decisions

Completion requires architecture approval for the exact product-approved story version. Draft architecture or an approval bound to an older story version is not complete.

### F — Technical Readiness

Inspect `sdlc_docs/01_requirements/04_user_story_technical_readiness.md`. Determine readiness per selected story and verify the exact story version, architecture version, and technical review identifier. Do not treat one ready story as project-wide readiness.

### G — Repository Issues

Inspect `sdlc_docs/03_implementation/00_repository_issue_registry.md` and, when available, the repository issue system. Completion requires verified issue mappings for the selected approved scope. Registry-only or issue-only state may require reconciliation.

### H — Implementation Planning

Inspect plans under `sdlc_docs/03_implementation/plans/`. Completion requires a current plan tied to selected issue identifiers, approved source versions, technical review, and codebase baseline. A plan may be complete while implementation itself remains unexecuted.

### Implementation Execution — External Stage

Skills A–K do not own implementation execution. Determine whether an exact commit, build, package, image, or implementation handoff exists. Without an exact artifact, Skill I may work in strategy mode but cannot complete execution evidence.

### I — Automated Testing and Verification

Inspect:

- `sdlc_docs/04_testing/00_testing_strategy.md`
- `sdlc_docs/04_testing/01_test_traceability.md`
- `sdlc_docs/04_testing/02_testing_results.md`

Completion requires results bound to an exact implementation artifact and environment. Strategy-only output is not execution completion. Verify integration, end-to-end, and regression applicability decisions.

### J — Stakeholder Validation and Acceptance

Inspect:

- `sdlc_docs/05_validation/00_validation_plan.md`
- `sdlc_docs/05_validation/01_acceptance_results.md`

Completion requires an authorized stakeholder disposition for the exact tested release candidate. Separate behavior results from waivers or acceptance decisions.

### K — Deployment Preparation

Inspect:

- `sdlc_docs/06_deployment/00_deployment_plan.md`
- `sdlc_docs/06_deployment/01_release_checklist.md`
- `sdlc_docs/06_deployment/02_rollback_plan.md`, when applicable

Completion requires an approved plan bound to the exact accepted release candidate and a named target environment. This does not prove deployment execution.

## Status Selection

For a project-level summary, show both:

- stage-level state;
- item-level exceptions, such as one story blocked while others are ready.

Choose the current stage according to the user's selected scope. Prefer the earliest invalid prerequisite over a later desired stage, but explain the routing instead of silently changing the user's objective.
