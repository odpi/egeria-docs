---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Connector

A **connector** is a Java client object that provides applications with access to a data source or service
(known as an [asset](asset.md)) along with its related metadata, and is part of the [Open Connector Framework (OCF)](/egeria-docs/frameworks/ocf).

An OCF connector provides four APIs:

| API | Description |
|---|---|
| Connector lifecycle | Manages the lifecycle state of the connector and includes `initialize()`, `start()` and `disconnect()`. |
| Metadata store initialization | If the connector is created by a metadata service then it adds a client to the metadata server called [`ConnectedAssetProperties`](connected-asset-properties.md) to the connector between `initialize()` and `start()`. The `ConnectedAssetProperties` client can be retrieved from the connector instance and used to retrieve metadata about the asset that is stored in the metadata server. |
| Specific initialization for the type of connector | Some types of connectors need additional initialization. These methods are called by the component creating the connector before the `start()` method is called. |
| Asset content | This API is crafted to provide the most natural interface to the asset's contents. Therefore, the asset content API is typically different for each type of connector. |

OCF connectors are not limited to representing assets as they are physically implemented.
An OCF connector can represent a simplified logical (virtual) asset, such as a data set, that is designed for the needs
of a specific application or tool.
This type of connector delegates the requests it receives to one or more physical data resources.
It is called a _virtual connector_.

!!! education "Further information"
    See the [developer guide](/egeria-docs/guides/developer) for information on writing connectors.

--8<-- "snippets/abbr.md"
