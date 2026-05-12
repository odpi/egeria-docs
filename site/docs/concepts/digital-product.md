
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Digital Product

A *digital product* is a [collection](/concepts/collection) of [assets](/concepts/asset) that describe [digital resources](/concepts/digital-resources) designed to meet a specific consumer need.  The digital product adds licenses and terms of use along with service level agreements that you can rely on when using the data.  There is often a non-technical data specification describing the data supported by the digital product that links through to glossary terms. 

Users of digital products create a subscription to the digital product.  This creates an agreement between the product consumer and the product provider (product manager) that is two-way.  The provider promises to deliver the data at a certain frequency and quality level.  he consumer agrees to the associate terms of use.  The consumer can then use the data in their own applications, or digital products.

The digital subscriptions define how popular (valuable) a digital product and where it is being used.  THis can be used to guide investment decisions, both on the part of the product provider and the consumer.

Digital subscriptions can be cancelled at any time.  Whether the consumer can keep the data they have already received is defined in the terms of use.

## Digital product definitions

A digital product definition is modelled in open metadata using the [DigitalProduct](/types/7/0710-Digital-Products) type.  This is a specialized [collection](/concepts/collection) that is used to gather the asses and documentation for the product.

![Structure of a Digital Product](digital-product.svg)

Related digital products can be grouped into [digital product families](/types/7/0710-Digital-Products).  These are also specialized collections.  A product consumer can subscribe to a digital product family to receive the data from all the digital products in that family.


## Digital product lifecycle

A new product asset is typically created when there is new data to share.
A new product release is created when specification changes.
A restatement occurs when data values need correcting.

???+ info "API for managing digital products"

    * The [Product Manager API](/services/omvs/product-manager/overview) provides a specialist API for managing digital product definitions.  It partners with the [Collection Manager API](/services/omvs/collection-manager/overview) which manages the structural collections used by digital products.  The [Governance Officer API](/services/omvs/governance-officer/overview) manages the governance definitions (licenses, certifications, sevice level agreements, ...) associated with the digital products.
    * The [Product Catalog API](/services/omvs/product-catalog/overview) provides an API for querying the digital products plus the ability to subscribe and unsubscribe to them.

--8<-- "snippets/abbr.md"
