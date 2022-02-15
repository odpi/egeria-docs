<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


Open metadata archives are introduced into the server through the admin services either:

1. provided as part of the contents of the server's configuration document, or
2. through the operational command that added the archive directly into the running server's repository.

![Processing of an open metadata archive](open-metadata-archive-processing.svg)

The archive is passed to the repository services' operational services, which in turn passes it on to the [archive manager](/services/omrs/archive-manager). Type information is passed to the [repository content manager](../services/omrs/repository-content-manager.md).

Both the types and instances are passed to the local repository (if there is one).

The archive loads in the following order:

1. Attribute Type Definitions (`AttributeTypeDef`s) from the type store, through `verifyAttributeTypeDef()` and then `addAttributeTypeDef()`:
    1. PrimitiveDefs
    2. CollectionDefs
    3. EnumDefs
2. New Type Definitions (`TypeDef`s) from the type store, through `verifyTypeDef()` and `addTypeDef()` calls to the local repository:
    1. EntityDefs
    2. RelationshipDefs
    3. ClassificationDefs
3. Updates to types (`TypeDefPatch`es)
4. Instances, as reference copies:
    1. Entities
    2. Relationships
    3. Classifications

!!! tip "Cohort propagation"
    If the server is connected to the cohort, the new content is sent as notifications to the rest of the cohort.


--8<-- "snippets/abbr.md"
