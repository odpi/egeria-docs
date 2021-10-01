<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Configuration Documents

A configuration document provides the configuration details for a single [OMAG Server](omag-server.md). It defines which subsystems are activated in the server and which connector implementations it should use.

## Configuration document structure

An OMAG Server's configuration document is structured into elements that each describe the configuration properties for each of its desired capabilities.

![Structure of the configuration document](configuration-document-structure.png)

The sections are as follows:

- [Default values](#default-values) to use when creating other configuration elements. These values need to be set up first.
- [Basic properties](#basic-properties) of any OMAG Server.
- [Specific subsystem configurations](#specific-subsystem-configurations) that provide the key capabilities for different types of OMAG Servers.
- [Audit trail](#audit-trail) that documents the changes that have been made to the configuration document.

It is possible to retrieve the configuration document for a server using the following command:

!!! get "GET - retrieve configuration document for a server"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/configuration
    ```

When the server is running, the following command returns the configuration document that was used to start it (since it may have changed in the configuration document store since the server was started):

!!! get "GET - retrieve configuration document used to start a server"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/instance/configuration
    ```

### Default values

At the top of the configuration document are:

- [Local server URL root](omag-server.md#platform-url-root), which defines the root of the network address for the [OMAG Server Platform](omag-server-platform.md) where the OMAG Server will run.
- [Event bus config](/egeria-docs/guides/admin/servers/configuring-a-metadata-access-point/#set-up-the-default-event-bus), which provides the configuration of the event bus (Apache Kafka or similar) where all the event topics that the server will use are located.

Both of these elements provide default values for other configuration elements.

If they are changed, their new values do not affect existing definitions in the configuration document.

### Basic properties

The basic properties of the OMAG Server are used in logging, events handing and security. They help to document the purpose of the server (which helps with problem determination) and enable performance improvements by allowing the server to ignore activity or metadata that is not relevant to its operation.

Find more information on configuring each through the sub-sections of the [configuring an OMAG Server](/egeria-docs/guides/admin/servers) portion of the administration guide.

### Specific subsystem configurations

Different types of servers can be configured with other specific subsystems, such as a local metadata repository, registering with a cohort, configuring access services or others.

Since these vary depending on the type of OMAG Server, find more details in the sub-sections under the [configuring an OMAG Server](/egeria-docs/guides/admin/servers) portion of the administration guide.

### Audit trail

The audit trail allows you to keep track of changes to the configuration document. This is helpful to audit what any recent changes might have been - particularly if a working server suddenly stops working - the first question is always, "what has changed recently?"

It also acts as a nice summary of how the server has been configured.

!!! example "Example of an audit trail"
    ```
    {
     "auditTrail" : [
        "Thu Jan 30 22:37:12 GMT 2020 garygeeke updated configuration for local server's URL root to https://localhost:9444.",
        "Thu Jan 30 22:37:12 GMT 2020 garygeeke updated configuration for maximum page size to 100.",
        "Thu Jan 30 22:37:12 GMT 2020 garygeeke updated configuration for local server type name to Open Metadata Server.",
        "Thu Jan 30 22:37:12 GMT 2020 garygeeke updated configuration for local server's owning organization's name to Coco Pharmaceuticals.",
        "Thu Jan 30 22:37:12 GMT 2020 garygeeke updated configuration for local server's userId to cocoMDS1npa.",
        "Thu Jan 30 22:37:12 GMT 2020 garygeeke updated configuration for local server's password to cocoMDS1passw0rd.",
        "Thu Jan 30 22:37:12 GMT 2020 garygeeke added configuration for an Open Metadata Server Security Connector",
        "Thu Jan 30 22:37:12 GMT 2020 garygeeke updated configuration for default event bus.",
        "Thu Jan 30 22:37:12 GMT 2020 garygeeke updated configuration for the local repository.",
        "Thu Jan 30 22:37:12 GMT 2020 garygeeke updated configuration for the local repository.",
        "Thu Jan 30 22:37:12 GMT 2020 garygeeke preserving local metadata collection id bfdfdc61-01bb-4564-9c29-6b81c0fb79f8.",
        "Thu Jan 30 22:37:12 GMT 2020 garygeeke updated configuration for cohort cocoCohort.",
        "Thu Jan 30 22:37:12 GMT 2020 garygeeke updated configuration for access services.",
        "Thu Jan 30 22:37:12 GMT 2020 garygeeke updated configuration for enterprise repository services (used by access services).",
        "Thu Jan 30 22:37:13 GMT 2020 garygeeke updated configuration for access services.",
        "Thu Jan 30 22:37:13 GMT 2020 garygeeke updated configuration for enterprise repository services (used by access services).",
        "Thu Jan 30 22:37:13 GMT 2020 garygeeke updated configuration for access services.",
        "Thu Jan 30 22:37:13 GMT 2020 garygeeke updated configuration for enterprise repository services (used by access services).",
        "Thu Jan 30 22:37:13 GMT 2020 garygeeke updated configuration for access services.",
        "Thu Jan 30 22:37:13 GMT 2020 garygeeke updated configuration for enterprise repository services (used by access services).",
        "Thu Jan 30 22:37:13 GMT 2020 garygeeke updated configuration for access services.",
        "Thu Jan 30 22:37:13 GMT 2020 garygeeke updated configuration for enterprise repository services (used by access services).",
        "Thu Jan 30 22:37:13 GMT 2020 garygeeke updated configuration for access services.",
        "Thu Jan 30 22:37:13 GMT 2020 garygeeke updated configuration for enterprise repository services (used by access services).",
        "Thu Jan 30 22:37:13 GMT 2020 garygeeke updated configuration for access services.",
        "Thu Jan 30 22:37:13 GMT 2020 garygeeke updated configuration for enterprise repository services (used by access services).",
        "Thu Jan 30 22:37:13 GMT 2020 garygeeke updated configuration for access services.",
        "Thu Jan 30 22:37:13 GMT 2020 garygeeke updated configuration for enterprise repository services (used by access services).",
        "Thu Jan 30 22:37:13 GMT 2020 garygeeke updated configuration for access services.",
        "Thu Jan 30 22:37:13 GMT 2020 garygeeke updated configuration for enterprise repository services (used by access services).",
        "Thu Jan 30 22:37:13 GMT 2020 garygeeke updated configuration for access services.",
        "Thu Jan 30 22:37:13 GMT 2020 garygeeke updated configuration for enterprise repository services (used by access services).",
        "Thu Jan 30 22:37:13 GMT 2020 garygeeke updated configuration for access services.",
        "Thu Jan 30 22:37:13 GMT 2020 garygeeke updated configuration for enterprise repository services (used by access services).",
        "Thu Jan 30 22:44:10 GMT 2020 garygeeke deployed configuration for server."
     ]
    }
    ```

## Storage

By default, the configuration document is stored as a JSON in a file in the default directory for the [OMAG Server Platform](omag-server-platform.md) that creates them.

These files may contain security certificates and passwords and so should be treated as sensitive. It is possible to change the storage location of configuration documents - or even the type of store.

The configuration document's persistence is managed by the *configuration document store connector*.

??? question "Configuration document store connector interface"
    The [admin-services-api :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/admin-services/admin-services-api){ target=gh } module provides the interface definition for this connector. Its interface is simple -- consisting of save, retrieve and delete operations:

    ```java
    /**
     * OMAGServerConfigStore provides the interface to the configuration for an OMAG Server.  This is accessed
     * through a connector.
     */
    public interface OMAGServerConfigStore
    {
        /**
         * Save the server configuration.
         * 
         * @param configuration configuration properties to save
         */
        void saveServerConfig(OMAGServerConfig   configuration);
    
    
        /**
         * Retrieve the configuration saved from a previous run of the server.
         *
         * @return server configuration
         */
        OMAGServerConfig  retrieveServerConfig();
    
    
        /**
         * Remove the server configuration.
         */
        void removeServerConfig();
    }
    ```

The configuration document is represented by the `OMAGServerConfig` structure. The name of the server is stored in the `localServerName` property in `OMAGServerConfig`.

### Sample implementations

The implementations of this connector provided by Egeria are found in the [configuration-store-connectors :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/configuration-store-connectors){ target=gh } module. There are two connectors:

- [configuration-file-store-connector :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/configuration-store-connectors/configuration-file-store-connector){ target=gh } supports managing the open metadata configuration as a clear text JSON file.
- [configuration-encrypted-file-store-connector :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/configuration-store-connectors/configuration-encrypted-file-store-connector){ target=gh } supports managing the open metadata configuration as an encrypted JSON file.

It is also possible to [write your own implementation :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/configuration-store-connectors){ target=gh }.

### Configuring the connector

See [configuring the configuration document store](/egeria-docs/guides/admin/configuring-the-omag-server-platform/#configuration-store) for the command to install a particular configuration document store connector into the OMAG Server Platform.

!!! education "Further information"
    - [Open Connector Framework (OCF)](/egeria-docs/frameworks/ocf) defines open connectors and connections since many of the sections in the configuration document take connection objects for connectors.
    - [Configuring an OMAG Server](/egeria-docs/guides/admin/servers) provides more detail on the process of creating a configuration document for various types of OMAG Servers.

--8<-- "snippets/abbr.md"
