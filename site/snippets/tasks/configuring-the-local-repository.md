<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

## Configure the local repository

A [metadata server](/egeria/concepts/metadata-server) supports a local metadata repository that has
native support for the
[Open Metadata Repository Services (OMRS) types and instances](../../../repository-services/docs/metadata-meta-model.md).

### Choose a repository

Egeria provides a number of implementations of such a repository -- only one of these options
can be configured for a given metadata server at a time.

=== "bi-temporal graph"

    This command enables a Crux-based metadata repository, which itself has a [number of pluggable back-end
    options for persistence and other configuration options :material-dock-window:](https://odpi.github.io/egeria-connector-crux/getting-started/setup/#options-for-configuring-crux){ target=crux }.

    This plugin repository is currently the [highest-performing, most fully-functional repository :material-dock-window:](https://odpi.github.io/egeria-connector-crux/cts/testing-overview/){ target=crux }
    for Egeria, supporting all metadata operations including historical metadata as well as being [highly-available
    through clustered deployment :material-dock-window:](https://odpi.github.io/egeria-connector-crux/high-availability/sample/){ target=crux }.

    !!! post "POST - enable the bi-temporal graph repository"
        ```
        {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/local-repository/mode/plugin-repository/connection
        ```

        ```json
        {
          "class": "Connection",
          "connectorType": {
            "class": "ConnectorType",
            "connectorProviderClassName": "org.odpi.egeria.connectors.juxt.crux.repositoryconnector.CruxOMRSRepositoryConnectorProvider"
          }
        }
        ```

    !!! attention "Requires additional connector libraries"
        Note that you will need to [obtain the additional connector libraries required to run the Crux plugin
        repository :material-dock-window:](https://odpi.github.io/egeria-connector-crux/getting-started/setup/#1-obtain-connector){ target=crux },
        as these are not embedded in the metadata server itself.

=== "non-temporal graph"

    This command enables a JanusGraph-based metadata repository that is embedded in the metadata server
    and uses the local disk to store the metadata, but does not manage any historical metadata.

    !!! post "POST - enable the graph repository"
        ```
        {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/local-repository/mode/local-graph-repository
        ```

=== "in-memory"

    The in-memory repository maintains an in-memory store of metadata. It is useful for demos and testing.
    No metadata is kept if the open metadata services are deactivated,
    or the server is shutdown. It should nto be used in a production environment.

    !!! post "POST - enable the in-memory repository"
        ```
        {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/local-repository/mode/in-memory-repository
        ```

=== "read-only"

    The read-only repository connector provides a compliant implementation of a local
    repository that can be configured into a metadata server.
    It does not support the interfaces for create, update, delete.
    However, it does support the search interfaces and is able to cache metadata.

    This means it can be loaded with metadata from an [open metadata archive](/egeria/concepts/open-metadata-archive)
    and connected to a cohort.
    The content from the archive will be shared with other members of the cohort.

    !!! post "POST - enable the read-only repository"
        ```
        {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/local-repository/mode/read-only-repository
        ```

### Remove the local repository

This command removes all configuration for the local repository.
This includes the [local metadata collection id](/egeria/services/omrs/metdata-repositories/#metadata-collection-id).
If a new local repository is added, it will have a new local metadata collection id and will
not be able to automatically re-register with its cohort(s).

!!! delete "DELETE - remove the local repository"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/local-repository
    ```
