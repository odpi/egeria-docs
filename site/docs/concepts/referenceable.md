---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Referenceable 

A [referenceable](/egeria-docs/types/0/0010-Base-Model/#referenceable) is the description of an element that is significant enough to need its own unique name so that it can be referred to accurately in different contexts (typically outside of open metadata).

The unique name is stored in the qualified name (*qualifiedName*) property and the [generic handlers](/egeria-docs/services/generic-handlers) module in the [metadata access servers](/egeria-docs/concepts/metadata-access-server) will validate that this value is unique within its type when a new referenceable is created or updated.

Nevertheless, it is possible that multiple metadata elements with the same qualified name could be present in the open metadata ecosystem. This may be because different repositories have loaded metadata about the same object. Alternatively, there is a name clash as two servers have used the same unique name for different objects.  

??? education "Further information"

    [Managing external identifiers](/egeria-docs/features/external-identifiers/overview)
    
--8<-- "snippets/abbr.md"
