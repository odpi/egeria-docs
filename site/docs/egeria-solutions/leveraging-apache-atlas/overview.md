
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Leveraging your Apache Atlas estate

[Apache Atlas](https://atlas.apache.org) is a metadata catalog originally designed for the Hadoop ecosystem.  It offers integration services called Hooks and Bridges to capture the schemas and data sets of data platforms such as [Apache Hive](https://hive.apache.org/), [Apache HBase](https://hbase.apache.org/) and [Apache Hadoop Distributed File System (HDFS)](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HdfsUserGuide.html) along with the processes for creating and maintaining data sets on these platforms.  The metadata descriptions of these data sets and processes are linked together using lineage relationships, allowing an understanding of how data is flowing through a Hadoop deployment.  Apache Atlas also supports glossaries and a tagging system that can be used both in searches and to control access to data through Apache Ranger (using the TagSync integration).

In recent years, Apache Atlas has been embedded in popular data catalogs such as [Microsoft Purview](https://azure.microsoft.com/en-gb/products/purview/) and [Atlan](https://atlan.com/), increasing the interest in being able to integrate with this metadata catalog.

Egeria's *Apache Atlas connectors* give you oversight of an Apache Atlas server, and a genuine two-way exchange of metadata with it - not just a one-off import.  They can:

* **Survey** an Apache Atlas server to build a picture of the types it has defined and how many instances of each are in use, without touching the business data those instances describe.
* **Catalog** the server, and keep glossaries, data sets and lineage synchronized between Apache Atlas and the open metadata ecosystem on an ongoing basis - in either direction, or both, depending on how you configure it.
* Do both of these using **standard governance action processes**, so onboarding an Apache Atlas server follows the same repeatable pattern as any other technology Egeria supports.

See [Apache Atlas vs Egeria](apache-atlas-vs-egeria.md) for a deeper comparison of the two technologies if you are evaluating one against the other, or migrating between them.


## Apache Atlas Technology Type Name

Unlike some of the other technologies Egeria integrates with, an Apache Atlas deployment isn't broken down into a hierarchy of technology types - it is catalogued as a single server.  The technology type name (aka [deployed implementation type](/concepts/deployed-implementation-type)) added to Egeria's reference data for Apache Atlas is:

* *Apache Atlas Server* - A data catalog for the Hadoop ecosystem.

What's inside an Apache Atlas server - its types, entities, glossaries and lineage - is captured either as a snapshot in a survey report, or as an ongoing, correlated exchange of metadata, rather than as individually catalogued Egeria assets underneath the server.


## Connectors to Apache Atlas

The [Apache Atlas connectors](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/system-connectors/apache-atlas-connectors) provide a suite of functions to access, survey, catalog and govern Apache Atlas.

| Connector Name                          | Connector Type                                                      | Purpose                                                                                                                                                     |
|-------------------------------------------|-------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **[Apache Atlas REST Connector :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/system-connectors/apache-atlas-connectors/docs/apache-atlas-rest-connector.md){ target=gh }** | [Digital Resource Connector](/concepts/digital-resource-connector) | A dependency-free Java wrapper around Apache Atlas's REST API.  It is used by the survey and integration connectors below, and can also be used directly by other components. |
| **[Apache Atlas Survey Action Service :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/system-connectors/apache-atlas-connectors/docs/apache-atlas-survey-action-service.md){ target=gh }** | [Survey Action Service](/concepts/survey-action-service) | Surveys the types and entity instances defined in an Apache Atlas server and records the findings in a survey report. |
| **[Apache Atlas Integration Connector :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/system-connectors/apache-atlas-connectors/docs/apache-atlas-catalog-integration-connector.md){ target=gh }** | [Integration Connector](/concepts/integration-connector) | Keeps glossaries, data sets, lineage and classification reference data synchronized between Apache Atlas and the open metadata ecosystem on an ongoing basis. |

These connectors, their template and the associated reference data are delivered together in the [Apache Atlas Content Pack](/content-packs/apache-atlas-content-pack/overview).


## Surveying an Apache Atlas server

A survey is a good first step when you encounter an Apache Atlas server you don't already have documented in Egeria.  The **Apache Atlas Survey Action Service** builds a [survey report](/concepts/survey-report) describing the types Apache Atlas has defined and how many instances of each exist, in three analysis steps that each build on the one before:

1. **Measure Resource** - retrieves overall metrics from the Apache Atlas server, such as the total number of entities, types and classifications in use.  This step needs only two REST API calls, so it has minimal impact on the Apache Atlas server.
2. **Schema Extraction** - retrieves Apache Atlas's type definitions (entity types, relationship types, classification types and business metadata types) and represents them as a graph schema, attached to the asset that represents the Apache Atlas server.
3. **Profile Data** - walks every entity in the server and counts, for each type, how many instances of each classification, relationship, label and business metadata property are attached to it.

Each step costs more than the last, so you can stop after any of them by setting the `finalAnalysisStep` property - as a configuration property on the survey's connection, or as a request parameter when it is run.  The default is `Profile Data`, the most complete (and most expensive) option.

### How the survey avoids touching your business data

The survey only calls Apache Atlas's own metadata REST APIs - `TypesREST` for type definitions and `DiscoveryREST`/`EntityREST` for instance counts.  It never reads the business data referenced by an Apache Atlas `DataSet` entity (the contents of the underlying Hive table or HDFS file, for example) - only Apache Atlas's own record of how many such entities exist and how they are classified and related.

### The annotations produced

| Annotation Type                                              | Analysis Step   | What it captures                                                                                     |
|-----------------------------------------------------------------|------------------|-------------------------------------------------------------------------------------------------------|
| **Apache Atlas Server Metrics**                               | Measure Resource | Entity, classification and type counts for the whole server - see the table below.                    |
| **Apache Atlas Type Analysis**                                | Schema Extraction | Identifies the graph schema created from Apache Atlas's type definitions (see below).                 |
| **Apache Atlas Attached Classification Types**                | Profile Data     | Per entity type: count of classification types attached to it.                                        |
| **Apache Atlas End 1 / End 2 Attached Relationship Types**    | Profile Data     | Per entity type: count of relationship types attached to it at each end.                               |
| **Apache Atlas Attached Labels**                               | Profile Data     | Per entity type: count of the different informal labels attached to it.                                |
| **Apache Atlas Attached Business Metadata Types**              | Profile Data     | Per entity type: count of the different business metadata property types attached to it.               |
| **Apache Atlas Attached Entity Types By Classification**       | Profile Data     | Per classification type: count of entities carrying it, broken down by entity type.                    |
| **Apache Atlas Attached Entity Types By Business Metadata**    | Profile Data     | Per business metadata type: count of entities carrying it, broken down by entity type.                 |
| **Apache Atlas Attached End 1 / End 2 Entity Types**           | Profile Data     | Per relationship type: count of entity types attached at each end.                                     |
| **Apache Atlas Attached Entity Type Pairs**                    | Profile Data     | Per relationship type: count of each pairing of entity types found at the two ends.                    |

The *Apache Atlas Server Metrics* annotation captures whole-server counts such as `entityInstanceCount`, `entityInstanceCount:*typeName*` (per type), `entityWithSubtypesInstanceCount:*typeName*`, `classificationCount`, `typeCount` and `typeUnusedCount`.  The nine *Profile Data* annotation types listed above are each attached to the graph schema attribute for the relevant type, rather than to the survey report directly.

??? example "Example annotations from surveying an Apache Atlas server"
    ```json
    {
      "class": "ResourceMeasureAnnotation",
      "annotationType": "Apache Atlas Server Metrics",
      "summary": "Metrics maintained by Apache Atlas.",
      "explanation": "These metrics are extracted through the Apache Atlas REST API.",
      "analysisStep": "Measure Resource",
      "resourceProperties": {
        "entityInstanceCount": "48213",
        "entityInstanceCount:hive_table": "1204",
        "classificationCount": "3661",
        "typeCount": "187",
        "typeUnusedCount": "22"
      }
    }
    ```
    ```json
    {
      "class": "ResourceProfileAnnotation",
      "annotationType": "Apache Atlas Attached Classification Types",
      "summary": "Count of classification types attached to this type of entity.",
      "explanation": "Classifications are used to group entities with similar characteristics together.",
      "analysisStep": "Profile Data",
      "valueCount": {
        "PII": "312",
        "Confidential": "58",
        "Approved": "890"
      },
      "additionalProperties": {
        "instanceCount": "1204"
      }
    }
    ```

### Apache Atlas types as a graph schema

The *Schema Extraction* step turns Apache Atlas's type system into a schema that describes the shape of the metadata found in the server, rather than the shape of any one data set:

* A *GraphVertex* schema attribute is created for each Apache Atlas entity type, business metadata type and classification type.
* A *GraphEdge* schema attribute is created for each Apache Atlas relationship type, and for each permitted use of a classification type by an entity type - linked to the two *GraphVertex* attributes it connects via *GraphEdgeLink* relationships.

All the graph vertices are linked to a single *[GraphSchemaType](/types/5/0533-Graph-Schemas)* attached to the Apache Atlas server's asset, so the whole type system can be browsed as one connected graph.

<!-- SCREENSHOT PLACEHOLDER: apache-atlas-survey-report.png - the survey report and its annotations, as shown against the Apache Atlas server asset in the Egeria UI. -->
*(Screenshot to follow: the survey report and its annotations, as displayed against the surveyed Apache Atlas server asset in the Egeria UI.)*


## Cataloguing and keeping metadata in sync

Cataloguing an Apache Atlas server sets up the **Apache Atlas Integration Connector** (internally named `ApacheAtlasExchange`), which - unlike a typical one-way cataloguing connector - maintains an *ongoing, two-way* exchange of metadata.  What flows, and in which direction, depends on the kind of metadata:

* **Glossaries, glossary categories and active glossary terms** can flow in either direction, or both, depending on configuration.  Elements that originate in the open metadata ecosystem are published into Apache Atlas (and any local changes made to them there are overwritten on the next refresh); elements that originate in Apache Atlas are copied into the open metadata ecosystem as read-only.
* **Data sets** (Apache Atlas entities of type `DataSet`) and **lineage relationships** (`dataset_process_inputs` and `dataset_process_outputs`) flow only from Apache Atlas into the open metadata ecosystem - Apache Atlas's entity and relationship metadata has no standard place to record a matching identifier back in the other direction, so this exchange can only be one-way.
* **Classification reference data** - a catalogue of the classification (tag) types in use in Apache Atlas - is maintained so it can be used both to create new classification definitions in Apache Atlas and to record which classifications from the open metadata ecosystem should also be visible to Apache Atlas users.

### Ownership and correlation

Every synchronized instance has exactly one owner - whichever system it was originally created in:

* Instances created in the open metadata ecosystem are owned by it; any changes or deletions made to their copy in Apache Atlas are reversed on the next refresh.
* Instances created in Apache Atlas are owned by Apache Atlas; when copied into the open metadata ecosystem, their [provenance](/features/metadata-provenance/overview) is set to show Apache Atlas as their origin, which makes them effectively read-only there.

The two copies of an instance are correlated using an [external identifier](/features/external-identifiers/overview) recording the counterpart's unique identifier - on the Apache Atlas side, this is stored as `egeriaGUID` (plus an `egeriaOwned` flag) in the instance's `additionalAttributes`.

### Controlling the exchange

The connector's connection accepts:

| Property | Purpose |
|---|---|
| `permittedSynchronization` | Controls the direction of flow: `FROM_THIRD_PARTY` (Apache Atlas → Egeria only), `TO_THIRD_PARTY` (Egeria → Apache Atlas only), or `BOTH_DIRECTIONS`. |
| `egeriaGlossaryQualifiedName` | Restricts publishing to a single named Egeria glossary.  If unset, every glossary in the open metadata ecosystem is copied to Apache Atlas. |
| `atlasGlossaryName` | Restricts synchronization to a single named Apache Atlas glossary.  If unset, every glossary in Apache Atlas is copied into the open metadata ecosystem. |
| `metadataSourceQualifiedName` | A unique name for this Apache Atlas server instance, used to identify the origin of the metadata it contributes - important if you are cataloguing more than one Apache Atlas server. |
| `refreshTimeInterval` | Minutes between refresh scans - for example, `1440` for once a day. |

<!-- SCREENSHOT PLACEHOLDER: apache-atlas-catalogued-server.png - the Apache Atlas server asset and synchronized glossary/data set elements shown in the Egeria UI. -->
*(Screenshot to follow: the catalogued Apache Atlas server, its synchronized glossaries and data sets, shown in the Egeria UI.)*


## Running this through the Automated Curation API

All of the capabilities above are packaged as ready-to-run **governance action processes**, delivered by the [Apache Atlas Content Pack](/content-packs/apache-atlas-content-pack/overview).  You initiate them through the [Automated Curation](/services/omvs/automated-curation/overview) API of a view server - either directly over REST, or through **pyegeria**.

| Governance Action Process                                          | What it does                                                                                                                 |
|--------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| `ApacheAtlasServer:CreateAndSurveyGovernanceActionProcess`         | Creates the *Apache Atlas Server* asset and runs the Apache Atlas Survey Action Service against it, printing out the resulting report. |
| `ApacheAtlasServer::CreateAsCatalogTargetGovernanceActionProcess`  | Creates the *Apache Atlas Server* asset and configures the Apache Atlas Integration Connector to start exchanging metadata with it. |
| `ApacheAtlasServer:DeleteAssetWithTemplateGovernanceActionProcess` | Deletes the server asset (and everything anchored to it) using the same template properties used to create it.               |

Below are the flows for the two most commonly used processes, showing the request parameters each one accepts:

=== "CreateAndSurvey"

    --8<-- "snippets/governance-action-processes/apacheatlasserver:createandsurvey-mermaid-graph.md"

=== "CreateAsCatalogTarget"

    --8<-- "snippets/governance-action-processes/apacheatlasserver::createascatalogtarget-mermaid-graph.md"


### Using the REST API

The REST calls below assume you have a running view server (`view-server` in these examples) and have already obtained a bearer token.

```http
@baseURL=https://localhost:9443
@viewServer=view-server

### Get a bearer token
# @name Token
POST {{baseURL}}/api/token
Content-Type: application/json

{
  "userId" : "peterprofile",
  "password" : "secret"
}

> {% client.global.set("token", response.body); %}

### Survey an Apache Atlas server
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/automated-curation/governance-action-processes/initiate
Authorization: Bearer {{token}}
Content-Type: application/json

{
  "processQualifiedName": "ApacheAtlasServer:CreateAndSurveyGovernanceActionProcess",
  "requestParameters" : {
    "serverName" : "LocalApacheAtlas1",
    "hostURL" : "http://localhost",
    "portNumber" : "21000",
    "secretsStorePathName" : "secrets/integration.omsecrets",
    "secretsCollectionName" : "Apache Atlas Server Secret",
    "versionIdentifier" : "1.0",
    "description" : "Apache Atlas metadata catalog."
  }
}

> {% client.global.set("surveyInstanceGUID", response.body.guid); %}

### Catalog the same Apache Atlas server and start the metadata exchange
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/automated-curation/governance-action-processes/initiate
Authorization: Bearer {{token}}
Content-Type: application/json

{
  "processQualifiedName": "ApacheAtlasServer::CreateAsCatalogTargetGovernanceActionProcess",
  "requestParameters" : {
    "serverName" : "LocalApacheAtlas1",
    "hostURL" : "http://localhost",
    "portNumber" : "21000",
    "secretsStorePathName" : "secrets/integration.omsecrets",
    "secretsCollectionName" : "Apache Atlas Server Secret",
    "versionIdentifier" : "1.0",
    "description" : "Apache Atlas metadata catalog."
  }
}

> {% client.global.set("catalogInstanceGUID", response.body.guid); %}

### Check progress of an engine action started by either process above
GET {{baseURL}}/servers/{{viewServer}}/api/open-metadata/automated-curation/engine-actions/active?startFrom=0&pageSize=5
Authorization: Bearer {{token}}

### Retrieve the flow definition and progress of a specific process instance
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/governance-officer/governance-action-processes/{{catalogInstanceGUID}}/graph
Authorization: Bearer {{token}}
```

Once the server is catalogued, the direction and scope of the ongoing exchange is controlled by setting `permittedSynchronization`, `egeriaGlossaryQualifiedName` and/or `atlasGlossaryName` as configuration properties on the resulting `ApacheAtlasExchange` connector - either directly in the integration daemon's configuration document, or via an [integration group](/concepts/integration-group) for dynamic control.

### Using pyegeria

This follows exactly the same pattern as the [PostgreSQL pyegeria walkthrough](/egeria-solutions/leveraging-postgres/overview#using-pyegeria) - just with the Apache Atlas process names and request parameters substituted in:

```python
from pyegeria import EgeriaTech, load_mermaid, render_mermaid

view_server = "qs-view-server"
url         = "https://host.docker.internal:9443"
user_id     = "erinoverview"
user_pwd    = "secret"

egeria_tech = EgeriaTech(view_server, url, user_id, user_pwd)
token = egeria_tech.create_egeria_bearer_token()

# See what Apache Atlas governance action processes are available
elements = egeria_tech.find_elements_by_property_value(
    property_value="ApacheAtlas",
    property_names=["qualifiedName"],
    metadata_element_type_name="GovernanceActionProcess",
)
for element in elements:
    properties = element.get("properties")
    print("* " + properties.get("qualifiedName") + " - " + properties.get("description"))

# Survey an Apache Atlas server
request_parameters = {
    "serverName" : "LocalApacheAtlas1",
    "hostURL" : "http://localhost",
    "portNumber" : "21000",
    "secretsStorePathName" : "secrets/integration.omsecrets",
    "secretsCollectionName" : "Apache Atlas Server Secret",
    "versionIdentifier" : "1.0",
    "description" : "Apache Atlas metadata catalog.",
}

survey_instance_guid = egeria_tech.initiate_gov_action_process(
    "ApacheAtlasServer:CreateAndSurveyGovernanceActionProcess",
    None, None, None, request_parameters, None, None,
)

# Watch the process run as a mermaid diagram
load_mermaid()
process_graph = egeria_tech.get_governance_process_graph(survey_instance_guid)
render_mermaid(process_graph.get("governanceActionProcessMermaidGraph"))

# Once you're happy with what the survey found, catalog the server too
catalog_instance_guid = egeria_tech.initiate_gov_action_process(
    "ApacheAtlasServer::CreateAsCatalogTargetGovernanceActionProcess",
    None, None, None, request_parameters, None, None,
)
```

A starter notebook for this walkthrough is being built up at [`survey-and-catalog-atlas.ipynb` :material-github:](https://github.com/odpi/egeria-workspaces/blob/main/workbooks/cataloguing-and-surveys/apache-atlas/survey-and-catalog-atlas.ipynb){ target=gh } in `egeria-workspaces`, alongside the equivalent PostgreSQL and Microsoft SQL Server notebooks.

To follow progress of the integration connector once cataloguing has started, use:

```python
from commands.ops.monitor_daemon_status import display_integration_daemon_status

display_integration_daemon_status(
    ["ApacheAtlasServerIntegrationConnector"],
    integ_server="qs-integration-daemon",
    paging=True,
    width=150,
)
```

<!-- SCREENSHOT PLACEHOLDER: apache-atlas-integration-daemon-status.png - display_integration_daemon_status() output showing the Apache Atlas Integration Connector running. -->
*(Screenshot to follow: `display_integration_daemon_status()` output for the Apache Atlas connector.)*


## Related information

* [Apache Atlas vs Egeria](apache-atlas-vs-egeria.md) - a deeper comparison of the two technologies.
* [Apache Atlas Content Pack](/content-packs/apache-atlas-content-pack/overview) - the connectors, template and reference data bundle described on this page.
* [Open Survey Framework](/frameworks/osf/overview) - background on survey reports, annotations and analysis steps.
* [Automated Curation](/services/omvs/automated-curation/overview) - the API used to initiate governance action processes.

--8<-- "snippets/abbr.md"
