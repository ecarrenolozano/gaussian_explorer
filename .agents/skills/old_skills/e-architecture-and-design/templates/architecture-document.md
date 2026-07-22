# Software Architecture

<!-- architecture | version: 1.0 | source-story-version: 1.0 | assessment: changes-required | decision: pending -->

## 1. Introduction and Goals

### 1.1 Purpose and Scope

### 1.2 Stakeholders

| Stakeholder | Concern | Expected architecture information |
|---|---|---|

### 1.3 Quality Goals

| Priority | Quality goal | Rationale | Validation scenario |
|---|---|---|---|

## 2. Constraints

### 2.1 Technical Constraints

### 2.2 Organizational Constraints

### 2.3 Conventions

## 3. Context and Scope

### 3.1 Business Context

Describe people, external systems, responsibilities, and external information flows.

- C4 view key: `<system-context-view-key>`
- Canonical model: `diagrams/workspace.dsl`
- Exported image: `diagrams/images/<system-context-image>.svg`
- Export status: `<exported | not-exported | stale>`

![C4 System Context view](diagrams/images/<system-context-image>.svg)

Remove the image line until a current export exists at the referenced path.

### 3.2 Technical Context

Describe external interfaces, protocols, data formats, and trust boundaries.

## 4. Solution Strategy

Summarize the fundamental solution ideas and their relationship to quality goals and constraints.

## 5. Building Block View

### 5.1 Software System

### 5.2 Containers

| Container | Type | Responsibility | Technology | Detailed documentation |
|---|---|---|---|---|

- C4 view key: `<container-view-key>`
- Canonical model: `diagrams/workspace.dsl`
- Exported image: `diagrams/images/<container-image>.svg`
- Export status: `<exported | not-exported | stale>`

![C4 Container view](diagrams/images/<container-image>.svg)

Remove the image line until a current export exists at the referenced path.

### 5.3 Significant Components and Data Models

| Owning container | Component or data model | Responsibility | Detailed documentation |
|---|---|---|---|

For each selected Component view, record the view key, canonical workspace, current exported image, and export status before embedding it.

### 5.4 Selective Code-Level Design

Include only design that is architecturally significant or shared across implementation work.

## 6. Runtime View

Document important success, failure, asynchronous, recovery, or operational scenarios. Reference C4 Dynamic view keys or supplementary sequence diagrams.

For each exported Dynamic view:

- C4 view key: `<dynamic-view-key>`
- Exported image: `diagrams/images/<dynamic-view-image>.svg`
- Export status: `<exported | not-exported | stale>`

## 7. Deployment View

Describe environments, deployment nodes, container instances, managed services, network or trust boundaries, scaling, and operational ownership.

- C4 deployment view key: `<deployment-view-key or not applicable>`
- Canonical model: `diagrams/workspace.dsl`
- Exported image: `diagrams/images/<deployment-image>.svg`
- Export status: `<exported | not-exported | stale | not applicable>`

Embed the current deployment image only when the view exists and the export is current.

## 8. Cross-Cutting Concepts

### 8.1 Security and Privacy

### 8.2 Data Management

### 8.3 Configuration and Secrets

### 8.4 Error Handling and Recovery

### 8.5 Logging, Monitoring, and Observability

### 8.6 Performance and Scalability

### 8.7 Testing Strategy

### 8.8 Additional Concepts

## 9. Architecture Decisions

| Decision | Status | Related stories | Record |
|---|---|---|---|

## 10. Quality Requirements

### 10.1 Quality Scenario Summary

| ID | Stimulus and context | Expected response | Measure | Related architecture elements |
|---|---|---|---|---|

### 10.2 Quality Evaluation Notes

## 11. Risks and Technical Debt

| Risk or debt | Impact | Likelihood | Mitigation or follow-up | Owner |
|---|---|---|---|---|

## 12. Glossary

| Term | Meaning |
|---|---|

## Diagram Export Summary

| View key | View type | Image path | Format | Export status | Architecture version | Last verified |
|---|---|---|---|---|---|---|

## Architecture Validation

- Structurizr rendering:
- Docker Compose validation:
- Diagram export validation:
- Markdown image-link validation:
- Traceability validation:
- Link validation:
- Known validation gaps:

## Architecture Version and Approval

- Architecture version:
- Source story version:
- Assessment:
- Decision:
- Approver:
- Date:
- Accepted risks:
- Diagram export status:
