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
- Specific interfaces used by the type of connector

!!! tip "No dependency on Egeria's OMAG Server Platform"
    Note that there is no dependency on Egeria's [OMAG Server Platform](/concepts/omag-server-platform) for these specific connector implementations: they could run in another runtime that supported the connector APIs.  In fact, even the Egeria interface modules should not be embedded in your jar file to allow your connector to run on any version of the OMAG Server Platform that supports your connector.

## Identify connection properties

Begin by identifying and designing the properties needed to connect to your tool or system. These will commonly include a network address, protocol, and user credentials, but could also include other information that can be stored in the configuration properties of the connection.

## Code the connector provider

--8<-- "docs/guides/developer/connector-provider-into.md"
--8<-- "docs/guides/developer/implemented-a-connector-provider.md"

!!! example "Example: connector provider for IBM DataStage"
    For example, the [`DataStageConnectorProvider` :material-github:](https://github.com/odpi/egeria-connector-ibm-information-server/blob/main/datastage-adapter/src/main/java/org/odpi/egeria/connectors/ibm/datastage/dataengineconnector/DataStageConnectorProvider.java){ target=gh } is used to instantiate connectors to IBM DataStage data processing engines. Therefore, its name and description refer to DataStage, and the connectors it instantiates are [`DataStageConnector`s :material-github:](https://github.com/odpi/egeria-connector-ibm-information-server/blob/main/datastage-adapter/src/main/java/org/odpi/egeria/connectors/ibm/datastage/dataengineconnector/DataStageConnector.java){ target=gh }.

!!! example "Example: connector provider for IBM Information Governance Catalog"
    Similarly, the [`IGCOMRSRepositoryConnectorProvider` :material-github:](https://github.com/odpi/egeria-connector-ibm-information-server/blob/main/igc-adapter/src/main/java/org/odpi/egeria/connectors/ibm/igc/repositoryconnector/IGCOMRSRepositoryConnectorProvider.java){ target=gh } is used to instantiate connectors to IBM Information Governance Catalog (IGC) metadata repositories. In contrast to the `DataStageConnectorProvider`, the `IGCOMRSRepositoryConnectorProvider`'s name and description refer to IGC, and the connectors it instantiates are [`IGCOMRSRepositoryConnector`s :material-github:](https://github.com/odpi/egeria-connector-ibm-information-server/blob/main/igc-adapter/src/main/java/org/odpi/egeria/connectors/ibm/igc/repositoryconnector/IGCOMRSRepositoryConnector.java){ target=gh }.

!!! tip "Connectors implement Egeria interfaces, not vice versa"
    Note that the code of all of these connector implementations exists outside Egeria itself (in separate code repositories), and there are no direct dependencies within Egeria on these external repositories or connectors.

All connectors can be configured with the network address and credential information needed to access the underlying tool or system. Therefore, you do not need to explicitly list properties for such basic details. However, the names of any additional configuration properties that may be useful to a specific type of connector can be described through the `recognizedConfigurationProperties` of the connector type.

### Implementation pattern

From the two examples ([`DataStageConnectorProvider` :material-github:](https://github.com/odpi/egeria-connector-ibm-information-server/blob/main/datastage-adapter/src/main/java/org/odpi/egeria/connectors/ibm/datastage/dataengineconnector/DataStageConnectorProvider.java){ target=gh } and [`IGCOMRSRepositoryConnectorProvider` :material-github:](https://github.com/odpi/egeria-connector-ibm-information-server/blob/main/igc-adapter/src/main/java/org/odpi/egeria/connectors/ibm/igc/repositoryconnector/IGCOMRSRepositoryConnectorProvider.java){ target = gh }), you will see that writing a connector provider follows a simple pattern:

- Extend a *connector provider* base class specific to your connector's interface.
- Define `static final` class members for the GUID, name, description and the names of any additional configuration properties.
- Write a single public constructor, with no parameters, that:
    - Calls `super.setConnectorClassName()` with the name of your connector class.
    - Creates a new `ConnectorType` object, sets it characteristics to the `static final` class members, and uses `.setConnectorProviderClassName()` to set the name of the connector provider class itself.
    - (Optional) Creates a list of additional configuration properties from the `static final` class members, and uses `.setRecognizedConfigurationProperties()` to add these to the connector type.
    - Sets `super.connectorTypeBean = connectorType`.

## Understand the connector interface

Now that you have the *connector provider* to instantiate your *connector*, you need to understand what your connector actually needs to do. For a service to use your connector, the connector must provide a set of methods that are relevant to that service.

!!! example "Example: data engine proxy connector interface"
    For example, the [data engine proxy services](/services/data-engine-proxy-services) integrate metadata from data engines with Egeria. To integrate DataStage with Egeria, we want our [`DataStageConnector` :material-github:](https://github.com/odpi/egeria-connector-ibm-information-server/blob/main/datastage-adapter/src/main/java/org/odpi/egeria/connectors/ibm/datastage/dataengineconnector/DataStageConnector.java){ target=gh } to be used by the data engine proxy services. Therefore, the connector needs to extend [`DataEngineConnectorBase` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/governance-servers/data-engine-proxy-services/data-engine-proxy-connector/src/main/java/org/odpi/openmetadata/governanceservers/dataengineproxy/connectors/DataEngineConnectorBase.java){ target=gh }, because this defines the methods needed by the data engine proxy services.

!!! example "Example: OMRS repository connector interface"
    Likewise, we want our [`IGCOMRSRepositoryConnector` :material-github:](https://github.com/odpi/egeria-connector-ibm-information-server/blob/main/igc-adapter/src/main/java/org/odpi/egeria/connectors/ibm/igc/repositoryconnector/IGCOMRSRepositoryConnector.java){ target=gh } to integrate IGC with Egeria as a metadata repository. Therefore, the connector needs to extend [`OMRSRepositoryConnector` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/repositoryconnector/OMRSRepositoryConnector.java){ target=gh }, because this defines the methods needed to integrate with [Open Metadata Repository Services (OMRS)](/services/omrs).

How would you know to extend these base classes? The *connector provider* implementations in the previous step each extended a base class specific to the type of connector they provide ([`DataEngineConnectorProviderBase` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/governance-servers/data-engine-proxy-services/data-engine-proxy-connector/src/main/java/org/odpi/openmetadata/governanceservers/dataengineproxy/connectors/DataEngineConnectorProviderBase.java){ target=gh } and [`OMRSRepositoryConnectorProviderBase` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/repositoryconnector/OMRSRepositoryConnectorProviderBase.java){ target=gh }). These *connector* base classes ([`DataEngineConnectorBase` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/governance-servers/data-engine-proxy-services/data-engine-proxy-connector/src/main/java/org/odpi/openmetadata/governanceservers/dataengineproxy/connectors/DataEngineConnectorBase.java){ target=gh } and [`OMRSRepositoryConnector` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/repositoryconnector/OMRSRepositoryConnector.java){ target=gh }) are in the same package structure as those *connector provider* base classes.

In both cases, by extending the abstract classes ([`DataEngineConnectorBase` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/governance-servers/data-engine-proxy-services/data-engine-proxy-connector/src/main/java/org/odpi/openmetadata/governanceservers/dataengineproxy/connectors/DataEngineConnectorBase.java){ target=gh } and [`OMRSRepositoryConnector` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/repositoryconnector/OMRSRepositoryConnector.java){ target=gh }) your connector must implement the methods these abstract classes define. These general methods implement your services (data engine proxy services and OMRS), without needing to know anything about the underlying technology. Therefore, you can simply "plug-in" the underlying technology: any technology with a connector that implements these methods can run your service. Furthermore, each technology-specific connector can decide how best to implement those methods for itself.

## Code the connector itself

Which brings you to writing the *connector* itself. Now that you understand the interface your connector must provide, you need to implement the methods defined by that interface.

Implement the connector by:

1. Retrieving *connection* information provided by the configuration. The default method for `initialize()` saves the connection object used to create the connector. If your connector needs to override the `initialize()` method, it should call `super.initialize()` to capture the connection properties for the base classes.
2. Implementing the `start()` method, where the main logic for your connector runs. Use the configuration details from the connection object to connect to your underlying technology. If the connector is long-running, this may be the time to start up a separate thread. However, this has to conform the rules laid down for the category of connector you are implementing.
3. Using pre-existing, technology-specific clients and APIs to talk to your underlying technology.
4. Translating the underlying technology's representation of information into the open metadata representation used by the connector interface itself.

For the first point, you can retrieve general connection information like:

- the server address and protocol, by first retrieving the embedded [`EndpointProperties` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/frameworks/open-connector-framework/src/main/java/org/odpi/openmetadata/frameworks/connectors/properties/EndpointProperties.java){ target=gh } with `getEndpoint()`:
    - retrieving the protocol by calling `getProtocol()` on the `EndpointProperties`
    - retrieving the address by calling `getAddress()` on the `EndpointProperties`
- the user Id, by calling `getUserId()` on the [`ConnectionProperties` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/frameworks/open-connector-framework/src/main/java/org/odpi/openmetadata/frameworks/connectors/properties/ConnectionProperties.java){ target=gh }
- the password, by calling either `getClearPassword()` or `getEncryptedPassword()` on the `ConnectionProperties`, depending on what your underlying technology can handle

Use these details to connect to and authenticate against your underlying technology, even when it is running on a different system from the connector itself. Of course, check for `null` objects (like the `EndpointProperties`) as well before blindly operating on them.

Retrieve additional properties by:

- calling `getConfigurationProperties()` on the `ConnectionProperties`, which returns a `Map<String, Object>`
- calling `get(name)` against that `Map<>` with the name of each additional property of interest

Implementation of the remaining points (2-3) will vary widely depending on the specific technology being used. See the examples previously linked to delve deeper.


