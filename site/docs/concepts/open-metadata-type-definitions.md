---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Open Metadata Type Definitions (TypeDefs)

TypeDefs define the characteristics of a particular type of an [open metadata instance/element](/concepts/open-metadata-instances).
There are three categories of TypeDefs (`TypeDefCategory`):

- *EntityDef*: the definition of a type of [entity](/concepts/open-metadata-instances)
- *RelationshipDef*: the definition of a type of [relationship](/concepts/open-metadata-instances)
- *ClassificationDef*: the definition of a type of [classification](/concepts/open-metadata-instances)

TypeDefs can inherit from other TypeDefs from the same category.  Open metadata supports single inheritance.

The basic description and the super type is stored in the standard header that all type definitions have.
TypeDefs also define the names and types of attributes for a metadata instance of that type.
Each attribute has a *TypeDefAttribute* definition that references an **AttributeTypeDef**
as its type.

The AttributeTypeDefs are the type definitions for attributes.
There are three categories of AttributeTypeDefs.

- *EnumDef*: the definition of an enumerated list of valid values.
- *CollectionDef*: the definition of a collection - such as an array of strings, or a map from string to object.
- *PrimitiveDef*: a primitive - such as a string, integer or date.

Type definitions for relationships and classifications also include information about the entities that they connect to.  ClassificationDefs include a list of EntityDefs that classifications of that type can attach to.  RelationshipDefs include details of the entity type that may be attached at End 1 of the relationship and, of course, the type of entity that can be attached at End 2.  The end 1 and end 2 entity types do not need to be the same. 

![Structure of TypeDefs](open-metadata-type-definitions.svg)

This is the JSON description of the *Referenceable* from the [Valid Metadata API](/services/omvs/valid-metadata/overview).

