
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# Data Engineer API

The Data Engineer API provides a persona-specific view for individuals responsible for
designing, building, and maintaining data processing systems and pipelines.
It enables the creation and maintenance of data pipelines, reference data, and tabular data sets.
It is used in conjunction with the [Asset Maker API](/services/asset-maker/overview).

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

## Further information

- [Reference Data Management](/features/reference-data-management/overview)
- [Tabular Data Set Concept](/concepts/tabular-data-set/)

____
Sample REST API requests can be found in:

- [Egeria-api-data-engineer.http](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/view-services/data-engineer/Egeria-api-data-engineer.http)
- [Egeria-api-data-engineer.http](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/view-services/data-engineer/Egeria-jacquard-data-sets.http)



---8<-- "snippets/abbr.md"






