<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0545 Reference Data

Reference data provides authoritative definitions of valid values for data.  An individual valid value can be either a *ValidValueSet* or a *ValidValueDefinition*.  *ValidValueSet*s can have other valid values nested inside them using the *ValidValueMember* relationship.  As such, valid values can be organized in a hierarchy.

A set of valid values can be used to describe the values that may be stored in a data field.  The *ValidValuesAssignment* relationship is used to link the valid value set to an element that represents the data field such as a [GlossaryTerm](/types/3/0330-Terms) or a [SchemaElement](/types/5/0501-Schema-Elements). The *strictRequirement* properties indicates whether the data field can only contain the values listed (strictRequirement=true) or the valid value set is just a suggestion.

Valid values from different sets can be linked together to show that they are equivalent values using the *ValidValuesMapping* relationship.

A *ValidValueSet* can also be implemented in an asset that can be used as a look-up table while data is being processed.  The *ValidValuesImplementation* relationship ([multi-link](/concepts/uni-multi-link)) maps the symbolic names from the valid values to the value implemented in the look-up table.  The Asset can be flagged as a look-up table using the *ReferenceData* classification.

Valid values can also be used as tags to indicate that an element has a particular property or belongs in a particular group.  The element to be tagged is linked to the appropriate valid value using the *ReferenceValueAssignment* relationship.


![UML](0545-Reference-Data.svg)

## ValidValueDefinition

Software often uses code values to store properties about a person, place, object or activity.  Each code value is mapped to one or more strings when its value is to be displayed.  This mapping is stored in a *code table*.

![Information codes](/features/reference-data-management/information-codes-example.svg)

The *ValidValueDefinition* can be used to represent a single code value along with its associated properties.

![Valid Value Definition](/features/reference-data-management/valid-value-definition.svg)


## ValidValuesSet and ValidValueMember

Code tables group related code values together to act as a look-up table.  The *ValidValuesSet* and the *ValidValueMember* relationship can be used to organize *ValidValueDefinition*s.

![Valid Value Set](/features/reference-data-management/valid-value-set.svg)

Some code values need to be organized into a hierarchy.  The *ValidValueMember* allows a *ValidValuesSet* to be nested inside another *ValidValuesSet* to form a hierarchy.

![Hierarchical information codes](/features/reference-data-management/hierarchical-information-codes.svg)

## ValidValuesAssignment

Often the values in a data field need to be restricted to a set of valid values (or possibly a single valid value).  The *ValidValuesAssignment* creates a link between the metadata element for the data field (typically a [GlossaryTerm](/types/3/0330-Terms) or a [SchemaElement](/types/5/0501-Schema-Elements)) and the appropriate valid values.

![Valid Values Assignment](/features/reference-data-management/valid-values-assignment.svg)

## ReferenceValueAssignment

Valid values can be used to tag other metadata elements to make them easy to find.

![Reference Value Tagging](/features/reference-data-management/tagging-example.svg)

This tagging is done using the *ReferenceValueAssignment* relationship.

![Reference Value Assignment](/features/reference-data-management/reference-value-assignment.svg)


## ValidValuesMapping

Valid values can come from many sources (such as standards, regulations, industry definitions etc.) and often there are equivalences between them. It is useful to be able to identify the corresponding values.

![Valid Values Mapping Example](/features/reference-data-management/valid-values-mapping-example.svg)

The *ValidValuesMapping* relationship allows this mapping to be captured.

![Valid Values Mapping](/features/reference-data-management/valid-values-mapping.svg)



## ValidValuesImplementation and ReferenceData

The implementation of a code table is represented in open metadata using an [Asset](/types/0/0010-Base-Model).  This asset can be tagged as containing valid values using the *ReferenceData* classification.

The organization will likely have many code tables for the same set of valid values.  This is because many systems implement their own code values without following any standards.  The *ValidValuesImplementation* relationship allows the capture of the mapping between the valid value and the implementation value.

![Valid Values Implementation](/features/reference-data-management/valid-values-implementation.svg)

With this information it is possible to manage the code tables using open metadata.  So when a new value is needed, a new valid value definition is created with *ValidValueImplementation* relationships for each destination code table.  Then an external program can use these metadata definitions to automatically update the code tables ensuring that they are consistent throughout an information supply chain.

![Manage Valid Values](/features/reference-data-management/manage-valid-values.svg)

Or even build mapping tables to help processes moving data between different systems to convert the code values used in each location.

![Valid Values Mapping Table](/features/reference-data-management/mapping-table.svg)


!!! info "Further Information"
    * [Reference Data Management](/features/reference-data-management/overview)

--8<-- "snippets/abbr.md"