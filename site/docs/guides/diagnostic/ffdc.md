<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


# First failure data capture (FFDC)

Egeria will typically be embedded in complex deployment environments. Because of this, the Egeria community tries to practice First Failure Data Capture (FFDC).

First Failure Data Capture (FFDC) is an approach to error handling that aims to guide the support team to the cause of an error based on the output of a single, or small number of, messages, rather than relying on tracing through the logic flow.

This is not always possible, particularly for bugs and unexpected
runtime conditions, but it is a worthy goal because it is rarely practical
to turn on debug tracing in a production system.

FFDC typically requires as much information as possible to be gathered
at the point where the error is first detected.  This information is added to as the
call unwinds.  This way it captures:

 - What went wrong precisely
 - What was the server doing when it went wrong
 - What is the consequence of this failure to the caller, or others

FFDC requires careful design by the developer because they need to anticipate the likely errors and design the error handling accordingly. Many modules have more error handling code than "happy path code". In addition, there is wide-spread use of two important components throughout Egeria.

- The [FFDC Services](/services/ffdc-services) -
  provides base services for implementing FFDC in an Egeria module.

     - Common audit log messages and exception codes.
     - Common exceptions and base exceptions.
     - Common REST Structures.
     - Invalid parameter handler for common parameter types.
     - REST Call logger for debug messages and performance logging.
     - Handler for common exceptions.
     
- The [Audit Log Framework (ALF)](/frameworks/alf/overview) -
  provides interface definitions and classes to enable connectors to support natural language enabled
  diagnostics such as exception messages and audit log messages.

The result is the consistent availability of detailed diagnostics when things go wrong.

In addition, the [Open Metadata Repository Services (OMRS)](/services/omrs) provides an extension to the ALF's audit log destination that supports multiple [audit log store connectors](/concepts/audit-log-connectors). This means that an OMAG Server can be configured to route audit log messages to multiple destinations.

![Using different log destination](/frameworks/alf/audit-log-framework-overview.svg)

