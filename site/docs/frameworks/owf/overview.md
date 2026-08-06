<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/tech-preview.md"

# Open Watchdog Framework (OWF)

The *Open Watchdog Framework (OWF)* defines the interfaces and base implementations for [watchdog action services](/concepts/watchdog-action-service) - specialized [connectors](/concepts/connector) that monitor the open metadata ecosystem for a specific situation or event and, when it occurs, notify the people, teams or processes that need to know.

OWF replaces the *watchdog governance action service* that used to be one of the five types of [governance action service](/frameworks/ogf/overview#governance-action-service) defined by the [Open Governance Framework (OGF)](/frameworks/ogf/overview).  The move is about setting clear expectations, not just tidying up the framework list.  OGF's remaining four types of governance action service - verification, triage, remediation and provisioning - are all designed to run as short, atomic actions: they start, do their work, and complete.  Watching for something to happen is fundamentally different in shape - a watchdog action service is expected to keep running for as long as the situation needs watching, which may be indefinitely.  Mixing a long-running listener in among services that are otherwise expected to finish quickly made it hard to tell, just from a governance service's type, what kind of lifecycle to expect from it.  Giving watchdog action services their own framework - and their own [engine service](#where-watchdog-action-services-run) - removes that ambiguity: a governance action service (OGF) is short-running, a watchdog action service (OWF) is long-running.

Having its own framework also lets watchdog action services do things that were awkward to fit into a short-running connector:

- Be described formally as a [*notification type*](#watching-through-a-notification-type), rather than only as configuration properties buried in a connector.
- Manage a durable, changing list of subscribers, rather than a fixed destination process.
- Run independently for as long as the situation needs watching, rather than as one step in a larger governance action process (although a watchdog action service can still trigger a governance action process when it detects something).

## Two ways to watch for something

A watchdog action service can be set up in either of two ways, matching the two [action target](#reference-data) types it recognizes.

### Watching an instance or type directly

The simplest form of monitoring points a watchdog action service at either a single metadata instance (element or relationship), or every instance of a particular open metadata type, and asks it to run a named [governance action process](/concepts/governance-action-process) whenever a particular kind of event occurs - a new element appearing, a property changing, a classification being added or removed, an element being deleted, and so on.  This is the pattern that the *watchdog governance action service* used before that capability moved into OWF:

--8<-- "snippets/connectors/watchdog-governance-action-service-intro.md"

The [Generic Element Watchdog :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/governance-action-connectors/docs/generic-element-watchdog-governance-action-service.md){ target=gh } and [Generic Folder Watchdog :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/governance-action-connectors/docs/generic-folder-watchdog-governance-action-service.md){ target=gh } governance action services are concrete, ready-to-configure examples of this pattern - the second is simply the first, pre-configured to watch a folder's `DataFile` assets.  Both accept a governance action process qualified name for each kind of event they should react to (see the [`WatchdogRequestParameter`](#reference-data) values below), and can either watch for a single occurrence and stop, or keep watching indefinitely.  They still run as OGF governance action services today, making them exactly the kind of long-running-in-a-short-running-framework case the OWF split is intended to resolve; new instance/type watching should be built directly against OWF's `WatchdogActionServiceConnector`, in the same way the [Baudot Subscription Manager](#watching-through-a-notification-type) already does for notification-type watching.

### Watching through a notification type

The richer form of monitoring is built around a [*NotificationType*](/types/4/0451-Notifications), an open metadata governance definition that formally describes:

- The resource, or resources, to monitor - linked via the *[MonitoredResource](/types/4/0451-Notifications#monitoredresource-relationship)* relationship.
- The subscribers that should be told when the situation occurs - linked via the *[NotificationSubscriber](/types/4/0451-Notifications#notificationsubscriber-relationship)* relationship.  A subscriber can hold more than one subscription to the same notification type at once, each independently tracked through its own [activity status](/types/0/0010-Base-Model).
- How often notifications should be sent - a single occurrence, a repeating interval (*notificationInterval*), or throttled so subscribers aren't overwhelmed (*minimumNotificationInterval*).

When the watchdog action service detects the situation the notification type describes, it works through the current subscribers and, for each one, creates a *[Notification](/types/1/0135-Actions-For-People#notification-entity)* - an action assigned to that subscriber describing what has happened.  A subscriber's relationship to the notification type is updated as this happens, so it is always possible to see who has been told, and who hasn't.

This pattern is deliberately more stateful than instance/type watching: a notification type persists as metadata in its own right, subscribers can be added and removed from it at any time (by people or by other governance processes), and the watchdog action service that services it is really managing an ongoing subscription list rather than reacting to a one-off event.

The [Baudot Subscription Manager :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/nanny-connectors/README.md#baudot-subscription-manager){ target=gh } is a production example of this pattern - it manages subscriptions to the digital products in the [Open Metadata Digital Product Catalog](/types/7/0710-Digital-Products).  It is passed the notification types to service as action targets, is designed to run indefinitely rather than complete, and uses each notification type's `multipleNotificationsPermitted` and `notificationInterval` properties to decide, per notification type, whether to send a single one-time notification, notify subscribers whenever a monitored product changes, or notify them on a fixed schedule.  It also watches the *NotificationSubscriber* relationship itself, so subscribers are welcomed and dismissed automatically as they subscribe and unsubscribe, and the *ActionTarget* relationship, so a new notification type can be added to a running instance without needing to restart it.


## Watchdog Action Service

A watchdog action service is implemented as a specialized connector that is passed a [*watchdog context*](#watchdog-context) as part of its initialization.  Its job, once started, is to register interest in the events it cares about and then process each one as it arrives - continuing to do so until it declares itself complete, or is stopped by an administrator.

The types of events a watchdog action service receives are controlled by up to three filters, combined together: the types of event (new element, updated element, deleted relationship, and so on), the open metadata types of the elements/relationships involved, and, optionally, a single specific instance to watch.  Only one set of filters can be active at a time, but a watchdog action service can change them while it is running - for example, switching what it is watching for part way through, or after it finishes with one notification type and moves on to the next.


## Watchdog Context

The *watchdog context* gives the watchdog action service access to information about the request, along with the open metadata repository interfaces it needs to do its work.

Like the [request parameters and action targets](#reference-data) used by other kinds of governance service, the context provides the request type, request parameters, action target elements and requesting user for this run of the service.

For notification-type-based monitoring, the context provides:

| Method | Purpose |
|---|---|
| `getNotificationTypesFromActionTargets()` | Extract the notification types passed in as action targets, ignoring any that are not in an active state. |
| `getNotificationType()` / `updateNotificationType()` | Retrieve or update the details of a specific notification type. |
| `getMonitoredResources()` | Retrieve the resources linked to a notification type via *MonitoredResource*. |
| `getNotificationSubscribers()` | Retrieve the actors currently linked to a notification type via *NotificationSubscriber*. |
| `welcomeSubscriber()` / `welcomeMonitoringSubscribers()` | Send the first notification to a new subscriber (or all of them) when they join. |
| `notifyMonitoringSubscribers()` | Notify subscribers each time the monitored situation occurs. |
| `notifyPeriodicSubscribers()` | Notify subscribers because a scheduled interval has elapsed, rather than because of a specific event. |
| `notifyOneTimeSubscribers()` | Send a single notification and mark the subscription as complete. |
| `dismissSubscriber()` / `dismissSubscribers()` | Notify a subscriber (or all of them) that the subscription has ended, for example because the notification type is no longer valid. |

For instance/type monitoring, the context provides a lower-level `registerListener()`/`disconnectListener()` pair that lets the watchdog action service supply its own listener along with the combination of event types, metadata types and (optionally) a specific instance it wants to hear about.

In both cases, the watchdog action service finishes by calling `recordCompletionStatus()`, in the same pattern used across Egeria's governance services - supplying a completion status, any output guards, and optionally new request parameters or action targets to pass on to whatever runs next.


## Reference data

Every watchdog action service automatically supports the following action targets, request parameters and guards, defined by the OWF so that watchdog action services stay consistent with one another.  A specific watchdog action service may support additional ones of its own.

### Action targets

| Action Target | Description |
|---|---|
| `notificationType` | The notification type that the watchdog action service should monitor. |
| `instanceToMonitor` | Requests that the watchdog action service monitors a single metadata instance directly, as an alternative to using a notification type. |

### Request parameters

These are used with instance/type monitoring, to describe what to watch for and what to do about it.

| Request Parameter | Description |
|---|---|
| `instanceToMonitor` | Requests that the watchdog action service monitors a single metadata instance. |
| `interestingTypeName` | Defines the type of element that this monitor is focused on. |
| `actionTargetName` / `actionTargetNameTwo` | Override the action target name(s) used for the element(s) involved in the detected event.  Default to `receivedElement` and `receivedElementTwo`. |
| `newElementProcessName` | Governance action process to run when a new element is detected. |
| `updatedElementProcessName` | Governance action process to run when an element's properties change. |
| `deletedElementProcessName` | Governance action process to run when an element is deleted. |
| `classifiedElementProcessName` | Governance action process to run when a classification is added to an element. |
| `reclassifiedElementProcessName` | Governance action process to run when a classification's properties change. |
| `declassifiedElementProcessName` | Governance action process to run when a classification is removed. |
| `newRelationshipProcessName` | Governance action process to run when a new relationship is detected. |
| `updatedRelationshipProcessName` | Governance action process to run when a relationship's properties change. |
| `deletedRelationshipProcessName` | Governance action process to run when a relationship is deleted. |
| `ChangedProperties` | A comma-separated list of the property names that changed, added to the request parameters passed on to whichever process is triggered. |

A process name that is not set means that kind of event is simply ignored.

### Guards

| Guard | Completion Status | Meaning |
|---|---|---|
| `monitoring-completed` | ACTIONED | The monitoring completed successfully. |
| `monitoring-invalid` | INVALID | The watchdog did not run because the supplied information (such as the notification type) is invalid for this type of watchdog. |
| `monitoring-failed` | FAILED | An unexpected error occurred during monitoring; the notification process is incomplete. |


## Where watchdog action services run

Watchdog action services run in a [watchdog action engine](/concepts/watchdog-action-engine), hosted by the [Watchdog Action OMES](/services/omes/watchdog-action/overview) running in an [Engine Host](/concepts/engine-host) - the same overall pattern used by [survey action services](/frameworks/osf/overview) and [governance action services](/frameworks/ogf/overview).  The Watchdog Action OMES provides a REST API to request that a watchdog action engine starts a watchdog action service and to check on its results; the engine itself calls back into a Metadata Access Server to read about the resources being monitored and to record the notifications it sends.


## Implementation in Egeria

OWF is implemented in the [open-watchdog-framework :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/frameworks/open-watchdog-framework){ target=gh } module.  The base connector class is `WatchdogActionServiceConnector`; it is passed a `WatchdogContext` and implements a single abstract method, `processEvent()`, that is called once for each matching event.

The open metadata types that support notification-based monitoring - *NotificationType*, *MonitoredResource* and *NotificationSubscriber* - are described in [0451 Notifications](/types/4/0451-Notifications).  The *Notification* entity that is created for each subscriber is described in [0135 Actions for People](/types/1/0135-Actions-For-People#notification-entity).

--8<-- "snippets/abbr.md"
