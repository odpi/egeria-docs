<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0415 Governance Responses

Governance policies outline how a governance domain will provide support to the [governance drivers](/types/4/0405-Governance-Drivers).  They are said to be the "responses to the challenges proposed by the governance drivers".

Governance policies are written in language that describes the desired end state or method of working.  They also describe the costs and benefits of achieving this end state and other related consequences.  They are further refined using [governance controls](/types/4//0420-Governance-Controls) that define specific actions in specific situations.

![UML](0415-Governance-Responses.svg)

## GovernancePolicy

The *GovernancePolicy* entity is a type of [*GovernanceDefinition*](/types/4/0401-Governance-Definitions).

There are three main types of policy:

* Principles define the overall values and guidelines for the organization.
* Obligations define specific actions or processing that must be accommodated.
* Approaches define best practices for how a resource should be implemented and managed.

## GovernancePrinciple

The *GovernancePrinciple* entity defines a policy that describes an end state that the organization aims to achieve.  

## GovernanceObligation

The *GovernanceObligation* entity defines a policy that describes a requirement, often coming from regulations, or from the organization's core values, that must be met.

## GovernanceApproach

The *GovernanceObligation* entity defines a policy that describes a method that should be used for a particular activity.

## GovernanceResponse

The *GovernanceResponse* relationship links a GovernanceDriver entity to a GovernancePolicy entity to show that following the policy will help to support the governance driver.

## GovernancePolicyLink

The *GovernancePolicyLink* relationship connects two related *GovernancePolicy* entities.

!!! info "Further Information"
    The [Governance Program OMAS](/services/omas/governance-program/overview) provides support for defining governance policies through its **GovernancePolicyMakingInterface**. 

--8<-- "snippets/abbr.md"