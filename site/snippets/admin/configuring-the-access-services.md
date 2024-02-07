<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

## Configure the access services

The [Open Metadata Access Services (OMASs)](/services/omas) provide the domain-specific APIs for metadata management and governance. They run in a [metadata access store](/concepts/metadata-access-store) or [metadata access point](/concepts/metadata-access-point) and typically offer a REST API, Java client and an event-based interface for asynchronous interaction.

!!! attention "Prerequisite configuration"
    The access service configuration depends on the definitions of the [event bus](#set-up-the-default-event-bus) and the [local server's userId](#set-the-servers-user-id-and-optional-password).

### List available access services

The OMASs are optional services of the OMAG Server Platform.  The command below list the access services that are available in your OMAG Server Platform.

!!! get "GET - list all available access services"
    ```
    {{platformURLRoot}}/open-metadata/platform-services/users/{{adminUserId}}/server-platform/registered-services/access-services
    ```

    ??? success "Example response listing available access services"
        ```json
        {
            "relatedHTTPCode": 200,
            "services": [
                {
                    "serviceName": "Asset Owner",
                    "serviceURLMarker": "asset-owner",
                    "serviceDescription": "Manage an asset",
                    "serviceWiki": "https://egeria.odpi.org/open-metadata-implementation/access-services/asset-owner/"
                },
                {
                    "serviceName": "Stewardship Action",
                    "serviceURLMarker": "stewardship-action",
                    "serviceDescription": "Manage exceptions and actions from open governance",
                    "serviceWiki": "https://egeria.odpi.org/open-metadata-implementation/access-services/stewardship-action/"
                },
                {
                    "serviceName": "Subject Area",
                    "serviceURLMarker": "subject-area",
                    "serviceDescription": "Document knowledge about a subject area",
                    "serviceWiki": "https://egeria.odpi.org/open-metadata-implementation/access-services/subject-area/"
                },
                {
                    "serviceName": "Governance Program",
                    "serviceURLMarker": "governance-program",
                    "serviceDescription": "Manage the governance program",
                    "serviceWiki": "https://egeria.odpi.org/open-metadata-implementation/access-services/governance-program/"
                },
                {
                    "serviceName": "Asset Lineage",
                    "serviceURLMarker": "asset-lineage",
                    "serviceDescription": "Store asset lineage",
                    "serviceWiki": "https://egeria.odpi.org/open-metadata-implementation/access-services/asset-lineage/"
                },
                {
                    "serviceName": "Design Model",
                    "serviceURLMarker": "design-model",
                    "serviceDescription": "Exchange design model content with tools and standard packages",
                    "serviceWiki": "https://egeria.odpi.org/open-metadata-implementation/access-services/design-model/"
                },
                {
                    "serviceName": "Glossary View",
                    "serviceURLMarker": "glossary-view",
                    "serviceDescription": "Support glossary terms visualization",
                    "serviceWiki": "https://egeria.odpi.org/open-metadata-implementation/access-services/glossary-view/"
                },
                {
                    "serviceName": "Security Manager",
                    "serviceURLMarker": "security-officer",
                    "serviceDescription": "Set up rules to protect data",
                    "serviceWiki": "https://egeria.odpi.org/open-metadata-implementation/access-services/security-officer/"
                },
                {
                    "serviceName": "Asset Consumer",
                    "serviceURLMarker": "asset-consumer",
                    "serviceDescription": "Access assets through connectors",
                    "serviceWiki": "https://egeria.odpi.org/open-metadata-implementation/access-services/asset-consumer/"
                },
                {
                    "serviceName": "IT Infrastructure",
                    "serviceURLMarker": "it-infrastructure",
                    "serviceDescription": "Manage information about the deployed IT infrastructure",
                    "serviceWiki": "https://egeria.odpi.org/open-metadata-implementation/access-services/it-infrastructure/"
                },
                {
                    "serviceName": "Asset Catalog",
                    "serviceURLMarker": "asset-catalog",
                    "serviceDescription": "Search and understand your assets",
                    "serviceWiki": "https://egeria.odpi.org/open-metadata-implementation/access-services/asset-catalog/"
                },
                {
                    "serviceName": "Data Science",
                    "serviceURLMarker": "data-science",
                    "serviceDescription": "Create and manage data science definitions and models",
                    "serviceWiki": "https://egeria.odpi.org/open-metadata-implementation/access-services/data-science/"
                },
                {
                    "serviceName": "Community Profile",
                    "serviceURLMarker": "community-profile",
                    "serviceDescription": "Define personal profile and collaborate",
                    "serviceWiki": "https://egeria.odpi.org/open-metadata-implementation/access-services/community-profile/"
                },
                {
                    "serviceName": "DevOps",
                    "serviceURLMarker": "devops",
                    "serviceDescription": "Manage a DevOps pipeline",
                    "serviceWiki": "https://egeria.odpi.org/open-metadata-implementation/access-services/dev-ops/"
                },
                {
                    "serviceName": "Software Developer",
                    "serviceURLMarker": "software-developer",
                    "serviceDescription": "Interact with software development tools",
                    "serviceWiki": "https://egeria.odpi.org/open-metadata-implementation/access-services/software-developer/"
                },
                {
                    "serviceName": "Discovery Engine",
                    "serviceURLMarker": "discovery-engine",
                    "serviceDescription": "Support for automated metadata discovery engines",
                    "serviceWiki": "https://egeria.odpi.org/open-metadata-implementation/access-services/discovery-engine/"
                },
                {
                    "serviceName": "Data Engine",
                    "serviceURLMarker": "data-engine",
                    "serviceDescription": "Exchange process models and lineage with a data engine",
                    "serviceWiki": "https://egeria.odpi.org/open-metadata-implementation/access-services/data-engine/"
                },
                {
                    "serviceName": "Project Management",
                    "serviceURLMarker": "project-management",
                    "serviceDescription": "Manage data projects",
                    "serviceWiki": "https://egeria.odpi.org/open-metadata-implementation/access-services/project-management/"
                },
                {
                    "serviceName": "Governance Engine",
                    "serviceURLMarker": "governance-engine",
                    "serviceDescription": "Set up an operational governance engine",
                    "serviceWiki": "https://egeria.odpi.org/open-metadata-implementation/access-services/governance-engine/"
                },
                {
                    "serviceName": "Digital Architecture",
                    "serviceURLMarker": "digital-architecture",
                    "serviceDescription": "Design of the digital services for an organization",
                    "serviceWiki": "https://egeria.odpi.org/open-metadata-implementation/access-services/digital-architecture/"
                },
                {
                    "serviceName": "Data Privacy",
                    "serviceURLMarker": "data-privacy",
                    "serviceDescription": "Manage governance of privacy",
                    "serviceWiki": "https://egeria.odpi.org/open-metadata-implementation/access-services/data-privacy/"
                },
                {
                    "serviceName": "Data Manager",
                    "serviceURLMarker": "data-manager",
                    "serviceDescription": "Capture changes to the data stores and data set managed by a technology managing collections of data",
                    "serviceWiki": "https://egeria.odpi.org/open-metadata-implementation/access-services/data-manager/"
                }
            ]
        }
        ```
    
These access services are available to configure either all together or individually.

### Enable access services

The access services can either all be enabled (with default configuration values) or individually enabled:

=== "all, with defaults"

    To enable all the access services (and the [enterprise repository services](/services/omrs/#enterprise-repository-services)
    that support them) with default configuration values use the following command.

    !!! post "POST - enable all access services"
        ```
        {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/access-services
        ```

=== "individually"

    Alternatively, each service can be configured individually with the following command:

    !!! post "POST - configure an individual access service"
        ```
        {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/access-services/{{serviceURLMarker}}
        ```

The service URL marker for each service is shown in the example response given above.

In both cases, it is possible to pass a list of properties to the access service that controls the behavior of each access service. These are sent in the request body. More details of which properties are supported are documented with each access service.

### Disable the access services

The access services can be disabled with the following command. This also disables the enterprise repository services since they are not being used.

!!! delete "DELETE - disable the access services"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/access-services
    ```

### Review configuration

!!! get "GET - retrieve current configuration for the access services"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/access-services/configuration
    ```

!!! post "POST - save changes back to the configuration"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/access-services/configuration
    ```
