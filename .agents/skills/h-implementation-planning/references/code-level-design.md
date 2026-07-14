# Code-Level Design

Define only when useful:

- affected modules or files grounded in the current repository;
- key functions, classes, data structures, or state transitions;
- public operations and internal dependencies;
- interface, data, configuration, and migration changes;
- algorithms and error behavior;
- compatibility and rollback considerations.

Do not design every class or method in advance. Use diagrams only when relationships are difficult to communicate in text.

Internal refactoring is allowed when it preserves approved component responsibilities, interfaces, data ownership, deployment boundaries, and architecture decisions. Otherwise create an architecture change request.
