# Architecture Decision 002 - Modular Analysis Pipeline

- Status: `accepted`
- Date: `2026-07-14`
- Decision makers: Edwin Carreno
- Related stories: US-0001, US-0002, US-0003, US-0004, US-0005, US-0006, US-0007, US-0008
- Affected arc42 sections: 4, 5, 6, 8, 10, 11
- Affected architecture elements: Workflow UI; CSV parsing and validation; Variable and GPR settings; GPR fitting and prediction; Prediction and uncertainty visualization; Export generation; Active analysis state

## Context and Problem

The MVP combines several responsibilities in one user workflow: data intake, validation, variable selection, model configuration, fitting, visualization, and export. The clarified requirements also ask for modular code that can support future extension.

## Decision Drivers

- Invalid-input handling spans upload, variable selection, and fitting.
- Exported artifacts must match the fitted analysis shown to the user.
- Future extension should be possible without rewriting the full UI workflow.
- Components should be testable outside the Streamlit widget layer where practical.

## Considered Options

| Option | Summary | Outcome |
|---|---|---|
| Modular internal components behind the Streamlit workflow | Keep one runtime app but separate parsing, validation, settings, fitting, visualization, and export responsibilities. | Selected. |
| Put all logic directly in the Streamlit script | Fastest initial implementation but hard to test and extend. | Rejected because it conflicts with the modularity requirement. |
| Split responsibilities into independent services | Strong isolation but adds deployment and integration cost. | Rejected for MVP because deployment automation and distributed runtime are out of scope. |

## Decision

Organize the Streamlit Web Application into cohesive internal components for workflow UI, CSV parsing and validation, variable and GPR settings, GPR fitting and prediction, prediction visualization, and export generation. Generate result exports from the same active analysis state used for visualization.

## Consequences

### Positive

- Each story has a clear owning component and validation point.
- Scientific outputs remain aligned because visualization and exports use the same fitted state.
- Core parsing, validation, fitting, and export behavior can be unit tested without relying solely on UI tests.
- Future kernels, charts, or export formats can be added behind stable workflow boundaries.

### Negative

- The implementation needs small module boundaries earlier than a one-file prototype would.
- Shared data structures for selected variables, settings, predictions, and metadata must be kept coherent.

### Risks

- Overly rigid module names could slow implementation; the architecture treats proposed paths as guidance, not mandated filenames.
- If export generation diverges from visualization state, reproducibility can be undermined.

## Validation

- Architecture traceability maps all active stories to the relevant components.
- Existing repository evidence confirms initial CSV intake support in `src/gaussian_explorer/data.py`.
- Implementation planning should refine concrete module names and data structures while preserving these responsibilities.

## Supersedes

None.

## Superseded By

None.
