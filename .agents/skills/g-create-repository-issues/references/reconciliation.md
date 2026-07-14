# Reconciliation

Classify each repository issue as:

- `linked`: valid lineage and registry entry exist;
- `missing-from-registry`: valid issue lineage exists but no registry entry exists;
- `missing-repository-lineage`: registry entry exists but issue lineage is absent or malformed;
- `candidate-match`: probable relationship requires human confirmation;
- `unlinked`: no workflow source can be established;
- `duplicate`: equivalent work is already represented elsewhere;
- `diverged`: issue scope materially differs from approved documentation.

Route direct issues as follows:

- new behavior or feature request -> Skill B;
- defect against approved behavior -> implementation and testing workflow;
- architecture change -> Skill E;
- technical investigation -> Skill F for spike definition;
- implementation work without approved lineage -> Skill C, D, E, and F as needed;
- unclear request -> remain unlinked until classified.

Do not automatically change approved documentation from repository issue text. Operational fields such as state, labels, and assignees may be reflected in the registry during reconciliation.
