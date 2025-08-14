<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->


# 0425 Subject Areas

[Subject areas](/concepts/subject-area) are topic areas that are important to the organization.  Typically, they cover data that is widely shared across the organization and there is business value in maintaining consistency in the data values in each copy.  
The role of the [SubjectAreaDefinition](/types/4/0440-Organizational-Controls) is to act as a collection point for all the subject area materials.  

![UML](0425-Subject-Areas.svg)

## SubjectAreaHierarchy relationship

A subject area may be subdivided into more specific subject areas.  The subject areas can be linked together into a hierarchy using *SubjectAreaHierarchy* relationships.

## SubjectArea classification

Elements that are part of the materials for a subject area are classified with the *SubjectArea* classification.  The *name* attribute in the classification matches the *subjectAreaName* attribute in the *SubjectAreaDefinition*.

This classification makes it easy to locate all the subject area's content.


??? deprecated "Deprecated types"
    - *SubjectAreaGovernance* - use [GovernedBy](/types/4/0401-Governance-Definitions) relationship instead.


--8<-- "snippets/abbr.md"