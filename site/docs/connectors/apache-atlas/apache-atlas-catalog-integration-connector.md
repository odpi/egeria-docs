<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# Apache Atlas Integration Connector

???+ info "Connector summary"
    - Connector Category: [Integration Connector](/concepts/integration-connector)
    - Hosting Server: [Integration Daemon](/concepts/integration-daemon)
    - Source Module: [apache-atlas-connectors :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/system-connectors/atlas-integration-connector){ target=gh }
    - Jar File Name: `apache-atlas-connectors.jar`
    - Connector Provider Class Name: `org.odpi.openmetadata.adapters.connectors.apacheatlas.integration.ApacheAtlasIntegrationProvider`

## Overview

---8<-- "snippets/systems/apache-atlas-intro.md"

Reasons for integrating Apache Atlas metadata into a wider open metadata ecosystem include:

* To push glossaries and classification definitions to Apache Atlas so its users get to use the same definitions for the governance of their data as other parts of the organization.  This may simply to help start up a new Apache Atlas deployment, or as part of a broader consistency initiative.
* To share glossaries and classification definitions that have been developed by an Apache Atlas user community in order to seed other projects and tools.
* To share details of the data sets that Apache Atlas has catalogued with other catalogs and tools.  For example, the Apache Atlas catalog of data sets may be shared with data science or stewardship tools.  Tags, classifications and semantic assignments made to these assets by users of these tools could then be pushed back to Apache Atlas to enhance the use and governance of their associated data through Apache Atlas.
* To extract lineage information for data flowing through the data platforms and processes that Apache Atlas is capturing.
* To improve the usefulness of Apache Atlas metadata by augmenting it with additional insight from the open metadata ecosystem.
* To improve the governance of Apache Atlas metadata by analysing and reporting on the content and usage of Apache Atlas metadata.

## Integration Connector function

The Apache Atlas integration connector provides an ongoing exchange of metadata between Apache Atlas and the open metadata ecosystem.

![Figure 1](apache-atlas-catalog-integration-connector.svg)
> **Figure 1:** Operation of the Apache Atlas integration connector

The type of metadata exchanged, and the direction of the exchange, is controlled by the configuration properties added to this connector's connection.  Specifically this connector can optionally:

* Publishes glossaries, glossary categories and ACTIVE glossary terms that originate from the open metadata ecosystem into Apache Atlas.  The connector makes no attempt to detect changes to these glossary elements in Apache Atlas.  Such changes will be overridden the next time the integration connector refreshes the glossary metadata in Apache Atlas.
* Publishes glossaries, glossary categories and glossary terms that originate in Apache Atlas into the open metadata ecosystem.  These elements will be read-only in the open metadata ecosystem.
* Catalog all Apache Atlas entities of type *DataSet* in the open metadata ecosystem.  
* Catalog all Apache Atlas lineage relationships (*dataset_process_inputs* and *dataset_process_outputs*) in the open metadata ecosystem.  These relationships link the DataSet entities from Apache Atlas and contribute to the enterprise's view of lineage.
* Maintain a reference data set of classifications used in Apache Atlas.  This reference data set can be used to create new classification definitions in Apache Atlas, catalog the Apache Atlas classificationDefs in the reference data set and record the classifications in use in Apache Atlas.
* Add definitions of open metadata entities and classifications linked to an open metadata entity that originated in Apache Atlas to its counterpart in Apache Atlas.  This way, the Apache Atlas users can see the same information about their data sets and the native users of the open metadata ecosystem.  There is specialized behaviour in how informal tags from the open metadata ecosystem are handled in Apache Atlas.

### Metadata ownership 

The concept of ownership of each metadata instance (such as glossary, glossary category, glossary term and data set) is strictly maintained.  Simply:

* If the instance was originally created in the open metadata ecosystem, it is owned by the open metadata ecosystem and any changes or deletions made to the copy in Apache Atlas will be reversed the next time the connector refreshes the Apache Atlas metadata.
* If the instance was originally created in Apache Atlas, it is owned by Apache Atlas.  When the instance is copied into the open metadata ecosystem, its [provenance](/features/metadata-provenance/overview) is set to indicate that this Apache Atlas server is its origin, which effectively makes it read-only in the open metadata ecosystem.

