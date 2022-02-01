---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

--8<-- "snippets/content-status/tech-preview.md"

# Engine host services

The engine host services support the behavior of the [engine host](/concepts/engine-host) OMAG Server.  They manage the start up and shutdown of the configured [Open Metadata Engine Services (OMESs)](/services/omes) as well as retrieve the configuration of their governance engines and governance services through the [Governance Engine OMAS](/services/omas/governance-engine/overview) running in a [Metadata Access Server](/concepts/metadata-access-server).

The engine host services also provide a REST API to query the status of the governance engines running in the server.

The internals of the Engine Host OMAG Server are shown in Figure 1:

![Figure 1](/services/omes/engine-services-engine-host-internals.svg)
> **Figure 1:** Inside the Engine Host OMAG Server

The engine host services shown at the top of the diagram are responsible for:

* Starting up each of the configured OMESs for the engine host.
* Retrieving the configuration for each governance engine and its governance services configured within the OMESs using the Governance Engine OMAS.
* Initializing an appropriate governance engine handler (implemented by the OMES) for each retrieved governance engine configuration.
* Listening for [governance action](/concepts/governance-action/overview) requests and passing each one to the appropriate governance engine handler for the governance engine that supports the [request type](/concepts/governance-request-type).  
* Monitor changes in the governance engine configuration and passing them on to the corresponding governance engine handler so the OMESs have the latest configuration.


??? education "Further information"

    There is more of an overview of open governance in the [Governance Action Framework (GAF)](/frameworks/gaf/overview).

    Instructions for [configuring an Engine Host OMAG Server](/guides/admin/server/configuring-an-engine-host) are found in the [Administration Guide](/guides/admin).

    Instructions for defining Governance Engines and Governance Services are located under the [Discovery and Stewardship](/features/discovery-and-stewardship) feature.

--8<-- "snippets/abbr.md"