# Technical Spike Candidate Rules

Load only when Step 5 assigns `needs-technical-spike`.

A spike is appropriate only when a specific decision cannot be made responsibly from current evidence. It must reduce uncertainty, not deliver production functionality.

Use `templates/technical-spike-candidate.md` and define:

- one decision-oriented question;
- why existing story, architecture, repository, or environment evidence is insufficient;
- affected story IDs and architecture elements;
- a bounded time box or effort limit supplied by the team, or `Unconfirmed` when absent;
- explicit investigation boundaries;
- required evidence, prototype, benchmark, compatibility check, recommendation, or ADR input;
- a completion condition tied to making a decision;
- the route after completion.

Do not invent a time box, success threshold, tool, or implementation approach. Do not use a spike for routine coding, detailed design that can be decided normally, or work already required by an implementation story.

This skill records a spike candidate only. `g-create-repository-issues` owns publication and repository identifiers.
