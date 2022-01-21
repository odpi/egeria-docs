<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->


# Governance Engine

A governance engine is responsible for executing requests to a collection of related [governance services](/egeria-docs/concepts/governance-service).

--8<-- "docs/concepts/governance-service-types.md"

The governance engine executes an [Open Metadata Engine Service (OMES)](/egeria-docs/services/omes)
running in an [Engine Host](/egeria-docs/concepts/engine-host) OMAG Server.

When a governance engine is called, it is passed a [governance request type](/egeria-docs/concepts/governance-request-type) and request parameters.  This is mapped to a call to a governance service through the governance engine definition.  Figure 1 shows the structure of a governance engine definition.

![Figure 1](/egeria-docs/guides/developer/open-metadata-archive/governance-engine-definition.svg)
> **Figure 1:** The structure of a governance engine definition

The open metadata types for this definition are in model [0461 - Governance Engines](/egeria-docs/types/4/0461-Governance-Engines) - specifically notice **Governance Engine** and **GovernanceService** linked by the **SupportedGovernanceService** relationship.

??? education "Further information"

    Each governance engine has a unique name.  A *governance engine definition* for this unique name is either created through the [Governance Engine OMAS](/egeria-docs/services/omas/governance-engine/overview) API or as part of a [governance engine pack](/egeria-docs/concepts/governance-engine-pack).


--8<-- "snippets/abbr.md"