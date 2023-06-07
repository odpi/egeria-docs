<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Open Metadata Repository

A metadata repository is a store of metadata. A metadata repository that supports the open metadata standards is called an *open metadata repository*.  There are two types of open metadata repository:

* *Native open metadata repository*: A native open metadata repository is one that stores [open metadata elements](/concepts/open-metadata-instances) natively.  They can typically store any type of open metadata element.  It is configured in a [metadata access store](/concepts/metadata-access-store).

* *Adapter open metadata repository*: An adapter open metadata repository supports an open metadata repository API, but translates calls to this API into calls to the native API of a third party metadata repository. It is configured in a [repository proxy](/concepts/repository-proxy).


Open metadata repositories contain one local [metadata collection](/concepts/metadata-collection) that is used for maintaining its own metadata.  The identifier for this collection is [configured in the server's configuration document](/concepts/metadata-collection-id).

An open metadata repository may also store metadata elements from other metadata collections, if it is able to preserve the metadata collection id that the metadata element belongs to and honor the maintenance rules associated with its [metadata collection type](/concepts/metadata-collection).  All native open metadata repositories can store multiple metadata collection.  You need to check the implementation of an adapter open metadata repository to verify its capability.

The value of being able to store metadata elements from other collections is:

* To be able to cache metadata elements from other members of the open metadata ecosystem.  These metadata elements are called *reference copies*.
* To be able to manage [external source metadata collections](/concepts/metadata-collection).
* To be able to store metadata from [open metadata archives](/concepts/open-metadata-archive).

Open metadata repositories are responsible for replicating metadata from their local metadata collection to other members of the connected cohorts.

--8<-- "snippets/abbr.md"


