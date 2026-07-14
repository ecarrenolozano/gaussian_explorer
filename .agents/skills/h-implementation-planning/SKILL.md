---
name: h-implementation-planning
description: create versioned implementation plans for technically approved repository work items using the approved user stories, architecture, current codebase, and tests. use after repository issue publication to define minimal code-level design, ordered implementation increments, test-driven-development guidance, migrations, dependencies, verification, and explicit routes for story or architecture changes.
---

# Implementation Planning

## Purpose

Translate approved repository work items into actionable, reviewable implementation plans that fit the current codebase and approved architecture.

## Governing Rules

- Plan only repository work items linked to technically approved stories or approved spike candidates.
- Preserve approved product behavior and architecture boundaries.
- Inspect the real codebase and tests before proposing code-level structure.
- Do not convert architecture labels into required module, package, class, service, or filename conventions.
- Define only the detail needed to implement and review the selected work.
- Route product, story, and architecture changes to their owning skills.
- Treat implementation-plan approval as conditional on project policy, risk, or explicit user request.

## Canonical Files

Read:

- `sdlc_docs/01_requirements/01_user_stories.md`
- `sdlc_docs/01_requirements/04_user_story_technical_readiness.md`
- `sdlc_docs/02_architecture/00_architecture_overview.md`
- `sdlc_docs/02_architecture/01_story_architecture_map.md`
- relevant component documents under `sdlc_docs/02_architecture/components/`
- relevant decisions under `sdlc_docs/02_architecture/decisions/`
- `sdlc_docs/03_implementation/00_repository_issue_registry.md`
- the current codebase, tests, and repository conventions

Create implementation plans under `sdlc_docs/03_implementation/plans/`.

## Core Workflow

### 1. Validate the Planning Scope

Confirm selected issue identifiers, source stories, current story version, architecture version, technical review, and repository revision. Stop when lineage or approval is stale or inconsistent.

Read `references/input-and-version-gate.md`.

### 2. Inspect the Current Implementation Context

Inspect relevant source code, tests, dependencies, configuration, migrations, and repository conventions. Identify reusable code and existing patterns before proposing new structure.

### 3. Map Work to Approved Architecture

Use the story-to-architecture map and component documents. Identify responsible architecture elements without redefining their responsibilities, interfaces, data ownership, or deployment boundaries.

### 4. Define the Minimum Code-Level Design

Describe only necessary internal changes, such as functions, classes, modules, data structures, algorithms, migrations, configuration, and error handling. Use names grounded in the existing codebase or clearly label proposed names as provisional implementation choices.

Read `references/code-level-design.md`.

### 5. Plan Incremental Implementation and Developer Tests

Order work into small, reviewable increments. For each increment, define the observable objective, affected code, dependencies, implementation change, verification, and tests. Use test-driven development where appropriate.

Read `references/tdd-and-verification.md`.

### 6. Identify Dependencies, Risks, and Change Routes

Record blockers, external dependencies, migrations, rollout concerns, and unanswered technical questions. Route requirement gaps to Skill B, story changes to Skill C and D, and architecture changes to Skill E.

### 7. Persist the Versioned Plan

Create one plan per issue or coherent issue group using `templates/implementation-plan.md`. Record the plan version and exact upstream versions. A material plan change creates a new plan version.

### 8. Assess Plan Readiness

Record `ready`, `ready-with-open-items`, `changes-required`, or `blocked`. Obtain human approval only when required by project policy, risk, complexity, or explicit instruction.

## Boundary with Other Skills

- Skill G publishes and reconciles repository issues.
- Skill H plans implementation but does not publish issues, change approved architecture, or implement code by default.
- Implementation execution produces the exact code revision or build consumed by Skill I.
- Skill I owns broader automated testing and verification.

## Resources

- `references/input-and-version-gate.md`
- `references/code-level-design.md`
- `references/tdd-and-verification.md`
- `references/persistence-and-readiness.md`
- `templates/implementation-plan.md`
