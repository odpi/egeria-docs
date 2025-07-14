<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0420 Governance Controls

Governance is enabled through People, Process and Technology. These are controlled through a combination of technical controls (implemented IT function) and organizational controls (training, responsibility, buddy-checking etc).

![UML](0420-Governance-Controls.svg)

## GovernanceControl entity

A *GovernanceControl* entity is a [GovernanceDefinition](/types/4/0401-Governance-Definitions) that describes how a particular [GovernancePolicy](/types/0415-Governance-Responses) should be implemented.  For example, there may be a governance principle that personal data is only available to people with a legitimate need to know.  One of the governance controls that support this principle could be the use of encryption on any storage device that holds personal data.  

A governance control definition is intended to act as a requirement to implementors.  So it may include details of the recommended encryption strength or approach to use.  However, it does not detail exactly how to enable encryption on different technologies, or which storage unit that it applies to.  The mapping of the governance control to the implementation is typically mapped through [Governance Execution Points](/types/4/0460-Governance-Execution-Points).  

## GovernanceImplementation relationship

A *GovernanceImplementation* relationship links a *GovernancePolicy* entity to a *GovernanceControl* entity that is implement all or part of the policy.  The `rationale` attribute describes why this implementation approach was chosen.

## GovernanceControlLink relationship

A *GovernanceControlLink* relationship links two related *GovernanceControl* entities together.  The `description` attribute describes the reason for the relationship.

## TechnicalControl entity

A *TechnicalControl* entity is a type of *GovernanceControl* that is automated using technology.  More information on technical controls can be found in [model 0430](/types/4/0430-Technical-Controls).

## OrganizationalControl entity

An *OrganizationalControl* entity is a type of *GovernanceControl* that is implemented as a manual process or a set of responsibilities linked to an individual, role or team.  More information on organizational controls can be found in [model 0440](/types/4/0440-Organizational-Controls).

## GovernanceResponsibility entity

*GovernanceResponsibility* describes a responsibility that is assigned to a person or team.  It could be a requirement to take certain action in specific circumstances, or to make particular types of decisions or to give approvals for particular actions.

## GovernanceProcedure entity

*GovernanceProcedure* describes a manual procedure that is performed under certain situations.  An example would be a visual check of a person's government identity document such as a passport or driving license.

!!! info "Further Information"

    * The [Governance Officer OMVS](/services/omvs/governance-officer/overview) provides support for defining governance policies through its REST API. 

    * There is further detail on the content of the governance controls in the following models:

       * [0430 Technical Controls](/types/4/0430-Technical-Controls) - describe automated behaviour that implements a governance control.
         * [0423 Security Definitions](/types/4/0423-Security-Definitions) - defines access control rules.
         * [0438 Naming Standards](/types/4/0438-Naming-Standards) - defines naming standard rules.
         * [0461 Governance Engines](/types/4/0461-Governance-Engines) - support the execution of technical controls.
         * [0462 Governance Action Processes](/types/4/0462-Governance-Action-Processes) - provide the choreography of the execution of technical controls.
       * [0440 Organizational Controls](/types/4/0440-Organizational-Controls) - identity governance roles and manual procedures (such as approvals) that implement a governance control.
         * [0445 Governance Roles](/types/4/0445-Governance-Roles) - define governance roles and the people associated with them.
    
    * [Governance Execution Points](/types/4/0460-Governance-Execution-Points) - describe classifications for software components that link them to a governance control.


--8<-- "snippets/abbr.md"