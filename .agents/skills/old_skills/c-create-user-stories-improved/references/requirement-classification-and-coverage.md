# Requirement Classification and Coverage Audit

Load during Steps 3 and 5.

## Classify Before Drafting

Classify each meaningful source statement as exactly one primary type:

- **User outcome:** an actor needs an observable capability for a supported value.
- **Workflow/state behavior:** a user-visible transition, mode, or interaction rule.
- **Business rule:** domain behavior that constrains a story or acceptance scenario.
- **Validation/error behavior:** supported failure, boundary, or recovery behavior.
- **Data/input/output requirement:** required data, artifact, or exchange format.
- **Reproducibility requirement:** what must be retained, exported, or replayed.
- **Quality attribute/NFR:** usability, performance, security, maintainability, extensibility, portability, reliability, accessibility, or similar.
- **Solution proposal:** framework, library, architecture, database, API, algorithm, or deployment choice.
- **Assumption:** an explicitly recorded temporary belief.
- **Open question:** unresolved information that affects scope or acceptance.
- **Exclusion:** explicitly out-of-scope behavior.

Do not classify a solution proposal as a confirmed constraint unless project context or the handoff explicitly records it as approved.

## Coverage Dispositions

Every classified statement must be mapped to one of:

- new story;
- existing story;
- acceptance criterion;
- NFR or measurable quality constraint;
- decision item;
- open question;
- explicit exclusion;
- duplicate/covered elsewhere.

No meaningful statement may remain unmapped.

## Completeness Lenses

Use these prompts to detect missing clarification. Do not invent answers.

### End-to-end workflow

- How does the user start?
- What must be configured?
- What action triggers processing?
- What feedback confirms success or failure?
- What can the user do with the result?
- Can the result be reused later?

### Data lifecycle

- Accepted formats and size limits?
- Variable selection and preprocessing?
- Missing, duplicate, malformed, or unsupported data?
- In-memory versus persisted data?

### Model lifecycle

- Initial versus fitted parameters?
- Fixed versus optimized parameters?
- Model-family-specific controls?
- Fit, refit, stale-state, and reset behavior?
- Inference on new values?
- Export, load, and reuse of the fitted model?

### Interaction and state

- Live update or explicit action?
- What happens when a toggle changes?
- Which values are editable, derived, fitted, or read-only?
- What becomes stale after configuration changes?

### Outputs and reproducibility

- Prediction table, plot, metadata, model artifact, software versions?
- What is sufficient to reproduce versus merely document the analysis?

### Technology and architecture

- Is a named framework mandatory, preferred, or assumed?
- What criteria should be used to compare alternatives?
- Does the requested solution satisfy dynamic UI, plotting, state, download, deployment, and extensibility needs?

### Terminology and usability

- Are scientific terms aligned with the domain source?
- Are units, variance versus standard deviation, and fixed versus optimized values unambiguous?

## Coverage Quality Gate

Before persistence, confirm:

- every source statement has a coverage row;
- every story traces to one or more source statements;
- every solution proposal has an explicit status;
- vague requirements have either measurable criteria or an open question;
- no story exists solely to implement a technical layer;
- missing lifecycle or state behavior is surfaced rather than silently omitted.
