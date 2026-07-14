# Architecture Decision 002: In-Memory Session and Export Reproducibility

- Status: `accepted`
- Date: `2026-07-14`
- Owners: Software engineers
- Architecture version: `1.0`
- Related user stories: `US-0001`, `US-0002`, `US-0003`, `US-0004`, `US-0005`, `US-0006`, `US-0007`, `US-0008`
- Related architecture areas: Data ownership, Export generation, In-memory analysis session

## Context

The clarified handoff explicitly assumes small experimental datasets can be processed in memory. It also states that reproducibility can be satisfied through exported settings, selected variables, prediction results, and plot metadata rather than server-side saved sessions. Server-side persistence, database storage, user accounts, and collaborative workflows are out of scope.

## Decision

Architecture version `1.0` keeps uploaded data, selected variables, model settings, fitted results, visualization state, and export metadata in the in-memory analysis session for the active workflow. Reproducibility is provided through export artifacts.

## Alternatives Considered

- Persist every analysis to a database. This is out of scope and introduces unapproved data ownership and retention decisions.
- Save server-side analysis history in files. This still creates persistence behavior not approved by the product gate.
- Require researchers to reproduce analyses manually without exported metadata. This does not satisfy the approved reproducibility expectation.

## Rationale

In-memory state matches the small-dataset assumption and avoids inventing persistence requirements. Export artifacts satisfy reproducibility while keeping long-lived artifact ownership with the researcher after download.

## Consequences

### Positive

- Keeps data lifecycle simple and bounded.
- Avoids unsupported account, retention, shared storage, and database decisions.
- Supports tabular, visual, and metadata exports.

### Negative and Trade-offs

- Past analyses are not available from the application after the active session ends.
- Researchers are responsible for retaining downloaded export artifacts.
- Very large files must be rejected or constrained to protect the in-memory workflow.

### Operational, Security, Migration, and Maintenance Effects

- No persistent application data store is introduced in architecture version `1.0`.
- Export generation must use the same active analysis state as visualization.
- Future server-side persistence requires new product approval and a new architecture version.

## Validation

`US-0006` and `US-0007` are satisfied through export artifacts; no active story requires server-side saved sessions.

## Follow-up

Accepted as part of architecture version `1.0` approval.
