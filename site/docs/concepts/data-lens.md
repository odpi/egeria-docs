---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Data Lens

A Data Lens defines a scope of data that is being used to support a business capability, or defines the data requirements for a [project](/concepts/project).

Depending on the type of project, the scope of the data required may need to be constrained through multiple dimensions such as subject area, location, time, organizational context, quality and regulatory framework.

The picture below shows an example of a data lens linked to a [collection](/concepts/collection) of [assets](/concepts/asset) that match the requirements in the data lens.  The relationship between the data lens and the collection is [GovernedBy](/types/4/0401-Governance-definitions).  

The matching resource list collection is linked to a [project](/concepts/project) through the [ResourceList](/types/0/0019-More-Information) relationship.  It acts as a mini-catalog of resources that match the needs of the project.  The relationship that links the asset to the matching resource list collection is the [CollectionMembership](/types/0/0021-Collections).  The properties in this relationship allow the project team to comment on and set a status on the usefulness of the asset in to the project.

![Data Lens linked to a collection of assets that match the requirements in the data lens.](data-lens.svg)

Matching [digital resources](/concepts/digital-resource) to a data lens can be tricky because information about the resource's scope is often not available in the metadata associated with the resource itself.  It typically takes additional curation to establish the scope of the resource.  This information is captured in the [DataScope](/types/2/0210-Data-Stores) classification attached to the [asset](/concepts/asset) or [digital product](/concepts/digital-product) that represents the digital resource.  When the data scope classification is in place, patching to the data lens is straightforward, and easily automated.

??? info "Further information"

    * A data lens is a type of governance definition and is maintained and queried using the [Governance Officer API](/services/omvs/governance-office/overview).
    * The *DataLens* open metadata type is described in [Model 0430 Technical Controls](/types/4/0430-Technical-Controls/).

--8<-- "snippets/abbr.md"