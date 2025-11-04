---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Deployed Implementation Type

A *deployed implementation type* is a type of reference data that describes a class of technology that is deployed in an organization's IT landscape.  Its purpose is to describe how technology of this class should be governed and the resources available to do so.  For example:

* An instance of this technology is likely to be catalogued in the open metadata ecosystem using an [asset](/concepts/asset).  The deployed implementation type can define the subtype of the asset to use.  It is also possible to define a template for creating the asset and associate it with the deployed implementation type.
* The governance action processes, governance services and connectors that support this type of technology can be identified.
* The *deployedImplementationType* attribute of the [Asset](/types/0/0010-Base-Model) entity type can be set from the matching deployed implementation type reference value.  Having consistent values for the deployedImplementationType attribute makes it possible to retrieve lists of all catalogued technology of a particular class.

## Examples of Deployed Implementation Types

--8<-- "snippets/content-packs/deployed-implementation-types.md"

--8<-- "snippets/abbr.md"
