# Technical-Readiness Checklist

Load during Step 4. Apply only criteria relevant to the reviewed story. Record `satisfied`, `partial`, `missing`, `conflicting`, `unknown`, or `not applicable` with supporting evidence.

## 1. Lineage and Architecture Path

- Story ID, source lineage, lifecycle, versions, and approvals are valid.
- The story maps to existing architecture responsibilities, containers, components, interfaces, data, and ADRs.
- No unresolved architecture decision prevents a coherent implementation path.
- Accepted ADRs and project constraints do not conflict with the story.

## 2. Interfaces and Integrations

- Required providers, consumers, owners, and interaction purpose are known.
- Request, response, event, file, command, device, or user-interface contracts are sufficiently defined for implementation.
- Compatibility, versioning, ordering, idempotency, timeout, retry, cancellation, and partial-failure behavior are addressed when material.
- External systems, teams, vendors, credentials, sandboxes, and availability dependencies are visible.

## 3. Data and State

- Authoritative sources and data ownership are known.
- Required fields, validation, units, precision, schema evolution, lifecycle, retention, deletion, and migration effects are understood where relevant.
- Concurrency, consistency, duplication, correction, replay, recovery, and audit behavior are bounded when material.
- Test data, privacy constraints, and environment-specific data needs are known.

## 4. Security, Privacy, and Safety

- Authentication, authorization, trust boundaries, and sensitive data paths are understood.
- Secret handling, logging, audit, minimization, retention, misuse, and abuse concerns are addressed where applicable.
- Required safe states, protective behavior, specialist evidence, or human validation are identified for high-consequence work.
- Technical controls support rather than reinterpret approved product behavior.

## 5. Quality Attributes

- Relevant latency, throughput, volume, availability, consistency, accuracy, compatibility, accessibility, resource, or recovery expectations are measurable or explicitly deferred.
- Architecture choices plausibly support those expectations.
- Failure handling, fallback, observability, diagnostics, and recovery evidence are defined where needed.
- No unsupported threshold is introduced to make the story appear ready.

## 6. Delivery and Operations

- Configuration, feature flags, rollout, rollback, migration, coexistence, and release dependencies are understood when relevant.
- Required monitoring, alerts, dashboards, runbooks, support, and documentation impacts are identified.
- Environment, infrastructure, hardware, certificate, policy, procurement, or external-team prerequisites are visible.
- Ownership exists for enabling or cross-cutting work.

## 7. Verification

- Acceptance criteria can be implemented as meaningful tests without inventing product behavior.
- Required unit, contract, integration, end-to-end, performance, security, accessibility, hardware, numerical, migration, or recovery evidence is identified where applicable.
- Required environments, fixtures, simulators, datasets, tools, and specialist review are available or explicitly blocked.
- Completion evidence is distinguishable from implementation activity.

## 8. Size, Dependencies, and Sequencing

- The story is small enough for the team's normal delivery unit or has a documented exception.
- Dependencies and sequencing are explicit.
- Any proposed split represents independently valuable or independently verifiable work, not frontend/API/database layers.
- Genuine research uncertainty is separated from implementation and can be answered by a bounded spike.

## Severity

- **blocking:** prevents safe implementation, reliable verification, or valid routing.
- **major:** likely to cause incorrect behavior or substantial rework.
- **moderate:** materially improves delivery confidence but does not block.
- **minor:** low-risk clarity or maintainability improvement.

A numeric or checklist majority never overrides a blocking finding.
