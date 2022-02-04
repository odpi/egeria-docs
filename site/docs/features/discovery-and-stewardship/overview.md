<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2019. -->

# Metadata discovery and stewardship

[Integrated cataloguing](/features/integrated-cataloguing) typically automates the creation the basic asset entry, its connection and optionally, its schema.  This is what is called technical metadata.

Metadata discovery uses advanced analysis to inspect the content of specific assets to derive new insights that can augment or validate their catalog entry.

The results can either be automatically applied to the asset's catalog entry or it can go through a stewardship process to have a subject matter expert confirm the findings (or not).

Discovery and stewardship are the most advanced form of automation for asset cataloging. Egeria provides the server runtime environment and component framework to allow third parties to create discovery services and governance action implementations. It has only simple implementations of these components, mostly for demonstration purposes. This is an area where vendors and other open source projects are expected to provide additional value.

## Metadata Discovery

Metadata discovery is an automated process that extracts metadata about a [digital resource](/concepts/resource). This metadata may be:

* embedded within the asset (for example a digital photograph has embedded metadata), or
* managed by the platform that is hosting the asset (for example, a relational database platform maintains schema information about the data store in its databases) or
* determined by analysing the content of the asset (for example a metadata discovery tool may analyse the data content to determine the types and range of values it contains and, maybe from that analysis, determine a quality score for the data).

Some metadata discovery may occur when the resource is first catalogued as an [asset](/concepts/asset). For example, the schema of a database may be catalogued through the [Data Manager OMAS](/services/omas/data-manager/overview) API. This schema may have been automatically extracted by an integration connector hosted in Egeria's [Database Integrator OMIS](/services/omis/database-integrator/overview).

Egeria also supports more advanced metadata discovery.

The [Open Discovery Framework (ODF)](/frameworks/odf/overview) has open APIs that define how automated discovery services can be operated and the resulting analysis stored in an open metadata repository. The metadata repository interfaces provide the metadata discovery service with:

 * the ability to manage discovery configuration,
 * a search function to locate assets in the metadata repository,
 * access to all of the metadata known about each asset including its connector and
 * the ability to record the results of its analysis.

This metadata repository interface for metadata discovery tools is implemented by the [Discovery Engine OMAS](/services/omas/discovery-engine).

Egeria is also able to host automated metadata discovery services that implement the ODF interfaces in its [Asset Analysis OMES](/services/omes/asset-analysis).

## Managing governance engine configuration

--8<-- "snippets/abbr.md"