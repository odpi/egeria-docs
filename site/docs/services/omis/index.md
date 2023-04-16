---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Open Metadata Integration Services (OMISs)

The integration services run in an [Integration Daemon](/concepts/integration-daemon) OMAG server.  Each type of integration service focuses on metadata exchange with a particular type of third party technology.

![Figure 1](/services/integration-daemon-in-action.svg)
> **Figure 1:** The integration daemon manages the automatic exchange of open metadata between third party technologies and Metadata Access Points or Metadata Servers that
are sharing this metadata across the Open Metadata Repository Cohorts that they are connected to

Each integration service provides a specialist API for the [integration connectors](/concepts/integration-connector) that it manages along with a context manager implementation that is used to set up the integration connectors inside the integration daemon.

![Figure 2](/services/integration-daemon-internals.svg)
> **Figure 2:** The integration services running in the integration daemon manage the integration connectors and supply them with a context that gives them access to the Egeria services they need.

The integration services available today are:

* [API Integrator](/services/omis/api-integrator/overview) - provides cataloguing for APIs.
* [Catalog Integrator](/services/omis/catalog-integrator/overview) - provides a two-way synchronization for data catalogs.
* [Database Integrator](/services/omis/database-integrator/overview) - provides metadata extraction from relational databases.
* [Display Integrator](/services/omis/display-integrator/overview) - provides metadata extraction from systems that provide user displays and forms to capture new data values.
* [Files Integrator](/services/omis/files-integrator/overview) - collects metadata about files stored in a filesystem or file manager.
* [Infrastructure Integrator](/services/omis/infrastructure-integrator/overview) - supports the extraction of metadata from IT infrastructure artifacts as well as the use of metadata to maintain IT infrastructure artifacts.
* [Lineage Integrator](/services/omis/lineage-integrator/overview) - collects metadata about processes, their internal logic and the data assets they work with.
* [Organization Integrator](/services/omis/organization-integrator/overview) - imports details of an organization's structure - such as teams and departments.
* [Search Integrator](/services/omis/search-integrator/overview) - supports the building of search indexes based on open metadata events.
* [Security Integrator](/services/omis/security-integrator/overview) - distributes security properties to access control enforcement points.
* [Stewardship Integrator](/services/omis/stewardship-integrator/overview) - exchanges requests for stewardship action (and results) with a human task manager.
* [Topic Integrator](/services/omis/topic-integrator/overview) - provides cataloguing of topics and event schema for event brokers.

??? education "Further information"

    * The operation of the integration daemon and the integration services within, along with details of how to set up these integration services are located in the [Administration Guide](/guides/admin/servers/configuring-an-integration-daemon).
    * [Writing integration connectors](/guides/developer/integration-connectors/overview) that use the integration services running in the integration daemon.

--8<-- "snippets/abbr.md"
