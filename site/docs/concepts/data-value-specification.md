<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Data Value Specification

A *data value specification* describes the values that a data field is expected to hold.  It sits between the structural description of data - which says a field is a string of 20 characters - and the meaning of the data, which is captured in a [glossary term](/concepts/glossary-term).  The data value specification says what a valid value actually looks like.

This is the information that automation needs.  A field typed as *string* tells a quality process nothing; a field assigned the *Date of Birth* specification tells it the format to expect, the plausible range, and which quality rules to run.

## Two specializations

Egeria defines two specializations of data value specification, each answering a different question:

* A [data class](/concepts/data-class) describes the *logical type* of the values in a field - what kind of thing each individual value is.
* A [data grain](/concepts/data-grain) describes the *level of detail* that a set of values represents - for example, whether a row of sales figures is one transaction, one day for one store, or one month for one region.

## Properties

* *specification* - a description of the matching data values.  This may be machine-readable or human-readable, so a rule can be stated explicitly in a rules language, or referred to by name.
* *specificationDetails* - additional values used by the specification, such as substitution values to insert into the specification string.
* *matchPropertyNames* - the property names that are filled out in this specification, helping automation work out which values it supports.
* *matchThreshold* - the percentage of values in a data resource that must match for the resource to be assigned this specification.
* *dataType* - the data type used to encode this kind of value.
* *units* - the units of measure for the values.
* *absoluteUncertainty* and *relativeUncertainty* - the uncertainty in the values.
* *namespacePath* - the namespace the specification is organized under.

## Hierarchies

The *DataValueHierarchy* relationship organizes data value specifications from the general to the specific: *date* at the top, with *date of birth* beneath it.  Automated discovery and stewardship can then work down the hierarchy to the most specific specification that fits a field, and run the most appropriate quality rules for it.

The same hierarchy is used in reverse when generating software artifacts such as OpenAPI specifications, DDL scripts or JSON schema.  If a field's specification has no equivalent in the target language, the generator navigates up the hierarchy to a more general specification that does.

## Assignment

A [survey action service](/concepts/survey-action-service) proposes data value assignments, recording them as annotations in its [survey report](/concepts/survey-report).  Subsequent stewardship - automated or with human assistance - confirms the assignment using the *DataValueAssignment* relationship.  The *DataValueAssignmentStatus* enumeration records how far that has got: *DISCOVERED*, *PROPOSED*, *IMPORTED*, *VALIDATED*, *DEPRECATED*, *OBSOLETE* or *OTHER*.

The *DataValueDefinition* relationship augments a [data structure](/concepts/data-structure) or [data field](/concepts/data-field) with its data value specification, so that a [data specification](/concepts/data-specification) carries the value-level requirements alongside the structural ones.

???+ info "Additional information"
    * The *DataValueSpecification* type and its relationships are described in [Model 0540 Data Value Specification](/types/5/0540-Data-Value-Specification).
    * The [Data Designer API](/services/omvs/data-designer/overview) provides the operations for defining data value specifications and attaching them to data structures and fields.

--8<-- "snippets/abbr.md"
