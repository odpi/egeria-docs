<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Writing Repository Connectors

The repository connector's API is provided by the [Open Metadata Repository Services (OMRS)](/services/omrs).  It defines a call interface to create, search, query, update and delete metadata stored in a metadata repository.

A [repository connector](/concepts/repository-connector) is made up of two objects:

* A connector that extends the [`OMRSRepositoryConnector` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/repositoryconnector/OMRSRepositoryConnector.java){ target=gh } abstract class.  The OMRS passes it the information it needs about the server (server name, metadata collection id, [repository helper](/concepts/repository-helper), [repository validator](/concepts/repository-validator) and so on) and then calls `getMetadataCollection()` to retrieve the metadata collection.
* A metadata collection that extends the [`OMRSMetadataCollection` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/OMRSMetadataCollection.java){ target=gh } abstract class.  This defines the methods for working with the type definitions and the metadata instances (entities, relationships and classifications) in the repository, so that metadata can be communicated and exchanged according to Egeria's protocols and [type definitions](/types).

These classes are in the *repository-services-apis* module.  You may want to see the [OMRS metamodel](/guides/developer/repository-connectors/metamodel/overview) for more details on the granularity of metadata exchange, and [Implementing a Repository Connector](/guides/developer/implement-repository-connector) for the steps to build one.

## Choosing a base class for the metadata collection

The `org.odpi.openmetadata.repositoryservices.connectors.stores.metadatacollectionstore` package provides base classes for the metadata collection:

| Base class | Use it when |
|---|---|
| `OMRSMetadataCollectionBase` | You want to manage the types yourself.  It extends `OMRSMetadataCollection`, provides protected parameter validation methods (such as `typeDefParameterValidation` and `newTypeDefParameterValidation`) and default implementations that report the optional functions as not supported (`reportUnsupportedOptionalFunction`).  The other two base classes extend it. |
| `OMRSDynamicTypeMetadataCollectionBase` | The repository can support any open metadata type.  It begins with no types and builds up its knowledge of the types as they are added through the API, from open metadata archives and from other members of the cohort.  The types defined through the API in this repository (those whose origin is this repository's metadata collection id) are validated and kept in the repository's own type store so they can be restored when the server restarts.  The metadata collection supplies its type store, an implementation of `OMRSDynamicTypeStore`, by overriding `getDynamicTypeStore()`; if it returns null, these types are not persisted and a request to delete a type is always refused as the type may be in use.  Egeria's native repositories use this base class. |
| `OMRSFixedTypeMetadataCollectionBase` | The repository has a fixed type system.  Its constructor takes the fixed list of types and attribute types that the repository supports, and it then supports all the type management methods. |

## Egeria's repository connectors

The following repository connectors are located in the [open-metadata-collection-store-connectors :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/open-metadata-collection-store-connectors){ target=gh } module and are useful examples:

* *postgres-repository-connector* - `PostgresOMRSRepositoryConnector` and `PostgresOMRSMetadataCollection` provide a native repository that stores metadata in a PostgreSQL database.  Each server has its own database schema.
* *inmemory-repository-connector* - `InMemoryOMRSRepositoryConnector` and `InMemoryOMRSMetadataCollection` provide a native repository that is entirely in memory.  It is useful for testing and demos.  The same module contains `ReadOnlyOMRSRepositoryConnector`, a read-only in-memory repository that hosts fixed content from an [open metadata archive](/concepts/open-metadata-archive).
* *omrs-rest-repository-connector* - `OMRSRESTRepositoryConnector` and `OMRSRESTMetadataCollection` call a remote cohort member through the OMRS REST API.  This is the [cohort member client connector](/guides/developer/runtime-connectors/cohort-member-client-connector) used for federated queries.

!!! attention "A common tripping point for conformance"
    Each metadata instance has a single home metadata collection, and only the home repository may change it.  The other members of the cohort hold read-only *reference copies*.  OMRS can only enforce these rules for requests that pass through it.  If the third party technology behind an adapter repository connector also provides its own services or user interface through which metadata can be updated, these too need to follow the same protocol - in particular, the reference copies must remain read-only through the product's own interfaces - in order for the repository to conform to the Egeria protocol.  The [Conformance Test Suite](/guides/cts) can be used to test the connector's conformance.

!!! info "Consider integrating catalogs with integration connectors"

    The [integration connector](/concepts/integration-connector) provides an alternative integration path for catalogs and other metadata managers that goes via an [integration daemon](/concepts/integration-daemon).

    Catalogs are able to have a two-way integration through this path without needing to conform to the repository service rules for managing home and reference copies. This is possible for two reasons:

    * Since the metadata from the catalog passes through Egeria's open metadata services, rather than being exchanged directly between repositories, Egeria has better control of the metadata from the catalog.
    * Since the catalog is not part of a federated query, any inconsistent updates to metadata that occur in its repository only impact the users of that catalog and not the whole cohort.

    If your catalog is not able to support reference copies, you may want to consider this option.

--8<-- "snippets/abbr.md"
