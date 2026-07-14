# Modeling and Diagram Rules

Load during Step 4.

## Naming

- Use clear human-readable names for people, systems, applications, services, data stores, components, interfaces, and deployment environments.
- Keep the same name across diagrams, tables, component documents, and story mappings when it refers to the same responsibility.
- Change a name only when the documented responsibility changes or the previous wording is misleading.
- Do not create shortened element identifiers, internal code names, or implementation names solely for documentation.
- Documentation filenames may use readable lowercase words separated by hyphens for navigation, but they must not prescribe source-code modules, packages, classes, services, or deployment names.
- When two elements have similar names, add a short descriptive qualifier instead of an abbreviation.

## Modeling Rules

- Give every element one clear responsibility and owner when known.
- Define each relationship once with direction, purpose, and communication method when supported.
- Keep data ownership singular or explicitly coordinated.
- Distinguish current-state elements from proposed target-state elements.
- Keep each diagram focused on one question and state its level of detail.
- Never include credentials, private endpoints, secrets, or sensitive sample data.
- Keep diagrams, tables, narrative, and story mapping semantically aligned.

## Mermaid Standard

Use Mermaid as the primary and required diagram notation for canonical architecture views in Markdown.

- Use `flowchart` for System Context, Container, Component, data-flow, and deployment views.
- Use `sequenceDiagram` for important interactions and failure paths that cross system boundaries.
- Use `stateDiagram-v2` for important lifecycle or business-state behavior.
- Use `erDiagram` for conceptual data relationships when it answers an important question.
- Keep Mermaid source blocks editable beside the explanatory narrative. Do not use exported images as the only diagram source.
- Use descriptive labels rather than abbreviations.
- Explain specialized terms near the diagram when a general reader may not know them.
- Prefer portable Mermaid syntax. Avoid experimental or renderer-specific features unless repository support is confirmed.
- Create only the views selected in Step 2. Do not add diagrams only to make the documentation appear complete.

## Optional External Modeling Artifacts

An architect may add an external modeling artifact when the user requests it, repository conventions require it, or it materially improves maintenance of a complex architecture.

- Do not assume a specific tool, file format, directory, or modeling language.
- Do not create or update an external model by default.
- Do not make architecture completion, assessment, or approval depend on an optional tool.
- Record each included artifact's path, purpose, role, and validation status in the architecture overview.
- Keep optional artifacts consistent with the approved Markdown documents, Mermaid diagrams, story map, component documents, and architecture decision records.
- Unless repository policy explicitly defines another source of truth, treat the approved Markdown and Mermaid package as canonical for this workflow.
- If an optional artifact conflicts with the canonical package, stop and reconcile the inconsistency before approval.
- If project tooling cannot validate an optional artifact, state that validation was not performed. Do not claim that it is valid.
