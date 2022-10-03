<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Developer Guide

This guide supports developers wishing to customize Egeria to run in additional environments, exchange metadata with additional third party technologies and/or augment existing tools and utilities. 

--8<-- "docs/guides/developer/developer-choices.md"

??? attention "REST APIs are intended for internal use"
    The REST APIs are usable directly for calling from non-Java platforms; however, they are designed for the internal use of Egeria and are not guaranteed to be backwards compatible.
    
    The structure of the URL for an Egeria REST API varies lightly depending on whether it is a call to an [OMAG Server Platform](/concepts/omag-server-platform) service or an [OMAG Server](/concepts/omag-server) service.

## Getting Started

The developer guide is organized as follows:

- [Working with the platform APIs](#working-with-the-platform-apis) - Using Egeria APIs to configure and operate Egeria's [OMAG Server Platform](/concepts/omag-server-platform).

- [Using connectors](#using-connectors) - initializing and calling a digital resource connector from external services and other connectors.

- [Building connectors](#building-connectors) - How to write new [connectors](#what-is-a-connector) to integrate different technologies together.

- [Building open metadata archives](#building-open-metadata-archives) - Working with [Open Metadata Archives](/concepts/open-metadata-archive) to add new open metadata types or standard metadata definitions that can be shared and loaded into multiple metadata repositories.

- [Working with the open metadata and governance APIs](#working-with-the-open-metadata-and-governance-apis) - Using Egeria's open metadata and governance APIs to create new services or to augment existing services.

- [Adding your own registered services](#adding-registered-services) - Extending Egeria by adding new [registered services](/concepts/omag-subsystem/#registered-services).


## Working with the platform APIs

The platform APIs fall into three categories:

* Configuring the [OMAG Server Platform](/concepts/omag-server-platform) and [OMAG Servers](/concepts/omag-server).
* Starting and stopping OMAG Servers
* Querying the status of the platform and its servers.

The Java clients for a specific platform API are located in its `-client` module.

--8<-- "docs/guides/developer/java-clients/platform-constructor-parameters.md"

Below is an example of using the [Administration Services](/services/admin-services/overview) to construct its `MetadataAccessStoreConfigurationClient` client.  As the name suggests, this client is used to configure a new [metadata access store](/concepts/metadata-access-store) server.

??? example "Example: Creating the configuration client for a Metadata Access Store"
    ```java linenums="1"
    MetadataAccessStoreConfigurationClient client = new MetadataAccessStoreConfigurationClient(clientUserId, serverName, platformURLRoot);
    ```

Once the client is created, use it to call the API it offers which is documented using [Javadoc](https://odpi.github.io/egeria/org/odpi/openmetadata/adminservices/client/MetadataAccessStoreConfigurationClient.html){ target=javadoc }.  
For example, the code below sets up the descriptive properties of the server.

??? example "Example: Calling the configuration client for a Metadata Access Store"
    ```java linenums="1"
    client.setServerDescription("Metadata Access Store called " + serverName + " running on platform " + platformURLRoot);
    client.setServerUserId(serverName + "npa");
    client.setServerType(null); // Let the admin service set up the server types
    client.setOrganizationName(organizationName);
    client.setMaxPageSize(maxPageSize);
    ```
    
!!! education "Further information"
    
    - [Administration Services](/services/admin-services/overview) for both configuring the OMAG Server Platform and OMAG Servers as well as starting and stopping them.
    - [Platform Operation Services](/services/platform-services/overview) for querying the status of the platform.
    - [Egeria's Javadoc](https://odpi.github.io/egeria/index.html).
  

## Working with the open metadata and governance APIs

The open metadata and governance APIs are provided by the [Open Metadata Access Services (OMASs)](/services/omas) and the [Open Metadata View Services (OMVSs)](/services/omvs).  The OMASs run in the [metadata access server](/concepts/metadata-access-server) and provide specialized services for querying and maintaining metadata in the local metadata repository (if any) and any metadata repository connected via [cohorts](/concepts/cohort-member).  The clients of the OMASs are written in Java and are designed to be used by applications running behind the fire-wall with the metadata repositories.  The OMVSs run in the [view server](/concepts/view-server) and are designed to be consumed by user interface code typically written in JavaScript.  These interfaces are called directly as REST API calls.

### Using the OMAS clients

The Java clients for an OMAS are located in its `-client` module.

--8<-- "docs/guides/developer/java-clients/omas-constructor-parameters.md"

Below is an example of using the [Asset Consumer OMAS](/services/omas/asset-consumer/overview) to construct its `AssetConsumer` client.

```
          AssetConsumer client = new AssetConsumer(serverName, platformURLRoot);
```
Once the client is created, use it to call the API it offers which is documented using [Javadoc](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/assetconsumer/client/AssetConsumer.html){ target=javadoc }.  For example, the code below adds a [like](/concepts/like) to an added and then queries its properties and all of the metadata elements attached to it.
```
          client.addLikeToAsset(clientUserId, assetGUID, true);
          
          AssetUniverse assetUniverse = client.getAssetProperties(clientUserId, assetGUID);

```
Each OMAS has its own specialized API and its own style, but typically there are methods for creating, updating and deleting elements along with methods for linking them together and unlinking them - also maintaining classifications.  If the OMAS is maintaining assets, you may see methods for publishing and withdrawing assets.  The publish method updates the asset's zones to the OMAS's `PublishedZones` and the withdraw method updates the asset's zones to the OMAS's `DefaultZones`.  Typically the asset is only visible to most users when the published zones are in use.  The default zones are used while the asset is being set up.

The `findXXX` methods typically take a regular expression and look for the value in all properties.  The `getXXXByName` style method does not use wild cards and retrieves the element if there is an exact match in the `qualifiedName` or `displayName`.  Finally, it is typical to have methods to retrieve a single element via its unique identifier (guid).


    
#### Registering a listener

Some OMASs offer an event interface for receiving events from the [out topic](/concepts/out-topic).  To use it, your java class needs to extend the event listener interface and implement the abstract `processEvent` method.  Below is a simple example from Asset Consumer OMAS.  The event type is used to determine which java class to use to cast the event so its payload can be accessed.

```java
public class AssetLookUp extends AssetConsumerEventListener
{
    /**
     * Process an event that was published by the Asset Consumer OMAS.
     *
     * @param event event object - call getEventType to find out what type of event.
     */
    public void processEvent(AssetConsumerEvent event)
    {
       if (event.getEventType() == AssetConsumerEventType.NEW_ASSET_EVENT)
       {
           NewAssetEvent assetEvent = (NewAssetEvent)event;
                   
           System.out.println("EVENT: " + assetEvent.getEventType().getEventTypeName() + " - for asset " + assetEvent.getAsset().getGUID());
       }
       else if (event.getEventType() == AssetConsumerEventType.UPDATED_ASSET_EVENT)
       {
           UpdatedAssetEvent assetEvent = (UpdatedAssetEvent)event;
       
           System.out.println("EVENT: " + assetEvent.getEventType().getEventTypeName() + " - for asset " + assetEvent.getAsset().getGUID() + " - at " + assetEvent.getUpdateTime());
       } 
    }
}
```

If your client is running outside of the OMAG Server Platform, you will need to add a dependency to your client for the [Open Metadata Topic Connector](/concepts/open-metadata-topic-connector) that is in use in the OMAG Server.  For example, if you see this error:

```bash

There was a org.odpi.openmetadata.frameworks.connectors.ffdc.ConnectionCheckedException exception when calling the OMAG Server Platform.  Error message is: OCF-CONNECTION-400-005 Unknown Connector Provider class org.odpi.openmetadata.adapters.eventbus.topic.kafka.KafkaOpenMetadataTopicProvider passed in connection <Unknown>

Process finished with exit code 0
```

```xml
        <dependency>
            <groupId>org.odpi.egeria</groupId>
            <artifactId>kafka-open-metadata-topic-connector</artifactId>
            <scope>compile</scope>
            <version>${open-metadata.version}</version>
        </dependency>

```

!!! education "Further information"
    
    - [Specific documentation for each OMAS](/services/omas).
    - [Egeria's Javadoc](https://odpi.github.io/egeria/index.html).

## Using connectors

--8<-- "docs/guides/developer/using-connectors.md"

## Building connectors

--8<-- "docs/guides/developer/inside-a-connector.md"


### Implementation steps 

To write an open connector you need to complete four steps:

1. Identify the properties for the connection.
2. Write the connector provider.
3. Understand the interface that the connector needs to implement and the support provided by its base class.
4. Write the connector itself.

All the code you write to implement these should exist in its own module, and as illustrated by the examples could even be in its own independent code repository. Their implementation will have dependencies on Egeria's:

- [Open Connector Framework (OCF)](/frameworks/ocf/overview)
- [Audit Log Framework (ALF)](/frameworks/alf/overview)
- Specific interfaces used by the type of connector

!!! tip "No dependency on Egeria's OMAG Server Platform"
    Note that there is no dependency on Egeria's [OMAG Server Platform](/concepts/omag-server-platform) for these specific connector implementations: they could run in another runtime that supported the connector APIs.  In fact, even the Egeria interface modules should not be embedded in your jar file to allow your connector to run on any version of the OMAG Server Platform that supports your connector.

## Extending Egeria using connectors

Egeria has extended the basic concept of the OCF connector and created specialized connectors for different purposes. The following types of connectors are supported by the Egeria subsystems with links to the documentation and implementation examples.

| Type of Connector             | Description | Documentation                                                                                 | Implementation Examples |
| :-----------------------------| :---------- |:----------------------------------------------------------------------------------------------| :---------------------- |
| Integration Connector         | Implements metadata exchange with third party tools. | [Building Integration Connectors](/guides/developer/integration-connectors/overview)          | [integration-connectors :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/integration-connectors){ target=gh } |
| Open Discovery Service        | Implements automated metadata discovery.| [Building Open Discovery Services](/guides/developer/open-discovery-services/overview)        | [discovery-service-connectors :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/discovery-service-connectors){ target=gh } |
| Governance Action Service     | Implements automated governance. | [Building Governance Action Services](/guides/developer/governance-action-services/overview)  | [governance-action-connectors :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/governance-action-connectors){ target=gh } |
| Configuration Document Store  | Persists the configuration document for an OMAG Server. | [Configuration Document Store Connectors](/concepts/configuration-document/#storage)          | [configuration-store-connectors :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/configuration-store-connectors){ target=gh } |
| Platform Security Connector   | Manages service authorization for the OMAG Server Platform. | [Metadata Security Connectors](/features/metadata-security)                                   | [open-metadata-security-samples :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-resources/open-metadata-samples/open-metadata-security-samples){ target=gh } |
| Server Security Connector     | Manages service and metadata instance authorization for an OMAG Server. | [Metadata Security Connectors](/features/metadata-security)                                   | [open-metadata-security-samples :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-resources/open-metadata-samples/open-metadata-security-samples){ target=gh } |
| Metadata Collection (repository) Store | Interfaces with a metadata repository API for retrieving and storing metadata. | [OMRS Repository Connectors](/concepts/repository-connector)                                  | [open-metadata-collection-store-connectors :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/open-metadata-collection-store-connectors){ target=gh } |
| Metadata Collection (repository) Event Mapper | Maps events from a third party metadata repository to open metadata events. | [OMRS Event Mappers](/concepts/event-mapper-connector)                                        | none |
| Open Metadata Archive Store   | Reads an open metadata archive from a particular type of store. | [OMRS Open Metadata Archive Store Connector](/concepts/open-metadata-archive-store-connector) | [open-metadata-archive-connectors :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/open-metadata-archive-connectors){ target=gh } |
| Audit Log Store               | Audit logging destination | [OMRS Audit Log Store Connector](/concepts/audit-log-store-connector)                         | [audit-log-connectors :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/audit-log-connectors){ target=gh } |
| Cohort Registry Store         | Local store of membership of an open metadata repository cohort. | [OMRS Cohort Registry Store](/concepts/cohort-registry-store-connector)                       | [cohort-registry-store-connectors :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/cohort-registry-store-connectors){ target=gh } |
| Open Metadata Topic Connector | Connects to a topic on an external event bus such as Apache Kafka. | [Open Metadata Topic Connectors](/concepts/open-metadata-topic-connector)                     | [open-metadata- topic-connectors :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/event-bus-connectors/open-metadata-topic-connectors){ target=gh } |

You can write your own connectors to integrate additional types of technology or extend the capabilities of Egeria - and if you think your connector is more generally useful, you could consider [contributing it to the Egeria project](/guides/community).

## Building open metadata archives

--8<-- "docs/concepts/open-metadata-archive-intro.md"
--8<-- "docs/guides/developer/open-metadata-archives/in-memory-archive-construction.md"

??? example "Open metadata archive examples"
    * [Defining new types](/guides/developer/open-metadata-archive/defining-new-types)
    * [Code samples of archive builders containing Coco Pharmaceuticals metadata](https://github.com/odpi/egeria-samples/tree/master/sample-metadata-archives/coco-metadata-archives)


## Adding registered services
  
Registered services are optional services that plug into Egeria's [OMAG Server Platform](/concepts/omag-server-platform). There are 4 types:
  
  - [Open Metadata Access Services (OMAS)](/services/omas) provide specialized APIs and events for retrieving and maintaining open metadata.  These services run in a [Metadata Access Server](/concepts/metadata-access-server).
  
  - [Open Metadata Engine Services (OMES)](/services/omes) provide specialist APIs that support specific types of governance engines.  These services run in an [Engine Host](/concepts/engine-host) and call an OMAS to retrieve and maintain open metadata.
  
  - [Open Metadata Integration Services (OMIS)](/services/omis) provide specialist connector APIs for exchanging open metadata with third party technologies.  These services run in an [Integration Daemon](/concepts/integration-daemon) and call an OMAS to retrieve and maintain open metadata.
  
  - [Open Metadata View Services (OMVS)](/services/omvs) provide specialist REST APIs for browser-based user interfaces (UIs).  These services run in a [View Server](/concepts/view-server) and call an OMAS to retrieve and maintain open metadata.

There are many choices of registered services within the Egeria project.  However, you may add your own. The recommended modules for registered services (required if it is to be contributed to the Egeria project) are shown in the table below:

| Module naming | Description | OMAS | OMES | OMIS | OMVS |
| --------------|-------------|------|------|------|------|
| *moduleName*-api | Client java interface(s), property beans and rest beans. | CP | CP | CP | P |
| *moduleName*-client | Java client implementation. | CP | C | C | N |
| *moduleName*-topic-connectors | Java connectors for sending and receiving events.  | OCP | N | N | N |
| *moduleName*-server | Server-side REST and event management implementation.  | P | P | P | P |
| *moduleName*-spring | Server-side REST API.  | P | P | P | P |

**Key:**

* CP - Required and runs in external clients plus in the OMAG Server Platform.
* C - Required and runs in external clients.
* P - Required and runs in the OMAG Server Platform.
* OCP - Optional and when provided runs in external clients plus in the OMAG Server Platform.
* N - Not implemented/needed.

The modules for each registered service that need to run in the OMAG Server Platform are delivered in their own jar that is available to the OMAG Server Platform via the CLASSPATH.  Inside the registered service's spring jar are one or more REST APIs implemented using [Spring Annotations](/guides/contributor/runtime/#spring).  On start up, the OMAG Server Platform issues a *Component Scan* to gather details of its REST APIs.  This process loads the spring module which in turn loads the server and api modules of registered services it finds and they are [initialized as part of the platform's capabilities](/concepts/omag-server-platform/#inside-the-omag-server-platform) and are callable via the platform's root URL and port.  The client module of an OMAS is loaded by an OMES, OMIS or OMVS registered service that is dependent on the OMAS to get access to open metadata.

The best guide for building registered services are the existing implementations found in [egeria.git](https://github.com/odpi/egeria/tree/master/open-metadata-implementation){ target=gh }.  You can see the way the code is organized and the services that they depend on.

## Summary

Egeria is designed to simplify the effort necessary to integrate different technologies so that they can actively share and consume metadata from each other.

It focuses on providing five types of integration interfaces.

- [Connectors](#what-is-a-connector) that translate between third party APIs and open metadata APIs. These connectors are hosted in the Egeria servers and support the active exchange of metadata with these technologies.
- [Connectors](/guides/developer/using-connectors) for accessing popular type of data sources that also retrieve open metadata about the data source. This allows applications and tools to understand the structure, meaning, profile, quality and lineage of the data they are using.
- [Java clients](#using-the-clients) for applications to call the [Open Metadata Access Service (OMAS)](/services/omas) interfaces, each of which are crafted for particular types of technology. These interfaces support both synchronous APIs, inbound event notifications and outbound asynchronous events.
- [REST APIs](#using-the-rest-apis) for the Egeria Services. These include the [access services](/services/omas), admin services and [platform services](/services/platform-services/overview).
- Kafka topics with JSON payloads for asynchronous communication (both in and out) with the open metadata ecosystem.
  [Learn more ...](/services/omas)


--8<-- "snippets/abbr.md"