??? info "Referenceable type definition (EntityDef)"
    ```json
    {
      "class": "TypeDefResponse",
      "relatedHTTPCode": 200,
      "typeDef": {
        "class": "OpenMetadataEntityDef",
        "guid": "a32316b8-dc8c-48c5-b12b-71c1b2a080bf",
        "name": "Referenceable",
        "status": "ACTIVE_TYPEDEF",
        "version": 1,
        "versionName": "1.0",
        "category": "ENTITY_DEF",
        "superType": {
          "guid": "4e7761e8-3969-4627-8f40-bfe3cde85a1d",
          "name": "OpenMetadataRoot",
          "status": "ACTIVE_TYPEDEF"
        },
        "description": "An open metadata entity that has a unique identifier.",
        "descriptionGUID": "d9a26761-40ba-441d-9981-cc8f137fe379",
        "descriptionWiki": "https://egeria-project.org/types/0/0010-Base-Model/",
        "beanClassName": "ReferenceableProperties",
        "origin": "bce3b0a0-662a-4f87-b8dc-844078a11a6e",
        "createdBy": "ODPi Egeria",
        "createTime": "2020-01-01T13:42:11.090+00:00",
        "validElementStatusList": [
          "ACTIVE",
          "DELETED"
        ],
        "initialStatus": "ACTIVE",
        "attributeDefinitions": [
          {
            "attributeName": "qualifiedName",
            "attributeType": {
              "class": "OpenMetadataPrimitiveDef",
              "version": 1,
              "versionName": "1.0",
              "category": "PRIMITIVE",
              "guid": "b34a64b9-554a-42b1-8f8a-7d5c2339f9c4",
              "name": "string",
              "primitiveDefCategory": "OM_PRIMITIVE_TYPE_STRING"
            },
            "attributeStatus": "ACTIVE_ATTRIBUTE",
            "attributeDescription": "Unique name for the element.",
            "attributeDescriptionGUID": "e31e5b9b-0f96-42a9-8e67-0e3fc66ad305",
            "valuesMinCount": 1,
            "valuesMaxCount": 1,
            "attributeCardinality": "ONE_ONLY",
            "indexable": true,
            "unique": true
          },
          {
            "attributeName": "identifier",
            "attributeType": {
              "class": "OpenMetadataPrimitiveDef",
              "version": 1,
              "versionName": "1.0",
              "category": "PRIMITIVE",
              "guid": "b34a64b9-554a-42b1-8f8a-7d5c2339f9c4",
              "name": "string",
              "primitiveDefCategory": "OM_PRIMITIVE_TYPE_STRING"
            },
            "attributeStatus": "ACTIVE_ATTRIBUTE",
            "attributeDescription": "Identifier used in an external system.",
            "attributeDescriptionGUID": "2f831c53-0c71-4e03-92ed-20a899ed771f",
            "valuesMinCount": 0,
            "valuesMaxCount": 1,
            "attributeCardinality": "AT_MOST_ONE",
            "indexable": true,
            "unique": false
          },
          {
            "attributeName": "displayName",
            "attributeType": {
              "class": "OpenMetadataPrimitiveDef",
              "version": 1,
              "versionName": "1.0",
              "category": "PRIMITIVE",
              "guid": "b34a64b9-554a-42b1-8f8a-7d5c2339f9c4",
              "name": "string",
              "primitiveDefCategory": "OM_PRIMITIVE_TYPE_STRING"
            },
            "attributeStatus": "ACTIVE_ATTRIBUTE",
            "attributeDescription": "Display name of the element used for summary tables and titles.",
            "attributeDescriptionGUID": "a42ceece-6cd8-4c71-9920-e3c96df3c8bb",
            "valuesMinCount": 0,
            "valuesMaxCount": 1,
            "attributeCardinality": "AT_MOST_ONE",
            "indexable": true,
            "unique": false
          },
          {
            "attributeName": "description",
            "attributeType": {
              "class": "OpenMetadataPrimitiveDef",
              "version": 1,
              "versionName": "1.0",
              "category": "PRIMITIVE",
              "guid": "b34a64b9-554a-42b1-8f8a-7d5c2339f9c4",
              "name": "string",
              "primitiveDefCategory": "OM_PRIMITIVE_TYPE_STRING"
            },
            "attributeStatus": "ACTIVE_ATTRIBUTE",
            "attributeDescription": "Description of the element or associated resource in free-text.",
            "attributeDescriptionGUID": "ee09b6f9-e15b-40fb-9799-ef3b98c1de2c",
            "valuesMinCount": 0,
            "valuesMaxCount": 1,
            "attributeCardinality": "AT_MOST_ONE",
            "indexable": true,
            "unique": false
          },
          {
            "attributeName": "versionIdentifier",
            "attributeType": {
              "class": "OpenMetadataPrimitiveDef",
              "version": 1,
              "versionName": "1.0",
              "category": "PRIMITIVE",
              "guid": "b34a64b9-554a-42b1-8f8a-7d5c2339f9c4",
              "name": "string",
              "primitiveDefCategory": "OM_PRIMITIVE_TYPE_STRING"
            },
            "attributeStatus": "ACTIVE_ATTRIBUTE",
            "attributeDescription": "Version identifier to allow different versions of the same resource to appear in the catalog as separate assets.",
            "attributeDescriptionGUID": "6e765a3f-04c2-4eca-bd2d-519cae777c03",
            "valuesMinCount": 0,
            "valuesMaxCount": 1,
            "attributeCardinality": "AT_MOST_ONE",
            "indexable": true,
            "unique": false
          },
          {
            "attributeName": "category",
            "attributeType": {
              "class": "OpenMetadataPrimitiveDef",
              "version": 1,
              "versionName": "1.0",
              "category": "PRIMITIVE",
              "guid": "b34a64b9-554a-42b1-8f8a-7d5c2339f9c4",
              "name": "string",
              "primitiveDefCategory": "OM_PRIMITIVE_TYPE_STRING"
            },
            "attributeStatus": "ACTIVE_ATTRIBUTE",
            "attributeDescription": "Descriptive name of the concept that this element applies to.",
            "attributeDescriptionGUID": "385d7ca6-bcdd-43e4-925f-026a1043e37d",
            "valuesMinCount": 0,
            "valuesMaxCount": 1,
            "attributeCardinality": "AT_MOST_ONE",
            "indexable": true,
            "unique": false
          },
          {
            "attributeName": "url",
            "attributeType": {
              "class": "OpenMetadataPrimitiveDef",
              "version": 1,
              "versionName": "1.0",
              "category": "PRIMITIVE",
              "guid": "b34a64b9-554a-42b1-8f8a-7d5c2339f9c4",
              "name": "string",
              "primitiveDefCategory": "OM_PRIMITIVE_TYPE_STRING"
            },
            "attributeStatus": "ACTIVE_ATTRIBUTE",
            "attributeDescription": "Primary address where this external source can be accessed from.",
            "attributeDescriptionGUID": "604dbf10-335d-4132-8a32-c30fa9fec154",
            "valuesMinCount": 0,
            "valuesMaxCount": 1,
            "attributeCardinality": "AT_MOST_ONE",
            "indexable": true,
            "unique": false
          },
          {
            "attributeName": "additionalProperties",
            "attributeType": {
              "class": "OpenMetadataCollectionDef",
              "version": 1,
              "versionName": "1.0",
              "category": "COLLECTION",
              "guid": "005c7c14-ac84-4136-beed-959401b041f8",
              "name": "map<string,string>",
              "description": "A map from string to string.",
              "descriptionGUID": "f285d0ca-50ab-4564-b129-c7e3ba4e8545",
              "collectionDefCategory": "OM_COLLECTION_MAP",
              "argumentCount": 2,
              "argumentTypes": [
                "OM_PRIMITIVE_TYPE_STRING",
                "OM_PRIMITIVE_TYPE_STRING"
              ]
            },
            "attributeStatus": "ACTIVE_ATTRIBUTE",
            "attributeDescription": "Additional properties for the element.",
            "attributeDescriptionGUID": "534b5665-73d4-4bdc-b83b-1a8fed19dba3",
            "valuesMinCount": 0,
            "valuesMaxCount": 1,
            "attributeCardinality": "AT_MOST_ONE",
            "indexable": true,
            "unique": false
          }
        ]
      }
    }
    ```

