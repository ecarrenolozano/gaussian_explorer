---
name: c-create-user-stories
description: create traceable agile user stories from clarified requirement batches in sdlc_docs/01_requirements/00_raw_ideas.md. use after b-requirements-clarifier to select eligible PRDB batches, formulate independently valuable stories, write testable acceptance criteria, assign stable identifiers and evidence-based priority, update canonical story and traceability files, and enforce version-specific human approval before downstream planning.
---

# Create User Stories

## Purpose

Turn clarified requirement handoffs into independently valuable, testable user stories without reinterpreting raw requests or inventing requirements. Preserve traceability to each source batch, maintain stable identifiers and document history, and require human approval before downstream planning.

This skill consumes the output contract of `b-requirements-clarifier`; it does not replace requirements clarification.

## Governing Rules

Apply these rules throughout the workflow:

- Generate stories only from canonical batches marked `status: processed` with a clarified handoff.
- Treat `Ready` batches as eligible and `Partially ready` batches as conditionally eligible. Do not generate from `Not ready` batches.
- Preserve requester intent, source evidence, open questions, scope boundaries, and explicitly recorded assumptions.
- Do not invent actors, capabilities, benefits, behavior, constraints, assumptions, acceptance conditions, or priority.
- Describe user-visible outcomes, not architecture, implementation, technologies, APIs, databases, or technical layers.
- Keep story identifiers, source mappings, document history, and prior approved content stable.
- Treat every generated or modified version as `Draft` until that exact version is explicitly approved.
- Do not create repository issues, architecture, implementation plans, task breakdowns, test plans, or code.

When source state is malformed, duplicated, or contradictory, do not append or overwrite content. Report the inconsistency and the corrective action required.

## Canonical Files

Read these files in order:

1. `sdlc_docs/00_project_context/project_context.md`
2. `sdlc_docs/01_requirements/00_raw_ideas.md`
3. `sdlc_docs/01_requirements/01_user_stories.md`
4. `sdlc_docs/01_requirements/02_traceability_matrix.md`

Use `project_context.md` for project-level scope, terminology, and approved decisions. Use clarified handoffs in `00_raw_ideas.md` as the authoritative source for batch-specific story generation. Treat the last two files as persistent outputs and generation state.

If `project_context.md` is missing, stop unless the user supplies equivalent project context and explicitly designates it as current. If `00_raw_ideas.md` is missing, stop. If an output file is missing, create it from its template during Step 7.

## Core Workflow

1. Gather and validate sources.
2. Select eligible requirement batches.
3. Extract candidate user outcomes.
4. Formulate and split user stories.
5. Write acceptance criteria and validate quality.
6. Assign identifiers, feature groups, and priority.
7. Persist stories and traceability.
8. Record version status and enforce approval.

### 1. Gather and Validate Sources

Read the canonical files and record which are available. Verify that requirement-batch tags, story identifiers, source-batch registry entries, traceability rows, and revision versions are not malformed, duplicated, or inconsistent.

Do not modify files when state is inconsistent.

### 2. Select Eligible Requirement Batches

Read and follow `references/eligibility-and-batches.md`.

Process the user-selected eligible batch. If none is selected, process the earliest eligible batch in document order. Process one batch unless the user explicitly requests multiple batches.

### 3. Extract Candidate User Outcomes

From each selected handoff, extract only evidence-supported actors, goals, value, workflows, inputs, outputs, business rules, constraints, edge cases, acceptance expectations, explicit assumptions, and open questions.

Do not write story prose in this step. Do not combine unrelated batches.

### 4. Formulate and Split User Stories

Read and follow:

1. `references/story-writing.md`
2. `templates/agile-user-story-template.md`

Create separate stories for independently valuable user outcomes. For `Partially ready` batches, generate only outcomes whose core actor, behavior, value, and scope are supported; preserve material uncertainty and defer blocked outcomes.

### 5. Write Acceptance Criteria and Validate Quality

Read and follow `references/acceptance-and-validation.md`.

Write observable Given/When/Then scenarios, then validate every candidate before assigning an identifier or modifying files. Revise failed drafts or defer them when evidence is insufficient.

### 6. Assign Identifiers, Feature Groups, and Priority

Continue following `references/acceptance-and-validation.md`.

Assign identifiers only after validation. Group stories by user-facing feature and assign `MVP`, `Post-MVP`, `Deferred`, or `Unconfirmed` only when supported by evidence.

### 7. Persist Stories and Traceability

Read and follow these resources in order:

1. `references/persistence-and-traceability.md`
2. `templates/user-stories-file.md`
3. `templates/traceability-matrix.md`

Stage all changes before writing. Update `01_user_stories.md`, its source-batch registry, and `02_traceability_matrix.md` consistently. Preserve existing content and verify one traceability row per `(Story ID, Source Batch)` relationship.

### 8. Record Version Status and Enforce Approval

Read and follow `references/approval-gate.md`.

Any story addition, modification, reprioritization, deprecation, or new source relationship creates a new draft document version. Record approval only for the exact current version after explicit human approval. Block downstream planning while the current version is not approved.

## Boundary with Other Skills

Send raw, unprocessed, `Not ready`, or materially ambiguous requirements back to `b-requirements-clarifier`. Do not conduct a clarification interview inside this skill beyond identifying the blocking question.

The approved current version of `01_user_stories.md` is the downstream input for issue generation, architecture, and implementation planning. Do not silently continue into those stages.

## Resources

Load supporting files only at the workflow steps that reference them:

- `references/eligibility-and-batches.md`
- `references/story-writing.md`
- `references/acceptance-and-validation.md`
- `references/persistence-and-traceability.md`
- `references/approval-gate.md`
- `templates/agile-user-story-template.md`
- `templates/user-stories-file.md`
- `templates/traceability-matrix.md`
