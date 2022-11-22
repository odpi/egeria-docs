---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Subject Area

Subject areas are topics or domains of knowledge that are important to the organization.  Typically, they cover data that is widely shared across the organization and there is business value in maintaining consistency in the data values in each copy.

The role of a [subject area definition](/types/4/0425-Subject-Areas) is to act as a collection point for all the subject area materials.  This includes:

* A [glossary of terms](/types/3/0310-Glossary) that describe the key concepts in the subject area.
* Lists and hierarchies of [reference data](/types/5/0545-Reference-Data) that relate to particular data values in the subject area.
* [Quality rules](/types/4/0430-Technical-Controls) for specific data values in the subject area.
* Preferred [data structures and schemas](/types/5/0501-Schema-Elements).

The materials that are part of the subject area are classified as such using the [SubjectArea](/types/4/0425-Subject-Areas) classification.

Each subject area has an owner (see [SubjectAreaOwner](/types/4/0445-Governance-Roles)) who is responsible for the materials relating to the subject area.  Often the subject area owner is a senior person in the organization with expertise in the subject area.  He/she coordinates other subject-matter experts to author and maintain the materials.

The *SubjectAreaDefinition* and appointment of a *SubjectAreaOwner* helps to coordinate the efforts to build the [materials](/practices/common-data-definitions/overview) for each subject area.

![Subject Area Content](/guides/planning/governance-program/subject-area-definition.svg)

The effort required to author and maintain these definitions, plus the governance process required to ensure they are used wherever appropriate is offset by the savings in managing and using the shared data associated with the subject area.

## Subject Area Domain

[Assets](/concepts/asset) that are managed using the subject area's materials are said to be part of the subject area's domain.  This is called the *Subject Area Domain* and is synonymous with *Data Domain* - although a subject area domain may manage assets that are not data assets (such as systems and infrastructure) which is why open metadata uses a more generic name.


!!! education "Further information"
    
    - [Governance Program OMAS](/services/omas/governance-program/overview/#subject-areas) provides support for the subject area definition and the ability to retrieve details of a subject area's materials.
    - [Subject Area OMAS](/services/omas/subject-area/overview) supports the definition of glossary terms for subject areas.
    - [Digital Architecture OMAS](/services/omas/digital-architecture/overview) supports the definition of reference data and quality rules for the subject area.
    - [Asset Manager OMAS](/services/omas/asset-manager/overview) supports the exchange of subject area information with other catalogs and quality tools.
    - [Common Data Definitions](/practices/common-data-definitions/overview) describes the management and use of subject areas.
    - The [Defining Subject Areas](/practices/coco-pharmaceuticals/scenarios/defining-subject-areas/overview/) scenario for Coco Pharmaceuticals walks through the process of setting up.
    - There are two code samples associated with this set of subject areas:
    
        * [Setting up the subject area definitions :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-samples/access-services-samples/governance-program-client-samples/governance-subject-area-sample){ target=gh }
        * [Setting up glossary categories for each subject area :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-samples/access-services-samples/subject-area-client-samples/subject-area-definition-sample){ target=gh } ready for subject area owners to start defining glossary terms associated with their subject area.


--8<-- "snippets/abbr.md"
