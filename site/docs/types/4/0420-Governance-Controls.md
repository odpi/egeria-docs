<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0420 Governance Controls

Governance is enabled through People, Process and Technology. These are controlled through a combination of technical controls (implemented IT function) and organizational controls (training, responsibility, buddy-checking etc).

![UML](0420-Governance-Controls.svg)

## GovernanceControl entity

A *GovernanceControl* entity is a [GovernanceDefinition](/types/4/0401-Governance-Definitions) that describes how a particular [GovernancePolicy](/types/0415-Governance-Responses) should be implemented.  For example, there may be a governance principle that personal data is only available to people with a legitimate need to know.  One of the governance controls that support this principle could be the use of encryption on any storage device that holds personal data.  

A governance control definition is intended to act as a requirement to implementors.  So it may include details of the recommended encryption strength or approach to use.  However, it does not detail exactly how to enable encryption on different technologies, or which storage unit that it applies to.  The mapping of the governance control to the implementation is typically mapped through [Governance Execution Points](/types/4/0460-Governance-Execution-Points).  

## GovernanceMechanism relationship

A *GovernanceMechanism* relationship links a *GovernancePolicy* entity to a *GovernanceControl* entity that describes all or part of the implementation for the policy.  The `rationale` attribute describes why this implementation approach was chosen.

## GovernanceControlLink relationship

A *GovernanceControlLink* relationship links two related *GovernanceControl* entities together.  The `description` attribute describes the reason for the relationship.


!!! info "Further Information"

    * The [Governance Officer OMVS](/services/omvs/governance-officer/overview) provides support for defining governance definitions through its REST API. 

    * There is further detail on the content of the governance controls in the following models:

       * [0430 Technical Controls](/types/4/0430-Technical-Controls) - describes governance controls that typically are implemented as automations.
       * [0440 Organizational Controls](/types/4/0440-Organizational-Controls) - identity governance roles and manual procedures (such as approvals) that implement a governance control.


--8<-- "snippets/abbr.md"