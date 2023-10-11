---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/in-development.md"

# Collection Manager OMVS

The Collection Manager Open Metadata View Services (OMVS) is a REST API designed to back user interfaces (UIs) that support the maintenance and browsing of hierarchies of [collections](/concepts/collection) and their members.

Collections are used to organize elements.  Elements (including other collections) are linked to a collection to show that they are a member of the collection.  An element can be a member of none, one or multiple collections.

There are different types of collections:

* **Collection Hierarchy** - A collection hierarchy is the root node of a hierarchy of collections.  Its members are typically other collections.
* **Folder** - a collection folder is a collection that is part of a collection hierarchy structure.  It may have members that are collections and/or other types of collections.
* **Digital Product** - A digital product is a collection of [assets](/concepts/asset) that have been especially crafted to support a specific use case (or related use cases).  The assets may represent different versions of the product or customized versions of the same data for different purposed, or supporting different non-functional requirements.

The Collection Manager OMVS supports:

* The creation and maintenance of the properties associated with a collection.  New collections can be created using another collection as a template.
* The management of the members of a collection.
* The attachment of a collection as a resource of an entity such as a project, community or user's profile.
* The ability to mark a collection as a template and search for the template collections in the open metadata ecosystem.
* The ability to search collections, with or without particular classifications and properties and navigate through a collection's membership.





---8<-- "snippets/abbr.md"






