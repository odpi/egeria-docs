<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0017 External Identifiers

External identifiers are used to correlate the identifiers used in third party systems with open metadata elements.  

![UML](0017-External-Identifiers.svg)

## ExternalId entity

The *ExternalId* entity describes an external identifier from a specific third party system. It includes:

* *identifier* - the unique identifier of the element in the third party metadata repository.
* *keyPattern* - The pattern used for the identifier (how it is generated and managed) is stored in the *KeyPattern* enumeration. 
* *externalInstanceTypeName* - the type name the instance in the external system.
* *externalInstanceCreatedBy* - the username of the person or process that created the instance in the external system.
* *externalInstanceCreationTime* - the date/time when the instance in the external system was created.
* *externalInstanceLastUpdatedBy* - the username of the person or process that last updated the instance in the external system.
* *externalInstanceLastUpdateTime* - the date/time that the instance in the external system was last updated.
* *externalInstanceVersion* - the latest version of the element in the external system.

## KeyPattern enumeration

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


## ExternalIdLink relationship

The mapping of identifiers can be many-to-many, which is why you see that the *ExternalIdLink* relationship between the [*OpenMetadataRoot*](/types/0/0010-Base-Model/#openmetadataroot) (open metadata resources) and the *ExternalId* entity is also many-to-many.

This relationship includes properties to help to map the *OpenMetadataRoot* entity to the external identifier.

## ExternalIdScope relationship

There is no guarantee that external identifiers from a third party metadata catalog are globally unique and so the *ExternalIdScope* relationship links the external identifier to the [Referenceable](/types/0/0010-Base-Model/#referenceable) that represents the third party system. Typically, this is a type of [SoftwareCapability](/types/0/0042-Software-Capabilities/#softwarecapability), for example, [AssetManager](/types/0/0056-Resource-Managers/#assetmanager).

## PermittedSynchronization enumeration

*PermittedSynchronization* defines the direction of flow of metadata.

| Enumeration      | Value | Name             | Description                                                                                                                                                                                                                                                                                 |
|------------------|-------|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BOTH_DIRECTIONS  | 0     | "Both Directions" | Metadata exchange is permitted in both directions.  Synchronization is halted on a specific element if potentially clashing updates have occurred both in the third party technology and open metadata.  Such conflicts are logged on the audit log and resolved through manual stewardship. |
| TO_THIRD_PARTY   | 1     | "To Third Party" | The third party technology is logically downstream of open metadata.  This means the open metadata ecosystem is the originator and owner of the metadata being synchronized. Any updates detected in the third technology are overridden by the latest open metadata values.                |
| FROM_THIRD_PARTY | 2     | "From Third Party" | The third party technology is logically upstream (the originator and owner of the metadata).  Any updates made in open metadata are not passed to the third party technology and the third party technology is requested to refresh the open metadata version.                              |
| OTHER            | 99    | "Other"          | Another type of synchronization rule - see description property.                                                                                                                                                                                                                            |

## Example

The picture below shows the value of the external identifiers in providing traceability between metadata elements in different systems.  

Starting on the left-hand side of the diagram is a [SoftwareCapability](/types/0/0042-Software-Capabilies) entity representing an Apache Atlas server.  

Following the *ExternalIdScope* relationships takes you to the identifiers of all the Apache Atlas entities that have been synchronized into the open metadata ecosystem.  

From one of the *ExternalId* entities it is possible to navigate to the open metadata entity/entities that store the equivalent metadata by following the *ExternalIdLink* relationships.  

An open metadata ecosystem entity may have been synchronized with multiple third party systems.  Following all the *ExternalIdLink* relationships from such an open metadata entity creates a list of external identifiers for each of the third party systems it has been synchronized with.  In this example, the glossary term has been synchronized with Apache Atlas and DataHub servers.  The *lastSynchronized* property in the *externalIdLink* documents when Egeria last checked for updates from the associated third party system.  The other properties in the *ExternalId* entity provide more detail about the element in the third party system.

![Example](external-identifier-example.svg)



??? education "Further information"
    There is an article on [managing external identifiers](/features/external-identifiers/overview) to correlate metadata elements from different types of technologies.

--8<-- "snippets/abbr.md"
