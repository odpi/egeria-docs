<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Personal Profile

A personal profile provides a place for an individual to share information about themselves
with the other people they are collaborating with.  It is associated with one or more
of the person's userIds.

Each userId is linked to the profile as a [UserIdentity](/egeria-docs/concepts/user-identity) object.

> ![Figure 1](profile-user-1.svg)

There can be more than one userId for a profile (for example if a user has an administrator userId and a normal userId)
> ![Figure 2](profile-user-2.svg)

However, the same userId can not be linked to two profiles.

> ![Figure 3](profile-user-3.svg)

This means we can retrieve a profile from the UserId.

Each profile has a qualified name that should uniquely identify the
individual.  For example, an employee identifier.

There is space to provide the name the individual wants to be
known as, and their full name, along with a job title.

An individual can also maintain collections of their
favourite Assets, Projects and Communities and control notifications
about changes to the member of these lists.

> ![Figure 4](contents-of-a-personal-profile.svg)

--8<-- "snippets/abbr.md"