---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/tech-preview.md"

# Files Integrator Open Metadata Integration Service (OMIS)

The Files Integrator OMIS supports the collection of information about files
stored in a filesystem for and then storing it in the open metadata ecosystem.

It supports a type of [integration connector](/concepts/integration-connector)
that are able to create [DataFile](/types/2/0220-Files-and-Folders)
and [FileFolder](/types/2/0220-Files-and-Folders) assets of various types
along with descriptions of the structures of the data that they store.

Optionally, this metadata can be tied to an [FileSystem](/types/2/0220-Files-and-Folders)
or a [FileSystem](/types/2/0220-Files-and-Folders).

## CSV Files

Figure 1 shows the types of metadata for CSV files that integrators connectors can create with this integration service.

![Figure 1](/services/omas/data-manager/csv-file-model.svg)
> **Figure 1:** CSV File metadata supported by the Files Integrator OMIS 

The structure of a CSV file is made up of [TabularColumn](/types/5/0530-Tabular-Schemas)s.

Figure 2 shows the open metadata types used to represent the CSV File metadata created through this service.

![Figure 2](/services/omas/data-manager/csv-file-open-metadata-types.svg)
> **Figure 2:** CSV file open metadata types supported by the Files Integrator OMIS 

If a FileSystem or FileManager is defined, any CSVFile asset created is automatically linked to it using the
[ServerAssetUse](/types/0/0045-Servers-and-Assets)
relationship.
When a TabularColumn is created for the file,
the service automatically inserts the
[AssetSchemaType](/types/5/0503-Asset-Schema) relationship,
[TabularSchemaType](/types/5/0530-Tabular-Schemas) entity and
[AttributeForSchema](/types/5/0505-Schema-Attributes) relationship
in between the file and the TabularColumn.

The tabular columns use
the [TypeEmbeddedAttribute](/types/5/0505-Schema-Attributes)
classification [method for defining the schema type](/guides/developer/mapping-technology/modelling-schemas).


## Avro Files

Figure 1 shows the types of metadata for CSV files that integrators connectors can create with this integration service.

![Figure 1](/services/omas/data-manager/avro-file-model.svg)
> **Figure 1:** Avro File metadata supported by the Files Integrator OMIS 

The structure of an Avro file is made up of nested [ObjectAttribute](/types/5/0532-Object-Schemas)s.

Figure 2 shows the open metadata types used to represent the Avro File metadata created through this service.

![Figure 2](/services/omas/data-manager/avro-file-open-metadata-types.svg)
> **Figure 2:** Avro file open metadata types supported by the Files Integrator OMIS 

If a FileSystem or FileManager is defined, any AvroFile asset created is automatically linked to it using the
[ServerAssetUse](/types/0/0045-Servers-and-Assets)
relationship.
When an ObjectAttribute is created for the file,
the service automatically inserts the
[AssetSchemaType](/types/5/0503-Asset-Schema) relationship,
[ObjectSchemaType](/types/5/0532-Object-Schemas) entity and
[AttributeForSchema](/types/5/0505-Schema-Attributes) relationship
in between the file and the ObjectAttribute.

Any object attributes created through this interface will use the
[ObjectAttribute](/types/5/0532-Object-Schemas) subtype
to allow for find requests that only return schema information for object type schemas.  The schema attributes also use
the [TypeEmbeddedAttribute](/types/5/0505-Schema-Attributes)
classification [method for defining the schema type](/guides/developer/mapping-technology/modelling-schemas).

## JSON Files

Figure 1 shows the types of metadata for JSON files that integrators connectors can create with this integration service.

![Figure 1](/services/omas/data-manager/json-file-model.svg)
> **Figure 1:** JSON File metadata supported by the Files Integrator OMIS 

The structure of an JSON file is made up of nested [DocumentSchemaAttribute](/types/5/0531-Document-Schemas)s.

Figure 2 shows the open metadata types used to represent the JSON File metadata created through this service.

![Figure 2](/services/omas/data-manager/json-file-open-metadata-types.svg)
> **Figure 2:** JSON file open metadata types supported by the Files Integrator OMIS 

If a FileSystem or FileManager is defined, any JSONFile asset created is automatically linked to it using the
[ServerAssetUse](/types/0/0045-Servers-and-Assets)
relationship.
When a DocumentSchemaAttribute is created for the file,
the service automatically inserts the
[AssetSchemaType](/types/5/0503-Asset-Schema) relationship,
[DocumentSchemaType](/types/5/0531-Document-Schemas) entity and
[AttributeForSchema](/types/5/0505-Schema-Attributes) relationship
in between the file and the ObjectAttribute.

Any object attributes created through this interface will use the
[DocumentSchemaAttribute](/types/5/0532-Object-Schemas) subtype
to allow for find requests that only return schema information for object type schemas.  The schema attributes also use
the [TypeEmbeddedAttribute](/types/5/0505-Schema-Attributes)
classification [method for defining the schema type](/guides/developer/mapping-technology/modelling-schemas).


## Module Implementation

The modules are as follows:

* *files-integrator-api* - defines the interface for an integration
connector that is supported by the Files Integrator OMIS.  This includes the implementation
of the context that wraps the Data Manager OMAS's clients.

* *files-integrator-server* - implements the context manager for
the Files Integrator OMIS.

* *files-integrator-spring* - implements a rest API for validating that a specific
integration connector is able to run under this service.

* *files-integrator-client* - implements a Java client for the REST API.



This integration service is paired with the [Data Manager](/services/omas/data-manager/overview)
Open Metadata Access Service (OMAS).

--8<-- "snippets/abbr.md"