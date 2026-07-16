# Skill Routing

## Routing Table

| Stage | Specialist skill | Primary responsibility |
|---|---|---|
| Project context | `a-project-context-interpretation` | Interpret, complete, and govern project context according to its own contract |
| Requirements clarification | `b-requirements-clarifier` | Clarify informal requirements and create evidence-based requirement batches |
| User stories | `c-create-user-stories` | Generate and revise traceable user stories from eligible clarified batches |
| Product readiness | `d-user-story-product-readiness` | Independently review and approve the exact user-story version |
| Architecture and design | `e-architecture-and-design` | Create and approve architecture for the exact product-approved story version |
| Technical readiness | `f-user-story-technical-readiness` | Review whether selected stories are technically ready under the approved architecture |
| Repository issues | `g-create-repository-issues` | Publish approved work as repository issues, reconcile issue-to-document relationships, and cluster contributor-created issue intake |
| Implementation planning | `h-implementation-planning` | Create code-level implementation plans for approved, linked work |
| Automated testing | `i-automated-testing-and-verification` | Plan, create, select, execute, and report applicable automated verification |
| Stakeholder validation | `j-stakeholder-validation-and-acceptance` | Perform manual validation and record authorized acceptance for an exact release candidate |
| Deployment preparation | `k-deployment-preparation` | Prepare and approve an environment-specific deployment and recovery plan |

## Natural-Language Routing Examples

- "Start this project" → inspect state, then route to the earliest missing project-context or requirements stage.
- "I have an idea for a new feature" → `b-requirements-clarifier`.
- "Turn the clarified requirements into stories" → `c-create-user-stories`.
- "Are these stories ready?" → distinguish product review (`d-user-story-product-readiness`) from technical review (`f-user-story-technical-readiness`).
- "Design the system" or "continue architecture" → `e-architecture-and-design`.
- "Create repository issues" → `g-create-repository-issues` in publication mode.
- "Someone created tracker issues manually" → `g-create-repository-issues` in reconciliation mode.
- "There are many direct tracker issues, duplicates, or similar requests" → `g-create-repository-issues` in intake reconciliation mode before requirements or implementation planning.
- "Plan the implementation" → `h-implementation-planning`.
- "Add integration, end-to-end, or regression tests" → `i-automated-testing-and-verification`.
- "Validate this release with the scientist/product owner" → `j-stakeholder-validation-and-acceptance`.
- "Prepare production deployment" → `k-deployment-preparation`.

## Ambiguous Requests

For "review the stories," ask or infer from context whether the user wants:

- product fidelity and approval → Skill D;
- technical feasibility and implementation readiness → Skill F.

For "test the feature," distinguish:

- automated technical verification → Skill I;
- manual acceptance by a stakeholder → Skill J.

For "deploy the release," route preparation to Skill K and state that execution is outside Skill K.

## Delegation Procedure

1. Resolve the sibling directory under the parent `skills/` directory.
2. Read the selected `SKILL.md`.
3. Pass the verified objective, identifiers, versions, paths, and blockers.
4. Follow the specialist skill's own canonical files and references.
5. Return to the wrapper only after the specialist completes or stops.
