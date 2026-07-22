---
name: h-implementation-planning
description: create and maintain living dependency-aware implementation roadmaps, planning batches, and versioned implementation plans for canonical repository tracker issues linked to technically approved stories or spike candidates. Use after repository issue publication and reconciliation when Codex must reject untriaged tracker intake from GitHub, GitLab, GitKraken, or other platforms, organize approved issue order, shard large issue sets, define exact code-level design with standard Mermaid UML diagrams and explicitly labeled supplemental diagrams, plan safe parallel assignment, developer tests, dependencies, verification, and explicit routes for story, architecture, or reconciliation changes.
---

# Implementation Planning

## Purpose

Translate approved repository work items into an actionable living implementation roadmap and issue plans that realize the approved architecture in the current codebase.

Bridge architecture and code by first organizing canonical published issues into dependency-aware waves for safe assignment, then following the path from the relevant arc42 concerns and C4 architecture to the owning container, component or data model to define the exact files, structures, diagrams, tasks, and developer tests required for the selected issue.

## Governing Rules

- Plan only canonical issues linked to technically approved stories or approved spike candidates.
- Reject untriaged, duplicate, similar-existing-scope, intake-only, or contributor-created tracker issues that lack approved lineage. Route them to Skill G reconciliation.
- Preserve approved product behavior, constraints, container ownership, component responsibilities, runtime flows, public interfaces, data ownership, deployment boundaries, cross-cutting concepts, quality scenarios, risks, and architecture decisions.
- Inspect the real codebase and tests before proposing implementation structure.
- Do not derive module, package, class, service, image, resource, or filename conventions automatically from architecture document names.
- Treat `confirmed` architecture mappings as evidence, `proposed` mappings as suggestions to review, `planned` mappings as accepted but unimplemented, and `not-mapped` entries as unresolved.
- Add issue-specific code design here, including standard UML diagrams in Mermaid syntax for non-trivial work. Use UML class, sequence, and state diagrams where those concerns apply; do not replace code-level UML with improvised box diagrams. Route reusable or architecturally significant design changes back to skill e-architecture-and-design.
- Define only the detail needed to implement and review the selected work.
- Maintain the roadmap incrementally across planning batches. Do not overwrite planning history when new informal requests later become approved stories and canonical issues.
- Do not record sprint estimates, sprint counts, sprint plans, sprint capacity, or calendar commitments.
- Do not publish issues, change approved stories or architecture, or implement code by default.

## Canonical Files

Read:

- `sdlc_docs/01_requirements/01_user_stories.md`
- `sdlc_docs/01_requirements/04_user_story_technical_readiness.md`
- `sdlc_docs/02_architecture/00_architecture_document.md`
- `sdlc_docs/02_architecture/01_architecture_traceability.md`
- `sdlc_docs/02_architecture/workspace.dsl`
- relevant files under `sdlc_docs/02_architecture/containers/`
- relevant files under `sdlc_docs/02_architecture/decisions/`
- `sdlc_docs/03_implementation/00_repository_issue_registry.md`
- reconciliation reports under `sdlc_docs/03_implementation/intake_reconciliation/`, when relevant
- selected repository issues, current codebase, tests, dependencies, and repository conventions

Create or refresh the roadmap at `sdlc_docs/03_implementation/01_implementation_roadmap.md`.

Create planning batches under `sdlc_docs/03_implementation/planning_batches/` for new sets of approved issues. For small legacy projects, existing flat `sdlc_docs/03_implementation/plans/` files may be read, but new large or incremental planning should use batch folders.

Maintain indexes under `sdlc_docs/03_implementation/indexes/` when the plan set is large enough that navigation or reconciliation would otherwise be error-prone.

## Core Workflow

### 1. Validate Planning Scope

Read `references/input-and-version-gate.md`. Confirm issue identifiers, source stories, story version, architecture version, technical review, repository revision, architecture path, and relevant arc42 concerns.

