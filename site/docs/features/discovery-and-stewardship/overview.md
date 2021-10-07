<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2019. -->

# Metadata discovery and stewardship

[Integrated cataloguing](/egeria-docs/features/integraated-cataloguing) typically automates the creation the basic asset entry, its connection and
optionally, its schema.  This is what is called technical metadata.

Metadata discovery uses advanced analysis to inspect the content of specific assets to derive new insights that can augment or validate their catalog entry.

The results can either be automatically applied to the asset's catalog entry or it can go through a stewardship process to have a subject matter expert confirm the findings (or not).

Discovery and stewardship are the most advanced form of automation for asset cataloging. Egeria provides the server runtime environment and component framework to
allow third parties to create discovery services and governance action implementations. It has only simple implementations of these components, mostly for demonstration purposes.
This is the area where vendors and other open source projects are expected to provide additional value.

## Metadata Discovery

Metadata discovery is an automated process that extracts metadata about an
[asset](/egeria-docs/concepts/assets).
This metadata may be:
* embedded within the asset 
  * (for example a digital photograph has embedded metadata), or
* managed by the platform that is hosting the asset
  * (for example, a relational database platform maintains
schema information about the data store in its databases) or
* determined by analysing the content of the asset
  * (for example a metadata
discovery tool may analyse the data content to determine the types and range of values it contains and,
maybe determine a quality score for the data).

Some metadata discovery may occur when the asset is first cataloged. For example, the schema of an asset may be stored through the
[Data Manager OMAS](/egeria-docs/services/omas/data-manager) API.
This schema may have been automatically extracted by a
metadata extractor connector hosted in Egeria's Open Metadata Integration Services like [Database Integrator OMIS](/egeria-docs/services/omis/database-integrator) or [Files Integrator OMIS](/egeria-docs/services/omis/files-integrator).

Egeria also supports more advanced metadata discovery.

The [Open Discovery Framework (ODF)](/egeria-docs/frameworks/odf) has open APIs that define how automated discovery services can be managed and interact with an open metadata repository.
The metadata repository interfaces provide the metadata discovery service with:
 * the ability to manage discovery configuration,
 * a search function to locate assets in the metadata repository,
 * access all of the metadata known about each asset including its connector and
 * the ability to record the results of its analysis.

This metadata repository interface for metadata discovery tools is implemented by the [Discovery Engine OMAS](/egeria-docs/services/omas/discovery-engine).

Egeria is also able to host automated metadata discovery services that implement the ODF interfaces in its [Asset Analysis OMES](/egeria-docs/services/omes/asset-analysis).


--8<-- "snippets/abbr.md"