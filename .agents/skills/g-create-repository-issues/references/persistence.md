# Persistence

Update the registry only after issue identity is verified. Preserve previous mappings and reconciliation history.

When issue creation succeeds but registry persistence fails, record partial completion with the verified issue number and repair the registry later. Do not create a replacement issue.

Store the exact documentation revision when available so issue scope can be compared with the source state used for publication.
