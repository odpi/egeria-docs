---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Modelling APIs


Figure 1 shows the types of metadata that describes an API..

![Figure 1](api-model.svg)
> **Figure 1:** API metadata

The structure of an API specification consist of a number of 
[APIOperation](/types/5/0536-API-Schemas)s
which in turn have optional
[APIParameterList](/types/5/0536-API-Schemas)s
for the header, request and response.
The details of these payloads are described using
[SchemaAttributes and SchemaTypes](/concepts/schema).

Figure 2 shows the open metadata types used to represent the metadata created through this service.

![Figure 2](api-open-metadata-types.svg)
> **Figure 2:** API open metadata types

If an APIManager is defined, any API created is automatically linked to it using the
[ServerAssetUse](/types/0/0045-Servers-and-Assets)
relationship.
When an APIOperation is created for the API,
the service automatically inserts the
[Schema](/types/5/0503-Asset-Schema) relationship,
[APISchemaType](/types/5/0536-API-Schemas) entity and
[APIOperations](/types/5/0536-API-Schemas) relationship
in between the DeployedAPI entity and the APIOperation entity.

Any schema attributes created through this interface will use the
[APIParameter](/types/5/0536-API-Schemas) subtype
to allow for find requests that only return schema information for APIs.  The schema attributes also use
the [TypeEmbeddedAttribute](/types/5/0505-Schema-Attributes)
classification [method for defining the schema type](/concepts/schema).


---8<-- "snippets/abbr.md"