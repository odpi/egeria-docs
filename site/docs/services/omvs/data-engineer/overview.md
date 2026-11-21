
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# Data Engineer API

The Data Engineer API provides a persona-specific view for individuals responsible for
designing, building, and maintaining data processing systems and pipelines.
It enables the creation and maintenance of data pipelines, reference data, tabular data sets, and descriptions of the data values used to configure processing.
It is used in conjunction with the [Asset Maker API](/services/omvs/asset-maker/overview).

## Key Features

The Data Engineer API provides the following capabilities:

- **Data Pipelines**: Support for defining and maintaining data pipelines, which are
  choreographed sequences of data processing steps that move and transform data.
- **Reference Data**: Capabilities for managing reference data, such as controlled lists of
  values used for classification and data quality.
- **Tabular Data Sets**: Tools for working with tabular data sets, including retrieving
  detailed reports that include data rows, column descriptions, and metadata.
- **Data Set Exploration**: Retrieving details of tabular data sets anchored to assets,
  supporting data discovery and analysis.
- **Data Values**: Describing particular data values, such as the values used to configure a
  process instance, and linking them to the elements that use them and the assets where they are stored.

## Describing data values

A [*DataValue*](/types/2/0208-Data-Values/#datavalue-entity) describes a particular data value, such as a value used to configure a process instance (for example, an analytic model run).  Data values help to explain why different runs of the same process produce different results.  A data value records the value's format, length, data type and usage, and can carry a fingerprint or hash of its content.

A [*LiteralDataValue*](/types/2/0208-Data-Values/#literaldatavalue-entity) is a data value that holds the data in open metadata, as a string (*dataValue*), a list of strings (*dataValueList*) or a map (*dataValueMap*).  It is maintained through the same operations as a data value: supply *LiteralDataValueProperties* in the request.

| Operation | URL (after `/data-engineer`) | Request body |
|---|---|---|
| *createDataValue* | `/data-values` | *NewElementRequestBody* |
| *createDataValueFromTemplate* | `/data-values/from-template` | *TemplateRequestBody* |
| *updateDataValue* | `/data-values/{dataValueGUID}/update` | *UpdateElementRequestBody* |
| *deleteDataValue* | `/data-values/{dataValueGUID}/delete` | *DeleteElementRequestBody* |
| *getDataValuesByName* | `/data-values/by-name` | *FilterRequestBody* |
| *findDataValues* | `/data-values/by-search-string` | *SearchStringRequestBody* |
| *getDataValueByGUID* | `/data-values/{dataValueGUID}/retrieve` | *GetRequestBody* |

A data value is linked to other elements with three relationships.  Each is attached with a `.../attach` request and removed with the matching `.../detach` request.

| Relationship | Operations | URL (after `/data-engineer`) | Purpose |
|---|---|---|---|
| [*ProcessingVariable*](/types/2/0208-Data-Values/#processingvariable-relationship) | *linkProcessingVariable* / *detachProcessingVariable* | `/elements/{elementGUID}/processing-variables/{dataValueGUID}/...` | Links an element, such as a process, to a data value used to configure its processing, with the position in which the value is passed. |
| [*EmbeddedDataValue*](/types/2/0208-Data-Values/#embeddeddatavalue-relationship) | *linkEmbeddedDataValue* / *detachEmbeddedDataValue* | `/data-values/{parentDataValueGUID}/embedded-data-values/{embeddedDataValueGUID}/...` | Places one data value inside another, with its position. |
| [*DataValueSource*](/types/2/0208-Data-Values/#datavaluesource-relationship) | *linkDataValueSource* / *detachDataValueSource* | `/data-values/{dataValueGUID}/data-value-sources/{assetGUID}/...` | Links a data value to the asset for the digital resource where the data is stored. |

The types of data value that a process can be configured with are described by schema types.  They are linked to the process through the [Schema Maker API](/services/omvs/schema-maker/overview).

## Further information

- [Reference Data Management](/features/reference-data-management/overview)
- [Tabular Data Set Concept](/concepts/tabular-data-set/)
- [0208 Data Values](/types/2/0208-Data-Values) describes the open metadata types for data values.

____
Sample REST API requests can be found in:

- [Egeria-api-data-engineer.http](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/view-services/data-engineer/Egeria-api-data-engineer.http)
- [Egeria-api-data-engineer.http](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/view-services/data-engineer/Egeria-jacquard-data-sets.http)



---8<-- "snippets/abbr.md"






