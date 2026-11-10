---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


# Files Metadata

Files are modeled using subtypes of the [DataFile](/types/2/0220-Files-and-Folders)
and [FileFolder](/types/2/0220-Files-and-Folders) assets
along with descriptions of the structures of the data that they store.

Optionally, this metadata can be tied to a [FileSystem](/types/0/0056-Resource-Managers)
or a [FileManager](/types/0/0056-Resource-Managers) software capability.

## CSV Files

Figure 1 shows the types of metadata for CSV files that integration connectors can create.

![Figure 1](csv-file-model.svg)
> **Figure 1:** CSV File metadata

The structure of a CSV file is made up of [TabularColumn](/types/5/0530-Tabular-Schemas)s.

Figure 2 shows the open metadata types used to represent the CSV File metadata.

![Figure 2](csv-file-open-metadata-types.svg)
> **Figure 2:** CSV file open metadata types

If the FileSystem or FileManager is catalogued, link each CSVFile asset to it using the
[CapabilityAssetUse](/types/0/0045-Servers-and-Assets)
relationship.
Between the file and its TabularColumns sit the
[Schema](/types/5/0503-Asset-Schema) relationship,
[TabularSchemaType](/types/5/0530-Tabular-Schemas) entity and
[AttributeForSchema](/types/5/0505-Schema-Attributes) relationship.

The tabular columns use
the [TypeEmbeddedAttribute](/types/5/0505-Schema-Attributes)
classification [method for defining the schema type](/concepts/schema).


## Avro Files

Figure 1 shows the types of metadata for Avro files that integration connectors can create.

![Figure 1](avro-file-model.svg)
> **Figure 1:** Avro File metadata

The structure of an Avro file is made up of nested [ObjectAttribute](/types/5/0532-Object-Schemas)s.

Figure 2 shows the open metadata types used to represent the Avro File metadata.

![Figure 2](avro-file-open-metadata-types.svg)
> **Figure 2:** Avro file open metadata types

If the FileSystem or FileManager is catalogued, link each AvroFile asset to it using the
[CapabilityAssetUse](/types/0/0045-Servers-and-Assets)
relationship.
Between the file and its ObjectAttributes sit the
[Schema](/types/5/0503-Asset-Schema) relationship,
[ObjectSchemaType](/types/5/0532-Object-Schemas) entity and
[AttributeForSchema](/types/5/0505-Schema-Attributes) relationship.

The object attributes use the
[ObjectAttribute](/types/5/0532-Object-Schemas) subtype
to allow for find requests that only return schema information for object type schemas.  The schema attributes also use
the [TypeEmbeddedAttribute](/types/5/0505-Schema-Attributes)
classification [method for defining the schema type](/concepts/schema).

## JSON Files

Figure 1 shows the types of metadata for JSON files that integration connectors can create.

![Figure 1](json-file-model.svg)
> **Figure 1:** JSON File metadata supported by the file classifier from the integration context

The structure of a JSON file is made up of nested [DocumentSchemaAttribute](/types/5/0531-Document-Schemas)s.

Figure 2 shows the open metadata types used to represent the JSON File metadata.

![Figure 2](json-file-open-metadata-types.svg)
> **Figure 2:** JSON file open metadata types supported by the file classifier from the integration context

If the FileSystem or FileManager is catalogued, link each JSONFile asset to it using the
[CapabilityAssetUse](/types/0/0045-Servers-and-Assets)
relationship.
Between the file and its DocumentSchemaAttributes sit the
[Schema](/types/5/0503-Asset-Schema) relationship,
[DocumentSchemaType](/types/5/0531-Document-Schemas) entity and
[AttributeForSchema](/types/5/0505-Schema-Attributes) relationship.

The schema attributes use the
[DocumentSchemaAttribute](/types/5/0531-Document-Schemas) subtype
to allow for find requests that only return schema information for document schemas.  The schema attributes also use
the [TypeEmbeddedAttribute](/types/5/0505-Schema-Attributes)
classification [method for defining the schema type](/concepts/schema).


--8<-- "snippets/abbr.md"