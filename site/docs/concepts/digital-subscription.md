<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Digital Subscription

A *digital subscription* is the agreement that is created when a consumer subscribes to a [digital product](/concepts/digital-product) - or to any other digital service or [asset](/concepts/asset) that is offered for subscription.

The subscription is a two-way arrangement.  The provider commits to delivering the data at an agreed frequency and quality; the subscriber accepts the product's terms of use, licences and any restrictions on what may be done with the data once it has been received.  Because both sides of the arrangement are recorded in open metadata, the commitment is visible, auditable and can be acted on by automated processes.

## What a subscription records

* **What is being delivered** - the *AgreementItem* relationship links the subscription to the digital product, digital service or asset being subscribed to.  A subscription to a *digital product family* delivers the data from every product in that family.
* **Who the subscriber is** - the *DigitalSubscriber* relationship links to the element representing the consumer.  This may be a [user identity](/concepts/user-identity), an [actor profile](/concepts/actor-profile), an [actor role](/concepts/actor-role) or an asset such as the system that will receive the data.
* **The service level offered** - the subscription names the commitment the provider is making.  A product typically offers a choice, ranging from a one-off delivery for evaluation, through a daily or weekly refresh, to a continuous feed where updates reach the destination within a fixed interval.
* **Where the data is to be delivered** - the subscriber names the destination, which may be a file, a database table or a topic.
* **The terms and conditions** - attached as [governance definitions](/concepts/governance-definition) using the *GovernedBy* relationship.

Since a digital subscription is a type of [collection](/concepts/collection), any additional supporting material - such as the [data specification](/concepts/data-specification) for the data being delivered - can be gathered inside it.

## Subscriptions as a measure of value

The set of active subscriptions to a product shows how popular it is and where its data has spread to.  This is one of the more valuable by-products of running a product catalog: it guides investment decisions on both sides, and it means that when a product has to change, the provider knows exactly who to tell.

Subscriptions can be cancelled at any time.  Whether the consumer may keep the data they have already received is determined by the product's terms of use rather than by the subscription itself.

Creating and cancelling a subscription are normally run as [governance actions](/concepts/governance-action), so the delivery is set up, recorded and torn down consistently.

???+ info "Additional information"
    * The *DigitalSubscription* type and the *DigitalSubscriber* relationship are described in [Model 0712 Digital Subscription](/types/7/0712-Digital-Subscription).  It is a specialization of the *Agreement* type described in [Model 0711 Agreements](/types/7/0711-Agreements).
    * The [Product Catalog API](/services/omvs/product-catalog/overview) is used by consumers to browse products and to request and manage their subscriptions.
    * The [Product Manager API](/services/omvs/product-manager/overview) is used by product managers to define the products and the subscription types they offer.
    * The [harvest and publish pattern](/patterns/harvest-and-publish/overview) shows subscriptions in use, delivering Egeria's own metadata as digital products.

--8<-- "snippets/abbr.md"
