<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2021,2022. -->

# Metadata discovery and stewardship

Metadata discovery is an automated process that extracts metadata about a [digital resource](/concepts/resource). This metadata may be:

* embedded within the asset (for example a digital photograph has embedded metadata), or
* managed by the platform that is hosting the asset (for example, a relational database platform maintains schema information about the data store in its databases) or
* determined by analysing the content of the asset (for example a quality tool may analyse the data content to determine the types and range of values it contains and, maybe from that analysis, determine a quality score for the data).

Some metadata discovery may occur when the digital resource is first catalogued as an [asset](/concepts/asset).  [Integrated cataloguing](/features/integrated-cataloguing) typically automates the creation the basic asset entry, its connection and optionally, its schema.  This is sometimes called *technical metadata*.  

??? example "Cataloguing database with integrated cataloguing"
    For example, the schema of a database may be catalogued through the [Data Manager OMAS](/services/omas/data-manager/overview) API. This schema may have been automatically extracted by an integration connector hosted in Egeria's [Database Integrator OMIS](/services/omis/database-integrator/overview).

The [*open discovery services*](/concepts/open-discovery-service) build on this initial cataloguing. They use advanced analysis to inspect the *content* of a digital resource to derive new insights that can augment or validate their catalog entry.

The results of this analysis is added to a [discovery analysis report](/concepts/discovery-analysis-report) linked off of the asset.

![Asset with discovery analysis reports](/guides/developer/open-discovery-services/asset-to-discovery-analysis-reports.svg)
> Each time an open discovery service runs to analyse a digital resource, a new discovery analysis report is created and attached to the resource's asset.  If the open discovery service is run regularly, it is possible to track how the contents are changing over time.

The analysis results documented in the discovery analysis report can either be automatically applied to the asset's catalog entry or it can go through a *stewardship process* where a subject-matter expert confirms the findings (or not).  

Discovery and stewardship are the most advanced form of automation for asset cataloging. Egeria provides the server runtime environment and component framework to allow third parties to create discovery services and governance action implementations. It has only simple implementations of these components, mostly for demonstration purposes. This is an area where vendors and other open source projects are expected to provide additional value.

## Open discovery services

Open discovery services run in the [Asset Analysis OMES](/services/omes/asset-analysis) that is hosted in a [Engine Host](/concepts/engine-host).  The metadata repository interface for metadata discovery tools is implemented by the [Discovery Engine OMAS](/services/omas/discovery-engine).

![Open Discovery Service](/connectors/discovery/discovery-service.svg)

--8<-- "docs/guides/developer/open-discovery-services/operation-of-a-discovery-service.md"

## Inside the discovery analysis report

The discovery analysis report structures the annotations in two ways:

* Annotations that describe a characteristic of the whole digital resource.
* Annotations that describe a characteristic of a single data field within the digital resource.

![Discovery analysis report structure](/guides/developer/open-discovery-services/discovery-analysis-report-structure.svg)

## Discovery actions

### Schema extraction

*Schema extraction* established the data fields discovered in the digital resource and if the schema is attached to the asset, it will attempt to match the data fields it finds to its schema attributes.

![Open discovery schema extraction](/guides/developer/open-discovery-services/open-discovery-schema-extraction.svg)

### Data Profiling

![Open discovery data profiling](/guides/developer/open-discovery-services/open-discovery-data-profiling.svg)

### Data class discovery

![Data class discovery](/guides/developer/open-discovery-services/open-discovery-data-class-discovery.svg)

### Semantic discovery

![Semantic discovery](/guides/developer/open-discovery-services/open-discovery-semantic-discovery.svg)

### Classification discovery

![Classification discovery](/guides/developer/open-discovery-services/open-discovery-classification-discovery.svg)

### Calculating quality scores

![Quality Scores](/guides/developer/open-discovery-services/open-discovery-quality-scores.svg)

### Relationship discovery

![Relationship discovery](/guides/developer/open-discovery-services/open-discovery-relationship-discovery.svg)

### Capturing measurements

![Data source measurements](/guides/developer/open-discovery-services/open-discovery-data-source-measurements.svg)

### Requesting stewardship action

![Request for action](/guides/developer/open-discovery-services/open-discovery-request-for-action.svg)

## Working with external engines

Open discovery services may directly implement the analysis function or may invoke an external service to create the annotations.

!!! education "Further information"
    * [Open discovery services supplied by the Egeria project](/connectors/#open-discovery-services)
    * [Writing your own open discovery services](/guides/developer/open-discovery-services/overview)

--8<-- "snippets/abbr.md"