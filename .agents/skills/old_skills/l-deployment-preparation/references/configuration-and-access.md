# Configuration, Access, and Secrets

For each affected container or managed resource, record:

- configuration source and owner;
- environment-specific values without secret content;
- secret, certificate, and key references;
- required permissions and access path;
- feature controls;
- external endpoints;
- validation method;
- rotation or expiration concerns.

Never copy secret values into deployment documentation.
