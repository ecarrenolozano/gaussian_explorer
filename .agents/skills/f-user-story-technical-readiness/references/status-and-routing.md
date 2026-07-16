# Status and Routing

Assign one primary status:

- `implementation-ready`: architecture path and implementation context are sufficient.
- `needs-requirement-clarification`: a missing product decision blocks interpretation.
- `needs-story-revision`: the story, acceptance, priority, or traceability is defective.
- `needs-architecture-change`: architecture structure, design, mapping, interface, data, deployment, or decision work is required.
- `needs-technical-spike`: a bounded investigation is required before implementation.
- `blocked-external`: an external dependency or authority blocks progress.
- `blocked-state`: canonical artifacts or approvals are inconsistent.

Route to the first owning stage that must act. Record secondary findings separately. Only `implementation-ready` stories may become publication-eligible.
