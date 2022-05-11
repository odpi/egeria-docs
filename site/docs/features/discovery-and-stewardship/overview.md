<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2021,2022. -->

# Metadata discovery and stewardship

Metadata discovery is an automated process that extracts metadata about a [digital resource](/concepts/resource). This metadata may be:

* embedded within the asset (for example a digital photograph has embedded metadata), or
* managed by the platform that is hosting the asset (for example, a relational database platform maintains schema information about the data store in its databases), or
* determined by analysing the content of the asset (for example a quality tool may analyse the data content to determine the types and range of values it contains and, maybe from that analysis, determine a quality score for the data).

Some metadata discovery may occur when the digital resource is first catalogued as an [asset](/concepts/asset).  [Integrated cataloguing](/features/integrated-cataloguing) typically automates the creation the basic asset entry, its connection and optionally, its schema.  This is sometimes called *technical metadata*.  

??? example "Cataloguing database with integrated cataloguing"
    For example, the schema of a database may be catalogued through the [Data Manager OMAS](/services/omas/data-manager/overview) API. This schema may have been automatically extracted by an integration connector hosted in Egeria's [Database Integrator OMIS](/services/omis/database-integrator/overview).

The [*open discovery services*](/concepts/open-discovery-service) build on this initial cataloguing. They use advanced analysis to inspect the *content* of a digital resource to derive new insights that can augment or validate their catalog entry.

The results of this analysis is added to a [discovery analysis report](/concepts/discovery-analysis-report) linked off of the asset for the digital resource.

The analysis results documented in the discovery analysis report can either be [automatically applied](/concepts/governance-action) to the asset's catalog entry or it can go through a *stewardship process* where a subject-matter expert confirms the findings (or not).  

Discovery and stewardship are the most advanced form of automation for asset cataloging. Egeria provides the server runtime environment and component framework to allow third parties to create discovery services and governance action implementations. It has only simple implementations of these components, mostly for demonstration purposes. This is an area where vendors and other open source projects are expected to provide additional value.

## Open discovery services

---8<-- "docs/connectors/discovery/discovery-service-intro.md"

## Open discovery pipelines

---8<-- "docs/guides/developer/open-discovery-services/discovery-pipeline-intro.md"

## Inside the discovery analysis report

The discovery analysis report structures the annotations in two ways:

* Annotations that describe a characteristic of the whole digital resource.
* Annotations that describe a characteristic of a single data field within the digital resource.

