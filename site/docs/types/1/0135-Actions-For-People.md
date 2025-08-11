<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0135 Actions for People

In an ideal world, most governance activity is automated by the [Governance Actions](/concepts/governance-action). However, there are inevitably actions that require a person, or an external agent, to perform. These actions may be simply be to read some information, or to approve a change or something more substantial.  The actor assigned to perform this work is linked via the [AssignmentScope](/types/1/0120-Assignment-Scopes) relationship.

![UML](0135-Actions-For-People.svg)

## Meetings

*Meetings* allow a record of meetings for projects or the governance program to be associated with the appropriate metadata elements.

## ToDo entity

A *ToDo* entity is a [*Referenceable*](/types/0/0010-Base-Model) that describes an item of work for an [*Actor*](/types/1/0110-Actors) to perform.  This work is performed outside the open metadata ecosystem.


--8<-- "snippets/abbr.md"
