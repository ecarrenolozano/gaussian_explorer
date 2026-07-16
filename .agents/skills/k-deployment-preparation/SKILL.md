---
name: k-deployment-preparation
description: prepare and approve an environment-specific deployment and recovery plan for the exact tested and stakeholder-accepted release candidate. use after j-stakeholder-validation-and-acceptance to derive affected deployable units, data stores, dependencies, configuration, secrets, migration order, health checks, monitoring, rollback, recovery, risks, and decision authority from the approved arc42 deployment view, runtime behavior, cross-cutting concepts, quality requirements, c4 containers, architecture decisions, testing evidence, and acceptance state without executing deployment.
---

# Deployment Preparation

## Purpose

Prepare a safe, environment-specific deployment and recovery package for the exact accepted release candidate. Translate approved deployment architecture and operational concerns into an executable plan for an authorized operator or pipeline without performing the deployment.

## Governing Rules

- Require stakeholder acceptance and automated testing evidence for the exact release candidate.
- Bind every plan to one architecture version and named target environment.
- Use arc42 section 7 as the primary deployment narrative, supported by relevant runtime views, cross-cutting concepts, quality scenarios, risks, decisions, C4 containers, and detailed documents.
- Distinguish architecture container names from actual image, package, service, job, schema, or infrastructure resource names. Verify real deployment mappings.
- Reference secrets; never copy secret values into documentation.
- Define rollback, forward recovery, pause, abort, and decision authority explicitly.
- Make approval specific to the exact artifact, environment, plan version, migration set, recovery approach, and accepted risks.
- Do not execute deployment, change infrastructure, or claim deployment success.

## Canonical Files

Read:

- accepted release-candidate evidence from Skill J;
- automated testing evidence from Skill I;
- `sdlc_docs/02_architecture/00_architecture_document.md`;
- `sdlc_docs/02_architecture/01_architecture_traceability.md`;
- `sdlc_docs/02_architecture/workspace.dsl`;
- relevant container, data-model, component, decision, implementation-plan, migration, and repository files;
- target-environment conventions and authorized operational procedures.

Create or update:

- `sdlc_docs/06_deployment/00_deployment_plan.md`;
- `sdlc_docs/06_deployment/01_release_checklist.md`;
- `sdlc_docs/06_deployment/02_rollback_plan.md` when recovery detail is substantial.

## Core Workflow

### 1. Validate the Release Entry State

Read `references/entry-and-version-gate.md`. Confirm artifact, acceptance, testing, architecture, target environment, deployable mappings, and decision-makers.

### 2. Establish Deployment Scope from Architecture and Repository Evidence

Identify affected containers, real deployment units, data stores, brokers, caches, external integrations, runtime dependencies, architecture decisions, quality scenarios, and risks. Resolve names against actual build and infrastructure definitions.

### 3. Prepare Configuration, Access, and Secrets

Read `references/configuration-and-access.md`. Record environment-specific configuration sources, secret references, permissions, certificates, endpoints, feature controls, and owners.

### 4. Prepare Migrations and Deployment Procedure

Read `references/migrations-and-procedure.md`. Define prerequisites, compatibility, backups, ordering, pause or abort conditions, verification, and decision authority.

### 5. Define Health Checks, Monitoring, and Communication

Read `references/verification-and-monitoring.md`. Derive checks and observation windows from architecture quality scenarios, cross-cutting observability concepts, runtime behavior, and accepted risk.

### 6. Define Rollback or Forward Recovery

Read `references/rollback-and-recovery.md`. Choose a viable recovery strategy per affected deployment and data boundary. Do not claim rollback is possible without evidence.

### 7. Persist the Versioned Deployment Package

Read `references/persistence-and-versioning.md`. Bind the documents to artifact, architecture version, environment, testing evidence, acceptance, and plan version.

### 8. Determine Readiness and Record Approval

Read `references/readiness-and-approval.md`. Use `ready-for-deployment`, `ready-with-accepted-risks`, `not-ready`, or `blocked`. Human approval applies only to the exact plan version, artifact, and environment.

## Boundary with Other Skills

- Skill E owns architecture containers, deployment views, runtime design, cross-cutting concepts, quality scenarios, risks, and data ownership.
- Skill I provides automated technical evidence.
- Skill J provides stakeholder acceptance.
- Skill K prepares and approves the plan only; an authorized operator or pipeline executes it.
- Architecture or deployment-boundary defects return to Skill E.
- Implementation defects return to implementation and Skill I for retesting.

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
