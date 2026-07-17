---
name: c-create-user-stories
description: Create and revise traceable agile user stories from clarified requirement batches, while auditing requirement completeness, separating user outcomes from non-functional requirements and solution assumptions, and recording unresolved product or technology decisions. Use after requirements clarification when ChatGPT must generate or update user stories, detect missing workflows and acceptance boundaries, challenge unverified implementation choices such as a requested framework, maintain coverage and traceability, and enforce version-specific approval before downstream planning.
---

# Create User Stories

## Purpose

Turn clarified requirements into independently valuable, testable user stories while preserving source evidence and exposing gaps that should not be hidden inside vague stories.

Do not assume that every sentence in a request belongs in a user story. Classify source statements first, then produce the appropriate artifact:

- user outcome -> user story;
- business rule or validation behavior -> acceptance criteria or supporting requirement;
- quality attribute -> non-functional requirement and acceptance measure;
- implementation suggestion or technology choice -> decision item unless already approved;
- unresolved ambiguity -> open question;
- research or comparison work -> discovery/decision item, not a user story.

This skill consumes the clarified output of `b-requirements-clarifier`; it does not replace clarification.

## Governing Rules

- Generate stories only from canonical batches marked `status: processed` with a clarified handoff.
- Treat `Ready` batches as eligible and `Partially ready` batches as conditionally eligible. Do not generate from `Not ready` batches.
- Preserve requester intent, source evidence, open questions, scope boundaries, and explicit assumptions.
- Never silently promote a requested technology, architecture, or framework into a confirmed requirement.
- Do not invent actors, user value, behavior, constraints, assumptions, acceptance conditions, or priority.
- Describe user-visible outcomes in stories; keep technical evaluation, architecture, and implementation work in decision items.
- Require every source statement to be accounted for by a story, NFR, decision item, open question, explicit exclusion, or duplicate mapping.
- Treat every generated or modified version as `Draft` until that exact version is explicitly approved.
- Do not create repository issues, architecture, implementation plans, test plans, or code.

Stop without modifying files when canonical state is malformed, duplicated, contradictory, or too incomplete to support the requested output.

## Canonical Files

Read in this order:

1. `sdlc_docs/00_project_context/project_context.md`
2. `sdlc_docs/01_requirements/00_raw_ideas.md`
3. `sdlc_docs/01_requirements/01_user_stories.md`
4. `sdlc_docs/01_requirements/02_traceability_matrix.md`
5. `sdlc_docs/01_requirements/03_decision_backlog.md`
6. `sdlc_docs/01_requirements/04_requirement_coverage.md`

The last four are persistent outputs and generation state. Create missing output files from templates during persistence.

## Core Workflow

1. Gather and validate sources.
2. Select eligible requirement batches.
3. Classify every source statement and audit coverage.
4. Audit solution assumptions and unresolved decisions.
5. Extract candidate user outcomes and completeness gaps.
6. Formulate and split user stories.
7. Write acceptance criteria and validate quality.
8. Assign identifiers, feature groups, and evidence-based priority.
9. Persist stories, decisions, coverage, and traceability.
10. Record version status and enforce approval.

### 1. Gather and Validate Sources

Read the canonical files and verify batch tags, story identifiers, decision identifiers, registries, traceability rows, coverage rows, and revision versions. Do not modify files when state is inconsistent.

### 2. Select Eligible Requirement Batches

Read `references/eligibility-and-batches.md`. Process the user-selected eligible batch, otherwise the earliest eligible batch. Process one batch unless multiple are explicitly requested.

### 3. Classify Every Source Statement and Audit Coverage

Read `references/requirement-classification-and-coverage.md`.

Classify each meaningful source statement before drafting stories. Build a provisional coverage list showing how each statement will be handled. Do not let broad phrases such as “sensible defaults,” “reproduce later,” “modular,” or “use Streamlit” pass without classification and a concrete disposition.

### 4. Audit Solution Assumptions and Decisions

Read `references/solution-assumptions-and-decisions.md`.

For every proposed technology, framework, architecture, storage approach, or algorithmic choice, determine whether it is:

- an approved constraint;
- a requester preference;
- an unverified assumption;
- a decision already supported by project context;
- a decision requiring evaluation.

Create or update a decision item when evaluation is required. Do not disguise a technical spike as a user story.

### 5. Extract Candidate User Outcomes and Completeness Gaps

From each selected handoff, extract evidence-supported actors, goals, value, workflows, inputs, outputs, state transitions, model or data lifecycle, business rules, constraints, failure behavior, quality attributes, assumptions, and open questions.

Apply the completeness lenses in `references/requirement-classification-and-coverage.md`. These lenses reveal questions; they do not authorize invention.

### 6. Formulate and Split User Stories

Read:

1. `references/story-writing.md`
2. `templates/agile-user-story-template.md`

Create separate stories for independently valuable outcomes. Avoid one broad “configure” story when the source supports materially different behaviors such as selecting a model family, exposing family-specific controls, toggling optimization, inspecting fitted values, or using the fitted model for inference.

### 7. Write Acceptance Criteria and Validate Quality

Read `references/acceptance-and-validation.md`.

Write observable Given/When/Then scenarios. Cover the primary path and all supported state, validation, alternate, and boundary behavior. Revise or defer candidates that fail validation.

### 8. Assign Identifiers, Feature Groups, and Priority

Continue following `references/acceptance-and-validation.md`. Assign identifiers only after validation. Group by user-facing feature. Assign priority only from evidence.

### 9. Persist Stories, Decisions, Coverage, and Traceability

Read in order:

1. `references/persistence-and-traceability.md`
2. `templates/user-stories-file.md`
3. `templates/traceability-matrix.md`
4. `templates/decision-backlog.md`
5. `templates/requirement-coverage.md`

Stage all updates before writing. Keep all persistent files mutually consistent. Every source statement must have one coverage disposition.

### 10. Record Version Status and Enforce Approval

Read `references/approval-gate.md`. Any content change creates a new draft version. Record approval only for the exact current version after explicit human approval.

## Boundary with Other Skills

Return raw, unprocessed, `Not ready`, or materially ambiguous requirements to `b-requirements-clarifier`.

Decision items identify what must be evaluated and the decision criteria. They do not perform architecture selection. Route the actual comparison or ADR to the appropriate architecture or research workflow.

The approved current user-story version is the downstream input for issue generation, architecture, and implementation planning. Do not silently continue into those stages.

## Resources

Load only when referenced by the workflow:

- `references/eligibility-and-batches.md`
- `references/requirement-classification-and-coverage.md`
- `references/solution-assumptions-and-decisions.md`
- `references/story-writing.md`
- `references/acceptance-and-validation.md`
- `references/persistence-and-traceability.md`
- `references/approval-gate.md`
- `templates/agile-user-story-template.md`
- `templates/user-stories-file.md`
- `templates/traceability-matrix.md`
- `templates/decision-backlog.md`
- `templates/requirement-coverage.md`
