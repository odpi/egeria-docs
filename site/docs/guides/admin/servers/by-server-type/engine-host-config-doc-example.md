<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


```json
{
    "class": "OMAGServerConfigResponse",
    "relatedHTTPCode": 200,
    "omagserverConfig": {
        "class": "OMAGServerConfig",
        "versionId": "V2.0",
        "localServerId": "099d1128-b466-4426-bca2-b6087f394f72",
        "localServerName": "engine-host",
        "localServerURL": "https://localhost:9443",
        "localServerUserId": "enginehostnpa",
        "maxPageSize": 1000,
        "repositoryServicesConfig": {
            "class": "RepositoryServicesConfig",
            "auditLogConnections": [
                {
                    "class": "Connection",
                    "headerVersion": 0,
                    "qualifiedName": "Console- default",
                    "displayName": "Console",
                    "connectorType": {
                        "class": "ConnectorType",
                        "headerVersion": 0,
                        "connectorProviderClassName": "org.odpi.openmetadata.adapters.repositoryservices.auditlogstore.console.ConsoleAuditLogStoreProvider"
                    },
                    "configurationProperties": {
                        "supportedSeverities": [
                            "Unknown",
                            "Information",
                            "Decision",
                            "Action",
                            "Error",
                            "Exception",
                            "Security",
                            "Startup",
                            "Shutdown",
                            "Asset",
                            "Cohort"
                        ]
                    }
                }
            ]
        },
        "engineHostServicesConfig": {
            "class": "EngineHostServicesConfig",
            "engineList": [
                {
                    "class": "EngineConfig",
                    "engineId": "4fe58760-ec4c-4f23-89c2-f7ae979e0e8b",
                    "engineQualifiedName": "AssetSurvey",
                    "engineUserId": "generalnpa"
                },
                {
                    "class": "EngineConfig",
                    "engineId": "a80b17a8-ce6f-4cbc-b8bc-ff71b594f175",
                    "engineQualifiedName": "FileProvisioning",
                    "engineUserId": "generalnpa"
                },
                {
                    "class": "EngineConfig",
                    "engineId": "1a86651a-c9c1-4aee-8a83-4c028d89f774",
                    "engineQualifiedName": "AssetGovernance",
                    "engineUserId": "generalnpa"
                }
            ],
            "omagserverPlatformRootURL": "https://localhost:9443",
            "omagserverName": "active-metadata-store"
        },
        "auditTrail": [
            "Fri Jan 26 15:13:20 GMT 2024 garygeeke updated configuration for local server's userId to enginehostnpa.",
            "Fri Jan 26 15:13:54 GMT 2024 garygeeke updated configuration for Engine Host Services access service root url to https://localhost:9443.",
            "Fri Jan 26 15:14:10 GMT 2024 garygeeke updated engine list."
        ]
    }
}
```