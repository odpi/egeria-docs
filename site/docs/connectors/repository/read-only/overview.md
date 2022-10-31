<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->


--8<-- "snippets/content-status/stable.md"

# Read-only Repository Connector

!!! info "Connector summary"

    - Connector Category: [Native Repository Connector](/concepts/repository-connector)
    - Hosting Service: [Open Metadata Reposiotry Services (OMRS)](/services/omrs)
    - Hosting Server: [Metadata Access Store](/concepts/metdata-access-store)
    - Source Module: [inmemory-repository-connector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/open-metadata-collection-store-connectors/inmemory-repository-connector){ target=gh }
    - Jar File Name: `inmemory-repository-connector.jar`
    - ConnectorProviderClassName: `org.odpi.openmetadata.adapters.repositoryservices.readonly.repositoryconnector/ReadOnlyOMRSRepositoryConnectorProvider.java`

The read only repository connector provides a compliant implementation of a local repository that can be configured into a [Metadata Access Store](/concepts/metadata-access-store).  It does not support the interfaces for create, update, delete.  However, it does support the search interfaces and is able to cache metadata. This means it can be loaded with metadata from an [Open Metadata Archive](/concepts/open-metadata-archive) and connected to a cohort.  The content from the archive will be shared with other members of the cohort.


--8<-- "snippets/abbr.md"

