<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Operations Guide

The operations guide describes the commands and actions that can be performed on a running [OMAG Server Platform](/egeria-docs/concepts/omag-server-platform) to discover its status, and the status of the servers and connectors that it is hosting.

## Platform Origin Service

The platform origin service is a simple REST API that returns basic information about an OMAG Server Platform. It is often used by operational scripts controlling the start up and shutdown of OMAG Server Platforms to determine if the server platform is running.

There is a single operation on this service called `server-platform-origin`.

The format of the operation is:

!!! get "GET - retrieve platform origin"
    ```
    {{platformURLRoot}}/open-metadata/platform-services/users/{{userId}}/server-platform-origin
    ```

where `{{platformURLRoot}}` is typically the host name and port number for the server platform's
network endpoint and `{{userId}}` is the userId of an authorized administrator.

The response is a single string describing the implementation and version of the server platform.

For example, this is the response from the ODPi Egeria implementation of the OMAG Server Platform
which has an endpoint of `https://localhost:9443`.  Gary Geeke (`garygeeke`) is the administrator.

```bash
$ curl --insecure -X GET https://localhost:9443/open-metadata/platform-services/users/garygeeke/server-platform-origin
Egeria OMAG Server Platform (version 3.4-SNAPSHOT)
```

## Listing Registered Services

An OMAG Server Platform has fixed services as well as optional registered services. It is possible to list the registered services that are loaded in an OMAG Server Platform.

!!! get "GET - list Open Metadata Access Services (OMASs)"
    ```
    {{platformURLRoot}}/open-metadata/platform-services/users/{{userId}}/server-platform/registered-services/access-services
    ```
    
!!! get "GET - list Open Metadata Engine Services (OMESs)"
    ```
    {{platformURLRoot}}/open-metadata/platform-services/users/{{userId}}/server-platform/registered-services/engine-services
    ```    

!!! get "GET - list Open Metadata Integration Services (OMISs)"
    ```
    {{platformURLRoot}}/open-metadata/platform-services/users/{{userId}}/server-platform/registered-services/integration-services
    ```    
!!! get "GET - list Open Metadata View Services (OMVSs)"
    ```
    {{platformURLRoot}}/open-metadata/platform-services/users/{{userId}}/server-platform/registered-services/view-services
    ```    

## Operating an OMAG Server

Once an [OMAG Server](/egeria-docs/concepts/omag-server) is [configured](/egeria-docs/guides/admin/servers) it can be started and stopped multiple times.

