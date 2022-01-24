---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Person Role

A person role is a placeholder in a [team](/egeria-docs/features/people-roles-organizations) that defines a set of skills and responsibilities that one or more individuals can perform.


Individuals are then appointed to the role.  This creates a relationship between their [profile](/egeria-docs/concepts/personal-profile) and the role.  This relationship is then removed when the individual leaves the role.  It is not unusual for [effectivity dates](/egeria-docs/features/effectivity-dates) to be used with this relationship to allow people to be appointed and removed from roles ahead of time, creating a smooth transition.

It is also common that an individual performs many roles in an organization.

## Head count limit

A role has an optional *head count* that indicated the maximum number of people that should be appointed to the role.  You can think of it as a planning or funding value that the organization has set.

Egeria does not prevent more people than this limit being appointed to the role, but the [Community Profile OMAS](/egeria-docs/services/omas/community-profile/overview) does send a notification (event) to indicate that the limit has been breached.

The organization can choose to increase the head count limit or remove one of the appointed people or ignore the situation.

## Examples of roles

### Asset Owner

A person who is accountable for the proper use and protection of an
[Asset](/egeria-docs/concepts/asset).

The Asset Owner is supported by the [Asset Owner OMAS](/egeria-docs/concepts/omas/asset-owner/overview).

### Governance Officer

A person who is responsible for leading a governance domain is called a governance officer. 

The governance officer is supported by the [Governance Program OMAS](/egeria-docs/concepts/omas/governance-program/overview).

### Project Manager

A project manager is a person who leads a [project](/egeria-docs/concepts/project).

The project manager role is supported by the [Project Management OMAS](/egeria-docs/concepts/omas/project-management/overview).

### Team Leader

The leader of a [team](/egeria-docs/concepts/organization/#team).

### Team Member

A member of a [team](/egeria-docs/concepts/organization/#team).

--8<-- "snippets/abbr.md