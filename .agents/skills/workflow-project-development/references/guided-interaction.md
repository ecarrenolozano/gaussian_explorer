# Guided Interaction

## Audience Assumption

Assume the user may understand the scientific or domain problem better than software-development terminology. Explain terms at first use without becoming verbose.

Examples:

- **Requirement batch:** a recorded group of related ideas and clarifications.
- **User story:** a small description of a user need and its value.
- **Approval gate:** a point where an authorized person confirms that a specific version may proceed.
- **Architecture:** the high-level organization and responsibilities of the system.
- **Release candidate:** the exact build being considered for acceptance and deployment.

## Start or Resume Presentation

Use this shape:

```text
Project workflow

You are currently at: <plain-language stage>

Completed:
- <stage>

Needs attention:
- <blocker or stale item>

Next recommended step:
<action and short reason>
```

Then identify the specialist skill in a secondary line. Do not lead with internal skill names for guided users.

## Questions

Ask a question only when:

- the repository root is unknown;
- the intended project or scope is ambiguous;
- multiple eligible batches, stories, issues, or environments require a human selection;
- an approval decision is required;
- the selected specialist skill requires missing information;
- an external write or consequential action requires confirmation.

Prefer one focused question at a time. Offer a small number of concrete choices when available.

## Approvals

Before an approval gate, explain:

1. what artifact and version are being approved;
2. what the approval permits next;
3. what it does not mean;
4. who must make the decision.

Never treat "looks good" as approval when the specialist skill requires a formal version-specific decision. Let that specialist apply its approval contract.

## Blockers

State blockers in plain language and give one repair route:

```text
Architecture cannot continue because the current user-story version has not been product-approved. The next step is a product-readiness review using d-user-story-product-readiness.
```

Do not expose every downstream consequence unless the user asks for expert detail.

## Completion

After a stage completes, summarize:

- what changed;
- the artifact or decision created;
- whether approval is still pending;
- the next eligible stage.

Ask before automatically entering the next consequential stage.
