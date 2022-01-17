<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Writing Archive Services

---8<-- "docs/connectors/archive/archive-service-intro.md"


## Interface

The interface that all archive services must implement is defined by [`ArchiveService` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/engine-services/archive-manager/archive-manager-api/src/main/java/org/odpi/openmetadata/engineservices/archivemanager/connectors/ArchiveService.java){ target=gh }:

![Figure 1](archive-service-methods.svg)
> **Figure 1:** Methods implemented by an archive service

- `initialize` is a standard method for all connectors that is called by the [connector broker](/egeria-docs/concepts/connector-broker) when the connector is created. The [connector](/egeria-docs/frameworks/ocf/#connector) is passed the [connection](/egeria-docs/frameworks/ocf/#connection) object from the configuration and a unique identifier for this instance of the connector.
- `setAuditLog` provides a logging destination (see [Audit Log Framework (ALF)](/egeria-docs/frameworks/alf/overview)).
- `setContext` sets up the archive context. This provides an interface to the repository services (OMRS) that provide access to the open metadata.
    - The ability to register a listener to receive events from the [Enterprise OMRS Topic](/egeria-docs/concepts/cohort-events/#enterprise-event-topic).
    - The ability to retrieve metadata instances from any connected open metadata repository.
- `start` indicates that the archive service is completely configured and can begin processing.  This call can be used to register a listener with the Enterprise OMRS Topic through the context and to update the archive store with the current state of the metadata in the repositories. 
- `disconnect` is called when the server is shutting down. The archive service should free up any resources that it holds since it is not needed any more.


??? education "Further information"
    - [Configuring an engine host](/egeria-docs/guides/admin/servers/configuring-an-engine-host) to understand how to set up an archive service.
    - [Overview of connectors)](/egeria-docs/frameworks/ocf/overview) that defines the behavior of all connectors.

--8<-- "snippets/abbr.md"
