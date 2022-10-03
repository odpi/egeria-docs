<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Integration Guide

The integration guide helps you to integrate a new technology into the open metadata ecosystem.  This may be an open source technology, a home-grown technology or a software product.


## Integrating Asset Managers (catalogs)

The [Asset Manager OMAS](/services/omas/asset-manager-overview) (in conjunction with the [Catalog Integrator OMIS](/services/omis/catalog-integrator/overview)) provides a new integration path for asset managers that goes via an integration service hosted in an [integration daemon](/concepts/integration-daemon).

Catalogs will be able to have a two-way integration through this path without needing to conform to the repository service rules for managing home and reference copies. This is possible for two reasons:

* Since the metadata from the catalog passes through an OMAS, Egeria will be able to have a better control of the metadata from the catalog.
* Since the catalog is not part of a federated query, any inconsistent updates to metadata that occurs in its repository, only impacts the users of that catalog and not the whole cohort.


--8<-- "snippets/abbr.md"
