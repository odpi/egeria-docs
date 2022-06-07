<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Governance Action Process

A *governance action process* is a predefined sequence of [governance actions](/concepts/governance-action) that are coordinated by the [Governance Engine OMAS](/services/omas/governance-engine/overview).

The steps in a governance action process are defined by linked [governance action types](/concepts/governance-action-type).  Each governance action type provides the specification of the governance action to run.  The links between then show which guards cause the governance action to run.

## Examples

![Example 1](governance-action-process-example-1.svg)
![Example 2](governance-action-process-example-2.svg)

Details of how to set up governance action process is described in the 
[Governance Engine OMAS User Guide](/services/omas/governance-engine/overview).


!!! education "Further information"
    - The [0461 Governance Engines](/types/4/0461-Governance-Engines) model shows how the request type links the governance action engine to the governance action service via the `SupportedGovernanceService` relationship.
    - Governance action processes are defined using the [Governance Engine OMAS](/services/omas/governance-engine/overview).
    - The [Open Metadata Engine Services (OMES)](/services/omes) provide the mechanisms that support the different types of [governance action engines](#configuring-governance-action-services). These engines run the [governance action services](#governance-action-services) that execute the [governance actions](#governance-action) defined by the governance action process.


--8<-- "snippets/abbr.md"