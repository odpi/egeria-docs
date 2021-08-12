---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Referenceable 

A [referenceable](/egeria-docs/types/0/0010-base-model/#referenceable) is the description of a resource that is
significant enough to need its own unique name so that it can be referred to accurately in different contexts
(typically outside of open metadata).

The unique name is stored in the qualified name (**qualifiedName**) property and the open
metadata servers validate that this value is unique within its type.

It is possible that two different metadata elements with the same qualified name
could be created in different metadata servers. This may be because
both servers have loaded metadata about the same object.
Alternatively, there is a name clash as two servers have used the same unique name for
two different objects.

--8<-- "snippets/abbr.md"
