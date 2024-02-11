<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

The governance daemon connectors contain specialist connectors for the [governance servers](/concepts/governance-server) that make active use of open metadata.

* The *Integration Connector* supports the ongoing exchange of metadata between open metadata and a third party technology.  It runs in an [Integration Daemon](/concepts/integraiton-daemon).
* The *Governance Service* is a connector that runs in a [Governance Engine](/concepts/governance-service) hosted on the [Engine Host](/concepts/engine-host).
* The *Lineage Warehouse Connector* provides access to a specialist repository for managing lineage information extracted from the open metadata ecosystem.  It runs in a [Lineage Warehouse](/concepts/lineage-warehouse).
* The *Data Engine Connector* extracts metadata from a data engine.  It has been designed around the needs of IBM's DataStage ETL Engine.  It runs in the [Data Engine Proxy](/concepts/data-engine-proxy).

