---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Governance server

A *Governance Server* is a specialized [OMAG Server](/concepts/omag-server). It is designed to host specific governance daemon connectors that manage metadata in different technologies or perform specific active governance actions.

![Governance server](governance-server.svg)

The governance servers each have a specific subsystem that contains its services. They are also paired with different [Open Metadata Access Services (OMASs)](/services/omas) that supports appropriate open metadata services needed by the governance server.

The table below shows the different types of governance servers and the OMASs they are paired with.

| Governance Server                                   | Description                                                              | Supported by subsystem                                               | Paired with OMAS                                                                                                                                                                                                                                             | 
|:----------------------------------------------------|:-------------------------------------------------------------------------|:---------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| 
| [Integration Daemon](/concepts/integraition-daemon) | Manages the capture of metadata through configured integration services. | [Integration Daemon Services](/services/integration-daemon-services) | [Governance Server OMAS](/services/omas/governance-server/overview) provides support for retrieving governance engine definitions.  The [integration services](../../integration-services) define the OMASs that support each type of integration connector. |
| [Engine Host](/concepts/engine-host)                | Manages governance engines.                                              | [Engine Host Services](/services/engine-host-services)               | [Governance Server OMAS](/services/omas/governance-server/overview) provides support for retrieving governance engine definitions. The [engine services](../../engine-services) define the OMASs that support each type of governance engine.                |
| [Data Engine Proxy](/concepts/data-engine-proxy)    | Manages capture of metadata from a data engine.                          | [Data Engine Proxy Services](/services/data-engine-proxy-services)   | [Data Engine OMAS](/services/omas/data-engine/overview)                                                                                                                                                                                                      | 
| [Lineage Warehouse](/concepts/lineage-warehouse)    | Provides a historic reporting warehouse for lineage.                     | [Lineage Warehouse Services](/services/lineage-warehouse-services)   | [Asset Lineage OMAS](/services/omas/asset-lineage/overview)                                                                                                                                                                                                  | 


--8<-- "snippets/abbr.md"
