<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2019. -->

# Connectors overview

A **connector** is a Java class that supports the standard [Open Connector Framework (OCF)](/egeria/frameworks/ocf)
APIs. The [Open Metadata Repository Services (OMRS)](/egeria/services/omrs) defines the following connectors to enable
support for specific operating platform services to be plugged into the OMRS:

- [Audit log store connector](audit-log-store-connector.md) - supports the reading and writing of
  audit log records to specific destinations on behalf of the [OMRS Audit Log](/egeria/concepts/audit-log).
- [Cohort registry store connector](cohort-registry-store-connector.md) - supports the
  reading and writing of the cohort registry store to specific destinations on behalf of
  the [cohort registry](/egeria/services/omrs/cohort/#cohort-registry).
- [Event mapper connector](event-mapper-connector.md) - informs a cohort
  of changes to metadata mastered in a third party metadata repository that
  occurred through the third party technology's own mechanisms.
  It is always paired with the repository connector for
  the third party technology.
- [OMRS topic connector](omrs-topic-connector.md) - manages the exchange 
  of [OMRS Events](/egeria/services/omrs/metadata-events/#omrs-events) with
  the [OMRS topic(s)](/egeria/services/omrs/metadata-events/#omrs-event-topic) by calling
  the [open metadata topic connector](open-metadata-topic-connector.md).
- [Open metadata archive store connector](open-metadata-archive-store-connector.md) - supports the
  reading and writing of [open metadata archives](/egeria/concepts/open-metadata-archive)
  on behalf of the [archive manager](/egeria/concepts/archive-manager).
- [Open metadata topic connector](open-metadata-topic-connector.md) - manages
  the calls to the [event bus](/egeria/concepts/event-bus) to support
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
the [Open Connector Framework (OCF)](/egeria/frameworks/ocf)
which means the OMRS uses the 
OCF [connector broker](/egeria/concepts/connector-broker)
to create the instances of the connectors it needs.
The type of connector needed is defined in a connection object.

The connection objects for OMRS's connectors are defined in the
OMAG server [configuration document](/egeria/concepts/configuration-document) that is passed to the
server when the open metadata services are activated.

This means that new implementations can be specified without needing
to change the OMRS code.

--8<-- "snippets/abbr.md"
