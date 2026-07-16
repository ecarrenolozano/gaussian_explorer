# Persistence, Review, and Approval

## Versioning

Bind the full architecture package to one architecture version and one source story version. A semantic change to goals, constraints, responsibilities, boundaries, relationships, data ownership, runtime behavior, deployment, cross-cutting concepts, quality strategy, risks, decisions, implementation mapping, view content, or view layout creates a new architecture version.

Exported images inherit the architecture version of `diagrams/workspace.dsl`. Re-export changed views before approval. Editorial corrections may retain the version when meaning is unchanged and the change is recorded.

## Validation

Before writing or approving:

- verify every active story has an architecture path or an explicit blocker;
- verify each arc42 section is relevant, explicitly not applicable, or marked open;
- verify each component is nested under its owning container;
- verify data stores are modeled as containers;
- verify traceability links resolve;
- verify names and responsibilities agree across files;
- verify accepted decisions are reflected in the narrative and model;
- verify quality goals and scenarios are consistent with selected design tactics;
- verify runtime and deployment views agree with container relationships;
- verify every Dynamic view is scoped to an element that can legally contain all referenced elements;
- verify every Dynamic-view interaction has a matching relationship declared in the model;
- verify every Deployment view references an existing `deploymentEnvironment` and does not define deployment nodes inline;
- verify `diagrams/workspace.dsl` is the only current canonical C4 source;
- verify `diagrams/docker-compose.yml` resolves its workspace from the diagram folder;
- verify every embedded C4 image exists under `diagrams/images/`;
- verify every embedded image corresponds to a current view key and architecture version;
- verify retired or stale exports are removed or clearly excluded from documentation;
- inspect exported images for clipped content, unreadable text, missing elements, or misleading layout;
- run `docker compose -f sdlc_docs/02_architecture/diagrams/docker-compose.yml config` when Docker Compose is available;
- run Structurizr locally and inspect fresh logs for `StructurizrDslParserException` when Docker is available;
- do not mark Structurizr rendering as validated from Docker Compose syntax alone;
- export selected views as SVG or PNG when supported export tooling is available;
- validate Markdown image links;
- record `not-validated` or `not-exported` with the reason when a tool check cannot be performed.

Stage related changes and write them together when possible. If a partial write occurs, report the inconsistent files and do not claim the architecture package is complete.

## Readiness

Use one assessment:

- `architecture-ready`;
- `changes-required`;
- `blocked`.

Architecture is ready only when the selected arc42 content and C4 views answer their intended questions, responsibilities and ownership are clear, significant internal designs are sufficient, quality and risk concerns are addressed, traceability is complete, required Markdown image references resolve, and no blocking decision remains.

A tool limitation may be recorded without invalidating the architecture semantics, but approval must not claim that rendering or image export was validated when it was not.

## Approval

Record human approval only for the exact architecture version and source story version. Record approver, date, assessment, material accepted risks, Structurizr validation status, and diagram export status. Approval becomes stale when the source story version, architecture version, current view content, or embedded exported images change.
