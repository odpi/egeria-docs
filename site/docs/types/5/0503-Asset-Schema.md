<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0503 Asset/Port Schema

Model 0503 shows the relationship between an [Asset](/types/0/0010-Base-Model) or [Port](/types/2/0217-Ports) and a [SchemaType](/types/5/0501-Schema-Elements).

When an [asset](/concepts/asset) is linked to a [schema type](/concepts/schema) it means that the schema type describes the structure of the data stored in the [resource](/concepts/resource) described by the asset.  Typically, the schema type that is attached to the asset is either a [RootSchemaType](/types/5/0530-Tabular-Schemas), an [ExternalSchemaType](types/5/0507-External-Schema-Type) or a [SchemaTypeChoice](/types/5/0501-Schema-Elements).


![UML](0503-Asset-Schema.svg)

## Schema relationship

The *Schema* relationship links an element to the schema type that describes the structure of the data associated with the digital resource that the linked element represents.

## RootSchemaType entity

*RootSchemaType* is an informational type in that it does not add new attributes to the type system.  Instead, it provides a marker to indicate that types that inherit from it are typically the root of a schema definition.  It is this element that connects to [assets](/types/0503-Asset-Schema) and [ports](/types/5/0520-Process-Schemas).

The attached schema type is not shared between different assets because information about a data field in a specific asset's resource is attached to the appropriate [schema attribute](/types/5/0505-Schema-Attributes) element.

If you are cataloging multiple assets with the same data structure, you can:

* Use a [template](/features/templated-cataloging/overview) which will copy the schema structure from the template asset to the new asset.  
* Attach an [*ExternalSchemaType*](/types/5/0507-External-Schema-Type) to the asset and link it to the common schema type using the *LinkedExternalSchemaType* relationship.

--8<-- "snippets/abbr.md"