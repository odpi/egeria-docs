<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# Automated Curation API

Key features of this service include:

* **Technology Type Management**: Browsing and searching for the technology types supported by the ecosystem's integration connectors and governance engines.
* **Governance and Engine Action Management**: Initiating, canceling, and monitoring governance actions and engine actions.
* **Governance Action Process Cancellation**: Cancelling every unfinished engine action of a running governance action process instance.
* **Templated Cataloguing**: Support for creating metadata elements using templates, ensuring consistency in the cataloguing process.
* **Client-Side Secret Management**: Saving and deleting secrets (such as credentials) used by client-side integration components.

## API Operations

The Automated Curation API provides services that can be used to set up and monitor the automation services from Egeria:

* Retrieving information about different technologies with their linked templates and resources.
* Adding catalog targets to [integration connectors](/concepts/integration-connector) running in an [Integration Daemon](/concepts/integration-daemon).
* Initiating governance action types, governance action processes and [engine actions](/concepts/engine-action).
* Monitoring the outcomes of engine actions.
* Cancelling engine actions and running governance action processes.

!!! warning "The operations for running engine actions have moved to the Governance Engine API"
    `claimEngineAction`, `getActiveClaimedEngineActions`, `updateEngineActionStatus`, `updateActionTargetStatus` and `recordCompletionStatus` are used by a governance engine to claim an engine action, report its progress and record its completion.  They were previously part of this API and are now in the [Governance Engine API](/services/omvs/governance-engine/overview).  Their paths, request bodies and responses are unchanged, so callers such as [pyegeria](/guides/developer/python-clients/overview) only need to replace the `automated-curation` URL marker with `governance-engine`.


## Retrieving details about supported technologies

Automated Curation API provides methods to query the supported technology types.  The technology types provide the reference data to guide the curator.  They are extracted from the valid values for [*deployedImplementationType*](/concepts/deployed-implementation-type).

The `getTechnologyTypesForOpenMetadataType` operation retrieves the list of deployed implementation type metadata elements linked to a particular open metadata type.

```
@typeName=SoftwareServer

POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/automated-curation/open-metadata-types/{{typeName}}/technology-types
Authorization: Bearer {{token}}
Content-Type: application/json

{
  "class" : "ResultsRequestBody",
  "startFrom" : 0,
  "pageSize" : 0
}
```
The `findTechnologyTypes` operation retrieves the list of deployed implementation type metadata elements that contain the search string.
```
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/automated-curation/technology-types/by-search-string
Authorization: Bearer {{token}}
Content-Type: application/json

{
  "class" : "SearchStringRequestBody",
  "searchString" : "PostgreSQL",
  "startsWith" : false,
  "endsWith" : false,
  "ignoreCase" : true,
  "startFrom" : 0,
  "pageSize" : 0
}
```
Once the desired technology has been identified, the attached templates and resources can be retrieved using the `getTechnologyTypeDetail` operation.
```
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/automated-curation/technology-types/by-name
Authorization: Bearer {{token}}
Content-Type: application/json

{
  "class" : "FilterRequestBody",
  "filter" : "PostgreSQL Server"
}
```
The request body is optional on each of these operations.  The paging values (`startFrom` and `pageSize`) and the search options (`startsWith`, `endsWith` and `ignoreCase`) are passed in the request body rather than as request parameters.  The same `FilterRequestBody` is used to name the technology type on the `getTechnologyTypeHierarchy` (`/technology-types/hierarchy`) and `getTechnologyTypeElements` (`/technology-types/elements`) operations.


