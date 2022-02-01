<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2019. -->

# Connectors consumed by the OMRS

A Connector is a Java class that supports the standard [Open Connector Framework (OCF)](/frameworks/ocf/overview) APIs. The Open Metadata Repository Services (OMRS) defines the following connectors to enable support for specific operating platform services to be plugged into the OMRS.

* **[Audit Log Destination Connector](/concepts/audit-log-destination-connector)** - supports the reading and writing of audit log records to specific destinations on behalf of the **[OMRS Audit Log](/concepts/audit-log**.

* **[Cohort Registry Store Connector](/concepts/cohort-registry-store-connector)** - supports the reading and writing of the cohort registry store to specific destinations on behalf of the **[Cohort Registry](/services/omrs/cohort-registry)**.

* **[Event Mapper Connector](/concepts/event-mapper-connector)** - informs a cohort of changes to metadata mastered in a third party metadata repository that occurred through the third party technology's own mechanisms. It is always paired with the repository connector for the third party technology.

* **[OMRS Topic Connector](/services/omrs/omrs-topic-connector)** - manages the exchange  of **[OMRS Events](/concepts/cohort-events)** with the `OMRS Topic` by calling the **[Open Metadata Topic Connector](/concepts/open-metadata-topic-connector)**.

* **[Open Metadata Archive Store Connector](/concepts/open-metadata-archive-store-connector)** - supports the reading and writing of **[open metadata archives](/concepts/open-metadata-archive)** on behalf of the repository services' **[archive manager](/services/omrs/archive-manager)**.

* **[Open Metadata Topic Connector](/concepts/open-metadata-topic-connector)** - manages the calls to the **[event bus](/concepts/event-bus)** to support specific topic connectors such as the OMRS Topic Connector described above.

* **[Repository Connector](/concepts/repository-connector)** defines the open metadata common interface to a metadata repository.  This may be a repository with native support for the open metadata types and instances or one that is mapping to a third party metadata repository API. In the case of it supporting an third party metadata repository, it is often paired with an event mapper connector described above.

The OMRS defines the interfaces for these connectors and selected implementations
are located in the **[adapters](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/repository-services-connectors)** module.

All of these connectors support the [Open Connector Framework (OCF)](/frameworks/ocf/overview) which means the OMRS uses the OCF [Connector Broker](/concepts/connector-broker) to create the instances of the connectors it needs. The type of connector needed is defined in a connection object.

The connection objects for OMRS's connectors are defined in the OMAG Server configuration document that is passed to the server when the open metadata services are activated.

This means that new implementations can be specified without needing to change the OMRS code.

--8<-- "snippets/abbr.md"