It is possible to create a new glossary term or glossary category in Apache Atlas within a glossary that originated from the open metadata ecosystem.  This new entity will be owned by Apache Atlas, even though it belongs to a glossary that is owned by the open metadata ecosystem.

Similarly, it is possible to create new glossary terms and categories in the open metadata ecosystem that are linked to a glossary that originated from Apache Atlas.  These new entities will be owned by the open metadata ecosystem.

### Correlation

In order to correlate the instances in Apache Atlas with the open metadata ecosystem instance, the connector:

* Adds two properties to the Apache Atlas glossary instances' *additionalAttributes* attribute:

    * *egeriaGUID* provides the unique identifier of the equivalent instance in the open metadata ecosystem.
    * *egeriaOwned* is a boolean flag describing whether the instance is owned by the open metadata ecosystem (true) or Apache Atlas (false).
  
    ??? example "Example of an Apache Atlas glossary category"
        This is an example of an Apache Atlas glossary category that has been copied from open metadata instance `805ba420-6fd5-446f-9d49-e9c7c97c4df4`.
        ```json
        {
            "guid": "50d104bd-af42-40a1-929d-4c4eeaae10d5",
            "qualifiedName": "Model Vocabulary: Cloud Information Model (CIM)@Cloud Information Model (CIM)",
            "name": "Model Vocabulary: Cloud Information Model (CIM)",
            "shortDescription": "The Cloud Information Model (CIM) is an open source glossary and data model that spans the following subject areas:\n\n•\tParty – people, their roles and organizations.\n•\tProduct – product descriptions, structures and packaging.\n•\tSales Order – customer orders for goods and services.\n•\tPayment Method – payment methods including cards, coupons and digital wallets.\n•\tPayment – individual payments for goods and services.\n•\tShipment – shipment of goods and services to the customer to fulfil an order.\n\nThis means it can provide common data structures for new services spanning customer and employee interaction around typical commercial activities such as buying and selling of goods and services.\n\nThe motivation behind the cloud information model is to support organizations who are transforming their digital services to run on a variety of cloud platforms and with their own data centres",
            "longDescription": "The Cloud Information Model (CIM) is an open source glossary and data model that spans the following subject areas:\n\n•\tParty – people, their roles and organizations.\n•\tProduct – product descriptions, structures and packaging.\n•\tSales Order – customer orders for goods and services.\n•\tPayment Method – payment methods including cards, coupons and digital wallets.\n•\tPayment – individual payments for goods and services.\n•\tShipment – shipment of goods and services to the customer to fulfil an order.\n\nThis means it can provide common data structures for new services spanning customer and employee interaction around typical commercial activities such as buying and selling of goods and services.\n\nThe motivation behind the cloud information model is to support organizations who are transforming their digital services to run on a variety of cloud platforms and with their own data centres.  Often, they are dealing with systems built on many different generations of technology, with data distributed amongst them.  The CIM provides a common language to describe the different types of data.\n\nThe CIM has been created to simplify the growing complexity companies experience when integrating data across different systemsin order to deliver highly intelligent and personalized customer engagements. It standardizes data interoperability by creating a set of guidelines to easily connect systems such as a point of sale system, email marketing platform, customer service center, customer relationship management (CRM) system and more. Developers will no longer need to spend months creating custom code in order to deliver innovative customer experiences. The CIM can be easily adopted and extended within days so that developers can focus on creating new innovations faster that deliver a truly connected, personalized and intelligent customer experience. \n",
            "additionalAttributes": {
                "egeriaGUID": "805ba420-6fd5-446f-9d49-e9c7c97c4df4",
                "egeriaOwned": "true"
            },
            "anchor": {
                "glossaryGuid": "991ea530-fba1-49cf-b58b-24439a3101ad",
                "relationGuid": "a0096490-5488-4daa-b23c-d675c56cc37b"
            }
        }
        ```

