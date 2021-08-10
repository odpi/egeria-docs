<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Connected asset properties

**Connected asset properties** are the properties known about an asset accessed through a connector,
and are part of the [Open Connector Framework (OCF)](/egeria-docs/frameworks/ocf).
These properties are presented at three levels:

## Asset summary

`AssetSummary` holds asset properties that are used for displaying details of
an asset in summary lists or hover text:

| Property | Description |
|---|---|
| `type` | metadata type information for the asset |
| `guid` | GUID for the asset |
| `url` | external link for the asset |
| `qualifiedName` | The official (unique) name for the asset. This is often defined by the IT systems management organization and should be used (when available) on audit logs and error messages. (Sourced from the `qualifiedName` attribute in `Referenceable` - [model 0010](/egeria-docs/types/0/0010-base-model)) |
| `displayName` | A consumable name for the asset. Often a shortened form of the asset's qualifiedName for use on user interfaces and messages. The asset's displayName should be only be used for audit logs and error messages if the qualifiedName is not set. (Sourced from `displayName` attribute within `Asset` - [model 0010](/egeria-docs/types/0/0010-base-model)))
| `shortDescription` | Short description about the asset. (Sourced from `assetSummary` within `ConnectionsToAsset` - [model 0205](/egeria-docs/types/2/0205-connection-linkage)) |
| `description` | Full description of the asset. (Sourced from `description` attribute within `Asset` - [model 0010](/egeria-docs/types/0/0010-base-model)) |
| `owner` | Name of the person or organization that owns the asset. (Sourced from the `AssetOwnership` classification - [model 0445](/egeria-docs/types/4/0445-governance-roles)) |
| `zoneMembership` | List of governance zones assigned to the asset. (Sourced from the `AssetZoneMembership` classification - [model 0445](/egeria-docs/types/4/0424-governance-zones)) |
| `classifications` | Full list of the classifications assigned to the asset along with their properties. |

## Asset detail

`AssetDetail` extends `AssetSummary` to provide all the properties directly related to this asset:

| Property | Description |
|---|---|
| `ExternalIdentifiers` | List of identifiers for this asset that are used in other systems. |
| `RelatedMediaReferences` | List of links to external media (images, audio, video) about this asset. |
| `NoteLogs` | List of NoteLogs for this asset, often providing more detail on how to use the asset and its current status. |
| `ExternalReferences` | List of links to additional information about this asset. |
| `Connections` | List of connections defined to access this asset. |
| `Licenses` | List of licenses associated with the asset. |
| `Certifications` | List of certifications that have been awarded to this asset. |

## Asset universe

`AssetUniverse` extends `AssetDetail`, and adds information about the
common open metadata entities related to this asset:

| Property | Description |
|---|---|
| `meanings` | Glossary term(s) assigned to this asset. |
| `schema` | Details of the schema type associated with the asset. |
| `feedback` | Details of the likes, reviews and comments, that are connected to the asset. |
| `knownLocations` | Details of the known locations of the asset. |
| `lineage` | Details of the lineage for the asset. |
| `relatedAssets` | Details of the assets linked to this asset. |

## Implementation details

The [connector broker](connector-broker.md) does not have access
to a metadata repository because the OCF is metadata repository neutral.
When it creates a connector, the connected asset properties
are null.

[Egeria Open Metadata Access Services (OMAS)](/egeria-docs/services/omas) such as
[Asset Consumer OMAS](/egeria-docs/services/omas/asset-consumer), 
[Asset Owner OMAS](/egeria-docs/services/omas/asset-owner) and
[Discovery Engine OMAS](/egeria-docs/services/omas/discovery-engine), 
include the connector broker in their clients and 
support APIs for managing connections and creating
connectors.

Connectors created by the Egeria access services
will include the connected asset properties object
configured to retrieve metadata from the
same open metadata repository where the OMAS is running.

The connected asset properties
are retrieved from the open metadata repositories by
[OCF Metadata Management](../../../../common-services/ocf-metadata-management).
It will use the same user id that was used to create the
connector.

--8<-- "snippets/abbr.md"
