<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0041 Server Purposes

The server purpose classifications allow more detail about the type of middleware software that are embedded in an instance of [`ITInfrastructure`](/egeria-docs/types/0/0030-Hosts-and-Platforms).  Typically these classifications are used with [`SoftwareServerPlatform`s](/egeria-docs/types/0/0037-Software-Server-Platforms) and [`SoftwareServer`s](/egeria-docs/types/0/0040-Software-Servers).

## ServerPurpose

`ServerPurpose` provides a common base type for the server purposes.  The `deployedImplementationType` identifies the software that supports this purpose - it could be a product or open source project name.

The subtypes of the `ServerPurpose` classification are:

- `ApplicationServer` - hosting application logic.
- `Webserver` - hosting endpoint for HTTP requests.
- `DatabaseServer` - hosting a database management system (DBMS).
- `IntegrationServer` - hosting data movement processes.
- `MetadataServer` - manages and stores a collection of metadata.
- `RepositoryProxy` - Acts as an adapter for a metadata server, translating requests between different APIs, formats and protocols.
- `StewardshipServer` - hosting stewardship processes.
- `GovernanceDaemon` -  hosting automated governance processing.

![UML](0041-Server-Purpose.svg)


--8<-- "snippets/abbr.md"
