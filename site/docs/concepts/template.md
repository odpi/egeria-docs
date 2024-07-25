---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Template

A *template* is a definition that can be used to provide values and structure to a newly created element.  It is implemented as a collection of [anchored](/concepts/anchor) elements with the [Template classification](/types/0/0011-Managing-Referenceables) attached to the anchor element.  The *Template* classification provides descriptive information about the purpose and use of the template.  

When a new element is created from a template, it is linked back to its template using the [SourcedFrom](/types/0/0011-Managing-Referenceables) relationship so that it is possible to trace the elements derived from a template if an update is required.  Templates also have a version identifier associated with them (in the *Template* classification).  When a new version of the template is created, it is also linked to the previous version using the *SourcedFrom* relationship.

The metadata elements that make up a template have [placeholder properties](/concepts/placeholder) in their attributes, values for which are supplied when the template is used.  The [specification](/concepts/specification) for these placeholder properties are defined using [ValidValueDefinition](/types/5/0545-Reference-Data/) entities linked to the template's anchor element using the [SpecificationPropertyAssignment](/types/5/0545-Reference-Data/) relationship.

Templates can be attached to other elements using the [CatalogTemplate](/types/0/0011-Managing-Referenceables) relationship.  This mechanism is used by [Automated Curation OMVS](/services/omvs/automated-curation/overview) when it is retrieving templates for particular technology types.


??? education "Further Information"
    * [Templated Cataloguing](/features/templated-cataloguing/overview) provides examples on how the templating mechanism works.
    * [Automated Curation OMVS](/services/omvs/automated-curation/overview) provides a REST API for querying the templates attached to particular technology types.
    * [Template Manager OMVS](/services/omvs/template-manager/overview) provides a REST API for creating new templates.
    * The [Generic Handlers](/services/generic-handlers) service takes credit for supplying the implementation if the templating mechanism.  This runs in the [metadata-access-server](/concepts/metadata-access-server).