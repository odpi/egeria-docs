<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Conformance Test Suite Overview

The open metadata conformance suite provides a testing framework to help the developers integrate a specific technology into the open metadata ecosystem.

![Overview of the open metadata conformance suite](conformance-suite-oveview.png)

The actual tests are run by an *open metadata conformance workbench* within the open metadata conformance suite server. Each workbench focuses on testing a specific type of technology, and typically define the set of functionality being tested in a *profile*.

!!! tip "Test cases within profiles"
    The profiles are supported by one or more test cases (described in detail within each profile).

    Each test case typically focuses on a specific requirement within a profile. However, it may verify other requirements from either the same of different profiles if it is efficient to do so.

    When a test case encounters errors, it will log them and if possible it will continue testing. However, some failures are blocking and the test case will end when one of these is encountered.

## Platform workbench

The open metadata conformance platform workbench is responsible for testing the various APIs supported by an [Open Metadata and Governance (OMAG) Server Platform](/egeria-docs/concepts/omag-server-platform).

This workbench supports the following profiles:

| Profile | Description |
|---|---|
| [Platform origin](profiles/platform-origin) | Does the platform support the `server-platform-origin` API. |

## Repository workbench

The open metadata conformance repository workbench is responsible for testing the ability of an open metadata repository to connect and interact with other open metadata repositories in a conformant way.

It tests both the repository's repository services API and its ability to exchange events with the [OMRS cohort event topic](/egeria-docs/services/omrs/metadata-events/#omrs-event-topic).

The workbench uses the registration information that is passed when the technology under test registers with the same [open metadata repository cohort](/egeria-docs/services/omrs/cohort) as the conformance suite. It will confirm that the information received in the events matches the information returned by the technology under test's repository services.

This workbench works as a pipeline processor, accumulating information from one test and using it to seed subsequent tests. A failure early on in the pipeline may prevent other tests from running.

In addition, this workbench dynamically generates tests based on the types returned by the repository. So for example, the [repository TypeDef test case](test-cases/repository-typedef-test-case.md) runs for each TypeDef returned by the repository. A failure in the early set up test cases will prevent the repository workbench from generating the full suite of test cases for the repository under test.

The functions expected of an open metadata repository are numerous. These functions are broken down into the profiles listed below. An open metadata repository needs to support at least one profile to be conformant: in practice, metadata sharing is required in order to support any of the other profiles, so it is mandatory.

| Profile | Description |
|---|---|
| [Metadata sharing](../repository-profiles/metadata-sharing) | The technology under test is able to share metadata with other members of the cohort. |
| [Reference copies](../repository-profiles/reference-copies) | The technology under test is able to store reference copies of metadata from other members of the cohort. |
| [Metadata maintenance](../repository-profiles/metadata-maintenance) | The technology under test supports requests to create, update and purge metadata instances. |
| [Effectivity dating](../repository-profiles/effectivity-dating) | The technology under test supports effectivity dating properties. |
| [Dynamic types](../repository-profiles/dynamic-types) | The technology under test supports changes to the list of its supported types while it is running. |
| [Graph queries](../repository-profiles/graph-queries) | The technology under test supports graph-like queries that return collections of metadata instances. |
| [Historical search](../repository-profiles/historical-search) | The technology under test supports search for the state of the metadata instances at a specific time in the past. |
| [Entity proxies](../repository-profiles/entity-proxies) | The technology under test is able to store stubs for entities to use on relationships when the full entity is not available. |
| [Soft-delete and restore](../repository-profiles/soft-delete-restore) | The technology under test allows an instance to be soft-deleted and restored. |
| [Undo an update](../repository-profiles/undo-update) | The technology under test is able to restore an instance to its previous version (although the version number is updated). |
| [Reidentify instance](../repository-profiles/reidentify-instance) | The technology under test supports the command to change the unique identifier (guid) of a metadata instance. |
| [Retype instance](../repository-profiles/retype-instance) | The technology under test supports the command to change the type of a metadata instance to either its super type or a subtype. |
| [Rehome instance](../repository-profiles/rehome-instance) | The technology under test supports the command to update the metadata collection id for a metadata instance. |
| [Entity search](../repository-profiles/entity-search) | The technology under test supports the ability to search for entity instances. |
| [Relationship search](../repository-profiles/relationship-search) | The technology under test supports the ability to search for relationnship instances. |
| [Entity advanced search](../repository-profiles/entity-advanced-search) | The technology under test supports the use of regular expressions to search for metadata instances. |
| [Relationship advanced search](../repository-profiles/relationship-advanced-search) | The technology under test supports the use of regular expressions to search for relationship instances. |

## Performance workbench

The open metadata conformance performance workbench is responsible for testing the performance of various APIs supported by an Open Metadata and Governance (OMAG) server repository.

