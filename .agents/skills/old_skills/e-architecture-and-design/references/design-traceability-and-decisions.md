# Design, Traceability, and Decisions

## Detailed Design

Create a container, component, or data-model document when one or more conditions apply:

- the detail would make the main architecture document hard to navigate;
- internal collaboration is not obvious;
- several modules or classes share a responsibility;
- state, lifecycle, concurrency, ownership, or failure recovery matters;
- domain relationships are complex;
- several developers need a shared design;
- the area is high-risk, safety-sensitive, security-sensitive, or difficult to test;
- the design will guide more than one implementation issue.

Do not create detailed documents for trivial or framework-obvious elements.

## Architecture-to-Code Mapping

For each relevant story, record:

- relevant arc42 concern or section;
- software system;
- owning container;
- component or data model;
- architectural responsibility;
- runtime or deployment concern when applicable;
- current or proposed implementation location;
- mapping status;
- related decisions and repository work when known.

Use one mapping status:

- `confirmed`: verified in the current repository;
- `proposed`: an architectural suggestion awaiting implementation review;
- `planned`: accepted by an implementation plan but not yet implemented;
- `not-mapped`: no reliable implementation location exists yet.

Do not derive code names automatically from architecture documentation names.

## Architecture Decisions

Create a decision record when a choice:

- changes a system, container, interface, data ownership, runtime behavior, deployment, or quality strategy;
- establishes a recurring cross-cutting concept;
- creates a long-lived constraint;
- has meaningful alternatives and consequences;
- affects several stories or implementation plans;
- would be expensive or risky to reverse.

Do not record routine library usage, formatting choices, or local refactoring as architecture decisions.
