<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Welcome

--8<-- "snippets/work-in-progress.md"

Egeria is an open source project from Linux Foundation (LF) AI and Data.  It is developed by a team of enthusiasts from different organizations, collectively called the *Egeria Community* that is [free to join](/guides/community).

## What does Egeria do?

Egeria manages context (linked information) about your organization's digital operations, including your data, systems, projects, locations, processes and the people around them.  In the age of AI, there is increasing recognition that this type of context is key to improving the reliability of AI applications because it helps to identify the scope of what is relevant to the requester.  This is true, of course, however there are many other use cases that make Egeria valuable, including:

* tradition data quality and finding data through a data catalog; 
* inventory of IT systems for management and security; 
* data lineage capture and management;
* knowedge management, for example in the form of glossary authoring;
* solution design and documentation;
* digital product marketplaces with subscriptions

... and many more.  

The design of Egeria recognizes that the breadth and depth of the context needed by an organization varies widely.  Typically, an organization will want to build up their context knowledge base on a project-by-project basis, possibly focusing on a specific part of the organization and use cases.  As time progresses, the richness of the context knowledge base grows.

Egeria benefits individuals and well as organizations.  A person can build their portfolio of expertise and contributions in Egeria.  Individuals and teams can link to one another, share news and information as well as form cross-organization communities.

## Latest News

Six years of working with leading enterprises to build metadata synchronization services has taught us a thing or two(!!)  and so the Egeria community proudly announces Version 6.0 of Egeria (expected release date **March 2026**).

- Egeria now has a leaner runtime, reducing cost of deployment and operation.  Despite doubling its capability, Egeria's runtime is now half the size of previous releases due to simplification and consolidation of interfaces and features at each level of the implementation.
- Simple up and running experience for small teams, demonstration and evaluation are available through [egeria-workspaces](/egeria-workspaces).
- The coding frameworks have been enhanced to enable the development of connectors that deliver a complete value chain from metadata capture to metadata synchronization, governance and insight for a type of technology.
    - For Java this includes:
        - Specifications to ease consumption of connectors both for people and automated tools.
        - Reference data management to enrich the capture of metadata.
        - A common context to provide access to open metadata and governance services to all types of connectors.
        - Iterators that ensure complete coverage of metadata from different systems and determine what has changed and the synchronization actions to take.
        - New survey action framework to assess the contents of different technology deployments.
    - New python libraries support the development of connectors in python as an alternative to using the Java frameworks.
- New patterns of use support greater engagement and automation in your organization.
    - No code interaction styles
        - Capture business context and business intent as decisions are made
        - Improve collaboration and data literacy across your organization including
            - Glossaries, data dictionaries and data specifications
            - Solution blueprints and information supply chains
        - Design and author your own reports *... also used as queries to our MCP server*
    - MCP server delivers business context to AI solutions in order to improve relevance and accuracy of answers.
    - Agents that analyse activity and metadata to deliver insight into who is engaged, where value is coming from and what is unused/obsolete
    - Automated harvesting of metadata, reference data, master data and agent insight into a digital product marketplace for easy consumption
    - Notification, agreements and subscription management for active data delivery
    - Management of external data sources, licenses and certifications associated with your data and models, for peace of mind and audit-ability.
    - Layered lineage queries and visualization from business perspective (information supply chains), system-level exchange, data sources lineage, to data mapping and column level lineage and not forgetting operation insight from open lineage.
    - Communities and karma points to enhance education, contact, collaboration and recognition of your most valuable people.
    - Organization and business capability modelling to show where responsibility lies that can be linked to your implementation providing traceability to the business when systems fail, or need to change.
    - Easy, auditable, handoff from automation to individuals/teams and back again
    - Context events, effectivity dating and as-of-time queries to investigate and understand causality.
- APIs restructured to deliver value
    - Use of open formats for representation and delivery of textual and graphical information.  This includes JSON, Markdown and Mermaid Graphs.
    - Consistent Request/Response structured reducing learning curve and decreasing the cost of integration
    - Results returned in context - properties, classifications, relationships, mermaid graphs
    - Complete, consistent coverage of all of your metadata
    - Advanced search operations
    - Secured with bearer tokens for authentication, and both functional and instance based authorization
- Out-of the-box support for commonly used technologies
    - Includes
        - Files
        - Databases
        - Unity Catalog
        - Apache Kafka
        - Open API spec
        - Open Lineage
    - Organized into [loadable solutions](/egeria-solutions) with reference data, commands and reports and documentation
- Distributed secrets management and workload
    - Allows decentralized control of secrets and when/where Egeria workloads operate
    - Self-service configuration of new workloads on deployed distributed platforms, empowering your teams to explore and build value from your existing estate.
    - Monitoring and reports on deployed Egeria estate and workloads covering activity and status.
- Fast, scalable industry standard repository built on PostgreSQL - grow with your business needs; no mysteries in operation, ha, backups and disaster recovery.

### Migrating to this release

With the changes to the Egeria runtime, repository types and services, the migration from earlier releases to Version 6.0 and beyond will require a migration project, rather than the typical simple software upgrade.  Contact our migration partner, Pragmatic Data Research Ltd, for assistance.

Beyond 6.0, the Egeria community will revert to the policy of maintaining backward compatibility of all aspects of the Egeria solution.




--8<-- "snippets/abbr.md"
