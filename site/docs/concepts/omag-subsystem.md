---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Open Metadata and Governance (OMAG) Subsystems

A *subsystem* is a collection of components within a software server platform that supports one or more related services. Subsystems can be organized in a hierarchy where course-grained subsystems can be decomposed into more fine-grained subsystems.

The [OMAG Server Platform](/egeria-docs/concepts/omag-server-platform) is a collection of subsystems that support open metadata and governance services as well as its own operational needs.

## Fixed services

Fixed services that are always present in the platform:

- [Server Chassis](/egeria-docs/services/server-chassis) provides the main class of the OMAG Server Platform that manages the start up and shutdown of a platform instance.

- [Administration Services](/egeria-docs/services/admin-services) support the configuration and operation (such as starting and stopping) of [OMAG Servers](/egeria-docs/concepts/omag-servers).

- [First Failure Data Capture (FFDC) services](/egeria-docs/services/ffdc-services) support the capture of diagnostics.

- [Multi-tenant Services](/egeria-docs/services/multi-tenant) manages information about the running servers so REST API requests made to the platform can be routed to the correct server. 

- [Platform Operation Services](/egeria-docs/services/platform-services) retrieves information about a running platform instance and its associated servers.

- [Open Metadata Repository Services (OMRS)](/egeria-docs/services/omrs) for supporting access to metadata stored in metadata repositories and the exchange of metadata between repositories via an [open metadata repository cohort](/egeria-docs/concepts/cohort-member). The repository services are further divided into [OMRS subsystems](/egeria-docs/services/omrs/#omrs-subsystems) that can be activated independently.

- [Repository Handler](/egeria-docs/services/repository-handler) manages calls to the open metadata repositories through the `OMRSRepositoryConnector` interface.  It manages error handling, provenance of metadata, deduplication and effectivity dating

- [Metadata Security Services](/egeria-docs/services/metadata-security services) supports calls to the security connectors at appropriate points in the call path for REST APIs and event handling.

- [Generic Handlers](/egeria-docs/services/generic-handlers) manage the conversion between OMAS specific beans and OMRS beans as well as templating, management of anchors and calls to the metadata security services for assets and connections.  It uses the repository handler to access stored metadata.

- Governance server services:

    - [Data engine services](/egeria-docs/services/data-engine-proxy-services) implements the services for the [Data Engine Proxy](/egeria-docs/concepts/date-engine-proxy).
    - [Engine host services](/egeria-docs/services/engine-host-services) implements the services for the [Engine Host](/egeria-docs/concepts/engine-host).
    - [Integration daemon services](/egeria-docs/services/integration-daemon-services) implements the services for the [Integration Daemon](/egeria-docs/concepts/integration-daemon).
    - [Open lineage services](/egeria-docs/services/open-lineage-services) implements services for the [Open Lineage Server](/egeria-docs/concepts/open-lineage-server).
    
- [Connected Asset Services](/egeria-docs/services/ocf-metadata-management) for supporting the server-side REST API behind the `ConnectedAsset` interface of an OCF connector.






## Registered services

Dynamically registered services provide specialist APIs for particular technologies and user roles. Each of these services runs in their own subsystem independent of the other registered services. The implementation may come from Egeria or a third party. The links are to Egeria provided dynamic services.

- [Open Metadata Access Services (OMASs)](/egeria-docs/services/omas) for supporting domain-specific services for metadata access and governance. Access services run in the [metadata access server](metadata-access-server.md).

- [Open Metadata Engine Services (OMESs)](/egeria-docs/services/omes) for supporting specialized governance engines that drive governance activity in the open metadata ecosystem. The engine services run in the [engine host](engine-host.md) server.
- [Open Metadata Integration Services (OMISs)](/egeria-docs/services/omis) for supporting specific types of [integration connectors](integration-connector.md). The integration services run in the [integration daemon](integration-daemon.md) server.
- [Open Metadata View Services (OMVSs)](/egeria-docs/services/omvs) for supporting REST services for a User Interface (UI). The view services run in a [view server](view-server.md).

## Activating the OMAG subsystems

The [OMAG Server](/egeria-docs/concepts/omag-server) is a dynamic software server whose subsystems can be activated (or not) through the presence (or absence) of the subsystem's configuration properties in the OMAG Server's [configuration document](/egeria-docs/concepts/configuration-document).

--8<-- "snippets/abbr.md"