If you compare it will the UML description of the type in model [0010 Basic Model](/types/0/0010-Base-Model) you will notice that the Valid Values API include all inherited attributes, whereas the UML version links to the element that it inherits from.

Next is an example of a RelationshipDef for the [SemanticAssignment](/types/3/0370-Semantic-Assignment) relationship.  Notice that a *Referenceable* entity is connected at end 1 and a [GlossaryTerm](/types/3/0330-Terms) is connected at end 2.

??? info "SemanticAssignment type definition (RelationshipDef)"
    ```json
    {
      "class": "TypeDefResponse",
      "relatedHTTPCode": 200,
      "typeDef": {
        "class": "OpenMetadataRelationshipDef",
        "guid": "e6670973-645f-441a-bec7-6f5570345b92",
        "name": "SemanticAssignment",
        "status": "ACTIVE_TYPEDEF",
        "version": 1,
        "versionName": "1.0",
        "category": "RELATIONSHIP_DEF",
        "description": "Links a glossary term to another element such as an asset or schema element to indicate that the data stored in the corresponding part of the digital resource has this meaning.",
        "descriptionGUID": "6b98085b-b70b-49cd-98e2-e87474d27e69",
        "descriptionWiki": "https://egeria-project.org/types/3/0370-Semantic-Assignment/",
        "beanClassName": "SemanticAssignmentProperties",
        "origin": "bce3b0a0-662a-4f87-b8dc-844078a11a6e",
        "createdBy": "ODPi Egeria",
        "createTime": "2020-01-01T13:42:11.090+00:00",
        "validElementStatusList": [
          "ACTIVE",
          "DELETED"
        ],
        "initialStatus": "ACTIVE",
        "attributeDefinitions": [
          {
            "attributeName": "termAssignmentStatus",
            "attributeType": {
              "class": "OpenMetadataEnumDef",
              "version": 1,
              "versionName": "1.0",
              "category": "ENUM_DEF",
              "guid": "c8fe36ac-369f-4799-af75-46b9c1343ab3",
              "name": "TermAssignmentStatus",
              "description": "Defines the provenance and confidence of a term assignment.",
              "descriptionGUID": "ae0313dd-921d-4a1f-a71c-b234e1b2e543",
              "elementDefs": [
                {
                  "ordinal": 0,
                  "value": "Discovered",
                  "description": "The term assignment was discovered by an automated process.",
                  "descriptionGUID": "6bfd3f33-e550-4575-a29f-7199f5865615"
                },
                {
                  "ordinal": 1,
                  "value": "Proposed",
                  "description": "The term assignment was proposed by a subject-matter expert.",
                  "descriptionGUID": "2c939678-7381-44ba-beec-f30791e0b560"
                },
                {
                  "ordinal": 2,
                  "value": "Imported",
                  "description": "The term assignment was imported from another metadata system.",
                  "descriptionGUID": "ac932f9e-a573-4c70-a49f-56830a5a535a"
                },
                {
                  "ordinal": 3,
                  "value": "Validated",
                  "description": "The term assignment has been validated and approved by a subject-matter expert.",
                  "descriptionGUID": "18b3d426-e406-4098-ba6a-bb1e42318b21"
                },
                {
                  "ordinal": 4,
                  "value": "Deprecated",
                  "description": "The term assignment should no longer be used.",
                  "descriptionGUID": "6234a509-6d96-4450-adaf-d97918ec8646"
                },
                {
                  "ordinal": 5,
                  "value": "Obsolete",
                  "description": "The term assignment must no longer be used.",
                  "descriptionGUID": "289ffbed-3fb7-4e6a-a4e1-8f11e83bd1ac"
                },
                {
                  "ordinal": 99,
                  "value": "Other",
                  "description": "The term assignment is in a locally defined state.",
                  "descriptionGUID": "74cfc2eb-4669-4780-a9b7-ca49d3661630"
                }
              ],
              "defaultValue": {
                "ordinal": 99
              }
            },
            "attributeStatus": "ACTIVE_ATTRIBUTE",
            "attributeDescription": "Defines the provenance and confidence of a term assignment.",
            "attributeDescriptionGUID": "d842dfdd-f080-4539-9a3c-eacdf0a03d07",
            "valuesMinCount": 0,
            "valuesMaxCount": 1,
            "attributeCardinality": "AT_MOST_ONE",
            "indexable": true,
            "unique": false
          },
          {
            "attributeName": "description",
            "attributeType": {
              "class": "OpenMetadataPrimitiveDef",
              "version": 1,
              "versionName": "1.0",
              "category": "PRIMITIVE",
              "guid": "b34a64b9-554a-42b1-8f8a-7d5c2339f9c4",
              "name": "string",
              "primitiveDefCategory": "OM_PRIMITIVE_TYPE_STRING"
            },
            "attributeStatus": "ACTIVE_ATTRIBUTE",
            "attributeDescription": "Description of the element or associated resource in free-text.",
            "attributeDescriptionGUID": "ee09b6f9-e15b-40fb-9799-ef3b98c1de2c",
            "valuesMinCount": 0,
            "valuesMaxCount": 1,
            "attributeCardinality": "AT_MOST_ONE",
            "indexable": true,
            "unique": false
          },
          {
            "attributeName": "expression",
            "attributeType": {
              "class": "OpenMetadataPrimitiveDef",
              "version": 1,
              "versionName": "1.0",
              "category": "PRIMITIVE",
              "guid": "b34a64b9-554a-42b1-8f8a-7d5c2339f9c4",
              "name": "string",
              "primitiveDefCategory": "OM_PRIMITIVE_TYPE_STRING"
            },
            "attributeStatus": "ACTIVE_ATTRIBUTE",
            "attributeDescription": "Expression used to create the annotation.",
            "attributeDescriptionGUID": "e130bc01-7c58-4799-8d8a-ae3ec659a064",
            "valuesMinCount": 0,
            "valuesMaxCount": 1,
            "attributeCardinality": "AT_MOST_ONE",
            "indexable": true,
            "unique": false
          },
          {
            "attributeName": "confidence",
            "attributeType": {
              "class": "OpenMetadataPrimitiveDef",
              "version": 1,
              "versionName": "1.0",
              "category": "PRIMITIVE",
              "guid": "7fc49104-fd3a-46c8-b6bf-f16b6074cd35",
              "name": "int",
              "primitiveDefCategory": "OM_PRIMITIVE_TYPE_INT"
            },
            "attributeStatus": "ACTIVE_ATTRIBUTE",
            "attributeDescription": "Level of confidence in the correctness of the element. 0=unknown; 1=low confidence; 100=total confidence.",
            "attributeDescriptionGUID": "26dd007a-cff3-45e7-963d-2a753c2b7000",
            "valuesMinCount": 0,
            "valuesMaxCount": 1,
            "attributeCardinality": "AT_MOST_ONE",
            "indexable": true,
            "unique": false
          },
          {
            "attributeName": "steward",
            "attributeType": {
              "class": "OpenMetadataPrimitiveDef",
              "version": 1,
              "versionName": "1.0",
              "category": "PRIMITIVE",
              "guid": "b34a64b9-554a-42b1-8f8a-7d5c2339f9c4",
              "name": "string",
              "primitiveDefCategory": "OM_PRIMITIVE_TYPE_STRING"
            },
            "attributeStatus": "ACTIVE_ATTRIBUTE",
            "attributeDescription": "Unique identifier for the steward performing the action.",
            "attributeDescriptionGUID": "6777fa1e-3289-4896-a032-1097b4ad78b2",
            "valuesMinCount": 0,
            "valuesMaxCount": 1,
            "attributeCardinality": "AT_MOST_ONE",
            "indexable": true,
            "unique": false
          },
          {
            "attributeName": "stewardTypeName",
            "attributeType": {
              "class": "OpenMetadataPrimitiveDef",
              "version": 1,
              "versionName": "1.0",
              "category": "PRIMITIVE",
              "guid": "b34a64b9-554a-42b1-8f8a-7d5c2339f9c4",
              "name": "string",
              "primitiveDefCategory": "OM_PRIMITIVE_TYPE_STRING"
            },
            "attributeStatus": "ACTIVE_ATTRIBUTE",
            "attributeDescription": "Type name of the Actor entity identifying the steward.",
            "attributeDescriptionGUID": "b4c4637d-b196-4268-86a2-c6daf444dd7d",
            "valuesMinCount": 0,
            "valuesMaxCount": 1,
            "attributeCardinality": "AT_MOST_ONE",
            "indexable": true,
            "unique": false
          },
          {
            "attributeName": "stewardPropertyName",
            "attributeType": {
              "class": "OpenMetadataPrimitiveDef",
              "version": 1,
              "versionName": "1.0",
              "category": "PRIMITIVE",
              "guid": "b34a64b9-554a-42b1-8f8a-7d5c2339f9c4",
              "name": "string",
              "primitiveDefCategory": "OM_PRIMITIVE_TYPE_STRING"
            },
            "attributeStatus": "ACTIVE_ATTRIBUTE",
            "attributeDescription": "Property name for the steward's unique identifier (typically guid or qualifiedName).",
            "attributeDescriptionGUID": "b9e55ebe-43fb-4eb0-8485-6ef22e07f0a8",
            "valuesMinCount": 0,
            "valuesMaxCount": 1,
            "attributeCardinality": "AT_MOST_ONE",
            "indexable": true,
            "unique": false
          },
          {
            "attributeName": "source",
            "attributeType": {
              "class": "OpenMetadataPrimitiveDef",
              "version": 1,
              "versionName": "1.0",
              "category": "PRIMITIVE",
              "guid": "b34a64b9-554a-42b1-8f8a-7d5c2339f9c4",
              "name": "string",
              "primitiveDefCategory": "OM_PRIMITIVE_TYPE_STRING"
            },
            "attributeStatus": "ACTIVE_ATTRIBUTE",
            "attributeDescription": "Details of the organization, person or process that created the element, or provided the information used to create the element.",
            "attributeDescriptionGUID": "9c40c4e3-1d6d-45fd-8df0-f1a2e09db636",
            "valuesMinCount": 0,
            "valuesMaxCount": 1,
            "attributeCardinality": "AT_MOST_ONE",
            "indexable": true,
            "unique": false
          },
          {
            "attributeName": "notes",
            "attributeType": {
              "class": "OpenMetadataPrimitiveDef",
              "version": 1,
              "versionName": "1.0",
              "category": "PRIMITIVE",
              "guid": "b34a64b9-554a-42b1-8f8a-7d5c2339f9c4",
              "name": "string",
              "primitiveDefCategory": "OM_PRIMITIVE_TYPE_STRING"
            },
            "attributeStatus": "ACTIVE_ATTRIBUTE",
            "attributeDescription": "Notes on why decision were made relating to this element, and other useful information.",
            "attributeDescriptionGUID": "577281c3-82f8-4c1d-ad95-04ef5919e57c",
            "valuesMinCount": 0,
            "valuesMaxCount": 1,
            "attributeCardinality": "AT_MOST_ONE",
            "indexable": true,
            "unique": false
          }
        ],
        "propagationRule": "NONE",
        "endDef1": {
          "entityType": {
            "guid": "a32316b8-dc8c-48c5-b12b-71c1b2a080bf",
            "name": "Referenceable",
            "status": "ACTIVE_TYPEDEF"
          },
          "attributeName": "assignedDataAssetElements",
          "attributeDescription": "Elements identified as managing data that has the same meaning as this glossary term.",
          "attributeCardinality": "ANY_NUMBER"
        },
        "endDef2": {
          "entityType": {
            "guid": "0db3e6ec-f5ef-4d75-ae38-b7ee6fd6ec0a",
            "name": "GlossaryTerm",
            "status": "ACTIVE_TYPEDEF"
          },
          "attributeName": "meaning",
          "attributeDescription": "Semantic definition for this element.",
          "attributeCardinality": "ANY_NUMBER"
        },
        "multiLink": false
      }
    }
    ```            

