<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/tech-preview.md"

# Asset Lineage Open Metadata Access Service (OMAS)

## Overview 

Asset Lineage is metadata access service (OMAS) that consolidates and exports lineage metadata for [assets](/concepts/asset){ target=_blank } in a cohort. This is achieved by actively watching the cohort and discovering specific asset types and relationships to other assets or metadata elements. 

Following asset types are considered:

- DataStore (subtypes)
- Process
- DataSet


Asset Lineage OMAS then builds complex graph structures (sometimes we call this asset context) that are sent to an [out topic](/concepts/out-topic){ target=_blank } address for further preservation and use with [Open Lineage Server :material-dock-window:](/services/open-lineage-services){ target=_blank }. 

The above works well for scenario where metadata is actively shared on the cohort while it gets created. In different scenario, additional repository already prepopulated with existing metadata can join the cohort. Asset Lineage OMAS offers endpoint to handle this as well by allowing external system to request (or actively poll) and extract the metadata relevant for building lineage graph.

In all cases, Asset Lineage OMAS always relies on underlying [Enterprise Repository Services :material-dock-window:](/services/omrs/subsystem-descriptions/enterprise-repository-services){ target=_blank } OMRS subsystem to find and consolidate metadata by combining different elements available across the cohort.


<!-- ### Metadata model -->
<!-- //TODO: Add metadata model describing input structures for lineage -->

## User Guide

Most of the interaction with the Asset Lineage OMAS will be driven by the external tools used to build lineage using [Data Engine OMAS :material-dock-window:](/services/omas/data-engine/overview) and [Data Engine Proxy :material-dock-window:](/services/data-engine-proxy-services) or integrated lineage via [Integration Services OMIS :material-dock-window:](/services/omis/) like Database integrator or Files integrator. 

When enabled in a OMAG Metadata Access Server, it subscribes to the enterprise cohort topic and uses following events triggers:

Relationship events that build lineage graph:

- Lineage Mappings between Assets 
- Lineage Mappings between Schema Elements
- Semantic Assignments between Glossary Terms and Schema Elements

Entity events to feed the changes assets that are crated or updated:

- Data Stores 
- Processes

## Interface choices

- [Java client :material-dock-window:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/access-services/asset-lineage/asset-lineage-client/docs/user/java-client){ target=gh } to integrate within Java programs,
- [REST API](#rest-api) to interact with external/remote systems,
- [Out Topic Events](#out-topic-events) to publish lineage related events.


### Out Topic Events

??? example "LineageEntityEvent"

    ```json
    {
        "class": "LineageEntityEvent",
        "eventVersionId": 1,
        "assetLineageEventType": "UPDATE_ENTITY_EVENT",
        "lineageEntity": {
            "guid": "a8f71cfc-bd59-440e-afb9-9719d60a8fe3",
            "typeDefName": "Process",
            "createdBy": "cocoETLnpa",
            "updatedBy": "cocoETLnpa",
            "createTime": 1636326254855,
            "updateTime": 1636326255079,
            "version": 2,
            "metadataCollectionId": "9beaa80a-50d9-44ba-b2ae-18f2379c9aa4",
            "properties": {
                "displayName": "ConvertFileToCSV",
                "qualifiedName": "ConvertFileToCSV@CocoPharma/DataEngine/CocoETL",
                "description": "Process named 'ConvertFileToCSV' representing high level processing activity performed by CocoETL tool."
            }
        }
    }
    ```
??? example "LineageRelationshipEvent"

    ```json
    {
        "class": "LineageRelationshipEvent",
        "eventVersionId": 1,
        "assetLineageEventType": "NEW_RELATIONSHIP_EVENT",
        "lineageRelationship": {
            "guid": "aa2b43c5-eb9a-49bf-93fd-aeddf55812f3",
            "typeDefName": "LineageMapping",
            "createdBy": "cocoETLnpa",
            "updatedBy": null,
            "createTime": 1636326312659,
            "updateTime": null,
            "version": 1,
            "metadataCollectionId": "9beaa80a-50d9-44ba-b2ae-18f2379c9aa4",
            "properties": {},
            "sourceEntity": {
                "guid": "b117f8a5-deaf-47d1-80fe-15425b5b7f1f",
                "typeDefName": "DataFile",
                "createdBy": "cocoETLnpa",
                "updatedBy": null,
                "createTime": 1636326233314,
                "updateTime": null,
                "version": 1,
                "metadataCollectionId": null,
                "properties": {
                    "qualifiedName": "file://secured/research/previous-clinical-trials/old-archive.dat@CocoPharma/DataEngine/CocoETL"
                }
            },
            "targetEntity": {
                "guid": "a8f71cfc-bd59-440e-afb9-9719d60a8fe3",
                "typeDefName": "Process",
                "createdBy": "cocoETLnpa",
                "updatedBy": "cocoETLnpa",
                "createTime": 1636326254855,
                "updateTime": 1636326255079,
                "version": 2,
                "metadataCollectionId": null,
                "properties": {
                    "qualifiedName": "ConvertFileToCSV@CocoPharma/DataEngine/CocoETL"
                }
            }
        }
    }
    ```
## REST API

### Publish Entity
Find the entity by guid and publish the context for it
!!! get "GET - Request lineage publish out for single entity (asset or term)"

    ```
    {{platformURLRoot}}/servers/{{serverName}}/open-metadata/access-services/asset-lineage/users/{{userId}}/publish-entity/{{entityTypeName}}/{{guid}}
    ```
### Publish Entities
Scan the cohort based on the given entity type and publish the contexts for the found entities to the out topic.
!!! get "GET - Request lineage publish out for entity type (asset or term)"

    ```
    {{platformURLRoot}}/servers/{{serverName}}/open-metadata/access-services/asset-lineage/users/{{userId}}/publish-entities/{{entityTypeName}}
    ```
### Publish Context
Find the entity by guid and publish the asset context for it. It applies for data tables and files.
!!! get "GET - Request asset context"

    ```
    {{platformURLRoot}}/servers/{{serverName}}/open-metadata/access-services/asset-lineage/users/{{userId}}/publish-context/{{entityTypeName}}/{{guid}}
    ```
### Out Topic Connection
Return the connection object for the Asset Lineage's OMAS's out topic.
!!! get "GET - Output topic OCF connection"
    ```
    {{platformURLRoot}}/servers/{{serverName}}/open-metadata/access-services/asset-lineage/users/{{userId}}/topics/out-topic-connection/{callerId}
    ```
## Configuration

!!! post "POST - Enable Asset Lineage OMAS with accessServiceOptions"

    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/access-services/asset-lineage
    ```
    With a request body like the following:

    ```json
    {
        "LineagePublisherBatchSize": 100,
        "LineageClassificationTypes": [
            "PrimaryCategory",
            "Confidentiality",
            "AssetZoneMembership",
            "SubjectArea",
            "AssetOwnership"
        ]
    }
    ```
Detailed description of the properties

| Property | Description |
|---|---|
| LineagePublisherBatchSize | Number of elements to be sent in a single event. This parameter is used to optimize event payload size and allow multiple elements to be grouped in a batch. Default is 1. |
| LineageClassificationTypes | List of classification types considered while producing lineage events. The access service is always preconfigured with the default set listed in the example request body. Additional types can be added when necessary, they are always merged with the default set. |

--8<-- "snippets/abbr.md"
