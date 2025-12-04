<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Troubleshooting issues with the integration daemon

The [integration daemon](/concepts/integration-daemon)
is designed to run as a background process.  It hosts 
[integration connectors](/concepts/integration-connector)
that exchange metadata with third party technologies.  It also
makes calls to a metadata server in order to retrieve and maintain metadata in the open metadata ecosystem.

Most of the time an integration daemon operates without intervention.  However, because digital landscapes are
dynamic, the integration daemon outputs messages to the audit log when it is starting, stopping,
refreshing the connectors and also if one of the connectors throws an exception.
This allows a remote operator to monitor for issues.
The integration daemon also has simple REST API for manually restarting and refreshing the connectors
to enable the integration daemon to recover from errors.

If a connector is incorrectly configured, the integration daemon's configuration document needs to be changed
using [administration commands](/user/admin/servers/configuring-an-integration-daemon/#configuring-the-integration-services)
and the integration daemon [restarted](/guides/operations/overview/#starting-and-stopping-an-omag-server).

## Sources of errors

There are three likely sources of error if an integration daemon is not working properly:

* An integration connector is incorrectly configured or misbehaving
* The third party technology is not available or misbehaving
* The metadata server is not available or misbehaving

The first step is work out which of these is occurring (remembering that there may be multiple failures occurring)
and then the likely cause.  For example:

* Is the configuration correct?
* Are the servers running?
* Do the components have appropriate security access?
* Is the code working properly?

## Diagnostics tools for the integration daemon

The integration daemon has a number of tools to help you diagnose problems.

### Audit Log

The integration daemon (and potentially the connectors) are writing to the audit log destinations
configured for the integration daemon.  This includes details of both the successful metadata exchange
and any errors or failures.

#### Server start up messages

The start-up messages confirm that the integration daemon started successfully.
Here is an example of the start-up of a server:

```
Sat Nov 22 18:46:12 GMT 2025 integration-daemon Startup OMRS-AUDIT-0064 The Open Metadata Repository Services (OMRS) has initialized the audit log for the Integration Daemon called integration-daemon
Sat Nov 22 18:46:12 GMT 2025 integration-daemon Startup SERVER-OPS-0001 The integration-daemon server is configured with a max page size of 1000
Sat Nov 22 18:46:12 GMT 2025 integration-daemon Startup OMRS-AUDIT-0001 The Open Metadata Repository Services (OMRS) is initializing the subsystems to support a new server
Sat Nov 22 18:46:12 GMT 2025 integration-daemon Startup OMRS-AUDIT-0007 The Open Metadata Repository Services (OMRS) has initialized
Sat Nov 22 18:46:12 GMT 2025 integration-daemon Startup SERVER-OPS-0100 The governance services subsystem for the Integration Daemon called integration-daemon is about to start
Sat Nov 22 18:46:12 GMT 2025 integration-daemon Startup INTEGRATION-DAEMON-SERVICES-0001 The integration daemon services are initializing in server integration-daemon
```
It then begins its periodic refresh of the connectors.

When a new connector initializes the context that provides the connector with access to open metadata.
```
Sat Nov 22 18:46:12 GMT 2025 integration-daemon Startup OIF-CONNECTOR-0001 The integration connector context manager is being initialized for calls to server active-metadata-store on platform https://localhost:9443
Sat Nov 22 18:46:12 GMT 2025 integration-daemon Startup OPEN-GOVERNANCE-0002 The open integration context manager is being initialized for calls to server active-metadata-store on platform https://localhost:9443
```


However, there is a sign of trouble in that each connector is reporting an exception at start up.
Message `INTEGRATION-DAEMON-SERVICES-0031` is reporting
```
INTEGRATION-DAEMON-SERVICES-0031 The integration connector OldMarketLandingAreaFilesMonitor method initialize 
has returned with a org.odpi.openmetadata.frameworks.connectors.ffdc.InvalidParameterException exception 
containing message OMAG-MULTI-TENANT-404-001 The OMAG Server cocoMDS1 is not available to service a request 
from user exchangeDL01npa
```
So the metadata server `cocoMDS1` is down and the connectors can not begin processing until it is restarted.

### Retrieving status of the connectors

It is also possible to retrieve the status of the connectors in the integration daemon through the following command:
```
GET {serverRootURL}/servers/{serverName}/open-metadata/integration-daemon/users/{userId}/status
```
Provided the integration daemon is running, it returns a list of connectors with their statuses. You can see the same errors that where recorded in the start-up messages.

```json
{
    "class": "IntegrationDaemonStatusResponse",
    "relatedHTTPCode": 200,
    "integrationServiceSummaries": [
        {
            "integrationServiceId": 4005,
            "integrationServiceFullName": "Files Integrator OMIS",
            "integrationServiceURLMarker": "files-integrator",
            "integrationServiceDescription": "Extract metadata about files stored in a file system or file manager.",
            "integrationServiceWiki": "https://egeria-project.io/services/omis/files-integrator/overview",
            "integrationConnectorReports": [
                {
                    "connectorName": "OakDeneLandingAreaFilesMonitor",
                    "connectorStatus": "FAILED",
                    "lastStatusChange": "2021-02-02T20:57:50.647+00:00",
                    "lastRefreshTime": "2021-02-02T21:01:11.399+00:00",
                    "minMinutesBetweenRefresh": 10,
                    "failingExceptionMessage": "OMAG-MULTI-TENANT-404-001 The OMAG Server cocoMDS1 is not available to service a request from user exchangeDL01npa"
                },
                {
                    "connectorName": "OldMarketLandingAreaFilesMonitor",
                    "connectorStatus": "FAILED",
                    "lastStatusChange": "2021-02-02T20:57:50.657+00:00",
                    "lastRefreshTime": "2021-02-02T21:01:11.399+00:00",
                    "minMinutesBetweenRefresh": 10,
                    "failingExceptionMessage": "OMAG-MULTI-TENANT-404-001 The OMAG Server cocoMDS1 is not available to service a request from user exchangeDL01npa"
                },
                {
                    "connectorName": "DropFootClinicalTrialResultsFilesMonitor",
                    "connectorStatus": "FAILED",
                    "lastStatusChange": "2021-02-02T20:57:50.668+00:00",
                    "lastRefreshTime": "2021-02-02T21:01:11.399+00:00",
                    "minMinutesBetweenRefresh": 10,
                    "failingExceptionMessage": "OMAG-MULTI-TENANT-404-001 The OMAG Server cocoMDS1 is not available to service a request from user exchangeDL01npa"
                }
            ]
        },
        {
            "integrationServiceId": 4004,
            "integrationServiceFullName": "Database Integrator OMIS",
            "integrationServiceURLMarker": "database-integrator",
            "integrationServiceDescription": "Extract metadata such as schema, tables and columns from database managers.",
            "integrationServiceWiki": "https://odpi.github.io/services/omis/database-integrator/overview/",
            "integrationConnectorReports": [
                {
                    "connectorName": "OakDeneLandingAreaDatabaseMonitor",
                    "connectorStatus": "FAILED",
                    "lastStatusChange": "2021-02-02T20:57:50.726+00:00",
                    "lastRefreshTime": "2021-02-02T21:01:11.399+00:00",
                    "minMinutesBetweenRefresh": 10,
                    "failingExceptionMessage": "OMIS-DATABASE-INTEGRATOR-400-001 Integration connector OakDeneLandingAreaDatabaseMonitor is not of the correct type to run in the Database Integrator OMIS integration service.  It must inherit from org.odpi.openmetadata.integrationservices.database.connector.DatabaseIntegratorConnector"
                }
            ]
        }
    ]
}
```

If the `cocoMDS1` metadata server is restarted, the status of the connectors does not change. This is because once a connector goes into **FAILED** status (caused by the connector throwing an exception on one of its standard methods), it needs to be restarted before the integration daemon will start calling it again.  It is possible to restart all connectors registered with an integration service with the following command:

```
GET {serverRootURL}/servers/{serverName}/open-metadata/integration-daemon/users/{userId}/integration-service/{service-url-marker}/restart
```
If you only want to restart a single connector, add the connector name to the request body. The `service-url-marker` for each integration services can be located using the following command:

```
GET {serverRootURL}/servers/{serverName}/platform-services/users/{userId}/server-platform/registered-services/integration-services
```
which returns a list of the valid integration services:
```json
{
    "class": "RegisteredOMAGServicesResponse",
    "relatedHTTPCode": 200,
    "services": [
        {
            "serviceName": "Files Integrator OMIS",
            "serviceURLMarker": "files-integrator",
            "serviceDescription": "Extract metadata about files stored in a file system or file manager.",
            "serviceWiki": "https://odpi.github.io/services/omis/files-integrator/overview/"
        },
        {
            "serviceName": "Security Integrator OMIS",
            "serviceURLMarker": "security-integrator",
            "serviceDescription": "Distribute security properties to security enforcement points.",
            "serviceWiki": "https://odpi.github.io/services/omis/security-integrator/overview/"
        },
        {
            "serviceName": "Database Integrator OMIS",
            "serviceURLMarker": "database-integrator",
            "serviceDescription": "Extract metadata such as schema, tables and columns from database managers.",
            "serviceWiki": "https://odpi.github.io/services/omis/database-integrator/overview/"
        },
        {
            "serviceName": "Lineage Integrator OMIS",
            "serviceURLMarker": "lineage-integrator",
            "serviceDescription": "Manage capture of lineage from a third party tool.",
            "serviceWiki": "https://odpi.github.io/services/omis/lineage-integrator/overview/"
        },
        {
            "serviceName": "Catalog Integrator OMIS",
            "serviceURLMarker": "catalog-integrator",
            "serviceDescription": "Exchange metadata with third party data catalogs.",
            "serviceWiki": "https://odpi.github.io/services/omis/catalog-integrator/overview/"
        },
        {
            "serviceName": "Organization Integrator OMIS",
            "serviceURLMarker": "organization-integrator",
            "serviceDescription": "Load information about the teams and people in an organization and return collaboration activity.",
            "serviceWiki": "https://odpi.github.io/services/omis/organization-integrator/overview/"
        }
    ]
}
```
So the `service-url-marker` for the Files Integrator OMIS is `files-integrator`.


Once the Files Integrator OMIS connectors are restarted, the status changes.  Disappointingly, there are still problems.

```json
{
    "class": "IntegrationDaemonStatusResponse",
    "relatedHTTPCode": 200,
    "integrationServiceSummaries": [
        {
            "integrationServiceId": 4005,
            "integrationServiceFullName": "Files Integrator OMIS",
            "integrationServiceURLMarker": "files-integrator",
            "integrationServiceDescription": "Extract metadata about files stored in a file system or file manager.",
            "integrationServiceWiki": "https://odpi.github.io/services/omis/files-integrator/overview/",
            "integrationConnectorReports": [
                {
                    "connectorName": "OakDeneLandingAreaFilesMonitor",
                    "connectorStatus": "FAILED",
                    "lastStatusChange": "2021-02-02T21:13:01.840+00:00",
                    "lastRefreshTime": "2021-02-02T21:14:02.042+00:00",
                    "minMinutesBetweenRefresh": 10,
                    "failingExceptionMessage": "BASIC-FILES-INTEGRATION-CONNECTORS-404-001 The directory named data/landing-area/hospitals/oak-dene/clinical-trials/drop-foot in the Connection object Connection{displayName='null', description='null', connectorType=ConnectorType{displayName='null', description='null', connectorProviderClassName='org.odpi.openmetadata.adapters.connectors.integration.basicfiles.DataFilesMonitorIntegrationProvider', recognizedAdditionalProperties=null, recognizedSecuredProperties=null, recognizedConfigurationProperties=null, qualifiedName='null', additionalProperties=null, type=null, guid='null', url='null', classifications=null}, endpoint=Endpoint{displayName='null', description='null', address='data/landing-area/hospitals/oak-dene/clinical-trials/drop-foot', protocol='null', encryptionMethod='null', qualifiedName='null', additionalProperties=null, type=null, guid='null', url='null', classifications=null}, userId='null', encryptedPassword='null', clearPassword='null', configurationProperties=null, securedProperties=null, assetSummary='null', qualifiedName='null', additionalProperties=null, meanings=null, securityTags=null, searchKeywords=null, confidentialityGovernanceClassification=null, confidenceGovernanceClassification=null, criticalityGovernanceClassification=null, retentionGovernanceClassification=null, type=null, GUID='null', URL='null', classifications=null, extendedProperties=null, headerVersion=0} does not exist"
                },
                {
                    "connectorName": "OldMarketLandingAreaFilesMonitor",
                    "connectorStatus": "FAILED",
                    "lastStatusChange": "2021-02-02T21:13:01.841+00:00",
                    "lastRefreshTime": "2021-02-02T21:14:02.042+00:00",
                    "minMinutesBetweenRefresh": 10,
                    "failingExceptionMessage": "BASIC-FILES-INTEGRATION-CONNECTORS-404-001 The directory named data/landing-area/hospitals/old-market/clinical-trials/drop-foot in the Connection object Connection{displayName='null', description='null', connectorType=ConnectorType{displayName='null', description='null', connectorProviderClassName='org.odpi.openmetadata.adapters.connectors.integration.basicfiles.DataFilesMonitorIntegrationProvider', recognizedAdditionalProperties=null, recognizedSecuredProperties=null, recognizedConfigurationProperties=null, qualifiedName='null', additionalProperties=null, type=null, guid='null', url='null', classifications=null}, endpoint=Endpoint{displayName='null', description='null', address='data/landing-area/hospitals/old-market/clinical-trials/drop-foot', protocol='null', encryptionMethod='null', qualifiedName='null', additionalProperties=null, type=null, guid='null', url='null', classifications=null}, userId='null', encryptedPassword='null', clearPassword='null', configurationProperties=null, securedProperties=null, assetSummary='null', qualifiedName='null', additionalProperties=null, meanings=null, securityTags=null, searchKeywords=null, confidentialityGovernanceClassification=null, confidenceGovernanceClassification=null, criticalityGovernanceClassification=null, retentionGovernanceClassification=null, type=null, GUID='null', URL='null', classifications=null, extendedProperties=null, headerVersion=0} does not exist"
                },
                {
                    "connectorName": "DropFootClinicalTrialResultsFilesMonitor",
                    "connectorStatus": "FAILED",
                    "lastStatusChange": "2021-02-02T21:13:01.843+00:00",
                    "lastRefreshTime": "2021-02-02T21:14:02.042+00:00",
                    "minMinutesBetweenRefresh": 10,
                    "failingExceptionMessage": "BASIC-FILES-INTEGRATION-CONNECTORS-404-001 The directory named data/data-lake/research/clinical-trials/drop-foot/weekly-measurements in the Connection object Connection{displayName='null', description='null', connectorType=ConnectorType{displayName='null', description='null', connectorProviderClassName='org.odpi.openmetadata.adapters.connectors.integration.basicfiles.DataFolderMonitorIntegrationProvider', recognizedAdditionalProperties=null, recognizedSecuredProperties=null, recognizedConfigurationProperties=null, qualifiedName='null', additionalProperties=null, type=null, guid='null', url='null', classifications=null}, endpoint=Endpoint{displayName='null', description='null', address='data/data-lake/research/clinical-trials/drop-foot/weekly-measurements', protocol='null', encryptionMethod='null', qualifiedName='null', additionalProperties=null, type=null, guid='null', url='null', classifications=null}, userId='null', encryptedPassword='null', clearPassword='null', configurationProperties=null, securedProperties=null, assetSummary='null', qualifiedName='null', additionalProperties=null, meanings=null, securityTags=null, searchKeywords=null, confidentialityGovernanceClassification=null, confidenceGovernanceClassification=null, criticalityGovernanceClassification=null, retentionGovernanceClassification=null, type=null, GUID='null', URL='null', classifications=null, extendedProperties=null, headerVersion=0} does not exist"
                }
            ]
        },
        {
            "integrationServiceId": 4004,
            "integrationServiceFullName": "Database Integrator OMIS",
            "integrationServiceURLMarker": "database-integrator",
            "integrationServiceDescription": "Extract metadata such as schema, tables and columns from database managers.",
            "integrationServiceWiki": "https://odpi.github.io/services/omis/database-integrator/overview/",
            "integrationConnectorReports": [
                {
                    "connectorName": "OakDeneLandingAreaDatabaseMonitor",
                    "connectorStatus": "FAILED",
                    "lastStatusChange": "2021-02-02T20:57:50.726+00:00",
                    "lastRefreshTime": "2021-02-02T21:14:04.052+00:00",
                    "minMinutesBetweenRefresh": 10,
                    "failingExceptionMessage": "OMIS-DATABASE-INTEGRATOR-400-001 Integration connector OakDeneLandingAreaDatabaseMonitor is not of the correct type to run in the Database Integrator OMIS integration service.  It must inherit from org.odpi.openmetadata.integrationservices.database.connector.DatabaseIntegratorConnector"
                }
            ]
        }
    ]
}
```
However, it is clear from the message identifier `BASIC-FILES-INTEGRATION-CONNECTORS-404-001` that the problem is being reported by the connector itself.  This means the integration service is now working ok even if the connectors are not.

Once the expected directories (folders) are created, the *files* integration connectors and be restarted and begin to work:

```json
{
    "class": "IntegrationDaemonStatusResponse",
    "relatedHTTPCode": 200,
    "integrationServiceSummaries": [
        {
            "integrationServiceId": 4005,
            "integrationServiceFullName": "Files Integrator OMIS",
            "integrationServiceURLMarker": "files-integrator",
            "integrationServiceDescription": "Extract metadata about files stored in a file system or file manager.",
            "integrationServiceWiki": "https://odpi.github.io/services/omis/files-integrator/overview/",
            "integrationConnectorReports": [
                {
                    "connectorName": "OakDeneLandingAreaFilesMonitor",
                    "connectorStatus": "RUNNING",
                    "lastStatusChange": "2021-02-02T21:39:31.496+00:00",
                    "lastRefreshTime": "2021-02-02T21:40:02.280+00:00",
                    "minMinutesBetweenRefresh": 10
                },
                {
                    "connectorName": "OldMarketLandingAreaFilesMonitor",
                    "connectorStatus": "RUNNING",
                    "lastStatusChange": "2021-02-02T21:39:31.662+00:00",
                    "lastRefreshTime": "2021-02-02T21:40:02.336+00:00",
                    "minMinutesBetweenRefresh": 10
                },
                {
                    "connectorName": "DropFootClinicalTrialResultsFilesMonitor",
                    "connectorStatus": "RUNNING",
                    "lastStatusChange": "2021-02-02T21:39:31.742+00:00",
                    "lastRefreshTime": "2021-02-02T21:40:02.392+00:00",
                    "minMinutesBetweenRefresh": 10
                }
            ]
        },
        {
            "integrationServiceId": 4004,
            "integrationServiceFullName": "Database Integrator OMIS",
            "integrationServiceURLMarker": "database-integrator",
            "integrationServiceDescription": "Extract metadata such as schema, tables and columns from database managers.",
            "integrationServiceWiki": "https://odpi.github.io/services/omis/database-integrator/overview/",
            "integrationConnectorReports": [
                {
                    "connectorName": "OakDeneLandingAreaDatabaseMonitor",
                    "connectorStatus": "FAILED",
                    "lastStatusChange": "2021-02-02T20:57:50.726+00:00",
                    "lastRefreshTime": "2021-02-02T21:40:00.220+00:00",
                    "minMinutesBetweenRefresh": 10,
                    "failingExceptionMessage": "OMIS-DATABASE-INTEGRATOR-400-001 Integration connector OakDeneLandingAreaDatabaseMonitor is not of the correct type to run in the Database Integrator OMIS integration service.  It must inherit from org.odpi.openmetadata.integrationservices.database.connector.DatabaseIntegratorConnector"
                }
            ]
        }
    ]
}
```

## Resynchronizing after a failure

If a connector has been unavailable for a while, it is possible it has missed some metadata changes either in the third party technology or in the open metadata ecosystem.  The integration daemon has a REST API to call `refresh` on:
* 
* All connectors
* All connectors in an integration service
* A single connector

The refresh command requests that the connector does a comparison of the metadata in its third party technology and the open metadata ecosystem and make good any discrepancies it finds.

These are the three forms of the refresh call in the order listed above. The first refreshes all connectors running in the integration daemon.

```
POST {serverRootURL}/servers/{serverName}/open-metadata/integration-daemon/users/{userId}/refresh
```

This second command refreshes all connectors running under an integration service. If the name of a connector is included in the request body then just that connector is refreshed.

```
POST {serverRootURL}/servers/{serverName}/open-metadata/integration-daemon/users/{userId}/integration-service/{service-url-marker}/refresh
```

The refresh processing can be an expensive operation, so it should only be requested when there has been an outage.

## Further information

* Configuring the [Integration daemon](/concepts/integration-daemon)
* Design of the [Integration daemon](/services/integration-daemon-services)
* Understanding [Integration connectors](/concepts/integration-connector)
* Understanding [Open Metadata Integration Services (OMIS)](/services/omis)

--8<-- "snippets/abbr.md"
