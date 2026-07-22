# Input and Version Gate

Verify:

- current story version and active story IDs;
- product approval for that exact story version;
- current architecture version and approval for that story version;
- one consistent architecture marker across `00_architecture_document.md` and `01_architecture_traceability.md`;
- existence of `workspace.dsl` and all architecture documents referenced by reviewed stories;
- relevant arc42 sections are populated, explicitly not applicable, or marked open;
- no newer story or architecture version makes approval stale;
- no duplicate current technical gate marker.

Stop and assign `blocked-state` when canonical state is missing, contradictory, or stale. Do not repair upstream files in this skill.
