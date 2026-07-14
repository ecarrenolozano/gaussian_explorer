---
name: e-architecture-and-design
description: create or evolve versioned, mermaid-first software architecture from the exact product-approved user-story version. use after d-user-story-product-readiness to define clear system boundaries, responsibilities, major applications and services, components, interfaces, data ownership, deployment, story-to-architecture mapping, and architecture decisions; preserve architecture history and require version-specific human approval before technical-readiness review.
---

# Architecture and Design

## Purpose

Create the simplest architecture that satisfies the exact product-approved user-story version. Define system boundaries, responsibilities, data and interfaces, the necessary System Context, Container, and Component views from the C4 model, and important architecture decisions. Record version-specific architecture approval before technical-readiness review.

Use Mermaid as the primary diagramming notation. Allow optional tools selected by the architect without making them workflow dependencies. Evolve existing architecture incrementally. Do not reinterpret product requirements or continue into implementation design.

## Governing Rules

- Require valid product approval from `d-user-story-product-readiness` for the exact current story version.
- Treat project context, approved stories, traceability, and the product-readiness report as authoritative inputs.
- Preserve product behavior, scope, user-story identifiers, traceability, architecture versions, accepted architecture decisions, and decision history.
- Separate confirmed architecture drivers, technical proposals, explicit assumptions, risks, and open questions.
- Prefer the least complex architecture that satisfies supported behavior and quality constraints.
- Use the C4 model only through the Component view by default. Do not define classes, methods, source-code modules, or task-level implementation details.
- Refer to architecture elements by clear human-readable names. Do not impose shortened identifiers, code names, module names, package names, service names, or filenames on the implementation.
- Use Mermaid for required architecture diagrams.
- Treat external modeling tools and formats as optional supporting material. Never require a specific external tool for architecture completion or approval.
- Record consequential technical choices as architecture decision records. Never use an architecture decision record to invent a product decision.
- Stop when approval or version information is missing, stale, malformed, duplicated, or contradictory.
- Record architecture approval only for the exact architecture version and source-story version.

## Canonical Files

Read in this order:

1. `sdlc_docs/00_project_context/project_context.md`
2. `sdlc_docs/01_requirements/01_user_stories.md`
3. `sdlc_docs/01_requirements/02_traceability_matrix.md`
4. `sdlc_docs/01_requirements/03_user_story_product_readiness.md`
5. Existing files under `sdlc_docs/02_architecture/`

Create or update:

- `sdlc_docs/02_architecture/00_architecture_overview.md`
- `sdlc_docs/02_architecture/01_story_architecture_map.md`
- `sdlc_docs/02_architecture/components/<clear-component-name>/architecture.md` when internal structure matters
- `sdlc_docs/02_architecture/decisions/architecture-decision-NNN-short-title.md` for important architecture decisions

Documentation names must be clear to readers and must not prescribe implementation names. Optional architect-selected modeling artifacts may be stored according to repository conventions. Do not create tool-specific directories or files unless an architect explicitly requests them or an established project convention requires them. Treat older architecture files as historical evidence, not current approval, until their version and source binding are validated.

## Core Workflow

1. Gather and validate approved inputs.
2. Extract architecture drivers and select views.
3. Establish the architecture scope and evolution plan.
4. Design or update the architecture model.
5. Define components, data, interfaces, deployment, and cross-cutting concerns.
6. Map stories and record architecture decisions.
7. Persist and validate the architecture package.
8. Record or verify architecture approval.

### 1. Gather and Validate Approved Inputs

Read and follow `references/input-and-version-gate.md`. Identify the exact current story version, verify its product approval, inspect existing architecture state, and determine whether this run creates, revises, reassesses, or approves architecture. Do not treat approval recorded by another skill as architecture approval.

### 2. Extract Architecture Drivers and Select Views

Read `references/drivers-and-views.md`. Extract only supported functional responsibilities, quality scenarios, constraints, data concerns, external dependencies, operational context, and architecture risks. Select only views that answer important stakeholder or implementation questions.

### 3. Establish the Architecture Scope and Evolution Plan

Define the system of interest, existing-state evidence, target scope, neighboring systems, and change boundaries. Reuse valid architecture elements and documents. Plan incremental updates instead of rewriting unchanged architecture.

### 4. Design or Update the Architecture Model

Read `references/modeling-and-diagrams.md`. Define people, systems, major independently running applications or services, components, relationships, and any necessary interaction, deployment, or data views. Use clear human-readable names throughout. Create every required diagram in Mermaid. Include external modeling artifacts only by explicit architect or project choice; they remain supporting material unless repository policy states otherwise.

### 5. Define Components, Data, Interfaces, Deployment, and Cross-Cutting Concerns

Document cohesive responsibilities, provider and consumer boundaries, data ownership and lifecycle, critical workflows, deployment context, trust boundaries, failure behavior, observability, and supported quality attributes. Create component documents only for major applications, services, or components whose internal collaboration matters.

### 6. Map Stories and Record Architecture Decisions

Map every active story in the approved version using `templates/story-architecture-map.md`. Read `references/architecture-decision-rules.md` and create or supersede architecture decision records only for consequential decisions. Route missing product decisions upstream instead of encoding them as technical assumptions.

### 7. Persist and Validate the Architecture Package

Read `references/persistence-and-versioning.md`. Load templates only for files being created or repaired. Stage all changes, assign one architecture version to the complete package, validate consistency and story coverage across files, then write all related changes together when possible.

### 8. Record or Verify Architecture Approval

Read `references/approval-gate.md` when approval is requested or before technical-readiness review. Approve only architecture assessed as ready, bound to the exact current source-story version, and explicitly approved by a known human. A newer story version, architecture version, or assessment makes earlier approval stale.

## Boundary with Other Skills

- Route missing or conflicting product decisions to `b-requirements-clarifier` through the affected requirement batch.
- Route story wording, splitting, acceptance criteria, priority, registry, or traceability changes to `c-create-user-stories`, then require a new product review by `d-user-story-product-readiness`.
- Do not perform product-readiness approval, technical story readiness, issue publication, implementation planning, test planning, or coding.
- Proceed to `f-user-story-technical-readiness` only after valid architecture approval for the exact architecture and story versions.

## Resources

Load only when referenced by the workflow:

- `references/input-and-version-gate.md`
- `references/drivers-and-views.md`
- `references/modeling-and-diagrams.md`
- `references/architecture-decision-rules.md`
- `references/persistence-and-versioning.md`
- `references/approval-gate.md`
- `templates/architecture-overview.md`
- `templates/story-architecture-map.md`
- `templates/component-architecture.md`
- `templates/architecture-decision.md`
