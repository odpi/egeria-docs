<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# January 2025

Welcome to the Egeria community's January 2025 newsletter.  Since our [last newsletter](https://egeria-project.org/release-notes/october-2024), the community has developed some exciting new capabilities as well as improving the function, reliability and performance of existing features.  

## New Native Open Metadata Repository built in PostgreSQL

We are excited to announce a new open metadata repository choice for Egeria, hosted on PostgreSQL.  The contents of the repository are stored in 7 tables within its own database schema.  A single PostgreSQL server/database may host multiple repositories.  

The [PostgresRepositoryConnector](https://egeria-project.org/connectors/repository/postgres/overview/) offers high-speed metadata loading, full range of queries, including bi-temporal queries and queries into metadata properties of type array and map.  It is possible to turn on debug logging and see every SQL command issued by Egeria.  This transparency has helped in debugging issues both in Egeria and calling code.  It has also lead to some valuable performance improvements in Egeria's core runtime.  These are incorporated in Egeria's 5.2 release.

Operationally, PostgreSQL has the advantage that it is available on many (all?) cloud platforms and most organizations have experience in managing PostgreSQL database (such as high-availability, backup and restore).

## Visualization using Mermaid

Good visualizations help to improve understanding and validation.  [Mermaid](https://mermaid.js.org/) is an amazing technology that generates graphical visualizations from and extended form of markdown.  The graphs can be rendered in Jupyter notebooks, [GitHub README pages](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/open-metadata-collection-store-connectors/postgres-repository-connector) and in their own [live editor](https://mermaid.live/edit).  Selective REST APIs from Egeria's view services are returning a mermaid visualization string with the query results.  The mermaid string describes a visualization of the query results, helping the caller get a quick understanding of the results they have just received.  More details of this capability can be found on the [Graph Visualizations](https://egeria-project.org/user-interfaces/mermaid/overview/) page.

## Extensions to pyegeria

The [*pyegeria* python libraries](https://egeria-project.org/concepts/pyegeria/) continues to evolve at a rapid pace offering [python interfaces](https://egeria-project.org/guides/developer/python-clients/overview/) to Egeria's services along with [scripting commands](https://egeria-project.org/guides/developer/scripting-commands/overview/) and the [*hey_egeria* command level interface](https://egeria-project.org/user-interfaces/hey-egeria/overview/).

In addition, there are new documentation pages that walk you through the different commands and associated displays:

* [Introduction to Hey_Egeria](https://github.com/odpi/egeria-python/blob/main/pyegeria/commands/doc/hey_egeria%3A%20a%20pyegeria%20command%20line%20interface/README.md)
* [Visual Command Reference](https://github.com/odpi/egeria-python/blob/main/pyegeria/commands/doc/Visual%20Command%20Reference/README.md)
* [Command Line Interface](https://github.com/odpi/egeria-python/blob/main/pyegeria/commands/doc/README.md)

## New Governance Action Processes

The [Technology Content Packs](https://egeria-project.org/content-packs/) contain the metadata necessary for activating the connectors and services that support particular types of technologies.  In the 5.2 release they also include governance action processes that simplify working with the connectors.  

* **Create and Survey Governance Action Processes** accept the placeholders for a technology template (such as a Unity Catalog Server), creates a metadata element to represent an instance of the technology, activates an appropriate survey, and then publishes the report.
* **Create and Catalog Governance Action Processes** accept the placeholders for a technology template, creates a metadata element to represent an instance of the technology, configures the appropriate integration connector to set up an ongoing metadata synchronization between Egeria and the named technology.
* **Delete Governance Action Processes** accept the placeholders for a technology template, looks up the corresponding metadata element that represents the requested instance of the technology and deletes it.  This is useful if you pass incorrect values to the previous two governance action process, since it cleans up the metadata created with the wrong values allowing you to start again.
* **Provision Governance Action Processes** accepts the identifier of a metadata element that describes a desired digital resource and provisions the resource in the appropriate third party technology.

As an example, below are mermaid visualizations for some of the new processes for [Unity Catalog](https://egeria-project.org/connectors/unity-catalog/):

![Create and Survey](https://egeria-project.org/governance-action-processes/unity-catalog-server-create-and-survey.png)

![Create and Catalog](https://egeria-project.org/governance-action-processes/unity-catalog-server-create-and-catalog.png)


## Governance Action Process Lineage

In addition to publishing [open lineage events](https://egeria-project.org/connectors/integration/governance-action-open-lineage-integration-connector/) when they run, governance action processes also create a [GovernanceActionProcessInstance](https://egeria-project.org/types/4/0462-Governance-Action-Processes/) entity linked to the [engine actions](https://egeria-project.org/concepts/engine-action/) that were created during the execution of the governance action process.  It is then possible to query both the design and the execution of the process via *pyegeria* and compare then using Mermaid visualizations.

| Design of Governance Action Process | Single Execution of this Governance Action Process |
| ----------------------------------- | --------------------------------------------------- |
| ![Daily Governance Action Process](https://egeria-project.org/governance-action-processes/daily-governance-action-process.png) | ![Daily Governance Action Process Instance](https://egeria-project.org/governance-action-processes/daily-governance-action-process-instance-thursday.png) |


## Improvements to template support

[Template placeholders](https://egeria-project.org/features/templated-cataloguing/overview/) are now resolved in classification and relationship properties - not just entities.  These placeholders may also be used for all types of properties - not just strings.  This increases the range and complexity of template to use when cataloguing technology in open metadata.


## Extensions to the View Services

There is a new view service called [Metadata Explorer OMVS](https://egeria-project.org/services/omvs/metadata-explorer/overview/) that offers a complex query interface, enabling you to retrieve any metadata that interests you.  This REST APIs return mermaid strings with the requested metadata elements.

![Relationship returned on a query](https://egeria-project.org/services/omvs/metadata-explorer/mermaid-visualization-relationships.png)

## Improvements to the Secrets Stores

[Secret Store Connectors](https://egeria-project.org/concepts/secret-store-connector) are now able to support the authentication of users calling the [Open Metadata View Services (OMVS)](https://egeria-project.org/services/omvs).  This makes it easier to integrate with a third party user directory (LDAP, Keycloak, etc) via an implementation of a Secrets Store Connector.

## Roles and contribution records for teams and automation

[Roles and contribution records](https://egeria-project.org/features/people-roles-organizations/overview/#contribution-records) used to be restricted to people. However, with the expansion of automated agents in the data management and governance space, it is valuable to be able to show where they are playing in the open metadata landscape. Release 5.2 includes:

* Reorganized open metadata types
* Generalized karma point collection
* IT Profiles added to the Integration Connectors in the Technology Content Packs so that karma points are automatically collected for their activity.

## Full release notes for V5.2

The full release notes for version 5.2 can be found on [Egeria's website](https://egeria-project.org/release-notes/previous/#release-52-january-2025).

## Future plans

Plans for [release 5.3](https://egeria-project.org/release-notes/previous/#release-53-march-2025) are open, and we are looking for suggestions.  This is being track using [GitHub projects](https://github.com/orgs/odpi/projects?query=is%3Aopen)

## Connecting with the project

With our new focus on Python and supporting data practitioners directly, the community is looking for new contributors to the project.  If these topics interest you, then please contact us and we can help you get started.

!!! info "Connecting with the community"
    Go to our [community guide](https://egeria-project.org/guides/community){target=blank} to find out more about the activities of the Egeria project nd ho to get engaged.

--8<-- "snippets/abbr.md"