Below is the list of technology types returned by `findTechnologyTypes` for `PostgreSQL`.
```json
{
  "class": "TechnologyTypeSummaryListResponse",
  "requestId": "fad0b6b4-6b9a-4177-bd65-016654d6e55f",
  "relatedHTTPCode": 200,
  "elements": [
    {
      "technologyTypeGUID": "aa50ce4c-917d-4880-a987-d6c771b822b2",
      "qualifiedName": "Egeria:ValidMetadataValue:TabularDataSet:deployedImplementationType-(PostgreSQL Tabular Data Set)",
      "displayName": "PostgreSQL Tabular Data Set",
      "description": "A database table hosted on a PostgreSQL relational database server that has the tabular data set interface.",
      "category": "Valid Metadata Values",
      "url": "https://www.postgresql.org/"
    },
    {
      "technologyTypeGUID": "c113b127-ae8d-417f-90f2-92108c141270",
      "qualifiedName": "Egeria:ValidMetadataValue:TabularDataSetCollection:deployedImplementationType-(PostgreSQL Tabular Data Set Collection)",
      "displayName": "PostgreSQL Tabular Data Set Collection",
      "description": "A database schema hosted on a PostgreSQL relational database server that has the tabular data set collection interface.",
      "category": "Valid Metadata Values",
      "url": "https://www.postgresql.org/"
    },
    {
      "technologyTypeGUID": "cdfedb9c-8020-422d-b89e-40c57df22bd0",
      "qualifiedName": "Egeria:ValidMetadataValue:DatabaseManager:deployedImplementationType-(PostgreSQL database manager (RDBMS))",
      "displayName": "PostgreSQL database manager (RDBMS)",
      "description": "The PostgreSQL capability that manages collections of data called relational databases which in turn are organized into a tabular format and accessed via the Structured Query Language (SQL).",
      "category": "Valid Metadata Values",
      "url": "https://egeria-project.org/types/0/0050-Applications-and-Processes/"
    },
    {
      "technologyTypeGUID": "e46811ac-8b86-42c3-aaea-2fe55f474044",
      "qualifiedName": "Egeria:ValidMetadataValue:DeployedDatabaseSchema:deployedImplementationType-(PostgreSQL Relational Database Schema)",
      "displayName": "PostgreSQL Relational Database Schema",
      "description": "A database schema hosted on a PostgreSQL relational database server capable of being called through a JDBC Driver.",
      "category": "Valid Metadata Values",
      "url": "https://www.postgresql.org/"
    },
    {
      "technologyTypeGUID": "f5edc367-6a11-4115-bf59-85278928f405",
      "qualifiedName": "Egeria:ValidMetadataValue:DataSet:deployedImplementationType-(PostgreSQL Table)",
      "displayName": "PostgreSQL Table",
      "description": "A table in a PostgreSQL database.  OpenLineage names it postgres://{host}:{port} + {database}.{schema}.{table}.",
      "category": "Valid Metadata Values",
      "url": "https://www.postgresql.org/"
    },
    {
      "technologyTypeGUID": "ff56fc56-c4a1-469e-8040-472e8fe54694",
      "qualifiedName": "Egeria:ValidMetadataValue:RelationalDatabase:deployedImplementationType-(PostgreSQL Relational Database)",
      "displayName": "PostgreSQL Relational Database",
      "description": "A database hosted on a PostgreSQL server.",
      "category": "Valid Metadata Values",
      "url": "https://www.postgresql.org/"
    },
    {
      "technologyTypeGUID": "ff7c8d09-9813-453e-9895-7a2b0a6b0be3",
      "qualifiedName": "Egeria:ValidMetadataValue:SoftwareServer:deployedImplementationType-(PostgreSQL Server)",
      "displayName": "PostgreSQL Server",
      "description": "A database server running the PostgreSQL software. PostgreSQL is an advanced open source relational database.PostgreSQL is an advanced open source relational database.",
      "category": "Valid Metadata Values",
      "url": "https://www.postgresql.org/"
    }
  ]
}
```
The next example shows the technology details returned by `getTechnologyTypeDetail` for "Apache Kafka Server".  The response is large, so the contents of the lists and the mermaid graph have been removed here, and are shown in the examples that follow.  Notice there are four sections to the detailed results:

* *catalogTemplates* lists the templates available for cataloguing Apache Kafka servers.
* *governanceActionProcesses* lists the [governance action processes](/concepts/governance-action-process) that work with this technology.
* *resourceList* lists the connectors, governance action types and other resources that support this technology.
* *mermaidGraph* is a [mermaid](/user-interfaces/mermaid/overview) graph of the technology type and everything linked to it.

The *url* is the link to the documentation for the technology.  It is stored in the *url* attribute of the technology type element, rather than in a linked external reference, and so the technology types supplied with Egeria have no *externalReferences* section in their detailed results.  This section only appears for a technology type that your organization has linked to its own external references.

