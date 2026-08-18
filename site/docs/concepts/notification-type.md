<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Notification Type

A *notification type* is the definition of a situation that should be detected and acted upon.  It is a [governance definition](/concepts/governance-definition) - specifically a governance control - which means the reason a notification exists is traceable back to the governance driver or policy that called for it.

A notification type brings together three things:

* **What to watch** - the *MonitoredResource* relationship links the notification type to the metadata elements that need to be monitored in order to detect the situation.
* **What the situation is** - described by the notification type itself.
* **Who needs to know** - the *NotificationSubscriber* relationship links the notification type to the [actors](/concepts/actor) or actions that should be triggered when the situation arises.

## Detecting the situation

Egeria's [watchdog action services](/concepts/watchdog-action-service) are the monitoring agents that detect changes in open metadata and evaluate them against the notification types.  An external monitor can equally read these definitions and configure its own monitoring, which means the same notification definitions drive detection wherever it happens.

Situations that typically warrant a notification type include:

* The creation, update or deletion of a specific metadata element, or of any element of a particular type.
* The detection of an unauthorized user action.
* The completion of a [process](/concepts/process).
* The production of a particular type of [audit log](/concepts/audit-log) record.
* A timer expiring.

## Acting on the situation

Each subscriber decides what happens next.  The response may be to create a user notification or a [to do](/concepts/to-do) for a person, to initiate a [governance action process](/concepts/governance-action-process), to raise an [incident report](/concepts/incident-report), to publish an event on a topic, or to call a remote API.

The *NotificationSubscriber* relationship is a [multi-link](/concepts/uni-multi-link) relationship, so the same subscriber can hold several subscriptions to one notification type - typically with only one of them active at a time, and the others held in a different state ready to be switched on.

## Controlling the flow of notifications

Left unchecked, a monitored situation that recurs frequently produces a flood of notifications that recipients quickly learn to ignore.  The notification type therefore carries properties that shape the delivery:

* *multipleNotificationsPermitted* - whether more than one notification should be sent when the situation recurs.
* *minimumNotificationInterval* - the shortest permitted gap between notifications.
* *notificationInterval* and *nextScheduledNotification* - used for periodic subscriptions, where notifications are sent on a schedule rather than being driven by a monitored resource.
* *notificationCount* - how many notifications have been triggered.
* *plannedStartDate* and *plannedCompletionDate* - the period during which the notification type is intended to be active.

???+ info "Additional information"
    * The *NotificationType* type and its relationships are described in [Model 0451 Notifications](/types/4/0451-Notifications).
    * The [Notification Manager API](/services/omvs/notification-manager/overview) provides the operations for maintaining notification types, their monitored resources and their subscribers.

--8<-- "snippets/abbr.md"
