<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Using the Java Clients

Egeria's Java clients support calls to Egeria's operational services.  They are used by [Runtime Manager OMVS](/services/omvs/runtime-manager/overview) to retrieve information about the running Egeria infrastructure and can be used by other monitoring programs.  There are [python](/guides/developer/python-clients/overview) alternatives for these interfaces.

Each client is located in the `-client` module of the service it calls:

| Client | Module | Purpose |
|---|---|---|
| [Administration Services Clients](https://odpi.github.io/egeria/org/odpi/openmetadata/adminservices/client/package-summary.html) | `admin-services-client` | Configure the OMAG Server Platform and OMAG Servers.  There is a client for each type of server, for example `MetadataAccessStoreConfigurationClient`, `ViewServerConfigurationClient`, `IntegrationDaemonConfigurationClient` and `EngineHostConfigurationClient`, plus `OMAGServerPlatformConfigurationClient` and `ConfigurationManagementClient`. |
| [Platform Services Client](https://odpi.github.io/egeria/org/odpi/openmetadata/platformservices/client/PlatformServicesClient.html) | `platform-services-client` | Query the platform's registered services and known/active servers, start servers (`activateWithStoredConfig`, `activateWithSuppliedConfig`), shut them down (`shutdownServer`, `shutdownAllServers`, `shutdownAndUnregisterServer`), shut down the platform, and maintain the platform's security connection and user accounts. |
| [Server Operations Client](https://odpi.github.io/egeria/org/odpi/openmetadata/serveroperations/client/ServerOperationsClient.html) | `server-operations-client` | Query the status, active configuration and active services of a running server, and load [open metadata archives](/concepts/open-metadata-archive) into it. |
| [Engine Host Client](https://odpi.github.io/egeria/org/odpi/openmetadata/governanceservers/enginehostservices/client/EngineHostClient.html) | `engine-host-services-client` | Retrieve summaries of the governance engines running in an [engine host](/concepts/engine-host) (`getGovernanceEngineSummary`, `getGovernanceEngineSummaries`) and refresh their configuration (`refreshConfig`). |
| [Integration Daemon Client](https://odpi.github.io/egeria/org/odpi/openmetadata/governanceservers/integrationdaemonservices/client/IntegrationDaemon.html) | `integration-daemon-services-client` | Query, refresh and restart the integration connectors running in an [integration daemon](/concepts/integration-daemon), update their configuration, and publish OpenLineage events, data contracts and data products to it. |
| [Repository Services Clients](https://odpi.github.io/egeria/org/odpi/openmetadata/repositoryservices/clients/package-summary.html) | `repository-services-client` | Call the repository services, for example `AuditLogServicesClient` to retrieve the audit log, and `MetadataHighwayServicesClient` to query cohort membership. |

## Creating a client

Each Java client has two constructors.  Both set up the connection to the [OMAG Server Platform](/concepts/omag-server-platform) and obtain a bearer token for the calls using a [secrets store connector](/concepts/secrets-store-connector).  They differ in how the secrets store is supplied:

* The first constructor takes the details of the secrets store and creates the secrets store connector itself.
* The second constructor takes a `Map<String, SecretsStoreConnector>` of secrets store connectors that have already been created.

Using the `PlatformServicesClient` as an example, the parameters are:

* `platformName` - the descriptive name of the OMAG Server Platform for error logging.  Clients that call a specific server, such as `ServerOperationsClient` or `EngineHostClient`, take the `serverName` here instead.
* `platformRootURL` - the [platform url root](/concepts/platform-url-root) of the OMAG Server Platform.
* `secretStoreProvider` - the class name of the secrets store connector's provider.
* `secretStoreLocation` - the location (network address or file name) of the secrets store.
* `secretStoreCollection` - the name of the collection of secrets to use to connect to the platform.
* `secretsStoreConnectorMap` - (second constructor) the secrets store connectors to use, in place of the three parameters above.
* `delegatingUserId` - the userId of the external user making the request, when the caller is acting on behalf of someone else.  It may be null.
* `auditLog` - logging destination for audit log messages.

The constructor throws `InvalidParameterException` if there is an issue setting up the client-side components based on the supplied parameters.

!!! tip "Calling a platform with a self-signed certificate"
    The [HTTP Helper](/guides/developer/http-helper/overview) turns off certificate checking in development environments.

## Working with open metadata from Java

Programs that need to create and retrieve open metadata in Java use the [Open Metadata Framework (OMF)](/frameworks/omf/overview).  Its `OpenMetadataClient` interface (package `org.odpi.openmetadata.frameworks.openmetadata.client`) is implemented by the `EgeriaOpenMetadataStoreClient` in the `omf-metadata-client` module, and the specialized handlers in the `org.odpi.openmetadata.frameworks.openmetadata.handlers` package (for example `AssetHandler`, `CollectionHandler` and `GlossaryTermHandler`) are built on top of an `OpenMetadataClient`.  These are the classes that Egeria's own view services and connectors use.  Applications written in other languages call the equivalent [REST APIs](/guides/developer/rest-apis) of the view services.

--8<-- "snippets/abbr.md"
