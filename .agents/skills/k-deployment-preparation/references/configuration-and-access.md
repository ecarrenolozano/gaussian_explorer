# Configuration, Access, and Secrets

Document only applicable items:

- deployment accounts and required permissions;
- environment-specific configuration sources;
- secret-manager references and responsible owners;
- certificates, keys, and renewal dependencies;
- feature controls and intended initial states;
- network, storage, and external-service prerequisites;
- configuration validation and restoration approach.

Never include secret values, access tokens, private keys, passwords, or confidential environment values.

When access or a required value is unavailable, name the owner and record the item as a blocker. Do not invent placeholders that could be mistaken for deployable values.