* Uses an [external identifier](/features/external-identifiers/overview) attached to the open metadata instance to hold the unique identifier (GUID) of the equivalent Apache Atlas metadata instance as well as using [metadata provenance](/features/metadata-provenance/overview) to identify the origin of instances being synchronized.  The external identifier is returned in the 

    * *correlationProperties* returns the external identifier.
    * *origin* of the *elementHeader* shows the metadata provenance.

    ??? example "Example of an open metadata glossary"
        This is an example of an open metadata glossary that has been copied from Apache Atlas's glossary with unique identifier `d36c7844-1dbc-4f15-bfd2-63a6125e9c4b`.
        ```json
        {
            "elementHeader": {
                "class": "ElementHeader",
                "headerVersion": 0,
                "status": "ACTIVE",
                "type": {
                "typeId": "36f66863-9726-4b41-97ee-714fd0dc6fe4",
                "typeName": "Glossary",
                "superTypeNames": [ "Referenceable", "OpenMetadataRoot"],
                "typeVersion": 1,
                "typeDescription": "A collection of related glossary terms."
                },
                "origin": {
                    "sourceServer": "cocoMDS1",
                    "originCategory": "EXTERNAL_SOURCE",
                    "homeMetadataCollectionId": "1cb8fa85-a1ba-480b-9d5e-5e7d3c562603",
                    "homeMetadataCollectionName": "ApacheAtlasDL01"
                },
                "versions": {
                    "createdBy": "generalnpa",
                    "createTime": "2023-07-19T17:09:36.767+00:00",
                    "version": 1
                },
                "guid": "e69cabed-5807-4467-a7e0-6a55acc15938",
                "classifications": [
                    {
                        "class": "ElementClassification",
                        "headerVersion": 0,
                        "status": "ACTIVE",
                        "type": {
                            "typeId": "adce83ac-10f1-4279-8a35-346976e94466",
                            "typeName": "LatestChange",
                            "typeVersion": 1,
                            "typeDescription": "Defines the latest change to an anchor entity and its associated attachments."
                        },
                        "origin": {
                            "sourceServer": "cocoMDS1",
                            "originCategory": "LOCAL_COHORT",
                            "homeMetadataCollectionId": "1cefccc2-082b-4c13-aafd-d1f0a67df3fc",
                            "homeMetadataCollectionName": "Data Lake Catalog"
                        },
                        "versions": {
                            "createdBy": "cocoMDS1npa",
                            "createTime": "2023-07-19T17:09:37.305+00:00",
                            "version": 1
                        },
                        "classificationOrigin": "ASSIGNED",
                        "classificationName": "LatestChange",
                        "classificationProperties": {
                            "relationshipType": "ExternalIdLink",
                            "attachmentType": "ExternalId",
                            "changeTarget": "EntityRelationship",
                            "description": "Linking Glossary e69cabed-5807-4467-a7e0-6a55acc15938 to ExternalId 565396f8-4300-4f30-b55b-a6c1f2a6070f",
                            "attachmentGUID": "565396f8-4300-4f30-b55b-a6c1f2a6070f",
                            "user": "generalnpa",
                            "changeAction": "Created"
                        }
                    }
                ]
            },
            "correlationHeaders": [
                {
                    "synchronizationDirection": "BOTH_DIRECTIONS",
                    "externalIdentifier": "d36c7844-1dbc-4f15-bfd2-63a6125e9c4b",
                    "externalIdentifierName": "atlasGUID",
                    "keyPattern": "LOCAL_KEY",
                    "assetManagerGUID": "1cb8fa85-a1ba-480b-9d5e-5e7d3c562603",
                    "assetManagerName": "ApacheAtlasDL01",
                    "lastSynchronized": "2023-07-19T17:09:37.045+00:00"
                }
            ],
            "glossaryProperties": {
                "class": "GlossaryProperties",
                "qualifiedName": "AtlasGlossary.Atlas Metadata Glossary",
                "displayName": "Atlas Metadata Glossary",
                "description": "This glossary has come from Apache Atlas.\n\nThis glossary is to replicated into the open metadata ecosystem by Egeria.",
                "language": "English",
                "usage": "Just for test"
            }
        }
        ```

