<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Repository entity paging test case

Validate that the repository honours the paging contract when a caller pages through the results of
[`findEntities` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/OMRSMetadataCollection.java){ target=gh }.

## The paging contract

A caller asks for a page of results by giving a starting element and a page size, and asks for the next page
a page size further on. What comes back tells the caller what to do next:

| Response | Meaning | What the caller does |
|---|---|---|
| A list of instances | These are the matching instances on this page. | Asks for the next page. |
| An empty list | Instances were retrieved for this page, but none of them could be returned (for example, they were filtered out). | Asks for the next page. |
| Null | There are no more matching instances from this starting element onwards. | Stops. |

Every layer above the repository pages on this understanding. This includes the enterprise connector, the
generic handlers, the REST APIs and the clients in every language. A repository that breaks the contract
breaks all of them, and neither kind of failure is noisy:

* **Returning null before the end** hides the remaining instances. The visible symptom is a "find by name"
  that reports *not found*, although a larger page size finds the element.
* **Returning an empty list at the end** means a caller that pages through the results never stops.

## Operation

This test runs once for each entity type supported by the technology under test.

1. It creates three entities of the type.
2. It retrieves every entity of the type in a single search, to learn how many instances paging should reach.
   If the repository holds more instances of the type (and its subtypes) than one search can return, the
   rest of the test is skipped rather than reporting on a partial view.
3. It pages through the same search with a page size of two, so that the instances span several pages. The
   results are sequenced by GUID so that every request sees the same order. An empty page moves the walk on
   to the next page, as the contract requires. The walk is bounded, so a repository that never returns null
   cannot hang the run.
4. It requests a page well beyond the last instance.

Finally, the entities created by this test are deleted and purged.

## Assertions

* **repository-entity-paging-01** No page of entities holds more than the page size requested.

* **repository-entity-paging-02** No entity is returned on more than one page.

    Each page starts a page size beyond the previous one, so with a stable sequencing order an instance must
    appear on exactly one page.

* **repository-entity-paging-03** Paging reaches every entity that a single search returns.

    The walk must reach the same number of distinct instances as the single search, including the three
    entities created by the test. A shortfall usually means the repository returned null before the last page.

* **repository-entity-paging-04** The end of the entities is signalled by null, not by an empty list.

    The walk must be ended by the repository returning null within the number of pages needed to cover the
    instances, plus one.

* **repository-entity-paging-05** A page requested beyond the last entity is null.

--8<-- "snippets/abbr.md"