* [Starting and stopping an OMAG Server](#starting-and-stopping-an-omag-server)

It is possible to load an [Open Metadata Archive](/egeria-docs/concepts/open-metadata-archives) into running OMAG Servers that are of type [Metadata Access Store](/egeria-docs/concepts/metadata-access-store).

* [Adding an Open Metadata Archive to a running Metadata Access Store](#adding-an-archive-to-a-running-metadata-access-store)

In addition there are different platform services that
can be used to find out more about the operation of the servers.

* [Querying the servers and services running in an OMAG Server Platform](#querying-an-omag-server-and-services)

Egeria also has an interactive graph-based user interface (UI) that enables you to explore the open metadata ecosystem.  This includes the OMAG Server Platforms and Servers, the types of metadata supported by each metadata repository and the contents of the metadata repositories. It is also possible to maintain the configuration of the OMAG Servers through this UI.

* [Using the ecosystem user interface](https://github.com/odpi/egeria-react-ui)

### Starting and Stopping an OMAG server

Once a [configuration document](/egeria-docs/concepts/configuration-document) has been completed
for an [OMAG Server](/egeria-docs/concepts/omag-server), it can be started using the following
REST call:

```
POST {platformURLRoot}/open-metadata/admin-services/users/{adminUserId}/servers/{serverName}/instance
```

and stopped, as follows:

```
DELETE {platformURLRoot}/open-metadata/admin-services/users/{adminUserId}/servers/{serverName}/instance
```

The configuration document is not changed by these calls. It is possible to query the running server's configuration using the following REST API:

```
GET {platformURLRoot}/open-metadata/admin-services/users/{adminUserId}/servers/{serverName}/instance/configuration
```

If you want to delete the server's configuration document then issue:

```
DELETE {platformURLRoot}/open-metadata/admin-services/users/{adminUserId}/servers/{serverName}
```

If the OMAG server is running, this command also unregisters the named server from the cohorts it
is connected to.  Only use this command if the server is being permanently removed.

### Adding an archive to a running Metadata Access Store

[Open Metadata Archives](/egeria-docs/concepts/open-metadata-archives) contain pre-canned metadata types and instances for [Cohort Members](/egeria-docs/concepts/cohort-member).

Archives can be [added to the configuration document](/egeria-docs/guides/operations/configuring-the-startup-archives) of a server to ensure their content is loaded each time the server is started.  This is intended for:

- Archives containing type definitions.
- Archives containing instances for repositories that do not store the archive content but keep it in memory.
Although, if an archive is loaded multiple times, its content is only added to the local repository
if the repository does not have the content already.

Archives can also be loaded to a running server using the following commands.

Typically, an open metadata archive is stored as JSON format in a file. To load such a file use the following command:

!!! post "POST - load file"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/instance/open-metadata-archives/file
    ```

    The body of the request should be the fully-qualified path name or path relative to the startup directory of the OMAG Server Platform -- and the file name should not have any quotes around it.

Alternatively it is possible to set up the list of open metadata archives as a list of [connections](/egeria-docs/concepts/connection). These connections refer to [open metadata archive connectors](/egeria-docs/connectors/open-metadata-archive-store-connector) that can read and retrieve the open metadata archive content.

!!! post "POST - load from connection(s)"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/instance/open-metadata-archives/connection
    ```

    The body of the request should be the list of connections from which to load archives.

This option can be used when the open metadata archives are not stored in a file, or a different file format from the default one for the OMAG Server Platform is required.

### Querying an OMAG Server and its services

!!! get "GET - is an OMAG Server known to the platform?"
    ```
    {{platformURLRoot}}/open-metadata/platform-services/users/{{userId}}/server-platform/servers/{{serverName}}/is-known
    ```    

!!! get "GET - retrieve list of servers known to the platform"
    ```
    {{platformURLRoot}}/open-metadata/platform-services/users/{{userId}}/server-platform/servers
    ```    

!!! get "GET - retrieve list of servers currently active on the platform"
    ```
    {{platformURLRoot}}/open-metadata/platform-services/users/{{userId}}/server-platform/servers
    ```    

!!! get "GET - retrieve server status"
    ```
    {{platformURLRoot}}/open-metadata/platform-services/users/{{userId}}/server-platform/servers/{{serverName}}/status
    ```    

!!! get "GET - retrieve the services available for an active server"
    ```
    {{platformURLRoot}}/open-metadata/platform-services/users/{{userId}}/server-platform/servers/{{serverName}}/services
    ```    

### Querying the audit log

!!! get "GET - retrieve the audit log severity definitions for an active server"
    ```
    {{platformURLRoot}}/servers/{{serverName}}/open-metadata/repository-services/users/{{userId}}/audit-log/severity-definitions
    ```    

!!! get "GET - retrieve the audit log's report"
    ```
    {{platformURLRoot}}/servers/{{serverName}}/open-metadata/repository-services/users/{{userId}}/audit-log/report
    ```    

### Querying the metadata highway

Return the details of the cohorts that this server is participating in.

!!! get "GET - retrieve the server's cohorts"
    ```
    {{platformURLRoot}}/servers/{{serverName}}/open-metadata/repository-services/users/{{userId}}/metadata-highway/cohort-descriptions
    ```  
    
Return the local registration information used by this server to register with open metadata repository cohorts.  No registration time is provided.  Use the cohort specific version to retrieve the registration time.

!!! get "GET - retrieve the server's generic local cohort registration information"
    ```
    {{platformURLRoot}}/servers/{{serverName}}/open-metadata/repository-services/users/{{userId}}/metadata-highway/local-registration
    ```  

Return the local registration information used by this server to register with the requested open metadata repository cohort.

!!! get "GET - retrieve the server's registration with a specific cohort"
    ```
    {{platformURLRoot}}/servers/{{serverName}}/open-metadata/repository-services/users/{{userId}}/metadata-highway/cohorts/{{cohortName}}/local-registration
    ```  

Return the list of registrations received from remote members of the cohort.

!!! get "GET - retrieve the server's remove partners in a specific cohort"
    ```
    {{platformURLRoot}}/servers/{{serverName}}/open-metadata/repository-services/users/{{userId}}/metadata-highway/cohorts/{{cohortName}}/remote-members
    ```  
    
--8<-- "snippets/abbr.md"