## Configuration

The Apache Atlas integration connector runs in an [Integration Daemon](/concepts/integration-daemon).  There are two parts to the configuration:

* The specification of the connection object the controls the behaviour of the connector itself.
* The inclusion of the connection object in the configuration of the Integration Daemon.

### The connection object

The [connection](/concepts/connection) object provides information about configurations properties and the endpoint where Apache Atlas is running.  A connection object has the following structure:

![Connection structure](/concepts/connection.svg)

The *Connection* defines the specific use of the connector.  The *Connector Type* identifies the implementation of connector to run and the *Endpoint* identifies the host and port where the Apache Atlas server is running.

Apache Atlas typically runs with *Basic Authorization* - that is a userId and password is passed in the header of REST API calls to Apache Atlas.  This userId and password are specified as *userId* and *clearPassword* properties in the connection object.

??? tip "Using secrets for Apache Atlas's userId and password"
    If you are uncomfortable with specifying the userId and password for Apache Atlas in the clear it is possible to embed a connection for a [Secrets Store Connector](/concepts/secrets-store-connector) in the connection for the Apache Atlas integration connector.  The secrets store connector will dynamically retrieve the userId and password when the connector starts up.

Finally, there is an optional set of configuration properties that controls the behaviour of the Apache Atlas integration connector:

* *egeriaGlossaryQualifiedName* specifies the qualified name of a single Egeria glossary to publish to Apache Atlas.  If this property is omitted, all glossaries found in the open metadata ecosystem will be copied into Apache Atlas.
* *atlasGlossaryName* specifies the name of a single Apache Atlas glossary that is to be synchronized with the open metadata ecosystem.  If this property is omitted, all glossaries found in Apache Atlas will be copied into the open metadata ecosystem.

!!! example "Example connection for the Apache Atlas integration connector"
    ```json linenums="1" hl_lines="14 16-17 20-21"
    {
        "connection" : 
        { 
            "class" : "Connection",
            "qualifiedName" : "Egeria:IntegrationConnector:Catalog:Apache Atlas Connection",
            "connectorType" : 
            {
                "class" : "ConnectorType",
                "connectorProviderClassName" : "org.odpi.openmetadata.adapters.connectors.integration.apacheatlas.ApacheAtlasIntegrationProvider"
            },
            "endpoint" :
            {
                "class" : "Endpoint",
                "address" : "{{atlasServerURL}}"
            },
            "userId" : "{{atlasUserId}}",
            "clearPassword" : "{{atlasPassword}}",
            "configurationProperties" :
            {
                "egeriaGlossaryQualifiedName" : "{{glossaryQualifiedName}}",
                "atlasGlossaryName" : "{{glossaryName}}"
            }
        }
    }
    ```

    - Replace `{{atlasServerURL}}` with the URL of the Apache Atlas server.
    - Replace `{{atlasUserId}}` with the userId passed on each REST API call to the Apache Atlas server.
    - Replace `{{atlasPassword}}` with the password passed on each REST API call to the Apache Atlas server.
    - Replace `{{glossaryQualifiedName}}` with the qualified name of the Egeria glossary to publish to Apache Atlas.
    - Replace `{{glossaryName}}` this with the name of a single Apache Atlas glossary that is to be synchronized with the open metadata ecosystem.

### Adding the connection to Egeria's configuration

This connector runs in the [Integration Daemon](/concepts/integration-daemon).

Once you have the connection specified for the Apache Atlas integration connector, you have two choices on how to add it to Egeria's configuration:

* *Static configuration* by adding it directly to the [configuration document](/concepts/configuration-document) for the Integration Daemon.  This creates a static configuration that requires a restart of the Integration Daemon to change the configuration.
* *Dynamic configuration* by adding it to an open metadata [integration group](concepts/integration-group).  The integration group is stored in the open metadata repository of a [Metadata Access Store](/concepts/metadata-access-store). The associate Integration Daemon(s) immediately adapts what they are running as changes are made to the integration group contents.

