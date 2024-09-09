---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Governance Engine Hosting Servers

An *engine host* is an [OMAG Server](/concepts/omag-server) that hosts one or more [governance engines](/concepts/governance-engine). Governance engines define collections of [governance services](/concepts/gpvernance-service) used to automate governance activity in the digital landscape. The governance services within the governance engines may access third party technology to perform their responsibilities or implement their behavior directly.

The engine host uses a [metadata access server](/concepts/metadata-access-server) to retrieve the [definitions of the governance engines](/governance-engine-definition) and the governance services within them. These definitions are retrieved through the [Governance Server OMAS](/services/omas/governance-server/overview). The Governance Server OMAS also manages the definition of [governance action processes](/concepts/governance-action-process) that choreograph calls to the services in a governance engine in order to implement technical controls in the governance program.

![Engine host in an OMAG Server ecosystem](engine-host.svg)

Typically, an engine host is deployed close to where the artifacts/resources/data are stored because it can generate a lot of network traffic when its services are running.  Multiple engine hosts may run the same governance engine to provide horizontal scalability.

The metadata interfaces needed by the governance engines are provided by the [Open Metadata Engine Services (OMES)](/services/omes) (or engine services for short). The engine services also run in the engine host.

--8<-- "snippets/concepts/governance-service-types.md"

The name and URL root of the server where the partner metadata service is running is needed to configure an engine service.  This is the metadata service used to access open metadata when a governance service runs.  The open metadata server configured for the engine host is used to retrieve the [governance engine definitions](/concepts/governance-engine-definition) for the governance engines configured for each engine service.    The metadata access servers used by the engine services does not need to be the same metadata server as the one used by the engine host server. This enables the management of metadata about the assets to be maintained close to the assets, and the definitions of the governance engines, services and processes to be maintained close to the governance team:

![Distribution of metadata managed by the engine host](distributed-engine-services-config.svg)

The engine host services have a REST API to query the status of the governance engines running in the engine services. The engine services also have a REST API to query specific details of their governance engines. All these REST APIs may be called by a [view server](/concepts/view-server) as part of the support for a user interface.

!!! education "Further information"

    - The capabilities of each of the engine services are described in the [engine services](/services/omes).
    - Configuring an engine host is described in the [Administration Guide](/guides/admin/servers/by-server-type/configuring-an-engine-host).

--8<-- "snippets/abbr.md"
