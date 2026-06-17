<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# Notification Manager API

The Notification Manager API is a REST API designed to support the management of resource monitoring, the maintenance of the list of subscribers to that monitoring, and the notification of significant events or situations to the registered subscribers.  

It supports a personalized notification service.  This includes the definition of the trigger for the
notification, the style of notification and the recipient.

## Key Features

The Notification Manager API supports the following key features:

* **Monitored Resources**: Link notification types to the metadata elements that should be monitored for changes.
* **Notification Subscribers**: Define the recipients of notifications for specific notification types.

## Further information

* [Notification Type Concept](/concepts/notification-type/)

Sample requests for the REST API can be found in [Egeria-api-notification-manager.http](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/view-services/notification-manager/Egeria-api-notification-manager.http).
In addition:

* [Egeria-baudot-create-subscription.http](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/view-services/notification-manager/Egeria-baudot-create-subscription.http) shows how to create a subscription for an Open Metadata Digital Product.
* [Egeria-baudot-subscription-processes.http](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/view-services/notification-manager/Egeria-baudot-subscription-processes.http) shows the subscription processes for an Open Metadata Digital Product.
* [Egeria-notification-types-and-actions.http](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/view-services/notification-manager/Egeria-notification-types-and-actions.http) shows how to retrieve information about the notification types used in Egeria.

## Usage Examples

Examples of events that could trigger a notification include:

* The creation, update or delete of specific metadata elements.
* The creation, update or delete of specific types of metadata elements.
* The detection of an unauthorized user action.
* The completion of a process.
* The production of a particular type of audit log record.
* A timer expiring.

When the specific notification occurs, the resulting action could be:

* To create a user notification
* To create a ToDo for a user
* To initiate a governance action process 
* To create an incident report
* To create an event on a specific topic
* To call a remote API

## Notification Types 

The notification definitions are stored in Open Metadata using [Notification Types](/concepts/notification-type).  Attached to the notification type are the resources to monitor and the subscribers to be notified if/when significant event happens around the monitored resources.  Subscribers are typically [actors](/concepts/actor) or automated processes.


Egeria supports a number of monitoring agents called [watchdog action services](/concepts/watchdog-action-service) that are able to support the monitoring of open metadata events and subscribers that are either [actors](/concepts/actor) or [governance actions](/concepts/governance-action).

The Notification Manager API supports search, create, update, and delete of the following types of open metadata that supports notifications.

* *Notification Types*
* *Subscribers*
* *Monitored Resources*

It may be used by a subscriber wishing to change their subscriptions, or an external monitor that is using the Open Metadata definitions to configure its monitoring and notification processes.






---8<-- "snippets/abbr.md"






