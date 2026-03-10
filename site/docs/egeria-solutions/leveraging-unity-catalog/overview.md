---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Leveraging your Unity Catalog estate

--8<-- "snippets/work-in-progress.md"

[Unity Catalog](https://www.unitycatalog.io/) is a data manager catalog that governs access to data.  It is typically managing data from data lakes and lakehouses where much of the data is in a parquet format, with a table abstraction over the top.  Unity catalog also supports folders of files (called Volumes) and functions.  Unity catalog is able to provide access to the data in its catalogs, and run the functions.

Often an organization has multiple Unity Catalog servers, each co-located with a data platform.  These data platforms may have been deployed on premises and/or across various cloud platforms depending on the project dynamics and funding at the time of deployment.  As data accumulates on these platforms, its sheer size makes it difficult to move, and so these platforms have a long life and are rarely consolidated.

Egeria's *Leveraging your Unity Catalog estate* solution gives you oversight across all of your Unity Catalog servers.  This includes:

* Ongoing surveys to give you a view of the types of data and models you have, where they are deployed, and how this is changing over time.
* Selective metadata synchronization between Unity Catalog servers.
* Creation of a full inventory of all of your data and models managed by your Unity Catalog estate, irrespective of their deployment location.  This inventory can be searched, classified and used to drive governance of your Unity Catalog resources.
* Coordination of the deployment of definitions to multiple destinations including Unity Catalog servers.



## Unity Catalog in Action

The picture below shows Unity Catalog managing access to data in [Delta Lake](https://delta.io/).

![Unity Lake with Delta Lake](unity-catalog-purpose.svg)

Internally, unity catalog's metadata is organized into catalogs.  (So one way to think of Unity Catalog is as a 'catalog of catalogs'.)  Each catalog has multiple schemas and these contain the resources:

* Tables - these are virtual tables, typically backed by an Apache Parquet file.
* Functions - these are callable functions, typically implemented in SQL, but may be a callable external component.
* Volumes - these are collections of files.

As a result of this structure, the resources in Unity Catalog have a three level name: *catalogName.schemaName.resourceName*.

## Unity Catalog Technology Type Names

The technology type names (aka [deployed implementation types](/concepts/deployed-implementation-type)) added to Egeria's reference data for Unity Catalog are:

* *Unity Catalog Server* - The OSS Unity Catalog (UC) Server is an operational data platform 'catalog of catalogs' that supports controlled access to data managed through a related data platforms.
* *Unity Catalog Catalog* - An operational data platform catalog within the Unity Catalog (UC) 'catalog of catalogs'.
* *Unity Catalog Schema* - A schema that organizes data assets for an operational data platform catalog within the Unity Catalog (UC) 'catalog of catalogs'.
* *Unity Catalog Table* - A relational table within the Unity Catalog (UC) 'catalog of catalogs'.
* *Unity Catalog Function* - A function found in Unity Catalog (UC) that is working with data.
* *Unity Catalog Volume* - A collection of related data files within the Unity Catalog (UC) 'catalog of catalogs'.

??? example "JSON output from tech type search for 'Unity Catalog'"
```json
{
  "class": "TechnologyTypeSummaryListResponse",
  "relatedHTTPCode": 200,
  "elements": [
    {
      "technologyTypeGUID": "2d89345f-2650-4c04-bd5c-8cdbab7a0b79",
      "qualifiedName": "Egeria:ValidMetadataValue:SoftwareServer:deployedImplementationType-(Unity Catalog Server)",
      "name": "Unity Catalog Server",
      "description": "The OSS Unity Catalog (UC) Server is an operational data platform 'catalog of catalogs' that supports controlled access to data managed through a related data platforms.",
      "category": "SoftwareServer:deployedImplementationType"
    },
    {
      "technologyTypeGUID": "2b28dd27-3d4e-4c75-a3e8-cbbcbe8cb62f",
      "qualifiedName": "Egeria:ValidMetadataValue:Catalog:deployedImplementationType-(Unity Catalog Catalog)",
      "name": "Unity Catalog Catalog",
      "description": "An operational data platform catalog within the Unity Catalog (UC) 'catalog of catalogs'.",
      "category": "Catalog:deployedImplementationType"
    },
    {
      "technologyTypeGUID": "c56ca4d1-ed5a-4b05-b75b-e4b6bd3500ff",
      "qualifiedName": "Egeria:ValidMetadataValue:DeployedDatabaseSchema:deployedImplementationType-(Unity Catalog Schema)",
      "name": "Unity Catalog Schema",
      "description": "A schema that organizes data assets for an operational data platform catalog within the Unity Catalog (UC) 'catalog of catalogs'.",
      "category": "DeployedDatabaseSchema:deployedImplementationType"
    },
    {
      "technologyTypeGUID": "3a1ad610-f5c5-4aba-a766-63965ac528be",
      "qualifiedName": "Egeria:ValidMetadataValue:VirtualRelationalTable:deployedImplementationType-(Unity Catalog Table)",
      "name": "Unity Catalog Table",
      "description": "A relational table within the Unity Catalog (UC) 'catalog of catalogs'.",
      "category": "VirtualRelationalTable:deployedImplementationType"
    },
    {
      "technologyTypeGUID": "7f15dd5f-7569-4697-a3f1-491e399f4351",
      "qualifiedName": "Egeria:ValidMetadataValue:DeployedAPI:deployedImplementationType-(Unity Catalog Function)",
      "name": "Unity Catalog Function",
      "description": "A function found in Unity Catalog (UC) that is working with data.",
      "category": "DeployedAPI:deployedImplementationType"
    },
    {
      "technologyTypeGUID": "dbabe8cb-345e-4665-a665-1bef56a26ecd",
      "qualifiedName": "Egeria:ValidMetadataValue:DataFolder:deployedImplementationType-(Unity Catalog Volume)",
      "name": "Unity Catalog Volume",
      "description": "A collection of related data files within the Unity Catalog (UC) 'catalog of catalogs'.",
      "category": "DataFolder:deployedImplementationType"
    }
  ]
}
```

## Open Metadata Type Mapping for Unity Catalog

The mapping from Unity Catalog metadata elements to the Open Metadata Types used in the Open Metadata Ecosystem is as follows:

| Technology Type        | Open Metadata Type                                                                                                                                   |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Unity Catalog Server   | [SoftwareServer](/types/0/0040-Software-Servers)                                                                                                     |
| Unity Catalog Catalog  | [Catalog](/types/0/0050-Applications-and-Processes)                                                                                                  |
| Unity Catalog Schema   | [DeployedDatabaseSchema](/types/2/0224-Databases)                                                                                                    |
| Unity Catalog Function | [DeployedAPI](/types/2/0212-Deployed-APIs) with an associated [DeployedSoftwareComponent](/types/2/0215-Software-Components) for its implementation. |
| Unity Catalog Table    | [VirtualRelationalTable](/types/2/0235-Information-View) with an associated [DataFolder](/types/2/0220-Files-and-Folders) for its files.             |
| Unity Catalog Volume   | [DataFolder](/types/2/0220-Files-and-Folders)                                                                                                        |

In addition, each of these elements have a [PropertyFacet](/types/0/0020-Property-Facets) and an [External Identifier](/types/0/0017-External-Identifiers) attached.  The property facet contains implementation specific details; the external identifier includes the guid from unity catalog plus other mapping values such as the catalog name, schema name and short name to enable the Unity Catalog connectors to ensure that the name of a element has not changed since the last time a Unity Catalog element was retrieved.

The diagram below illustrates the mapping of the Unity Catalog metadata resource to the Open Metadata Types.

![Type Mapping](unity-catalog-type-mapping.svg)

Below is the field mapping from Unity Catalog to these Open Metadata Types:

=== "Catalogs"

    --8<-- "snippets/unity-catalog/catalog-mapping.md"

=== "Schemas"

    --8<-- "snippets/unity-catalog/schema-mapping.md"

=== "Volumes"

    --8<-- "snippets/unity-catalog/volume-mapping.md"

=== "Tables"

    --8<-- "snippets/unity-catalog/table-mapping.md"

=== "Functions"

    --8<-- "snippets/unity-catalog/function-mapping.md"


The templates that implement this mapping are described in [Unity Catalog Templates](/catalog-templates/unity-catalog-templates).

### Anchor design for Unity Catalog

In order to have correct delete semantics, each of the unity catalog resources is its own [anchored structure](/concepts/anchor).  In addition, each resource is anchored to its parent.  So each table, function and volume is anchored to its schema and each schema is anchored to its catalog.  The catalogs are anchored to their appropriate server.

The result is, if for example, a catalog is deleted, all the schemas, tables, functions and volumes nested underneath it are deleted too - ensuring there are no orphaned fragments of metadata left in the repository.

### Metadata Collections

Each catalog in a Unity Catalog server is assigned its own metadata collection.  The schemas, tables, functions and volumes within the catalog are all part of the catalog's metadata collection making it easy to identify the origin of these metadata elements.

![Metadata Collections for Unity Catalog Resources](unity-catalog-metadata-collections.svg)

The unity connectors also use the metadata collections to scope the metadata they are processing.


## Connectors to Unity Catalog

The [Unity Catalog connectors](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/data-manager-connectors/unity-catalog-connectors) provide a suite of functions that integrate a Unity Catalog server into the open metadata ecosystem.

![Unity Catalog Connectors](unity-catalog-connectors.svg)

| Connector Name                                | Connector Type                                                     | Purpose                                                                                                                                                               |
|-----------------------------------------------|--------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Unity Catalog Resource Connector**          | [Digital Resource Connector](/concepts/digital-resource-connector) | Provides wrapper around Unity Catalog's REST API.                                                                                                                     |
| **Unity Catalog Server Survey**               | [Survey Action Service](/concepts/survey-action-service)           | Surveys the contents of a Unity Catalog Server.                                                                                                                       |
| **Unity Catalog Catalog Survey**              | [Survey Action Service](/concepts/survey-action-service)           | Surveys the contents of a Unity Catalog Catalog.                                                                                                                      |
| **Unity Catalog Schema Survey**               | [Survey Action Service](/concepts/survey-action-service)           | Surveys the contents of a Unity Catalog Schema.                                                                                                                       |
| **Unity Catalog Server Synchronizer**         | [Integration Connector](/concepts/integration-connector)           | Bootstraps the cataloguing of a Unity Catalog Server by retrieving the catalogs and configuring the Inside Catalog Connector (below).                                 |
| **Unity Catalog Inside Catalog Synchronizer** | [Integration Connector](/concepts/integration-connector)           | Synchronizes the metadata describing a Unity Catalog Server's catalogs, schemas, tables, functions and volumes between Unity Catalog and the Open Metadata Ecosystem. |



--8<-- "snippets/abbr.md"