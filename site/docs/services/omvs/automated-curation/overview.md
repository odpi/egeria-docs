---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# Automated Curation Open Metadata View Service (OMVS)

The Automated Curation OMVS provides services that can be used to set up and monitor the automation services from Egeria:

* Retrieving information about different technologies with their linked templates and resources.
* Adding catalog targets to [integration connectors](/concepts/integration-connector) running in an [Integration Daemon](/concepts/integration-daemon).
* Initiating governance action types, governance action processes and [engine actions](/concepts/engine-action).
* Monitoring the outcomes of engine actions.


## Retrieving details about supported technologies

Automated Curation OMAS provides methods to query the supported technology types.  The technology types provide the reference data to guide the curator.  They are extracted from the valid values for [*deployedImplementationType*](/concepts/deployed-implementation-type).

The `getTechnologyTypesForOpenMetadataType` operation retrieves the list of deployed implementation type metadata elements linked to a particular open metadata type.

```
@typeName=SoftwareServer

GET {{baseURL}}/servers/{{viewServer}}/api/open-metadata/automated-curation/open-metadata-types/{{typeName}}/technology-types?startFrom=0&pageSize=0
Authorization: Bearer {{token}}
Content-Type: application/json
```
The `findTechnologyTypes` operation Retrieve the list of deployed implementation type metadata elements that contain the search string.
```
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/automated-curation/technology-types/by-search-string?startFrom=0&pageSize=0&startsWith=false&endsWith=false&ignoreCase=true
Authorization: Bearer {{token}}
Content-Type: application/json

{
   "string" : "PostgreSQL"
}
```
One the desired technology has been identified, the attached templates and resources can be retrieved using the `getTechnologyTypeDetail` operation.
```
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/automated-curation/technology-types/by-name
Authorization: Bearer {{token}}
Content-Type: application/json

{
  "string" : "PostgreSQL Server"
}

```
Below is the list of technology types for `PostgreSQL`.
```json
{
  "class": "TechnologyTypeSummaryListResponse",
  "relatedHTTPCode": 200,
  "elements": [
    {
      "technologyTypeGUID": "95b26833-b317-486d-8b4b-587db5b3649e",
      "qualifiedName": "Egeria:ValidMetadataValue:SoftwareServer:deployedImplementationType-(PostgreSQL Server)",
      "name": "PostgreSQL Server",
      "description": "A database server running the PostgreSQL software.",
      "category": "SoftwareServer:deployedImplementationType"
    },
    {
      "technologyTypeGUID": "7cb5872f-91c7-4def-bd71-25cbbdab06f9",
      "qualifiedName": "Egeria:ValidMetadataValue:DeployedDatabaseSchema:deployedImplementationType-(PostgreSQL Relational Database Schema)",
      "name": "PostgreSQL Relational Database Schema",
      "description": "A database schema hosted on a PostgreSQL relational database server capable of being called through a JDBC Driver.",
      "category": "DeployedDatabaseSchema:deployedImplementationType"
    },
    {
      "technologyTypeGUID": "079fd2f5-5fad-4df7-90b9-755d66c71901",
      "qualifiedName": "Egeria:ValidMetadataValue:DatabaseManager:deployedImplementationType-(PostgreSQL database manager (RDBMS))",
      "name": "PostgreSQL database manager (RDBMS)",
      "description": "The PostgreSQL capability that manages collections of data called relational databases which in turn are organized into a tabular format and accessed via the Structured Query Language (SQL).",
      "category": "DatabaseManager:deployedImplementationType"
    },
    {
      "technologyTypeGUID": "a0368801-b914-467a-bbcf-ef14af20e280",
      "qualifiedName": "Egeria:ValidMetadataValue:TableDataSet:deployedImplementationType-(PostgreSQL Relational Database Table)",
      "name": "PostgreSQL Relational Database Table",
      "description": "A database table hosted on a PostgreSQL relational database server capable of being called through a JDBC Driver.",
      "category": "TableDataSet:deployedImplementationType"
    },
    {
      "technologyTypeGUID": "cae3a106-3756-424c-a8fa-74c5acd2b7f1",
      "qualifiedName": "Egeria:ValidMetadataValue:RelationalDatabase:deployedImplementationType-(PostgreSQL Relational Database)",
      "name": "PostgreSQL Relational Database",
      "description": "A database hosted on a PostgreSQL server.",
      "category": "RelationalDatabase:deployedImplementationType"
    }
  ]
}
```
The next example shows the technology details for "Apache Kafka Server".  Notice there are three sections to the detailed results:

* *catalogTemplates* list the templates available for cataloguing Apache Kafka servers.
* *resourceList* lists the connectors that support this technology.
* *externalReferences* links to additional documentation.

