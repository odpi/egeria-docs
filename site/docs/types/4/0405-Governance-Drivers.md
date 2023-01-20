<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0405 Governance Drivers

Governance drivers define the motivations behind the governance program.  Often they show both the business opportunities and the constraints that must guide the organization's activity.

![UML](0405-Governance-Drivers.svg)

## GovernanceDriver

The *GovernanceDriver* entity is the common super type for the governance drivers.

## GovernanceStrategy

The *GovernanceStrategy* entity defines the strategy used in the development of the governance domain's activities.
It defines how the governance domain supports the business strategy.

## BusinessImperative

The *BusinessImperative* entity defines a business goal that is critical to the success of the organization.

## Regulation

The *Regulation* entity defines a relevant legal regulation that the business operation must comply with.  Often regulations are divided in regulation articles.

## RegulationArticle

A *RegulationArticle* entity is an article in a regulation.  Dividing the regulation into articles can help in planning to comply and reporting on the effectiveness of the associated activities.

## Threat

The *Threat* entity describes a particular threat to the organization's operations that must either be guarded against or some for of mitigation must be in place to reduce its impact.

## GovernanceDriverLink

The *GovernanceDriverLink* relationship is used to link related governance drivers together.  THe *description* described the relationship.

## Related Information

* Governance Drivers are types of *GovernanceDefinitions* which are located in model [0401](/types/4/0401-Governance-Definitions).

* The [Governance Program OMAS](/services/omas/governance-program/overview)
  provides support for defining governance drivers through its **GovernanceDriversInterface**. 

--8<-- "snippets/abbr.md"