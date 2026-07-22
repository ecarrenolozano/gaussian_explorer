# arc42, C4, and Structurizr Guidance

## Division of Responsibility

- Use arc42 to structure the architecture narrative.
- Use the C4 model to describe the system at different levels of zoom.
- Use `diagrams/workspace.dsl` as the canonical text model for C4 views.
- Use `diagrams/docker-compose.yml` to run the local Structurizr viewer.
- Use `diagrams/images/` for exported, static copies of selected C4 views.
- Use separate architecture decision records for significant decisions.

## arc42 Sections

Maintain these sections in `00_architecture_document.md`:

1. Introduction and Goals
2. Constraints
3. Context and Scope
4. Solution Strategy
5. Building Block View
6. Runtime View
7. Deployment View
8. Cross-Cutting Concepts
9. Architecture Decisions
10. Quality Requirements
11. Risks and Technical Debt
12. Glossary

For each section, add relevant content, state `Not applicable` with a short reason, or mark unresolved content as open. Prefer concise evidence over generic prose.

## C4 Placement inside arc42

- Section 3: System Context view and external interfaces.
- Section 5: Container views and selected Component views.
- Section 6: Dynamic views or supplementary sequence diagrams for important runtime scenarios.
- Section 7: Deployment views when topology or environment matters.
- Section 5 or detailed component documents: selective Code-level diagrams when they add value.

## C4 Terms

- **Person:** a human role that uses or is affected by the system.
- **Software system:** the complete system being designed or an external system it uses.
- **Container:** an independently running application, service, worker, command-line program, database, cache, message broker, file store, or similar runtime unit. It does not necessarily mean a Docker container.
- **Component:** a cohesive responsibility inside one application container, exposed through a defined interface.
- **Code-level design:** selective detail about modules, classes, functions, schemas, or internal collaboration when needed for implementation understanding.

## Hierarchy Rules

- Put each component inside exactly one owning application container.
- Do not place frontend and backend components in one flat list.
- Model databases and other data stores as containers. Use `data-model.md` for their internal data design instead of creating artificial application components.
- Label every relationship with its purpose and direction.
- Use clear names and descriptions that explain responsibility.

## View Selection

Create by default:

- System Context view for the software system in scope.
- Container view for the software system in scope.

Create only when useful:

- Component view for a significant application container.
- Dynamic view for an important cross-container or cross-component flow.
- Deployment view when runtime topology, environment, scaling, security, or operations matter.
- Code-level diagram when internal design is genuinely complex or high-risk.

Every view must have a clear title, scope, intended audience, notation explanation, and stable view key.

## Structurizr DSL View Guardrails

These rules prevent common parser failures. Apply them before saving `diagrams/workspace.dsl`.

### Dynamic Views

- A Dynamic view may only reference elements that are valid for its scope.
- If a Dynamic view references components inside one container, scope the view to that container, for example:

```dsl
dynamic application "MainFlow" {
    person -> uiComponent "Starts workflow"
    uiComponent -> domainComponent "Delegates work"
}
```

- Do not scope such a view to the parent software system. Structurizr rejects components in a Dynamic view scoped to a software system.
- Every relationship listed in a Dynamic view must already exist in the model section with the same source and destination. Dynamic views show ordered instances of model relationships; they do not create relationships.
- If a person interacts with a component in a Dynamic view, add an explicit model relationship such as `user -> uiComponent "Interacts with"` before the view.
- If the flow crosses containers, either scope the Dynamic view to the lowest common valid parent and reference container-level relationships, or create the missing container-level relationships in the model. Do not mix component-level steps from different containers unless Structurizr accepts that scope.

### Deployment Views

- Deployment nodes and container instances belong in the `model` section under a named `deploymentEnvironment`.
- A Deployment view references the software system and deployment environment name; it does not define deployment nodes inline.
- Use this pattern:

```dsl
model {
    softwareSystem = softwareSystem "Software System" {
        application = container "Application" "Provides behavior." "Technology"
    }

    deploymentEnvironment "Local" {
        deploymentNode "Runtime" "Execution environment" "Technology" {
            containerInstance application
        }
    }
}

views {
    deployment softwareSystem "Local" "LocalDeployment" {
        include *
        autoLayout lr
    }
}
```

