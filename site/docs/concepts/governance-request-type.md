<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->


# Governance Request Type

The *governance request type* defines the descriptive name of a specific governance activity that the organization wishes to run.

The request type is mapped to a [governance service](/concepts/governance-service) implementation along with request parameters to configure the behaviour of the service in a [governance engine definition](/concepts/governance-engine) as shown in Figure 1.

![Figure 1](/guides/developer/open-metadata-archives/governance-engine-definition.svg)
> **Figure 1:** Governance request types as part of a governance engine definition

Governance services are run by the [Open Metadata Engine Services (OMES)](/services/omes) in an [Engine Host](/concepts/engine-host) OMAG Server.  The [Engine Host Services](/services/engine-host-services) in the engine host call the [Governance Engine OMAS](/services/omas/governance-engine/overview) to retrieve the governance engine definition.  When a [governance action](/concepts/governance-action) request is made, the supplied request type is used by the OMES to determine which [Governance Service](/concepts/governance-service) to run.


??? education "Further information"

    The Open Metadata Types model *[0461 Governance Action Engines](/types/4/0461-Governance-Engines)* shows how the request type links the governance engine to the governance service via the *SupportedGovernanceService* relationship.
    
    Governance engine definitions are typically maintained as a [governance engine pack](/concepts/governance-engine-pack).  They may also be defined through the [Governance Engine OMAS](/services/omas/governance-engine/overview)


--8<-- "snippets/abbr.md"