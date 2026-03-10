<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Digital Resource Connector

A *digital resource connector* is used to call the API of a particular type of [digital resource](/concepts/digital-resource) in order to access its content or metadata.  They may also listen for events from the digital resource if it emits them.  For example, you may have a digital resource connector to access a file, another to access a database, another to listen to an Apache Kafka topic, and another to access a system such as Apache Atlas.

## What is the interface of a digital resource connector?

The interface of a digital resource connector is a combination of the standard methods of an [Open Connector Framework (OCF)](/frameworks/ocf/overview) connector, to enable Egeria to start and stop it, plus something similar to the standard API provided by the digital resource.  The aim is to make its interface familiar to the developer who is coding the calls to the digital resource.

## Why develop and use a digital resource connector?

The real value of a digital resource connector over just calling the digital resource's API directly is that an instance of a digital resource connector can be created from the information contained in a [connection](/concepts/connection).  The connection includes details of the digital resource connectors' implementation, the endpoint of the digital resource plus any security information needed to access the digital resource.  A connection can be described as a Java object, as a JSON document or stored in open metadata as a collection of related entities starting with the [Connection entity](/types/2/0201-Connectors-and-Connections).  The connection, therefore, provides a standard way to distribute details about how to access the content of a particular digital resource, regardless of its type, around the open metadata ecosystem.

The security information supplied through the connection keeps secrets out of the caller's code.  The additional use of [secret store connectors](/concepts/secrets-store-connector) within a digital resource connector helps to keep these secrets out of the connection object and stored within encrypted vaults until they are needed.  Using a secrets store connector within a digital resource connector has no impact on the caller of the digital resource connector.

## Cataloguing a digital resource

When a digital resource is catalogued in open metadata, it is represented as an [Asset](/concepts/asset) entity.  Ideally, the Asset entity is linked to a Connection entity that describes the appropriate digital resource connector, any security information and the digital resource's endpoint.

Thus the combination of the asset and its connection allows the distribution of both descriptive information about the digital resource, plus the information needed to access it.

Since different users may be granted different levels of access to the digital resource's contents, it is also possible to add multiple connections to the asset, each with different security information attached.  When a particular user requests the digital resource connector for the asset, the [Metadata Access Server](/concepts/metadata-access-server) supplying the connection metadata calls its [server metadata security connector](/concepts/server-metadata-security-conector) to choose the appropriate connection for the user.

## How are digital resource connectors used?

The [Open Connector Framework (OCF)](/frameworks/ocf/overview) has a client called the *ConnectedAssetClient* that can be used to create an instance of a digital resource connector for an asset.   This connector can then be used in a view service API request, or by other connectors, such as [Integration Connectors](/concepts/integration-connector) and [Governance Services](/concepts/governance-service), to access the digital resource.

![Digital Resource Connector](digital-resource-connector.svg)

For example, this mechanism is used by the [Data Engineer API](/services/data-engineer/overview) to extract tabular data sets, and by the [Runtime Manager API](/services/runtime-manager/overview) to manage Egeria's runtime environments.

## Egeria's Digital Resource Connectors

* [JDBC Resource Connector](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/data-store-connectors/jdbc-resource-connector)
* [Basic File Resource Connector](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/data-store-connectors/file-connectors/basic-file-connector)
* [CSV File Resource Connector](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/data-store-connectors/file-connectors/csv-file-connector)
* [Data Folder Resource Connector](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/data-store-connectors/file-connectors/data-folder-connector)
* [Egeria's OMAG Server Platform and Servers Resource Connectors](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/system-connectors/egeria-system-connectors)
* [Apache Kafka Admin Resource Connector](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/system-connectors/apache-kafka-connectors)
* [Apache Kafka Topic Resource Connector](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/event-bus-connectors/open-metadata-topic-connectors/kafka-open-metadata-topic-connector)
* [Apache Atlas REST API Resource Connector](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/system-connectors/apache-atlas-connectors)
* [Unity Catalog REST API Resource Connector](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/data-manager-connectors/unity-catalog-connectors)

!!! education "Further information"
    
    - [Open Connector Framework (OCF)](/frameworks/ocf/overview).

---8<-- "snippets/abbr.md"
