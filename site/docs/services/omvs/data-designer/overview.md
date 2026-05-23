<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# Data Designer API

The Data Designer API provides a REST API to support user interfaces (UIs)
relating to the definition of data structures, data fields and data value specifications.
These can be assembled into data specifications to describe the data requirements for a project or digital product.

## Key Features

The Data Designer API supports the following key concepts:

* **Data Structures**: Reusable definitions of the structure of data (e.g., a record or a message).
* **Data Fields**: Individual fields within a data structure.
* **Data Value Specifications**: Definitions of the valid values and formats for data, including data classes and data grains.
* **Data Specifications**: Assembly of data structures and fields with semantic definitions (glossary terms)
  and data value specifications to provide a complete description of data requirements.

These definitions can also be linked to certification types to guide automated data quality checks.

## Further information

* [Data Structure Concept](/concepts/data-structure)
* [Data Field Concept](/concepts/data-field)
* [Data Value Specification Concept](/concepts/data-value-specification)
* [Data Specification Concept](/concepts/data-specification)

Sample requests for the REST API can be found in [Egeria-api-data-designer.http](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/view-services/data-designer/Egeria-api-data-designer.http).
In addition:

* [Egeria.coco-create-data-spec.http](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/view-services/data-designer/Egeria-coco-create-data-spec.http) provides an example of creating a data specification.
* [Egeria-jacquard-data-design.http](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/view-services/data-designer/Egeria-jacquard-data-design.http) provides an example of using the Data Designer API to review data specification from the Open Metadata Digital Product Catalog.

---8<-- "snippets/abbr.md"






