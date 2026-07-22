# Invalidation and Repair Rules

## General Rule

A downstream artifact is current only when it references the exact upstream identifiers and versions on which it depends. When an upstream semantic change occurs, mark dependent downstream evidence as stale until its owning skill reassesses it.

Do not delete historical approvals or reports. Preserve them as history and create or record a new current review according to the owning skill.

## Common Invalidation Paths

| Changed artifact or decision | Potentially stale downstream stages | Route first |
|---|---|---|
| Project context scope, stakeholder, constraint, or terminology | B through K as affected | Skill A, then reassess affected stages |
| Clarified requirement batch | C through K for mapped stories | Skill B, then Skill C |
| User-story behavior, acceptance condition, scope, or active set | D through K | Skill C, then Skill D |
| Product-readiness decision | E through K | Skill D |
| Architecture responsibility, boundary, interface, data ownership, or decision | F through K | Skill E |
| Technical-readiness result or approved story set | G through K | Skill F |
| Repository issue scope or linkage | H and related implementation/test/validation records | Skill G |
| Implementation plan | implementation handoff and affected test strategy | Skill H |
| Implementation artifact or code revision | I through K | implementation execution, then Skill I |
| Automated test result, environment, or tested artifact | J and K | Skill I |
| Acceptance decision or release candidate | K | Skill J |
| Deployment environment, artifact, migration, rollback, or material risk | deployment approval | Skill K |

## Semantic Versus Editorial Change

Treat a change as semantic when it affects behavior, scope, constraints, architecture meaning, implementation intent, evidence, release content, environment, or risk. Reassess downstream state.

Treat spelling, formatting, and wording changes as editorial only when meaning and identifiers remain unchanged. Do not invalidate downstream artifacts solely for an editorial correction, but preserve revision history where required.

When uncertain, mark the relationship `needs-review` rather than declaring it current.

## Repair Routing

- Missing or contradictory requirement evidence → Skill B.
- Story or traceability defect → Skill C; product approval afterward through Skill D.
- Product-review defect → Skill D.
- Architecture defect → Skill E.
- Technical feasibility or readiness defect → Skill F.
- Missing, direct, duplicated, or divergent repository issue → Skill G reconciliation.
- Plan defect → Skill H.
- Missing automated evidence or failed technical test → Skill I after implementation correction where needed.
- Manual behavior failure or stakeholder decision → Skill J, with defects routed to their owners.
- Deployment-plan defect → Skill K.

Do not use the wrapper to edit an artifact simply because its owner is obvious. Delegate the repair.
