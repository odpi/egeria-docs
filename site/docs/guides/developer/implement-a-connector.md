<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->


To write an open connector you need to complete four steps:

1. Identify the properties for the [connection](/concepts/connection).
2. Write the [connector provider](/concepts/connector-provider).
3. Understand the interface that the connector needs to implement and the support provided by its base class.
4. Write the [connector](/concepts/connector) itself.

All the code you write to implement these should exist in its own module, and as illustrated by the examples could even be in its own independent code repository. Their implementation will have dependencies on Egeria's:

- [Open Connector Framework (OCF)](/frameworks/ocf/overview)
- [Audit Log Framework (ALF)](/frameworks/alf/overview)
- [Open Metadata Framework (OMF)](/frameworks/omf/overview) - the OCF exposes some of its types, such as its exceptions, on its API
- Specific interfaces used by the type of connector

!!! tip "No dependency on Egeria's OMAG Server Platform"
    Note that there is no dependency on Egeria's [OMAG Server Platform](/concepts/omag-server-platform) for these specific connector implementations: they could run in another runtime that supported the connector APIs.  In fact, even the Egeria interface modules should not be embedded in your jar file to allow your connector to run on any version of the OMAG Server Platform that supports your connector.

## Identify connection properties

Begin by identifying and designing the properties needed to connect to your tool or system. These will commonly include a network address, protocol, and user credentials, but could also include other information that can be stored in the configuration properties of the connection.

## Code the connector provider

--8<-- "docs/guides/developer/connector-provider-intro.md"
--8<-- "docs/guides/developer/implementing-a-connector-provider.md"

!!! example "Example: connector provider for a repository connector"
    The [`InMemoryOMRSRepositoryConnectorProvider` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/open-metadata-collection-store-connectors/inmemory-repository-connector/src/main/java/org/odpi/openmetadata/adapters/repositoryservices/inmemory/repositoryconnector/InMemoryOMRSRepositoryConnectorProvider.java){ target=gh } extends `OMRSRepositoryConnectorProviderBase` and passes `EgeriaOpenConnectorDefinition.IN_MEMORY_REPOSITORY_CONNECTOR` and the class name of its connector to the base class.  The connectors it instantiates are [`InMemoryOMRSRepositoryConnector`s :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/open-metadata-collection-store-connectors/inmemory-repository-connector/src/main/java/org/odpi/openmetadata/adapters/repositoryservices/inmemory/repositoryconnector/InMemoryOMRSRepositoryConnector.java){ target=gh }.

!!! example "Example: connector provider for an integration connector"
    Similarly, the [`DataFilesMonitorIntegrationProvider` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/integration-connectors/files-integration-connectors/src/main/java/org/odpi/openmetadata/adapters/connectors/integration/basicfiles/DataFilesMonitorIntegrationProvider.java){ target=gh } (through its superclass `BasicFilesMonitorIntegrationProviderBase`) extends `IntegrationConnectorProvider`.  It passes `EgeriaOpenConnectorDefinition.DATA_FILES_MONITOR_INTEGRATION_CONNECTOR` to the base class and then adds its catalog target types, supported technology types and supported configuration properties.  The connectors it instantiates are [`DataFilesMonitorIntegrationConnector`s :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/integration-connectors/files-integration-connectors/src/main/java/org/odpi/openmetadata/adapters/connectors/integration/basicfiles/DataFilesMonitorIntegrationConnector.java){ target=gh }.

!!! tip "Connectors implement Egeria interfaces, not vice versa"
    Connectors do not need to be part of Egeria's code base.  They can be built in separate code repositories, and Egeria has no direct dependencies on them.  They are loaded at runtime using the connector provider class name in the connection's connector type.

All connectors can be configured with the network address and credential information needed to access the underlying tool or system. Therefore, you do not need to explicitly list properties for such basic details. However, the names of any additional configuration properties that may be useful to a specific type of connector can be described through the `recognizedConfigurationProperties` of the connector type.

### Implementation pattern

Writing a connector provider follows a simple pattern:

- Extend a *connector provider* base class specific to your connector's interface (or `OpenConnectorProviderBase` if there is no specific base class).
- Describe the connector in an `OpenConnectorDefinition` (typically an enum value) giving its component identifier, connector type GUID, names, description, connector provider class name, development status and supported asset/deployed implementation types.
- Define `static final` class members for the connector class name and the names of any additional configuration properties.
- Write a single public constructor, with no parameters, that calls `super()` with the connector definition, the connector class name and the list of recognized configuration property names.
- (Optional) Set up the `supportedTechnologyTypes`, `supportedConfigurationProperties` and `supportedTemplateTypes` that describe the connector to the tools that configure it.

