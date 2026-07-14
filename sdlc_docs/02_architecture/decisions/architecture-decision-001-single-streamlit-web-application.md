# Architecture Decision 001: Single Streamlit Web Application

- Status: `accepted`
- Date: `2026-07-14`
- Owners: Software engineers
- Architecture version: `1.0`
- Related user stories: `US-0001`, `US-0002`, `US-0003`, `US-0004`, `US-0005`, `US-0006`, `US-0007`, `US-0008`
- Related architecture areas: System context, Container view, Streamlit web application

## Context

The approved product scope requires a Streamlit application for researchers to upload CSV data, choose variables, configure and fit GPR, view uncertainty, and export results. No approved story requires user accounts, database storage, external integrations, collaboration, batch processing, or deployment automation.

## Decision

Architecture version `1.0` uses one Streamlit web application as the only independently running application.

## Alternatives Considered

- Separate frontend and backend applications. This adds service boundaries and operations without an approved product need.
- Notebook or command-line workflow. This conflicts with the approved Streamlit web application requirement.
- Streamlit application plus database. Server-side persistence and database storage are explicitly out of scope unless later requested.

## Rationale

A single Streamlit web application is the least complex architecture that satisfies the approved stories while preserving the confirmed Streamlit constraint and keeping the first version easy to extend.

## Consequences

### Positive

- Minimal runtime and deployment surface.
- Direct fit for the approved researcher workflow.
- Clear future extension point if persistence, collaboration, or batch processing is later approved.

### Negative and Trade-offs

- Multi-service scaling, background processing, and collaborative workflows are not addressed in architecture version `1.0`.
- Large files must be rejected or constrained before analysis because the workflow is in-memory.

### Operational, Security, Migration, and Maintenance Effects

- Operations focus on one Streamlit runtime.
- CSV upload is the primary trust boundary.
- Future persistence or multi-service changes require a new architecture version.

## Validation

All active stories map to the Streamlit web application; no active story requires another independently running application.

## Follow-up

Accepted as part of architecture version `1.0` approval.
