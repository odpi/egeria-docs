<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0017 External Identifiers

External identifiers are used to correlate the identifiers used in third party metadata catalogs with open metadata elements.

![UML](0017-External-Identifiers.svg)

## ExternalId

The *`ExternalId`* entity describes an external identifier from a specific third party metadata repository. It includes:

- The identifier value itself in `identifier`.
- The pattern used for the identifier (how it is generated and managed) is stored in `keyPattern`. 

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


## ExternalIdLink

The mapping of identifiers can be many-to-many, which is why you see that the *`ExternalIdLink`* relationship between the [`OpenMetadataRoot`](/types/0/0010-Base-Model/#openmetadataroot) (open metadata resources) and the `ExternalId` is also many-to-many.

This relationship includes properties to help to map the `OpenMetadataRoot` to the external identifier.

## ExternalIdScope

There is no guarantee that external identifiers from a third party metadata catalog are globally unique and so the *`ExternalIdScope`* relationship links the external identifier to the [`Referenceable`](/types/0/0010-Base-Model/#referenceable) that represents the third party metadata catalog. Typically, this is a type of [`SoftwareCapability`](/types/0/0042-Software-Capabilities/#softwarecapability), for example, [`AssetManager`](/types/0/0056-Resource-Managers/#assetmanager).

## PermittedSynchronization

*PermittedSynchronization* defines the direction of flow of metadata.

| Enumeration      | Value | Name             | Description                                                                                                                                                                                                                                                                                 |
|------------------|-------|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BOTH_DIRECTIONS  | 0     | "Both Directions" | Metadata exchange is permitted in both directions.  Synchronization is halted on a specific element if potentially clashing updates have occurred both in the third party technology and open metadata.  Such conflicts are logged on the audit log and resolved through manual stewardship. |
| TO_THIRD_PARTY   | 1     | "To Third Party" | The third party technology is logically downstream of open metadata.  This means the open metadata ecosystem is the originator and owner of the metadata being synchronized. Any updates detected in the third technology are overridden by the latest open metadata values.                |
| FROM_THIRD_PARTY | 2     | "From Third Party" | The third party technology is logically upstream (the originator and owner of the metadata).  Any updates made in open metadata are not passed to the third party technology and the third party technology is requested to refresh the open metadata version.                              |
| OTHER            | 99    | "Other"          | Another type of synchronization rule - see description property.                                                                                                                                                                                                                            |

??? education "Further information"
    There is an article on [managing external identifiers](/features/external-identifiers/overview) to correlate metadata elements from different types of technologies.

--8<-- "snippets/abbr.md"
