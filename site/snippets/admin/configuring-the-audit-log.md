<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

## Configure the audit log

Egeria's [audit log](/concepts/audit-log) provides a configurable set of destinations for audit records and other diagnostic logging for an [OMAG Server](/concepts/omag-server). Some destinations also support a query interface to allow an administrator to understand how the server is running.

Each audit log record has a severity that can be used to route it to one or more specific destinations.  Therefore, when an audit log destination is configured, it is optionally supplied with a list of severities to filter the types of audit log records it should receive.

The audit log severities are as follows:

| Severity | Description |
|---|---|
| `Information` | The server is providing information about its normal operation. |
| `Event` | An event was received from another member of the open metadata repository cohort. |
| `Decision` | A decision has been made related to the interaction of the local metadata repository and the rest of the cohort. |
| `Action` | An Action is required by the administrator. At a minimum, the situation needs to be investigated and if necessary, corrective action taken. |
| `Error` | An error occurred, possibly caused by an incompatibility between the local metadata repository and one of the remote repositories. The local repository may restrict some of the metadata interchange functions as a result. |
| `Exception` | An unexpected exception occurred. This means that the server needs some administration attention to correct configuration or fix a logic error because it is not operating as a proper peer in the open metadata repository cohort. |
| `Security` | Unauthorized access to a service or metadata instance has been attempted. |
| `Startup` | A new component is starting up. |
| `Shutdown` | An existing component is shutting down. |
| `Asset` | An auditable action relating to an asset has been taken. |
| `Types` | Activity is occurring that relates to the open metadata types in use by this server. |
| `Cohort` | The server is exchanging registration information about an open metadata repository cohort that it is connecting to. |
| `Trace` | This is additional information on the operation of the server that may be of assistance in debugging a problem. It is not normally logged to any destination, but can be added when needed. |
| `PerfMon` | This log record contains performance monitoring timing information for specific types of processing. It is not normally logged to any destination, but can be added when needed. |
| `<Unknown>` | Uninitialized Severity |



The default audit log destination is the console audit log destination.  This writes selected parts of each audit log record to "standard out" (stdout). 


It is configured to receive log records of all severities except `Activity`, `Event`, `Trace` and `PerfMon`.  It is added automatically to a server's configuration document when other sections are configured.  



### Add audit log destinations

If the server is a development or test server, then the default audit log configuration is probably sufficient, and you should use the following command:

!!! post "POST - set default audit log destination"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/audit-log-destinations/default
    ```

*Note:* Using this command overrides all previous audit log destinations configured for the server.

If this server is a production server then you will probably want to set up the audit log destinations explicitly. You can add multiple destinations and each one can be set up to receive different severities of audit log records. 

There are various destinations that can be configured for the audit log:

=== "console"

    Since the default audit log destination is also a console audit log destination, only use this option to add the `Trace` and `PerfMon` severities.

    !!! post "POST - add console audit log destination"

        ```
        {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/audit-log-destinations/console
        ```
        !!! tip "The body of the request should be a list of severities"
            If an empty list is passed as the request body then all severities are supported by the destination.

=== "file"
    This destination writes JSON files in a shared directory.  One file for each audit log record.

    !!! post "POST - add JSON file-based audit log destination"
        ```
        {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/audit-log-destinations/files
        ```
        !!! tip "The body of the request should be a list of severities"
            If an empty list is passed as the request body then all severities are supported by the destination.

=== "event"
    This destination writes each log record as an event on the supplied event topic. It assumes that the [event bus](#set-up-the-default-event-bus) is set up first.

    !!! post "POST - add event-based audit log destination"
        ```
        {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/audit-log-destinations/event-topic
        ```
        !!! tip "The body of the request should be a list of severities"
            If an empty list is passed as the request body then all severities are supported by the destination.

=== "slf4j"
    This writes full log records to the slf4j ecosystem.   When configuring slf4j as destination you also need to specify audit log logger category via the application properties of the [OMAG Server Platform](/concepts/omag-server-platform). This is described in [Connecting the OMAG Audit Log Framework](/guides/admin/omag-server-platform-logging/#connecting-the-omag-audit-log-framework) section of the developer logging guide.

    The configuration of the slf4j ecosystem determines it ultimate destination(s).

    !!! post "POST - add slf4j audit log destination"
        ```
        {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/audit-log-destinations/slf4j
        ```
        !!! tip "The body of the request should be a list of severities"
            If an empty list is passed as the request body then all severities are supported by the destination.

=== "connection"
    This sets up an audit log destination that is described though a [connection](/concepts/connection). In this case, the connection is passed in the request body and the supported severities are supplied in the connection's configuration properties.

    !!! post "POST - add connection-based audit log destination"
        ```
        {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/audit-log-destinations/connection
        ```

=== "list"
    It is also possible to set up all the audit log destinations in one command as a list of connections. Using this option overrides all previous audit log destinations and so can be used as the update command.  The list of connections is passed in the request body and the supported severities are supplied in each connection's configuration properties.

    !!! post "POST - add a list of connection-based audit log destinations"
        ```
        {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/audit-log-destinations
        ```

### Retrieving audit log destinations

The configured list of audit log destinations can be retrieved using this command:

!!! get "GET - the list of configured audit log destinations"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/audit-log-destinations
    ```

### Updating audit log destinations

Audit log destinations can be updated individually, by qualified name using the following command:

!!! post "POST - update connection-based audit log destination"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/audit-log-destinations/connection/{{qualifiedName}}
    ```

If you are not sure what the audit log connection is called, [retrieve the list of configured audit log connections](#retrieving-audit-log-destinations) and the resulting list of audit log connections will include the qualified names.

### Remove audit log destinations

The following will remove all audit log destinations, enabling you to add a new set of audit log destinations.

!!! delete "DELETE - clear all audit log destinations"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/audit-log-destinations
    ```

It is also possible to remove a single audit log destination using its connection's qualified name.

!!! delete "DELETE - clear then named audit log destination"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/audit-log-destinations/{{qualifiedName}}
    ```