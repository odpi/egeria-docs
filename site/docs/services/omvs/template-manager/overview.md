<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# Template Manager API

The Template Manager API enables the caller to retrieve and refine the templates for use during cataloguing.
It supports the management of template definitions and their application to other metadata elements.

## Key Features

Key features of the service include:

* **Template Management**: Classifying metadata elements as templates or template substitutes, which allows them to be used as blueprints for creating new elements.
* **Templated Cataloguing**: Linking elements to the templates they were sourced from, maintaining the connection between the template and its instances.
* **Catalog Template Management**: Associating templates with broader contexts, such as projects, to make them easily discoverable for specific cataloguing tasks.

These capabilities help ensure consistency and quality in the metadata catalog by promoting the reuse of well-defined templates.

## Further information

* [Templated Cataloguing](/features/templated-cataloguing/overview/)

----
Sample REST API requests can be found in [Egeria-api-template-manager.http](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/view-services/template-manager/Egeria-api-template-manager.http).

---8<-- "snippets/abbr.md"






