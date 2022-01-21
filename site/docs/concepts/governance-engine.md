<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->


# Governance Engine

A *governance engine* is responsible for executing requests to a collection of related [governance services](/egeria-docs/concepts/governance-service).

--8<-- "docs/concepts/governance-service-types.md"

The governance engine executes an [Open Metadata Engine Service (OMES)](/egeria-docs/services/omes)
running in an [Engine Host](/egeria-docs/concepts/engine-host) OMAG Server.

When a governance engine is called, it is passed a [governance request type](/egeria-docs/concepts/governance-request-type) and request parameters.  This is mapped to a call to a governance service through the [governance engine definition](/egeria-docs/concepts/governance-engine-definition).

![Governance Engine Definition](/egeria-docs/guides/developer/open-metadata-archives/governance-engine-definition.svg)
> The structure of a governance engine definition



??? education "Further information"

    Each governance engine has a unique name.  A *governance engine definition* for this unique name is either created through the [Governance Engine OMAS](/egeria-docs/services/omas/governance-engine/overview) API or as part of a [governance engine pack](/egeria-docs/concepts/governance-engine-pack).  The [governance engine is configured](/egeria-docs/guides/admin/servers/configuring-an-engine-host/#configure-engine-service) in the [engine host](/egeria-docs/concepts/engine-host) using this unique name.

    The open metadata types for this definition are in model [0461 - Governance Engines](/egeria-docs/types/4/0461-Governance-Engines) - specifically notice **Governance Engine** and **GovernanceService** linked by the **SupportedGovernanceService** relationship.

--8<-- "snippets/abbr.md"