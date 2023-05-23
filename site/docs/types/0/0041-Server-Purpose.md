<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0041 Server Purposes

The server purpose classifications allow more detail about the type of middleware software that are embedded in an [*ITInfrastructure*](/types/0/0030-Hosts-and-Platforms) entity.  Typically, these classifications are used with [*SoftwareServerPlatform*](/types/0/0037-Software-Server-Platforms) and [*SoftwareServer*](/types/0/0040-Software-Servers) entities.

![UML](0041-Server-Purpose.svg)

## ServerPurpose

The *deployedImplementationType* attribute in [SoftwareServerPlatform](/types/0/0037-Software-Server-Platforms) and [Software Server](/types/0/0040-Software-Servers) identifies the software is running in the platform - it could be a name from a product or open source project.  For example, if the open metadata types were describing an Egeria deployment, the [OMAG Server Platform](/concepts/omag-server-platform) would be represented as a *SoftwareServerPlatform* entity

The *ServerPurpose* classification provides a common base type for the server purposes - so it is possible to, for example, query a list of database servers, even through they are implemented using various technologies.

The subtypes of the *ServerPurpose* classification are:

- *ApplicationServer* - hosting application logic.
- *Webserver* - hosting endpoint for HTTP requests.
- *DatabaseServer* - hosting a database management system (DBMS).
- *IntegrationServer* - hosting data movement processes.
- *MetadataServer* - manages and stores a collection of metadata.
- *RepositoryProxy* - Acts as an adapter for a metadata server, translating requests between different APIs, formats and protocols.
- *StewardshipServer* - hosting stewardship processes.
- *GovernanceDaemon* -  hosting automated governance processing.



--8<-- "snippets/abbr.md"
