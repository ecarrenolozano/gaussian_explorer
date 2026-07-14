---
name: k-deployment-preparation
description: prepare a versioned, environment-specific deployment plan for an exact stakeholder-accepted release candidate. use after automated testing and stakeholder validation to define release scope, artifacts, configuration, secrets, migrations, deployment steps, health checks, monitoring, rollback, ownership, accepted risks, and deployment readiness without executing the deployment.
---

# Deployment Preparation

## Purpose

Prepare an exact stakeholder-accepted release candidate for safe, repeatable deployment and recovery in a named environment.

Produce and approve the deployment plan. Do not execute the deployment, change infrastructure, expose secrets, or claim deployment success.

## Governing Rules

- Bind every plan and decision to an exact release candidate and target environment.
- Require current automated-testing evidence and stakeholder acceptance for that release candidate.
- Treat deployment preparation and deployment execution as separate activities.
- Preserve approved release scope and accepted limitations.
- Do not invent commands, credentials, environment values, migration behavior, or recovery procedures.
- Never store plaintext secrets in documentation.
- Define recovery and decision ownership before declaring readiness.
- Make approval environment-specific and version-specific.
- Report missing or inconsistent state as a blocker; do not silently repair upstream artifacts.

## Canonical Files

Read:

- `sdlc_docs/00_project_context/project_context.md`
- `sdlc_docs/01_requirements/01_user_stories.md`
- `sdlc_docs/01_requirements/02_traceability_matrix.md`
- `sdlc_docs/02_architecture/00_architecture_overview.md`
- relevant component documents under `sdlc_docs/02_architecture/components/`
- relevant architecture decisions under `sdlc_docs/02_architecture/decisions/`
- `sdlc_docs/03_implementation/00_repository_issue_registry.md`, when present
- relevant implementation plans and implementation handoff records
- `sdlc_docs/04_testing/02_testing_results.md`
- `sdlc_docs/05_validation/01_acceptance_results.md`
- existing deployment, infrastructure, migration, and operational documentation

Create or update:

- `sdlc_docs/06_deployment/00_deployment_plan.md`
- `sdlc_docs/06_deployment/01_release_checklist.md`
- `sdlc_docs/06_deployment/02_rollback_plan.md`, when rollback requires a separate document

## Core Workflow

### 1. Validate the Release Entry State

Confirm the exact release candidate, included stories, current testing assessment, current stakeholder-acceptance decision, target environment, and responsible deployment decision-makers.

Stop when acceptance does not permit deployment preparation or when the release candidate cannot be identified uniquely.

Read `references/entry-and-version-gate.md`.

### 2. Establish the Deployment Scope

Record included and excluded work, artifact identifiers, environment, deployment window, dependencies, compatibility expectations, downtime, and known limitations.

Do not expand release scope during deployment preparation.

### 3. Prepare Configuration, Access, and Secrets

Identify required access, environment-specific configuration, secret references, certificates, feature controls, and ownership. Document where values are managed without copying secret values.

Read `references/configuration-and-access.md`.

### 4. Prepare Migrations and Deployment Procedure

Define ordered prerequisites, backup or recovery preparation, migrations, deployment actions, verification points, pause conditions, and decision owners.

Use exact commands only when they are known, reviewed, and repository-supported. Otherwise record the unresolved action as a blocker.

Read `references/migrations-and-procedure.md`.

### 5. Define Health Checks, Monitoring, and Communication

Select critical post-deployment checks, expected signals, alert conditions, observation period, responsible people, and communication steps.

Do not repeat the complete automated-testing or stakeholder-validation phase.

Read `references/verification-and-monitoring.md`.

### 6. Define Rollback or Recovery

Document rollback triggers, decision authority, application recovery, data recovery, configuration restoration, verification, and communication. State explicitly when rollback is impossible and a forward recovery is required.

Read `references/rollback-and-recovery.md`.

### 7. Persist the Versioned Deployment Package

Create or update the canonical deployment documents using the bundled templates. Bind them to the release candidate, target environment, testing evidence, acceptance result, and deployment-plan version.

Read `references/persistence-and-versioning.md`.

### 8. Determine Readiness and Record Approval

Use one readiness assessment:

- `ready-for-deployment`
- `ready-with-accepted-risks`
- `not-ready`
- `blocked`

Human approval applies only to the exact deployment-plan version, release candidate, and target environment. A changed plan, artifact, environment, migration, or material risk makes the earlier approval stale.

Read `references/readiness-and-approval.md`.

## Boundary with Other Skills

- Skill I provides automated technical-testing evidence.
- Skill J provides stakeholder acceptance for the exact release candidate.
- Skill K prepares and approves the deployment plan only.
- An authorized operator, deployment pipeline, or separate execution process performs deployment.
- Implementation defects return to implementation and Skill I for retesting.
- Validation defects or changed acceptance return to Skill J or the appropriate upstream owner.
- Architecture or deployment-boundary defects return to Skill E.
- New or missing product behavior returns to Skills B–D as appropriate.

## Resources

- `references/entry-and-version-gate.md`
- `references/configuration-and-access.md`
- `references/migrations-and-procedure.md`
- `references/verification-and-monitoring.md`
- `references/rollback-and-recovery.md`
- `references/persistence-and-versioning.md`
- `references/readiness-and-approval.md`
- `templates/deployment-plan.md`
- `templates/release-checklist.md`
- `templates/rollback-plan.md`
