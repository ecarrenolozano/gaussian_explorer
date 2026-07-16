# Persistence and Readiness

Use a plan filename that references the repository issue without prescribing code names, for example `issue-42-implementation-plan.md`.

For new incremental work, store issue plans inside a planning batch:

```text
sdlc_docs/03_implementation/planning_batches/batch-<nnn>/plans/issue-42-implementation-plan.md
```

Use existing flat `sdlc_docs/03_implementation/plans/` files only for legacy or small projects that already use that convention.

Bind each plan version to:

- issue IDs;
- source story IDs and version;
- architecture version;
- technical review;
- relevant arc42 concerns;
- software system, container, component or data model;
- runtime or deployment concern;
- related architecture decisions;
- repository revision;
- planning batch ID;
- reconciliation batch ID when applicable;
- plan assessment and approval when required.

A material change to scope, architecture path, files, migration, sequencing, quality tactics, observability, configuration, code-level diagrams, or verification creates a new plan version.

The roadmap is a living document. Preserve planning-batch history when refreshing the current roadmap view. Do not erase older batches to make the current ready queue look cleaner.

Assess:

- `ready`;
- `ready-with-open-items`;
- `changes-required`;
- `blocked`.
