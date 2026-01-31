<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/types/open-metadata-types-intro.md"

## Understanding the models

![Guide to reading the open metadata type models](model-guidance.svg)

The diagram above shows a few fragments from the models. Each of the UML classes represents an open metadata type. The stereotype on the UML class in the double angle brackets of *entity*, *relationship* and *classification* defines the [category of the type](/introduction/key-concepts/#metadata-instances). The line between entities with the big arrow head means "inheritance". A type points to its supertype.

???+ example "The example on the left comes from model [0010](/types/0/0010-Base-Model)"
    It shows that `Asset` inherits from `Referenceable` which inherits from `OpenMetadataRoot`. This means that `Asset` is a subtype of `Referenceable`, which is a subtype of `OpenMetadataRoot`. Alternatively, `OpenMetadataRoot` is the supertype of `Referenceable`, which is a supertype of `Asset`. This inheritance identifies which attributes (instance properties) are valid for an instance of a particular type since it is the aggregation of the attributes defined explicitly for the type and all of its supertypes.

    For example, `Asset` has two attributes defined: `name` and `description`. It also supports `qualifiedName` and `additionalProperties` because they are inherited from `Referenceable`. `OpenMetadataRoot` does not have any attributes defined so `Asset` gets nothing from it.

???+ example "The example on the right comes from model [0011](/types/0/0011-Templates)"
    It shows the classification called `Template` that can be connected to a `Referenceable`. Since `Referenceable` is already defined in model 0010, it is shown without the white box where the attributes are show (called the "attribute container" in UML parlance).

    `SourcedFrom` is a relationship that connects two instances of `Referenceable` and any of its subtypes. This means `SourcedFrom` could connect two instances of type `Asset` together. The types of the instances connected do not need to be the same - `SourcedFrom` could connect a `Referenceable` instance with an `Asset` instance.

    The thickness of the relationship line indicates which relationships are [*uni-link* or *multi-link*](/concepts/uni-multi-link).  A thin line indicates uni-link.  Multi-link is represented by a thick line.

The UML model diagrams show the currently active types. Some types and attributes have been deprecated and these have been removed from the model diagrams. However, there is a description of the deprecated types and which of the active types to use instead. Although the deprecated types can be used (for backwards compatibility) it is always preferable to use the latest types since they are typically more efficient and more consistent than their predecessors.

## Attribute type definitions

The properties defined on each open metadata type must be a defined attribute type.  There are three choices:

* Primitives (described by *PrimitiveDefs*).
* Collections such as arrays and maps (described by *CollectionDefs*).
* Enumerations - that is lists of valid values (described by *EnumDefs*).

### Primitives

The primitive defined in the open metadata types are:

- `object` 
- `boolean`
- `byte`
- `char`
- `short`
- `int`
- `long`
- `float`
- `double`
- `biginteger`
- `bigdecimal`
- `string`
- `date`

### Collections

The collections defined in the opn metadata types are:

- `map<string,string>`
- `map<string,boolean>`
- `map<string,int>`
- `map<string,long>`
- `map<string,object>`
- `array<string>`
- `array<int>`

### Enumerations

The enumerations are defined with the [open metadata types for entities, relationships and classifications](#open-metadata-subject-areas).


--8<-- "snippets/abbr.md"
