<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0715 Digital Business

This model supports the description of the business domain where the digital product owners and consumers reside.

![UML](0715-Digital-Business.svg)


## BusinessCapability entity

*BusinessCapability* describes the business responsibility or services provided by a team in an organization.  It is linked to the owning team using the *BusinessCapabilityTeam* relationship.

## BusinessCapabilityType enum

*BusinessCapabilityType* lists the broad categories of business capability.

## Organization entity

*Organization* represents the root of an organization. It inherits from [Team](/types/1/0115-Teams) so that the organization structure can be built underneath it using the [TeamStructure](/types/1/0115-Teams) relationship.

## BusinessCapabilityTeam relationship


## DigitalSupport relationship


--8<-- "snippets/abbr.md"