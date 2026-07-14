# Migrations and Deployment Procedure

## Migrations

For each database, data, configuration, or infrastructure migration, record:

- purpose and affected systems;
- prerequisites and backup requirements;
- compatibility with the current and new release;
- execution order and expected duration;
- expected service impact;
- verification and failure signals;
- recovery approach;
- responsible owner.

Do not assume reversibility. State whether recovery uses rollback, restoration, replay, or a forward correction.

## Deployment procedure

Use ordered steps with:

- responsible role;
- prerequisite;
- action;
- expected result;
- verification;
- failure or pause condition.

Commands must come from verified repository or operational documentation. Mark unknown commands as unresolved rather than generating plausible commands.
