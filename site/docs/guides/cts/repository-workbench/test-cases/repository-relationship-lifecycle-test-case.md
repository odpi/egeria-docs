<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Repository relationship lifecycle test case

This test validates that relationships can be managed through all stages of their life cycle.

## Operation

The relationship lifecycle tests extract each of the type definitions for relationships and create an instance of that
relationship (along with appropriate entities) and
drives it through each phase of its lifecycle validating that the relationship values are correctly maintained.

## Assertions

* **repository-relationship-lifecycle-00** - `typeName` relationship type definition matches known type.
* **repository-relationship-lifecycle-01** - `typeName` new relationship created.
* **repository-relationship-lifecycle-02** - `typeName` new relationship has createdBy user.
* **repository-relationship-lifecycle-03** - `typeName` new relationship has creation time.
* **repository-relationship-lifecycle-04** - `typeName` new relationship has correct provenance type.
* **repository-relationship-lifecycle-05** - `typeName` new relationship has correct initial status.
* **repository-relationship-lifecycle-06** - `typeName` new relationship has correct type.
* **repository-relationship-lifecycle-07** - `typeName` new relationship has local metadata collection.
* **repository-relationship-lifecycle-08** - `typeName` new relationship has version greater than zero.
* **repository-relationship-lifecycle-09** - `typeName` new relationship is known.
* **repository-relationship-lifecycle-10** - `typeName` new relationship retrieved.
* **repository-relationship-lifecycle-15** - `typeName` relationship properties cleared to min.
* **repository-relationship-lifecycle-16** - `typeName` relationship with min properties version number is `versionNumber`
* **repository-relationship-lifecycle-17** - `typeName` relationship has properties restored.
* **repository-relationship-lifecycle-18** - `typeName` relationship after undo version number is `versionNumber`
* **repository-relationship-lifecycle-19** - `typeName` relationship deleted version number is `versionNumber`
* **repository-relationship-lifecycle-20** - `typeName` relationship no longer retrievable after delete.
* **repository-relationship-lifecycle-21** - `typeName` relationship restored.
* **repository-relationship-lifecycle-22** - `typeName` relationship restored version number is `versionNumber`
* **repository-relationship-lifecycle-23** - `typeName` relationship retrieved following restore.
* **repository-relationship-lifecycle-24** - `typeName` relationship purged.
* **repository-relationship-lifecycle-25** - `typeName` historical retrieval returned correct version relationship.
* **repository-relationship-lifecycle-27** - `typeName` relationship end types are supported by repository.
* **repository-relationship-lifecycle-28** - `typeName` repository supports creation of instances.
* **repository-relationship-lifecycle-29** - `typeName` repository supports undo of operations.
* **repository-relationship-lifecycle-30** - `typeName` repository supports soft delete.
* **repository-relationship-lifecycle-31** - `typeName` repository supports historic retrieval.
* **repository-relationship-lifecycle-32** - `typeName` relationship versions NOT returned before create time.
* **repository-relationship-lifecycle-33** - `typeName` relationship versions returned after create.
* **repository-relationship-lifecycle-34** - `typeName` relationship versions returned after update.
* **repository-relationship-lifecycle-35** - `typeName` relationship versions returned while deleted.
* **repository-relationship-lifecycle-36** - `typeName` relationship versions returned after restore.
* **repository-relationship-lifecycle-37** - `typeName` relationship versions are ordered BACKWARDS as requested.
* **repository-relationship-lifecycle-38** - `typeName` relationship versions NOT returned after purge.
* **repository-relationship-lifecycle-39** - `typeName` relationship is not known after purge.
* **repository-relationship-lifecycle-41** - `typeName` relationship versions are ordered FORWARDS as requested.
* **repository-relationship-lifecycle-42** - `typeName` relationship is known when deleted.
* **repository-relationship-lifecycle-43** - `typeName` second undo of relationship reinstates the update that the first undo reversed.
* **repository-relationship-lifecycle-44** - `typeName` relationship after second undo version number is `versionNumber`
* **repository-relationship-lifecycle-101** - `typeName` new entity created.

The numbers are not contiguous: an assertion that is retired is not replaced, so that an assertion's identifier always means the same thing.

**repository-relationship-lifecycle-101** is only issued if the repository is not able to create the entities for the ends of the relationship.

## Optional function

A repository does not have to support every part of the lifecycle.  Creating instances ([metadata maintenance](/guides/cts/repository-workbench/profiles/metadata-maintenance)), undoing updates ([undo an update](/guides/cts/repository-workbench/profiles/undo-update)), soft delete with restore ([soft delete and restore](/guides/cts/repository-workbench/profiles/soft-delete-restore)) and retrieving the history of an instance ([instance versions](/guides/cts/repository-workbench/profiles/instance-versions)) belong to optional conformance profiles.

When the repository responds to one of these operations by reporting that the function is not supported, the test case does not fail.  The assertion is recorded in the `notSupportAssertions` list of the results, instead of in `successfulAssertions` or `unsuccessfulAssertions`, and the test case moves on to the next part of the lifecycle that it is able to test.