## Understand the connector interface

Now that you have the *connector provider* to instantiate your *connector*, you need to understand what your connector actually needs to do. For a service to use your connector, the connector must provide a set of methods that are relevant to that service.

!!! example "Example: integration connector interface"
    For example, an [integration connector](/concepts/integration-connector) exchanges metadata between third party technologies and Egeria.  It extends [`IntegrationConnectorBase` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/frameworks/open-integration-framework/src/main/java/org/odpi/openmetadata/frameworks/integration/connectors/IntegrationConnectorBase.java){ target=gh }, which defines the methods called by the [integration daemon](/concepts/integration-daemon).

!!! example "Example: OMRS repository connector interface"
    Likewise, a repository connector that integrates a metadata repository with Egeria extends [`OMRSRepositoryConnector` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/repositoryconnector/OMRSRepositoryConnector.java){ target=gh }, because this defines the methods needed to integrate with [Open Metadata Repository Services (OMRS)](/services/omrs).

How would you know to extend these base classes? The *connector provider* implementations in the previous step each extended a base class specific to the type of connector they provide ([`IntegrationConnectorProvider` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/frameworks/open-integration-framework/src/main/java/org/odpi/openmetadata/frameworks/integration/connectors/IntegrationConnectorProvider.java){ target=gh } and [`OMRSRepositoryConnectorProviderBase` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/repositoryconnector/OMRSRepositoryConnectorProviderBase.java){ target=gh }). The matching *connector* base classes (`IntegrationConnectorBase` and `OMRSRepositoryConnector`) are in the same packages as those *connector provider* base classes.

By extending these abstract classes your connector must implement the methods they define. These general methods implement your services (open integration framework and OMRS), without needing to know anything about the underlying technology. Therefore, you can simply "plug-in" the underlying technology: any technology with a connector that implements these methods can run your service. Furthermore, each technology-specific connector can decide how best to implement those methods for itself.

## Code the connector itself

Which brings you to writing the *connector* itself. Now that you understand the interface your connector must provide, you need to implement the methods defined by that interface.

Implement the connector by:

1. Retrieving *connection* information provided by the configuration. The default method for `initialize()` saves the connection object used to create the connector in the protected `connectionBean` variable. If your connector needs to override the `initialize()` method, it should call `super.initialize()` to capture the connection properties for the base classes.
2. Implementing the `start()` method, where the main logic for your connector runs. Use the configuration details from the connection object to connect to your underlying technology. If the connector is long-running, this may be the time to start up a separate thread. However, this has to conform the rules laid down for the category of connector you are implementing.
3. Using pre-existing, technology-specific clients and APIs to talk to your underlying technology.
4. Translating the underlying technology's representation of information into the open metadata representation used by the connector interface itself.

For the first point, you can retrieve general connection information from the [`Connection` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/frameworks/open-connector-framework/src/main/java/org/odpi/openmetadata/frameworks/connectors/properties/beans/Connection.java){ target=gh } object (returned by `getConnection()` or stored in `connectionBean`) like:

- the server address and protocol, by first retrieving the embedded [`Endpoint` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/frameworks/open-connector-framework/src/main/java/org/odpi/openmetadata/frameworks/connectors/properties/beans/Endpoint.java){ target=gh } with `getEndpoint()`:
    - retrieving the protocol by calling `getProtocol()` on the `Endpoint`
    - retrieving the address by calling `getNetworkAddress()` on the `Endpoint`
- the user Id, by calling `getUserId()` on the `Connection`
- the password, by calling either `getClearPassword()` or `getEncryptedPassword()` on the `Connection`, depending on what your underlying technology can handle
- any secured properties, by calling `getSecuredProperties()` on the `Connection`

Use these details to connect to and authenticate against your underlying technology, even when it is running on a different system from the connector itself. Of course, check for `null` objects (like the `Endpoint`) as well before blindly operating on them.

Retrieve additional properties by:

- calling `getConfigurationProperties()` on the `Connection`, which returns a `Map<String, Object>`
- calling `get(name)` against that `Map<>` with the name of each additional property of interest

Alternatively, use the helper methods inherited from `ConnectorBase`, such as `getStringConfigurationProperty()`, `getBooleanConfigurationProperty()`, `getIntConfigurationProperty()` and `getArrayConfigurationProperty()`.

Implementation of the remaining points (2-4) will vary widely depending on the specific technology being used. See the examples previously linked to delve deeper.

