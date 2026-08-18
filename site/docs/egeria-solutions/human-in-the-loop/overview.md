<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Human in the loop

Automation can catalogue, survey, classify, provision and monitor.  What it cannot do is make the judgement calls: whether these two records really are the same customer, whether this data set may be released, whether an unexpected survey result is a problem or a quirk.  Those need a person - and the person needs to find out that they are needed, understand the situation well enough to decide, and have their decision picked up by the process that was waiting.

Getting that loop to work is the difference between automation that scales and automation that stalls.

## People need to see what is happening

The first half of the loop is visibility.  Egeria's [user interfaces](/user-interfaces) present both the structural picture and the operational one.

**The structural picture** - what exists and how it fits together:

* [The Catalog](/user-interfaces/the-catalog/overview) for the inventories of infrastructure, data assets, APIs and processes.
* [Egeria Explorer](/user-interfaces/egeria-explorer/overview) for the wider knowledge graph, including the type system and the valid value sets behind it.
* [Lineage Explorer](/user-interfaces/lineage-explorer/overview) for where data came from and where it goes.
* [Mermaid graphs](/user-interfaces/mermaid/overview), generated from the metadata itself, so a diagram is never out of date with what it describes.

**The operational picture** - what the ecosystem is doing right now:

* [Egeria Operations](/user-interfaces/egeria-operations/overview) shows the status of servers, connectors, governance engines and engine actions, and supports simple commands such as refresh, restart and cancel.
* [Egeria Audit](/user-interfaces/egeria-audit/overview) shows exceptions, certifications, licenses and users.
* [My Egeria](/user-interfaces/my-egeria/overview) gives an individual their own view: their to-dos, meetings, reviews, roles, communities and teams, as either a terminal or browser application.

Being able to see both matters more than it sounds.  A person asked to make a decision needs the structural context to understand what they are deciding about, and the operational context to know whether what they are looking at is current.

## Automation needs to reach people

The second half of the loop is the outbound call - and it has a range, not a single mechanism.  What is appropriate depends on how much the automation needs from the person.

| Mechanism | What it asks of the recipient | Does the process wait? |
|-----------|-------------------------------|------------------------|
| [Notification](/concepts/notification) | Read this.  Any action is the recipient's choice. | No |
| Notification type and subscription | Tell me when this kind of thing happens to something I care about. | No |
| [Request for action](/concepts/request-for-action) | A survey found something that needs looking at. | Not usually |
| [To-do](/concepts/to-do) | Do this specific thing, by this time. | Often yes |
| [Incident report](/features/incident-reporting/overview) | Coordinate with others to resolve a situation. | Yes |

A [notification](/concepts/notification) is simply a record to be read, organized into a note log - an activity log entry, a blog entry, a journal entry.  Nothing depends on the reader doing anything.

A **notification type** goes further: it defines the trigger, the style of notification and the recipient, so people subscribe to the situations they care about instead of watching everything.  This is managed through the [Notification Manager](/services/omvs/notification-manager/overview) API, which links notification types to the elements being monitored and maintains the list of subscribers.  The graph below shows an engine action doing exactly this - a watchdog service maintaining the notification types for every subscription in the digital product catalog:

--8<-- "snippets/actions/baudot-subscription-manager-(egeriawatchdog)-mermaid-graph.md"

A **[to-do](/concepts/to-do)** is the strong form: a work item with a description, a priority, a due date and a status that moves from *requested* through *in progress* to *complete*.  It has an originator - which may be a person or a [governance action process](/concepts/governance-action-process) - and it is assigned to a [role](/concepts/person-role) rather than directly to an individual, so the work survives someone changing jobs or going on leave.  When automation raises a to-do, it is usually because it cannot proceed until the work is done.

An **[incident report](/features/incident-reporting/overview)** is for situations rather than tasks: it provides a focal point for coordinating a response, accumulating the cause, the affected resources, related incidents and the actions taken, so there is a complete record afterwards.

## Closing the loop

An individual has no REST API to call.  So the pattern is always the same: the automation records what it needs and notifies someone; the person investigates through the user interfaces, makes the change through the APIs or a connected tool; the automation sees the change and continues.

This is described in more detail under [working with people](/features/people-roles-organizations/overview/#working-with-people), and it is the basis of *stewardship*: [survey action services](/concepts/survey-action-service) produce findings, and rather than applying every finding blindly, the significant ones are put in front of a subject-matter expert who confirms or rejects them.  Even when human validation is required, the effort is far smaller than doing the work by hand - the person is reviewing a candidate answer rather than producing one.

Two things make this practical at scale:

* **Assignment to roles, not people.**  Because responsibilities are held as [roles](/patterns/organization-engagement/overview) with appointees, automation can address the *responsibility* and let the organization decide who currently holds it.
* **A record of what was decided.**  The to-do, its status and the change that resulted are all in the metadata, so a decision made under time pressure can be explained later.

## The same mechanisms serve AI

Automation connected to Egeria is no longer only Egeria's own governance engines.  AI applications working through Egeria's APIs participate in the same loop: they read the structural and operational context from the knowledge graph, and they raise the same range of notifications and work items when they need a person - whether that is an informational message, or a decision the application is waiting on before it acts.

Keeping people addressable in the same way as any other participant is what allows an organization to add AI to a process without losing the ability to say who approved what.

!!! info "Related information"

    * [To do](/concepts/to-do), [notification](/concepts/notification) and [request for action](/concepts/request-for-action) concepts.
    * [Notification Manager](/services/omvs/notification-manager/overview) API - monitored resources, subscribers and notification types.
    * [Incident reporting](/features/incident-reporting/overview) - coordinating a response to a situation.
    * [Active Governance](/patterns/active-governance/overview) - the automation that raises this work in the first place.
    * [Organization Engagement](/patterns/organization-engagement/overview) - roles, communities and the people the automation is calling on.

--8<-- "snippets/abbr.md"
