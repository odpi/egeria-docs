<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Harvest and Publish

Organizations accumulate valuable data - both the data they run their business on, and the reference data and insight that the open metadata ecosystem itself generates as a by-product of its activity.  In both cases the data is worth more when other teams can find it, understand it and receive it reliably, without the owner having to hand-craft every exchange.

The *Harvest and Publish* pattern covers the two capabilities Egeria provides for this:

* The **[data sharing hub](#the-data-sharing-hub)** organizes the data stores that hold authoritative data suitable for sharing, derives a data dictionary that describes what they hold, and tracks the requests and agreements under which that data is shared.
* The **[Open Metadata Digital Product Catalog](#the-open-metadata-digital-product-catalog)** harvests the content of the open metadata ecosystem into digital products that other teams and tools can subscribe to and have delivered on a schedule.

The two are independently useful, and they also work well together: a hub is the natural place to discover which data is worth [formalizing into a digital product](#from-data-sharing-hub-to-digital-product).

## The Data Sharing Hub

Sharing data inside an organization is rarely limited by the technology.  It is limited by the effort of answering the same questions over and over: what data is available, what does this field actually mean, who approved this copy, and what exactly was sent.

A [data sharing hub](/concepts/data-sharing-hub) addresses this by making the sharing arrangement itself explicit in open metadata.  The *DataSharingHub* entity in [model 0705 Data Sharing](/types/7/0705-Data-Sharing) is a [collection](/types/0/0021-Collections) whose members are the data stores holding authoritative data that is available for sharing, provided the requester satisfies the requirements laid down by the data owner.

An architecture built around a hub also gives the business a picture it can reason about.  In the [new systems architecture](/practices/coco-pharmaceuticals/scenarios/defining-new-systems-architecture/overview) that Erin Overview and Peter Profile sketch for Coco Pharmaceuticals, the hub sits at the centre with labelled data flows to and from each business unit, so every business owner can see what their teams contribute and what they receive in return.  Captured as a [solution blueprint](/concepts/solution-blueprint), that picture becomes visible to a wider audience, tracks the progress of the implementation as components are linked to it, and - once operational - acts as the aggregation point for the statistics that show the data exchange is working.

### The Liskov Data Sharing Hub Manager

Maintaining a description of what a hub contains is exactly the sort of work that should not be done by hand.  The *Liskov Data Sharing Hub Manager* - named in recognition of [Barbara Liskov](https://en.wikipedia.org/wiki/Barbara_Liskov)'s work on data abstraction - is the [integration connector](/concepts/integration-connector) that does it.

Liskov detects each data sharing hub as it is created and begins monitoring the data stores that are members of it.  From their schemas it builds an abstracted [data dictionary](/concepts/data-dictionary), anchored to the hub, containing:

* **[Data fields](/concepts/data-field)** - the types of data value found in the hub.  A data field identifies *similar data in different data stores*, so a consumer asks for the data they want once, rather than once per store.
* **[Data structures](/concepts/data-structure)** - the groupings of those fields that reflect how the data is organized.

Relational databases, file folders and CSV files are all handled, and the dictionary is refreshed as the underlying stores change.  The point of the abstraction is to lift the description away from the technical implementation: a consumer selects from a dictionary of business-meaningful fields without needing to know which database or file holds them.

The generated dictionary is complete but bare - it has the fields and their types, and lacks the descriptions that explain what the values mean and where they come from.  That curation is left to the people who know.  The hub owner can add organizing folders of their own, and fill in the descriptions through the [Data Designer](/services/omvs/data-designer/overview) API or, more comfortably, by requesting a Markdown form from [Dr.Egeria](/user-interfaces/dr-egeria/overview), completing it with the help of colleagues, and loading it back.

Crucially, each entry in the dictionary stays linked to the schema elements it was derived from.  That linkage is what allows an automated pipeline to navigate from the fields a requester asked for to the actual tables and columns that hold them.

### Managing data sharing requests

A request for data is work, not just a record, so the *DataSharingRequest* entity is a type of [ToDo](/types/1/0135-Actions-For-People).  It tracks the status of the request and gathers its details: the [data specification](/concepts/data-specification) describing the data being asked for, the data sharing agreement, and the related resources.

This covers both directions of sharing.  A requester inside the organization can describe what they need and the purpose they need it for; a request from an external third party - who has no access to the hub itself - can be managed on their behalf, along with any conditions imposed by the contract between the organizations.

The benefit that turns out to matter most is auditability.  In the [patient data sharing hub](/practices/coco-pharmaceuticals/scenarios/patient-data-sharing-hub/overview) scenario, [Robbie Records](/practices/coco-pharmaceuticals/personas/robbie-records) is managing requests by hand: copying data into a new database per project, keeping a folder of documents describing each one, and exporting password-protected CSV files.  Reconstructing what happened for an auditor was a job in itself.  With the hub in place, the agreements, the users with access, and exactly what data was shared are all recorded as they happen, and the reports that demonstrate compliance can be produced on demand.

!!! summary "Usage"
    A data sharing hub turns ad-hoc data sharing into a managed service: a single description of what is on offer, a tracked request and agreement for each consumer, and a durable record of what was shared with whom.

## From data sharing hub to digital product

A data sharing hub and a digital product catalog answer different questions, and it is worth being clear about which problem you are solving.

A **data sharing hub** is about the data you already hold.  It gathers the authoritative data stores together, describes what they contain, and handles requests for that data one at a time.  Each request is negotiated: the requester says what they need and why, the owner decides what to release and under what conditions.  This is valuable in its own right, and it is a forgiving place to start, because nothing has to be perfect on day one.  The dictionary can begin as bare field names and gain its descriptions as people ask about them, and the stores can be groomed into genuinely authoritative sources over time, informed by what consumers actually turn out to need.

A **digital product** is about data you have decided to offer.  It is defined ahead of demand, conforms to a specification, carries a service level objective, and is delivered to subscribers on a schedule without anyone negotiating each time.  That is a stronger commitment, and it only pays back for data that enough people want.

This is why the hub makes such a good feeder for the product catalog.  As data sharing requests accumulate, they become evidence: the same fields requested by team after team, the same data set copied for project after project, the same conditions attached each time.  Those are the candidates worth promoting - the popular data sets where the effort of defining a product, committing to a refresh cycle and letting subscriptions run unattended replaces work that was being repeated by hand.  The dictionary entries, the curated descriptions and the terms and conditions gathered while handling individual requests are exactly the material a product definition needs.

This is the path [Robbie Records](/practices/coco-pharmaceuticals/personas/robbie-records) ends up on.  Once the patient data sharing hub is running, his reputation grows, he is asked to take ownership of more data sources, and the research teams petition for funding to expand what is on offer.  One of the results is a digital product catalog for the popular data sets - built on top of the hub, not instead of it.

## The Open Metadata Digital Product Catalog

The second half of the pattern turns the open metadata ecosystem's own content into something other teams can consume.

A [digital product](/concepts/digital-product) is a collection of digital resources produced for a particular consumer or purpose, conforming to a specification and offering guarantees of service - see [model 0710 Digital Products](/types/7/0710-Digital-Products).  Packaging metadata this way matters because it changes the terms of the exchange: rather than granting a team access to the repository and hoping they query it correctly, the metadata is published as a defined data set, with a stated refresh commitment, delivered to where they already work.

The *Open Metadata Digital Product Catalog* is Egeria's own catalog of such products, supplied by the `OpenMetadataDigitalProductsContentPack` and assembled by the [nanny connectors](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/nanny-connectors).

### The components

| Component | Role |
|-----------|------|
| **Jacquard Digital Product Loom** | An integration connector that harvests open metadata and weaves it into digital products, each presented as a [tabular data set](/concepts/tabular-data-set), organized into the product catalog.  Named for [Joseph Marie Jacquard](https://en.wikipedia.org/wiki/Joseph_Marie_Jacquard). |
| **Baudot Subscription Manager** | An integration connector that manages the subscriptions to those products, including issuing notifications to subscribers.  Named for [Emile Baudot](https://en.wikipedia.org/wiki/%C3%89mile_Baudot). |
| **Wedgwood Data Provisioner** | A [governance action service](/concepts/governance-action-service), called from Baudot, that provisions the product data into the destination the subscriber supplied.  Named for [Thomas Wedgwood](https://en.wikipedia.org/wiki/Thomas_Wedgwood_(photographer)). |
| **Babbage Analytical Engine** and **Lovelace Services** | An integration connector and the governance services it orchestrates, which analyse the content of open metadata and store the resulting insight as classifications.  These insights become the raw material for the observability products described below, and are covered by the [Metadata Insight](/patterns/metadata-insight/overview) pattern. |
| **External harvester connectors** | Harvest data from sources outside the ecosystem and record the resulting insight in open metadata for Jacquard to publish. |

### What is in the catalog

The catalog is a *DigitalProductCatalog* collection.  Alongside the products themselves it carries the material a consumer needs to make sense of them: a glossary of the terminology used (product basics, subscriptions, the semantics of the data items, and the questions the products can answer), the [perspectives](/types/1/0145-Perspectives) the products support, and a data dictionary describing the types of data field they contain.

The products are grouped into families:

| Product family | What it publishes |
|----------------|-------------------|
| Valid Metadata Value Sets | An extract per valid metadata value set, usable as standard reference values when building other products so that consumers can join data from several products together. |
| Reference Data Sets | An extract per reference data set managed in open metadata. |
| Open Metadata Types | Perspectives on the type system itself: the types, their attributes (including inherited ones), the properties and the data types. |
| Actors, Places and Products | The master data of the ecosystem - organizations, people, locations and digital products. |
| Survey Reports | The insight produced by [surveys](/concepts/survey-report): the reports, their annotations, requests for action, and the measurements collected from relational data managers, schemas, tables and columns, files, folders, resources and profiles. |
| Organization Observability | Insight into the activity of the organization as observed through the open metadata ecosystem. |
| Governance Observability | Governance controls, exceptions, certifications and licenses. |
| IT Operations Observability | The operational health of the infrastructure supporting the ecosystem, such as the software servers catalogued in open metadata. |
| Security Observability | The security settings supporting the ecosystem. |
| Secrets Observability | The secrets stores and secrets collections known to the ecosystem. |
| User Observability | The user identities and user accounts known to the ecosystem. |
| Governance Zone Observability | Zone membership totals and profiles, showing what each [governance zone](/concepts/governance-zone) controls the visibility of. |
| Service Observability | The servers, services and operations supporting the ecosystem, from a security perspective. |

Some families are populated dynamically: Jacquard generates a product for each valid metadata value set and each reference data set it finds, so the catalog grows with the ecosystem rather than needing to be redefined.

### Subscriptions and delivery

A consumer subscribes to a product rather than querying it.  Each product offers a choice of [subscription](/concepts/digital-subscription), each with its own service level objective:

| Subscription | Commitment |
|--------------|------------|
| Evaluation | The data is delivered to the destination once, so the product can be evaluated. |
| Daily refresh | The data is delivered once a day. |
| Weekly refresh | The data is delivered once a week. |
| Ongoing update | Updates reach the destination within an hour of the new data being received. |

Because every product is a tabular data set, it can be delivered into anything that holds tabular data - a CSV file, a database table, or a Kafka topic - and the subscriber names the destination.  Creating and cancelling a subscription are themselves governance actions, so the arrangement is recorded, auditable and repeatable.

Consumers browse and subscribe through the [Product Catalog](/services/omvs/product-catalog/overview) API, while the products and their families are defined and maintained through the [Product Manager](/services/omvs/product-manager/overview) API.

!!! summary "Usage"
    Publishing metadata as subscribed products means the teams who need it - analysts, auditors, platform owners, AI applications - receive current data in the form and place they already work, and the ecosystem gains a record of who is consuming what.

!!! info "Related information"

    * [Model 0705 Data Sharing](/types/7/0705-Data-Sharing) - the data sharing hub and data sharing request types.
    * [Model 0710 Digital Products](/types/7/0710-Digital-Products), [0711 Agreements](/types/7/0711-Agreements) and [0712 Digital Subscription](/types/7/0712-Digital-Subscription) - the digital product, agreement and subscription types.
    * [Data dictionary](/concepts/data-dictionary), [data field](/concepts/data-field) and [data structure](/concepts/data-structure) - the elements Liskov maintains.
    * [Tabular data set](/concepts/tabular-data-set) - the form every open metadata digital product takes.
    * [Metadata Insight](/patterns/metadata-insight/overview) - where the insight published by the observability products comes from.

--8<-- "snippets/abbr.md"
