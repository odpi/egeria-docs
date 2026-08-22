<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Repository find type definitions by category test case

This test validates that all the supported type definitions (TypeDefs) can be retrieved by category.

## Operation

Extract all known TypeDefs.  Separate them into three lists: 
Entity TypeDefs (EntityDefs), 
Relationship TypeDefs (RelationshipDefs)
and Classification TypeDefs (Classification).
Issue a query for each of these categories of TypeDef and validate that what is returned matches
the original complied lists.

## Assertions

* **repository-find-typedefs-by-category-01** - All type definitions returned by category.

   The correct list of TypeDefs were returned.

## Discovered Properties

* **Number of supported EntityDefs** - count of returned entity types
* **Supported EntityDefs** - list of returned entity types
* **Number of supported RelationshipDefs** - count of returned relationship types
* **Supported RelationshipDefs** - list of returned relationship types
* **Number of supported ClassificationDefs** - count of returned classification types
* **Supported ClassificationDefs** - list of returned classification types

## Example Output

!!! info "About this sample"
    The output below is illustrative.  It was captured from one repository running an earlier release, and
    shows the *shape* of the result rather than the current type system: the type and attribute-type lists
    are elided, and the counts are the ones that run reported.  Both depend on the repository under test and
    the release it supports.  For the types Egeria defines today, see the
    [open metadata type models](/types).

```json
{
      "class" : "OpenMetadataTestCaseResult",
      "testCaseId" : "repository-find-typedefs-by-category",
      "testCaseName" : "Repository find type definitions by category test case",
      "testCaseDescriptionURL" : "https://egeria.odpi.org/open-metadata-conformance-suite/docs/repository-workbench/repository-find-typedefs-by-category-test-case.md",
      "assertionMessage" : "Type definitions can be extracted by category",
      "successfulAssertions" : [ "All type definitions returned by category." ],
      "unsuccessfulAssertions" : [ ],
      "discoveredProperties" : {
        "Supported ClassificationDefs" : [ "Confidentiality", "ControlPoint", "AbstractConcept", "CloudService", "ListenerInterface", "MeteringLog", "ContextDefinition", "PrimaryKey", "..." ],
        "Supported EntityDefs" : [ "PropertyFacet", "UserIdentity", "Referenceable", "ExternalId", "Document", "Network", "Database", "StructSchemaType", "..." ],
        "Supported RelationshipDefs" : [ "ProfileIdentity", "GovernanceControlLink", "Antonym", "NestedLocation", "ReplacementTerm", "GovernanceResults", "AdjacentLocation", "AttachedNoteLog", "..." ],
        "Number of supported RelationshipDefs" : 117,
        "Number of supported EntityDefs" : 140,
        "Number of supported ClassificationDefs" : 60
      }
}
```


--8<-- "snippets/abbr.md"
