---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

--8<-- "snippets/content-status/stable.md"

# Lineage warehouse services

The open lineage services support the behavior of the [Lineage Warehouse](/concepts/lineage-warehouse) and its main purpose to preserve and report lineage metadata.

![Figure 1 - Services in Lineage Warehouse](lineage-warehouse-services.svg)

Following sequence explains how different services interact in and out the Lineage Warehouse:

1. Metadata instance events from the cohort are distributed to Metadata Access Server running [Asset Lineage OMAS]/services/omas/asset-lineage/overview. This access service is always paired with Lineage Warehouse.

2. [Asset Lineage OMAS](/services/omas/asset-lineage/overview) feeds the lineage warehouse by selecting and sending the instance types suitable for lineage. It retrieves asset related metadata and completes the asset context portion of the graph. Once ready, this lineage context graph structured as vertices and edges is sent on Lineage Output Topic for further processing and preservation.

3. **Lineage event listener** consumes asset context events and uses technology connector such as [Lineage Warehouse Janus Connector](/connectors/governance-daemon/lineage-warehouse-janus-connector) to persist these lineage elements building up the large lineage graph. 

4. **Lineage jobs** run tasks that get executed in server background to:

    - Poll for changes and request updates using REST API (`AssetLineageUpdateJob`); and 
    - Scan the lineage graph and augment lineage paths for optimized querying (`LineageGraphJob`).

5. **Lineage query service** provides REST API used to query asset lineage store for specific business views such as horizontal and vertical.

# Further information

- Configuring the lineage warehouse following the [admin guide](/guides/admin/servers/by-server-type/configuring-a-lineage-warehouse/).

- Find out how to configure options for the [Lineage Warehouse JanusGraph Connector](/connectors/governance-daemon/lineage-warehouse-janus-connector) and supported underlying storage and indexing backend technologies.

- [Lineage Management](/features/lineage-management/overview/) feature overview.

--8<-- "snippets/abbr.md"