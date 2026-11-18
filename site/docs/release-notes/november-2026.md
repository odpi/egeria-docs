<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# November 2026

Welcome to the Egeria community's November 2026 newsletter. Since our [last newsletter](https://egeria-project.org/release-notes/october-2026/), we have released Egeria 6.3.

Our October newsletter was about producing trustworthy context for people and AI: data products, contracts and lineage on open standards. This month is about what it takes to keep delivering that context, day after day, from a platform that has been running for months. Egeria 6.3 is faster on a large repository, does more of its own housekeeping, is easier to recover when something goes wrong, and is more secure by default. It also speaks two more families of standards out of the box: DCAT for sharing catalogs, and the NIST and ISO/IEC security frameworks.

## What's new

### Fast on a large, busy platform

A metadata repository that is used gets bigger, and every change adds to its history. We measured where a long-running platform was spending its time and removed the worst of it.

- **Reading metadata.** The PostgreSQL repository now reads the current version of an element without being slowed by its history. On a copy of a large repository, reading an element with 238,795 versions went from 131 milliseconds to 0.05 milliseconds.
- **Searching.** Searches are filtered by governance zone inside the repository, so a user who may see only a little of the metadata no longer waits while everything else is read and thrown away.
- **Events.** The Apache Kafka topic connector sent 344 events a second in our benchmark. It now sends 210,000, and a slow or unavailable Kafka can no longer bring the platform down.
- **Lineage graphs.** In our sample environment, the lineage graph of one schema reached 1,057 elements and 52 MB. Graphs are now limited to 8 hops by default, with a marker where the lineage continues, so they come back quickly and can be displayed.
- **Open Lineage analysis.** Open Lineage events can now be stored in PostgreSQL. Analysing 30 days of events (864,000 of them) took 17 to 19 minutes from files; it takes about three seconds from the database.

