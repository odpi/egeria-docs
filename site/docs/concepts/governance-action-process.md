<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Governance Action Process

A governance action process is a predefined sequence of [governance actions](/egeria-docs/concepts/governance-action) that are coordinated by the [Governance Engine OMAS](/egeria-docs/services/omas/governance-engine/overview).

The steps in a governance action process are defined by linked [governance action types](/egeria-docs/concepts/governance-action-type).  Each governance action type provides the specification of the governance action to run.  The links between then show which guards cause the governance action to run.

## Examples

![Example 1](governance-action-process-example-1.svg)
![Example 2](governance-action-process-example-2.svg)

Details of how to set up governance action process is described in the 
[Governance Engine OMAS User Guide](../services/omas/governance-engine/user).


## Open metadata types

[0462 Governance Action Types](/egeria-docs/types/4/0462-Governance-Action-Types)
shows the structure of the incident report.
It is a [Referenceable](/egeria-docs/types/0//0010-Base-Model)
so it can support comments and have [governance actions](/egeria-docs/concepts/governance-action) linked to it.

## Further information

* The [Open Metadata Engine Services (OMES)](/egeria-docs/services/omes) provide the mechanisms
  that support the different types of [governance engines](/egeria-docs/concepts/governance-engine).  These engines run the [governance services](/egeria-docs/concepts/governance-service) that execute the [governance actions](/egeria-docs/concepts/governance-action) defined by the governance action process.
 
 

--8<-- "snippets/abbr.md"