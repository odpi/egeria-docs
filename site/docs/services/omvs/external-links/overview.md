<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# External Links API

The External Links API is a REST API that enables the caller to maintain and search for external identifiers and external references attached to open metadata elements.

### Key Features

* **External Reference Management**: Support for creating, retrieving, updating, and deleting external references (links to resources outside of the open metadata ecosystem).
* **External Identifier Management**: Support for adding, updating, and deleting external identifiers that link an open metadata element to its equivalent in an external system.
* **Relationship Management**:
    * Linking external references to any metadata element.
    * Managing specialized external references such as media references and cited document references.
    * Managing the synchronization status and confirmation of external identifiers.
* **Discovery and Search**: Finding external references and external identifiers by name, search strings, or through their unique identifiers (GUIDs).

### Further information

* [External Reference Concept](/concepts/external-reference/)
* [External Identifier Concept](/features/external-identifiers/overview)

----
Sample REST API requests can be found in [Egeria-api-external-links.http](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/view-server-generic-services/external-links/Egeria-api-external-links.http).

---8<-- "snippets/abbr.md"






