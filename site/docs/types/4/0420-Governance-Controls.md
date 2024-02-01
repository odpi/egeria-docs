<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0420 Governance Controls

Governance is enabled through People, Process and Technology. These are controlled through a combination of technical controls (implemented IT function) and organizational controls (training, responsibility, buddy-checking etc).

![UML](0420-Governance-Controls.svg)

## GovernanceControl entity

A *GovernanceControl* entity describes how a particular [GovernancePolicy](/types/0415-Governance-Responses) is implemented.  It is a type of [GovernanceDefinition](/types/4/0401-Governance-Definitions) that is linked to the element it is controlling using the [GovernedBy](/types/4/0401-Governance-definitions) relationship.

## GovernanceImplementation relationship

A *GovernanceImplementation* relationship links a *GovernancePolicy* entity to a *GovernanceControl* entity that is implement all or part of the policy.  The `rationale` attribute describes why this implementation approach was chosen.

## GovernanceControlLink relationship

A *GovernanceControlLink* relationship links two related *GovernanceControl* entities together.  The `description` attribute describes the reason for the relationship.

## TechnicalControl entity

A *TechnicalControl* entity is a type of *GovernanceControl* that is automated using technology.

## OrganizationalControl entity

An *OrganizationalControl* entity is a type of *GovernanceControl* that is implemented as a manual process or a set of responsibilities linked to an individual, role or team.

!!! info "Further Information"

    * Governance controls are types of [*GovernanceDefinitions*](/concepts/governance-definition) which are located in model [0401](/types/4/0401-Governance-Definitions). The governance policies are defined in model [0415](/types/4/0415-Governance-Responses).

    * The [Governance Program OMAS](/services/omas/governance-program/overview) provides support for defining governance policies through its *GovernanceDefinitionsInterface*. 

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