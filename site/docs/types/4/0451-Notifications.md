<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0451 Notifications

The *NotificationType* is a [GovernanceControl](/types/4/0420-Governance-Controls) that describes a situation or event.  It is linked to resources that need to be monitored in order to detect the situation and subscribers that need to know whenever the event/situation arises.

![UML](0451-Notifications.svg)

## NotificationType entity

The *NotificationType* entity describes a situation or event.  It is linked to resources that need to be monitored to detect the situation and subscribers that need to know with the event/situation arises.

* *plannedStartDate* - the date that the notification type is planned to become active.
* *multipleNotificationsPermitted* - flag to indicate whether multiple notifications should be sent to the notification subscribers when the situation/event occurs.
* *minimumNotificationInterval* - the minimum time between notifications that should be sent to the notification subscribers when the situation/event occurs.
* *notificationInterval* - the time between notifications that should be sent to the notification subscribers. Used for periodic subscriptions.
* *nextScheduledNotification* - the time when the next notification is expected. Used for periodic subscriptions.  Will be null if one or more resources are being monitored.
* *notificationCount* - the number of notifications that have been triggered. The notification is sent only to the notification subscribers that are in the correct state.
* *plannedCompletionDate* - the date that the notification type is planned to become inactive.

## MonitoredResource relationship

The *MonitoredResource* relationship links a notification type to the resource (or resources) that need to be monitored to detect the event or situation that the notification type describes.

* *label* - the name of the monitored resource.
* *description* - additional information about the monitored resource.

## NotificationSubscriber relationship

The *NotificationSubscriber* relationship links the notification type to the actors or actions that need to be performed if/when the situation/event described in the notification type occurs.

* *label* - the name of the notification subscriber.
* *description* - additional information about the notification subscriber.
* *activityStatus* - the status of the notification subscriber.
* *zoneMembership* - the zones that any notification sent to this notification subscriber should be tagged with.

Notice that the *NotificationSubscriber* relationship is a [multi-link](/concepts/uni-multi-link) relationships which allows a subscriber to have multiple subscriptions to the same notification type.  Each of these subscriptions would be in a different state with typically only one in an active state.


--8<-- "snippets/abbr.md"