```json
{
  "class": "TechnologyTypeReportResponse",
  "relatedHTTPCode": 200,
  "element": {
    "technologyTypeGUID": "9676530f-dfe7-4657-adb9-0123b2d31f55",
    "qualifiedName": "Egeria:ValidMetadataValue:SoftwareServer:deployedImplementationType-(Apache Kafka Server)",
    "name": "Apache Kafka Server",
    "description": "A software server supporting an event broker that enables high speed, reliable topic-based event exchange.",
    "category": "SoftwareServer:deployedImplementationType",
    "catalogTemplates": [],
    "resourceList": [],
    "externalReferences": []
  }
}
```
This is an example of a template description.  Notice the specification identifies the placeholder variables used in the template.  The `relatedElement` is the header of the template.
```json
      {
        "specification": {
          "placeholderProperty": [
            {
              "dataType": "string",
              "description": "The name of the Apache Kafka server being catalogued.",
              "placeholderName": "serverName",
              "required": "true",
              "example": "myKafkaServer"
            },
            {
              "dataType": "string",
              "description": "The host IP address or domain name of the Apache Kafka server.",
              "placeholderName": "hostIdentifier",
              "required": "true",
              "example": "coconet.com"
            },
            {
              "dataType": "string",
              "description": "The number of the port to use to connect to the Apache Kafka server.",
              "placeholderName": "portNumber",
              "required": "true",
              "example": "1234"
            }
          ]
        },
        "relatedElement": {
          "class": "ElementStub",
          "headerVersion": 0,
          "status": "ACTIVE",
          "type": {
            "typeId": "aa7c7884-32ce-4991-9c41-9778f1fec6aa",
            "typeName": "SoftwareServer",
            "superTypeNames": [
              "ITInfrastructure",
              "Infrastructure",
              "Asset",
              "Referenceable",
              "OpenMetadataRoot"
            ],
            "typeVersion": 2,
            "typeDescription": "Software services to support a runtime environment for applications and data stores."
          },
          "origin": {
            "sourceServer": "active-metadata-store",
            "originCategory": "CONTENT_PACK",
            "homeMetadataCollectionId": "09450b83-20ff-4a8b-a8fb-f9b527bbcba6",
            "homeMetadataCollectionName": "OpenConnectorsArchive",
            "license": "Apache-2.0"
          },
          "versions": {
            "createdBy": "Egeria Project",
            "createTime": "2022-04-11T14:22:58.059+00:00",
            "version": 1
          },
          "guid": "5e1ff810-5418-43f7-b7c4-e6e062f9aff7",
          "classifications": [
            {
              "class": "ElementClassification",
              "headerVersion": 0,
              "status": "ACTIVE",
              "type": {
                "typeId": "aa44f302-2e43-4669-a1e7-edaae414fc6e",
                "typeName": "Anchors",
                "typeVersion": 3,
                "typeDescription": "Identifies the anchor entity for an element that is part of a large composite object such as an asset."
              },
              "origin": {
                "sourceServer": "active-metadata-store",
                "originCategory": "CONTENT_PACK",
                "homeMetadataCollectionId": "09450b83-20ff-4a8b-a8fb-f9b527bbcba6",
                "homeMetadataCollectionName": "OpenConnectorsArchive"
              },
              "versions": {
                "createdBy": "Egeria Project",
                "createTime": "2022-04-11T14:22:58.059+00:00",
                "version": 1
              },
              "classificationOrigin": "ASSIGNED",
              "classificationName": "Anchors",
              "classificationProperties": {
                "anchorTypeName": "SoftwareServer",
                "anchorGUID": "5e1ff810-5418-43f7-b7c4-e6e062f9aff7"
              }
            },
            {
              "class": "ElementClassification",
              "headerVersion": 0,
              "status": "ACTIVE",
              "type": {
                "typeId": "25fad4a2-c2d6-440d-a5b1-e537881f84ee",
                "typeName": "Template",
                "typeVersion": 2,
                "typeDescription": "Marks the referenceable as a template for creating new objects."
              },
              "origin": {
                "sourceServer": "active-metadata-store",
                "originCategory": "CONTENT_PACK",
                "homeMetadataCollectionId": "09450b83-20ff-4a8b-a8fb-f9b527bbcba6",
                "homeMetadataCollectionName": "OpenConnectorsArchive"
              },
              "versions": {
                "createdBy": "Egeria Project",
                "createTime": "2022-04-11T14:22:58.059+00:00",
                "version": 1
              },
              "classificationOrigin": "ASSIGNED",
              "classificationName": "Template",
              "classificationProperties": {
                "name": "Apache Kafka Server template",
                "versionIdentifier": "V1.0"
              }
            }
          ],
          "uniqueName": "Apache Kafka Server:{{serverName}}"
        },
        "name": "Apache Kafka Server template"
      }
```
This is an example of an entry in the `resourceList`.  It is for a [governance action type](/concepts/governance-action-type) that invokes a [survey action service](/concepts/survey-action-service) that retrieves the topics from the Apache Kafka server and publishes them to a survey report.

