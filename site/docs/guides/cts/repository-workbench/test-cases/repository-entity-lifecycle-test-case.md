<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Repository entity lifecycle test case

This test validates that entities can be managed through all stages of their life cycle.

## Operation

The entity lifecycle tests extract each of the type definitions for entity and create an instance of that entity and
drive it through each phase of its lifecycle validating that the entity values are correctly maintained.

## Assertions

* **repository-entity-lifecycle-01** - `typeName` new entity created.
* **repository-entity-lifecycle-02** - `typeName` new entity has createdBy user.
* **repository-entity-lifecycle-03** - `typeName` new entity has creation time.
* **repository-entity-lifecycle-04** - `typeName` new entity has correct provenance type.
* **repository-entity-lifecycle-05** - `typeName` new entity has correct initial status.
* **repository-entity-lifecycle-06** - `typeName` new entity has correct type.
* **repository-entity-lifecycle-07** - `typeName` new entity has local metadata collection.
* **repository-entity-lifecycle-08** - `typeName` new entity has version greater than zero.
* **repository-entity-lifecycle-09** - `typeName` new entity is known.
* **repository-entity-lifecycle-10** - `typeName` new entity summarized.
* **repository-entity-lifecycle-11** - `typeName` new entity retrieved.
* **repository-entity-lifecycle-12** - `typeName` new entity is unattached.
* **repository-entity-lifecycle-17** - `typeName` entity properties cleared to min.
* **repository-entity-lifecycle-18** - `typeName` entity with min properties version number is `versionNumber`
* **repository-entity-lifecycle-19** - `typeName` entity has properties restored.
* **repository-entity-lifecycle-20** - `typeName` entity after undo version number is `versionNumber`
* **repository-entity-lifecycle-21** - `typeName` entity deleted version number is `versionNumber`
* **repository-entity-lifecycle-22** - `typeName` entity no longer retrievable after delete.
* **repository-entity-lifecycle-23** - `typeName` entity restored.
* **repository-entity-lifecycle-24** - `typeName` entity restored version number is `versionNumber`
* **repository-entity-lifecycle-25** - `typeName` entity retrieved following restore.
* **repository-entity-lifecycle-26** - `typeName` entity purged.
* **repository-entity-lifecycle-27** - `typeName` historical retrieval returned correct version of entity.
* **repository-entity-lifecycle-28** - `typeName` repository supports creation of instances.
* **repository-entity-lifecycle-29** - `typeName` repository supports undo of operations.
* **repository-entity-lifecycle-30** - `typeName` repository supports soft delete.
* **repository-entity-lifecycle-31** - `typeName` repository supports historic retrieval.
* **repository-entity-lifecycle-32** - `typeName` entity versions NOT returned before create time.
* **repository-entity-lifecycle-33** - `typeName` entity versions returned after create.
* **repository-entity-lifecycle-34** - `typeName` entity versions returned after update.
* **repository-entity-lifecycle-35** - `typeName` entity version is returned while deleted.
* **repository-entity-lifecycle-36** - `typeName` entity versions returned after restore.
* **repository-entity-lifecycle-37** - `typeName` entity versions returned after update.
* **repository-entity-lifecycle-38** - `typeName` entity versions NOT returned after purge.
* **repository-entity-lifecycle-39** - `typeName` entity is not known after purge.
* **repository-entity-lifecycle-40** - `typeName` entity versions are ordered BACKWARDS as requested.
* **repository-entity-lifecycle-41** - `typeName` entity versions are ordered FORWARDS as requested.
* **repository-entity-lifecycle-43** - `typeName` entity is known when deleted.
* **repository-entity-lifecycle-44** - `typeName` property stored with no value is returned with no value.
* **repository-entity-lifecycle-45** - `typeName` second undo of entity reinstates the update that the first undo reversed.
* **repository-entity-lifecycle-46** - `typeName` entity after second undo version number is `versionNumber`

The numbers are not contiguous: an assertion that is retired is not replaced, so that an assertion's identifier always means the same thing.

## Optional function

A repository does not have to support every part of the lifecycle.  Creating instances ([metadata maintenance](/guides/cts/repository-workbench/profiles/metadata-maintenance)), undoing updates ([undo an update](/guides/cts/repository-workbench/profiles/undo-update)), soft delete with restore ([soft delete and restore](/guides/cts/repository-workbench/profiles/soft-delete-restore)) and retrieving the history of an instance ([instance versions](/guides/cts/repository-workbench/profiles/instance-versions)) belong to optional conformance profiles.

When the repository responds to one of these operations by reporting that the function is not supported, the test case does not fail.  The assertion is recorded in the `notSupportAssertions` list of the results, instead of in `successfulAssertions` or `unsuccessfulAssertions`, and the test case moves on to the next part of the lifecycle that it is able to test.

## Sample Output

This is the output for the *Asset* type from a run against the in-memory repository, which supports all of the optional function.  The first two assertions are issued for every repository test case to confirm that the workbench is able to call the repository.

