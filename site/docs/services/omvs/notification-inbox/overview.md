---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/in-development.md"

# Notification Inbox OMVS

The Notification Inbox Open Metadata View Services (OMVS) is a REST API designed to back user interfaces (UIs) that support notification for a specific user.

The notifications are defined and managed by the [Stewardship Action OMAS](/services/omas/stewardship-action/overview).

The Notification Inbox OMVS calls the Stewardship Action OMAS to retrieve the list of user notifications for the calling user.  

Each user notification has a status, summary description and a link to one or more elements that the notification refers to.  For example, a notification may indicate that:

* New data is available for a digital product that the user is watching.
* A new To Do for the user has been created.
* An asynchronous process initiated by the user has finished.

The user can view the details of the notification, change the status of the notification, or delete it.


---8<-- "snippets/abbr.md"






