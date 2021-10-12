<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->


# Governance Request Type

The governance request type defines the descriptive name of a specific
governance activity that the organization wishes to run.

The request type is mapped to a [governance service](governance-service.md) implementation
along with request parameters to configure the behaviour of the service
in a [governance engine definition](governance-engine.md) as shown in
Figure 1.

![Figure 1](../services/omas/governance-engine/governance-request-type.png)
> **Figure 1:** Governance request types as part of a governance engine definition

Governance services are run by the
[Open Metadata Engine Services (OMES)](/egeria-docs/services/omes)
in an [Engine Host](/egeria-docs/concepts/engine-host)
OMAG Server.  The [Engine Host Services](/egeria-docs/services/engine-host-services)
called the [Governance Engine OMAS](/egeria-docs/services/omas/governance-engine/overview)

They are used by the [Governance Engines](governance-engine.md)
to determine which [Governance Service](governance-service.md)
to run.



## Related Information

The Open Metadata Types model 
*[0461 Governance Action Engines](/egeria-docs/types/4/0461-Governance-Engines)*
shows how the request type links the governance engine to the
governance service via the *SupportedGovernanceService* relationship.


--8<-- "snippets/abbr.md"