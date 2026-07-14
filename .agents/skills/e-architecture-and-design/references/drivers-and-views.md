# Architectural Drivers and View Selection

Load during Step 2.

## Extract Drivers

Use only approved project and story evidence. Capture:

- user and business outcomes that create system responsibilities;
- external actors, systems, devices, and organizations;
- important business rules and state transitions;
- data sensitivity, ownership, lifecycle, volume, provenance, and residency;
- security, privacy, safety, accessibility, compatibility, and regulatory obligations;
- performance, latency, throughput, availability, consistency, recovery, and resource constraints;
- deployment, operational, support, migration, and organizational constraints;
- known dependencies, existing-system boundaries, and irreversible choices;
- architecture risks and unanswered technical questions.

Express important quality attributes as observable scenarios: source, stimulus, context, expected response, and measurable response where evidence supports a measure. Do not invent targets.

Prefer project categories already recorded in `project_context.md`. Otherwise infer categories cautiously and state them. Categories guide emphasis; they do not impose technology.

## Separate Evidence States

Label material items as:

- **Confirmed driver:** supported by an authoritative input.
- **Technical proposal:** a reversible design direction not yet approved.
- **Architecture assumption:** a limited technical assumption needed to continue and not a substitute for product behavior.
- **Open question:** a decision or fact still required.
- **Risk:** an uncertain event or condition with material impact.

Architecture assumptions must be explicit, reversible, and bounded. Do not assume actors, business rules, authorization, acceptance behavior, data ownership, compliance classification, or product thresholds.

## Select Views Proportionally

The C4 model describes software architecture at four levels. This skill normally uses only the first three: System Context, Container, and Component. In this model, a container means a major independently running application, service, process, or data store; it does not necessarily mean a Docker container.

Create only views that answer a material question:

- **System Context:** system ownership, people, external systems, and relationships. Use for all but truly trivial systems.
- **Container:** deployable or independently running applications, services, data stores, and responsibilities. Use when more than one major runtime or store exists.
- **Component:** internal collaboration within a complex, risky, or high-change container. Do not create for every module.
- **Dynamic or sequence:** a critical cross-boundary workflow, failure path, or asynchronous interaction.
- **Deployment:** nodes, environments, zones, devices, networks, or trust boundaries when topology affects behavior.
- **Data flow:** sensitive, regulated, scientific, high-volume, or transformation-heavy data paths.

Stop at the Component view by default. Any lower-level detail must be minimal, preliminary, and necessary to prove feasibility or remove an approval blocker.
