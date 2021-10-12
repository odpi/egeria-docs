---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Integration Connectors

An *integration connector* is a pluggable component that manages the metadata exchange to a third party technology. It is hosted in an [integration service](/egeria-docs/services/omis) which is, in turn, running in an [integration daemon](/egeria-docs/concepts/integration-daemon).

![Figure 1](/egeria-docs/connectors/integration/integration-connectors.svg)
> **Figure 1:** Integration connectors

The integration connectors can:

- Listen on a blocking call for the third party technology to send a notification.
- Register with an external notification service that sends notifications on its own thread.
- Register a listener with the OMAS client to act on notifications from the OMAS's [Out Topic](/egeria-docs/concepts/out-topic).
- Poll the third party technology each time that the `refresh()` method is called.

## Interface

The interface that all integration connectors must implement is defined by [`IntegrationConnectorBase` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/governance-servers/integration-daemon-services/integration-daemon-services-api/src/main/java/org/odpi/openmetadata/governanceservers/integrationdaemonservices/connectors/IntegrationConnectorBase.java){ target=gh }:

![Figure 2](integration-connector-methods.svg)
> **Figure 2:** Methods implemented by an integration connector

- `initialize` is a standard method for all connectors that is called by the [connector broker](/egeria-docs/concepts/connector-broker) when the connector is created. The [connector](/egeria-docs/frameworks/ocf/#connector) is passed the [connection](/egeria-docs/frameworks/ocf/#connection) object from the configuration and a unique identifier for this instance of the connector.
- `setAuditLog` provides a logging destination (see [Audit Log Framework (ALF)](/egeria-docs/frameworks/alf/overview)).
- `setConnectorName` provides the name of the connector for logging.
- `setContext` sets up the integration-specific context. This provides an interface to the services of the OMAS that the integration service is paired with. Although the interfaces vary from integration service to integration service, they typically offer the following types of method call for each type of metadata it supports:
    - The ability to register a listener to receive events from the OMAS's [Out Topic](/egeria-docs/concepts/out-topic), or send events to the OMAS's [In Topic](/egeria-docs/concepts/in-topic).
    - The ability to create and update metadata instances.
    - For assets, the ability to change an asset's visibility by changing its zone membership using the `publish` and `withdraw` methods.
    - The ability to delete metadata.
    - Various retrieval methods to help when comparing the metadata in the open metadata repositories with the metadata in the third party technology.
- `start` indicates that the connector is completely configured and can begin processing. This call can be used to register with non-blocking services. For example, it can register a listener with the OMAS [Out Topic](/egeria-docs/services/omas/client-server/#in-topic) with the context.
- `engage` is used when the connector is configured to need to issue blocking calls to wait for new metadata. It is called from its own thread. It is recommended that the `engage()` method returns when each blocking call completes. The integration daemon will pause a second and then call `engage()` again. This pattern enables the calling thread to detect the shutdown of the integration daemon server.
- `refresh` requests that the connector does a comparison of the metadata in the third party technology and open metadata repositories. Refresh is called:
    1. when the integration connector first starts and then
    1. at intervals defined in the connector's configuration as well as
    1. any external REST API calls to explicitly refresh the connector.
- `disconnect` is called when the server is shutting down. The connector should free up any resources that it holds since it is not needed any more.

## Two approaches to designing the connections for an integration connector 

Figure 3 shows the approach used for a dedicated connector to a specific third party technology deployment.

![Figure 3](explicit-endpoints.svg)
> **Figure 3:** An explicit endpoint is added to the integration connector's connection in its configuration

Figure 4 shows the approach used to catalog all instances of a particular type of technology.

![Figure 4](learned-endpoints.svg)
> **Figure 4:** No endpoint is configured in the integration connector's connection.

Location is determined from the endpoints that are stored in open metadata.  The connector registers a listener with the context and it listens for events relating to endpoint of the appropriate values.

An integration connector can choose to support one of these patterns or switch dynamically depending on the presence of the endpoint in the connector's configuration. 

??? education "Further information"
    - [Open Connector Framework (OCF)](/egeria-docs/frameworks/ocf/overview) that defines the behavior of all connectors.
    - [Configuring an integration daemon](/egeria-docs/guides/admin/servers/configuring-an-integration-daemon) to understand how to set up an integration connector.
    - [Developer guide](/egeria-docs/guides/developer) for more information on writing connectors.

--8<-- "snippets/abbr.md"
