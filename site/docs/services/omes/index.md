---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Open Metadata Engine Services (OMES)

The engine services run in the [engine host](/concepts/engine-host).  They provide the special services that are available to the [governance services](/concepts/governance-services) through their context.  There is an engine service for each type of governance service.  Each engine service also maps the calls from the governance service to calls to the services of a [metadata access server](/concepts/metadata-access-server).  The table below summarizes the engine services, the type of governance service they support and the service on the metadata access server that they call.

| Name of the Engine Service                                                  | Type of Governance Service supported                                     | Partner service in the metadata                                     |
|-----------------------------------------------------------------------------|--------------------------------------------------------------------------|---------------------------------------------------------------------|
| [Survey Action OMES](/services/omes/survey-action/overview)                 | [Survey Action Service](/concepts/survey-action-service)                 | [Asset Owner OMAS](/services/omas/asset-owner/overview)             |
| [Governance Action OMES](/services/omes/governance-action/overview)         | [Governance Action Service](/concepts/governance-action-service)         | [Governance Engine OMAS](/services/omas/governance-engine/overview) |
| [Event Action OMES](/services/omes/event-action/overview)                   | [Event Action Service](/concepts/event-action-service)                   | [Data Science OMAS](/services/omas/data-science/overview)           |
| [Repository Governance OMES](/services/omes/repository-governance/overview) | [Repository Governance Service](/concepts/repository-governance-service) | [Repository Governance OMAS](/services/omrs)                        |
| [Asset Analysis OMES](/services/omes/asset-analysis/overview) (Deprecated)  | [Open Discovery Service](/concepts/open-discovery-service)               | [Discovery Engine OMAS](/services/omas/discovery-engine/overview)   |


The diagram below shows the generic picture of an engine service plugged into the Engine Host.  The [engine host services](/services/engine-host-services) provide most of the capability of the Engine Host.  This includes managing the retrieval of the [governance engine definitions](/concepts/governance-engine-definition) from the metadata access server that map the engine action requests to calls to the governance services.  

The engine services each provide an implementation of the governance engine handler that is able to run a particular type of governance service.  When an [engine action](/concepts/engine-action) is initiated, the engine host services receives it, claims it, selects the right engine handler and passes the engine action to it.   The governance engine handler runs the governance service through its governance service handler, making calls to the partner service as required.  It records the outcome in the engine outcome in the metadata access server.

![Engine Host Internals](engine-services-engine-host-internals.svg)


--8<-- "snippets/abbr.md"
