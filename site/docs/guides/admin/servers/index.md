<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Configuring an OMAG Server

An [OMAG Server](/concepts/omag-server) is a configured set of services and connectors that support the integration of a particular type of technology.  This configuration is located in a [configuration document](/concepts/configuration-document) that is stored in the [configuration document store](/concepts/configuration-document-store-connector).

There are [different types of OMAG Server](/concepts/omag-server#types-of-omag-server) each with a specific purpose. Each server is configured separately.  They then may call to one another once they are running.

The configuration document for the OMAG Server determines which OMAG subsystems (and hence the types of services) should be activated in the OMAG Server. For example:

- Basic descriptive properties of the server that are used in logging and events originating from the server.
- The type of local repository to use.
- Which services should be started.
- Which cohorts to connect to.

Many of the configuration values are [connections](/concepts/connection) to allow the server to create the connectors to the resources it needs.

These connectors enable Egeria to run in different deployment environments and to connect to different third party technologies.

![Connector types supported by the OMAG Servers](omag-server-connector-types.svg)


## Configuration commands

It is possible to supply a configuration document to the OMAG Server Platform that has been filled out by an external offline utility.  This is often used by vendors that have embedded Egeria in their product and want the configuration of it to be part of their standard configuration tools.  This option is also used by organizations that have developed their own server patterns and standards that are supported by their own utility.

Egeria's OMAG server Platform also provides configuration helper commands.  Each of the configuration helper commands builds up a section in the configuration document.  The appropriate section is stored immediately during each configuration helper command, so it is available for use by the next command.

There are two basic types of helper services: the course-grained helper services and the fine-grained helper services.

 * The course-grained helper commands allow you to configure each section of the configuration document separately. This is useful for editing the configuration document, or if you want a different set of options to those offered in the fine-grained configuration services. You would use these for example, if you did not want to have any audit logs configured - or in the case of one of the organizations that runs Egeria in production, they do not want the console audit log at all, only the SLF4J audit log.

 * The fine-grained helper commands are designed to offer simple configuration options that use a lot of defaults. They are aimed at developers, or people learning about Egeria. If the defaults are not what is needed, then the course-grained helper services are there. So the fine-grained services are not intended to be comprehensive - just to help people get up and running. There is a fine balance between coverage of potential options and too many helper services to choose from.

In order to show which type of command you are working with, they are colour-coded.

???+ beginner "Fine-grained helper command"

???+ intermediate "Course-grained helper command"

???+ expert "Working with the whole configuration document"

In the descriptions of the configuration helper commands, there are placeholders for the specific configuration values: they are names of the value in double curly braces. For example:

- `{{platformURLRoot}}` - the network address where the OMAG Server Platform is registered, such as `https://localhost:9443`.
- `{{adminUserId}}` - the user id of the administrator, for example `garygeeke`.
- `{{serverName}}` - the name of the OMAG Server, for example `cocoMDS1`.

## Retrieving the configuration

!!! get "GET - retrieve the configuration document for a specific OMAG Server"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/configuration
    ```

!!! get "GET - retrieve the origin of the server"
    It is also possible to query the origin of the server supporting the open metadata services.
    For the Egeria OMAG Server Platform, the response is `Egeria OMAG Server Platform (version {{releaseName}})`.

    ```
    {{platformURLRoot}}/open-metadata/platform-services/users/{{adminUserId}}/servers/{{serverName}}/server-platform-origin
    ```

## Migrating configuration documents

As Egeria evolves, the content of the configuration document expands. Many of the changes are pure additions and are therefore backward compatible.

!!! attention "OMAG Server Platform fails to load configuration document"
    From time to time the structure of the configuration document needs to change. When this happens, the OMAG Server Platform is not able to load the configuration document and a message similar to this is returned:

    ```json
    {
        "class": "VoidResponse",
        "relatedHTTPCode": 400,
        "exceptionClassName": "org.odpi.openmetadata.adminservices.ffdc.exception.OMAGInvalidParameterException",
        "exceptionErrorMessage": "OMAG-ADMIN-400-022 The configuration document for OMAG Server cocoMDS1 is at version V1.0 which is not compatible with this OMAG Server Platform which supports versions [V2.0]",
        "exceptionSystemAction": "The system is unable to configure the local server because it can not read the configuration document.",
        "exceptionUserAction": "Migrate the configuration document to a compatible version (or delete and recreate it).  See https://egeria.odpi.org/open-metadata-implementation/admin-services/docs/user/migrating-configuration-documents.html"
    }
    ```

### Migrating a configuration document from V1.0 to V2.0

The `additionalProperties` property name changed to `configurationProperties`. To migrate the configuration document, make a global change from `additionalProperties` to `configurationProperties` throughout the configuration document.

### Release 2.x+ of Egeria

Release 2.0 encrypts the configuration document by default. This includes automatically detecting and encrypting any clear-text (unencrypted) configuration document that may already exist. No user action is required for this migration, the encryption will be handled automatically when the clear-text configuration document is first opened by the platform in these releases.

--8<-- "snippets/abbr.md"