Details of the supported audit log store connectors and how to set them up are described in [Configuring the Audit Log](/guides/admin/servers/by-section-repository-services-section/#configuring-the-audit-log).

## FFDC principles practised by the Egeria community

- Each type of message has a unique identifier and the parameters embedded in it are sufficient to determine the call parameters and the code path to the exact point where the error is detected.

- All parameters are validated both client side and server side.

- APIs use different types of exceptions to separate:

  - Invalid parameters from the caller
  - User security errors that need administrator action
  - Temporary problems in the server
  - Bugs and logic errors (ie reaching a point in the path that should be impossible).
  
  Typically, the modules use checked exceptions for the first three types of errors and runtime exceptions for the last.
  
- Where there is no direct external caller, errors are logging the Audit Log rather than throwing an exception in a background thread.
  
- Exception objects containing stack traces never leave the OMAG Server Platform. The full exception is added to the Audit Log so the stack trace can be analysed by the platform team. Important diagnostic information - such as the exception type, message, system action and user action is captured in the REST response. If the calling program is an Egeria client, it recreates the exception (minus the stack trace of course) and throws it to its caller. That way, all information about the exception is preserved without compromising the security of the server platform.

## Audit log record examples

Below is an example of an audit log record formatted in JSON.  This is the style of output from Egeria's file-based and topic-based audit log destinations.  Notice it includes details of the originating server, component and thread.  The message description includes information about how to resolve an issue (if there is one to resolve).  The message parameters are the values from the runtime that are inserted into the message.  They are provided to allow translated messages to be produced for non-English speakers.

```json
{
    "guid": "f150879d-f807-47ae-a7e6-5d48118044a5",
    "timeStamp": 1689528452722,
    "originatorProperties": {
        "organizationName": null,
        "serverType": "Open Metadata and Governance Server",
        "serverName": "atlasexchange"
    },
    "originatorComponent": {
        "componentId": 659,
        "componentDevelopmentStatus": "IN_DEVELOPMENT",
        "componentName": "Egeria:IntegrationConnector:Catalog:ApacheAtlas:3ab99700-7750-4eca-8670-55b6f21bda14",
        "componentDescription": "Connector publishes active glossary terms to Apache Atlas.",
        "componentWikiURL": "https://egeria-project.org/connectors/integration/apache-atlas-integration-connector/"
    },
    "actionDescription": "processAtlasGlossaryTerm",
    "threadId": 185,
    "threadName": "atlasexchange::IntegrationDaemonThread",
    "severityCode": 5,
    "severity": "Error",
    "messageId": "APACHE-ATLAS-INTEGRATION-CONNECTOR-0015",
    "messageText": "The open metadata glossary term 52ca009f-0fa6-495e-b760-2a5b33f7281f for equivalent Apache Atlas glossary term custName has been unilaterally deleted; connector AtlasIntegrator is putting it back",
    "messageParameters": [
        "52ca009f-0fa6-495e-b760-2a5b33f7281f",
        "custName",
        "AtlasIntegrator"
    ],
    "systemAction": "The open metadata glossary term can not be retrieved.  This glossary term is owned by Apache Atlas.  The connector is creating a new copy of the Apache Atlas glossary term in the open metadata ecosystem.",
    "userAction": "Open metadata glossary terms that are copies from Apache Atlas should not be unilaterally removed.  Investigate why this element is missing from the open metadata ecosystem and make changes so it can not happen again."
}
```

This next example shows an *Exception* message.  Typically, these are produced (rather than an "Error" audit log record) when the cause and resolution is unknown, and so some expert diagnotics work may be needed to resolve the issue.  It includes information of the exception and the stack trace.
```json
{
    "guid": "fa564cc3-699d-4c52-afdf-db4f578baf9e",
    "timeStamp": 1689539792943,
    "originatorProperties": {
        "organizationName": null,
        "serverType": "Open Metadata and Governance Server",
        "serverName": "atlasexchange"
    },
    "originatorComponent": {
        "componentId": 659,
        "componentDevelopmentStatus": "IN_DEVELOPMENT",
        "componentName": "Egeria:IntegrationConnector:Catalog:ApacheAtlas:3ab99700-7750-4eca-8670-55b6f21bda14",
        "componentDescription": "Connector publishes active glossary terms to Apache Atlas.",
        "componentWikiURL": "https://egeria-project.org/connectors/integration/apache-atlas-integration-connector/"
    },
    "actionDescription": "saveAtlasGlossaryCategory(glossaryGUID)",
    "threadId": 297,
    "threadName": "OpenMetadataTopicListener: egeria.omag.server.cocoMDS1.omas.assetmanager.outTopic",
    "severityCode": 6,
    "severity": "Exception",
    "messageId": "APACHE-ATLAS-INTEGRATION-CONNECTOR-0031",
    "messageText": "A client-side exception was received from API call saveAtlasGlossaryCategory(glossaryGUID) to server Apache Atlas at https://cocopharmaceuticals.com:21000.  The error message was CLIENT-SIDE-REST-API-CONNECTOR-503-002 A client-side exception org.springframework.web.client.HttpClientErrorException$Conflict was received by method saveAtlasGlossaryCategory(glossaryGUID) from API call https://cocopharmaceuticals.com:21000/api/atlas/v2/glossary/category/{0} to server Apache Atlas on platform https://cocopharmaceuticals.com:21000.  The error message was 409 Conflict: \"{\"errorCode\":\"ATLAS-409-00-00A\",\"errorMessage\":\"Glossary category with qualifiedName Payment Method.Payment Method@Cloud Information Model (CIM) already exists\"}\"",
    "messageParameters": [
        "saveAtlasGlossaryCategory(glossaryGUID)",
        "Apache Atlas",
        "https://cocopharmaceuticals.com:21000",
        "CLIENT-SIDE-REST-API-CONNECTOR-503-002 A client-side exception org.springframework.web.client.HttpClientErrorException$Conflict was received by method saveAtlasGlossaryCategory(glossaryGUID) from API call https://cocopharmaceuticals.com:21000/api/atlas/v2/glossary/category/{0} to server Apache Atlas on platform https://cocopharmaceuticals.com:21000.  The error message was 409 Conflict: \"{\"errorCode\":\"ATLAS-409-00-00A\",\"errorMessage\":\"Glossary category with qualifiedName Payment Method.Payment Method@Cloud Information Model (CIM) already exists\"}\""
    ],
    "systemAction": "The server has issued a call to the open metadata access service REST API in a remote server and has received an exception from the local client libraries.",
    "userAction": "Look for errors in the local server's console to understand and correct the source of the error.",
    "exceptionClassName": "org.odpi.openmetadata.adapters.connectors.restclients.ffdc.exceptions.RESTServerException",
    "exceptionMessage": "CLIENT-SIDE-REST-API-CONNECTOR-503-002 A client-side exception org.springframework.web.client.HttpClientErrorException$Conflict was received by method saveAtlasGlossaryCategory(glossaryGUID) from API call https://cocopharmaceuticals.com:21000/api/atlas/v2/glossary/category/{0} to server Apache Atlas on platform https://cocopharmaceuticals.com:21000.  The error message was 409 Conflict: \"{\"errorCode\":\"ATLAS-409-00-00A\",\"errorMessage\":\"Glossary category with qualifiedName Payment Method.Payment Method@Cloud Information Model (CIM) already exists\"}\"",
    "exceptionStackTrace": "RESTServerException{reportedHTTPCode=503, reportingClassName='org.odpi.openmetadata.adapters.connectors.restclients.spring.SpringRESTClientConnector', reportingActionDescription='saveAtlasGlossaryCategory(glossaryGUID)', errorMessage='CLIENT-SIDE-REST-API-CONNECTOR-503-002 A client-side exception org.springframework.web.client.HttpClientErrorException$Conflict was received by method saveAtlasGlossaryCategory(glossaryGUID) from API call https://cocopharmaceuticals.com:21000/api/atlas/v2/glossary/category/{0} to server Apache Atlas on platform https://cocopharmaceuticals.com:21000.  The error message was 409 Conflict: \"{\"errorCode\":\"ATLAS-409-00-00A\",\"errorMessage\":\"Glossary category with qualifiedName Payment Method.Payment Method@Cloud Information Model (CIM) already exists\"}\"', reportedSystemAction='The client has issued a call to the open metadata access service REST API in a remote server and has received an exception from the local client libraries.', reportedUserAction='Review the error message to determine the cause of the error.  Check that the server is running an the URL is correct. Look for errors in the local server's console to understand and correct the cause of the error. Then rerun the request', reportedCaughtException=org.springframework.web.client.HttpClientErrorException$Conflict: 409 Conflict: \"{\"errorCode\":\"ATLAS-409-00-00A\",\"errorMessage\":\"Glossary category with qualifiedName Payment Method.Payment Method@Cloud Information Model (CIM) already exists\"}\"}\n\tat org.odpi.openmetadata.adapters.connectors.restclients.spring.SpringRESTClientConnector.callPutRESTCall(SpringRESTClientConnector.java:568)\n\tat org.odpi.openmetadata.adapters.connectors.integration.apacheatlas.ApacheAtlasRESTClient.callPutRESTCall(ApacheAtlasRESTClient.java:610)\n\tat org.odpi.openmetadata.adapters.connectors.integration.apacheatlas.ApacheAtlasRESTClient.saveAtlasGlossaryCategory(ApacheAtlasRESTClient.java:343)\n\tat org.odpi.openmetadata.adapters.connectors.integration.apacheatlas.ApacheAtlasIntegrationConnector.refreshEgeriaGlossaryCategoryInAtlas(ApacheAtlasIntegrationConnector.java:1585)\n\tat org.odpi.openmetadata.adapters.connectors.integration.apacheatlas.ApacheAtlasIntegrationConnector.processEgeriaGlossaryCategory(ApacheAtlasIntegrationConnector.java:946)\n\tat org.odpi.openmetadata.adapters.connectors.integration.apacheatlas.ApacheAtlasIntegrationConnector.processEvent(ApacheAtlasIntegrationConnector.java:407)\n\tat org.odpi.openmetadata.accessservices.assetmanager.connectors.outtopic.AssetManagerOutTopicClientConnector.processEvent(AssetManagerOutTopicClientConnector.java:75)\n\tat org.odpi.openmetadata.repositoryservices.connectors.openmetadatatopic.OpenMetadataTopicConnector.distributeEvent(OpenMetadataTopicConnector.java:163)\n\tat org.odpi.openmetadata.repositoryservices.connectors.openmetadatatopic.OpenMetadataTopicConnector.run(OpenMetadataTopicConnector.java:121)\n\tat java.base/java.lang.Thread.run(Thread.java:833)\nCaused by: org.springframework.web.client.HttpClientErrorException$Conflict: 409 Conflict: \"{\"errorCode\":\"ATLAS-409-00-00A\",\"errorMessage\":\"Glossary category with qualifiedName Payment Method.Payment Method@Cloud Information Model (CIM) already exists\"}\"\n\tat org.springframework.web.client.HttpClientErrorException.create(HttpClientErrorException.java:121)\n\tat org.springframework.web.client.DefaultResponseErrorHandler.handleError(DefaultResponseErrorHandler.java:183)\n\tat org.springframework.web.client.DefaultResponseErrorHandler.handleError(DefaultResponseErrorHandler.java:137)\n\tat org.springframework.web.client.ResponseErrorHandler.handleError(ResponseErrorHandler.java:63)\n\tat org.springframework.web.client.RestTemplate.handleResponse(RestTemplate.java:915)\n\tat org.springframework.web.client.RestTemplate.doExecute(RestTemplate.java:864)\n\tat org.springframework.web.client.RestTemplate.execute(RestTemplate.java:764)\n\tat org.springframework.web.client.RestTemplate.exchange(RestTemplate.java:646)\n\tat org.odpi.openmetadata.adapters.connectors.restclients.spring.SpringRESTClientConnector.callPutRESTCall(SpringRESTClientConnector.java:533)\n\t... 9 more\n"
}
```

## Exceptions

### An example of a response from a REST API call

This is how an exception is passed from the OMAG Server Platform to a calling program.  

```json
{
    "class": "VoidResponse",
    "relatedHTTPCode": 400,
    "exceptionClassName": "org.odpi.openmetadata.frameworks.connectors.ffdc.PropertyServerException",
    "exceptionCausedBy": "java.lang.NullPointerException",
    "actionDescription": "refreshService",
    "exceptionErrorMessage": "OMAG-COMMON-400-016 An unexpected java.lang.NullPointerException exception was caught by refreshService; error message was null",
    "exceptionErrorMessageId": "OMAG-COMMON-400-016",
    "exceptionErrorMessageParameters": [
        "java.lang.NullPointerException",
        "refreshService",
        "null"
    ],
    "exceptionSystemAction": "The system is unable to process the request and has returned an exception to the caller.",
    "exceptionUserAction": "Review the error message.  Also look up its full message definition which includes the system action and user action.  This is most likely to describe the correct action to take to resolve the error.  If that does not help, look for other diagnostics created at the same time.  Also validate that the caller is a valid client of this server and is operating correctly."
}
```

and another example:

```json
{
    "class": "VoidResponse",
    "relatedHTTPCode": 404,
    "exceptionClassName": "org.odpi.openmetadata.frameworks.connectors.ffdc.InvalidParameterException",
    "actionDescription": "refreshService",
    "exceptionErrorMessage": "OMAG-MULTI-TENANT-404-001 The OMAG Server exchangeDL01 is not available to service a request from user garygeeke",
    "exceptionErrorMessageId": "OMAG-MULTI-TENANT-404-001",
    "exceptionErrorMessageParameters": [
        "exchangeDL01",
        "garygeeke"
    ],
    "exceptionSystemAction": "The system is unable to process the request because the server is not running on the called platform.",
    "exceptionUserAction": "Verify that the correct server is being called on the correct platform and that this server is running. Retry the request when the server is available.",
    "exceptionProperties": {
        "serverName": "exchangeDL01",
        "parameterName": "serverName"
    }
}
```

Additional examples of common errors are shown [here](/guides/diagnostic/examples-of-common-rest-api-errors).

## Audit Log Messages

The diagram below illustrates the structure of the audit log records:

![Audit log record structure](/concepts/audit-log-record.svg)

### Audit Log Record Severities

The audit log severities supported by the OMAG Servers are as follows:

- *Information* - The server is providing information about its normal operation.
- *Event* - An event was received from another member of the open metadata repository cohort.
- *Decision* - A decision has been made related to the interaction of the local metadata repository and the rest of the cohort.
- *Action* - An Action is required by the administrator. At a minimum, the situation needs to be investigated and 
  if necessary, corrective action taken.
- *Error* - An error occurred, possibly caused by an incompatibility between the local metadata repository
  and one of the remote repositories. The local repository may restrict some of the metadata interchange
  functions as a result.
- *Exception* - An unexpected exception occurred.  This means that the server needs some administration
  attention to correct configuration or fix a logic error because it is not operating as a proper peer in the
  open metadata repository cohort.
- *Security* - Unauthorized access to a service or metadata instance has been attempted.
- *Startup* - A new component is starting up.
- *Shutdown* - An existing component is shutting down.
- *Asset* - An auditable action relating to an asset has been taken.
- *Types* - Activity is occurring that relates to the open metadata types in use by this server.
- *Cohort* - The server is exchanging registration information about an open metadata repository cohort that
  it is connecting to.
- *Trace* - This is additional information on the operation of the server that may be
  of assistance in debugging a problem.  It is not normally logged to any destination, but can be added when needed.,
- *PerfMon* - This log record contains performance monitoring timing information for 
  specific types of processing. It is not normally logged to any destination, but can be added when needed.
- *\<Unknown\>* - Uninitialized Severity

### Example of an audit log message
Below is an example of the types of information captured in an audit log record.
```json
{
    "guid": "bfc4ebe9-0550-4c33-b3d6-aa760401b400",
    "timeStamp": 1583442856062,
    "originatorProperties": {
        "Server Name": "findItDL01",
        "Organization Name": "Coco Pharmaceuticals",
        "Server Type": "Open Metadata and Governance Server"
    },
    "originatorComponent": {
        "componentId": 2000,
        "componentName": "Discovery Engine Services",
        "componentWikiURL": "https://egeria.odpi.org/open-metadata-implementation/governance-servers/discovery-engine-services/",
        "componentType": "Run automated discovery services"
    },
    "actionDescription": "Register configuration listener",
    "threadId": 116,
    "threadName": "org.odpi.openmetadata.governanceservers.discoveryengineservices.handlers.DiscoveryConfigurationRefreshHandler",
    "severityCode": 5,
    "severity": "Error",
    "messageId": "DISCOVERY-ENGINE-SERVICES-0028",
    "messageText": "Failed to refresh configuration for discovery engine AssetQuality.  The exception was org.odpi.openmetadata.frameworks.connectors.ffdc.PropertyServerException with error message DISCOVERY-ENGINE-SERVICES-400-014 Properties for discovery engine called AssetQuality have not been returned by open metadata server cocoMDS1 to discovery server cocoMDS1",
    "messageParameters": [
        "AssetQuality",
        "org.odpi.openmetadata.frameworks.connectors.ffdc.PropertyServerException",
        "DISCOVERY-ENGINE-SERVICES-400-014 Properties for discovery engine called AssetQuality have not been returned by open metadata server cocoMDS1 to discovery server cocoMDS1"
    ],
    "additionalInformation": [
        "PropertyServerException{reportedHTTPCode=400, reportingClassName='org.odpi.openmetadata.governanceservers.discoveryengineservices.handlers.DiscoveryEngineHandler', reportingActionDescription='refreshConfig', errorMessage='DISCOVERY-ENGINE-SERVICES-400-014 Properties for discovery engine called AssetQuality have not been returned by open metadata server cocoMDS1 to discovery server cocoMDS1', reportedSystemAction='The discovery server is not able to initialize the discovery engine and so it will not de able to support discovery requests targeted to this discovery engine.', reportedUserAction='This may be a configuration error or the metadata server may be down.  Look for other error messages and review the configuration of the discovery server.  Once the cause is resolved, restart the discovery server.', reportedCaughtException=null, relatedProperties=null}"
    ],
    "systemAction": "The discovery engine is unable to process any discovery requests until its configuration can be retrieved.",
    "userAction": "Review the error messages and resolve the cause of the problem.  Either wait for the discovery server to refresh the configuration, or issue the refreshConfigcall to request that the discovery engine calls the Discovery Engine OMAS to refresh the configuration for the discovery service.",
    "exceptionClassName": "org.odpi.openmetadata.frameworks.connectors.ffdc.PropertyServerException",
    "exceptionMessage": "DISCOVERY-ENGINE-SERVICES-400-014 Properties for discovery engine called AssetQuality have not been returned by open metadata server cocoMDS1 to discovery server cocoMDS1",
    "exceptionStackTrace": "PropertyServerException{reportedHTTPCode=400, reportingClassName='org.odpi.openmetadata.governanceservers.discoveryengineservices.handlers.DiscoveryEngineHandler', reportingActionDescription='refreshConfig', errorMessage='DISCOVERY-ENGINE-SERVICES-400-014 Properties for discovery engine called AssetQuality have not been returned by open metadata server cocoMDS1 to discovery server cocoMDS1', reportedSystemAction='The discovery server is not able to initialize the discovery engine and so it will not de able to support discovery requests targeted to this discovery engine.', reportedUserAction='This may be a configuration error or the metadata server may be down.  Look for other error messages and review the configuration of the discovery server.  Once the cause is resolved, restart the discovery server.', reportedCaughtException=null, relatedProperties=null}\n\tat org.odpi.openmetadata.governanceservers.discoveryengineservices.handlers.DiscoveryEngineHandler.refreshConfig(DiscoveryEngineHandler.java:154)\n\tat org.odpi.openmetadata.governanceservers.discoveryengineservices.handlers.DiscoveryConfigurationRefreshHandler.run(DiscoveryConfigurationRefreshHandler.java:140)\n\tat java.lang.Thread.run(Thread.java:748)\n",
    "originator": {
        "serverName": "findItDL01",
        "serverType": "Open Metadata and Governance Server",
        "organizationName": "Coco Pharmaceuticals"
    },
    "reportingComponent": {
        "componentId": 2000,
        "componentName": "Discovery Engine Services",
        "componentWikiURL": "https://egeria.odpi.org/open-metadata-implementation/governance-servers/discovery-engine-services/",
        "componentType": "Run automated discovery services"
    }
}
```

## Further information

* [Configuring the audit log destinations](/guides/admin/servers/by-section/repository-services-section/#configuring-the-audit-log).


--8<-- "snippets/abbr.md"
