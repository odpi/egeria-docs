<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0712 Digital Subscription

A digital subscription is an agreement by a producer of a digital artifact (typically a [DigitalProduct](/types/7/0710-Digital-Service)) to deliver it to a consumer at an agreed time and quality.

![UML](0712-Digital-Subscription.svg)

## DigitalSubscription

The *DigitalSubscription* entity is a specialized [Agreement](/types/7/0711-Agreements) for a subscription to a [Digital Service](/types/7/0710-Digital-Service), [Digital Product](/types/7/0710-Digital-Service) or [Asset](/types/0/0010-Base-Model).  The [AgreementItem](/types/7/0711-Agreements) relationship links the *DigitalSubscription* entity to the element being subscribed to.

## DigitalSubscriber

The *DigitalSubscriber* relationship links to the element that represents the subscriber.  For example, this could be a [UserIdentifier](/types/1/0110-Actors), [PersonRole](/types/1/0112-People), [ActorProfile](/types/1/0110-Actors) or [Asset](/types/0/0010-Base-Model) such as a system.




--8<-- "snippets/abbr.md"