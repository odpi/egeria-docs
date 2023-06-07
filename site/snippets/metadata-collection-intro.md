<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


A *metadata collection* is a collection of [open metadata instances](/concepts/open-metadata-instances) that are maintained together. Each metadata collection has a unique identifier, called the *metadata collection id* and an optional *metadata collection name*. 

An *open metadata instance* can only belong to one metadata collection.  It includes the metadata collection id and metadata collection name in its header.  This is the open metadata instance's *home* metadata collection. Typically, an open metadata instance's home metadata collection is the one where it was created, although, in rare circumstances, it is possible to change the home metadata collection.

There are 6 types of metadata collection, and they are stored in [open metadata repositories](/concepts/open-metadata-repository), [open metadata archives](/concepts/open-metadata-archive) and [configuration stores](/concepts/configuration-document-store-connector).  The type of metadata collection determines where its open metadata instances are stored and how it can be maintained (updated/deleted).

* A *Local Cohort* metadata collection is one managed by a [member of an open metadata repository cohort](/concepts/cohort-member) and stored in an [open metadata repository](/concepts/open-metadata-repository).  Security permitting, it can be updated through any open metadata ecosystem API.

* An *External Source* metadata collection contains metadata that originates in a third party technology and a copy is maintained in the open metadata ecosystem through an [Open Metadata Access Service (OMAS)](/services/omas). Typically, the OMAS is called via an [Open Metadata Integration Service (OMIS)](/services/omis) running in an [Integration Daemon](/concepts/integration-daemon).  The metadata collection id and name is defined in Open Metadata as the [unique identifier, or GUID,](/concepts/guid) and [unique name, or qualified name,](/concepts/referenceable) of a [Software Capability](/concepts/software-capability) representing the source technology.  This metadata can only be updated through an OMAS call that supplies the correct unique identifier for the metadata collection (called the *externalSourceGUID*).  Otherwise, it is read only to the rest of the open metadata ecosystem.

* A *Configuration* metadata collection means the metadata comes from a [Configuration Document](/concepts/configuration-document).  Configuration documents control the capabilities of an [OMAG Server](/concepts/omag-server).  This metadata is maintained through Egeria's [Administration Services](/guides/admin/overview) and is stored in a [configuration store](/concepts/configuration-document-store-connector).

* A *Content Pack* metadata collection is located in an [open metadata archive](/concepts/open-metadata-archive) that contains a collection of standard definitions.  Content packs could contain glossaries, reference data sets, definitions from regulations and other types of standards. The archive documents the metadata collection id and name for the collection.  In addition, a content pack is used to define [Open Metadata Types](/types).  The metadata from a content pack can be updated by loading a later version of the content pack.  Updated instances and types from the archive are replaced by the newer versions.

* *Metadata Export* is also content from an [open metadata archive](/concepts/open-metadata-archive).  However, it has been exported from an [open metadata repository](/concepts/open-metadata-repository) outside the open metadata ecosystem. It is intended as a means of transporting metadata from one open metadata ecosystem to another.

* *Deregistered Repository* means that the metadata collection is owned by a server that has been disconnected from the open metadata ecosystem.  This means it is no longer sending updates to the other members of the open metadata ecosystem.  Its metadata is still visible because *reference copies* (read only copies) have been kept by the other members.  However, it should be used with caution since it may not be up-to-date.

When a metadata instance from the metadata collection is shared within the broader open metadata ecosystem, its identifies the *home* metadata collection of the metadata instance.