```json
{
  "class": "TechnologyTypeReportResponse",
  "relatedHTTPCode": 200,
  "element": {
    "technologyTypeGUID": "47ab900d-7507-4a52-8b1e-f1692dcb97e0",
    "qualifiedName": "Egeria:ValidMetadataValue:SoftwareServer:deployedImplementationType-(Apache Kafka Server)",
    "displayName": "Apache Kafka Server",
    "description": "A software server supporting an event broker that enables high-speed, reliable topic-based event exchange.",
    "category": "Valid Metadata Values",
    "url": "https://kafka.apache.org/",
    "catalogTemplates": [],
    "governanceActionProcesses": [],
    "resourceList": [],
    "mermaidGraph": "..."
  }
}
```
This is an example of a template description from *catalogTemplates*.  Notice the specification identifies the placeholder variables used in the template.  The `relatedElement` is the template itself.  In this example, and the ones that follow, the `elementHeader` has been reduced to its unique identifier and type name, and the `specificationMermaidGraph` has been removed.
```json
{
  "displayName": "Apache Kafka Server template",
  "description": "Create a Apache Kafka Server SoftwareServer with an associated SoftwareCapability and Connection.",
  "specification": {
    "placeholderProperty": [
      {
        "class": "PlaceholderProperty",
        "specificationPropertyType": "PLACEHOLDER_PROPERTY",
        "name": "description",
        "description": "The description of the element to help a consumer understand its content and purpose.",
        "dataType": "string",
        "example": "This file contains a week's worth of patient data for the Teddy Bear Drop Foot clinical trial.",
        "required": false
      },
      {
        "class": "PlaceholderProperty",
        "specificationPropertyType": "PLACEHOLDER_PROPERTY",
        "name": "versionIdentifier",
        "description": "The string version identifier for the element.  This is typically of the form Vx.y.z where x is the major version number, y is the minor version number, and z is an option patch identifier.",
        "dataType": "string",
        "example": "6.4-SNAPSHOT",
        "required": false
      },
      {
        "class": "PlaceholderProperty",
        "specificationPropertyType": "PLACEHOLDER_PROPERTY",
        "name": "resourceName",
        "description": "The technical identifier for the element.  It is often an identifier from the owning technology platform.",
        "dataType": "string",
        "example": "my_asset",
        "required": false
      },
      {
        "class": "PlaceholderProperty",
        "specificationPropertyType": "PLACEHOLDER_PROPERTY",
        "name": "hostIdentifier",
        "description": "The host IP address or domain name.",
        "dataType": "string",
        "example": "coconet.com",
        "required": false
      },
      {
        "class": "PlaceholderProperty",
        "specificationPropertyType": "PLACEHOLDER_PROPERTY",
        "name": "serverName",
        "description": "The name of the server being catalogued.",
        "dataType": "string",
        "example": "myServer",
        "required": false
      },
      {
        "class": "PlaceholderProperty",
        "specificationPropertyType": "PLACEHOLDER_PROPERTY",
        "name": "portNumber",
        "description": "The number of the port to use to connect to a service.",
        "dataType": "string",
        "example": "1234",
        "required": false
      }
    ]
  },
  "specificationMermaidGraph": "...",
  "relatedElement": {
    "elementHeader": {
      "class": "ElementHeader",
      "guid": "5e1ff810-5418-43f7-b7c4-e6e062f9aff7",
      "type": {
        "typeName": "SoftwareServer"
      }
    },
    "properties": {
      "class": "SoftwareServerProperties",
      "typeName": "SoftwareServer",
      "qualifiedName": "Apache Kafka Server::~{serverName}~",
      "identifier": "~{serverName}~",
      "displayName": "~{serverName}~",
      "description": "~{description}~",
      "versionIdentifier": "~{versionIdentifier}~",
      "resourceName": "~{resourceName}~",
      "deployedImplementationType": "Apache Kafka Server",
      "deploymentStatus": "ACTIVE"
    }
  },
  "versionIdentifier": "6.4-SNAPSHOT",
  "templateGUID": "5e1ff810-5418-43f7-b7c4-e6e062f9aff7"
}
```
This is an example of an entry in *governanceActionProcesses*.  It is the process that deletes the asset for an Apache Kafka server.  The `resourceUse` describes what the process is used for.
```json
{
  "displayName": "Catalog Resource",
  "description": "Delete the asset for Apache Kafka Server using the same template properties that were used to create it.  This will delete all of the metadata anchored to the asset and relationships to other entities such as the catalog target relationships.",
  "additionalProperties": {
    "templateGUID": "5e1ff810-5418-43f7-b7c4-e6e062f9aff7"
  },
  "relatedElement": {
    "elementHeader": {
      "class": "ElementHeader",
      "guid": "a1cc2e94-667a-4b3c-9468-70b027532d34",
      "type": {
        "typeName": "DeletingActionProcess"
      }
    },
    "properties": {
      "class": "DeletingActionProcessProperties",
      "typeName": "DeletingActionProcess",
      "qualifiedName": "ApacheKafkaServer:DeleteAssetWithTemplateGovernanceActionProcess",
      "displayName": "ApacheKafkaServer:DeleteAsset",
      "url": "https://egeria-project.org/egeria-solutions/leveraging-apache-kafka/overview/",
      "summary": "Delete the asset for Apache Kafka Server using the same template properties that were used to create it.  This will delete all of the metadata anchored to the asset and relationships to other entities such as the catalog target relationships.",
      "domainIdentifier": 0
    }
  },
  "resourceUse": "Catalog Resource"
}
```
This is an example of an entry in the *resourceList*.  It is for a [governance action type](/concepts/governance-action-type) that invokes a [survey action service](/concepts/survey-action-service) that retrieves the topics from the Apache Kafka server and publishes them to a survey report.  Its specification describes the request parameters and action targets it supports, and the guards, action targets and annotations it produces.