!!! attention "Focused purely on measuring performance"
    Note that the workbench is focused purely on measuring performance, and will not extensively test for correctness of results across a variety of edge cases, etc. For that, use the normal [repository workbench](#repository-workbench).

    For example, to allow testing the performance of repositories that may support asynchronous write operations (and therefore not return complete or even any result to operations like `updateEntityProperties`), this workbench only validates that operations return without throwing any exceptions: it does not look at the contents of the response at all.

This workbench runs the following profiles, in the following order:

| Profile | Description |
|---|---|
| [Entity creation](../performance-profiles/entity-creation) | tests the performance of `addEntity` and `saveEntityReferenceCopy` methods |
| [Entity search](../performance-profiles/entity-search) | tests the performance of `findEntities`, `findEntitiesByProperty` and `findEntitiesByPropertyValue` methods |
| [Relationship creation](../performance-profiles/relationship-creation) | tests the performance of `addRelationship` and `saveRelationshipReferenceCopy` methods |
| [Relationship search](../performance-profiles/relationship-search) | tests the performance of `findRelationships`, `findRelationshipsByProperty` and `findRelationshipsByPropertyValue` methods |
| [Entity classification](../performance-profiles/entity-classification) | tests the performance of `classifyEntity` and `saveClassificationReferenceCopy` methods |
| [Classification search](../performance-profiles/classification-search) | tests the performance of `findEntitiesByClassification` method |
| [Entity update](../performance-profiles/entity-update) | tests the performance of `updateEntityProperties` method |
| [Relationship update](../performance-profiles/relationship-update) | tests the performance of `updateRelationshipProperties` method |
| [Classification update](../performance-profiles/classification-update) | tests the performance of `updateEntityClassification` method |
| [Entity undo](../performance-profiles/entity-undo) | tests the performance of `undoEntityUpdate` method |
| [Relationship undo](../performance-profiles/relationship-undo) | tests the performance of `undoRelationshipUpdate` method |
| [Entity retrieval](../performance-profiles/entity-retrieval) | tests the performance of `isEntityKnown`, `getEntitySummary` and `getEntityDetail` methods |
| [Entity history retrieval](../performance-profiles/entity-history-retrieval) | tests the performance of `getEntityDetail` (with non-null `asOfTime`) and `getEntityDetailHistory` methods |
| [Relationship retrieval](../performance-profiles/relationship-retrieval) | tests the performance of `isRelationshipKnown` and `getRelationship` methods |
| [Relationship history retrieval](../performance-profiles/relationship-history-retrieval) | tests the performance of `getRelationship` (with non-null `asOfTime`) and `getRelationshipHistory` methods |
| [Entity history search](../performance-profiles/entity-history-search) | tests the performance of the same search operations as Entity Search, but in each case with a non-null `asOfTime` |
| [Relationship history search](../performance-profiles/relationship-history-search) | tests the performance of the same search operations as Relationship Search, but in each case with a non-null `asOfTime` |
| [Graph queries](../performance-profiles/graph-perf-queries) | tests the performance of `getRelationshipsForEntity`, `getEntityNeighborhood`, `getRelatedEntities` and `getLinkingEntities` methods |
| [Graph history queries](../performance-profiles/graph-history-queries) | tests the performance of the same operations as Graph Queries, but in each case with a non-null `asOfTime` |
| [Entity re-home](../performance-profiles/entity-re-home) | tests the performance of `reHomeEntity` method |
| [Relationship re-home](../performance-profiles/relationship-re-home) | tests the performance of `reHomeRelationship` method |
| [Entity declassify](../performance-profiles/entity-declassify) | tests the performance of `declassifyEntity` and `purgeClassificationReferenceCopy` methods |
| [Entity re-type](../performance-profiles/entity-retype) | tests the performance of `reTypeEntity` method |
| [Relationship re-type](../performance-profiles/relationship-retype) | tests the performance of `reTypeRelationship` method |
| [Entity re-identify](../performance-profiles/entity-re-identify) | tests the performance of `reIdentifyEntity` method |
| [Relationship re-identify](../performance-profiles/relationship-re-identify) | tests the performance of `reIdentifyRelationship` method |
| [Relationship delete](../performance-profiles/relationship-delete) | tests the performance of `deleteRelationship` method |
| [Entity delete](../performance-profiles/entity-delete) | tests the performance of `deleteEntity` method |
| [Entity restore](../performance-profiles/entity-restore) | tests the performance of `restoreEntity` method |
| [Relationship restore](../performance-profiles/relationship-restore) | tests the performance of `restoreRelationship` method |
| [Relationship purge](../performance-profiles/relationship-purge) | tests the performance of `purgeRelationship` and `purgeRelationshipReferenceCopy` methods |
| [Entity purge](../performance-profiles/entity-purge) | tests the performance of `purgeEntity` and `purgeEntityReferenceCopy` methods |
| [Environment](../performance-profiles/environment) | does not actually perform any tests, but rather gives statistics about the environment in which the tests were performed (instance counts, etc) |

In each profile, the methods being tested will be executed a number of times and the elapsed time of each execution captured. These elapsed times are available through the detailed profile results of the Conformance Test Suite reports, and can be extracted to calculate more detailed statistics (min, max, median, mean, etc).

Configuration of the performance test can be done through the properties passed in to the admin services prior to executing it:

| Property | Use |
|---|---|
| `instancesPerType` | controls how many instances of metadata to create (per type supported by the repository) (defaults to `50`) |
| `maxSearchResults` | controls how many results to retrieve per page for any search operations (defaults to `10`) |
| `waitBetweenScenarios` | controls an optional wait-point between write and read scenarios, in case you are testing a repository that has an eventually-consistent index (defaults to `0` to avoid any wait) |
| `profilesToSkip` | is an optional array of strings of the profile names that should be skipped during performance testing (for example, to skip very long-running profiles like the graph queries at the larger scales, where thousands or more relationships and entities could be returned by each query) |
| `methodsToSkip` | is an optional array of strings of the method names that should be skipped during performance testing (for example, to skip very long-running methods like the `getRelatedEntities` graph query at the larger scales, where thousands or more relationships and entities could be returned by each query) |

--8<-- "snippets/abbr.md"
