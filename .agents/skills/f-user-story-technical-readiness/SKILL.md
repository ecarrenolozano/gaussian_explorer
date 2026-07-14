---
name: f-user-story-technical-readiness
description: evaluate product-approved user stories against the exact approved architecture version to determine per-story implementation readiness and publication eligibility. use after e-architecture-and-design and before g-create-repository-issues to validate architecture paths, interfaces, data, dependencies, quality attributes, delivery, operations, verification, and technical uncertainty; route defects to the owning upstream skill and record version-bound technical approval.
---

# User Story Technical Readiness

## Purpose

Determine whether each reviewed user story can be implemented and verified safely within the exact approved architecture version. Identify technical blockers, required upstream changes, external dependencies, and genuine investigation needs, then record which stories are eligible for repository issue publication.

Assess readiness without rewriting stories, redesigning architecture, or publishing issues.

## Governing Rules

- Require valid product approval for the exact current story version and valid architecture approval bound to that version.
- Review only active stories with stable identifiers, traceability, and a current story-to-architecture mapping.
- Use story, architecture, repository, environment, and explicit team-standard evidence; do not invent contracts, thresholds, ownership, infrastructure, or test conditions.
- Distinguish requirement gaps, story defects, architecture changes, technical investigations, external blockers, and artifact-state failures.
- Assign one primary routing status per story and preserve secondary findings separately.
- Recommend story splitting or architecture changes without performing them.
- Define spike candidates only for decision-relevant uncertainty; do not disguise implementation as research.
- Preserve upstream artifacts, versions, identifiers, approvals, report history, and prior technical decisions.
- Bind every assessment and approval to exact story and architecture versions.
- Do not publish repository issues, create implementation plans, write test plans, or produce code.

## Canonical Files

Read in this order:

1. `sdlc_docs/00_project_context/project_context.md`
2. `sdlc_docs/01_requirements/01_user_stories.md`
3. `sdlc_docs/01_requirements/02_traceability_matrix.md`
4. `sdlc_docs/01_requirements/03_user_story_product_readiness.md`
5. `sdlc_docs/02_architecture/00_architecture_overview.md`
6. `sdlc_docs/02_architecture/01_story_architecture_map.md`
7. Relevant component documents and Architecture Decision Records under `sdlc_docs/02_architecture/`
8. `sdlc_docs/01_requirements/04_user_story_technical_readiness.md`

Use relevant repository, interface, environment, and team-standard evidence when available. Do not treat it as a substitute for canonical product or architecture approval.

Create the output report from its template when absent. Treat legacy `04_technical_readiness.md` as read-only history, not current approval evidence.

## Core Workflow

1. Gather and validate upstream state.
2. Establish the technical review scope.
3. Trace stories through the approved architecture.
4. Evaluate technical readiness.
5. Determine status, routing, dependencies, and spike candidates.
6. Persist the technical-readiness report.
7. Record or verify technical approval.

### 1. Gather and Validate Upstream State

Read and follow `references/input-and-version-gate.md`. Identify the exact current story and architecture versions, verify product and architecture approval, validate mapping and artifact integrity, and stop when state is stale or inconsistent.

### 2. Establish the Technical Review Scope

Review all active stories by default. Review a user-selected subset when requested. Assign a sequential `TR-XXX` review identifier and record the reviewed story IDs, upstream versions, available technical evidence, and review mode.

A selected review may approve implementation-ready stories independently when their dependencies permit. It does not approve unreviewed stories.

### 3. Trace Stories Through the Approved Architecture

For each reviewed story, follow the architecture mapping through responsible containers, components, interfaces, data, ADRs, deployment, and operational paths. Verify that references exist and identify any cross-story or external dependency.

### 4. Evaluate Technical Readiness

Read `references/technical-readiness-checklist.md`. Apply only relevant criteria and record evidence, unknowns, severity, verification needs, and blocking conditions. Do not re-run product discovery unless a technical finding exposes a missing product decision.

### 5. Determine Status, Routing, Dependencies, and Spike Candidates

Read `references/status-and-routing.md`. Assign one primary status to every reviewed story and determine publication eligibility. Read `references/spike-rules.md` only when genuine technical uncertainty requires investigation. Do not modify upstream artifacts.

### 6. Persist the Technical-Readiness Report

Read `references/persistence.md`. Load `templates/technical-readiness-report.md` only when creating or repairing the report. Load `templates/technical-spike-candidate.md` only when a spike candidate is needed.

Append a new review section and history row, preserve prior reviews, update the Current Gate marker, and verify report consistency before writing.

### 7. Record or Verify Technical Approval

Read `references/approval-gate.md` when approval is requested or before issue publication. Approve only stories assessed `implementation-ready`, bound to unchanged approved upstream versions, and explicitly approved by a known human. A newer review covering an approved story resets that story to pending; a newer story version, architecture version, or upstream approval state invalidates all affected technical approval.

## Boundary with Other Skills

- Route missing product decisions to `b-requirements-clarifier`, followed by `c-create-user-stories` and `d-user-story-product-readiness`.
- Route story wording, splitting, acceptance, priority, registry, or traceability changes to `c-create-user-stories`, then require product reapproval and architecture impact review.
- Route system-wide or cross-story architecture changes and ADRs to `e-architecture-and-design`.
- Recommend technical spike candidates here; let `g-create-repository-issues` publish approved spike or implementation issues.
- Do not alter product approval, architecture approval, user stories, architecture documents, repository issues, implementation plans, tests, or code.

## Resources

Load only when referenced by the workflow:

- `references/input-and-version-gate.md`
- `references/technical-readiness-checklist.md`
- `references/status-and-routing.md`
- `references/spike-rules.md`
- `references/persistence.md`
- `references/approval-gate.md`
- `templates/technical-readiness-report.md`
- `templates/technical-spike-candidate.md`