[Read the detail in the release notes](https://egeria-project.org/release-notes/latest/)

### A platform that looks after itself

Last month we introduced Darwin and Mendel, two of the "nanny" connectors that maintain the metadata so that people do not have to. They have new colleagues and new duties.

- **Pasteur** clears out finished actions once they are old enough, so the history of governance actions and to dos no longer grows without end. Anything with lineage is archived rather than deleted.
- **Mendel** now removes exact duplicates, the identical copies left behind when a process adds the same thing twice. There is nothing for a steward to decide, so Mendel keeps the oldest copy and removes the rest.
- **Simon** awards karma points to the people who contribute to the catalog, and only to people: automation is ignored.
- **Baudot** and **Wedgwood**, which deliver data products to their subscribers, now deliver only when the data has changed, and write only the records that differ. On our sample platform about 70% of the notifications Baudot sent were unnecessary; they have gone.

Several connectors that used to react to every event now gather what has changed and do the work once per refresh. The result is a platform that is quieter, with fewer versions, fewer notifications and audit logs that reflect what users actually asked for.

Learn more about [metadata observability](https://egeria-project.org/features/metadata-observability/overview/) and [duplicate management](https://egeria-project.org/features/duplicate-management/overview/).

### Mistakes can be undone

People, and increasingly AI agents, make changes to metadata, and some of those changes are mistakes. In 6.3 an update can be undone and a delete or archive can be restored. Restore reverses the whole command: bring back a deleted database schema and its tables, columns, connection and relationships come back with it.

Deletes are also more careful. Deleting a column used to be able to take the rest of its table, schema and asset with it. Now a delete takes the element and what belongs to it, and nothing else. A running governance action process can be cancelled, too.

Learn more about [anchor management](https://egeria-project.org/features/anchor-management/overview/) and the [Metadata Expert API](https://egeria-project.org/services/omvs/metadata-expert/overview/).

### Secure by default, and ready for security teams

[Governance zones](https://egeria-project.org/features/governance-zoning/overview/) control who can see and change which metadata. A zone with no access control used to be ignored, so a mistyped zone name could expose the elements in it. Zones now fail closed: no access control means no access, and Egeria reports the zones that need attention.

We have also added content and types for the work security teams do:

- A new **Security Content Pack** with the NIST Cybersecurity Framework 2.0 and NIST SP 800-53 Rev. 5 control catalogs: 106 CSF subcategories and 1,014 controls and enhancements, ready to link to your own policies and evidence.
- **Statements of applicability**, recording which controls from a standard such as ISO/IEC 27001 apply to your organization, why, and how far each has been implemented.
- The six **STRIDE** threats as standard definitions, so every threat model refers to the same threats.
- New annotations for the results of **security testing**: findings, known vulnerabilities, penetration test results and overall security posture.
- Data products that describe how the ecosystem is secured (users, secrets, zones) are now visible only to the security team.

Learn more about the [Security Content Pack](https://egeria-project.org/content-packs/security-content-pack/overview/) and [threat modelling](https://egeria-project.org/egeria-solutions/threat-modelling/overview/).

### Sharing catalogs with DCAT

The W3C Data Catalog Vocabulary (DCAT) is the standard that governments and many other organizations use to describe the data they make available. Egeria now reads and writes DCAT version 3. Drop DCAT documents into a directory, or send them to a Kafka topic, and the datasets, distributions and data services they describe are catalogued as assets. In the other direction, add an asset to a publishing collection and Egeria writes its DCAT description ready for a data portal to harvest; remove it and the description is withdrawn.

Learn more about [exchanging asset descriptions](https://egeria-project.org/features/asset-description-exchange/overview/) and the [DCAT Content Pack](https://egeria-project.org/content-packs/dcat-content-pack/overview/).

### Lineage you can follow, layer by layer

Darwin now keeps every layer of lineage consistent, from column mappings up through the data fabric and the systems it runs on to the data mesh. At each boundary it adds the relationships that the detail beneath implies, and raises an exception for a steward where someone has asserted lineage that the detail does not support. Every lineage relationship records where it came from, so you can tell what was asserted by a person from what was derived, and by which rule.

Information supply chains are easier to see as well. One diagram of a large supply chain was often too big to display, so there are now five: the design and its deployment status, the data mesh, the system fabric, the data fabric and the data mappings. An Open Lineage run can also report that it serves several information supply chains at once.

Learn more about [lineage management](https://egeria-project.org/features/lineage-management/overview/) and [information supply chains](https://egeria-project.org/concepts/information-supply-chain/).

### Organizing what you see

Every relationship type and classification type in Egeria now has a declared purpose, such as structural, membership, design lineage, action or activity for relationships, and governance, descriptive or analytical for classifications. User interfaces can use the purpose to group what is attached to an element and to show each audience what matters to it. Egeria uses it too: the diagram of an element's context now leaves out its ever-growing history of actions and activity, which have diagrams of their own.

Learn more about [relationship purpose](https://egeria-project.org/concepts/relationship-purpose/) and [classification purpose](https://egeria-project.org/concepts/classification-purpose/).

## Egeria Workspaces

Egeria Workspaces, our ready-to-run environment, has kept pace with the 6.3 work, and its portal has grown.

- **Statements of applicability can be explored in Egeria Explorer**, starting with Coco's sample for ISO/IEC 27001. It shows how far each control has been implemented.
- **Resource Locator** is a new app for finding resources, not just data. It shows what a resource contains and what it means, and supports work lists, team sharing and private notes.
- **Relationships and classifications are grouped by purpose** throughout the portal, in Egeria Explorer, the Data Mesh view and The Catalog, so a busy element is much easier to read.
- **Lineage controls** let you choose how many hops of lineage to show, and every diagram has an Expand button that opens it in a viewer you can pan and zoom.
- **Dashboards and report specifications are now held in Egeria** as open metadata, organized in folders by the tools that use them, so they can be shared, secured by governance zone and reused rather than living in local files. New tutorials cover report specs, analytic functions, local dashboards and saved queries.
- **The Overview now only shows numbers it has measured**, and results say when more may exist.
- **Airflow and Marquez start with the demo**, and Airflow's Open Lineage events flow into Egeria, so you can watch lineage arrive from running pipelines.
- **Every column and pane in the portal can be resized**, and your choices are remembered.

For those running their own environment, a new `egeria-upgrade-reset` tool plans and performs an upgrade or reset of the quickstart step by step, with a verified backup, and the sample content now heals itself afterwards.

You can [try the live demo](https://egeria.pdr-associates.com){target=blank} without installing anything (signing up takes a minute), or run [Egeria Workspaces](https://egeria-project.org/egeria-workspaces/) locally with Docker or Podman.

## Technical preview: Resource Explorer, Egeria Advisor and Studio

The AI applications on Trellis are released alongside Egeria 6.3 as a technical preview. Resource Explorer now publishes what it finds into Egeria and runs its surveys on Egeria's own engine host. Egeria Advisor works with the same dashboards and report specifications held in Egeria as the portal does, and the new Studio application is for authoring them. You can try Resource Explorer and Egeria Advisor on the [live demo](https://egeria.pdr-associates.com){target=blank}. Please tell us what works for you.

## pyegeria and Dr.Egeria

pyegeria, our Python client, and Dr.Egeria, which turns markdown documents into metadata, have followed the new function in 6.3. There are new Dr.Egeria commands and templates for statements of applicability, business capabilities, report specifications, measurements and dashboards, and for setting an element's governance zones. Reports can be produced as documents and as DCAT catalogs, and searches now page through complete results and say so plainly when a result has been capped.

Install or upgrade with `pip install -U pyegeria`. The [pyegeria release notes](https://github.com/odpi/egeria-python/tree/main/docs/release-notes){target=blank} describe each release.

## Full release notes for V6.3

The full release notes for version 6.3 are on [Egeria's website](https://egeria-project.org/release-notes/latest/). Several defaults have changed in this release: governance zones fail closed, lineage graphs are limited to 8 hops, and old finished actions and exact duplicates are cleaned up when the new content packs are loaded. If you maintain your own user directory there are new accounts to add. Please read the [upgrade notes](https://egeria-project.org/release-notes/latest/#upgrade-notes) before upgrading.

## Future plans

The [next release](https://egeria-project.org/release-notes/next/), 6.4, is expected in late December and lays the foundations for context intelligence. Release 7.0, a platform upgrade, is planned for mid February 2027. Plans are open, and we welcome suggestions.

## Connecting with the project

Egeria is an open source project under LF AI & Data, and it grows through the people who use it and shape it. With our focus on AI and on supporting data practitioners directly, we are looking for new users and contributors. Whether you want to try Egeria on your own metadata, contribute code or content, or bring a hard problem to the discussion, we would be glad to hear from you.

- Talk with the team and other users on [Slack](https://slack.lfaidata.foundation){target=blank}.
- Watch demos and walkthroughs on [YouTube](https://www.youtube.com/@egeria-project){target=blank}.
- Follow the project on [LinkedIn](https://www.linkedin.com/company/egeria-project/){target=blank}.
- Read our blogs and articles on [Pragmatic Data Research, LTD](https://pdr-associates.com)

!!! info "Connecting with the community"
    Go to our [community guide](https://egeria-project.org/guides/community){target=blank} to find out more about the activities of the Egeria project and how to get involved.

--8<-- "snippets/abbr.md"
