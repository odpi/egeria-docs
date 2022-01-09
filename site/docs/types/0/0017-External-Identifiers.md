<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0017 External Identifiers

External identifiers are used to correlate the identifiers used in third party metadata catalogs with open metadata elements.

![UML](0017-External-Identifiers.svg)

## ExternalId

The *`ExternalId`* entity describes an external identifier from a specific third party metadata repository. It includes:

- The identifier value itself in `identifier`.
- The pattern used for the identifier (how it is generated and managed) is stored in `keyPattern`. These are the values it can take, with the default (and most used) being `LOCAL_KEY`:

    | Value | Meaning |
    |---|---|
    | `LOCAL_KEY` | Unique key allocated and used within the scope of a single system. |
    | `RECYCLED_KEY` | Key allocated and used within the scope of a single system that is periodically reused for different records. |
    | `NATURAL_KEY` | Key derived from an attribute of the entity, such as email address, passport number. |
    | `MIRROR_KEY` | Key value copied from another system. |
    | `AGGREGATE_KEY` | Key formed by combining keys from multiple systems. |
    | `CALLERS_KEY` | Key from another system can bey used if system name provided. |
    | `STABLE_KEY` | Key value will remain active even if records are merged. |
    | `OTHER` | Another key pattern. |

## ExternalIdLink

The mapping of identifiers can be many-to-many, which is why you see that the *`ExternalIdLink`* relationship between the [`OpenMetadataRoot`](/egeria-docs/types/0/0010-Base-Model/#openmetadataroot) (open metadata resources) and the `ExternalId` is also many-to-many.

This relationship includes properties to help to map the `OpenMetadataRoot` to the external identifier.

## ExternalIdScope

There is no guarantee that external identifiers from a third party metadata catalog are globally unique and so the *`ExternalIdScope`* relationship links the external identifier to the [`Referenceable`](/egeria-docs/types/0/0010-Base-Model/#referenceable) that represents the third party metadata catalog. Typically, this is a type of [`SoftwareCapability`](/egeria-docs/types/0/0042-Software-Capabilities/#softwarecapability), for example, [`AssetManager`](/egeria-docs/types/0/0056-Resource-Managers/#assetmanager).

??? education "Further information"
    There is an article on [managing external identifiers](/egeria-docs/features/external-identifiers/overview) to correlate metadata elements from different types of technologies.

--8<-- "snippets/abbr.md"
