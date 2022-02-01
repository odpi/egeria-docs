<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Integrated cataloging

## Why automate?

It is possible to add metadata to a metadata repository using no automation beyond the management of the metadata once it is created.  Individuals enter information about digital resources and associates intellectual property into Egeria through tools that call Egeria's [Open Metadata Access Services (OMASs)](/services/omas).

The [Asset Owner OMAS](/services/omas/asset-owner) is the principle interface for manual cataloguing of digital resources.  It is possible to catalog any type of digital resource through this interface although it is biased towards cataloging data sources such as data stores, data feeds, files, data sets, APIs and events.  The digital resources are represented in the catalog as [assets](/concepts/asset).

In addition there are specific cataloguing interfaces for particular types of subject matter expert.

* [IT Infrastructure OMAS](/services/omas/it-infrastructure) provides specialist interfaces for cataloguing infrastructure such as servers, host systems and applications.

* [Digital Architecture OMAS](/services/omas/digital-architecture) provides specialist interfaces for architects and integration engineers to manually catalog [reference data sets](/features/reference-data-management) and processes. Reference data sets are assets in their own right, and their content can be used as classifiers to augment the description of other assets. Processes are also assets that, when linked together, show the [lineage](/features/lineage-management) of the assets they are partly responsible for maintaining.

Manual cataloguing works well for infrequent cataloguing.  However it is expensive and error prone when aiming to systematically catalog your digital landscape since it is complex and continually changing.

## How does integrated cataloguing work?

`Integrated cataloging` uses an [*integration daemon*]((/concepts/integration-daemon)) to monitor a specific digital technology that hosts particular types of digital resources and then automatically maintain the metadata descriptions of these digital resources in the catalog.

![Figure 1](/concepts/integration-daemon-in-action.svg)
> **Figure 1:** The integration daemon manages the automatic exchange of open metadata between third party technologies and Metadata Access Servers that are sharing this metadata across the Open Metadata Repository Cohorts that they are connected to

For example, an integration daemon may be monitoring a database server, updating the metadata catalog each time a new database is added, or a schema is changed.

Inside the integration daemon are the [Open Metadata Integration Services (OMISs)](/services/omis) that provide specialist interfaces to [integration connectors](/concepts/integration-connector).  

Integration connectors support different [integration patterns](/patterns/metadata-exchange) to meet the variety of capabilities of digital technologies.  For example, it may poll the technology or listen for events from it that indicate changes in the assets.  They are limited to the metadata supported by the technology they are working with.  However, typically the integration connectors are able to capture `technical metadata` that includes the name of the digital resource (stored in the [asset](/concepts/asset)) and the structure of the data fields within it (if any).  This structure is described in a [schema](/concepts/schema).  It may be possible to also extract, or derive the connection information required to connect to the digital resource.  This is stores in a [connection](/concepts/connection).

## Other types of automation

Below are other types of automation to minimise the effort in managing your asset catalog.

* [Templated cataloguing](/features/templated-cataloguing) - copies the values from an existing catalogued asset into the catalog entry for a new asset. This can reduce the opportunities for error where similar assets are being catalogued.  It can be used both in manual cataloguing and integrated cataloguing.
* [Discovery and stewardship](/features/discovery-and-stewardship) - analyses the contents of a digital resource to discover metadata and attach it as annotations to the corresponding asset in the catalog.


--8<-- "snippets/abbr.md"