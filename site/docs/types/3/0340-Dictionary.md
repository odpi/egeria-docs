<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0340 Dictionary

The dictionary model adds some basic term classification used to show how particular terms are used.

![UML](0340-Dictionary.svg)

## ActivityDescription

*ActivityDescription* is a classification used to indicate that the term describes a verb, or an activity.

Most term definitions are nouns, they describe concepts or things.
However, it is useful to be able to define the assets of particular activities in the glossary.
The ActivityDescription classification highlights when a term describes such an activity.

ActivityDescription has a single property called `type` which is an enumeration called *ActivityType* with the following value:
    
* OPERATION - describes a function or API call
* ACTION - describes a governance action that results from evaluating governance rules.
* TASK - describes a task performed by a person.
* PROCESS - describes a process, which is a series of steps that are performed in a defined order.
* PROJECT - describes a type of project.
* OTHER - describes some other type of activity
  
## AbstractConcept classification

*AbstractConcept* is a classification that means that the term describes an abstract concept.

## DataValue classification

*DataValue*  is a classification that means that the glossary term describes a valid value for a data item.

## DataFieldValues classification

The *DataFieldValues* describe the characteristics of a collection of data values located in a particular data field (such as a [RelationalColumn](/types/5/0534-Relational-Schemas)).  It is typically attached to a [*GlossaryTerm*](/types/3/03303-Terms) entity or a [*SchemaAttribute*](/types/5/0505-Schema-Attributes) entity.   For example:

* It can be attached to a glossary term to indicate that the glossary term describes a data field and the characteristics of this type of data.  This can be used to guide a steward, or an automated process (such as an [open discovery service](/concepts/open-discovery-service)) to create a candidate mappings from a [SchemaAttribute](/types/5/0505-Schema-Attributes) or [DataField](/types/6/0615-Schema-Extraction) to the glossary term.
* It can be attached to a schema attribute to describe the properties of the data stored in the location that the schema attribute represents.

Its attributes are:

* *defaultValue* - Value that is used when an instance of the data field is created.
* *sampleValues* - List of sample values for the data field.
* *dataPatterns* - Regular expressions that characterize the values in the data field.
* *namePatterns* - Regular expressions that characterize the name of the data field.


--8<-- "snippets/abbr.md"