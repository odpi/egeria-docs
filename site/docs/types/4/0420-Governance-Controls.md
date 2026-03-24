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

       * [0423 Security Definitions](/types/4/0423-Security-Definitions) - describes governance controls that focus on protecting the organization.
       * [0424 Governance Zones](/types/4/0424-Governance-Zones) - describes security controls that control how access to a collection of metadata is controlled.
       * [0430 Development Controls](/types/4/0430-Development-Controls) - describes governance controls that that focus on fulfilling unmet needs of the organization through the development of technology.
       * [0440 Organizational Controls](/types/4/0440-Organizational-Controls) - identity governance roles and manual procedures (such as approvals) that implement a governance control.
       * [0450 Governance Rollout](/types/4/0450-Governance-Rollout) - describes governance controls that are used when rolling out a governance program to the organization.
       * [0451 Notifications](/types/4/0451-Notifications) - describes governance controls that are used to notify people of changes, schedules and events.
       * [0462 Governance Actions](/types/4/0462-Governance-Actions) - describes governance controls that are used to implement governance actions.

    Governance controls that are automatedare deployed into the IT landscape as software components and data assets.  The implementation of asuch a governance control (often called a technical control) can be identified by the [ImplementedBy](/types/7/0737-Solution-Implementation) relationship.  This may be directly to an [Asset](/types/0/0010-Base-Model) or to a [SolutionComponent](/types/7/0730-Solution-Components).  Alternatively, [Governance Execution Points](/types/4/0460-Governance-Execution-Points) can provide a more sophisticated mapping to the implementation, particularly where the implementation is distributed and requires the collaboration of multiple components to achieve the desired behaviour.


--8<-- "snippets/abbr.md"