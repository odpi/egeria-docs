<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->


# Repository get type definition gallery test case

Validate that it is possible to retrieve type definitions from the repository.

## Operation

This test uses the getAllTypes
(`/open-metadata/repository-services/users/{userId}/types/all`)
operation to retrieve all of the supported types.
The type definition gallery (TypeDefGallery)
returned contains definitions of both the attribute types (AttributeTypeDefs)
and entity, relationship and classification type (TypeDefs) supported by the
repository.
The contents of the type definition gallery
is used to verify the results of other
calls to the repository services.

## Assertions

* **repository-get-typedef-gallery-01** TypeDefGallery retrieved.
  
  The `getAllTypes` call returned a type definition gallery.
  
## Discovered Properties

* **Number of supported AttributeTypeDefs** count of the attribute type definitions returned.
* **Supported AttributeTypeDefs** list of the attribute type definitions returned.
* **Number of supported TypeDefs** count of the type definitions returned.
* **Supported TypeDefs** list of the type definitions returned.

## Example output

!!! info "About this sample"
    The output below is illustrative.  It was captured from one repository running an earlier release, and
    shows the *shape* of the result rather than the current type system: the type and attribute-type lists
    are elided, and the counts are the ones that run reported.  Both depend on the repository under test and
    the release it supports.  For the types Egeria defines today, see the
    [open metadata type models](/types).

```json
{
      "class" : "OpenMetadataTestCaseResult",
      "testCaseId" : "repository-get-typedef-gallery",
      "testCaseName" : "Repository get type definition gallery test case",
      "testCaseDescriptionURL" : "https://egeria.odpi.org/open-metadata-conformance-suite/docs/origin-workbench/repository-get-typedef-gallery-test-case.md",
      "assertionMessage" : "Repository type definition gallery retrieved",
      "successfulAssertions" : [ "TypeDefGallery retrieved." ],
      "unsuccessfulAssertions" : [ ],
      "discoveredProperties" : {
        "Supported AttributeTypeDefs" : [ "CrowdSourcingRole", "string", "char", "TermRelationshipStatus", "map<string,string>", "ContactMethodType", "BusinessCapabilityType", "StarRating", "..." ],
        "Supported TypeDefs" : [ "PropertyFacet", "Confidentiality", "UserIdentity", "ProfileIdentity", "Referenceable", "ControlPoint", "GovernanceControlLink", "ExternalId", "..." ],
        "Number of supported AttributeTypeDefs" : 39,
        "Number of supported TypeDefs" : 314
      }
}
```



--8<-- "snippets/abbr.md"