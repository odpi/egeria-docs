<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0451 Notifications

The [NotificationType](/types/4/0430-Technical-Controls) describes a situation or event.  It is linked to resources that need to be monitored in order to detect the situation and subscribers that need to know whenever the event/situation arises.

![UML](0451-Notifications.svg)

## MonitoredResource relationship

The *MonitoredResource* relationship links a notification type to the resource (or resources) that need to be monitored to detect the event or situation that the notification type describes.

## NotificationSubscriber relationship

The *NotificationSubscriber* links the notification type to the actors or actions that need to be performed if/when the situation/event described in the notification type occurs.




--8<-- "snippets/abbr.md"