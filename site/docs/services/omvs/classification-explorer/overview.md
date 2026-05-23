<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# Classification Explorer API

The Classification Explorer API is a REST API designed to back user interfaces (UIs) that enables the caller to issue queries to understand how metadata elements are linked and classified.
It provides a flexible way to explore the metadata ecosystem, focusing on how elements are categorized and interconnected.

## Key features

- **Classification Management**: Support for managing various governance classifications such as impact, confidence, criticality, confidentiality, and retention.
- **Relationship Management**: Capabilities for linking elements through semantic assignments, scopes, resource lists, and more.
- **Metadata Exploration**: Tools for finding elements by type, unique name, property values, or specific classifications.
- **Governance and Security**: Managing security tags, ownership, and governance expectations/measurements.
- **Duplicate Management**: Identifying and linking peer or consolidated duplicates.
- **Search and Keywords**: Attaching and managing search keywords for enhanced discoverability.

## Further information

* [Setting up your governance program](/guides/planning/governance-program/overview/)


Sample REST API requests: [Egeria-api-classification-explorer.http](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/view-server-generic-services/classification-explorer/Egeria-api-classification-explorer.http)


---8<-- "snippets/abbr.md"






