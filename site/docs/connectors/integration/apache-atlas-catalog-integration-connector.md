<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

--8<-- "snippets/content-status/tech-preview.md"

# Apache Atlas Integration Connector

!!! info "Connector details"
    - Connector Category: [Integration Connector](/concepts/integration-connector)
    - Hosting Service: [Catalog Integrator OMIS](/services/omis/catalog-integrator/overview)
    - Hosting Server: [Integration Daemon](/concepts/integration-daemon)
    - Source Module: [atlas-integration-connector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/integration-connectors/atlas-integration-connector){ target=gh }
    - Jar File Name: `atlas-integration-connector.jar`

## Overview

The Apache Atlas integration connector publishes ACTIVE glossary terms to Apache Atlas.  It can be configured to publish just from a single glossary or all glossaries.  The connector makes no attempt to detect changes to these glossary terms in Apache Atlas.  However, such changes will be overridden the next time the integration connector refreshes the glossary metadata in Apache Atlas.

![Figure 1](apache-atlas-catalog-integration-connectors.svg)
> **Figure 1:** Operation of the Apache Atlas integration connector


## Configuration

This connector uses the [Catalog Integrator OMIS](/services/omis/catalog-integrator/overview) running in the [Integration Daemon](/concepts/integration-daemon).

This is its connection definition to use on the [administration commands that configure the Catalog Integrator OMIS](/guides/admin/configuring-an-integration-daemon/#configure-the-integration-services) if you want all glossaries published to Apache Atlas.

!!! example "Connection configuration for all glossaries"
    ```json linenums="1" hl_lines="14"
    {
        "connection" : 
        { 
            "class" : "Connection",
            "qualifiedName" : "Egeria:IntegrationConnector:Catalog:Apache Atlas Connection",
            "connectorType" : 
            {
                "class" : "ConnectorType",
                "connectorProviderClassName" : "org.odpi.openmetadata.adapters.connectors.integration.apacheatlas.ApacheAtlasIntegrationProvider"
            },
            "endpoint" :
            {
                "class" : "Endpoint",
                "address" : "{{atlasServerURL}}"
            }
        }
    }
    ```

    - Replace `{{atlasServerURL}}` with the URL of the Apache Atlas server.


!!! example "Connection configuration for a selected glossary"
    ```json linenums="1" hl_lines="14 17"
    {
        "connection" :
        {
            "class" : "Connection",
            "qualifiedName" : "Egeria:IntegrationConnector:Catalog:Apache Atlas Connection",
            "connectorType" :
            {
                "class" : "ConnectorType", 
                "connectorProviderClassName" : "org.odpi.openmetadata.adapters.connectors.integration.apacheatlas.ApacheAtlasIntegrationProvider"
            },
            "endpoint" :
            {
                "class" : "Endpoint",
                "address" : "{{atlasServerURL}}"
            },
            "configurationProperties" :
            {
                "glossaryQualifiedName" : "{{glossaryQualifiedName}}"
            }
        }
    }
    ```

    - Replace `{{atlasServerURL}}` with the URL of the Apache Atlas server.
    - Replace `{{glossaryQualifiedName}}` with the qualified name of the Egeria glossary to publish to Apache Atlas.

---8<-- "snippets/abbr.md"
