<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0715 Digital Business

This model supports the description of the business domain where the digital product owners and consumers reside.

![UML](0715-Digital-Business.svg)


## BusinessCapability entity

*BusinessCapability* describes the business responsibility or services provided by a team in an organization.  It is linked to the owning team using the *CollectionMembership* relationship.

## BusinessCapabilityType enum

*BusinessCapabilityType* lists the broad categories of business capability.

* *BusinessService* - A functional business capability.
* *BusinessArea* - A collection of related business services.
* *BusinessDomain* - An overall area of activity in which a business operates.  A single organization may operate multiple business domains, such a retail, distribution, banking, ...


## BusinessCapabilityDependency relationship

Business domains can be modelled with nested business areas and business services. The *BusinessCapabilityDependency* relationship describes the dependency between two business capabilities. 

## DigitalSupport relationship

*DigitalSupport* describes the support provided by a digital service to a business capability.  The *supportedBusinessCapability* is supported by the *usesDigitalService* element that is typically an [Asset](/concepts/asset) or [DigitalProduct](/concepts/digital-product).

--8<-- "snippets/abbr.md"