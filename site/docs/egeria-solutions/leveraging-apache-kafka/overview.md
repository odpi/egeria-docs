
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Leveraging your Apache Kafka estate

[Apache Kafka](https://kafka.apache.org/) is the event broker most Egeria deployments already depend on - it is Egeria's own default technology for exchanging events between [OMAG Servers](/concepts/omag-server), via the [Event Bus Configuration](/concepts/event-bus).  It is usually also carrying plenty of other traffic: application events, change-data-capture streams, and the topics that other technologies (including [Open Lineage events](/egeria-solutions/leveraging-open-lineage/overview)) are published to and consumed from.

Egeria's *Apache Kafka connectors* let you treat a Kafka server as a technology to catalog and govern in its own right, not just as plumbing:

* **Survey** an Apache Kafka server to see what topics it actually has, without needing to consume from any of them.
* **Catalog** the server and keep its topic list synchronized with open metadata as topics are created and removed.
* **Detect drift** between what's really running on the broker and what open metadata thinks is there, using a standalone audit connector.
* Do the survey and cataloguing using **standard governance action processes**, the same repeatable pattern used for Egeria's other technology connectors.


## Apache Kafka Technology Type Names

The technology type names (aka [deployed implementation types](/concepts/deployed-implementation-type)) added to Egeria's reference data for Apache Kafka are:

* *Apache Kafka Server* - A software server supporting an event broker that enables high-speed, reliable topic-based event exchange.
* *Apache Kafka Event Broker* - A software capability that enables high-speed, reliable topic-based event exchange.  This is the capability attached to the *Apache Kafka Server* asset.
* *Apache Kafka Topic* - the deployed implementation type used to tag each `Topic` asset catalogued from the broker.


## Connectors to Apache Kafka

The [Apache Kafka connectors](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/system-connectors/apache-kafka-connectors) provide a Java Admin API wrapper, a survey action service and an integration connector for working with an Apache Kafka broker.  A separate [Kafka Open Metadata Topic Connector](#the-kafka-open-metadata-topic-connector) is used for the very different job of sending and receiving events over Kafka topics.

| Connector Name                                    | Connector Type                                                     | Purpose                                                                                                                              |
|-------------------------------------------------------|--------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| **Apache Kafka Admin Connector**                     | [Digital Resource Connector](/concepts/digital-resource-connector) | A thin Java wrapper around Apache Kafka's native Admin API - lists topics, describes them, and retrieves broker metrics.  Used by the survey action service below; not separately documented outside its source. |
| **[Apache Kafka Cataloguer :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/system-connectors/apache-kafka-connectors/README.md#kafka-monitor-integration-connector){ target=gh }** | [Integration Connector](/concepts/integration-connector) | Catalogs the topics found on an Apache Kafka server as `Topic` assets, and removes the corresponding asset when a topic disappears. |
| **Apache Kafka Server Survey Service**               | [Survey Action Service](/concepts/survey-action-service)           | Surveys an Apache Kafka server to find out what topics it has. |

These connectors, their template and the associated reference data are delivered together in the *ApacheKafkaContentPack*.

### The Kafka Open Metadata Topic Connector

Separately from the connectors above, the [Kafka Open Metadata Topic Connector :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/event-bus-connectors/open-metadata-topic-connectors/kafka-open-metadata-topic-connector/README.md){ target=gh } implements a [resource connector](/concepts/digital-resource-connector) for a single Kafka topic that exchanges Java objects as JSON payloads.  This is the connector Egeria itself uses by default to send and receive events between its own servers, and it's also available for your own [integration connectors](/concepts/integration-connector) to use when they need to talk to a third-party technology over Kafka.  It isn't part of the Apache Kafka survey/catalogue story described below - it's plumbing, not a target to catalogue.

### Detecting drift: the Kafka Audit Log Integration Connector

The [Kafka Audit Log Integration Connector :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/integration-connectors/kafka-audit-integration-connector/README.md){ target=gh } takes a different approach: rather than keeping open metadata in sync with the broker, it listens for Audit Log Records published over Kafka by an OMAG Server and routes them to the [audit log destination connectors](/concepts/audit-log-destination-connector) configured as its catalog targets.  It is a standalone connector, configured directly in an integration daemon rather than through the governance action processes described below.


## Surveying an Apache Kafka server

The **Apache Kafka Server Survey Service** is deliberately simple: it uses the Apache Kafka Admin Connector to list the topics defined on the server, and records what it finds as two annotations on the survey report:

| Annotation Type                    | What it captures                                                                                          |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------|
| **Apache Kafka Topic List**        | A *[Resource Profile Annotation](/types/6/0620-Resource-Profiling)* whose `valueList` is the full list of topic names found. |
| **Apache Kafka Topic Inventory**   | The same list written out as a *[Resource Profile Log Annotation](/types/6/0620-Resource-Profiling)* - useful when there are too many topics to want listed directly in open metadata. |

??? example "Example annotation from surveying an Apache Kafka server"
    ```json
    {
      "class": "ResourceProfileAnnotation",
      "annotationType": "Apache Kafka Topic List",
      "summary": "List of topics known to the Apache Kafka server.",
      "explanation": "Topics provide the mechanism to organize events.  They may be explicitly configured, or created dynamically.",
      "analysisStep": "Profiling Associated Resources",
      "valueList": [
        "egeria.omag.openmetadata.repositoryservices.cohort.cocoCohort.OMRSTopic",
        "egeria.omag.server.cocoMDS1.omas.AssetOwner.OutTopic",
        "clinical-trials.patient-enrollment"
      ]
    }
    ```

Because the survey only calls Kafka's Admin API to list and describe topics, it never subscribes to a topic or reads any of the events flowing through it - it has no visibility into message content at all.

<!-- SCREENSHOT PLACEHOLDER: apache-kafka-survey-report.png - the survey report and its topic-list annotations, as shown against the Apache Kafka server asset in the Egeria UI. -->
*(Screenshot to follow: the survey report and its annotations, as displayed against the surveyed Apache Kafka server asset in the Egeria UI.)*


## Cataloguing an Apache Kafka server

Cataloguing a server configures the **Apache Kafka Cataloguer** integration connector, which creates a `Topic` asset (tagged with the *Apache Kafka Topic* deployed implementation type) for each topic it finds, and removes the asset again if the topic disappears from the broker.  The connector accepts either an event broker or a software server as its catalog target - if you give it a software server, that server must have an event broker software capability attached, which is exactly what the *Apache Kafka Server* template creates for you.

<!-- SCREENSHOT PLACEHOLDER: apache-kafka-catalogued-topics.png - the Apache Kafka server asset and its catalogued Topic assets shown in the Egeria UI. -->
*(Screenshot to follow: the catalogued Apache Kafka server and its Topic assets, shown in the Egeria UI.)*


## Running this through the Automated Curation API

The survey and cataloguing capabilities above are packaged as ready-to-run **governance action processes**, delivered by the *ApacheKafkaContentPack*.  You initiate them through the [Automated Curation](/services/omvs/automated-curation/overview) API of a view server - either directly over REST, or through **pyegeria**.

| Governance Action Process                                            | What it does                                                                                                                 |
|--------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| `ApacheKafkaServer:CreateAndSurveyGovernanceActionProcess`            | Creates the *Apache Kafka Server* asset and runs the Apache Kafka Server Survey Service against it, printing out the resulting report. |
| `ApacheKafkaServer::CreateAsCatalogTargetGovernanceActionProcess`     | Creates the *Apache Kafka Server* asset and configures the Apache Kafka Cataloguer to start cataloguing its topics.          |
| `ApacheKafkaServer:DeleteAssetWithTemplateGovernanceActionProcess`    | Deletes the server asset (and everything anchored to it) using the same template properties used to create it.              |

Below are the flows for the two most commonly used processes, showing the request parameters each one accepts:

=== "CreateAndSurvey"

    --8<-- "snippets/governance-action-processes/apachekafkaserver:createandsurvey-mermaid-graph.md"

=== "CreateAsCatalogTarget"

    --8<-- "snippets/governance-action-processes/apachekafkaserver::createascatalogtarget-mermaid-graph.md"


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

### Survey an Apache Kafka server
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/automated-curation/governance-action-processes/initiate
Authorization: Bearer {{token}}
Content-Type: application/json

{
  "processQualifiedName": "ApacheKafkaServer:CreateAndSurveyGovernanceActionProcess",
  "requestParameters" : {
    "serverName" : "LocalApacheKafka1",
    "hostIdentifier" : "localhost",
    "portNumber" : "9092",
    "versionIdentifier" : "1.0",
    "description" : "Apache Kafka event broker."
  }
}

> {% client.global.set("surveyInstanceGUID", response.body.guid); %}

### Catalog the same Apache Kafka server (and its topics)
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/automated-curation/governance-action-processes/initiate
Authorization: Bearer {{token}}
Content-Type: application/json

{
  "processQualifiedName": "ApacheKafkaServer::CreateAsCatalogTargetGovernanceActionProcess",
  "requestParameters" : {
    "serverName" : "LocalApacheKafka1",
    "hostIdentifier" : "localhost",
    "portNumber" : "9092",
    "versionIdentifier" : "1.0",
    "description" : "Apache Kafka event broker."
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

Unlike the database connectors, there is no `includeTopicList`/`excludeTopicList` style filtering on the survey or cataloguer today - every topic found on the broker is surveyed and, once cataloguing is configured, catalogued.

### Using pyegeria

This follows exactly the same pattern as the [PostgreSQL pyegeria walkthrough](/egeria-solutions/leveraging-postgres/overview#using-pyegeria) - just with the Apache Kafka process names and default port (9092) substituted in:

```python
from pyegeria import EgeriaTech, load_mermaid, render_mermaid

view_server = "qs-view-server"
url         = "https://host.docker.internal:9443"
user_id     = "erinoverview"
user_pwd    = "secret"

egeria_tech = EgeriaTech(view_server, url, user_id, user_pwd)
token = egeria_tech.create_egeria_bearer_token()

# See what Apache Kafka governance action processes are available
elements = egeria_tech.find_elements_by_property_value(
    property_value="ApacheKafka",
    property_names=["qualifiedName"],
    metadata_element_type_name="GovernanceActionProcess",
)
for element in elements:
    properties = element.get("properties")
    print("* " + properties.get("qualifiedName") + " - " + properties.get("description"))

# Survey an Apache Kafka server
request_parameters = {
    "serverName" : "LocalApacheKafka1",
    "hostIdentifier" : "localhost",
    "portNumber" : "9092",
    "versionIdentifier" : "1.0",
    "description" : "Apache Kafka event broker.",
}

survey_instance_guid = egeria_tech.initiate_gov_action_process(
    "ApacheKafkaServer:CreateAndSurveyGovernanceActionProcess",
    None, None, None, request_parameters, None, None,
)

# Watch the process run as a mermaid diagram
load_mermaid()
process_graph = egeria_tech.get_governance_process_graph(survey_instance_guid)
render_mermaid(process_graph.get("governanceActionProcessMermaidGraph"))

# Once you're happy with what the survey found, catalog the server too
catalog_instance_guid = egeria_tech.initiate_gov_action_process(
    "ApacheKafkaServer::CreateAsCatalogTargetGovernanceActionProcess",
    None, None, None, request_parameters, None, None,
)
```

To follow progress of the integration connector once cataloguing has started, use:

```python
from commands.ops.monitor_daemon_status import display_integration_daemon_status

display_integration_daemon_status(
    ["ApacheKafkaCataloguer"],
    integ_server="qs-integration-daemon",
    paging=True,
    width=150,
)
```

<!-- SCREENSHOT PLACEHOLDER: apache-kafka-integration-daemon-status.png - display_integration_daemon_status() output showing the Apache Kafka Cataloguer connector running. -->
*(Screenshot to follow: `display_integration_daemon_status()` output for the Apache Kafka connector.)*


## Related information

* [Leveraging your PostgreSQL estate](/egeria-solutions/leveraging-postgres/overview) - the equivalent solution for PostgreSQL, following the same governance action process pattern.
* [Leveraging Open Lineage](/egeria-solutions/leveraging-open-lineage/overview) - Kafka is also the transport most Open Lineage event capture runs over.
* [Open Survey Framework](/frameworks/osf/overview) - background on survey reports, annotations and analysis steps.
* [Automated Curation](/services/omvs/automated-curation/overview) - the API used to initiate governance action processes.

--8<-- "snippets/abbr.md"
