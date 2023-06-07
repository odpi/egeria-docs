<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

## Validating your integration

Once the integration daemon is configured it can be started.  It will read the configuration and start up the integration connectors described within.

Once it is running, the following command can be used to show the status of the integration connectors

```
GET {{serverURLRoot}}/servers/{{serverName}}/open-metadata/integration-daemon/users/{{userId}}/status
```
Here is an example of the result ... the integration connectors are organized by the integration services that are providing access to the open metadata APIs. In this case, there are three file-oriented integration connectors running with the [Files Integration OMIS](/services/omis/files-integrator/overview).

```json
{
    "class": "IntegrationDaemonStatusResponse",
    "relatedHTTPCode": 200,
    "integrationServiceSummaries": [
        {
            "integrationServiceId": 605,
            "integrationServiceFullName": "Files Integrator OMIS",
            "integrationServiceURLMarker": "files-integrator",
            "integrationServiceDescription": "Extract metadata about files stored in a file system or file manager.",
            "integrationServiceWiki": "https://egeria-project.org/services/omis/files-integrator/overview/",
            "integrationConnectorReports": [
                {
                    "connectorId": "7f4d641d-71cc-4df6-b7b9-aed29e3bdf7f",
                    "connectorName": "OakDeneLandingAreaFilesMonitor",
                    "connection": {
                        "class": "Connection",
                        "headerVersion": 0,
                        "connectorType": {
                            "class": "ConnectorType",
                            "headerVersion": 0,
                            "connectorProviderClassName": "org.odpi.openmetadata.adapters.connectors.integration.basicfiles.DataFilesMonitorIntegrationProvider"
                        },
                        "endpoint": {
                            "class": "Endpoint",
                            "headerVersion": 0,
                            "address": "data/landing-area/hospitals/oak-dene/clinical-trials/drop-foot"
                        }
                    },
                    "connectorInstanceId": "6471c86d-0f2f-4cd1-ad90-d0f396a1d31e",
                    "connectorStatus": "RUNNING",
                    "lastStatusChange": "2022-11-06T21:48:30.032+00:00",
                    "lastRefreshTime": "2022-11-06T21:48:38.893+00:00",
                    "minMinutesBetweenRefresh": 10
                },
                {
                    "connectorId": "0b64de6f-6cb6-46ac-844a-012bd0b96a9d",
                    "connectorName": "OldMarketLandingAreaFilesMonitor",
                    "connection": {
                        "class": "Connection",
                        "headerVersion": 0,
                        "connectorType": {
                            "class": "ConnectorType",
                            "headerVersion": 0,
                            "connectorProviderClassName": "org.odpi.openmetadata.adapters.connectors.integration.basicfiles.DataFilesMonitorIntegrationProvider"
                        },
                        "endpoint": {
                            "class": "Endpoint",
                            "headerVersion": 0,
                            "address": "data/landing-area/hospitals/old-market/clinical-trials/drop-foot"
                        }
                    },
                    "connectorInstanceId": "4ab6cbec-69fd-4c8f-bea4-c92b861bfe0b",
                    "connectorStatus": "FAILED",
                    "lastStatusChange": "2022-11-06T21:48:38.898+00:00",
                    "lastRefreshTime": "2022-11-06T21:48:38.898+00:00",
                    "minMinutesBetweenRefresh": 10,
                    "failingExceptionMessage": "BASIC-FILES-INTEGRATION-CONNECTORS-404-001 The directory named data/landing-area/hospitals/old-market/clinical-trials/drop-foot does not exist"
                },
                {
                    "connectorId": "51545de2-8776-453c-af8a-0a4dadad5c46",
                    "connectorName": "DropFootClinicalTrialResultsFolderMonitor",
                    "connection": {
                        "class": "Connection",
                        "headerVersion": 0,
                        "connectorType": {
                            "class": "ConnectorType",
                            "headerVersion": 0,
                            "connectorProviderClassName": "org.odpi.openmetadata.adapters.connectors.integration.basicfiles.DataFolderMonitorIntegrationProvider"
                        },
                        "endpoint": {
                            "class": "Endpoint",
                            "headerVersion": 0,
                            "address": "data/data-lake/research/clinical-trials/drop-foot/weekly-measurements"
                        }
                    },
                    "connectorInstanceId": "c6452f6a-620d-49b2-9500-af260403feef",
                    "connectorStatus": "RUNNING",
                    "lastStatusChange": "2022-11-06T21:48:38.945+00:00",
                    "lastRefreshTime": "2022-11-06T21:48:39.000+00:00",
                    "minMinutesBetweenRefresh": 10
                }
            ]
        }
    ]
}
```

This table summarises the results shown above:

| Connector name                            | Status  | Error Message                                                                                                                                  | Connector implementation                                                                              |
|-------------------------------------------|---------|------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| OakDeneLandingAreaFilesMonitor            | RUNNING |                                                                                                                                                | org.odpi.openmetadata.adapters.connectors.integration.basicfiles.DataFilesMonitorIntegrationProvider  |
| OldMarketLandingAreaFilesMonitor          | FAILED  | BASIC-FILES-INTEGRATION-CONNECTORS-404-001 The directory named data/landing-area/hospitals/old-market/clinical-trials/drop-foot does not exist | org.odpi.openmetadata.adapters.connectors.integration.basicfiles.DataFilesMonitorIntegrationProvider  |
| DropFootClinicalTrialResultsFolderMonitor | RUNNING |                                                                                                                                                | org.odpi.openmetadata.adapters.connectors.integration.basicfiles.DataFolderMonitorIntegrationProvider |

Once any problems have been corrected, the integration service can be restarted, which will restart the integration connectors:

```
POST {{serverURLRoot}}/servers/{{serverName}}/open-metadata/integration-daemon/users/{{userId}}/integration-services/files-integrator/restart
```

!!! education "Further information"
    - [Diagnostic Guide](/guides/diagnostic/integration-daemon-diagnostic-guide)


