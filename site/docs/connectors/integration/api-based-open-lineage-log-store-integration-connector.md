<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

--8<-- "snippets/content-status/tech-preview.md"

# API-based Open Lineage Log Store Integration Connector

!!! info "Connector details"
    - Connector Category: [Integration Connector](/connectors/integration-connector)
    - Hosting Service: [Lineage Integrator OMIS](/services/omis/lineage-integrator)
    - Hosting Server: [Integration Daemon](/concepts/integration-daemon)
    - Source Module: [lineage-integration-connectors :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/integration-connectors/lineage-integration-connectors){ target=gh }
    - Jar File Name: `lineage-integration-connectors.jar`

## Overview

The API-based OpenLineage Log Store integration connector calls an OpenLineage compliant API to store open lineage events that have been published to the Lineage Integrator OMIS instance where this connector is running.

![Figure 1](api-based-open-lineage-log-store-integration-connector.svg)
> **Figure 1:** Operation of the API-based OpenLineage log store integration connector


## Configuration

This connector uses the [Lineage Integrator OMIS](/services/omis/lineage-integrator/overview)
running in the [Integration Daemon](/concepts/integration-daemon).

This is its connection definition to use on the [administration commands that configure the Lineage Integrator OMIS](/guides/admin/configuring-an-integration-daemon/#configure-the-integration-services).

!!! example "Connection configuration"
    ```json linenums="1" hl_lines="14"
    {
       "connection" : 
                    { 
                        "class" : "Connection",
                        "qualifiedName" : "Egeria:IntegrationConnector:Lineage:APIBasedOpenLineageLogStore Connection",
                        "connectorType" : 
                        {
                            "class" : "ConnectorType",
                            "connectorProviderClassName" : "org.odpi.openmetadata.adapters.connectors.integration.openlineage.APIBasedOpenLineageLogStoreProvider"
                        },
                        "endpoint" :
                        {
                            "class" : "Endpoint",
                            "address" : "{{logStoreURL}}"
                        }
                    }
    }
    ```

    - Replace `{{logStoreURL}}` with the URL of the destination API.

---8<-- "snippets/abbr.md"