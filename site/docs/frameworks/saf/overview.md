<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/tech-preview.md"

# Survey Action Framework (SAF)
  
The *Survey Action Framework (SAF)* enables [metadata survey tools](/features/discovery-and-stewardship) to integrate with open metadata repositories by defining the interfaces for surveyor components (called [survey action services](#survey-action-service)) to:

- Access survey request configuration.
- Search for [assets](/concepts/asset) and related metadata in the metadata repository.
- Extract all the metadata known about a specific asset.
- Record the results of the analysis in the open metadata repository and attach it to the asset's metadata for later processing.


## Survey action service

A *survey action service* provides specific analysis of the real-world resources associated with an [asset](/concepts/asset) on request.  It may provide the complete implementation of the function, or invoke the services of an external tool.

The results of the analysis are stored in an [*survey report*](#survey-report).

The result is one or more sets of related properties that the survey action service has discovered about the asset, its metadata, structure and/or content. These are stored in a set of [annotations](#annotations) linked off of a [survey report](#survey-report). The survey report is linked off of the asset definition in the open metadata repository.


### Survey action pipeline

A *survey action pipeline* is a specialized implementation of a [survey action service](#survey-action-service) that runs a set of survey action services against a single asset. The implementation of the survey action pipeline determines the order that these survey action services are run.

The aim of the survey action pipeline is to enable a detailed picture of the properties of an asset to be built up by the nested survey action services it calls. Each survey action service is able to access the results of the survey action services that have run before it.


## Survey report

The *survey report* lists the [annotations](#annotations) that were created during the execution of a [survey action service](#survey-action-service).

The survey report is created automatically in the open metadata repository when the survey action service is started.  Annotations are published to report as soon as they are created by the survey action service so it is possible to process the annotations from a long-running survey before it has completed.

### Annotations

An *annotation* describes one or more related properties about an [asset](/concepts/asset) that has been surveyed by a [survey action service](#survey-action-service).

Different types of annotations provide different types of information.

| Annotation type | Description |
|---|---|
| Classification annotation | Captures a recommendation of which classifications to attach to this asset. It can be made at the asset or data field level. |
| Data class annotation | Captures a recommendation of which data class this data field closely represents. |
| Data profile annotation | Capture the characteristics of the data values stored in a specific data field in a data source. |
| Data profile log annotation | Capture the names of the log files where profile characteristics of the data values stored in a specific data field. This is used when the profile results are too large to store in open metadata. |
| Data source measurement annotation | Collect arbitrary properties about a data source. |
| Data source physical status annotation | Documents the physical characteristics of a data source asset. |
| Relationship advice annotation | Document a recommended relationship that should be established with the asset. |
| Quality annotation | Document calculated quality scores on different dimensions. |
| Semantic annotation | Documents suggested meanings for this data based on the values and name of the field. |
| Suspect duplicate annotation | Identifies other asset definitions that seem to point to the same physical asset. |

## Survey context

A survey action service is implemented as a specialized [connector](/concepts/connector) that is passed a *survey context* as part of its initialization process.

The *survey context* provides the [survey action service](#survey-action-service) with access to information about the survey request along with the open metadata repository interfaces.

![Survey context](survey-context.svg)

The survey context provides parameters used by a survey action service to locate and analyze an asset and then record the results.  

### Annotation store

The annotation store provides a survey action service with methods to write [annotations](#annotation) to an open metadata repository. These annotations describe the results of the analysis performed on an asset by the survey action service.

The annotations are automatically linked to the survey survey report that is in turn linked off of the analysed asset.  Each annotation can also be linked to other metadata elements that is describes.

## Survey asset store

A survey action service is able to create a [resource connector](/concepts/digital-resource-connector) for the asset it is to analyze using the *survey asset store*.

## Open Metadata store

The *open metadata store* provides a search interface that enables a survey action service to locate assets and related metadata that are described in the open metadata repository.  It is also able to make updates to these elements.

## Implementation in Egeria

Survey action services run under the [Survey Action OMES](/services/omes/survey-action/overview) hosted in an [Engine Host](/concepts/engine-host).

The open metadata types for a annotations are described in [area 6](/types/6) of the model.  The main entity type is called [*Annotation*](/types/6/0610-Annotations). It is extended by *DataFieldAnnotation* to distinguish annotations that refer, primarily to a data field rather than the whole asset. Other more specialist annotations extend these two basic annotation types.

--8<-- "snippets/abbr.md"
