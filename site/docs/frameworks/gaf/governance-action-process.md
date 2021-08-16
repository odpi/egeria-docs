<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Governance Action Process

A governance action process defines a prescribed sequence of [governance actions](governance-action.md). Its definition consists of a linked set of [governance action types](governance-action-type.md). Each governance action type describes which [governance action service](/egeria-docs/frameworks/gaf/#governance-action-services) to run from which [governance action engine](/egeria-docs/frameworks/gaf/#configuring-governance-action-services) along with the *request type* and *request parameters* to pass. The linkage between the governance action types shows the [guards](guard.md) that must be true to initiate the next governance action in the flow.

- The [0461 governance action engines](/egeria-docs/types/4/0461-governance-engines.md) model shows how the request type links the governance action engine to the governance action service via the `SupportedGovernanceActionService` relationship.
- The [0470 incident reporting](/egeria-docs/types/4/0470-incident-reporting) model shows the structure of the incident report. It is a [Referenceable](/egeria-docs/types/0/0010-base-model/#referenceable) so it can support comments and have [governance actions](governance-action.md) linked to it.

!!! education "Further information"
    - Governance action processes are defined using the [Governance Engine OMAS](/egeria-docs/services/omas/governance-engine).
    - The [Open Metadata Engine Services (OMES)](/egeria-docs/services/omes) provide the mechanisms that support the different types of [governance action engines](/egeria-docs/frameworks/gaf/#configuring-governance-action-services). These engines run the [governance action services](/egeria-docs/frameworks/gaf/#governance-action-services) that execute the [governance actions](governance-action.md) defined by the governance action process.

--8<-- "snippets/abbr.md"
