<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Writing Configuration Document Store Connectors

---8<-- "docs/connectors/runtime/configuration-document-store-connector-intro.md"

## Configuration document store connector interface
    
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


!!! education "Further information"
    - [Open Connector Framework (OCF)](/frameworks/ocf/overview) defines open connectors and connections since many of the sections in the configuration document take connection objects for connectors.
    - [Configuring the configuration document store connector](/guides/admin/configuring-the-omag-server-platform/#configuration-store) for the command to install a particular configuration document store connector into the OMAG Server Platform.

--8<-- "snippets/abbr.md"
