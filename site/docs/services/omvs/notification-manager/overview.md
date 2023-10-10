---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/in-development.md"

# Notification Manager OMVS

The Notification Manager Open Metadata View Services (OMVS) is a REST API designed to back user interfaces (UIs) that support the control of notifications.  These notifications define a specific trigger and the action to take.

Examples of triggers include:

* The creation, update or delete of specific metadata elements.
* The creation, update or delete of specific types of metadata elements.
* The detection of an unauthorized user action.
* The completion of a process.
* The production of a particular type of audit log record.

When the specific trigger occurs, the resulting action could be:

* To create a user notification
* To create a ToDo for a user
* To initiate a governance action process 
* To create an incident report
* To create an event on a specific topic
* To call a remote API

The notification definitions are defined and managed by the [Stewardship Action OMAS](/services/omas/stewardship-action/overview).

The Notification Manager OMVS calls the Stewardship Action OMAS to search for, create, update, and delete notification definitions.  Once these definitions are in place, the Stewardship Action OMAS begins monitoring for the requested events, and when they occur, it takes the appropriate actions.






---8<-- "snippets/abbr.md"






