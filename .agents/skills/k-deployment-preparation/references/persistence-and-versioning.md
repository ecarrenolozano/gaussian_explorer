# Persistence and Versioning

Use one deployment-plan version for the coordinated deployment package.

Bind the package to:

- exact release candidate;
- target environment;
- included story identifiers;
- automated-testing evidence;
- stakeholder-acceptance result;
- relevant architecture version and decisions;
- migration plan or version when applicable.

Increment the deployment-plan version when deployment steps, environment, artifact, migration, rollback, monitoring, or material risks change.

Editorial changes that do not alter execution or risk may be recorded without creating a new substantive version.

Keep the current state near the top of `00_deployment_plan.md`. Preserve revision and decision history. Do not overwrite evidence of prior plans or approvals.

Use a marker such as:

```html
<!-- deployment-plan | version: 1.0 | release-candidate: <exact-artifact> | environment: <name> | assessment: blocked | decision: pending -->
```

This marker is workflow metadata and does not prescribe implementation names.
