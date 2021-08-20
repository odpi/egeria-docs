<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2019. -->

# Connectors Overview

A [*connector*](/egeria-docs/frameworks/ocf/#connector) is a Java class that supports the standard [Open Connector Framework (OCF)](/egeria-docs/frameworks/ocf) APIs. It is a client to a third party technology: Egeria calls the connector, and the connector translates these calls into requests to the third party technology.

Some connectors are also able to listen for notifications from the third party technology: when a notification is received, the connector converts its content into a call to Egeria to distribute the information to the open metadata ecosystem.

Egeria has a growing collection of connectors to third party technologies. These connectors help to accelerate the rollout of your open metadata ecosystem since they can be used to automate the extraction and distribution of metadata to the third party technologies.

Connectors enable Egeria to operate in many environments and with many types of third party technologies, just by managing the configuration of the [OMAG servers](/egeria-docs/concepts/omag-server). This allows new implementations to be provided and plugged-in over time, without changing the core code of Egeria itself.

Connector implementations supplied by the Egeria community can be broadly organized into three categories:

## Runtime connectors

*Runtime* connectors support Egeria's runtimes:

| Type | Description |
|---|---|
| Event bus connectors | |
| [Cohort registry store connectors](cohort-registry-store) | |
| [Configuration store connectors](configuration-store) | |
| [Audit log destination connector connectors](audit-log-destination) | |
| [Audit log store connectors](audit-log-store-connector.md) | support the reading and writing of audit log records to specific destinations on behalf of the [audit log](/egeria-docs/concepts/audit-log) |
| [Open metadata archive store connectors](open-metadata-archive-store) | |
| REST client connectors | |
| Cohort member remote repository connectors | |
| [OMRS topic connectors](omrs-topic-connector.md) | manage the exchange of [OMRS events](/egeria-docs/services/omrs/metadata-events/#omrs-events) with the [OMRS topic(s)](/egeria-docs/services/omrs/metadata-events/#omrs-event-topic) by calling the [open metadata topic connector](open-metadata-topic-connector.md) |
| [Open metadata archive store connectors](open-metadata-archive-store-connector.md) | support the reading and writing of [open metadata archives](/egeria-docs/concepts/open-metadata-archive) on behalf of the [archive manager](/egeria-docs/concepts/archive-manager) |
| [Open metadata topic connectors](open-metadata-topic-connector.md) | manage the calls to the [event bus](/egeria-docs/concepts/event-bus) to support specific topic connectors such as the OMRS topic connector described above |
| [Cohort registry store connector](cohort-registry-store-connector.md) | support the reading and writing of the cohort registry store to specific destinations on behalf of the [cohort registry](/egeria-docs/services/omrs/cohort/#cohort-registry) |

## Exchange connectors

*Exchange* connectors support the exchange and maintenance of metadata:

| Type | Description |
|---|---|
| [Integration connectors](integration) | manage the metadata exchange to a third party technology through an [integration service](/egeria-docs/services/omis) |
| [Repository connectors](repository) | integrate metadata repositories through the [repository services](/egeria-docs/services/omrs): either with native support for the open metadata types and instances or that map to a third party metadata repository API, in which case they are often paired with an event mapper connector |
| [Event mapper connectors](event-mapper-connector.md) | inform a cohort of changes to metadata homed in a third party metadata repository that occurred through the third party technology's own mechanisms |
| [Discovery services](discovery) | analyze the content of resources in the digital landscape and create annotations that are attached to the resource's [asset](/egeria-docs/concepts/asset) metadata element in the open metadata repositories in the form of an open discovery report |
| [Governance action services](governance-action) | perform monitoring of metadata changes, validation of metadata, triage of issues, assessment and/or remediation activities on request |

## Data connectors

*Data* connectors provide access to digital resources and their metadata that is stored in the open metadata ecosystem.

--8<-- "snippets/abbr.md"
