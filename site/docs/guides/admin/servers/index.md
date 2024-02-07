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
