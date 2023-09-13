<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# 0057 Software Services

![UML](0057-Software-Services.svg)

## SoftwareService

A *SoftwareService* provides a well-defined software component that can be called by remote clients across the network. They may offer a request-response or an event-driven interface or both.

## ApplicationService

Typically, software services implement specific business functions such as on-boarding a new customer, taking an order or sending an invoice. These are called *ApplicationService`s*

## SecurityService

A *SecurityService* service describes a server that provides security services.  The [Policy Management Classifications](/types/4/0435-Policy-Management-Capabilities) define the role that the service is playing in the security architecture.

## Open Metadata and Governance Services

Egeria offers specialized software services related to the capture and management of open metadata. These are shown as specialist types:

### MetadataIntegrationService

A *MetadataIntegrationService* describes an [Open Metadata Integration Service (OMIS)](/services/omis) that runs in an [integration daemon](/concepts/integration-daemon).

### MetadataAccessService

A *MetadataAccessService* describes an [Open Metadata Access Service (OMAS)](/services/omas) that runs in a [metadata access point](/concepts/metadata-access-point).

### EngineHostingService

An *EngineHostingService* describes an [Open Metadata Engine Service (OMES)](/services/omes) that runs in an [engine host](/concepts/engine-host).

### UserViewService

A *UserViewService* describes an [Open Metadata View Service (OMVS)](/services/omvs) that runs in a [view server](/concepts/view-server).

### EnterpriseAccessLayer

A *EnterpriseAccessLayer* describes the enterprise repository services provided by the [Open Metadata Repository Services (OMRS)](/services/omrs) that runs in a [Metadata Access Server](/concepts/metadata-access-server).

### MetadataRepositoryService

A *MetadataRepositoryService* service describes the services provided by the [Open Metadata Repository Services (OMRS)](/services/omrs) that provides access to a metadata repository, either local or remote.  It could be a [Metadata Access Server](/concepts/metadata-access-server), [Repository Proxy](/concepts/repository-proxy) or a third party metadata service.

### CohortMember

A *CohortMember* service describes the cohort services provided by the [Open Metadata Repository Services (OMRS)](/services/omrs) that runs in a [cohort member server](/concepts/cohort-member).


--8<-- "snippets/abbr.md"
