<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# My Profile API

The My Profile API provides a REST API to support user interfaces (UIs)
relating to the maintenance of a user's personal profile as well as tracking their actions,
responsibilities and activities.

## Key Features

The My Profile API supports the following key features:

* **Personal Profile Management**: Retrieve and maintain the personal profile of the logged-on user.
* **Action Tracking**: Track actions that have been assigned to, sponsored by, or requested by the user.
* **Roles and Responsibilities**: Retrieve the user identities, actor profiles, roles, and resources
  associated with the user.
* **Activity Logging**: Maintain a record of the user's activity through activity logs, journals, and blogs.

## Further information

* [Personal Profile Concept](/concepts/personal-profile/)
* [Action Concept](/concepts/action/)

Sample requests for the REST API can be found in [Egeria-api-my-profile.http](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/view-services/my-profile/Egeria-api-my-profile.http).

## API Overview

The *My Profile API* supports personalization in the open metadata ecosystem. At the heart of personalization is the [personal profile](/concepts/personal-profile) that describes an individual with details such as their name, job role and contact details.  The personal profile then becomes the parent node where the individual can attach and maintain collections of favourite elements such as assets, projects and links to the profiles of other people in their network.  User interfaces, connectors and other services can use this information to provide special service to the individual.

### Retrieving the personal profile

This service only has one operation called *getMyProfile*.  It extracts the user identity (aka userId or username) from the bearer token and looks up/returns the personal profile for that user.  The returned profile includes all of the caller's existing roles, userIds, contact details and peers associated with the profile.  This information supplies the necessary GUIDs to work with other APIs such as Actor Manager, Collection Manager and Asset Maker to build out a rich personal profile.

### Setting up a personal profile

If nothing is returned from *getMyProfile* it means you do not have a personal profile.  Use the *addMyProfile* operation to create one.

### Notification Inbox

The Notification Inbox is a feature of My Profile API designed to back user interfaces (UIs) that support notification for a specific user.

Each user notification, also known as an [action](/concepts/action), has a status, summary description and a link to one or more elements that the notification refers to.  For example, a notification may indicate that:

* New data is available for a digital product that the user is watching.
* A new action for the user has been created.
* An asynchronous process initiated by the user has finished.

The user can view the details of the notification, change the status of the notification, or delete it.




---8<-- "snippets/abbr.md"






