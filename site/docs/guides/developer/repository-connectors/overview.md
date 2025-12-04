<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Writing Repository Connectors

The repository connector's API is provided by the [Open Metadata Repository Services (OMRS)](/services/omrs).  It defines a call interface to create, search, query, update and delete metadata stored in the metadata repository.

The [repository connectors](/connectors/repository-connector) implement the [`OMRSMetadataCollection` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/OMRSMetadataCollection.java){ target=gh } interface to allow metadata to be communicated and exchanged according to Egeria's protocols and [type definitions](/types).

You may want to see the [OMRS metamodel](/guides/developer/metamodel/overview) for more details on the granularity of metadata exchange.

!!! attention "A common tripping point for conformance"
    The routing behavior described for homed metadata instances can only be enforced when the requests go through OMRS itself. For third party tools that provide their own services / user interface through which updates can be made, a common tripping point becomes the fact that these services / user interfaces need to adhere to the same protocol principles outlined above -- specifically, ensuring reference copies are also immutable through these product-native interfaces -- in order to conform to the Egeria protocol.

    For cases where the tool is unable to do so, we are actively investigating other mitigation measures like providing a [Smart Repository Proxy :material-github:](https://github.com/odpi/egeria/issues/5402){ target=gh } to ensure that any changes to metadata that violate the protocol remain isolated in that third party technology and are not inadvertently propagated elsewhere in the cohort.


!!! info "Consider integrating Catalogs with Integration Connectors"

    The [integration connector](/concepts/integration-connector) provides a new integration path for asset managers that goes via an [integration daemon](/concepts/integration-daemon).

    Catalogs will be able to have a two-way integration through this path without needing to conform to the repository service rules for managing home and reference copies. This is possible for two reasons:

    * Since the metadata from the catalog passes through an OMAS, Egeria will be able to have a better control of the metadata from the catalog.
    * Since the catalog is not part of a federated query, any inconsistent updates to metadata that occurs in its repository, only impacts the users of that catalog and not the whole cohort.

    If your catalog is not able to support reference copies, you may want to consider this option

--8<-- "snippets/abbr.md"
