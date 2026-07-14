# Input and Publication Gate

## Eligible story issue

Require all of the following:

- current story identifier and story version;
- current architecture version;
- applicable technical review identifier;
- per-story status `implementation-ready`;
- explicit human technical approval covering that story and those versions;
- no newer overlapping technical review or stale upstream approval.

## Eligible spike issue

Require an explicit spike candidate in the technical-readiness report and human authorization to publish it.

## Other work types

Publish architecture changes, migrations, enabling work, or dependencies only when an authoritative upstream artifact defines their purpose and scope. Do not infer them while formatting an issue.

## Issue lineage

Include a human-readable documentation lineage section and a machine-readable marker:

```html
<!-- workflow-link
source-type: user-story
source-identifier: US-0001
story-version: 1.0
architecture-version: 1.0
technical-review-identifier: TR-001
publication-batch-identifier: publication-001
documentation-revision: <repository-revision>
-->
```

The documentation revision should identify the repository revision containing the source documents when available.
