<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Governance Service

A governance service is a specialized [connector](/egeria-docs/concepts/connector) that implements a specific [type of governance action](/egeria-docs/concepts/governance-action).

--8<-- "docs/concepts/governance-service-types.md"

## Catalog of governance services

* [Open Discovery Service Catalog](/egeria-docs/connectors/#open-discovery-services)
* [Governance Action Service Catalog](/egeria-docs/connectors/#governance-action-services)
* [Archive Service Catalog](/egeria-docs/connectors/#archive-services)

## Implementing your own governance services

Instructions for implementing your own governance services are in the developer guide under the following sections: 

* [Writing Open Discovery Services](/egeria-docs/guides/developer/open-dicovery-services/overview)
* [Writing Governance Action Services](/egeria-docs/guides/developer/governance-action-services/overview)
* [Writing Archive Services](/egeria-docs/guides/developer/archive-services/overview)

## Support for running governance services

The [Governance Engine OMAS](/egeria-docs/services/omas/governance-engine/overview) provides:

* The API to create [governance engine definitions](/egeria-docs/concepts/governance-engine) for the governance services.
* The API to link governance services together into [governance action processes](/egeria-docs/concepts/governance-action-process).
* The metadata support for the [Engine Host Services](/egeria-docs/services/engine-host-services) to drive the governance services in an [Engine Host](/egeria-docs/concepts/engine-host) OMAG Server.


--8<-- "snippets/abbr.md"