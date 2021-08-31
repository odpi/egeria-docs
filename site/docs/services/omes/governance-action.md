---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/in-development.md"

# Governance Action Open Metadata Engine Services (OMES)

The Governance Action Open Metadata Engine Service (OMES) runs in an [Engine Host OMAG Server](/egeria-docs/concepts/engine-host).

It provides access to the open metadata ecosystem for [governance action services](/egeria-docs/frameworks/gaf/#governance-action-service). These are pluggable connectors that manage governance of open metadata. Their interfaces are defined by the [Governance Action Framework (GAF)](/egeria-docs/frameworks/gaf) and supported by the Governance Action OMES.

The governance Action OMES also provides an API to allow a third party tool to validate that a specific governance action service will load in the engine host server, and it returns the usage information encoded in the service's implementation.

## Using the Governance Action OMES

Governance action services are defined and linked to one or more [governance action engines](/egeria-docs/frameworks/gaf/#governance-action-engine) using the [Governance Engine OMAS](/egeria-docs/services/omas/governance-engine). The definitions for both the governance action engines and their linked services are stored in a [metadata server](/egeria-docs/concepts/metadata-server).

When the Governance Action OMES is configured in the engine host, a list of governance action engines is supplied. This determines which governance action engines and hence governance action services that it supports.

The Governance Action OMES is responsible for initializing the governance action engines and providing the context and runtime environment for [governance action services](/egeria-docs/frameworks/gaf/#governance-action-service) when they are requested by third party technologies or through the governance action processing of the [Governance Engine OMAS](/egeria-docs/services/omas/governance-engine).

--8<-- "snippets/abbr.md"
