<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0565 Design Models

Design models are used during the development of data structures and their related software to provide templates and abstractions of the implementation(s).

Representations of design models are supported in the open metadata types to support implementation generation and to show the lineage of software components from their design to implementation.

Model 0565 shows the definition of a generic design model and a design model element within it.

![UML](0565-Design-Models.svg)

## DesignModel entity

The *DesignModel* entity describes a [Collection](/types/0/0021-Collections) of *DesignModelElement* entities.  The *DesignModelElement* entities are linked to one or more *DesignModel* elements using the [CollectionMembership](/types/0/0021-Collections) relationship.

* *authors* allow one or more authors of the model to be acknowledged.
* *userDefinedStatus* is used to define your own statuses for your model elements.

There are specializations of *DesignModel* for describing different situations.

* [ConceptModel](/types/5/0571-Concept-Models) described a collection of modelled concepts.
* [SolutionBlueprint](/types/7/0740-Solution-Blueprints) described a collection of components that make up a solution.

## DesignModelElement entity

The *DesignModelElement* describes an element in one or more models.

* *canonicalName* allows a name to be defined that can be used for code generation.  Each word in the name is capitalized and space separated.  For example "Customer Name".
* *authors* allow one or more authors of the model element to be acknowledged.  This is useful if the work on the model is divided and different authors are responsible for different parts of the model.
* *userDefinedStatus* is used to define your own statuses for your models.

The subtype of the element defines the type of object it is describing.

* [ConceptModelElement](/types/5/0571-Concept-Models) described a collection of modelled concepts.
* [SolutionComponent](/types/7/0730-Solution-Components) described a collection of components that make up a solution.

--8<-- "snippets/abbr.md"