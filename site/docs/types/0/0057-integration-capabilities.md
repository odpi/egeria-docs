<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# 0057 Integration Capabilities

![UML](0057-integration-capabilities.svg)

## SoftwareService

A *`SoftwareService`* provides a well-defined software component that can be called by remote clients across the network. They may offer a request-response or an event-driven interface or both.

Typically, software services implement specific business functions such as on-boarding a new customer, taking an order or sending an invoice. Egeria offers specialized software services related to the capture and management of open metadata. These are shown as specialist types:

### MetadataIntegrationService

A *`MetadataIntegrationService`* describes an [Open Metadata Integration Service (OMIS)](/egeria-docs/services/omis) that runs in an [integration daemon](/egeria-docs/concepts/integration-daemon).

### MetadataAccessService

A *`MetadataAccessService`* describes an [Open Metadata Access Service (OMAS)](/egeria-docs/services/omas) that runs in a [metadata access point](/egeria-docs/concepts/metadata-access-point).

### EngineHostingService

An *`EngineHostingService`* describes an [Open Metadata Engine Service (OMES)](/egeria-docs/services/omes) that runs in an [engine host](/egeria-docs/concepts/engine-host).

### UserViewService

A *`UserViewService`* describes an [Open Metadata View Service (OMVS)](/egeria-docs/services/omvs) that runs in a [view server](/egeria-docs/concepts/view-server).

--8<-- "snippets/abbr.md"
