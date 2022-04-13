<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

The [digital resource connectors](/concepts/digital-resource-connector) provide access to digital resources and their metadata that is stored in the open metadata ecosystem.  These connectors are for use by external applications and tools to connect with resources and services in the digital landscape.  These connectors also supply the Asset metadata from Egeria that describes these resources.

Instances of these connectors are created through the [Asset Consumer OMAS](/services/omas/asset-consumer/overview), [Asset Owner OMAS](/services/omas/asset-owner/overview) and [Discovery Engine OMAS](/services/omas/discovery-engine/overview) interfaces. They use the Connection linked to the corresponding Asset in the open metadata ecosystem.  If there are more than one connection associated with the asset, then a selection is made by the server [metadata security connector](/concepts/server-metadata-security-conector) running in the OMASs' server.

Connection objects are associated with assets in the metadata catalog using the Asset Owner OMAS, [Data Manager OMAS](/services/omas/data-manager/overview) and [Asset Manager OMAS](/services/omas/asset-manager/overview).

![Digital Resource Connector](/connectors/resource/digital-resource-connector.svg)


--8<-- "snippets/abbr.md"
