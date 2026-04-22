---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Leveraging Open Lineage

--8<-- "snippets/work-in-progress.md"

Egeria is able to capture open lineage events to:

* Harvest information about data stores and processes that are emitting open lineage events.
* Providing organized storage of open lineage events to allow later analysis.
* Routing open lineage events to other services (such as Marquez) either:

    * Received through the open lineage topic
    * Produced by Egeria's governance processes 

### Open Lineage Connectors

The [open lineage connectors](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/integration-connectors/openlineage-integration-connectors) work with the [Open Lineage standard](/features/lineage-management/overview/#the-openlineage-standard)

* **Open Lineage Event Receiver integration connector** receives open lineage events from an event topic and publish them to integration connectors with listeners registered in the same integration daemon server.
* **Governance Action to Open Lineage integration connector** listens for governance actions executing in the open metadata ecosystem, generate open lineage events for them and publish them to the integration connectors running in the same integration daemon instance that are listening for OpenLineage events.
* **API-based Open Lineage Log Store integration connector** calls an OpenLineage compliant API to store the open lineage events that are passed to it through the OpenLineage listener that is registered with the integration daemon.
* **File-based Open Lineage Log Store integration connector** stores the open lineage events that are passed to it through the OpenLineage listener that is registered with the integration daemon. Each OpenLineage event is stored in its own file in JSON format.  These files are organized according to the namespace and job name in the event.
* **Open Lineage Cataloguer integration connector** registers an Open Lineage listener with the integration daemon and to catalog any processes that are not already known to the open metadata ecosystem.

--8<-- "snippets/abbr.md"