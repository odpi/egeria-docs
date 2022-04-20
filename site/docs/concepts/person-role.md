---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Person Role

A person role is a placeholder in a [team](/features/people-roles-organizations) that defines a set of skills and responsibilities that one or more individuals can perform.


Individuals are then appointed to the role.  This creates a relationship between their [profile](/concepts/personal-profile) and the role.  This relationship is then removed when the individual leaves the role.  It is not unusual for [effectivity dates](/features/effectivity-dates) to be used with this relationship to allow people to be appointed and removed from roles ahead of time, creating a smooth transition.

It is also common that an individual performs many roles in an organization.

## Head count limit

A role has an optional *head count* that indicated the maximum number of people that should be appointed to the role.  You can think of it as a planning or funding value that the organization has set.

Egeria does not prevent more people than this limit being appointed to the role, but the [Community Profile OMAS](/services/omas/community-profile/overview) does send a notification (event) to indicate that the limit has been breached.

The organization can choose to increase the head count limit or remove one of the appointed people or ignore the situation.

!!! education "Further information"

    * [Examples of roles](/practices/roles/overview)



--8<-- "snippets/abbr.md