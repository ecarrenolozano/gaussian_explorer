# Entry and Version Gate

Proceed only when all required state is identifiable and consistent:

- exact release candidate or immutable artifact;
- included user-story identifiers and current story version;
- current automated-testing result for the same artifact;
- current stakeholder-acceptance result permitting deployment preparation;
- named target environment;
- deployment owner, rollback decision owner, and approval authority.

Treat selected-story acceptance as insufficient for a full release unless the selected stories exactly equal the declared release scope.

Stop and report `blocked` when:

- the testing or acceptance evidence refers to another artifact;
- the release candidate has changed since testing or acceptance;
- acceptance is rejected, incomplete, or outside the required scope;
- the target environment is unknown;
- required ownership or authorization is missing.

A new release candidate requires new testing and stakeholder validation unless a documented impact assessment explicitly establishes that existing evidence remains applicable.
