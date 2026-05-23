
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# Runtime Manager API

he Runtime Manager API enables the caller to retrieve configuration and status from platforms and servers.
It is also used to manage the lifecycle of servers, their registration in cohorts and the loading
of open metadata archives.

## Key Features

Key features of the API include:

* **Platform Management**: Retrieving configuration and status (reports) from OMAG Server Platforms.
* **Server Management**: Retrieving configuration and status (reports) from OMAG Servers.
* **Server Lifecycle Management**: Activating and shutting down OMAG Servers using stored configuration.
* **Cohort Management**: Managing open metadata repository cohorts and their members, including connecting, disconnecting, and unregistering servers.
* **Archive Management**: Loading open metadata archives into running repositories.
* **Engine and Integration Management**: Refreshing configuration for governance engines and integration daemons, and managing integration connectors (configuration properties, endpoints, and connections).
* **Open Lineage Support**: Publishing open lineage events to the integration service.

Sample REST API requests can be found in the
[Egeria-api-runtime-manager.http](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/view-services/runtime-manager/Egeria-api-runtime-manager.http) file.
In addition

* [Egeria-load-content-packs.http](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/view-services/runtime-manager/Egeria-load-content-packs.http) illustrates how to load a content pack in a running system.
* [Egeria-omag-server-reports.http](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/view-services/runtime-manager/Egeria-omag-server-reports.http) illustrates how to retrieve reports from a running Egeria platform.
* [Egeria-baudot-tabular-data-sets.http](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/view-services/runtime-manager/Egeria-baudot-tabular-data-sets.http) illustrates how to retrieve tabular data sets supporting the Open Metadata Digital Products from a running Egeria platform.

## Further Information

* [OMAG Server Platform](/concepts/omag-server-platform/)
* [OMAG Server](/concepts/omag-server/)
* [Cohort](/concepts/cohort-member/)
* [Open Metadata Archive](/concepts/open-metadata-archive/)
* [Governance Engine](/concepts/governance-engine/)
* [Integration Connector](/concepts/integration-connector/)


## API Overview

The Runtime Manager API is a REST API designed to support user interfaces (UIs) and python environments that work with the Egeria infrastructure to:

* Display the status of an [OMAG Server Platform](/concepts/omag-server-platform), and which [OMAG Servers](/concepts/omag-server) are known/active to it.
* The status of an OMAG Server, its active history and the health of the components running within it.
* The status of the connectors an OMAG Server is hosting.

It is also able to:

* Activate/deactivate servers on a platform.
* For [metadata access stores](/concepts/metadata-access-store), it can:

    * Load [open metadata archives](/concepts/open-metadata-archive).
    * Connect and disconnect from connected [cohorts](/concepts/cohort-member).
  
* For [integration daemons](/concepts/integration-daemon), it can:

   * Temporarily change integration connector configuration.
   * Restart and refresh integration connectors.
   * Send [open lineage events](/features/lineage-management/overview) for augmentation, analysis, and distribution through the open metadata ecosystem.
   * Refresh the server's integration group configuration stored in the connected metadata access server.
  
* For [engine hosts](/concepts/engine-host) it can:

   * Refresh the server's governance engine configuration stored in the connected metadata access server.
     

The Runtime Manager API is able to work with any platform (and its hosted servers) that are reachable via REST APIs.  The calling user (provided they have sufficient security privileges) is able to work with the [platform services](/services/platform-services/overview), [server operation services](/services/server-operations), [integration daemon services](/services/integration-daemon-services) and [engine-host-services](/services/engine-host-services) as if they were calling them directly.  This allows remote management without needing to expose the back-end platforms' endpoints to the administrative users.

![Production Deployment](production-deployment.svg)

## Egeria's resource connectors

The secret to this service is that it works with Egeria's resource connectors that are responsible for making the calls.  

![Egeria resource connectors](egeria-system-connectors.svg)

These resource connectors are accessed via the catalog entries for the platforms and servers.  The catalog entries for the OMAG Server Platforms need to be created explicitly.  

---8<-- "snippets/abbr.md"