The annotations for the data fields are linked off of the data fields created by [schema extraction](#schema-extraction).

![Discovery analysis report structure](/guides/developer/open-discovery-services/discovery-analysis-report-structure.svg)

## Discovery actions

Open discovery can be used for the following types of analysis.

### Schema extraction

For digital resources that include structured data, *schema extraction* documents the data fields present in the digital resource and if the schema is attached to the asset, it will attempt to match the data fields it finds to its schema attributes.

Schema extraction uses the [schema analysis annotation](/types/6/0615-Schema-Extraction).  It is linked directly off of the discovery analysis report.

[Data field](/types/6/0615-Schema-Extraction) entities, one for each data field in the digital resource, are then linked together to show the structure of the data in the digital resource and this structure is linked off of the schema analysis annotation.

![Open discovery schema extraction](/guides/developer/open-discovery-services/open-discovery-schema-extraction.svg)

The schema of the data in the digital resource is defined in a *SchemaType* linked from the digital resource's asset using the *AssetSchemaType* relationship.  This may be established before the open discovery service runs, or may be derived by a [governance action](/concepts/governance-action) once the open discovery service has run.

If the schema is defined, the open discovery service that creates the data fields may maintain relationships between the schema and the data fields:

* The *SchemaTypeDefinition* links the schema analysis annotation to the top level schema type.
* The *SchemaAttributeDefinition* links a data field to is corresponding schema attribute.

Alternatively, these relationships can be established by a governance action that is processing the results of the schema extraction.  They are useful for consumers of the asset to be able to navigate to the specific data field annotations from the schema.

![Schema Extraction in Report](/guides/developer/open-discovery-services/open-discovery-schema-extraction-with-schema-links.svg)

Where a digital resource has a fixed structure that does not support repeating fields, such as a relational database, the schema extraction can use the schema to create the data fields since the result will always be one-to-one (assuming the schema is being actively maintained).

However, if there are repeating groups in the digital resource's data fields then the schema extraction needs to work off of the data in the digital resource.

### Data profiling

Profiling analysis looks at the data values in the resource and summarizes their characteristics.  There are three types of annotations used in data profiling.

* [Data Profile Annotation](/types/6/0620-Data-Profiling) - Capture the characteristics of the data values stored in a specific data field in a data source.
* [Data Profile Log Annotation](/types/6/0620-Data-Profiling) - Capture the named of the log files where profile characteristics of the data values stored in a specific data field.  This is used when the profile results are too large to store in open metadata.
* [Fingerprint Annotation](/types/6/0620-Data-Profiling) - Capture the characteristics of the data values stored in a specific data field or the whole digital resource and express it as a single value.

![Open discovery data profiling](/guides/developer/open-discovery-services/open-discovery-data-profiling.svg)

For structured data, data profiling needs to run after schema extraction to allow the data profiling annotations that refer to a specific data field to be linked from the appropriate data field entity.

### Data class discovery

Data class discovery captures the analysis on how close a data field matches the specification defined in a [data class](/concepts/data-class).

![Data class discovery](/guides/developer/open-discovery-services/open-discovery-data-class-discovery.svg)

The recommendation for a specific data class are stored in a [data class annotation](/types/6/0625-Data-Class-Discovery) linked off of the appropriate data field.  Data class discovery needs to run after schema extraction.  It often builds on the information provided by data profiling.

### Semantic discovery

Semantic discovery is attempting to define the meaning of the data values in the asset. The result is a recommended glossary term stored as a [semantic annotation](/types/6/0630-Semantic-Discovery).

![Semantic discovery](/guides/developer/open-discovery-services/open-discovery-semantic-discovery.svg)

These annotations are the metadata discovery equivalent of the *Informal Tag* shown in [0150 - Feedback](/types/1/0150-feedback) in Area 1.  It typically takes confirmation by a subject-matter expert to convert this into a [Semantic Assignment](/types/3/0370-Semantic-Assignment).  Semantic discovery needs to run after schema extraction.  It often builds on the information provided by data profiling and data class discovery.

### Classification discovery

Classification discovery adds recommendations for new classifications that should either be added to the asset, or to a schema attribute in the asset.  It uses the [classification annotation](/types/6/0635-Classification-Discovery) to describe the classification and its properties.
If the classification is for the asset, the classification annotation is linked off of the discovery analysis report.  If it is for a specific schema attribute, it is linked off of the corresponding data field.

![Classification discovery](/guides/developer/open-discovery-services/open-discovery-classification-discovery.svg)

### Calculating quality scores

Quality scores describe how well the data values, typically in a data field, conform to a specification.  For example, do the values match a list of valid values.

![Quality Scores](/guides/developer/open-discovery-services/open-discovery-quality-scores.svg)

### Relationship discovery

Relationship discovery identifies relationships between different resources (or data fields), such as two columns that have a foreign key relationship.

It is possible to create the relationship as a relationship annotation or attach a relationship advice to the discovery analysis report.

![Relationship discovery](/guides/developer/open-discovery-services/open-discovery-relationship-discovery.svg)

### Capturing measurements

The measurement annotations capture a snapshot of the physical dimensions and activity levels at a particular moment in time.  For example, it may calculate the size of the data source or the number of users accessing it.

![Data source measurements](/guides/developer/open-discovery-services/open-discovery-data-source-measurement.svg)

### Requesting stewardship action

A RequestForAction entity (RfA) is used when an open discovery service performs a test on the data (such as a discovery rule) or has discovered an anomaly in the data landscape compared to its metadata that potentially needs a steward or a curator's action.

![Request for action](/guides/developer/open-discovery-services/open-discovery-request-for-action.svg)

The [Stewardship Action OMAS](/services/omas/stewardship-action/overview) is designed to respond to the requests for actions (RfAs).

## Working with external engines

Open discovery services may directly implement the analysis function or may invoke an external service to create the annotations.

## Initiating stewardship

Stewardship is initiated either through the creation of a *Request for Action* annotation or when the *discovery analysis report's* status changes to COMPLETE.

!!! education "Further information"
    * [Open discovery services supplied by the Egeria project](/connectors/#open-discovery-services)
    * [Writing your own open discovery services](/guides/developer/open-discovery-services/overview)

--8<-- "snippets/abbr.md"