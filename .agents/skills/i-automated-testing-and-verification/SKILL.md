---
name: i-automated-testing-and-verification
description: plan, create, execute, and report automated technical verification for an exact implementation artifact. use after implementation to assess existing coverage and add applicable integration, end-to-end, regression, performance, security, compatibility, migration, recovery, or other risk-based automated tests without duplicating adequate developer tests or performing stakeholder acceptance.
---

# Automated Testing and Verification

## Purpose

Provide objective automated evidence that an exact implementation artifact satisfies approved behavior and applicable quality expectations.

Always consider integration, end-to-end, and regression testing. Create or run each category only when applicable, and record the reason when it is not required, blocked, or already covered.

## Governing Rules

- Bind every result to an exact commit, package, image, build, or other immutable implementation artifact.
- Inspect existing tests before adding new ones.
- Reuse adequate developer tests and avoid redundant coverage.
- Use risk-based selection rather than maximizing test count.
- Keep manual stakeholder validation outside this skill.
- Do not change expected behavior to make tests pass.
- Report failures, gaps, and blocked verification honestly.

## Canonical Files

Read:

- approved user stories and traceability;
- approved architecture and relevant decisions;
- applicable technical-readiness reports;
- repository issue registry;
- relevant implementation plans;
- implementation handoff or exact artifact identifier;
- source code, existing tests, continuous-integration configuration, and available test results.

Create or update:

- `sdlc_docs/04_testing/00_testing_strategy.md`
- `sdlc_docs/04_testing/01_test_traceability.md`
- `sdlc_docs/04_testing/02_testing_results.md`

## Core Workflow

### 1. Select the Operating Mode and Artifact

Use **strategy mode**, **execution mode**, or **combined mode**. Execution requires an exact implementation artifact and test environment.

Read `references/artifact-and-entry-gate.md`.

### 2. Inspect Existing Test Evidence

Inspect developer tests, integration tests, end-to-end tests, regression suites, and continuous-integration results. Do not infer gaps only from documentation.

### 3. Assess Test Category Applicability

For each relevant category, record `required`, `already-covered`, `not-required`, or `blocked`, with a reason.

Always evaluate:

- integration tests;
- end-to-end tests;
- regression tests.

Evaluate performance, security, reliability, compatibility, migration, recovery, accessibility, and other quality tests when requirements or risk justify them.

Read `references/test-category-selection.md`.

### 4. Define the Minimum Additional Automated Test Set

Map approved behavior and risks to existing evidence and missing automated tests. Prefer the lowest effective test level while retaining enough end-to-end coverage for critical workflows.

### 5. Create or Update Automated Tests

When requested and tools allow, implement the selected automated tests according to repository conventions. Do not create manual validation procedures.

### 6. Execute the Selected Tests

Run relevant tests in the identified environment. Capture commands, environment, counts, failures, blocked tests, and evidence references.

### 7. Persist Traceability and Results

Separate verification status from evidence type. Use `templates/testing-strategy.md`, `templates/test-traceability.md`, and `templates/testing-results.md`.

### 8. Determine the Testing Assessment

Use one assessment:

- `testing-passed`;
- `testing-passed-with-known-limitations`;
- `testing-failed`;
- `testing-incomplete`;
- `testing-blocked`.

This assessment is technical evidence, not stakeholder acceptance.

## Boundary with Other Skills

- Skill H guides developer tests during implementation.
- Skill I owns broader automated integration, end-to-end, regression, and risk-based verification.
- Skill J owns manual validation and stakeholder acceptance.
- Implementation defects return to implementation, followed by retesting.
- Requirement, story, or architecture defects return to their owning skills.

## Resources

- `references/artifact-and-entry-gate.md`
- `references/test-category-selection.md`
- `references/evidence-and-status.md`
- `references/persistence.md`
- `templates/testing-strategy.md`
- `templates/test-traceability.md`
- `templates/testing-results.md`
