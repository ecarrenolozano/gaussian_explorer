---
name: e-architecture-and-design
description: create or evolve versioned software architecture from the exact product-approved user-story version. use after d-user-story-product-readiness to document the architecture with a compact arc42 structure, model c4 views in structurizr dsl, organize containers and significant components, add selective code-level design, maintain architecture decisions and story-to-code traceability, validate the architecture package, and require version-specific human approval before technical-readiness review.
---

# Architecture and Design

## Purpose

Create the simplest and scalable architecture that satisfies the exact product-approved user-story version and gives stakeholders and developers a navigable path from goals and constraints to runtime structure, deployment, significant design, and implementation locations.

Use arc42 as the documentation structure, the C4 model for architecture views, Structurizr DSL as the canonical C4 model, exported SVG or PNG files for static documentation, and separate architecture decision records for significant choices. Keep the package compact: one main architecture document, one traceability file, one diagram workspace, selective container or component detail, and separate decisions.

## Governing Rules

- Require valid product approval from `d-user-story-product-readiness` for the exact current story version.
- Treat project context, approved stories, traceability, and the product-readiness report as authoritative inputs.
- Use `00_architecture_document.md` as the canonical architecture narrative organized by the twelve arc42 sections.
- Use `diagrams/workspace.dsl` as the canonical C4 model for people, software systems, containers, components, relationships, dynamic views, and deployment views.
- Keep the Structurizr viewer configuration and generated C4 images under `diagrams/` so diagram sources, tooling, and exports remain together.
- Treat exported files under `diagrams/images/` as generated documentation artifacts. Never edit an exported diagram manually; update `workspace.dsl` and export again.
- Prefer SVG for architecture documentation because it scales cleanly. Use PNG when the documentation renderer or delivery format does not support SVG reliably.
- Include exported diagrams in `00_architecture_document.md` with relative Markdown image paths. Do not embed an image that is missing, stale, or exported from a different architecture version.
- Use the C4 System Context view in arc42 section 3, Container and selected Component views in section 5, Dynamic views in section 6, and Deployment views in section 7.
- Create System Context and Container views by default. Add Component, Dynamic, Deployment, or Code-level views only when they answer a material question.
- Represent frontend applications, backend applications, workers, databases, caches, brokers, file stores, and other independently running applications or data stores as containers.
- Place every component inside its owning application container. Do not maintain a flat component catalog that hides ownership.
- Model databases and similar stores as containers; document internal data design in `data-model.md` instead of inventing application components.
- Create detailed container, component, or data-model documents only when the information would make the main architecture document hard to navigate or the design is architecturally significant.
- Use Mermaid only for supplementary class, sequence, state, package, or data diagrams that do not duplicate the canonical C4 model.
- Use clear human-readable architecture names. Structurizr identifiers are internal references only and must not become module names, package names, service names, class names, or filenames.
- Record implementation mappings as `confirmed`, `proposed`, `planned`, or `not-mapped`; never present a proposed path as an approved code structure.
- Record consequential technical choices as architecture decisions. Do not use architecture decisions to invent product behavior.
- For every arc42 section, document relevant information, state `Not applicable` with a reason, or mark unresolved information as open. Do not add filler.
- Preserve existing approved architecture that remains valid and evolve it incrementally.
- Bind the architecture document, C4 workspace, exported diagrams, traceability, detailed designs, decisions, assessment, and approval to the same architecture version.
- Stop when upstream approval, version, or architecture state is missing, stale, malformed, duplicated, or contradictory.

## Canonical Files

Read in this order:

1. `sdlc_docs/00_project_context/project_context.md`
2. `sdlc_docs/01_requirements/01_user_stories.md`
3. `sdlc_docs/01_requirements/02_traceability_matrix.md`
4. `sdlc_docs/01_requirements/03_user_story_product_readiness.md`
5. Existing files under `sdlc_docs/02_architecture/`

Create or update:

- `sdlc_docs/02_architecture/00_architecture_document.md`
- `sdlc_docs/02_architecture/01_architecture_traceability.md`
- `sdlc_docs/02_architecture/diagrams/workspace.dsl`
- `sdlc_docs/02_architecture/diagrams/docker-compose.yml`
- `sdlc_docs/02_architecture/diagrams/images/`
- `sdlc_docs/02_architecture/diagrams/images/<exported-view>.svg` or `.png` for selected views
- `sdlc_docs/02_architecture/containers/<container-name>/README.md` when container detail should be separated
- `sdlc_docs/02_architecture/containers/<container-name>/components/<component-name>.md` when significant internal design is justified
- `sdlc_docs/02_architecture/containers/<data-store-name>/data-model.md` when data design matters
- `sdlc_docs/02_architecture/decisions/README.md`
- `sdlc_docs/02_architecture/decisions/architecture-decision-NNN-short-title.md` when a significant decision is required

