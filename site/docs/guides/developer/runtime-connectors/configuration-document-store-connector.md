<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Writing Configuration Document Store Connectors

    
The [admin-services-api :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/admin-services/admin-services-api){ target=gh } module provides the interface definition for a [configuration document store connector](/concepts/configuration-document-store-connector) in the `org.odpi.openmetadata.adminservices.store` Java package. Its interface is simple - consisting of save, retrieve and remove operations, along with a method to set the name of the server and a method to retrieve every configuration document in the store:

```java
/**
 * OMAGServerConfigStore provides the interface to the configuration for an OMAG Server.  This is accessed
 * through a connector.
 */
public interface OMAGServerConfigStore
{
    /**
     * Set up the name of the server for this configuration document.
     *
     * @param serverName name of the server
     */
    void setServerName(String  serverName);


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

    /**
     * Retrieve all the stored server configurations
     *
     * @return the set of server configurations present in this OMAG Server Config store
     */
    Set<OMAGServerConfig> retrieveAllServerConfigs();
}
```

The configuration document is represented by the `OMAGServerConfig` structure. The name of the server is stored in the `localServerName` property in `OMAGServerConfig`.

The same package provides two base classes:

* `OMAGServerConfigStoreConnectorBase` - extends `ConnectorBase` and implements `setServerName`, saving the server name in the protected `serverName` variable.  It also provides the protected `getStoreName(template, params...)` method that uses `java.text.MessageFormat` to insert values, such as the server name, into a template for the name of the store.  For example, the template `data/servers/{0}/config/{0}.config` becomes `data/servers/cocoMDS1/config/cocoMDS1.config` for a server called `cocoMDS1`.
* `OMAGServerConfigStoreProviderBase` - extends `OpenConnectorProviderBase` and is the base class for the connector provider.

### Sample implementation

The implementation of this connector provided by Egeria is found in the [configuration-store-connectors :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/configuration-store-connectors){ target=gh } module:

- [configuration-file-store-connector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/configuration-store-connectors/configuration-file-store-connector){ target=gh } supports managing the open metadata configuration as a clear text JSON file.  Its connector provider is `FileBasedServerConfigStoreProvider` and its connector is `FileBasedServerConfigStoreConnector`.  The file name template is taken from the network address of the endpoint in its connection.  If no endpoint is supplied, the template `./data/servers/{0}/config/{0}.config` is used.  Its implementation of `retrieveAllServerConfigs` scans the file system for files that match the template.

### Configuring the connector

The configuration document store connector is a platform connector.  It is typically configured in the OMAG Server Platform's `application.properties` file using the `platform.configstore.provider` property (the class name of the connector provider) and the `platform.configstore.endpoint` property (the template for the name of the store).  It can also be set dynamically with a `POST` request to `/open-metadata/admin-services/stores/connection`, passing the connection for the connector in the request body.

!!! education "Further information"
    - [Open Connector Framework (OCF)](/frameworks/ocf/overview) defines open connectors and connections since many of the sections in the configuration document take connection objects for connectors.
    - [Configuring the configuration document store connector](/guides/admin/configuring-the-omag-server-platform/#configuration-document-store) for the properties that install a particular configuration document store connector into the OMAG Server Platform.

--8<-- "snippets/abbr.md"
