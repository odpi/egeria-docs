<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Governance Action Open Lineage Integration Connector

??? info "Connector details"
    - Connector Category: [Integration Connector](/egeria-docs/connectors/integration-connector)
    - Hosting Service: [Lineage Integrator OMIS](/egeria-docs/services/omis/lineage-integrator)
    - Hosting Server: [Integration Daemon](/egeria-docs/concepts/integration-daemon)
    - Source Module: [lineage-integration-connectors :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/integration-connectors/lineage-integration-connectors){ target=gh }
    - Jar File Name: `lineage-integration-connectors.jar`

## Overview

The Governance Action OpenLineage integration connector listens for governance actions executing in the open metadata ecosystem and generates open lineage events for them and publish them to any integration connector running in the same instance of Lineage Integrator OMIS.

![Figure 1](governance-action-open-lineage-integration-connector.svg)
> **Figure 1:** Operation of the File-based OpenLineage log store integration connector


## Configuration

This connector uses the [Lineage Integrator OMIS](/egeria-docs/services/omis/lineage-integrator/overview)
running in the [Integration Daemon](/egeria-docs/concepts/integration-daemon).

This is its connection definition to use on the [administration commands that configure the API Integrator OMIS](/egeria-docs/guides/admin/servers/configuring-an-integration-daemon/#configure-the-integration-services).

!!! example "Connection configuration"
    ```json linenums="1" hl_lines="14"
    {
       "connection" : 
                    { 
                        "class" : "Connection",
                        "qualifiedName" : "Egeria:IntegrationConnector:Lineage:GovernanceActionOpenLineage Connection",
                        "connectorType" : 
                        {
                            "class" : "ConnectorType",
                            "connectorProviderClassName" : "org.odpi.openmetadata.adapters.connectors.integration.lineage.GovernanceActionOpenLineageIntegrationProvider"
                        },
                    }
    }
    ```

---8<-- "snippets/abbr.md"