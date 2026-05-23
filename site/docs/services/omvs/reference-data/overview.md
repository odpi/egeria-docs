<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# Reference Data API

The Reference Data API provides a REST API to support user interfaces (UIs)
relating to the capture and maintenance of reference data such as code tables and valid metadata values.

## Key Features

The Reference Data API supports the following key features:

* **Valid Value Definition Management**: Creation, retrieval, update and deletion of valid value definitions.
* **Valid Value Set Management**: Organizing valid values into sets and hierarchies to represent code tables and taxonomies.
* **Reference Data Mapping**: Linking valid values to their equivalents in different systems to support synchronization and mapping.
* **Implementation and Consumption Tracking**: Identifying which systems and data fields use specific reference data.
* **Discovery and Exploration**: Tools for finding valid value definitions by name, search string, or unique identifier.

## Further information

* [Valid Value Concept](/concepts/valid-value-definition)
* [Reference Data Management](/features/reference-data-management/overview)

Sample requests for the REST API can be found in [Egeria-api-reference-data.http](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/view-services/reference-data/Egeria-api-reference-data.http).
[Egeria-coco-sales-territories.http](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/view-services/reference-data/Egeria-coco-sales-territories.http) shows how to use the Reference Data API to create a reference data set.
    
---8<-- "snippets/abbr.md"






