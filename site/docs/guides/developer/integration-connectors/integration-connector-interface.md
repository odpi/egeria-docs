<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


An integration connector can:

- Poll the third party technology each time that the integration daemon calls your integration connector's `refresh()` method.
- Register a listener with its context to act on notifications from the open metadata ecosystem.
- Register with an external notification service that sends notifications on its own thread.
- Listen on a blocking call, waiting for the third party technology to send a notification.
- Issue queries and maintenance (create, update, delete) requests to the open metadata repositories.

Access to open metadata is provided via a *context* object defined by the [Open Integration Framework (OIF)](/frameworks/oif/overview).  There is a [single context interface](/guides/developer/integration-connectors/integration-context) for all integration connectors; it provides:

- The ability to register a listener to receive events from the open metadata ecosystem.
- A [client for each type of open metadata element](/guides/developer/integration-connectors/integration-context/#the-open-metadata-clients) that can create, update, classify, link and delete metadata, along with the retrieval methods needed to compare open metadata with the metadata in the third party technology.
- The ability to create a [digital resource connector](/concepts/digital-resource-connector) for an asset so that the third party technology can be called.
- Support for [external identifiers](/features/external-identifiers/overview), [templates](/features/templated-cataloguing/overview) and [external source metadata provenance](/features/metadata-provenance/overview).
- Utilities such as the file classifier, the directory listeners and the name case converters.

!!! attention "The integration services have been removed"
    Earlier releases of Egeria offered a range of *Open Metadata Integration Services (OMISs)*, each with its own specialized context interface and its own set of base classes (`DatabaseIntegratorConnector`, `FilesIntegratorConnector`, `TopicIntegratorConnector` and so on).  Choosing the right integration service was the first decision a connector developer had to make.
    
    These services have been removed.  All function is now available through the single [integration context](/guides/developer/integration-connectors/integration-context) supplied by the Open Integration Framework, and there are just two base classes to choose between (described below).  If you are migrating an older connector, the mapping is mostly mechanical: replace the `XXXIntegratorConnector` superclass with `DynamicIntegrationConnectorBase`, and replace the `getContext()` calls with the `integrationContext` variable.

## Dependencies

These are the standard dependencies for an integration connector:

* [Audit log framework (ALF)](/frameworks/alf/overview) - for logging audit log messages.
* [Open Connector Framework (OCF)](/frameworks/ocf/overview) - basic connector interfaces.
* [Open Metadata Framework (OMF)](/frameworks/omf/overview) - the open metadata clients, properties and types used by the context.
* [Open Integration Framework (OIF)](/frameworks/oif/overview) - the integration connector base classes and the integration context.
* [Open Governance Framework (OGF)](/frameworks/ogf/overview) - the catalog target properties and the ability to initiate governance actions.

??? example "Example of the Gradle dependencies for an integration connector ..."

    ```groovy
    dependencies {
        compileOnly 'org.odpi.egeria:audit-log-framework'
        compileOnly 'org.odpi.egeria:open-connector-framework'
        compileOnly 'org.odpi.egeria:open-metadata-framework'
        compileOnly 'org.odpi.egeria:open-integration-framework'
        compileOnly 'org.odpi.egeria:open-governance-framework'
    }
    ```

??? example "Example of the Maven dependencies for an integration connector ..."
    
    ```xml
            <dependency>
                <groupId>org.odpi.egeria</groupId>
                <artifactId>audit-log-framework</artifactId>
                <scope>provided</scope>
                <version>${open-metadata.version}</version>
            </dependency>
    
            <dependency>
                <groupId>org.odpi.egeria</groupId>
                <artifactId>open-connector-framework</artifactId>
                <scope>provided</scope>
                <version>${open-metadata.version}</version>
            </dependency>

            <dependency>
                <groupId>org.odpi.egeria</groupId>
                <artifactId>open-metadata-framework</artifactId>
                <scope>provided</scope>
                <version>${open-metadata.version}</version>
            </dependency>

            <dependency>
                <groupId>org.odpi.egeria</groupId>
                <artifactId>open-integration-framework</artifactId>
                <scope>provided</scope>
                <version>${open-metadata.version}</version>
            </dependency>

            <dependency>
                <groupId>org.odpi.egeria</groupId>
                <artifactId>open-governance-framework</artifactId>
                <scope>provided</scope>
                <version>${open-metadata.version}</version>
            </dependency>
    ```
    
    !!! tip "Use provided scope ..."

        Notice the `<scope>provided</scope>` setting for the Egeria libraries (`compileOnly` in Gradle).  This prevents the Egeria libraries from being included in your connector jar file.  By using the provided scope, your connector can run with any level of Egeria that supports this type of connector.  Without it, duplicate Egeria classes would be loaded into your OMAG Server Platform and if the platform was running at a different level it is not certain which version of the classes would run. (It "may" be ok but experience, as we know, teaches us that "if it can go wrong it will go wrong" so avoiding problems is always preferable :).

You will also need to add the dependencies for the third party technology that your connector is calling.

## Choosing a base class

All integration connectors inherit from (extend) the [`IntegrationConnectorBase` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/frameworks/open-integration-framework/src/main/java/org/odpi/openmetadata/frameworks/integration/connectors/IntegrationConnectorBase.java){ target=gh }.  This class defines the lifecycle methods of the integration connector.  There are two ways to build on it:

=== "DynamicIntegrationConnectorBase (recommended)"

    [`DynamicIntegrationConnectorBase` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/frameworks/open-integration-framework/src/main/java/org/odpi/openmetadata/frameworks/integration/connectors/DynamicIntegrationConnectorBase.java){ target=gh } extends `IntegrationConnectorBase` to add support for [catalog targets](/concepts/catalog-target).

    A single running instance of the connector works with many pieces of third party technology.  Each one is attached to the connector's metadata element using a *CatalogTarget* relationship, and the work for it is performed by a [catalog target processor](/guides/developer/integration-connectors/catalog-targets).  The base class discovers the catalog targets, creates and starts a processor for each one, calls `refresh()` on each of them, distributes open metadata events to them, and disconnects the ones that are removed.

    This is the right choice for almost every new connector.  See [supporting catalog targets](/guides/developer/integration-connectors/catalog-targets).

=== "IntegrationConnectorBase"

    Extending `IntegrationConnectorBase` directly means your connector works with exactly one piece of third party technology, identified by the [endpoint](/concepts/endpoint) in its own [connection](/concepts/connection).  To monitor three databases you would deploy three configured instances of the connector.

    Use this style only when the connector is not working with a catalogued resource at all - for example, the [OpenLineage log store connectors :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/integration-connectors/openlineage-integration-connectors/README.md){ target=gh } that write a log of open lineage events to a fixed destination.

## The lifecycle methods

![Methods implemented by an integration connector](/guides/developer/integration-connectors/integration-connector-methods.svg)
> Methods implemented by an integration connector.  The base class implements the `initialize()`, `setAuditLog()`, `setConnectorName()`, `initializeEmbeddedConnectors()` and `setContext()` methods.  Your integration connector supplies the `start()`, `refresh()` and `disconnect()` methods.  It implements the `engage()` method only if it needs to issue a blocking call.  When the connector supports catalog targets, the `start()`, `refresh()` and `disconnect()` methods are also implemented on each target processor - one for each catalog target.

- `initialize` is a standard method for all connectors that is called by the [connector broker](/concepts/connector-broker) when a request is made to create an instance of the connector. The connector broker uses the initialize method to pass the [connection](/concepts/connection) object used to create the connector instance and a unique identifier for this instance of the connector. This method is provided by the integration connector's base class.  Your code can access the connection via the `connectionBean` variable and the connector's unique identifier via the `connectorInstanceId` variable.

- `setAuditLog` provides an [Audit Log Framework (ALF)](/frameworks/alf/overview) compatible logging destination. This method is provided by the integration connector's base class.  Your code can access the audit log via the `auditLog` variable.

- `setConnectorName` provides the name of the connector from the configuration, so it can be used for logging. This method is provided by the integration connector's base class.  Your code can access your integration connector's name via the `connectorName` variable.

- `initializeEmbeddedConnectors` saves the optional list of embedded connectors that were defined in the connection object for your integration connector when it was configured.  These connectors are [digital resource connectors](/concepts/digital-resource-connector) - a secrets store connector is a common example. This method is provided by the integration connector's base class.  Your code can access the embedded connectors via the `embeddedConnectors` variable.

- `setContext` sets up the [integration context](/guides/developer/integration-connectors/integration-context) object. This method is provided by the integration connector's base class.  Your code accesses the context through the `integrationContext` variable.  Note that when the connector supports catalog targets, each catalog target processor has its own specialized `CatalogTargetContext`, also called `integrationContext`, which is set up for the metadata source and permitted synchronization of its particular catalog target.
    
- `start` indicates that the connector is completely configured (that is all the methods listed above have been called) and it can begin processing. This call is where the configuration properties are extracted from the connection object.  It is also where the catalog targets manager is created, so always call `super.start()` first.

- `engage` is used as an alternative to `refresh` when the connector is configured to need to issue blocking calls to wait for new metadata. It is called from its own thread. It is recommended that the `engage()` method returns when each blocking call completes. The integration daemon will pause a second and then call `engage()` again. This pattern enables the calling thread to detect the shutdown of its hosting integration daemon server.  The base class implementation throws an exception because a call to it indicates a mismatch between the configuration and the connector implementation.  You only need to override it if your integration connector is issuing blocking calls.

- `refresh` requests that the connector does a comparison of the metadata in the third party technology and open metadata repositories. Refresh is called from the connector's own thread under the following conditions:

    1. when the integration connector first starts and then
    1. at intervals defined in the connector's configuration as well as
    1. any external REST API calls to explicitly refresh the connector.

    `DynamicIntegrationConnectorBase` implements `refresh()` for you: it re-reads the catalog targets and calls `refresh()` on each catalog target processor.  If you override it, call `super.refresh()`.
    
- `disconnect` is called when the server is shutting down. The connector should free up any resources that it holds since it is not needed any more.  The base class disconnects the catalog targets' resource connectors, so call `super.disconnect()`.  Once disconnect has been called the context is no longer valid; calls to it throw `UserNotAuthorizedException`.

Therefore, you are typically looking to implement the `start`, `refresh` and `disconnect` methods in your integration connector, and optionally overriding the `engage` method if your connector issues blocking calls.  If your connector supports catalog targets, most of this work moves to the [catalog target processor](/guides/developer/integration-connectors/catalog-targets), and the connector class itself becomes very small.
