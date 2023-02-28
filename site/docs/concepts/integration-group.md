---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Integration Group

An *integration group* describes a collection of [integration connectors](/concepts/integration-connector) that are to run together in one or more [integration daemons](/concepts/integration-daemon).  The integration daemon is configured with a list of qualified names for various integration groups.  It retrieves the list of integration connectors in each of these groups from the open metadata ecosystem and starts to run them.  It continues to monitor for changes to the integration groups and their linked integration connectors, changing the connectors it is running as needed.  

??? education "Further information"

    Each integration group has a unique name.  An *IntegrationGroup* entity with a qualifiedName set to this unique name is created through the [Governance Engine OMAS](/services/omas/governance-engine/overview) API.  This API is also used to create and link the integration connector definitions into the integration group.

    The [integration group's qualifiedName is configured (/guides/admin/servers/configuring-an-integration-daemon/#configure-dynamic-integration-groups) in the [integration daemon](/concepts/integration-daemon).

    The open metadata types for this definition are in model [0464 - Dynamic Integration Groups](/types/4/0464-Dynamic-Integration-Groups) - specifically notice that *IntegrationGroup* and *IntegrationConnector* are linked by the *RegisteredIntegrationConnector* relationship.

--8<-- "snippets/abbr.md"