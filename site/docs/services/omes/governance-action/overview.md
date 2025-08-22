---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# Governance Action Open Metadata Engine Services (OMES)

The Governance Action Open Metadata Engine Service (OMES) runs in an [Engine Host OMAG Server](/concepts/engine-host).

![Governance Action OMES](/services/omes/engine-services-governance-action-server-side.svg)

It provides access to the open metadata ecosystem for [governance action services](/guides/developer/governance-action-services/overview). These are pluggable connectors that manage governance of open metadata. Their interfaces are defined by the [Open Governance Framework (OGF)](/frameworks/ogf/overview) and supported by the Governance Action OMES.

The governance Action OMES also provides an API to allow a third party tool to validate that a specific governance action service implementation will load in the engine host server, and it returns the usage information encoded in the service's implementation.

## Using the Governance Action OMES

Governance action services are defined and linked to one or more [governance action engines](/concepts/governance-action-engine) using the [Governance Server OMAS](/services/omas/governance-server/overview). The definitions for both the governance action engines and their linked services are stored in a [governance engine definition](/concepts/governance-engine-definition).

When the Governance Action OMES is configured in the engine host, a list of governance action engines is supplied. This determines which governance action engines and hence governance action services that it supports.

The Governance Action OMES is responsible for initializing the governance action engines and providing the context and runtime environment for its governance action services.

--8<-- "snippets/abbr.md"