```json
{
  "class": "OpenMetadataTestCaseResult",
  "testCaseId": "repository-entity-lifecycle-Asset",
  "testCaseName": "Repository entity lifecycle test case",
  "testCaseDescriptionURL": "https://egeria-project.org/guides/cts/repository-workbench/test-cases/repository-entity-lifecycle-test-case",
  "successMessage": "Entities can be managed through their lifecycle",
  "successfulAssertions": [
    "repository-test-case-base-01: Repository connector supplied to conformance suite.",
    "repository-test-case-base-02: Metadata collection for repository connector supplied to conformance suite.",
    "repository-entity-lifecycle-28: Asset repository supports creation of instances ",
    "repository-entity-lifecycle-01: Asset new entity created.",
    "repository-entity-lifecycle-02: Asset new entity has createdBy user.",
    "repository-entity-lifecycle-03: Asset new entity has creation time.",
    "repository-entity-lifecycle-04: Asset new entity has correct provenance type.",
    "repository-entity-lifecycle-05: Asset new entity has correct initial status.",
    "repository-entity-lifecycle-06: Asset new entity has correct type.",
    "repository-entity-lifecycle-07: Asset new entity has local metadata collection.",
    "repository-entity-lifecycle-08: Asset new entity has version greater than zero.",
    "repository-entity-lifecycle-32: Asset entity versions NOT returned before create time ",
    "repository-entity-lifecycle-09: Asset new entity is known.",
    "repository-entity-lifecycle-10: Asset new entity summarized.",
    "repository-entity-lifecycle-11: Asset new entity retrieved.",
    "repository-entity-lifecycle-33: Asset entity versions returned after create ",
    "repository-entity-lifecycle-33: Asset entity versions returned after create ",
    "repository-entity-lifecycle-33: Asset entity versions returned after create ",
    "repository-entity-lifecycle-12: Asset new entity is unattached.",
    "repository-entity-lifecycle-17: Asset entity properties cleared to min.",
    "repository-entity-lifecycle-18: Asset entity with min properties version number is 2",
    "repository-entity-lifecycle-34: Asset entity versions returned after update ",
    "repository-entity-lifecycle-34: Asset entity versions returned after update ",
    "repository-entity-lifecycle-34: Asset entity versions returned after update ",
    "repository-entity-lifecycle-36: Asset entity versions returned after restore ",
    "repository-entity-lifecycle-36: Asset entity versions returned after restore ",
    "repository-entity-lifecycle-41: Asset entity versions are ordered FORWARDS as requested ",
    "repository-entity-lifecycle-29: Asset repository supports undo of operations ",
    "repository-entity-lifecycle-19: Asset entity has properties restored.",
    "repository-entity-lifecycle-20: Asset entity after undo version number is 3",
    "repository-entity-lifecycle-37: Asset entity versions returned after update  ",
    "repository-entity-lifecycle-37: Asset entity versions returned after update  ",
    "repository-entity-lifecycle-40: Asset entity versions are ordered BACKWARDS as requested ",
    "repository-entity-lifecycle-37: Asset entity versions returned after update  ",
    "repository-entity-lifecycle-37: Asset entity versions returned after update  ",
    "repository-entity-lifecycle-41: Asset entity versions are ordered FORWARDS as requested ",
    "repository-entity-lifecycle-45: Asset second undo of entity reinstates the update that the first undo reversed.",
    "repository-entity-lifecycle-46: Asset entity after second undo version number is 4",
    "repository-entity-lifecycle-30: Asset repository supports soft delete ",
    "repository-entity-lifecycle-21: Asset entity deleted version number is 5",
    "repository-entity-lifecycle-22: Asset entity no longer retrievable after delete.",
    "repository-entity-lifecycle-43: Asset entity is known when deleted ",
    "repository-entity-lifecycle-35: Asset entity version is returned while deleted ",
    "repository-entity-lifecycle-35: Asset entity version is returned while deleted ",
    "repository-entity-lifecycle-35: Asset entity version is returned while deleted ",
    "repository-entity-lifecycle-23: Asset entity restored ",
    "repository-entity-lifecycle-24: Asset entity restored version number is 6",
    "repository-entity-lifecycle-25: Asset entity retrieved following restore ",
    "repository-entity-lifecycle-36: Asset entity versions returned after restore ",
    "repository-entity-lifecycle-36: Asset entity versions returned after restore ",
    "repository-entity-lifecycle-40: Asset entity versions are ordered BACKWARDS as requested ",
    "repository-entity-lifecycle-36: Asset entity versions returned after restore ",
    "repository-entity-lifecycle-36: Asset entity versions returned after restore ",
    "repository-entity-lifecycle-41: Asset entity versions are ordered FORWARDS as requested ",
    "repository-entity-lifecycle-27: Asset historical retrieval returned correct version of entity ",
    "repository-entity-lifecycle-44: Asset property stored with no value is returned with no value ",
    "repository-entity-lifecycle-26: Asset entity purged.",
    "repository-entity-lifecycle-39: Asset entity is not known after purge ",
    "repository-entity-lifecycle-27: Asset historical retrieval returned correct version of entity ",
    "repository-entity-lifecycle-38: Asset entity versions NOT returned after purge ",
    "repository-test-case-base-01: Repository connector supplied to conformance suite.",
    "repository-test-case-base-02: Metadata collection for repository connector supplied to conformance suite."
  ],
  "unsuccessfulAssertions": [],
  "notSupportAssertions": []
}
```


--8<-- "snippets/abbr.md"
