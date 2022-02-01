---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/in-development.md"

# Lineage Integrator Open Metadata Integration Service (OMIS)

The Lineage Integrator OMIS supports the following services for its hosted [integration connectors](/concepts/integration-connector):

- Registering a listener for [OpenLineage events](/features/lineage-management/overview/#openlineage-standard) received either:
    - through the Lineage Integrator OMIS's OpenLineage REST API or 
    - published by other integration connectors running in the same Lineage Integrator OMIS.
    
- Registering a listener for events from the Asset Manager OMAS OutTopic. These events notify the integration connector of any changes to open metadata elements (entities) that are visible through the Asset Manager OMAS.  These events can be used to drive the publishing of lineage information to third party technologies.

- Publishing OpenLineage events to other integration connectors running in the same Lineage Integrator OMIS that have registered a listener for these events.

- Cataloguing lineage information from a third party technology.  Specifically this include process structure, ports, schemas and the data assets they are working with.

It has an external REST API with two operations:

- Validate whether a connector implementation is an integration connector that will run in the Lineage Integrator OMIS.

- Receive an *OpenLineage event* from a third party.

Both of these REST APIs are callable through Lineage Integrator OMIS's java client *LineageIntegrator*.


!!! education "Further information"
    - [Lineage Management](/features/lineage-management/overview) describes how to set up Egeria to capture, steward, preserve and use lineage.
    - [Lineage Integration Connectors](/connectors/#lineage) describe the pre-built connectors that run in the Lineage Integrator OMIS.
    - [Writing an Integration Connector](/guides/developer/integration-connectors/overview) describes how to wrote your own integration connectors for the Lineage Integrator OMAS.


## Module Implementation

The modules are as follows:

- *lineage-integrator-api* - defines the interface for an integration
connector that is supported by the Lineage Integrator OMIS. This includes the implementation
of the context that wraps the Asset Manager OMAS's clients.

- *lineage-integrator-server* - implements the context manager for
the Lineage Integrator OMIS.

- *lineage-integrator-spring* - implements a rest API for validating that a specific
integration connector is able to run under this service.

- *lineage-integrator-client* - implements a Java client for the REST API.  There are two operations. To query

This integration service is paired with the [Asset Manager](/services/omas/asset-manager/overview)
Open Metadata Access Service (OMAS).

--8<-- "snippets/abbr.md"