<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2021,2022. -->

# Metadata discovery and stewardship

Metadata discovery is an automated process that extracts metadata about a [digital resource](/concepts/digital-resource). This metadata may be:

* embedded within the asset (for example a digital photograph has embedded metadata), or
* managed by the platform that is hosting the asset (for example, a relational database platform maintains schema information about the data store in its databases), or
* determined by analysing the content of the asset (for example a quality tool may analyse the data content to determine the types and range of values it contains and, maybe from that analysis, determine a quality score for the data).

Some metadata discovery may occur when the digital resource is first catalogued as an [asset](/concepts/asset).  [Integrated cataloguing](/features/integrated-cataloguing/overview) typically automates the creation the basic asset entry, its connection and optionally, its schema.  This is sometimes called *technical metadata*.  

??? example "Cataloguing database with integrated cataloguing"
    For example, the schema of a database may be catalogued through the [Data Manager OMAS](/services/omas/data-manager/overview) API. This schema may have been automatically extracted by an integration connector hosted in Egeria's [Database Integrator OMIS](/services/omis/database-integrator/overview).

The [*survey action services*](/concepts/survey-action-service) build on this initial cataloguing. They use advanced analysis to inspect the *content* of a digital resource to derive new insights that can augment or validate their catalog entry.

The results of this analysis is added to a [survey report](/concepts/survey-report) linked off of the asset for the digital resource.

The analysis results documented in the survey report report can either be [automatically applied](/concepts/governance-action) to the asset's catalog entry or it can go through a *stewardship process* where a subject-matter expert confirms the findings (or not).  

Discovery and stewardship are the most advanced form of automation for asset cataloging. Egeria provides the server runtime environment and component framework to allow third parties to create survey action services and governance action implementations. It has only simple implementations of these components, mostly for demonstration purposes. This is an area where vendors and other open source projects are expected to provide additional value.

## Survey action services

---8<-- "snippets/connectors/survey-action-service-intro.md"

## Inside the survey report

The survey report structures the annotations in two ways:

* Annotations that describe a characteristic of the whole digital resource.
* Annotations that describe a characteristic of a single data field within the digital resource.

The annotations for the data fields are linked off of the schema attributes created by [schema extraction](#schema-extraction).

![Survey report structure](/frameworks/osf/survey-report-structure.svg)

## Survey actions

Survey actions can be used for the following types of analysis.

### Schema extraction

For digital resources that include structured data, *schema extraction* documents the data fields present in the digital resource and if the schema is attached to the asset, it will attempt to match the data fields it finds to its schema attributes.

Schema extraction uses the [schema analysis annotation](/types/6/0615-Schema-Extraction).  It is linked directly off of the survey report.  The schema of the data in the digital resource is defined in a [*SchemaType*](/types/5/0501-Schema-Elements) linked from the digital resource's asset using the [*AssetSchemaType*](/types/5/0503-Asset-Schema) relationship.  This may be established before the survey action service runs, or may be derived by the survey action service itself.

### Resource profiling

Profiling analysis looks at the data values in the resource and summarizes their characteristics.  There are three types of annotations used in resource profiling.

* [Resource Profile Annotation](/types/6/0620-Resource-Profiling) - Capture the characteristics of the data values stored in a specific resource.
* [Resource Profile Log Annotation](/types/6/0620-Resource-Profiling) - Capture the named of the log files where profile characteristics are captured.  This is used when the profile results are too large to store in open metadata.
* [Fingerprint Annotation](/types/6/0620-Resource-Profiling) - Capture the characteristics of the resource and express it as a single value.

![Resource profiling](/frameworks/osf/survey-action-resource-profiling.svg)

For structured data, resource profiling needs to run after schema extraction to allow the resource profiling annotations that refer to a specific data field to be linked from the appropriate data field entity.

### Data class discovery

Data class discovery captures the analysis on how close a data field matches the specification defined in a [data class](/concepts/data-class).

![Data class discovery](/frameworks/osf/survey-action-data-class-discovery.svg)

The recommendation for a specific data class are stored in a [data class annotation](/types/6/0625-Data-Class-Discovery) linked off of the appropriate data field.  Data class discovery needs to run after schema extraction.  It often builds on the information provided by resource profiling.

Subsequent stewardship - either automated or with human assistance - can confirm the correct assignment using the [*DataClassAssignment*](/types/5/0540-Data-Classes) relationship.

### Semantic discovery

Semantic discovery is attempting to define the meaning of the data values in the asset. The result is a recommended glossary term stored as a [semantic annotation](/types/6/0630-Semantic-Discovery).

![Semantic discovery](/frameworks/osf/survey-action-semantic-discovery.svg)

These annotations are the metadata discovery equivalent of the *Informal Tag* shown in [0150 - Feedback](/types/1/0150-feedback) in Area 1.  It typically takes confirmation by a subject-matter expert to convert this into a [Semantic Assignment](/types/3/0370-Semantic-Assignment).  Semantic discovery needs to run after schema extraction.  It often builds on the information provided by data profiling and data class discovery.

### Classification discovery

Classification discovery adds recommendations for new classifications that should either be added to the asset, or to a schema attribute in the asset.  It uses the [classification annotation](/types/6/0635-Classification-Discovery) to describe the classification and its properties.
If the classification is for the asset, the classification annotation is linked off of the discovery analysis report.  If it is for a specific schema attribute, it is linked off of the corresponding data field.

![Classification discovery](/frameworks/osf/survey-action-classification-discovery.svg)

### Calculating quality scores

Quality scores describe how well the data values, typically in a data field, conform to a specification.  For example, do the values match a list of valid values.   This type of annotation is often used within a [data quality program](/features/data-quality/overview) to provide assessments of the data for different purposes.

![Quality Scores](/frameworks/osf/survey-action-quality-scores.svg)

### Relationship discovery

Relationship discovery identifies relationships between different resources (or data fields), such as two columns that have a foreign key relationship.

It is possible to create the relationship as a relationship annotation or attach a relationship advice to the discovery analysis report.

![Relationship discovery](/frameworks/osf/survey-action-relationship-discovery.svg)

### Capturing measurements

The measure annotations capture a snapshot of the physical dimensions and activity levels at a particular moment in time.  For example, it may calculate the size of the resource or the number of users accessing it.

![Data source measurements](/frameworks/osf/survey-action-data-source-measurement.svg)

### Requesting stewardship action

A RequestForAction entity (RfA) is used when a survey action service performs a test on the data (such as a [quality rule](/features/data-quality/overview)) or has discovered an anomaly in the data landscape compared to its metadata that potentially needs a steward or a curator's action.

![Request for action](/frameworks/osf/survey-action-request-for-action.svg)

The [Stewardship Action OMAS](/services/omas/stewardship-action/overview) is designed to respond to the requests for actions (RfAs).

## Working with external engines

Survey action services may directly implement the analysis function or may invoke an external service to create the annotations.

## Initiating stewardship

Stewardship is initiated either through the creation of a *Request for Action* annotation or when the *discovery analysis report's* status changes to COMPLETE.

!!! education "Further information"
    * [Survey action services supplied by the Egeria project](/connectors/#open-discovery-services)
    * [Writing your own survey action services](/guides/developer/survey-action-services/overview)

--8<-- "snippets/abbr.md"