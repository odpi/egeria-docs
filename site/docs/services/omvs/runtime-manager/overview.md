---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/tech-preview.md"

# Runtime Manager OMVS

The Runtime Manager Open Metadata View Services (OMVS) is a REST API designed to support user interfaces (UIs) and python environments that work with the Egeria infrastructure to:

* Display the status of an [OMAG Server Platform](/concepts/omag-server-platform), and which [OMAG Servers](/concepts/omag-server) are known/active to it.
* The status of an OMAG Server, its active history and the health of the components running within it.
* The status of the connectors an OMAG Server is hosting.

It is also able to:

* Activate/deactivate servers on a platform.
* For [metadata access stores](/concepts/metadata-access-store), it can:

    * Load [open metadata archives](/concepts/open-metadata-archive).
    * Connect and disconnect from connected [cohorts](/concepts/cohort-member).
  
* For [integration daemons](/concept/integration-daemon), it can:

   * Temporarily change integration connector configuration.
   * Restart and refresh integration connectors.
   * Send [open lineage events](/features/lineage-management/overview) for augmentation, analysis, and distribution through the open metadata ecosystem.
   * Refresh the server's integration group configuration stored in the connected metadata access server.
  
* For [engine hosts](/concepts/engine-host) it can:

   * Refresh the server's governance engine configuration stored in the connected metadata access server.
     

The Runtime Manager OMVS is able to work with any platform (and its hosted servers) that are reachable via REST APIs.  The calling user (provided they have sufficient security privileges) is able to work with the [platform services](/services/platform-services/overview), [server operation services](/services/server-operations), [integration daemon services](/services/integration-daemon-services) and [engine-host-services](/services/engine-host-services) as if they were calling them directly.  This allows remote management without needing to expose the back-end platforms' endpoints to the administrative users.

![Production Deployment](production-deployment.svg)

## Egeria's resource connectors

The secret to this service is that it works with Egeria's resource connectors that are responsible for making the calls.  

![Egeria resource connectors](egeria-system-connectors.svg)

These resource connectors are accessed via the catalog entries for the platforms and servers.  The catalog entries for the OMAG Server Platforms need to be created explicitly.  

---8<-- "snippets/abbr.md"






