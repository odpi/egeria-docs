<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

## Configure the native repository connector

A [metadata access store](/concepts/metadata-access-store) supports a metadata repository that has native support for the [open metadata types and instances](/types).  This is enabled by adding a native metadata repository connector to the server's configuration document.

### Add a repository connector implementation

Egeria provides a number of implementations of such a repository -- only one of these options can be configured for a given metadata server at a time.

=== "bi-temporal graph"

    This command enables a XTDB-based metadata repository, which itself has a [number of pluggable back-end options for persistence and other configuration options](/connectors/repository/xtdb/#options-for-configuring-xtdb).

    This native metadata repository is currently the [highest-performing, most fully-functional repository](/connectors/repository/xtdb/performance) for Egeria, supporting all metadata operations including historical metadata as well as being [highly-available through clustered deployment](/connectors/repository/xtdb/#high-availability).

    !!! post "POST - enable the bi-temporal graph repository"
        ```
        {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/local-repository/mode/plugin-repository/connection
        ```

        ```json
        {
          "class": "Connection",
          "connectorType": {
            "class": "ConnectorType",
            "connectorProviderClassName": "org.odpi.egeria.connectors.juxt.xtdb.repositoryconnector.XtdbOMRSRepositoryConnectorProvider"
          }
        }
        ```

    !!! attention "May require additional driver libraries"
        Note that depending on the persistence you configure, you may need to [obtain additional driver libraries for your back-end service](/connectors/repository/xtdb/#pluggable-persistence), as not every driver is embedded in the XTDB connector itself.

=== "non-temporal graph"

    This command enables a JanusGraph-based native metadata repository that is embedded in the metadata server
    and uses the local disk to store the metadata, but does not manage any historical metadata.

    !!! post "POST - enable the graph repository"
        ```
        {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/local-repository/mode/local-graph-repository
        ```

=== "in-memory"

    The in-memory native repository maintains an in-memory store of metadata. It is useful for demos and testing.
    No metadata is kept if the metadata access server is shutdown. It should not be used in a production environment.

    !!! post "POST - enable the in-memory repository"
        ```
        {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/local-repository/mode/in-memory-repository
        ```

=== "read-only"

    The read-only native repository connector provides a compliant implementation of a local
    repository that can be configured into a metadata server.
    It does not support the interfaces for create, update, delete.
    However, it does support the search interfaces and is able to cache metadata.

    This means it can be loaded with metadata from an [open metadata archive](/concepts/open-metadata-archive)
    and connected to a cohort.
    The content from the archive will be shared with other members of the cohort.

    !!! post "POST - enable the read-only repository"
        ```
        {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/local-repository/mode/read-only-repository
        ```

### Remove the native repository connector

This command removes all configuration for the local repository. This includes the [local metadata collection id](/services/omrs/metdata-repositories/#metadata-collection-id). If a new local repository is added, it will have a new local metadata collection id and will not be able to automatically re-register with its cohort(s).

!!! delete "DELETE - remove the local repository"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/local-repository
    ```
