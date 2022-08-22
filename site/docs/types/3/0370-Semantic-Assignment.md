---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0370 Semantic Assignment

*SemanticAssignment* is a relationship used to assign a term to a [referenceable](/types/0/0010-Base-Model) object. This means that the term describes the meaning of data that is described by the linked referenceable object.  For example, the referenceable object may describe a [Relational Column](/types/5/0534-Relational-Schemas) in a [Database](/types/2/0224-Databases).  A term linked to it via the *SemanticAssignment* relationship describes the meaning of the data stored in the column in the database.


![UML](0370-Semantic-Assignment.svg)

The setting up of the *SemanticAssignment* relationship needs to be controlled when it defines how the data is to be governed (for example, when it is used to [control access to the data](/features/synchronized-access-control/overview)).

* *TermAssignmentStatus* defines how much the semantic assignment should be trusted.

    * DISCOVERED - this semantic assignment was added by a discovery engine.
    * PROPOSED - this semantic assignment was proposed by person - they may be a subject-matter expert, or consumer of the Referenceable asset.
    * IMPORTED - the relationship has been imported from outside the open metadata cohort.
    * VALIDATED - this relationship has been reviewed and is highly trusted.
    * DEPRECATED - this relationship is being phased out.  There may be another semantic relationship to the Referenceable that will ultimately replace this relationship.
    * OBSOLETE - this relationship is no longer in use.
    * OTHER - the status of the relationship does not match any of the other term status values.  The description field can be used to add details about the relationship.

* The *createdBy* attribute found in all elements identifies the user that created the relationship.
* The *confidence* attribute in the relationship stores the level of confidence (0-100%) in the correctness of the relationship - it is typically set up by [discovery engines](/concepts/open-discovery-engine).
* The steward is the person responsible for assessing the relationship and deciding if it should be approved or not.


!!! info "Similar relationships"
    * The [*MoreInformation*](0019-More-Information) relationship is used to show that one element provides more information.  For example, if a glossary term describes a team or a project, the *MoreInformation* relationship could link the term to the [Team](/types/1/0115-Teams) or [Project](/types/1/0130-Projects) element as appropriate.

--8<-- "snippets/abbr.md"