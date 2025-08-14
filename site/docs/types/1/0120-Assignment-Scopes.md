<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0120 Assignment Scopes

Open metadata supports the capture of the business and organizational context around the catalogued assets.  Part of this context identifies who is responsible for, say driving a result, or resolving an issue.  This model defines two important relationships for identifying responsibility called *AssignmentScope* and *Stakeholder*.


![UML](0120-Assignment-Scopes.svg)

## AssignmentScope relationship

The *AssignmentScope* relationship identifies the people, teams, projects or other types of actors that have been assigned to manage the resources represented by the linked element.

The *assignmentScope* attribute describes the type of association.  Its values are typically defined in a [valid metadata value](/guides/planning/valid-values/overview) set.  Egeria supplies the following values as an initial set:

* *Contributor* - Individual is able to be a contributing member of the initiative.  This is the default.
* *Administrator* - Individual is able to administer the initiative.
* *Leader* - Individual leads the activity of the initiative.
* *Owner* - Individual sets the direction of the initiative.
* *Observer* - Individual is observing the work of the initiative, but has no special responsibilities.
* *Sponsor* - Individual is funding/supporting the work of the initiative.
* *Other* - Another meaning.

## ScopedBy relationship

*ScopedBy* links an element to the elements ([Organizations](/types/5/), [Projects](/types/1/0115-Teams), [Teams](/types/1/0115-Teams), ...) that are scoping the impact or applicability of its affect.


--8<-- "snippets/abbr.md"