## Sample Output

This is the output for the *License* relationship type from a run against the in-memory repository, which supports all of the optional function.  The first two assertions are issued for every repository test case to confirm that the workbench is able to call the repository.

```json
{
  "class": "OpenMetadataTestCaseResult",
  "testCaseId": "repository-relationship-lifecycle-License",
  "testCaseName": "Repository relationship lifecycle test case",
  "testCaseDescriptionURL": "https://egeria-project.org/guides/cts/repository-workbench/test-cases/repository-relationship-lifecycle-test-case",
  "successMessage": "Relationships can be managed through their lifecycle",
  "successfulAssertions": [
    "repository-test-case-base-01: Repository connector supplied to conformance suite.",
    "repository-test-case-base-02: Metadata collection for repository connector supplied to conformance suite.",
    "repository-relationship-lifecycle-00: License relationship type definition matches known type  ",
    "repository-relationship-lifecycle-28: License repository supports creation of instances ",
    "repository-relationship-lifecycle-01: License new relationship created.",
    "repository-relationship-lifecycle-02: License new relationship has createdBy user.",
    "repository-relationship-lifecycle-03: License new relationship has creation time.",
    "repository-relationship-lifecycle-04: License new relationship has correct provenance type.",
    "repository-relationship-lifecycle-05: License new relationship has correct initial status.",
    "repository-relationship-lifecycle-06: License new relationship has correct type.",
    "repository-relationship-lifecycle-07: License new relationship has local metadata collection.",
    "repository-relationship-lifecycle-08: License new relationship has version greater than zero.",
    "repository-relationship-lifecycle-32: License relationship versions NOT returned before create time ",
    "repository-relationship-lifecycle-09: License new relationship is known.",
    "repository-relationship-lifecycle-10: License new relationship retrieved.",
    "repository-relationship-lifecycle-15: License relationship properties cleared to min.",
    "repository-relationship-lifecycle-16: License relationship with min properties version number is 2",
    "repository-relationship-lifecycle-34: License relationship versions returned after update ",
    "repository-relationship-lifecycle-34: License relationship versions returned after update ",
    "repository-relationship-lifecycle-34: License relationship versions returned after update ",
    "repository-relationship-lifecycle-36: License relationship versions returned after restore ",
    "repository-relationship-lifecycle-36: License relationship versions returned after restore ",
    "repository-relationship-lifecycle-41: License relationship versions are ordered FORWARDS as requested ",
    "repository-relationship-lifecycle-29: License repository supports undo of operations ",
    "repository-relationship-lifecycle-17: License relationship has properties restored.",
    "repository-relationship-lifecycle-18: License relationship after undo version number is 3",
    "repository-relationship-lifecycle-43: License second undo of relationship reinstates the update that the first undo reversed.",
    "repository-relationship-lifecycle-44: License relationship after second undo version number is 4",
    "repository-relationship-lifecycle-30: License repository supports soft delete ",
    "repository-relationship-lifecycle-19: License relationship deleted version number is 5",
    "repository-relationship-lifecycle-20: License relationship no longer retrievable after delete.",
    "repository-relationship-lifecycle-42: License relationship is known when deleted ",
    "repository-relationship-lifecycle-35: License relationship versions returned while deleted ",
    "repository-relationship-lifecycle-35: License relationship versions returned while deleted ",
    "repository-relationship-lifecycle-35: License relationship versions returned while deleted ",
    "repository-relationship-lifecycle-21: License relationship restored ",
    "repository-relationship-lifecycle-22: License relationship restored version number is 6",
    "repository-relationship-lifecycle-23: License relationship retrieved following restore ",
    "repository-relationship-lifecycle-36: License relationship versions returned after restore ",
    "repository-relationship-lifecycle-36: License relationship versions returned after restore ",
    "repository-relationship-lifecycle-37: License relationship versions are ordered BACKWARDS as requested ",
    "repository-relationship-lifecycle-36: License relationship versions returned after restore ",
    "repository-relationship-lifecycle-36: License relationship versions returned after restore ",
    "repository-relationship-lifecycle-41: License relationship versions are ordered FORWARDS as requested ",
    "repository-relationship-lifecycle-27: License relationship end types are supported by repository  ",
    "repository-relationship-lifecycle-24: License relationship purged.",
    "repository-relationship-lifecycle-39: License relationship is not known after purge ",
    "repository-relationship-lifecycle-25: License historical retrieval returned correct version relationship ",
    "repository-relationship-lifecycle-38: License relationship versions NOT returned after purge ",
    "repository-test-case-base-01: Repository connector supplied to conformance suite.",
    "repository-test-case-base-02: Metadata collection for repository connector supplied to conformance suite."
  ],
  "unsuccessfulAssertions": [],
  "notSupportAssertions": []
}
```


--8<-- "snippets/abbr.md"
