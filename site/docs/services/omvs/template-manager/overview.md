---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# Template Manager API

The Template Manager API is a REST API designed to support user interfaces (UIs) that support the management of [templates](/features/templated-cataloguing/overview) that are used when creating new metadata.

## The Template classification

## Specification properties

[Specification properties](/concepts/specification) are attached to templates to guide people when using a template.  They define which values need to be supplied in order to use the template successfully.

There are two types of specification properties:

* *replacementAttribute* - Name of attribute that should be provided when using the attached template.  Replacement attributes map to the root entity of the template, or, the first occurrence of the attribute in attached relationships, classifications or entities.
* *placeholderProperty* - Placeholder names are located through the attribute values found in a template.  They are identified with double braces, for example {{variableName}}.  The value supplied is substituted for the placeholder variable.

They can be attached to a template, and maintained through the [Valid Metadata API](/services/omvs/valid-metadata/overview).

## Linking templates to technology types

The [Automated Curation API](/services/omvs/automated-curation/overview) supports the retrieval of the templates and connectors that support a particular type of technology.  It uses the valid metadata values for [] 

---8<-- "snippets/abbr.md"






