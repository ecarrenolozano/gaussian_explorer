# Test Category Selection

## Integration testing

Use when changes affect boundaries such as databases, files, services, application programming interfaces, queues, storage, authentication, migrations, or external systems.

## End-to-end testing

Use a small number of tests for critical user workflows, high-risk failure paths, authorization boundaries, important persistence behavior, and release-critical processes.

## Regression testing

Select tests based on change impact. Include:

- affected existing tests;
- tests for new behavior;
- a regression case for corrected defects when practical;
- critical unaffected workflows whose failure risk increased.

Regression is a purpose, not a separate test level; its suite may contain unit, integration, and end-to-end tests.

## Other categories

Select performance, security, reliability, compatibility, migration, recovery, accessibility, or contract tests only when approved requirements, architecture, operational risk, or known defects justify them.
