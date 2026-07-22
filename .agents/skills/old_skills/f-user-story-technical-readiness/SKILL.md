---
name: f-user-story-technical-readiness
description: evaluate product-approved user stories against the exact approved architecture version to determine per-story implementation readiness and repository-publication eligibility. use after e-architecture-and-design to verify the relevant arc42 concerns, c4 system and container path, component or data-model ownership, runtime and deployment behavior, quality requirements, cross-cutting concepts, decisions, implementation mapping, dependencies, verification needs, and technical uncertainty; route defects to the owning skill and record version-bound technical approval.
---

# User Story Technical Readiness

## Purpose

Determine whether each reviewed story can be implemented and verified safely within the exact approved architecture version. Confirm that the architecture provides sufficient story-specific evidence from the arc42 document, C4 model, detailed design, decisions, and implementation mapping without redesigning the architecture.

## Governing Rules

- Require valid product approval for the exact story version and valid architecture approval bound to it.
- Review only active stories with stable identifiers and current traceability.
- Treat `01_architecture_traceability.md` as the primary story-to-architecture path and verify its referenced files.
- Require only arc42 sections relevant to the reviewed story. Do not reject a story because an unrelated section is brief or explicitly not applicable.
- Do not create or modify architecture goals, constraints, containers, components, runtime views, deployment views, cross-cutting concepts, data models, code-level design, quality scenarios, risks, or architecture decisions.
- Use repository and environment evidence without replacing canonical approvals.
- Distinguish requirement gaps, story defects, architecture changes, technical investigations, external blockers, and inconsistent artifact state.
- Assign one primary routing status per story.
- Bind each review and approval to exact story and architecture versions.
- Do not publish issues, create implementation plans, tests, or code.

## Canonical Files

Read in this order:

1. `sdlc_docs/00_project_context/project_context.md`
2. `sdlc_docs/01_requirements/01_user_stories.md`
3. `sdlc_docs/01_requirements/02_traceability_matrix.md`
4. `sdlc_docs/01_requirements/03_user_story_product_readiness.md`
5. `sdlc_docs/02_architecture/00_architecture_document.md`
6. `sdlc_docs/02_architecture/01_architecture_traceability.md`
7. `sdlc_docs/02_architecture/workspace.dsl`
8. Relevant container, component, data-model, and decision documents under `sdlc_docs/02_architecture/`
9. `sdlc_docs/01_requirements/04_user_story_technical_readiness.md`

Create the technical-readiness report from its template when absent.

## Core Workflow

### 1. Gather and Validate Upstream State

Read `references/input-and-version-gate.md`. Verify exact story and architecture versions, product and architecture approval, active story identifiers, and architecture package integrity.

### 2. Establish the Review Scope

Review all active stories by default or a user-selected subset. Assign a sequential `TR-XXX` review identifier and record reviewed story IDs, versions, evidence, and review mode.

### 3. Trace Each Story Through the Architecture

For every story, verify a path through relevant arc42 concerns, software system, owning container, component or data model, responsibility, runtime or deployment behavior, decisions, and implementation mapping. Confirm that referenced detailed documents exist when the design requires them.

### 4. Evaluate Technical Readiness

Read `references/technical-readiness-checklist.md`. Apply only relevant criteria. Record evidence, unknowns, severity, verification needs, mapping status, dependencies, and blockers.

### 5. Determine Status and Routing

Read `references/status-and-routing.md`. Assign one primary status, determine publication eligibility, and create a spike candidate only for decision-relevant uncertainty. Do not modify upstream artifacts.

### 6. Persist the Review

Read `references/persistence.md`. Append the review, update current gate state, preserve history, and verify version and story coverage before writing.

### 7. Record or Verify Technical Approval

Read `references/approval-gate.md`. Approve only stories assessed `implementation-ready`, bound to unchanged approved story and architecture versions, and explicitly approved by a known human.

## Boundary with Other Skills

- Route missing product decisions to `b-requirements-clarifier`, followed by story regeneration and product review.
- Route story defects to `c-create-user-stories`, followed by `d-user-story-product-readiness` and architecture impact review.
- Route missing or conflicting arc42 content, C4 views, containers, components, data design, runtime or deployment behavior, cross-cutting concepts, quality scenarios, risks, code-level design, decisions, or architecture mappings to `e-architecture-and-design`.
- Let `g-create-repository-issues` publish approved stories and spike candidates.
- Do not alter architecture, user stories, approvals, issues, plans, tests, or code.

## Resources

- `references/input-and-version-gate.md`
- `references/technical-readiness-checklist.md`
- `references/status-and-routing.md`
- `references/spike-rules.md`
- `references/persistence.md`
- `references/approval-gate.md`
- `templates/technical-readiness-report.md`
- `templates/technical-spike-candidate.md`
