<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

--8<-- "snippets/content-status/in-development.md"

# Asset Manager Open Metadata Access Service (OMAS)

The Asset Manager OMAS provides APIs for supporting the exchange of metadata with a third party asset manager.  An [asset manager](/concepts/software-capability) is typically a catalog of [assets](/concepts/asset).  It is responsible for maintaining details of the assets including their characteristics, ownership, assessments and governance requirements.

The Asset Manager OMAS (in conjunction with the [Catalog Integrator OMIS](/services/omis/catalog-integrator/overview)) provides a new integration path for metadata catalogs the goes via an integration service hosted in an [integration daemon](/concepts/integration-daemon).

Catalogs will be able to have a two-way integration through this path without needing to conform to the repository service rules for managing home and reference copies. This is possible for two reasons:

* Since the metadata from the catalog passes through an OMAS, Egeria will be able to have a better control of the metadata from the catalog.
* Since the catalog is not part of a federated query, any inconsistent updates to metadata that occurs in its repository, only impacts the users of that catalog and not the whole cohort.

## Identifying your asset manager

The Asset Manager OMAS provides an API for managing an element that represents your asset manager.  This element can then be linked to the assets and their properties contributed from your asset manager to show where the metadata came from and the scope of any identifiers that are mapped to 

## External Identifiers

A major challenge when exchanging metadata with third party asset managers is that there is often a mismatch between the structure of the metadata in a third party asset manager and the structure of the[open metadata types](/types)used by the Asset Manager OMAS.

For this reason, the Asset Manager OMAS supports the ability to [associate multiple external identifiers with an open metadata instance](/features/external-identifiers/overview).  These external identifiers are scoped to a particular third party asset manager so that there is no confusion if two third party asset managers happen to use the same unique identifier within their repositories. Each of these external identifiers can be mapped to the appropriate open metadata instances without confusion.


There are also API calls for querying open metadata instances using external identifiers and the identifier of the third party asset manager.




## KeyPattern

*KeyPattern* describes the pattern used for the identifier (how it is generated and managed). These are the values it can take, with the default (and most used) being `LOCAL_KEY`:

| Enumeration   | Value | Name             | Description                                                                                                   |
|---------------|-------|------------------|---------------------------------------------------------------------------------------------------------------|
| LOCAL_KEY     | 0     | "Local Key"      | Unique key allocated and used within the scope of a single system.                                            |
| RECYCLED_KEY  | 1     | "Recycled Key"   | Key allocated and used within the scope of a single system that is periodically reused for different records. |
| NATURAL_KEY   | 2     | "Natural Key"    | Key derived from an attribute of the entity, such as email address, passport number.                          |
| MIRROR_KEY    | 3     | "Mirror Key"     | Key value copied from another system.                                                                         |
| AGGREGATE_KEY | 4     | "Aggregate Key"  | Key formed by combining keys from multiple systems.                                                           |
| CALLERS_KEY   | 5     | "Caller's Key"   | Key from another system can bey used if system name provided.                                                 |
| STABLE_KEY    | 6     | "Stable Key"     | Key value will remain active even if records are merged.                                                      |
| OTHER         | 99    | "Other"          | Another key pattern.                                                                                          |


## PermittedSynchronization

*PermittedSynchronization* defines the direction of flow of metadata.

| Enumeration      | Value | Name             | Description                                                                                                                                                                                                                                                                                 |
|------------------|-------|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BOTH_DIRECTIONS  | 0     | "Both Directions" | Metadata exchange is permitted in both directions.  Synchronization is halted on a specific element if potentially clashing updates have occurred both in the third party technology and open metadata.  Such conflicts are logged on the audit log and resolved through manual stewardship. |
| TO_THIRD_PARTY   | 1     | "To Third Party" | The third party technology is logically downstream of open metadata.  This means the open metadata ecosystem is the originator and owner of the metadata being synchronized. Any updates detected in the third technology are overridden by the latest open metadata values.                |
| FROM_THIRD_PARTY | 2     | "From Third Party" | The third party technology is logically upstream (the originator and owner of the metadata).  Any updates made in open metadata are not passed to the third party technology and the third party technology is requested to refresh the open metadata version.                              |
| OTHER            | 99    | "Other"          | Another type of synchronization rule - see description property.                                                                                                                                                                                                                            |


## DataItemSortOrder

*DataItemSortOrder* provides the valid values for the *sortOrder* property of SchemaAttribute.  It indicates whether the rows/instances of the data stored in this schema appear in any particular order or not.

| Enumeration | Value | Name           | Description                                                                       |
|-------------|-------|----------------|--------------------------------------------------------------------------------------------------|
| UNKNOWN     | 0     | "<Unknown>"    | "The sort order is not specified. |
| ASCENDING   | 1     | "Ascending"    | "The attribute instances are organized so that the smallest/lowest value is first and the rest of the instances follow in ascending order. |
| DESCENDING  | 2     | "Descending"   | The attribute instances are organized so that the largest/highest value is first and the rest of the instances follow in descending order. |
| UNSORTED    | 3     | "Unsorted"     | "The instances of the schema attribute may appear in any order. |                                                                            


## Supplementary Properties

It is common for external asset managers to include extensive descriptive properties for assets
that include both a technical name and description as well as a business name and description.
The Asset Manager OMAS supports this distinction and stores the technical name and
description in an Asset metadata instance and the business name and description in a glossary term
metadata instance that is linked to the asset using a
[**MoreInformation** relationship](/types/0/0019-More-Information).
The properties that are stored in the glossary term are referred to as supplementary properties.

--8<-- "snippets/abbr.md"
