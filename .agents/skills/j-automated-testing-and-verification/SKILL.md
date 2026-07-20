---
name: i-automated-testing-and-verification
description: plan, create, select, execute, and report automated technical verification for an exact implementation artifact. use after implementation to derive integration, end-to-end, regression, performance, security, reliability, migration, recovery, and other applicable tests from approved stories, arc42 runtime and deployment views, c4 boundaries, cross-cutting concepts, quality scenarios, risks, architecture decisions, implementation plans, and code changes; bind evidence to the exact artifact and route manual acceptance to j-stakeholder-validation-and-acceptance.
---

# Automated Testing and Verification

## Purpose

Create and evaluate automated technical evidence for an exact implementation artifact. Use approved behavior, arc42 architecture evidence, C4 boundaries, implementation plans, and change impact to select the minimum sufficient test scope.

## Governing Rules

- Identify the exact commit, build, package, image, or other artifact before claiming execution results.
- Separate strategy mode, execution mode, and combined mode.
- Consider integration, end-to-end, and regression testing for every scope and record `required`, `already-covered`, `not-required`, or `blocked`.
- Derive test scope from relevant runtime views, deployment boundaries, cross-cutting concepts, quality scenarios, risks, decisions, and changed architecture relationships.
- Do not duplicate developer tests already owned by implementation planning unless they form part of the required evidence set.
- Do not rewrite acceptance criteria, architecture, or implementation plans.
- Record failures, blocked evidence, and limitations honestly.
- Manual stakeholder validation belongs to Skill J.

## Canonical Files

Read:

- approved user stories and acceptance references;
- `sdlc_docs/01_requirements/04_user_story_technical_readiness.md`;
- `sdlc_docs/02_architecture/00_architecture_document.md`;
- `sdlc_docs/02_architecture/01_architecture_traceability.md`;
- relevant container, component, data-model, and decision documents;
- relevant implementation plans and issue registry;
- current code, tests, dependencies, continuous-integration configuration, and exact implementation artifact.

Create or update:

- `sdlc_docs/04_testing/00_testing_strategy.md`;
- `sdlc_docs/04_testing/01_test_traceability.md`;
- `sdlc_docs/04_testing/02_testing_results.md`.

## Core Workflow

### 1. Establish Mode, Artifact, and Scope

Read `references/artifact-and-entry-gate.md`. Identify exact artifact, stories, issues, architecture version, implementation-plan version, environment, and affected architecture.

### 2. Inspect Existing Evidence and Change Impact

Inspect existing tests, continuous-integration results, changed files, affected containers, components, interfaces, data, runtime flows, deployment boundaries, quality scenarios, risks, and decisions.

### 3. Select Applicable Test Categories

Read `references/test-category-selection.md`. Record applicability and rationale for integration, end-to-end, regression, and other risk-based categories.

### 4. Design or Update Automated Tests

Create or update tests only in execution or combined mode. Reuse project conventions. Map each test to story, architecture concern, boundary, risk, quality scenario, and implementation artifact.

### 5. Execute and Collect Evidence

Run the selected automated checks when tools and environment are available. Record commands, environment, timestamps, results, evidence references, failures, and limitations.

### 6. Assess Results and Route Findings

Read `references/evidence-and-status.md`. Separate test result, evidence type, defect classification, and release implication. Route implementation defects to implementation, plan defects to Skill H, architecture defects to Skill E, and manual acceptance to Skill J.

### 7. Persist Testing State

Read `references/persistence.md`. Preserve history and bind one current result set to the exact artifact and environment.

## Boundary with Other Skills

- Skill H owns developer-focused implementation tests and coding sequence.
- Skill E owns architecture and quality strategy.
- Skill I owns broader automated technical verification.
- Skill J owns manual validation and stakeholder acceptance.
- Do not make the stakeholder acceptance decision.

## Resources

- `references/artifact-and-entry-gate.md`
- `references/test-category-selection.md`
- `references/evidence-and-status.md`
- `references/persistence.md`
- `templates/testing-strategy.md`
- `templates/test-traceability.md`
- `templates/testing-results.md`
