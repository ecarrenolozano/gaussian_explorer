# Architecture Decision 001 - Streamlit In-Memory MVP

- Status: `accepted`
- Date: `2026-07-14`
- Decision makers: Edwin Carreno
- Related stories: US-0001, US-0002, US-0003, US-0004, US-0005, US-0006, US-0007, US-0008
- Affected arc42 sections: 2, 3, 4, 5, 6, 7, 8, 10, 11
- Affected architecture elements: Streamlit Web Application; In-memory Analysis Session

## Context and Problem

The approved MVP requires a Streamlit application for small experimental datasets. Researchers need upload, variable selection, GPR configuration, fitting, visualization, export, and invalid-input feedback. The clarified scope excludes user accounts, server-side persistence, collaboration, database storage, batch processing, and deployment automation.

## Decision Drivers

- The application shall be built with Streamlit.
- Small experimental datasets can be processed in memory.
- Reproducibility is satisfied through exported settings, selected variables, prediction results, plot output, and metadata.
- The MVP should remain simple and implementable without introducing persistence that product scope does not require.

## Considered Options

| Option | Summary | Outcome |
|---|---|---|
| Single Streamlit application with in-memory session state | One runtime app owns UI, orchestration, and active analysis state. | Selected. |
| Streamlit frontend plus backend API and database | Split UI, compute, and persisted sessions. | Rejected for MVP because it adds infrastructure outside scope. |
| Notebook or command-line workflow | Avoids web app runtime. | Rejected because the requester explicitly asked for a Streamlit application. |

## Decision

Build the MVP as a single Streamlit web application that keeps uploaded data, selected variables, model settings, prediction results, visualization state, and generated exports in memory for the active analysis session.

## Consequences

### Positive

- Matches the approved Streamlit requirement directly.
- Keeps the MVP architecture small and easy to understand.
- Avoids premature database, account, or deployment infrastructure.
- Supports fast iteration and local testing for small datasets.

### Negative

- Active analysis state is lost when the Streamlit process or session ends.
- Horizontal scaling is constrained because state is not shared.
- Large datasets and long-running analyses are intentionally outside the design center.

### Risks

- Future persistence or collaboration requirements would require an architecture change.
- Implementation must enforce file-size and row-count limits to protect process memory.

## Validation

- Product approval confirms Streamlit and in-memory small-dataset assumptions.
- Architecture traceability maps all active stories to the Streamlit Web Application and In-memory Analysis Session.
- Implementation planning must define concrete upload limits and session-state handling.

## Supersedes

None.

## Superseded By

None.
