# Platform and Write Safety

- Read repository-native issue forms and contribution rules before drafting.
- Prefer existing labels and milestones; do not create new ones without approval.
- Do not assign people without explicit instruction.
- Preview every issue and metadata mutation.
- Preview every issue relationship mutation, including GitHub sub-issue links and GitLab issue links.
- Preview delivery-plan guidance separately from issue writes. Priority order and parallelization groups are planning metadata, not repository writes, unless the user explicitly approves labels, milestones, projects, issue types, or assignees to represent them.
- Batch approval is valid only when every planned write is enumerated.
- Verify issue URLs and identifiers after creation.
- For GitHub, use native sub-issues for approved parent/child story relationships when available. To create a new sub-issue, use `gh issue create --parent <parent-number-or-url>`. To add an existing issue as a sub-issue, use `gh issue edit <parent-number-or-url> --add-sub-issue <child-number-or-url>`.
- For GitHub dependency edges that cannot be represented as sub-issues because a child would need multiple parents, use native issue dependencies with `gh issue edit <dependent-number-or-url> --add-blocked-by <dependency-number-or-url>` when available.
- For GitLab, use linked issues through the issue links API when available. Use `blocks` or `is_blocked_by` for dependency relationships and `relates_to` only for non-directional relationships or fallback.
- Do not create multiple repository issues for one source story just to satisfy platform hierarchy. If a source story would need multiple parents, preview a warning and use dependency links/body references unless the user explicitly approves a single-parent choice.
- When a write result is uncertain, search for the lineage marker before retrying.
- When no repository connector is available, produce drafts only and state that publication did not occur.