- Do not write `deployment softwareSystem "ViewKey" { ...deploymentNode... }`. Structurizr interprets the second argument as an environment name and will fail if that environment is missing.
- Keep the deployment view key stable and separate from the environment name when clarity helps, for example environment `Local` and view key `LocalDeployment`.

## Diagram Folder Contract

Use this structure:

```text
02_architecture/
└── diagrams/
    ├── workspace.dsl
    ├── docker-compose.yml
    └── images/
        ├── <exported-view>.svg
        └── <exported-view>.png
```

- Keep diagram source, local viewer configuration, and generated images together.
- Treat `workspace.dsl` as the source of truth.
- Treat files in `images/` as generated artifacts.
- Do not store hand-edited variants of a Structurizr view in `images/`.
- Use clear, stable filenames. Prefer a filename derived from the view key when the exporter permits it.
- Remove or replace exports for retired view keys so the folder does not misrepresent the current architecture.

## Structurizr Viewing and Export

Run the local viewer from the diagram folder:

```bash
docker compose up
```

Or run it from the repository root:

```bash
docker compose -f sdlc_docs/02_architecture/diagrams/docker-compose.yml up
```

`docker compose config` validates only the Docker Compose file. It does not parse `workspace.dsl` and must not be used as the only Structurizr validation.

To validate the DSL with the local viewer, start or restart the viewer and inspect fresh logs for parser errors:

```bash
docker compose -f sdlc_docs/02_architecture/diagrams/docker-compose.yml restart
docker compose -f sdlc_docs/02_architecture/diagrams/docker-compose.yml logs --since 30s
```

If logs contain `StructurizrDslParserException`, fix the DSL and repeat until the fresh logs are clean. Only then record Structurizr rendering as validated.

When an installed Structurizr CLI supports PNG or SVG export, run the export from `diagrams/`, for example:

```bash
structurizr.sh export -workspace workspace.dsl -format svg -output images
```

In case automatic export will be not possible, the software architect is responsible to export manually the images. This should be a mandatory instruction.

Use the actual executable name provided by the installation. Prefer SVG. Use PNG when SVG is not supported by the target documentation renderer.

PNG and SVG export may require a Structurizr CLI build with browser-rendering support and local browser dependencies. The prebuilt local-viewer Docker image must not be assumed to provide image export. When automated export is unavailable:

- record the export status and limitation;
- use a project-approved manual export process when available;
- do not generate a misleading placeholder;
- do not replace the canonical C4 model with a Mermaid copy.

After exporting:

1. Verify that each image corresponds to the intended view key.
2. Inspect the image for clipped labels, unreadable text, missing elements, and incorrect layout.
3. Record the image path and export status in the relevant architecture section.
4. Embed the image using a relative Markdown path, for example:

```markdown
![C4 System Context view](diagrams/images/system-context.svg)
```

5. Re-export after any semantic workspace or layout change.

## Structurizr Modeling Rules

- Keep one canonical `workspace.dsl` until maintenance requires decomposition.
- Use descriptive internal DSL identifiers such as `customer`, `storefrontApplication`, and `commerceDatabase`. These are internal references only.
- Keep model names human-readable and independent from code naming.
- Keep the workspace, exported images, architecture document, traceability, and detailed documents consistent.
- Do not duplicate the canonical C4 model in Mermaid.

## Supplementary Diagrams

Use Mermaid or another project-approved notation only where it communicates non-C4 detail more clearly, such as:

- sequence diagrams;
- state diagrams;
- class or package diagrams;
- entity-relationship diagrams;
- small algorithm or data-flow explanations.

Keep supplementary diagram source in the Markdown document that explains it unless reuse or complexity justifies a separate source file. Do not place supplementary exports in `diagrams/images/` unless the project intentionally treats that folder as the common generated-image destination.

## Primary References

- arc42 documentation: https://docs.arc42.org/home/
- C4 model diagrams: https://c4model.com/diagrams
- Structurizr DSL: https://docs.structurizr.com/dsl
- Structurizr local quickstart: https://docs.structurizr.com/local/quickstart
- Structurizr export command: https://docs.structurizr.com/export
- Structurizr PNG and SVG export: https://docs.structurizr.com/export/png-and-svg
