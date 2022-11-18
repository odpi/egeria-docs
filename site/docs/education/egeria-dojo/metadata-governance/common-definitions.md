<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

## Common definitions

**Recap:** 

* *Common definitions* define the standards for your data and its use. They cover data that is widely shared across the organization and there is business value in maintaining consistency in the data values in each copy.
* *Common definitions* are organized in to topic areas called [Subject Areas](/concepts/subject-area).  Each subject area has an owner who is responsible for coordinating the development and maintenance of the subject area's common definitions.
* The effort required to author and maintain common definitions, plus the governance process required to ensure they are used wherever appropriate is offset by the savings in managing and using the shared data associated with the subject area.
* [Assets](/concepts/asset) that are managed using the subject area's common definitions are said to be part of the subject area's "domain".  This is called the *Subject Area Domain* and is synonymous with *Data Domain* - although a subject area domain may manage assets that are not data assets (such as systems and infrastructure) which is why open metadata uses a more generic name.

--8<-- "docs/practices/common-data-definitions/semantic-to-implementation.md"


??? education "Using common definitions in Egeria"

    - [Governance Program OMAS](/services/omas/governance-program/overview/#subject-areas) provide support for the definition of subject areas and the ability to retrieve details of the common definitions that are part of the subject area.
    - [Subject Area OMAS](/services/omas/subject-area/overview) supports the definition of glossary terms for subject areas.
    - [Digital Architecture OMAS](/services/omas/digital-architecture/overview) supports the definition of reference data and quality rules for the subject area.
    - [Asset Manager OMAS](/services/omas/asset-manager/overview) supports the exchange of subject area information with other catalogs and quality tools.
    - [Common Data Definitions](/practices/common-data-definitions/overview) describes the management and use of subject areas.
    - The [Defining Subject Areas](/practices/coco-pharmaceuticals/scenarios/defining-subject-areas/overview/) scenario for Coco Pharmaceuticals walks through the process of setting up.
    - There are two code samples associated with this set of subject areas:
    
        * [Setting up the subject area definitions :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-samples/access-services-samples/governance-program-client-samples/governance-subject-area-sample){ target=gh }
        * [Setting up glossary categories for each subject area :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-samples/access-services-samples/subject-area-client-samples/subject-area-definition-sample){ target=gh } ready for subject area owners to start defining glossary terms associated with their subject area.


??? intermediate "Creating glossaries (30 mins)"
    --8<-- "docs/education/egeria-dojo/metadata-governance/creating-glossaries.md"

??? intermediate "Managing reference data (60 mins)"
    --8<-- "docs/education/egeria-dojo/metadata-governance/managing-reference-data.md"

??? intermediate "Using open metadata archives for shared definitions (30 mins)"
    --8<-- "docs/education/egeria-dojo/metadata-governance/using-open-metadata-archives.md"


--8<-- "snippets/abbr.md"