Finally, this is the definition of the [Anchors](/types/0/0010-Base-Model) classification.  This classification connects to [OpenMetadataRoot](/types/0/0010-Base-Model), which effectively means it can be added to any type of entity.

??? info "Anchors type definition (ClassificationDef)"
    ```json
    {
      "class": "TypeDefResponse",
      "relatedHTTPCode": 200,
      "typeDef": {
        "class": "OpenMetadataClassificationDef",
        "guid": "aa44f302-2e43-4669-a1e7-edaae414fc6e",
        "name": "Anchors",
        "status": "ACTIVE_TYPEDEF",
        "version": 1,
        "versionName": "1.0",
        "category": "CLASSIFICATION_DEF",
        "description": "Identifies the anchor entity for an element that is part of a large composite object such as an asset.",
        "descriptionGUID": "09708101-5b38-4c3c-b1e5-983f9c731e5c",
        "descriptionWiki": "https://egeria-project.org/types/0/0010-Base-Model/",
        "beanClassName": "AnchorsProperties",
        "origin": "bce3b0a0-662a-4f87-b8dc-844078a11a6e",
        "createdBy": "ODPi Egeria",
        "createTime": "2020-04-30T15:42:46.992+00:00",
        "validElementStatusList": [
          "ACTIVE",
          "DELETED"
        ],
        "initialStatus": "ACTIVE",
        "attributeDefinitions": [
          {
            "attributeName": "anchorGUID",
            "attributeType": {
              "class": "OpenMetadataPrimitiveDef",
              "version": 1,
              "versionName": "1.0",
              "category": "PRIMITIVE",
              "guid": "b34a64b9-554a-42b1-8f8a-7d5c2339f9c4",
              "name": "string",
              "primitiveDefCategory": "OM_PRIMITIVE_TYPE_STRING"
            },
            "attributeStatus": "ACTIVE_ATTRIBUTE",
            "attributeDescription": "The unique identifier of the referenceable that this element is directly or indirectly anchored to.",
            "attributeDescriptionGUID": "e7de4efc-6fa4-4942-97eb-e9b5be701875",
            "valuesMinCount": 0,
            "valuesMaxCount": 1,
            "attributeCardinality": "AT_MOST_ONE",
            "indexable": true,
            "unique": false
          },
          {
            "attributeName": "anchorTypeName",
            "attributeType": {
              "class": "OpenMetadataPrimitiveDef",
              "version": 1,
              "versionName": "1.0",
              "category": "PRIMITIVE",
              "guid": "b34a64b9-554a-42b1-8f8a-7d5c2339f9c4",
              "name": "string",
              "primitiveDefCategory": "OM_PRIMITIVE_TYPE_STRING"
            },
            "attributeStatus": "ACTIVE_ATTRIBUTE",
            "attributeDescription": "Unique name of the type of the anchor.",
            "attributeDescriptionGUID": "605c9dd5-fa79-4457-b299-9169c5567f97",
            "valuesMinCount": 0,
            "valuesMaxCount": 1,
            "attributeCardinality": "AT_MOST_ONE",
            "indexable": true,
            "unique": false
          },
          {
            "attributeName": "anchorDomainName",
            "attributeType": {
              "class": "OpenMetadataPrimitiveDef",
              "version": 1,
              "versionName": "1.0",
              "category": "PRIMITIVE",
              "guid": "b34a64b9-554a-42b1-8f8a-7d5c2339f9c4",
              "name": "string",
              "primitiveDefCategory": "OM_PRIMITIVE_TYPE_STRING"
            },
            "attributeStatus": "ACTIVE_ATTRIBUTE",
            "attributeDescription": "Unique name of the domain of the anchor.  This is an Open Metadata Type Name that either directly inherits from OpenMetadataRoot or Referenceable.",
            "attributeDescriptionGUID": "00ba532f-792f-4b78-8940-b5a9fd72f854",
            "valuesMinCount": 0,
            "valuesMaxCount": 1,
            "attributeCardinality": "AT_MOST_ONE",
            "indexable": true,
            "unique": false
          },
          {
            "attributeName": "anchorScopeGUID",
            "attributeType": {
              "class": "OpenMetadataPrimitiveDef",
              "version": 1,
              "versionName": "1.0",
              "category": "PRIMITIVE",
              "guid": "b34a64b9-554a-42b1-8f8a-7d5c2339f9c4",
              "name": "string",
              "primitiveDefCategory": "OM_PRIMITIVE_TYPE_STRING"
            },
            "attributeStatus": "ACTIVE_ATTRIBUTE",
            "attributeDescription": "Unique identifier of the scope of the anchor.  This is an Open Metadata GUID of an element that represents a scope/ownership of an anchor element.  It is used to restrict searches.",
            "attributeDescriptionGUID": "65afae9b-54d5-440f-b955-6ebe9c0eba21",
            "valuesMinCount": 0,
            "valuesMaxCount": 1,
            "attributeCardinality": "AT_MOST_ONE",
            "indexable": true,
            "unique": false
          }
        ],
        "validEntityDefs": [
          {
            "guid": "4e7761e8-3969-4627-8f40-bfe3cde85a1d",
            "name": "OpenMetadataRoot",
            "status": "ACTIVE_TYPEDEF"
          }
        ],
        "propagatable": true
      }
    }
    ```





--8<-- "snippets/abbr.md"