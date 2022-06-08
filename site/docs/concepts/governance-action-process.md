<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Governance Action Process

A *governance action process* is a predefined sequence of [governance actions](/concepts/governance-action) that are coordinated by the [Governance Engine OMAS](/services/omas/governance-engine/overview).

The steps in a governance action process are defined by linked [governance action types](/concepts/governance-action-type).  Each governance action type provides the specification of the governance action to run.  The links between then show which [guards](/concepts/guard) cause the governance action to run.

## Examples

![Example 1](governance-action-process-example-1.svg)
![Example 2](governance-action-process-example-2.svg)


!!! education "Further information"
    - The [0462 Governance Action Types](/types/4/0462-Governance-Action-Types) model shows how the governance action process flow is built out of [governance action types](/concepts/governance-action-type).
    - Governance action processes are defined using the [Governance Engine OMAS](/services/omas/governance-engine/overview) API.
    - The [Open Metadata Engine Services (OMES)](/services/omes) provide the mechanisms that support the different types of [governance engines](/concepts/governance-engine). These engines run the [governance services](/concepts/governance-service) that execute the [governance actions](/concepts/governance-action) defined by the governance action process.


--8<-- "snippets/abbr.md"