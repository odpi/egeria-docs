<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Referenceable 

The term *Referenceable* is used to describe an open metadata element that represents something (person, place, data set, system, event, etc) that is significant enough *to be referred to*.  As such it needs a *identity*.  This is a unique name to accurately identify it.  

In open metadata, the unique name is called the qualified name (*qualifiedName* attribute).  However, many things that are described by open metadata have no natural unique name and so this qualified name has to be invented.  If this thing is also described in other systems, these systems will also have invented a unique name for it.

The attributes of a referenceable seek to capture all the unique names of the thing it represents so that information about it from different sources can be correlated and synchronized. 


## GUID verses qualified name

Every open metadata element has a unique identifier called its [GUID](/concepts/guid) that is assigned by the [open metadata repository](/concepts/open-metadata-repository) where it is first stored.  The GUID is of the form:

> 4908b6d2-0d5c-471d-af18-bc66a2b90320

This format is good for automated processes, but not for humans because it has no relationship to the element it represents.  The qualified name is more closely aligned to the element's content and so, while not necessarily memorable, it is more meaningful to people working with element.

For example, the qualified name often includes the type name, and maybe the identifier (see below) or display name.  In some situations, it may include a timestamp relating to when the thing it represents was created.

## The identifier

The *identifier* attribute is also part of a referenceable.  This is a unique name with the scope of its type.  For example, the name of a [governance zone](/concepts/governance-zone) is stored in the identifier attribute.

The identifier may come from an external system.  For example, the identifier for an employee may be their employment number.

## Other identifiers

[External identifier elements](/features/external-identifiers/overview) can be linked to the referenceable to capture other identifiers from external sources.  They support the situation where the mapping of an external identifier from one source is not a one-to-one mapping with the open metadata elements.

## Duplicate qualified names

Before creating a new referenceable element, Egeria will validate that the qualified name is unique.  It also checks for uniqueness if the qualified name is updated.  If the qualified name is not unique, an error is returned to the caller.

Despite this validation, it is possible that multiple metadata elements with the same qualified name could be present in the open metadata ecosystem. This is often because the elements with these names were created before the repositories were connected together in a [cohort](/concepts/cohort-member).

API calls that retrieve an element by its qualified name are only able to return a single element.  If more than one element with the same qualified name is retrieved from the repositories, an error is returned.  When this occurs, use a findXXXByName reuest that allows a list of elements to be returned.  Using the GUID from the returned elements, update the qualified names so they are unique.

If these elements also represent the same thing, use Egeria's [duplicate management](/features/duplicate-management/overview) to link them together so they will be treated as a single element.

???+ info "Further information"

    * The open metadata type definition for Referenceable is in [Model 0010](/types/0/0010-Base-Model).
    * [Managing external identifiers](/features/external-identifiers/overview) describes how to capture the external identifier for something (person, place, system, dataset, ...) that is used in another system and link it to the referenceable in open metadata.  This enables searches in open metadata using the identifiers from other systems, makingi t easier to synchronized information between systems.
    * The [generic handlers](/services/generic-handlers) module in the [metadata access servers](/concepts/metadata-access-server) is responsible for validating the uniqueness of a qualified name.
    
--8<-- "snippets/abbr.md"