When legacy `workspace.dsl` or `docker-compose.yml` files exist directly under `02_architecture/`, move their maintained content into `02_architecture/diagrams/` and update references. Do not keep duplicate current diagram sources.

When a legacy `00_architecture_overview.md` exists and the new document does not, use it as migration input, create `00_architecture_document.md`, preserve meaningful history, and do not maintain both files as current sources.

Documentation folder names support navigation only. They do not prescribe implementation names.

## Core Workflow

### 1. Gather and Validate Approved Inputs

Read `references/input-and-version-gate.md`. Verify the exact current story version and product approval. Inspect existing architecture and classify the run as `create`, `evolve`, `reassess`, `migrate`, or `approve`.

### 2. Establish the arc42 Documentation Scope

Read `references/arc42-c4-and-structurizr.md`. Extract supported stakeholders, goals, quality goals, constraints, context, solution ideas, runtime behavior, deployment needs, cross-cutting concepts, decisions, risks, debt, and terminology. Tailor each section to project size and risk.

### 3. Build or Update the Canonical C4 Model

Model people, external systems, the software system, containers, significant components, and labelled relationships in `diagrams/workspace.dsl`. Create System Context and Container views by default. Add selected Component, Dynamic, and Deployment views only when they add value.

Before adding Dynamic or Deployment views, follow the Structurizr guardrails in `references/arc42-c4-and-structurizr.md`. In particular: scope Dynamic views to the lowest element that owns every referenced element, define every relationship used in a Dynamic view in the model first, and define deployment nodes under a `deploymentEnvironment` in the model before creating the Deployment view.

### 4. Export and Register Selected C4 Diagrams

Export the selected views from `diagrams/workspace.dsl` into `diagrams/images/`, preferably as SVG. Use the actual generated filenames, record the view key and export status, and verify that every embedded image represents the current architecture version. When PNG or SVG export tooling is unavailable, record the limitation and do not create or reference a placeholder image.

### 5. Document the arc42 Architecture Narrative

Update `00_architecture_document.md` so the C4 model, exported diagrams, and supporting prose tell one consistent story. Embed current exported images in their relevant arc42 sections and link each image to its Structurizr view key and canonical workspace. Link to detailed files instead of copying the same information into several places.

### 6. Document Container Ownership and Significant Design

Create container folders only for significant runtime units. Place component documents beneath the owning container. Add selective code-level design when internal collaboration, interfaces, state, domain relationships, concurrency, failure handling, or risk requires shared understanding.

### 7. Record Runtime, Deployment, and Cross-Cutting Concerns

Document important runtime scenarios, failure and recovery flows, deployment topology, security, configuration, observability, error handling, data management, testing strategy, and other recurring concepts only to the depth justified by the system.

### 8. Create Architecture Traceability

Read `references/design-traceability-and-decisions.md`. Map every active story to the relevant arc42 concern, C4 software system, owning container, component or data model, runtime or deployment concern, implementation location, mapping status, and architecture decisions.

### 9. Record Architecture Decisions

Create or supersede a decision only when a choice has significant, long-lived consequences. Include context, drivers, options, decision, consequences, validation, related stories, and affected architecture elements.

### 10. Persist and Validate the Architecture Package

Read `references/persistence-review-and-approval.md`. Update the main document, traceability, workspace, exported images, selected detailed documents, and decisions as one architecture version. Validate links, story coverage, arc42 completeness, C4 hierarchy, Docker Compose syntax, Structurizr rendering, image exports, and Markdown image references when tools are available.

Do not treat `docker compose config` as Structurizr DSL validation. It validates only Docker Compose syntax. When Docker is available, start or restart the Structurizr viewer and check fresh logs for `StructurizrDslParserException` before marking Structurizr rendering as validated.

### 11. Record or Verify Architecture Approval

Approve only an architecture assessed as ready, bound to the exact current story version, and explicitly approved by a known human. A semantic architecture change, newer source story version, changed view, or stale exported image makes earlier approval stale.

## Boundary with Other Skills

- Route missing or conflicting product decisions to `b-requirements-clarifier` through the affected requirement batch.
- Route story wording, splitting, acceptance, priority, or traceability changes to `c-create-user-stories`, followed by `d-user-story-product-readiness`.
- Let `f-user-story-technical-readiness` assess whether each story is implementable within the approved architecture.
- Let `h-implementation-planning` define exact files, coding sequence, and issue-specific implementation details.
- Do not publish issues, write implementation plans, create tests, or implement code.

## Resources

Load only when referenced:

- `references/input-and-version-gate.md`
- `references/arc42-c4-and-structurizr.md`
- `references/design-traceability-and-decisions.md`
- `references/persistence-review-and-approval.md`
- `templates/architecture-document.md`
- `templates/architecture-traceability.md`
- `templates/workspace.dsl`
- `templates/docker-compose.yml`
- `templates/container-readme.md`
- `templates/component-design.md`
- `templates/data-model.md`
- `templates/decisions-readme.md`
