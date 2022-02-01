---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

--8<-- "snippets/content-status/released.md"

# Open lineage services

The open lineage services support the behavior of the [open lineage server](/concepts/open-lineage-server) and its main purpose to preserve and report lineage metadata.

![Figure 1 - Services in Open Lineage Server](open-lineage-services.svg)

Following sequence explains how different services interact in and out the open lineage server:

1. Metadata instance events from the cohort are distributed to Metadata Access Server running **Asset Lineage OMAS**. This access service is always paired with open lineage server.

2. [Asset Lineage OMAS](/services/omas/asset-lineage/overview) feeds the lineage warehouse by selecting and sending the instance types suitable for lineage. It retrieves asset related metadata and completes the asset context portion of the graph. Once ready, this lineage context graph structured as vertices and edges is sent on Lineage Output Topic for further processing and preservation.

3. **Lineage event listener** consumes asset context events and uses technology connector such as [Lineage Janus Connector](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/governance-daemon-connectors/open-lineage-connectors/open-lineage-janus-connector) to persist these lineage elements building up the large lineage graph. 

4. **Lineage jobs** run tasks that get executed in server background to:

    - Poll for changes and request updates using REST API (`AssetLineageUpdateJob`); and 
    - Scan the lineage graph and augment lineage paths for optimized querying (`LineageGraphJob`).

5. **Lineage query service** provides REST API used to query asset lineage store for specific business views such as horizontal and vertical.

# Further information

- Configuring the open lineage server following the [admin guide](/guides/admin/servers/configuring-an-open-lineage-server/).

- Find out how to configure options for the [Janus Lineage Connector](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/governance-daemon-connectors/open-lineage-connectors/open-lineage-janus-connector) and supported underlying storage and indexing backend technologies.

- [Lineage Management](/features/lineage-management/overview/) feature overview.

--8<-- "snippets/abbr.md"