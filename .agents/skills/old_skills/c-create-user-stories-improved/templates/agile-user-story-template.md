# Agile User Story Template

A User Story represents a small piece of business value that a team can deliver in an iteration.

User Stories are not simply requirements, user stories answer this:
- Who is this for?
- What do they need?
- Why do they need?

Each User Story contains the following sections:

1. A brief description of the need and business value.
2. A traceability component that includes source and constraints.
3. Any assumption or details
    - For instance: if an application requires persistance, and it is known that it will be a RDBM, we can use that information as an assumption.  

4. The definition of "done"
    - How we know when this user story is completed?
    - Acceptance Criteria should answer that question.

Remove all bracketed guidance from the completed story. Omit optional bullets that have no supported content.

## US-XXXX - <concise user-outcome title>

<!-- story-id: US-XXXX | source-batch: PRDB-XXX | priority: MVP | lifecycle: active -->

### Description

**As a** <some role>
**I need** <some functionality>
**So that** <some benefit>

### Assumptions & Details

- <List of assumptions>
- <Document any details that may help the developers to understand the story and complete it>

### **Source and constraints**

- Source batch: `PRDB-XXX (YYYY-MM-DD)`
- Source requirement or decision: <concise evidence label>
- Confirmed constraints: <optional>
- Explicit assumptions: <optional; only assumptions recorded in the handoff>
- Open questions: <material unresolved items or `None`>

#### **Scenario: <observable primary outcome>**

Given <starting state or context>
When <user action or event>
Then <observable result>

<!-- Add supported alternate, negative, permission, validation, boundary, or failure scenarios as needed. -->