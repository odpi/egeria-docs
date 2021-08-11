<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2019. -->

# Connectors overview

A [**connector**](/egeria-docs/concepts/connector) is a Java class that supports the standard [Open Connector Framework (OCF)](/egeria-docs/frameworks/ocf)
APIs. It is a client to a third party technology: Egeria alls the connector, and the connector translates these
calls into requests to the third party technology.

Some connectors are also able to listen for notifications from the third party technology: when a notification
is received, the connector converts its content into a call to Egeria to distribute the information to the
open metadata ecosystem.

## Catalog

Egeria has a growing collection of connectors to third party technologies.
These connectors help to accelerate the rollout of your open metadata
ecosystem since they can be used to automate the extraction and
distribution of metadata to the third party technologies.

Connectors enable Egeria to operate in many environments
and with many types of third party technologies, just by managing the configuration of the [OMAG servers](/egeria-docs/concepts/omag-server).

The catalog here lists the connector implementations supplied by the Egeria community,
organized into three broad categories:

- [Exchange connectors](exchange) support the exchange and maintenance of metadata. This includes integration connectors,
  repository connectors, discovery services and governance action services.
- [Runtime connectors](runtime) support Egeria's runtimes. This includes event bus connectors, cohort registry stores,
  configuration stores, audit log destination connectors, open metadata archive stores, REST client connectors and cohort
  member remote repository connectors
- [Data connectors](data) provide access to digital resources and their metadata that is stored in the open metadata
  ecosystem.

## Repository services use

The [Open Metadata Repository Services (OMRS)](/egeria-docs/services/omrs) defines the following connectors to enable
support for specific operating platform services to be plugged into the OMRS:

- [Audit log store connector](audit-log-store-connector.md) - supports the reading and writing of
  audit log records to specific destinations on behalf of the [audit log](/egeria-docs/concepts/audit-log).
- [Cohort registry store connector](cohort-registry-store-connector.md) - supports the
  reading and writing of the cohort registry store to specific destinations on behalf of
  the [cohort registry](/egeria-docs/services/omrs/cohort/#cohort-registry).
- [Event mapper connector](event-mapper-connector.md) - informs a cohort
  of changes to metadata mastered in a third party metadata repository that
  occurred through the third party technology's own mechanisms.
  It is always paired with the repository connector for
  the third party technology.
- [OMRS topic connector](omrs-topic-connector.md) - manages the exchange 
  of [OMRS Events](/egeria-docs/services/omrs/metadata-events/#omrs-events) with
  the [OMRS topic(s)](/egeria-docs/services/omrs/metadata-events/#omrs-event-topic) by calling
  the [open metadata topic connector](open-metadata-topic-connector.md).
- [Open metadata archive store connector](open-metadata-archive-store-connector.md) - supports the
  reading and writing of [open metadata archives](/egeria-docs/concepts/open-metadata-archive)
  on behalf of the [archive manager](/egeria-docs/concepts/archive-manager).
- [Open metadata topic connector](open-metadata-topic-connector.md) - manages
  the calls to the [event bus](/egeria-docs/concepts/event-bus) to support
  specific topic connectors such as the OMRS topic connector described above.
- [Repository connector](repository-connector.md) - defines the open metadata common interface
  to a metadata repository. This may be a repository with
  native support for the open metadata types and instances or
  one that is mapping to a third party metadata repository API.
  In the case of it supporting a third party metadata repository,
  it is often paired with an event mapper connector described above.

The OMRS defines the interfaces for these connectors and selected implementations
are located in the [adapters :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/repository-services-connectors){ target=gh }
package.

All of these connectors support
the [Open Connector Framework (OCF)](/egeria-docs/frameworks/ocf)
which means the OMRS uses the 
OCF [connector broker](/egeria-docs/concepts/connector-broker)
to create the instances of the connectors it needs.
The type of connector needed is defined in a connection object.

The connection objects for OMRS's connectors are defined in the
OMAG server [configuration document](/egeria-docs/concepts/configuration-document) that is passed to the
server when the open metadata services are activated.

This means that new implementations can be specified without needing
to change the OMRS code.

--8<-- "snippets/abbr.md"