Whichever method is used, there are four properties that will affect the behaviour of your connector:

* *metadataSourceQualifiedName* provides a unique name for your Apache Atlas server instance.  This value is used to identify the origin of the metadata that comes from your Apache Atlas server instance.  If you were running multiple Apache Atlas servers, each one should have its own *metadataSourceQualifiedName*.
* *refreshTimeInterval* defines the number of minutes between each scan the connector makes to find new metadata or changes to metadata.  The value to use depends on how often the metadata is likely to change.  It could, for instance be set to 1440 for the connector to run a refresh scan once a day.
* *usesBlockingCalls* must be set to *false*.
* *permittedSynchronization* defines which direction metadata is to flow. It may be:

    * *FROM_THIRD_PARTY* meaning that metadata only flows from Apache Atlas to the open metadata ecosystem.
    * *TO_THIRD_PARTY* meaning that metadata only flows from the open metadata ecosystem to Apache Atlas.
    * *BOTH_DIRECTIONS* meaning the metadata flows between the open metadata ecosystem and Apache Atlas in both directions.

??? education "Configuring the Integration Daemon"
    See [Configuring the integration connectors](/guides/admin/servers/by-section/integration-daemon-services-section) to find out how to add you connection object to the integration daemon.  For example, issuing the following command adds the Apache Atlas connection information to the Catalog Integrator OMIS in an Integration Daemon identified by `{integrationDaemonName}}`.  

    ```
    POST {{baseURL}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{integrationDaemonName}}/integration-services/catalog-integrator
    ```
    with request body:
    ```json
    {
        "class": "IntegrationServiceRequestBody",
        "omagserverPlatformRootURL": "http://54798.cocopharmaceuticals.org:9443",
        "omagserverName": "cocoMDS1",
        "integrationConnectorConfigs": [
            {
                "class": "IntegrationConnectorConfig",
                "connectorName": "AtlasIntegrator",
                "connectorUserId": "generalnpa",
                "connection": {
                    "class": "Connection",
                    "connectorType": {
                        "class": "ConnectorType",
                        "connectorProviderClassName": "org.odpi.openmetadata.adapters.connectors.integration.apacheatlas.ApacheAtlasIntegrationProvider"
                    },
                    "endpoint": {
                        "class": "Endpoint",
                        "address": "http://54798.cocopharmaceuticals.org:21000"
                    },
                    "userId" : "admin",
                    "clearPassword" : "admin"
                },
                "metadataSourceQualifiedName": "ApacheAtlasDL01",
                "refreshTimeInterval": "1440",
                "usesBlockingCalls": "false",
                "permittedSynchronization": "BOTH_DIRECTIONS"
            }
        ]
    }
    ```


## Implementation

The Apache Atlas integration connector makes use of the [Apache Atlas Glossary REST API](https://atlas.apache.org/api/v2/index.html) to query and update the metadata in Apache Atlas.  This REST API is divided into different groups of operations that each follow their own style. 

* *DiscoveryREST* provides the ability to search for entities, relationships and classifications.
* *EntityREST* supports the maintenance of entity instances.
* *GlossaryREST* supports both the querying and maintenance of glossaries, glossary categories and glossary terms.
* *LineageREST* provides for the capture and retrieval of lineage information for an entity.
* *RelationshipREST* supports the maintenance of relationship instances.
* *TypesREST* supports the definition and retrieval of type definitions.

This difference in style is why the Apache Atlas integration connector provides different capabilities for different types of metadata.  For example:

* Glossary terms can only be updated in their origin server because the Apache Atlas Glossary REST API does not record the version and update time to glossary element instances making it impossible to reconcile the order that updates have been made across the open metadata ecosystem and Apache Atlas.
* Entities/relationships do not have a standard place to store additional attributes, so it is not possible to store the corresponding unique identifier from the open metadata ecosystem.  The consequence is that entity and relationship metadata can only flow from Apache Atlas to the open metadata ecosystem.


---8<-- "snippets/abbr.md"
