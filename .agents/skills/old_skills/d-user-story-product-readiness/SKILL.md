---
name: d-user-story-product-readiness
description: review the current user-story document version against clarified PRDB handoffs and the requirements traceability matrix. use after c-create-user-stories to verify product-level fidelity, coverage, scope, assumptions, and observable acceptance behavior; route requirement gaps to b-requirements-clarifier and story corrections to c-create-user-stories; and record version-specific product approval before architecture work.
---

# User Story Product Readiness

## Purpose

Independently verify that the current user-story version faithfully represents its clarified requirement batches. Identify product-level defects, missing coverage, unsupported behavior, and unresolved decisions, then record version-specific product approval before architecture work.

Review stories without rewriting them, repeating requirements clarification, or assessing implementation feasibility.

## Governing Rules

- Treat project context and clarified PRDB handoffs as authoritative product evidence.
- Review the exact current story version and all active stories for an approval-gate review.
- Verify fidelity, coverage, scope, user-visible behavior, and acceptance conditions without inventing decisions.
- Preserve identifiers, lineage, versions, history, and prior approvals.
- Do not edit stories, handoffs, or traceability; report defects and route them to the owning skill.
- Keep product findings separate from architecture and implementation signals.
- Record product approval only in this skill's report and only for the exact reviewed version.
- Stop on malformed, duplicated, stale, missing, or contradictory source state.

## Canonical Files

Read in this order:

1. `sdlc_docs/00_project_context/project_context.md`
2. `sdlc_docs/01_requirements/01_user_stories.md`
3. `sdlc_docs/01_requirements/02_traceability_matrix.md`
4. Matching clarified batches in `sdlc_docs/01_requirements/00_raw_ideas.md`
5. `sdlc_docs/01_requirements/03_user_story_product_readiness.md`

Use active story metadata and traceability to identify PRDB IDs, then read only those batch sections from `00_raw_ideas.md`.

Stop when project context, user stories, traceability, or a referenced clarified handoff is missing. Route the gap to its owner. Create the output report from its template when absent. Treat legacy `03_user_story_readiness.md` as read-only history, not approval evidence.

## Core Workflow

1. Gather and validate review state.
2. Establish the review scope.
3. Assess lineage, coverage, and product readiness.
4. Apply relevant product-domain overlays.
5. Determine assessment and routing.
6. Persist the report.
7. Record or verify product approval.

### 1. Gather and Validate Review State

Read existing canonical files. Identify the current content version as the highest `Generated` or `Revised` version in `01_user_stories.md`. Validate story IDs and metadata, lifecycle values, registry markers, traceability relationships, document status, and revision history. Do not modify inconsistent artifacts.

### 2. Establish the Review Scope

A full-gate review includes every active story in the current version and every referenced source batch. A selected subset may receive a diagnostic review but cannot receive approval.

Record review mode, story version, active IDs, source batches, and project categories. Load only relevant project-context sections and clarified handoffs.

### 3. Assess Lineage, Coverage, and Product Readiness

Read and follow `references/review-rules.md`.

Compare active stories and traceability against their clarified handoffs. Evaluate each story using evidence, record findings and severity, and identify represented, deferred, duplicated, contradicted, or missing source outcomes. Do not silently repair content.

### 4. Apply Relevant Product-Domain Overlays

Read `references/category-selection.md`, then load only the selected `references/overlay-*.md` files. Apply product-facing concerns only; do not require technical design.

### 5. Determine Assessment and Routing

Continue following `references/review-rules.md`. Assign per-story and overall assessments using the least-ready applicable result. Route source gaps to `b-requirements-clarifier`, story defects to `c-create-user-stories`, and non-product technical signals downstream.

### 6. Persist the Report

Read `references/persistence.md`. Load `templates/product-readiness-report.md` only when creating the report or repairing missing structure.

Create or update `03_user_story_product_readiness.md`, preserving prior version reviews and decision history. Every new assessment resets the reviewed version's human decision to pending.

### 7. Record or Verify Product Approval

Read `references/approval-gate.md` when approval is requested or before architecture work.

Approve only a full-gate review whose latest overall assessment is `product-ready`. Bind approval to the exact current story version and a known human approver. A newer story version or assessment makes earlier approval stale.

## Boundary with Other Skills

- Return source ambiguity, contradictions, or missing product decisions to `b-requirements-clarifier`.
- Return story wording, splitting, acceptance criteria, priority, registry, or traceability corrections to `c-create-user-stories`.
- Do not create architecture, spikes, issues, implementation plans, test plans, or code.
- Proceed to `e-architecture-and-design` only after valid product approval for the exact current story version.

## Resources

Load only when referenced by the workflow:

- `references/review-rules.md`
- `references/category-selection.md`
- `references/overlay-*.md`
- `references/persistence.md`
- `references/approval-gate.md`
- `templates/product-readiness-report.md`
