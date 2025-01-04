<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# Open Metadata Access Security Connector

!!! info "Connector details"
    - Connector Category: [Metadata Security Connector](/features/metadata-security/overview)
    - Source Module: [metadata-access-secrets-store-connector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/metadata-security-connectors/open-metadata-access-security-connector){ target=gh }
    - Jar File Name: `yaml-secrets-store-connector.jar`

## Overview

The *YAML File Secrets Store Connector* is a [Secrets Store Connector](/concepts/secrets-store-connector) that retrieves secrets from a named YAML file.  By convention, these YAML files have a file extension of `omsecrets`. 

![Figure 1](yaml-file-secrets-store-connector.svg)
> **Figure 1:** Operation of the YAML File Secrets Store Connector

Secrets within the YAML file are organized into collections. Each collection represents a set of secrets needed by a particular type of caller. When the YAML File Secrets Store Connector starts up, it opens the YAML file using the address passed in the endpoint of its connection.  It located the appropriate collection using the name specified in the `secretsCollectionName` property found in the connection's `configurationProperties`.  The connector will fail if either of these two values are missing.



Inside a collection are:

* A refresh time interval (`refreshTimeInterval`) that defines how long the secrets can be cached.  When the time expires, the connector retrieves the secrets from the cache.
* A map of named secrets (`secrets`) - such as details of certificates or userId and passwords.  These secrets are used by other connectors, and automated services to log on to remote services.
* The details of an API to call to retrieve a token (`tokenAPI`).  This includes the HTTP request type, URL and details fo the request and response body.  This supplements the secrets map allowing certain secrets to be retrieved dynamically.
* A map of userIds to user account details (`users`).  This is needed by a connector that is supporting a user authentication service.
* A map of named lists (`namedLists`) that is used to represent organizational units, security roles and groups needed by an authorization service.

Complete details of this structure can be found in [Egeria's Javadoc](https://odpi.github.io/egeria/org/odpi/openmetadata/adapters/connectors/secretsstore/yaml/secretsstore/package-summary.html) and an example can be found in [GitHub](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-deployment/secrets).

## Configuration

This is its connection definition to embed into a calling connector's connection object.

!!! example "Connection configuration for the environment variable secrets store connector"
    ```json linenums="1" hl_lines="14"
    {
        "connection" : 
        { 
            "class" : "Connection",
            "qualifiedName" : "Egeria:SecretsStoreConnector:YAML File Connection",
            "connectorType" : 
            {
                "class" : "ConnectorType",
                "connectorProviderClassName" : "org.odpi.openmetadata.adapters.connectors.secretsstore.yaml.YAMLSecretsStoreProvider"
            },
            "endpoint" :
            {
                "class" : "Endpoint",
                "address" : {{secretsStoreFileLocation}}
            },
            "configurationProperties" :
            {
                "secretsCollectionName" : {{secretsCollectionName}}
            }
        }
    }
    ```

---8<-- "snippets/abbr.md"
