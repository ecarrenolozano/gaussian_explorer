# Test Category Selection

Record `required`, `already-covered`, `not-required`, or `blocked` for every applicable category.

## Integration Tests

Use integration tests for collaboration:

- between components inside one container when the boundary has meaningful behavior;
- between application containers;
- between an application and a database, cache, broker, file store, or external system;
- across interface contracts, messaging, authentication, migrations, retries, failure recovery, or recurring cross-cutting behavior.

Use arc42 building blocks, runtime views, concepts, and decisions to identify these boundaries.

## End-to-End Tests

Use end-to-end tests for a small set of critical actor journeys and operational scenarios that cross real system boundaries. Select them from approved behavior, runtime views, deployment context, and material risks. Do not duplicate every criterion at the most expensive level.

## Regression Tests

Select regression tests from:

- existing behavior in affected containers and components;
- relationships, runtime flows, concepts, or decisions changed by the implementation;
- critical neighboring flows with increased risk;
- every corrected defect when practical;
- existing suites required by project policy.

Regression is a purpose and may include unit, integration, and end-to-end tests.

## Quality and Risk-Based Tests

Assess performance, scalability, security, privacy, reliability, resilience, compatibility, migration, recovery, configuration, observability, accessibility automation, and other categories when arc42 quality scenarios, cross-cutting concepts, deployment view, risks, decisions, or requirements justify them.

Do not invent thresholds. Use approved measures or report the missing decision.
