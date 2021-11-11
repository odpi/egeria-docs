---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Entity Restore Profile

The performance of programmatically reversing the latest soft-delete of an existing entity instance.

The [Open Metadata Repository Services (OMRS)](/egeria-docs/services/omrs) interface for a metadata repository defines an optional method for reverting soft-deletes on entity instances:

| Method | Description |
|---|---|
| `restoreEntity` | reverts the last soft-delete that was made to an entity |

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | `repository-entity-restore-performance-restoreEntity` | See (2) in detailed logic below. |

For every entity type supported by the technology under test, this profile does the following (in order):

1. Searches for `instancesPerType` entity GUIDs of that type that have been soft-deleted. (This uses `findEntitiesByProperty` with a condition to limit to the status `DELETED` only and its performance is recorded as part of the [entity search](entity-search.md) profile.)
1. For each of these entity GUIDs, `restoreEntity` is called to revert the soft-delete and make the entity active again.

!!! example "Example"
    So, for example, if the technology under test supports 50 entity types, and the `instancesPerType` parameter is set to 100, then this profile will re-activate 50 (types) x 100 (instances per type) = 5000 entities. (And it will run `findEntitiesByProperty` 50 times.)

--8<-- "snippets/abbr.md"
