
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# Lineage Linker API

The Lineage Linker is a REST API that enables the caller to maintain lineage relationships.

## Key Features

- **Lineage Relationship Management**: Create, update, and remove lineage relationships between elements.
- **Support for Various Lineage Types**: Handle different types of lineage flows including:
    - **Data Flows**: Showing the movement of data between assets.
    - **Control Flows**: Representing the sequence of execution or control.
    - **Process Calls**: Linking processes to the sub-processes they invoke.
    - **Lineage Mappings**: General mapping of lineage between elements.
    - **Data Mappings**: Detailed mapping of data transformations, including formulas and queries.
    - **Ultimate Source and Destination**: Identifying the original source and final destination of data.

## Further information

- [Lineage Management Concept](/features/lineage-management/overview/)
- [Sample REST API requests](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/view-server-generic-services/lineage-linker/Egeria-api-lineage-linker.http)


---8<-- "snippets/abbr.md"






