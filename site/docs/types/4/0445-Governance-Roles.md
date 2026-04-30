
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0445 Governance Roles

Although we aim to automate governance as much as possible, it is often necessary to assign responsibility for specific actions to specific people.

![UML](0445-Governance-Roles.svg)
> Figure 1: Assignment of Governance Roles

## GovernanceRole entity

In Figure 1, the responsibilities of someone assigned to manage a particular aspect of governing a resource or related element ([Referenceable](/types/0/0010-Base-Model)) is represented by a *GovernanceRole* entity. Since *GovernanceRole* inherits from [PersonRole](/types/1/0112-People)an individual is assigned the Governance Role through the [PersonRoleAppointment](/types/1/0112-People)relationship.

## Ownership classification

Ownership is assigned to an element by adding the *Ownership* classification to it. This classification can assign ownership as an [ActorProfile](/1/0110-Actors), [UserIdentity](/types/1/0110-Actors) or [PersonRole](/types/1/0112-People).  The *userIds* property is used by the security connector if you want to restrict access to the resource based on the ownership.

--8<-- "snippets/abbr.md"