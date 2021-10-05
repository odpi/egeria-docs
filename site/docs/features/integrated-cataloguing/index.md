<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Integrated cataloging

It is possible to add metadata to a metadata repository using no automation beyond the management of the metadata once it is created.  Individuals enter information about the assets into Egeria through tools that call Egeria's [Open Metadata Access Services (OMASs)](/egeria-docs/services/omas).

The [Asset Owner OMAS](/egeria-docs/services/omas/asset-owner)
is the principle interface for such manual cataloguing.  It is possible to catalog any type of
asset through this interface although it is biased towards cataloging data assets such
as data stores, data feeds, files, data sets, APIs and events.

In addition there are specific cataloguing interfaces for particular types of subject matter expert.

* [IT Infrastructure OMAS](/egeria-docs/services/omas/it-infrastructure) provides specialist interfaces for cataloguing infrastructure such as servers, host systems and applications.

* [Digital Architecture OMAS](/egeria-docs/services/omas/digital-architecture) provides specialist interfaces for architects and integration engineers to manually catalog reference data sets and processes. Reference data sets are assets in their own right, and their content can be used as classifiers to augment the description of other assets. Processes are also assets that, when linked together, show the lineage of the assets they are partly responsible for maintaining.

Manual cataloguing works well for infrequent cataloguing.  However it is expensive and error prone when aiming to systematially catalog your digital landscape.
 
Integrated cataloging uses an [*integration daemon*]((/egeria-docs/concepts/integration-daemon)) to monitor a specific digital technology that hosts particular types of assets and automatically maintain the catalog with information about these assets.

For example, an integration daemon may be monitoring a database server, updating the asset catalog each time a new database is added, or a schema is changed.

Integration daemons support different integration patterns to meet the variety of capabilities of digital technologies.  For example, it may poll the technology or listen for events from it that indicate changes in the assets.  They are limited to the metadata supported by the technology they are working with.

## Other types of automation

Below are other types of automation to minimise the effort in managing your asset catalog.

* [Templated cataloguing](/egeria-docs/features/templated-cataloguing) - copying predefined assets.
* [Discovery and stewardship](/egeria-docs/features/discovery-and-stewardship) - analysis of asset contents to create metadata.


--8<-- "snippets/abbr.md"