<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Integration Guide

Many tools and platforms today maintain a store of metadata.  This metadata drives the behaviour of the technology.  For example, a database server maintains the structure of its databases in a schema catalog.  This schema is used to structure queries and optimize the extraction of data.  Many tools that enable their users to work with data keep metadata about the known data sources.  This helps their users find the data they need and to work with it.  The example below shows an analytics workbench that data scientists may use to build analytics models. 

![Third party technology metadata](third-party-metadata.svg)

Egeria's integration guide helps you to integrate third party technologies into the open metadata ecosystem.  The technology may be an open source technology, a home-grown technology or a software product.  This does not matter.  The integration may be to import metadata into the open metadata ecosystem, or to export it to the third party technology, or both. Egeria's integration capabilities are extremely flexible. The only limitations to metadata exchange between a third party technology and the open metadata ecosystem derive from the capabilities of the external APIs and events provided by the third party technology.


--8<-- "docs/guides/integration/metadata-supply-chains.md"

--8<-- "docs/guides/integration/introducing-integration-daemon.md"

--8<-- "docs/guides/integration/configuring-integration-daemon.md"

--8<-- "docs/guides/integration/types-of-metadata-repository.md"

## Integrating Asset Managers (catalogs)

The [Asset Manager OMAS](/services/omas/asset-manager-overview) (in conjunction with the [Catalog Integrator OMIS](/services/omis/catalog-integrator/overview)) provides a new integration path for asset managers that goes via an integration service hosted in an [integration daemon](/concepts/integration-daemon).

Catalogs will be able to have a two-way integration through this path without needing to conform to the repository service rules for managing home and reference copies. This is possible for two reasons:

* Since the metadata from the catalog passes through an OMAS, Egeria will be able to have a better control of the metadata from the catalog.
* Since the catalog is not part of a federated query, any inconsistent updates to metadata that occurs in its repository, only impacts the users of that catalog and not the whole cohort.

--8<-- "docs/guides/integration/validating-your-integration.md"


--8<-- "snippets/abbr.md"
