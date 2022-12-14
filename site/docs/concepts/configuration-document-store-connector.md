<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Configuration Document Store Connector

---8<-- "docs/connectors/runtime/configuration-document-store-connector-intro.md"


The configuration document's persistence is managed by the [configuration document store connector](/concepts/configuration-document-store-connector).

By default, the configuration document is stored as an encrypted JSON in a file under the default directory for the [OMAG Server Platform](/concepts/omag-server-platform) that creates them.

Configuration documents may contain security certificates and passwords and so should be treated as sensitive. It is possible to [change the storage location](/guides/admin/configuring-the-omag-server-platform) of configuration documents - or even the type of store.


??? question "Configuration document store connector interface"
The [admin-services-api :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/admin-services/admin-services-api){ target=gh } module provides the interface definition for this connector. Its interface is simple -- consisting of save, retrieve and delete operations:

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

The implementations of this connector provided by Egeria are found in the [configuration-store-connectors :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/configuration-store-connectors){ target=gh } module. There are two connectors:

- [configuration-file-store-connector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/configuration-store-connectors/configuration-file-store-connector){ target=gh } supports managing the open metadata configuration as a clear text JSON file.
- [configuration-encrypted-file-store-connector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/configuration-store-connectors/configuration-encrypted-file-store-connector){ target=gh } supports managing the open metadata configuration as an encrypted JSON file.

It is also possible to [write your own implementation](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/configuration-store-connectors){ target=gh }.

### Configuring the connector

See [configuring the configuration document store](/guides/admin/configuring-the-omag-server-platform/#configuration-store) for the command to install a particular configuration document store connector into the OMAG Server Platform.

--8<-- "snippets/abbr.md"
