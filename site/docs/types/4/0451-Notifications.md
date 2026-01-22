<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0451 Notifications

The *NotificationType* is a [GovernanceControl](/types/4/0420-Governance-Controls) that describes a situation or event.  It is linked to resources that need to be monitored in order to detect the situation and subscribers that need to know whenever the event/situation arises.

![UML](0451-Notifications.svg)

## NotificationType entity

The *NotificationType* entity describes a situation or event.  It is linked to resources that need to be monitored in order to detect the situation and subscribers that need to know with the event/situation arises.

## MonitoredResource relationship

The *MonitoredResource* relationship links a notification type to the resource (or resources) that need to be monitored to detect the event or situation that the notification type describes.

* *label* - the name of the monitored resource.
* *description* - additional information about the monitored resource.

## NotificationSubscriber relationship

The *NotificationSubscriber* links the notification type to the actors or actions that need to be performed if/when the situation/event described in the notification type occurs.

* *label* - the name of the notification subscriber.
* *description* - additional information about the notification subscriber.
* *activityStatus* - the status of the notification subscriber.
* *zoneMembership* - the zones that any notification sent to this notification subscriber should be tagged with.


--8<-- "snippets/abbr.md"