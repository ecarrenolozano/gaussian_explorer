# Product-Domain Category Selection

Load this file during Step 5.

Prefer project categories explicitly recorded in `project_context.md`. Otherwise infer cautiously from documented product behavior and state the selected categories. Load only overlays that introduce material product-readiness risk.

| Overlay | Select for |
|---|---|
| `overlay-interface-and-accessibility.md` | Web, mobile, desktop, interactive, multilingual, or accessibility-sensitive user experiences |
| `overlay-workflow-and-integration.md` | Enterprise workflows, approvals, external integrations, developer-facing contracts, or migration behavior |
| `overlay-data-ai-science.md` | Data-intensive, analytical, scientific, research, AI, or machine-learning outcomes |
| `overlay-regulated-and-high-consequence.md` | Privacy, cybersecurity, financial, healthcare, safety-critical, or other specialist-governed outcomes |
| `overlay-device-and-real-time.md` | Embedded, IoT, edge, sensor, actuator, device-lifecycle, real-time, or control behavior |
| `overlay-distributed-and-operations.md` | Cloud, distributed, multi-region, availability, support, incident, or observability-sensitive outcomes |

A project may use multiple overlays. Do not load an overlay solely because a technology might be used internally.
