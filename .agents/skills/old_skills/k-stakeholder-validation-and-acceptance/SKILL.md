---
name: j-stakeholder-validation-and-acceptance
description: prepare and perform manual validation for an exact tested release candidate, derive scenarios from approved acceptance criteria, collect evidence, separate observed behavior from stakeholder disposition, record explicit waivers, and issue an authorized acceptance recommendation. use after i-automated-testing-and-verification; consult relevant arc42 runtime, deployment, context, quality, risk, and c4 architecture information only to prepare realistic environments, dependencies, data, roles, and operational conditions without turning internal architecture checks into acceptance criteria.
---

# Stakeholder Validation and Acceptance

## Purpose

Validate an exact tested release candidate manually against approved acceptance criteria and record the authorized stakeholder decision. Use architecture information only to prepare a realistic validation context and diagnose setup dependencies.

## Governing Rules

- Require an exact release candidate and automated testing assessment for the same artifact.
- Reuse approved acceptance criteria; do not rewrite expected behavior.
- Keep manual validation separate from automated technical verification.
- Use relevant arc42 context, runtime, deployment, cross-cutting, quality, and risk information only when it affects user-visible behavior, environment setup, external dependencies, data, roles, or operational workflow.
- Do not make internal container, component, or code structure itself an acceptance criterion unless the approved requirement explicitly exposes it.
- Record behavior result separately from stakeholder disposition.
- Record explicit waivers without changing approved acceptance criteria.
- Bind every result and decision to the exact artifact, story version, testing evidence, environment, evaluator, and date.

## Canonical Files

Read:

- approved user stories and acceptance references;
- `sdlc_docs/04_testing/02_testing_results.md`;
- `sdlc_docs/02_architecture/00_architecture_document.md` and `01_architecture_traceability.md` only as needed for validation setup;
- relevant runtime, deployment, external-system, quality, or risk information;
- known defects and release-candidate metadata.

Create or update:

- `sdlc_docs/05_validation/00_validation_plan.md`;
- `sdlc_docs/05_validation/01_acceptance_results.md`.

## Core Workflow

### 1. Validate Entry State and Scope

Read `references/entry-and-scope.md`. Confirm artifact, stories, testing evidence, environment, participants, and validation mode.

### 2. Prepare Manual Validation

Read `references/manual-validation.md`. Select approved acceptance criteria and define roles, test data, evaluator actions, evidence, environment, and external dependencies. Use architecture information only where it improves realism or setup correctness.

### 3. Perform and Record Validation

Execute the manual scenarios when the environment and participants are available. Record actual behavior and evidence without interpreting missing execution as success.

### 4. Classify Findings and Route Defects

Read `references/status-and-routing.md`. Separate behavior failures, environment blockers, requirement defects, implementation defects, architecture limitations, and new requests.

### 5. Record Stakeholder Disposition

Record `accepted`, `rejected`, `accepted-by-explicit-waiver`, or `pending` for the exact release candidate. The approver must be known and authorized.

### 6. Persist the Validation State

Read `references/persistence-and-acceptance.md`. Preserve history, waivers, routed findings, and release recommendation.

## Boundary with Other Skills

- Skill I owns automated technical evidence.
- Skill J owns manual validation and stakeholder acceptance.
- Skill E owns architecture correctness.
- Skill K consumes accepted release evidence for deployment preparation.
- Do not modify requirements, stories, architecture, implementation plans, tests, or code.

## Resources

- `references/entry-and-scope.md`
- `references/manual-validation.md`
- `references/status-and-routing.md`
- `references/persistence-and-acceptance.md`
- `templates/validation-plan.md`
- `templates/acceptance-results.md`
