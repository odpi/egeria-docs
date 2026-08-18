<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Valid Value Definition

A *valid value definition* stores a single authoritative value that data - or metadata - is allowed to take.  It is the building block of Egeria's [reference data management](/features/reference-data-management/overview).

Most systems store coded values: a country is held as `GB`, an order status as `03`, a department as a four-digit number.  Each system tends to invent its own codes, and the meaning of those codes lives in a code table somewhere - or in someone's head.  A valid value definition brings that code table into open metadata, where it can be governed, shared and used to drive the systems that depend on it.

## Properties

In addition to the properties it inherits as a referenceable, a valid value definition records:

* *preferredValue* - the actual value to use.
* *dataType* - the type of value this valid value represents.
* *usage* - the intended use of the value.
* *scope* - the scope within which the value is valid.
* *ordinal* - an integer used to sequence the values within a set.
* *isCaseSensitive* - whether the value is case sensitive.
* *namespacePath* - the root of the properties path name, where one applies.

## Organizing valid values

Valid value definitions are gathered into sets using the *ValidValueMember* relationship.  Because a set can be nested inside another set, valid values form a hierarchy - which is how taxonomies and multi-level code tables are represented.

Several specializations cover the different jobs valid values do:

* **ReferenceDataValue** - a single code value from a business code table, with its associated properties.  **ReferenceDataSet** represents the top of such a hierarchy.
* **SpecificationPropertyValue** - the [specification](/concepts/specification) of a configurable property, such as the properties a connector or [catalog template](/concepts/catalog-template) expects.
* **ValidMetadataValue** - a valid value for an open metadata property, allowing open metadata itself to be governed by reference data.
* **TechnologyType** - a specialized *ValidMetadataValue* holding the valid values of [deployedImplementationType](/concepts/deployed-implementation-type).  These are the technology types that drive Egeria's automated cataloguing.

## Using valid values

* *ValidValuesAssignment* links a set of valid values to the element representing a data field - a [data field](/concepts/data-field), [glossary term](/concepts/glossary-term) or schema element.  Its *strictRequirement* property says whether the listed values are the only ones permitted, or merely the preferred ones.
* *ValidValuesImplementation* maps a valid value to the value actually used in a particular code table, which is what makes it possible to keep the code tables across an [information supply chain](/concepts/information-supply-chain) consistent - or to generate the mapping tables that translate between them.
* *ValidValuesMapping* records that values from different sets - different standards, regulations or industry definitions - are equivalent.
* *ConsistentValidValues* supports cross-field validation, showing which values in one set are consistent with values in another.
* *ReferenceValueAssignment* uses a valid value as a tag on another metadata element, marking that the element has a particular property or belongs to a particular group.

???+ info "Additional information"
    * The *ValidValueDefinition* type, its subtypes and its relationships are described in [Model 0545 Reference Data](/types/5/0545-Reference-Data).
    * The [Reference Data API](/services/omvs/reference-data/overview) manages valid value definitions, sets and mappings.  The [Valid Metadata API](/services/omvs/valid-metadata/overview) provides specialist operations for the valid values of open metadata properties and for specification properties.
    * [Reference Data Management](/features/reference-data-management/overview) describes the practice in full, with worked examples.

--8<-- "snippets/abbr.md"
