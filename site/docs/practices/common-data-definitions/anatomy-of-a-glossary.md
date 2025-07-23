<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Anatomy of a glossary

A *glossary* is a collection of semantic definitions, typically focused on defining the meaning of data. An organization may have multiple glossaries that represent different collections of definitions, each reflecting a scope of use or a source of the definitions.

Each glossary defined should have a well-defined content and an owner, who is responsible for ensuring that the contributed content meets the needs of its consumers.

Figure 1 shows the typical content of a glossary.

![Figure 1](glossary-structure.svg)
> Figure 1: Elements within a glossary

A *glossary term* describes a single concept.  The *glossary categories* are like folders to organize the glossary terms. Glossary terms that are related to one another can be linked together with *term relationships* .  There are different types of term relationships that help to pin down exactly how the glossary terms are related.  Finally there are *classifications* that can be linked to the glossary itself, the glossary categories or the glossary terms. The classification provide more information about the kind of element it is connected to, or its intended use.


## Inside a glossary term

A glossary term is a definition of the meaning of a concept, object or activity.  At a minimum glossary its has a name - this is the concept it describes, and a short description that explains at a high level what this concept means.   This short description should distinguish it from other terms.

For some glossaries, this may be all that you need.  However, if this is an important term and the consumers of it will want to know much more, then the glossary term can be built out to include a more detailed description and supplementary information such as:

* links to further information
* images of the concept
* descriptions of its usage
* examples of its use.

![Figure 2](anatomy-of-a-glossary-term.svg)
> Figure 2: Contents of a glossary term

The glossary term may then be organized into one or more [collections](/concepts/collection), classified and linked to related terms.

## Glossary term relationships

Glossary terms can be linked together in pairs to show that they are related in some way.

![Figure 4](glossary-term-relationships.svg)
> Figure 4: Glossary term relationships

The relationships between glossary terms are divided into two groups:

* Relationships that show how the meanings of terms are related:
  
    * *RelatedTerm* is a relationship used to say that the linked glossary term may also be of interest. It is like a "see also" link in a dictionary.
    * *Synonym* is a relationship between glossary terms that have the same, or a very similar meaning.
    * *Antonym* is a relationship between glossary terms that have the opposite (or near opposite) meaning.
    * *PreferredTerm* is a relationship that indicates that one term should be used in place of the other term linked by the relationship.
    * *ReplacementTerm* is a relationship that indicates that one term must be used instead of the other. This is stronger version of the PreferredTerm.
    * *Translation* is a relationship that defines that the linked terms represent the same meaning, but each are written in a different language. Hence one is a translation of the other. The language of each term is defined in the Glossary that owns the term.
    * *IsARelationship* is a relationship that defines that the one term is a more generic term than the other term. For example, this relationship would be used to say that "Cat" IsA "Animal".
    * *ValidValue* is a relationship that defines that the one term represents a value that than the other term can be set to. For example, this relationship would be used to say that "France" is a valid value for "Country".

* Relationships that show how terms are typically used together:
  
    * *UsedInContext* links a term to another term that describes a context.  This helps to distinguish between terms that have the same name but different meanings depending on the context.
   
## Glossary classifications

The contents of a glossary can be further described using classifications. These are descriptions that tell the consumer more about how the glossary is defines and used.

![Figure 5](glossary-classifications.svg)
> Figure 5: Glossary classifications

There are different types of classifications for the glossary itself, each glossary category and each glossary term.

### Classifications for a glossary

A glossary may be classified to describe the way its content should be used.

* *Taxonomy* means that the same term is not present in more than one of its categories.  This is used in glossaries that are designed to provide an organizing structure for other types of information, such as a document library.

* *CanonicalVocabulary* means the glossary only includes terms that have a unique name.  Thus there is only one definition for any concept.

* *EditingGlossary* means that the glossary contains a collection of glossary terms and categories that are in the process of being edited.
* 
* *StagingGlossary* means that the glossary contains a collection of glossary terms and categories that are in the process of being reviewed ready for publishing.

### Classifications for a term

* *ActivityDescription* is a classification used to indicate that the term describes a verb, or an activity. Most term definitions are nouns, they describe concepts or things. However, it is useful to be able to define the meanings of particular activities in the glossary. The ActivityDescription classification highlights when a term describes such an activity.  This classification can be further refined with a specific activity type:

    - OPERATION - describes a function or API call
    - ACTION - describes a governance action that results from evaluating governance rules.
    - TASK - describes a task performed by a person.
    - PROCESS - describes a process, which is a series of steps that are performed in a defined order.
    - PROJECT - describes a type of project.
    - OTHER - describes some other type of activity
  
* *AbstractConcept* means that the term describes an abstract concept.
* *DataValue* means that the glossary term describes a valid value for a data item.
* *ContextDefinition* indicates that the term describes a context.  Contexts define where a specific definition is used.


!!! education "Further information"
    * [Defining a glossary example](/practices/coco-pharmaceuticals/scenarios/defining-a-glossary/overview)
    * [Open metadata types for a glossary](/types/3/overview)

--8<-- "snippets/abbr.md"