```json
{
  "displayName": "Survey Resource",
  "description": "Discovers the topics supported by the Apache Kafka Server.",
  "specification": {
    "producedAnnotationType": [
      {
        "class": "ProducedAnnotationType",
        "specificationPropertyType": "PRODUCED_ANNOTATION_TYPE",
        "name": "Apache Kafka Topic List",
        "description": "List of topics known to the Apache Kafka server.",
        "otherPropertyValues": {
          "typeName": "ResourceProfileAnnotation"
        },
        "analysisStepName": "Profiling Associated Resources",
        "openMetadataTypeName": "ResourceProfileAnnotation",
        "explanation": "Topics provide the mechanism to organize events.  They may be explicitly configured, or created dynamically."
      },
      {
        "class": "ProducedAnnotationType",
        "specificationPropertyType": "PRODUCED_ANNOTATION_TYPE",
        "name": "Apache Kafka Topic Inventory",
        "description": "Log file of topics known to the Apache Kafka server.",
        "otherPropertyValues": {
          "typeName": "ResourceProfileLogAnnotation"
        },
        "analysisStepName": "Produce Inventory",
        "openMetadataTypeName": "ResourceProfileLogAnnotation",
        "explanation": "Topics provide the mechanism to organize events.  They may be explicitly configured, or created dynamically."
      }
    ],
    "supportedRequestParameter": [
      {
        "class": "SupportedRequestParameter",
        "specificationPropertyType": "SUPPORTED_REQUEST_PARAMETER",
        "name": "finalAnalysisStep",
        "description": "The name of the last analysis step that the survey action service is to run.  The survey stops once this step is complete.  If the survey never reaches the named step, it runs to completion.  It overrides the configuration property of the same name.",
        "otherPropertyValues": {
          "validValues": "Check Asset,Profiling Associated Resources,Produce Inventory"
        },
        "dataType": "string",
        "example": "Check Asset",
        "required": false
      }
    ],
    "producedGuard": [
      {
        "class": "ProducedGuard",
        "specificationPropertyType": "PRODUCED_GUARD",
        "name": "survey-completed",
        "description": "The survey completed successfully.  The survey report is attached to the asset.",
        "otherPropertyValues": {
          "completionStatusDescription": "The governance action service for the governance action has successfully completed processing."
        },
        "completionStatus": "ACTIONED"
      },
      {
        "class": "ProducedGuard",
        "specificationPropertyType": "PRODUCED_GUARD",
        "name": "survey-invalid",
        "description": "The survey did not run because the supplied information (such as the asset) is invalid for this type of survey.",
        "otherPropertyValues": {
          "completionStatusDescription": "The governance action service has not performed the requested action because it is not appropriate (for example, a false positive)."
        },
        "completionStatus": "INVALID"
      },
      {
        "class": "ProducedGuard",
        "specificationPropertyType": "PRODUCED_GUARD",
        "name": "survey-failed",
        "description": "An unexpected error occurred during the survey process.  The survey report is incomplete.",
        "otherPropertyValues": {
          "completionStatusDescription": "The governance action service failed to execute the requested action."
        },
        "completionStatus": "FAILED"
      }
    ],
    "supportedAnalysisStep": [
      {
        "class": "SupportedAnalysisStep",
        "specificationPropertyType": "SUPPORTED_ANALYSIS_STEP",
        "name": "Profiling Associated Resources",
        "description": "The survey action service is profiling other resources associated with the surveyed resource."
      },
      {
        "class": "SupportedAnalysisStep",
        "specificationPropertyType": "SUPPORTED_ANALYSIS_STEP",
        "name": "Produce Inventory",
        "description": "The survey action service is writing an inventory of the contents of the surveyed resource."
      },
      {
        "class": "SupportedAnalysisStep",
        "specificationPropertyType": "SUPPORTED_ANALYSIS_STEP",
        "name": "Check Asset",
        "description": "The survey action service is checking that the asset is of the correct type and the connection defines the correct type of connector."
      }
    ],
    "producedActionTarget": [
      {
        "class": "ProducedActionTarget",
        "specificationPropertyType": "PRODUCED_ACTION_TARGET",
        "name": "stewardAction",
        "description": "To Do element created for the steward.",
        "openMetadataTypeName": "ToDo",
        "required": false
      },
      {
        "class": "ProducedActionTarget",
        "specificationPropertyType": "PRODUCED_ACTION_TARGET",
        "name": "surveyReport",
        "description": "The survey report created by a survey action service.",
        "openMetadataTypeName": "SurveyReport",
        "required": false
      },
      {
        "class": "ProducedActionTarget",
        "specificationPropertyType": "PRODUCED_ACTION_TARGET",
        "name": "steward",
        "description": "The person, or team who is responsible for setting up the governance metadata associated with .",
        "openMetadataTypeName": "Actor",
        "required": false
      }
    ],
    "supportedActionTarget": [
      {
        "class": "SupportedActionTarget",
        "specificationPropertyType": "SUPPORTED_ACTION_TARGET",
        "name": "*",
        "description": "Any Software Server entity that represents an Apache Kafka server linked to the connection for the Apache Kafka Admin connector.",
        "openMetadataTypeName": "SoftwareServer",
        "deployedImplementationType": "Apache Kafka Server",
        "required": false
      }
    ]
  },
  "specificationMermaidGraph": "...",
  "relatedElement": {
    "elementHeader": {
      "class": "ElementHeader",
      "guid": "71c73133-6817-42a1-9cc6-b610cee34a8b",
      "type": {
        "typeName": "GovernanceActionType"
      }
    },
    "properties": {
      "class": "GovernanceActionTypeProperties",
      "typeName": "GovernanceActionType",
      "qualifiedName": "ApacheKafkaSurvey::survey-kafka-server",
      "displayName": "survey-kafka-server (ApacheKafkaSurvey)",
      "description": "Discovers the topics supported by the Apache Kafka Server.",
      "domainIdentifier": 4,
      "waitTime": 0
    }
  },
  "resourceUse": "Survey Resource"
}
```

