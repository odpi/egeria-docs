
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0615 Schema Extraction

Schema extraction creates a set of [*SchemaElement*](/types/5/0501-Schema-Elements) entities that represent how the data is structured in the digital resource. 

This is then either matched with an existing schema or a new schema is created (see [Area 5](/types/5)). This may be completely automated, or with stewards' assistance.

![UML](0615-Schema-Extraction.svg)

## SchemaAnalysis entity

The *SchemaAnalysis* entity identifies that the [survey action service](/concepts/survey-action-service) either created or verified the schema description for the analysed resource.  It identifies which schema it analysed both in its attributes and, typically using the [*AssociatedAnnotation*](/types/6/0610-Annotations) relationship to link to the root schema type.

--8<-- "snippets/abbr.md"