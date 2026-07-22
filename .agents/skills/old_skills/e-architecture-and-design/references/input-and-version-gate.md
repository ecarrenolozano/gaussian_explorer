# Input and Version Gate

1. Read the current story-document version and active story identifiers.
2. Verify that `03_user_story_product_readiness.md` contains valid human product approval for that exact version.
3. Verify that the traceability matrix is consistent with the active stories.
4. Inspect the current architecture marker, history, `00_architecture_document.md`, traceability, `diagrams/workspace.dsl`, exported images, container documents, and decisions.
5. If `workspace.dsl` or `docker-compose.yml` exists directly under `02_architecture/`, classify the diagram layout as legacy and migrate the maintained content into `02_architecture/diagrams/`.
6. If only `00_architecture_overview.md` exists, classify the run as `migrate` and preserve its meaningful content in the new arc42 document.
7. Classify the run as `create`, `evolve`, `reassess`, `migrate`, or `approve`.
8. Stop when the reviewed story version is not current, approval is stale, duplicate current markers exist, or architecture files disagree about their version.

When evolving architecture:

- preserve unchanged valid elements and decisions;
- identify added, changed, and retired scope;
- assess whether changed stories affect goals, constraints, containers, components, data, runtime flows, deployment, cross-cutting concepts, quality scenarios, risks, implementation mappings, view keys, or exported images;
- mark exported images stale whenever their source view or layout changes;
- never treat an old architecture approval as approval of changed content.
