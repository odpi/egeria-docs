<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Writing an Open Discovery Service

---8<-- "docs/connectors/discovery/discovery-service-intro.md"


## Discovery Context

The discovery context provides the *open discovery service* with access to information about the discovery request along with the open metadata repository interfaces.

![Structure of the discovery context](/frameworks/odf/discovery-context.svg)

### Discovery Asset Catalog Store

The discovery asset catalog store provides a search interface that enables an open discovery service to locate assets that are described in the open metadata repository.

### Discovery Annotation Store

The discovery annotation store provides a open discovery service with access to the annotations created about a specific asset both from past invocations of open discovery services and those created during the current execution.

### Discovery Asset Store

The discovery asset catalog store provides an open discovery service with access to all of the known metadata about the digital resource it is to analyse.  It is able to create a connector to the digital resource based on the connection(s) attached to the asset.

### Discovery Analysis Report Store

The discovery analysis report store is a client to an open metadata server that enables an open discovery service to query the properties of its discovery analysis report and update the analysis step that is currently executing and the status of its processing.

The discovery analysis report store is accessed from the [discovery annotation store](#discovery-annotation-store).


## Discovery Annotations

A discovery annotation describes one or more related properties about the digital resource. Some annotations refer to an entire digital resource and others refer to a data field within the digital resource.   The annotations that describe a single data field are called *data field annotations*.

The annotation types defined in the  [Open Discovery Framework (ODF)](/frameworks/odf/overview) are as follows:

* **Classification Annotation** - Captures a recommendation of which classifications to attach to this asset.  It can be made at the asset or data field level.
* **Data Class Annotation** - Captures a recommendation of which data class this data field closely represents.
* **Data Profile Annotation** - Capture the characteristics of the data values stored in a specific data field in a data source.
* **Data Profile Log Annotation** - Capture the named of the log files where profile characteristics of the data values stored in a specific data field.  This is used when the profile results are too large to store in open metadata.
* **Data Source Measurement Annotation** - collect arbitrary properties about a data source.
* **Data Source Physical Status Annotation** - documents the physical characteristics of a data source asset.
* **Relationship Advice Annotation** - document a recommended relationship that should be established with the asset.
* **Quality Annotation** - document calculated quality scores on different dimensions.
* **Schema Analysis Annotation** - document the structure of the data (schema) inside the asset.
* **Semantic Annotation** - documents suggested meanings for this data based on the values and name of the field.
* **Suspect Duplicate Annotation** - identifies other asset definitions that seem to point to the same physical asset.

??? "education" Open Metadata Types for Discovery Annotations

    The open metadata types for a discovery annotations are describe in [Area 6](/types/6).

    The main entity type is called [Annotation](/types/6/0610-Annotations).  It is extended by [DataFieldAnnotation](/types/6/0617-Data-Field-Analysis.md) to distinguish annotations that refer, primarily to a data field. Other more specialist annotations extend these two basic annotation types.

## Implementing Open discovery services

An open discovery service is implemented as a specialized [Open Connector Framework (OCF)](/frameworks/ocf/overview) connector.  The interface and base class are provided by the [Open Discovery Framework (ODF)](/frameworks/odf/overview).  It is initialized with a connector to the Asset it is to analyze and details of the results of other discovery services that have run before it if it is part of a [discovery pipeline](#open-discovery-pipelines).


## Open Discovery Pipelines

---8<-- "docs/guides/developer/open-discovery-services/discovery-pipeline-intro.md"

## Example implementations

The definition of the connector interfaces for discovery services is defined in the [open-discovery-services :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/frameworks/open-discovery-framework/src/main/java/org/odpi/openmetadata/frameworks/discovery){ target=gh } module.

There are implementations of discovery services in the [discovery-service-connectors](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/discovery-service-connectors){ target=gh } module.

---8<-- "snippets/abbr.md"