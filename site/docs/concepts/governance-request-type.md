<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->


# Governance Request Type

The *governance request type* defines the descriptive name of a specific governance action that the organization wishes to run.  It is passed to the activated [governance service](/concepts/governance-service) along with some request parameters (name-value pairs of properties) and its [action targets](/concepts/action-target) when it starts.  The governance request type, request parameters and action targets collectively instruct the governance service on the action to perform.

The governance request type is also used to identify which governance service to run. It is mapped to a [governance service](/concepts/governance-service) implementation along with an initial set of request parameters in a [governance engine definition](/concepts/governance-engine) as shown in Figure 1.

![Figure 1](/guides/developer/open-metadata-archives/governance-engine-definition.svg)
> **Figure 1:** Governance request types as part of a governance engine definition

When the governance engine is called with the request type, the governance engine definition is used to identify the governance service to run.

!!! education "Further information"
    * The Open Metadata Types model *[0461 Governance Action Engines](/types/4/0461-Governance-Engines)* shows how the governance request type links the governance engine to the governance service via the *SupportedGovernanceService* relationship.
    * [Building governance action services](/guides/developer/governance-action-services/overview) describes how the governance request type, request parameters and target actions are passed to a governance action service.
    


--8<-- "snippets/abbr.md"