
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# Schema Maker API

The Schema Maker API provides user interfaces supporting the creation and editing of schema types and schema attributes.

### Key Features

*   **Schema Type Management**: Full lifecycle management of schema types, which define the structure and data types of metadata elements.
*   **Schema Attribute Management**: Capabilities for creating and maintaining schema attributes that represent individual fields or columns within a schema type.
*   **Templated Creation**: Support for creating new schema types and attributes using existing elements as templates to ensure consistency and speed up the design process.
*   **Schema Exploration**: Tools for searching and retrieving schema types and attributes by name, search strings, or unique identifiers (GUIDs).
*   **Process Schemas**: Linking an element, such as a process, to the schema types that describe the kinds of data value used to initialize or configure it.  The [*SupportedVariableType*](/types/5/0520-Process-Schemas/#supportedvariabletype-relationship) relationship records the position in which a value of that type is passed and how many values are allowed (*linkSupportedVariableType* / *detachSupportedVariableType*).  The data values themselves are described through the [Data Engineer API](/services/omvs/data-engineer/overview).

### Further information

*   [Schema Concept](/concepts/schema)

Sample REST API requests are found in [Egeria-api-schema-maker.http](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/view-server-generic-services/schema-maker/Egeria-api-schema-maker.http)

---8<-- "snippets/abbr.md"






