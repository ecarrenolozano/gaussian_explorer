---
name: j-stakeholder-validation-and-acceptance
description: prepare, execute, and record manual stakeholder validation against approved user stories and acceptance criteria for an exact tested release candidate. use after automated testing to collect manual evidence, distinguish defects from new requirements, record explicit waivers, determine story dispositions, and capture the authorized stakeholder acceptance decision before deployment preparation.
---

# Stakeholder Validation and Acceptance

## Purpose

Validate the delivered behavior from the stakeholder perspective through manual scenarios based on approved acceptance criteria, then record the authorized decision for an exact tested release candidate.

## Governing Rules

- Reuse approved acceptance criteria as the expected behavior; do not silently rewrite them.
- Bind validation and acceptance to an exact release candidate and testing evidence.
- Keep automated technical testing in Skill I.
- Require an authorized human stakeholder for acceptance decisions.
- Separate observed behavior from stakeholder disposition.
- Classify defects, new requirements, clarification needs, and architecture limitations before routing them.
- Do not approve on behalf of the stakeholder.

## Canonical Files

Read:

- approved user stories and traceability;
- product-readiness approval;
- current architecture and technical-readiness state when relevant;
- automated testing strategy and results;
- exact release candidate or build;
- known defects, limitations, and implementation notes.

Create or update:

- `sdlc_docs/05_validation/00_validation_plan.md`
- `sdlc_docs/05_validation/01_acceptance_results.md`

## Core Workflow

### 1. Validate the Entry State and Scope

Select either **selected-story validation** or **release-candidate validation**. Confirm story version, story IDs, exact release candidate, testing assessment, environment, evaluator, and authorized decision-maker.

Read `references/entry-and-scope.md`.

### 2. Prepare Manual Validation Scenarios

Create understandable manual procedures derived from approved acceptance criteria. Add environment, test data, evaluator actions, and evidence requirements without changing expected behavior.

Read `references/manual-validation.md`.

### 3. Execute or Facilitate Validation

Ask the evaluator to execute or observe each scenario. Record actual results, evidence, comments, and related defects or issues accurately.

### 4. Record Behavior Results and Stakeholder Dispositions

For each criterion, record behavior result separately from stakeholder disposition. An unmet criterion cannot be described as met merely because a deviation is accepted.

### 5. Classify Findings and Route Them

Route implementation defects to implementation and Skill I for retesting; plan defects to Skill H; missing technical evidence to Skill I; story defects to Skill C and D; requirement gaps or new behavior to Skill B; architecture limitations to Skill E and downstream reassessment.

Read `references/status-and-routing.md`.

### 6. Determine Story and Release Outcomes

Assign story outcomes from the evidence. A selected-story validation may accept those stories but cannot approve a full release outside its scope.

### 7. Persist Evidence and the Stakeholder Decision

Use `templates/validation-plan.md` and `templates/acceptance-results.md`. Record evaluator, authorized approver, exact artifact, accepted limitations, waivers, and evidence.

### 8. Determine the Release Recommendation

Use one recommendation:

- `ready-for-deployment-preparation`;
- `ready-with-approved-limitations`;
- `not-ready`;
- `validation-incomplete`.

Deployment preparation is blocked unless the recommendation permits it.

## Boundary with Other Skills

- Skill I owns automated technical verification.
- Skill J owns manual validation and stakeholder acceptance.
- Skill J does not modify requirements, stories, architecture, implementation plans, code, or automated tests.
- A new release candidate requires new or explicitly scoped revalidation.

## Resources

- `references/entry-and-scope.md`
- `references/manual-validation.md`
- `references/status-and-routing.md`
- `references/persistence-and-acceptance.md`
- `templates/validation-plan.md`
- `templates/acceptance-results.md`
