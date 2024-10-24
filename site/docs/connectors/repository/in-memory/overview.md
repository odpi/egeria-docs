<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->


--8<-- "snippets/content-status/stable.md"

# In Memory Repository Connector

!!! info "Connector summary"

    - Connector Category: [Native Repository Connector](/concepts/repository-connector)
    - Hosting Service: [Open Metadata Repository Services (OMRS)](/services/omrs)
    - Hosting Server: [Metadata Access Store](/concepts/metadata-access-store)
    - Source Module: [inmemory-repository-connector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/open-metadata-collection-store-connectors/inmemory-repository-connector){ target=gh }
    - Jar File Name: `inmemory-repository-connector.jar`
    - ConnectorProviderClassName: `org.odpi.openmetadata.adapters.repositoryservices.inmemory.repositoryconnector/InMemoryOMRSRepositoryConnectorProvider.java`


The In-memory OMRS Repository Connector provides a simple repository implementation that "stores" metadata in hash maps within the JVM. It is used for testing, or for environments where metadata maintained in other repositories needs to be cached locally for performance/scalability reasons.


--8<-- "snippets/abbr.md"

