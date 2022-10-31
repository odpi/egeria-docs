<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# October 2022

This is the first monthly report from the Egeria community.  It is an idea that came out of the recent quarterly face-to-face meeting.  Up to this point, we published release notes for each release of the [core egeria repository](https://github.com/odpi/egeria) - which occurred about once a month.  If you have been watching the project, however, you will have noticed that we have been splitting our work across multiple git repositories that each have their own release schedule.  With so much interesting work going on in these new repositories, it seemed appropriate that our monthly report should evolve to cover the activity of these repositories too.  

## Quarterly face-to-face meeting

This month we held a face-to-face meeting at [IBM's Hursley Park](https://en.wikipedia.org/wiki/IBM_Hursley).  The discussions lead to this monthly newsletter and included exciting news about the new combined UI platform for Egeria.

## Branch rename

The Linux Foundation (LF) has been encouraging its projects to focus on the terminology to ensure it is inclusive.  Part of this initiative is to rename the default branch from *master* to *main*.  October 2022 was the month that we completed our rename.  If you have forks of our repositories, you may see messages on GitHub informing you of the change.  Follow the suggested instructions and your forks/clones will be updated to work with the new default branch.

## User interfaces

The demo users for the Egeria UI have been updated.  The *admin* user account is now for "Generic Admin" rather than "James Bond".  Also, *Erin Overview* and *Peter Profile* now have admin access which means they have access to all features of the UI including the Repository Explorer and the Type Explorer.

## Security

The Open Metadata and Governance APIs for core Egeria now support API Tokens.  They are added to thread local storage when a REST API request is received by the [OMAG Server Platform](/concepts/omag-server-platform) and can be inspected by the [Server Metadata Security Connector](/concepts/server-metadata-security-connector).  When Egeria makes an outbound REST call, and APITokens are propagated with the request.

## Database support

Testing of the new [JDBC Resource Connector](/connectors/resource/jdbc-resource-connector) and [JDBC Integration Connector](/connectors/integration/jdbc-integration-connector) is going well with support for **PostgreSQL** and **MariaDB** demonstrated.

## Data products

Egeria's data product support is progressing well.  New types based around [Digital Services](/types/7/0710-Digital-Service) and [Solution Components](/types/7/0730-Solution-Components) have been added to the [Open Metadata Types](/types).  These types represent the business aspects of data products and link to the [Assets](/concepts/asset) that implement them.

Next month look our for the new APIs in [Digital Service OMAS](/services/omas/digital-service/overview), [Digital Architecture OMAS](/services/omas/digital-architecture/overview), [Asset Owner OMAS](/services/omas/asset-owner/overview) and [Asset Consumer OMAS](/services/omas/asset-consumer/overview)

## Community news

Congratulations to [Dan Wolfson](https://github.com/dwolfson) who becomes our latest contributor.

## Core Egeria

The *Core Egeria* technology is located in the [egeria.git](https://github.com/odpi/egeria) repository.  It provides the [OMAG Server Platform](/concepts/omag-server-platform), java clients for the [OMAG Servers](/concepts/omag-server) that run on the OMAG Server Platform along with the [Conformance Test Suite (CTS)](/guides/cts/overview).  

!!! info "Core Egeria Releases"
    [Release 3.12](/release-notes/3.12) was shipped in October 2022.  The work this month is contributing to [Release 3.13](/release-notes/3.13).

The database support for the Data Manager OMAS REST API has had a major refactor to improve its consistency with other parts of the REST API and to allow databases to be catalogued in the [Local Cohort](/concepts/metadata-collection) metadata collections.

The [Open Connector Framework (OCF)](/frameworks/ocf/overview) beans and its corresponding [Connected Asset API](/services/ocf-metadata-management) now support schemas for APIs and events.

## Events

### Egeria Dojos

The next run of an Egeria Dojo will be the new [Metadata Governance Dojo](/education/egeria-dojo/metadata-governance/overview) on Monday 21st November 2022. 

### Community Meetings

Over the last few community meetings we have reviewed the Egeria education curriculum from [Pragmatic Data Research](https://pdr-associates.com/), and a new Open Metadata Lab that demonstrates the workings of an [Open Metadata Repository Cohort](/concepts/cohort-member).

### Conference Presentations

Last month, the Egeria community gave two presentations at the European Open Source Summit in Dublin.

* [Building an Open Metadata and Governance Ecosystem](https://www.youtube.com/watch?v=C-hglq31mfQ) - An overview and demo of Egeria
* [Truly Open Lineage](https://www.youtube.com/watch?v=eNbGa1iDri4) - covering the integration of the Egeria, Marquez and OpenLineage projects.

## New documentation pages

Each month we will select a some new pages that where added/updated in the last month to [https://egeria-project.org](https://egeria-project.org) so you can keep up-to-date with how it is evolving.

* [Open metadata instances](/concepts/open-metadata-instances)
* [Metadata collection](/concepts/metadata-collection)
* [0530 Tabular Schemas](/types/5/0530-Tabular-Schemas)

## Postman collections

There is new postman collect for the [Asset Consumer OMAS](/services/omas/asset-consumer/overview) REST API.

* [Link on GitHub](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/access-services/asset-consumer)

The postman collection for [Data Manager OMAS](/services/omas/data-manager/overview) needs updating since the updates to its REST API.

* [Link on GitHub](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/access-services/data-manager)


## Future items

### Annual Project Review

The Egeria project annual review by the [Technical Advisory Board (TAC)](https://wiki.lfaidata.foundation/pages/viewpage.action?pageId=7733341) of the LF AI and Data foundation is scheduled for 15th December 2022.  Please encourage people who work with Egeria to *Star* each of our repositories on Github as we are trying to get [our total count to 1000](https://landscape.lfai.foundation/?selected=egeria).

### Moving to Gradle

Our build technology for the Java based projects has used both Maven and Gradle.  We plan to move entirely to gradle in the next few months, so you will see:

* Repositories such as egeria-dev-projects.git and egeria-samples.git move from maven to gradle.
* The Egeria Development Dojo will use gradle in the exercises.

The [Core Egeria](https://github.com/odpi/egeria) repository has offered both a maven and a gradle option.  The maven option will be removed once we are sure the gradle build is able to support the release process.

## Connecting with the project

!!! info "Connecting with the project"
    Go to our [community guide](/guides/community) to find out how to find out more about the activities of the Egeria project. 

--8<-- "snippets/abbr.md"
