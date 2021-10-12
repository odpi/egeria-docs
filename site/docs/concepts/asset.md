---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Asset

An *asset* is a metadata element that describes either a digital or physical resource.  This resource is described in the metadata catalog because it provides value to the organization that owns it.
Examples of resources that might be catalogued as assets include:

- Data sources such as databases, files and data feeds.
- IT infrastructure and applications that automate many aspects of an organization's operation.
- APIs that provide access to the services offered by the organization.
- Analytical models and processes that differentiate an organization from its competitors or ensure it is operating legally and ethically.
- Buildings and other locations.
- Physical objects that have a unique identity (eg a serial number).

Much governance is centered around an organization's resources since they represent tangible value. This involves maintaining information about the resource and managing events related to the resource in order to keep it protected and to get the maximum value from it.

Egeria is particularly focused on maintaining the information necessary for managing digital resources and the infrastructure that supports them. It also has a flexible type model to allow the definition of asset to be expanded to include a broader range of physical resources.

## Open metadata types

The information about a resource that covers its characteristics and how it should be managed is stored in a sub-graph of open metadata instances (entities and relationships) with the [Asset](/egeria-docs/types/0/0010-Base-Model/#asset) entity at the root. The asset entity contains a small amount of information that merely captures the existence of the real resource. Then other entities are linked to it to add more information. It is likely that this additional information is identified, captured and stored by different tools. The open metadata services gather this information together and distribute it to provide the most complete view of the resource's properties.

More information on the types of attachments that can be added to an asset can be found in [Managing Metadata](/egeria-docs/patterns/managing-metadata/overview).

Inheriting from asset is a hierarchy of increasingly-specialized definitions for different types of assets. Each definition adds more properties about the asset:

![Asset hierarchy](asset-hierarchy.svg)

**[Area 2](/egeria-docs/types/2)** is where the asset hierarchy is built out.

## Accessing asset content through connectors

Egeria provides an open framework for accessing the content of digital assets and the information about them. It is called the [Open Connector Framework (OCF)](/egeria-docs/frameworks/ocf/overview) and it provides specialized connectors (clients) for accessing specific types of assets and the information about them.

The type of connector to use is specified in the [connection](/egeria-docs/concepts/connection) entity that is linked to the asset.

[Model 0205](/egeria-docs/types/2/0205-Connection-Linkage) in the open metadata types shows how an asset is associated with a [connection](/egeria-docs/concepts/connection) object. The connection object provides the properties necessary to create a connector to access the asset's contents.

## APIs and events for managing asset information (metadata)

Egeria's [Open Metadata Access Services (OMAS)](/egeria-docs/services/omas) provide the specialized services for managing assets. Each OMAS focuses on a particular part of the asset lifecycle or person/tool that is working with the assets.

Some examples:

| OMAS | Description |
|---|---|
| [Analytics Modeling OMAS](/egeria-docs/services/omas/analytics-modeling/overview) | enables business intelligence and data virtualization tools to maintain information about the data views and reporting assets they are maintaining. |
| [Asset Catalog OMAS](/egeria-docs/services/omas/asset-catalog/overview) | provides a search service for locating assets. |
| [Asset Consumer OMAS](/egeria-docs/services/omas/asset-consumer/overview) | provides a service for accessing the content of an asset, extracting additional information that is known about the asset and providing feedback about the asset. It is designed for tools that consume assets to support the work of their users. These users can provide feedback on the asset description and the resource that it describes. |
| [Asset Manager OMAS](/egeria-docs/services/omas/asset-manager/overview) | provides a service for exchanging metadata about assets and related information with a third party [asset manager](/egeria-docs/concepts/server-capability). This API supports the many-to-many correlation of identifiers used in the third party asset manager and the open metadata ecosystem. |
| [Asset Owner OMAS](/egeria-docs/services/omas/asset-owner/overview) | provides a service for the owner of an asset to classify and manage the asset, and understand how it is being used by the organization. |
| [Discovery Engine OMAS](/egeria-docs/services/omas/discovery-engine/overview) | provides a service for adding annotations to an asset's information that has been determined by specific analysis of the asset's contents by a [discovery service](/egeria-docs/concepts/open-discovery-service). |
| [Data Manager OMAS](/egeria-docs/services/omas/data-manager/overview) | enables a data manager (such as a database or file system) to maintain information about the assets it stores. |
| [Governance Engine OMAS](/egeria-docs/services/omas/governance-engine/overview) | provides the metadata services for [governance action services](/egeria-docs/concepts/governance-action-service) that verify, enhance and correct the properties of assets and their associated elements. |
| [IT Infrastructure OMAS](/egeria-docs/services/omas/it-infrastructure/overview) | provides a service for maintaining information about the IT assets and supporting infrastructure owned or used by an organization. |
| [Data Science OMAS](/egeria-docs/services/omas/data-science/overview) | provides a service for maintaining information about analytical models and related assets such as python notebooks. |

## Sharing information about assets

Egeria's [Open Metadata Repository Services (OMRS)](/egeria-docs/services/omrs) provides the ability to store and extract information about assets in a distributed collection of servers called an [open metadata repository cohort](/egeria-docs/services/omrs/cohort). The cohort provides both peer-to-peer exchange of metadata via an event bus topic and federated queries between different members of the cohort. Egeria provides a [metadata server](/egeria-docs/concepts/metadata-server), a [metadata access point](/egeria-docs/concepts/metadata-access-point) and a [repository proxy](/egeria-docs/concepts/repository-proxy) server that are all able to join a cohort. The repository proxy supports the integration of third party servers (typically [asset managers](../server-capabilities/asset-manager.md)) into the cohort. The mapping between the third party server's APIs and the open metadata APIs in this case is implemented in an [repository connector](/egeria-docs/connectors/repository-connector).

It is also possible to manage the exchange of asset metadata with other types of third party technologies using the [Open Metadata Integration Services (OMIS)](/egeria-docs/services/omis) running in an [integration daemon](/egeria-docs/concepts/integration-daemon). Using this pattern is simpler to integrate but involves maintaining a copy of the third party technology's metadata in a [metadata server](/egeria-docs/concepts/metadata-server) that can then join one or more open metadata repository cohorts to share this metadata more broadly. The mapping between the third party technology's APIs and the open metadata APIs in this case is implemented in an [integration connector](/egeria-docs/connectors/integration-connector).

--8<-- "snippets/abbr.md"