If an issue is missing approved lineage markers, maps to a reconciliation class such as `duplicate`, `similar-existing-scope`, `new-requirement-candidate`, or `needs-human-review`, or was created directly in a repository tracker without canonicalization, stop planning that issue and route to Skill G.

### 2. Create or Refresh the Living Implementation Roadmap

Read `references/roadmap-and-dependencies.md`. Use published issue mappings, story priority, technical-readiness dependencies, architecture runtime flow, component ownership, and current codebase evidence to organize issues into dependency-aware waves, safe parallel assignment guidance, Kanban status, sequencing risks, and open questions.

For new approved issue sets, append a planning batch entry and update the current roadmap view. Preserve previous batch history.

### 3. Inspect Current Implementation Context

Inspect relevant code, tests, dependencies, configuration, migrations, observability, and conventions. Identify reusable structures and existing implementation locations.

### 4. Follow the Architecture Path

Map the issue through architecture goals and constraints, software system, owning container, component or data model, runtime scenario, deployment context, cross-cutting concepts, quality scenarios, decisions, risks, and current mapping status. Do not plan work in the wrong frontend, backend, worker, database, or infrastructure boundary.

### 5. Define Code-Level Design and UML Diagrams

Read `references/code-level-design.md`. Define exact modules, classes, functions, schemas, algorithms, interfaces, configuration, observability, and files only when supported by repository evidence or clearly marked as proposed implementation choices.

For non-trivial issues, include code-level UML diagrams in Mermaid syntax. Use `classDiagram` for classes, dataclasses, DTOs, result objects, exceptions, services, and their relationships; `sequenceDiagram` for runtime collaborations; and `stateDiagram-v2` for workflow, session, or lifecycle states. Use supplemental non-UML diagrams only for algorithms, data flow, or module dependency sketches that are not naturally expressed as UML, and label them explicitly as supplemental.

When a design changes system or container boundaries, component responsibilities, shared interfaces, data ownership, runtime behavior, deployment, cross-cutting strategy, quality tactics, or a reusable cross-issue design, stop and route it to skill e-architecture-and-design.

### 6. Plan Incremental Implementation and Developer Tests

Read `references/tdd-and-verification.md`. Create small reviewable increments. For each increment, record the architecture element, arc42 concern, affected files, change, developer tests, verification, dependencies, and completion condition.

### 7. Plan Data, Configuration, Migration, and Operations

Tie data changes to the owning data-store container and data model. Define migrations, compatibility, configuration, secret references, logging, metrics, tracing, feature controls, and recovery needs without inventing unknown commands or environment values.

### 8. Record Risks and Change Routes

Record blockers, external dependencies, unresolved design questions, rollout concerns, quality risks, and any route back to requirements, stories, or architecture.

### 9. Persist and Assess the Plan

Read `references/persistence-and-readiness.md`. Bind the plan to exact upstream versions, issue IDs, repository revision, architecture scope, and plan version. Preserve history and record readiness.

## Boundary with Other Skills

- Skill e-architecture-and-design owns reusable architecture, arc42 content, C4 views, container and component boundaries, runtime and deployment design, cross-cutting concepts, quality tactics, and architecture decisions.
- Skill H owns issue ordering guidance, safe parallel assignment guidance, exact issue-specific code changes, implementation sequence, developer tests, and local design detail.
- Skill I owns broader automated integration, end-to-end, regression, and release-level verification.
- Route product or acceptance changes to Skills B, C, and D.
- Do not implement code or claim implementation completion.

## Resources

- `references/input-and-version-gate.md`
- `references/roadmap-and-dependencies.md`
- `references/code-level-design.md`
- `references/tdd-and-verification.md`
- `references/persistence-and-readiness.md`
- `templates/implementation-roadmap.md`
- `templates/planning-batch-summary.md`
- `templates/implementation-plan.md`
