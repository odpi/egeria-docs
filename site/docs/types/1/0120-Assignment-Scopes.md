<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0120 Assignment Scopes

Open metadata supports the capture of the business and organizational context around the catalogued assets.  Part of this context identifies who is responsible for, say driving a result, or resolving an issue.  This model defines two important relationships for identifying responsibility called *AssignmentScope* and *Stakeholder*.

In addition, there is the [*GovernanceResponsibilityAssignment*](/types/4/0445-Governance-Roles) relationship that links a *GovernanceResponsibility* entity to a *GovernanceRole* entity.


![UML](0120-Assignment-Scopes.svg)

## AssignmentScope relationship

The *AssignmentScope* relationship identifies the people, teams, projects or other types of actors that have been assigned to manage the resources represented by the linked element.

## Stakeholder relationship

The *Stakeholder* relationship identifies the actors, such as [ActorProfiles](/types/1/0110-Actors) or [PersonRoles](/types/1/0112-people) that commissioned work (such as a project or a community) or a capability, service or assets.

--8<-- "snippets/abbr.md"
