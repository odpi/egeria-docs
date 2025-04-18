<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# Design Model Open Metadata Access Service (OMAS)

The Design Model OMAS supports the management of design model intellectual property that has either been provided as standard or created in a software architecture and design modeling tool.

The current implementation of this service focuses on the development and maintenance of data design artifacts used to construct [data dictionaries](/concepts/data-dictionary) and [data specifications](/concepts/data-specification):

* [Data fields](/concepts/data-field) describe the logical structure of a data item.
* [Data classes](/concepts/data-class) describe the data values that may be stored in the data fields.  Data classes can be used to configure data quality validators running in the [Survey Action Engine](/survey-action-engine).
* [Data structures](/concepts/data-structure) describe the data fields for each required data source in a data specification.

## Use

The Design Model OMAS supports the [Data Designer OMVS](/services/omvs/data-designer/overview).

## Implementation

The Design Model OMAS is built on the [Open Metadata Store REST API](/services/oms-metadata-management) and so does not add new REST APIs of its own.

--8<-- "snippets/abbr.md"
