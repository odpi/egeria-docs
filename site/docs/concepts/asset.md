---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Asset

An *asset* is a metadata element that describes either a [digital or physical resource](/concepts/resource).  This resource is described in a metadata catalog because it provides value to the organization that owns it.
Examples of resources that might be catalogued as assets include:

- Data sources such as databases, files and data feeds.
- IT infrastructure and applications that automate many aspects of an organization's operation.
- APIs that provide access to the services offered by the organization.
- Analytical models and processes.
- Addresses and other locations. 
- Physical objects such as buildings that can have a digitized representation with a unique identity (for example, serial number).

Governance activities are often centered around an organization's resources since they represent tangible value. This involves maintaining information about the resource and managing events related to the resource in order to keep it protected and to get the maximum value from it.

Egeria is particularly focused on maintaining the information necessary for managing digital resources and the infrastructure that supports them. It also has a flexible type model to allow the definition of asset to be expanded to include new kinds of resources as they become relevant.

## Open metadata types

The information about a resource is stored as a linked collection of open metadata instances (entities and relationships) with the [Asset](/types/0/0010-Base-Model/#asset) entity at the root. The asset entity contains a small amount of information that merely captures the existence of the resource. Then other entities are linked to it to add more information. It is likely that this additional information is identified, captured and stored by different tools. The open metadata services gather this information together and distribute it to provide the most complete view of the resource's properties. 

More information on the types of attachments that can be added to an asset can be found in [Managing Metadata](/patterns/managing-metadata/overview).

Inheriting from asset is a hierarchy of increasingly-specialized definitions for different types of assets. Each definition adds more properties about the asset:

![Figure 1](asset-hierarchy.svg)
> **Figure 1:** Hierarchy of asset types defined in the open metadata types

*[Area 2 of the open metadata types](/types/2)* of the open metadata types is where the asset hierarchy is built out. 


## Accessing asset content through connectors

Egeria provides an open framework for accessing the content of digitized resources and the information about them. It is called the [Open Connector Framework (OCF)](/frameworks/ocf/overview) and it provides specialized connectors (clients) for accessing specific types of assets and the information about them.

The type of connector to use is specified in the [connection](/concepts/connection) that is linked to the asset.

[Model 0205](/types/2/0205-Connection-Linkage) in the open metadata types shows how an asset is associated with a [connection](/concepts/connection) object. The connection object provides the properties necessary to create a connector to access the asset's contents.

## APIs and events for managing asset information (metadata)

Egeria's [Asset Maker API](/services/omvs/asset-maker/overview) provide the specialized services for managing assets. 

## Sharing information about assets

Egeria's [Open Metadata Repository Services (OMRS)](/services/omrs) provides the ability to store and extract information about assets in a distributed collection of servers called an [open metadata repository cohort](/concepts/cohort-member). The cohort provides both peer-to-peer exchange of metadata via an event bus topic and federated queries between different members of the cohort. Egeria provides a [metadata access store](/concepts/metadata-access-store), a [metadata access point](/concepts/metadata-access-point) and a [repository proxy](/concepts/repository-proxy) server that are all able to join a cohort. The repository proxy supports the integration of third party servers (typically [asset managers](/software-capability/#asset-manager)) into the cohort. The mapping between the third party server's APIs and the open metadata APIs in this case is implemented in a [repository connector](/concepts/repository-connector).

It is also possible to manage the exchange of asset metadata with other types of third party technologies using the [Integration Connectors (OMISs)](/concepts/integraiton-connector) running in an [integration daemon](/concepts/integration-daemon). Using this pattern is simpler to integrate but involves maintaining a copy of the third party technology's metadata in a [metadata access store](/concepts/metadata-access-store) that can then join one or more open metadata repository cohorts to share this metadata more broadly. The mapping between the third party technology's APIs and the open metadata APIs in this case is implemented in an [integration connector](/connectors/integration-connector).

--8<-- "snippets/abbr.md"
