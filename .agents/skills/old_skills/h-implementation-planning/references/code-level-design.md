# Code-Level Design

Use repository evidence first. Define only what the implementation requires.

Possible design detail includes:

- exact files to create or modify;
- modules, packages, classes, functions, interfaces, schemas, or configuration;
- internal UML class, sequence, and state diagrams;
- supplemental algorithm, data-flow, or module-dependency diagrams only when UML is not the right notation;
- algorithms and error handling;
- transaction and concurrency behavior;
- compatibility and migration strategy;
- logging, metrics, traces, feature controls, and operational hooks.

## UML Diagram Requirement

Include code-level UML diagrams in Mermaid syntax for non-trivial plans. A plan is non-trivial when it touches multiple modules, introduces or changes shared data structures, coordinates UI/state/model/export behavior, changes runtime sequencing, adds integration points, or needs precise handoff across developers.

Use:

- `classDiagram` for dataclasses, DTOs, result objects, domain entities, exceptions, service/helper classes, public functions grouped as utility classes when needed, and relationships between those structures;
- `sequenceDiagram` for runtime collaborations, validation gates, request/response behavior, and handoffs between UI, services, model, export, and state;
- `stateDiagram-v2` for workflow, session, lifecycle, and validation-state transitions.

Use supplemental `flowchart` diagrams only for algorithms, data-flow sketches, or module-dependency views that are not naturally expressed as UML. Do not use generic boxes as a substitute for UML class, sequence, or state diagrams when the plan discusses classes, dataclasses, DTOs, result objects, services, or lifecycle states.

A trivial single-function or single-file change may state why no UML diagram is required.

Each diagram must map back to the relevant architecture element and arc42 concern. Keep diagrams implementation-specific and inside approved boundaries.

## Naming Discipline

Use standard UML diagram names in headings and mapping tables:

- `UML class diagram`
- `UML sequence diagram`
- `UML state machine diagram`

Use names such as `data-flow sketch` or `module-dependency sketch` only for supplemental non-UML diagrams. Do not invent new architecture diagram categories for code-level plans.

Route to Skill E when the change affects:

- software-system or container boundaries;
- component responsibilities or ownership;
- shared or public interfaces;
- data ownership;
- important runtime flows;
- deployment topology;
- recurring cross-cutting concepts;
- significant quality strategy or tactics;
- architecture risks or decisions;
- reusable design that should govern multiple issues.

Do not convert architecture documentation names into code names without repository or plan evidence.
