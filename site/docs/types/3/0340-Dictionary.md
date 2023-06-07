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
  
## AbstractConcept

*AbstractConcept* is a classification that means that the term describes an abstract concept.

## DataValue

*DataValue*  is a classification that means that the glossary term describes a valid value for a data item.


--8<-- "snippets/abbr.md"