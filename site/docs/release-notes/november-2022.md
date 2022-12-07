<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# November 2022

This is November's monthly report from the Egeria community.  

## What is new in Egeria?

### Core Egeria

!!! info "Core Egeria Releases"
    [Release 3.13](/release-notes/3-13) was shipped in early November 2022.  The work this month is contributing to [Release 3.14](/release-notes/3-14).

#### Support for DEREGISTERED_REPOSITORY provenance type

The repository services now support the DEREGISTERED_REPOSITORY [provenance type](/features/metadata-provenance/overview) when elements are retrieved from the repository.  This value is set in the header of each element and indicates that it originated from a repository that is no longer registered with any connected cohorts.  It acts as a warning that this metadata is no longer being updated and may be out-of-date.

This required an update to the [Conformance Test Suite (CTS)](/guides/cts/overview) which was coding around this missing function.

### Connectors

#### Database support

The Generic JDBC connectors have been used to catalog a simple **[Trino](https://trino.io/)** database.  There is also ongoing testing of IBM's DB2 database.

#### Integration connectors

There is a new [sample integration connector](https://github.com/odpi/egeria-connector-integration-lineage-event-driven-sample) that listens on an event topic that is supplying proprietary lineage data and transforms and publishes it into the open metadata ecosystem.

### Data products

This month we clarified the relationship between a subject area and a data domain. See [Subject Area Domain](/concepts/subject-area/#subject-area-domain).

### Open Metadata Labs

The [open metadata labs](/education/open-metadata-labs/overview) are Jupyter Notebooks that allow you to issue commands to the Egeria APIs to explore various capabilities.  These are the latest updates and will run with Egeria 3.14 or later:

* **The Information Architecture Labs** - in the first information architecture lab, *Working with Standard Models*, Erin Overview is using the Cloud Information Model as a set of standard terms to clarify the new sales procedures needed for their personalized medicine business.
* **The Development Labs** - there are currently three development labs that show Erin and Peter giving education sessions to the software development team. These labs demonstrate the technical details and operation of various mechanisms in Egeria's software.

    * The *Metadata Representations Lab* shows how a database, event topic and an API are represented in open metadata.
    * The *Simple Cohort Demo Lab* shows how servers connect to an Open Metadata Repository Cohort to share metadata. It explains how trace the origin of a metadata element through its metadata collection id.
    * The *Governance Server Operation Lab* describes the operation on the Integration Daemon and the Engine Host governance servers.

* **The Asset Management Labs** - in the asset management labs  we look at how different roles work with the data lake and how Egeria's open metadata is captured, maintained and used.

    * The *Automated Curation Lab* shows Peter and Erin automating the cataloguing procedure described in Building a Data Catalog so that files are made available to Callie as soon as they arrive.  This lab has been redesigned to work with governance engine definitions that are loaded from an archive.  It required some fixes to Egeria Core and so requires Egeria 3.15-SNAPSHOT or later to run.
    * The *Improving Data Quality* and *Understanding an Asset* labs are still incomplete.

### Postman collections

No new postman collections this month.

### New documentation pages

Each month we select some new pages that where added/updated in the last month to [https://egeria-project.org](https://egeria-project.org) so you can keep up-to-date with how our website is evolving.

* [Metadata governance introduction](/patterns/metadata-governance/overview)
* [Building subject area materials](/practices/common-data-definitions/open-metadata-for-common-definitions)

## Egeria plans

### Moving to Gradle

Another reminder that the version 4.0 release will be gradle only. This build is successfully running on the V4.0 branch and testing of the resulting artifacts is underway.

## Community news

Congratulations to [Juergen Hemelt](https://github.com/juergenhemelt) who becomes our latest contributor.

## Events

### Metadata Governance Dojo

The big event this month was the new [Metadata Governance Dojo](/education/egeria-dojo/metadata-governance/overview).  We held two live sessions (3 hours each) and extended the discussion of the governance engines to one of the community calls.  The topics covered the philosophy and purpose of metadata governance, details of the operation of the [Integration Daemon](/concepts/integration-daemon) as well as [governance processes](/concepts/governance-action-process) and [services](/concepts/governance-service) running in the [Engine Host](/concepts/engine-host).  There are also sections on building the materials for a [subject area](/concepts/subject-area), [incident reporting](/concepts/incident-report), [lineage](/concepts/lineage) and [templated cataloguing](/features/templated-catalouing/overview).

### Community Meetings

Over the last few community meetings ...

* We reviewed the use cases and requirements for our Kubernetes support. Nigel Jones has [two helm charts](/guides/operations/kubernetes/overview) plus an operator in development.  We concluded that the helm charts should focus on helping people get Egeria up and running for demos, education and evaluation purposes.  The operator should focus on supporting production use.
* Juergen Hemelt described the connectors the Atruvia and IBM have built to support their cataloguing of event schemas and topics. [Recording](https://wiki.lfaidata.foundation/display/EG/2022-11-23+CM+-+Atruvia+demo+of+Event+schema+and+Dataskop+Egeria+Connectors)
* We reviewed the [content packs](https://github.com/odpi/egeria/tree/main/content-packs) that supply sample for the labs and default metadata for normal operations.

### Annual Project Review

The Egeria project annual review by the [Technical Advisory Board (TAC)](https://wiki.lfaidata.foundation/pages/viewpage.action?pageId=7733341) of the LF AI and Data foundation has moved to 9th March 2023.
Here are [the metrics for our community](https://landscape.lfai.foundation/?selected=egeria).

### Face-to-Face meeting

The next face-to-face meeting is in Amsterdam from 17th-19th January 2023.

### Dates for the winter break

The last community call this year will be 14th December 2022 when we will review the highlights of 2022.
We will back on 11th January 2023 with a demonstration of how to manage valid values for your metadata.

## Connecting with the project

!!! info "Connecting with the project"
    Go to our [community guide](/guides/community) to find out how to find out more about the activities of the Egeria project. 

--8<-- "snippets/abbr.md"