## Cancelling engine actions and governance action processes

The `cancelEngineAction` operation requests that an [engine action](/concepts/engine-action) is cancelled.  Its status is set to `CANCELLED` and any governance service running it is told to stop.

```
###
# @name cancelEngineAction
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/automated-curation/engine-actions/{{engineActionGUID}}/cancel
Authorization: Bearer {{token}}
```

An engine action that has already finished - that is, its status is `COMPLETED`, `INVALID`, `IGNORED`, `FAILED`, `CANCELLED` or `ABANDONED` - is left unchanged, so the record of how it finished is kept.  The request still succeeds, and an informational message, `OMAG-GENERIC-HANDLERS-0026`, is written to the audit log.  Any other engine action can be cancelled, including one that is `PAUSED` or `WAITING`.

The `cancelGovernanceActionProcess` operation cancels a running [governance action process](/concepts/governance-action-process) instance.  The `processInstanceGUID` is the unique identifier returned by `initiateGovernanceActionProcess`.

```
###
# @name cancelGovernanceActionProcess
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/automated-curation/governance-action-process-instances/{{processInstanceGUID}}/cancel
Authorization: Bearer {{token}}
```

It cancels every engine action of the process instance that has not finished, in the same way as `cancelEngineAction`, and leaves the finished ones unchanged.  Because cancelled engine actions never record their completion, the process instance would otherwise never be marked as complete, so its `completionTime` is set to the time of the cancel - unless it is already set, in which case the process instance had already finished and its own completion time is kept.  The number of engine actions cancelled is reported in the audit log message `OMAG-GENERIC-HANDLERS-0031`.

## Further information

* [Integration Connector Concept](https://egeria-project.org/concepts/integration-connector/)
* [Governance Action Concept](https://egeria-project.org/concepts/governance-action/)
* [Integration Daemon Concept](https://egeria-project.org/concepts/integration-daemon/)

Sample REST API requests can be found in [Egeria-api-automated-curation.http](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/view-server-generic-services/automated-curation/Egeria-api-automated-curation.http).


--8<-- "snippets/abbr.md"
