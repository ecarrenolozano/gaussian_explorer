# Migrations and Deployment Procedure

Tie every migration to an owning data-store or infrastructure container and verify it against the approved deployment and runtime architecture.

Record:

- prerequisites and backups;
- compatibility window;
- migration order;
- application, worker, data-store, cache, broker, and external-integration order;
- quality or risk conditions that affect sequencing;
- exact commands only when repository-supported and reviewed;
- pause and abort conditions;
- verification after each major step;
- owner and decision authority.

Unknown commands or unsafe migration behavior are blockers, not placeholders to invent.
