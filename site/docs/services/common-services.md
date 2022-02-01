<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# OMAG Common Services (common-services)

This module provides common services to clients and the registered services that run in the [OMAG Server Platform](/concepts/omag-server-platform).

* **[First-Failure Data Capture (FFDC) Services](/services/ffdc-services)** - supports common exceptions and error handling.  It can but used by clients and server-side services.

* **[Multi-Tenant Services](/services/multi-tenant)** - supports the management of [Open Metadata and Governance (OMAG) Server](/concepts/omag-server) instances running in an [OMAG Server Platform](/concepts/omag-server-platform).

* **[Metadata Security](/services/metadata-security-services)** - supports authorization of access to OMAG Services and specific metadata instances.

* **[Generic Handlers](/services/generic-handlers)** - supports the management of specific types of open metadata elements.  The generic handlers provide services to translate OMAS requests built around that service's private beans into calls to the repository services (through the repository handler).

* **[Repository Handler](/services/repository-handler)** - supports access to multiple related metadata instances from the
[Open Metadata Repository Services (OMRS)](/services/omrs/overview). It manages the provenance checking, deduplication and translates OMRS exceptions into [Open Connector Framework (OCF)](/frameworks/ocf/overview) exceptions that are
used extensively across the [Open Metadata Access Services (OMASs)](/services/omas).

In addition, there is a shared metadata management module for
server-side services that make use of the beans defined in the OCF that underpins Egeria.

* **[OCF Metadata Management](/services/ocf-metadata-management)** - managing metadata about assets, connections and all of the different types of metadata defined in the asset properties in the [Open Connector Framework (OCF)](/frameworks/ocf/overview).

--8<-- "snippets/abbr.md"