```json
{
        "specification": {
          "producedAnnotationType": [
            {
              "placeholderName": "Apache Kafka Topic List"
            }
          ],
          "producedGuard": [
            {
              "placeholderName": "survey-failed"
            },
            {
              "placeholderName": "survey-completed"
            }
          ],
          "supportedAnalysisStep": [
            {
              "description": "The survey action service is profiling other resources associated with the surveyed resource.",
              "placeholderName": "Profiling Associated Resources"
            },
            {
              "description": "The survey action service is checking that the asset is of the correct type and the connection defines the correct type of connector.",
              "placeholderName": "Check Asset"
            }
          ],
          "supportedActionTarget": [
            {
              "dataType": "SoftwareServer",
              "description": "Any Software Server entity that represents an Apache Kafka server linked to the connection for the Apache Kafka Admin connector.",
              "placeholderName": "*",
              "required": "false",
              "deployedImplementationType": "Apache Kafka Server"
            }
          ],
          "producedActionTarget": [
            {
              "placeholderName": "surveyReport"
            }
          ]
        },
        "relatedElement": {
          "class": "ElementStub",
          "headerVersion": 0,
          "status": "ACTIVE",
          "type": {
            "typeId": "92e20083-0393-40c0-a95b-090724a91ddc",
            "typeName": "GovernanceActionType",
            "superTypeNames": [
              "Referenceable",
              "OpenMetadataRoot"
            ],
            "typeVersion": 2,
            "typeDescription": "A description of a call to a governance engine that acts as a template when creating the appropriate engine action instance."
          },
          "origin": {
            "sourceServer": "active-metadata-store",
            "originCategory": "CONTENT_PACK",
            "homeMetadataCollectionId": "09450b83-20ff-4a8b-a8fb-f9b527bbcba6",
            "homeMetadataCollectionName": "OpenConnectorsArchive",
            "license": "Apache-2.0"
          },
          "versions": {
            "createdBy": "Egeria Project",
            "createTime": "2022-04-11T14:22:58.059+00:00",
            "version": 1
          },
          "guid": "e2575dc7-3309-4b15-95ee-4766d6808f4e",
          "classifications": [
            {
              "class": "ElementClassification",
              "headerVersion": 0,
              "status": "ACTIVE",
              "type": {
                "typeId": "aa44f302-2e43-4669-a1e7-edaae414fc6e",
                "typeName": "Anchors",
                "typeVersion": 3,
                "typeDescription": "Identifies the anchor entity for an element that is part of a large composite object such as an asset."
              },
              "origin": {
                "sourceServer": "active-metadata-store",
                "originCategory": "CONTENT_PACK",
                "homeMetadataCollectionId": "09450b83-20ff-4a8b-a8fb-f9b527bbcba6",
                "homeMetadataCollectionName": "OpenConnectorsArchive"
              },
              "versions": {
                "createdBy": "Egeria Project",
                "createTime": "2022-04-11T14:22:58.059+00:00",
                "version": 1
              },
              "classificationOrigin": "ASSIGNED",
              "classificationName": "Anchors",
              "classificationProperties": {
                "anchorTypeName": "SurveyActionEngine",
                "anchorGUID": "2adeb8f1-0f59-4970-b6f2-6cc25d4d2402"
              }
            }
          ],
          "uniqueName": "Egeria:GovernanceActionType:2adeb8f1-0f59-4970-b6f2-6cc25d4d2402survey-kafka-server"
        },
        "resourceUse": "Survey Resource",
        "resourceUseDescription": "Discovers the topics supported by the Apache Kafka Server."
      }
```
Finally, this is an example of an external reference.
```json
 [
      {
        "elementHeader": {},
        "properties": {
          "class": "ExternalReferenceProperties",
          "qualifiedName": "Egeria:ValidMetadataValue:SoftwareServer:deployedImplementationType-(Apache Kafka Server)_wikiLink",
          "typeName": "ExternalReference",
          "extendedProperties": {
            "numberOfPages": 0
          },
          "displayName": "More information about deployedImplementationType: Apache Kafka Server",
          "uri": "https://kafka.apache.org/"
        }
      }
    ]
```
--8<-- "snippets/abbr.md"
