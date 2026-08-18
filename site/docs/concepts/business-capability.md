<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Business Capability

A *business capability* describes a function, a capability or a skill set that an organization has - or needs.  It answers the question *what does this organization do?* rather than *how is it organized?* or *what technology does it run?*

This distinction is what makes business capabilities useful.  Organizational structures are re-drawn regularly and systems are replaced, but the capabilities an organization needs in order to operate change far more slowly.  Describing the business in terms of its capabilities gives a stable frame that both the [teams](/concepts/team) that provide them and the [digital services](/practices/digital-services/overview) that support them can be attached to.

## Types of business capability

The *businessCapabilityType* property records the granularity of the capability:

* **Business domain** - an overall area of activity in which the business operates.  A single organization may run several, such as retail, distribution and banking.
* **Business area** - a collection of related business services within a domain.
* **Business service** - a single functional capability.

Business domains, areas and services are organized into a hierarchy using the *BusinessCapabilityDependency* relationship, which records the dependency between two business capabilities.

A business capability is a type of [collection](/concepts/collection), and the team that owns it is linked to it using the *CollectionMembership* relationship.

## Connecting the business to its digital estate

Business capabilities are the anchor point for the business context of technical metadata:

* The *DigitalSupport* relationship records that a [digital product](/concepts/digital-product) or [asset](/concepts/asset) supports a particular business capability.  This is what allows the question *if this system fails, what part of the business stops?* to be answered from the catalog.
* The *BusinessSignificance* classification marks a metadata element as significant to a specific business capability.
* The *AccountingCodes* classification attaches the accounting codes used to track the financial aspects of an element - a single *accountingCode*, an *accountingCodeList*, or an *accountingCodeMap* of name-to-code mappings for organizations with complex accounting structures.
* An [information supply chain](/concepts/information-supply-chain) can name the business capability that initiates or consumes each flow of data.
* The *DataScope* classification on a data store is often matched to a [data lens](/concepts/data-lens) defining the scope of data for a business capability.

???+ info "Additional information"
    * The *BusinessCapability* type, the *BusinessCapabilityType* enumeration and the related relationships and classifications are described in [Model 0715 Digital Business](/types/7/0715-Digital-Business).
    * The [Digital Business API](/services/omvs/digital-business/overview) provides the operations for defining business capabilities, linking them to the digital services that support them, and classifying elements with their business significance.

--8<-- "snippets/abbr.md"
