---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# Lineage Modeling

The open integration framework supports the following services for its hosted [integration connectors](/concepts/integration-connector):

- Registering a listener for [OpenLineage events](/features/lineage-management/overview/#openlineage-standard) received either:
    - through the integration daemon's OpenLineage REST API or 
    - published by other integration connectors running in the same integration daemon.
    
- Registering a listener for events from the Open MEtadata Services OutTopic. These events notify the integration connector of any changes to open metadata elements (entities) that are visible through the Asset Manager OMAS.  These events can be used to drive the publishing of lineage information to third party technologies.

- Publishing OpenLineage events to other integration connectors running in the same integration daemon that have registered a listener for these events.

- Cataloguing lineage information from a third party technology.  Specifically this include process structure, ports, schemas and the data assets they are working with.

It has an external REST API with two operations:

- Validate whether a connector implementation is an integration connector that will run in the integration daemon.

- Receive an *OpenLineage event* from a third party.

Both of these REST APIs are callable through the [Runtime Manager API](/services/omvs/runtime-manager/overview).


!!! education "Further information"
    - [Lineage Management](/features/lineage-management/overview) describes how to set up Egeria to capture, steward, preserve and use lineage.
    - [Writing an Integration Connector](/guides/developer/integration-connectors/overview) describes how to wrote your own integration connectors for the Lineage Integrator OMAS.


--8<-- "snippets/abbr.md"