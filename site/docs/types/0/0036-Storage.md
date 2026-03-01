<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0036 Storage

It is common for the processing running on a [*Host*](/types/0/0030-Hosts-and-Platforms/#host) to need to persist data to storage.  Knowing the location of this storage can be critical in managing backups and other data recovery scenarios.  It is also valuable in data sovereignty scenarios where the permitted locations for certain types of data is defined by regulation or law.


![UML](0036-Storage.svg)

## StorageVolume entity

*StorageVolume* describes a persistent storage volume.  It inherits from the [Referenceable](/types/0/0010-Basic-Model) entity that supplied the attributes to name and describe the volume.  It adds the following attributes:

* *storageCapacity* - the amount of data the volume can store.
* *units* - the units of measurement for the capacity, such as bytes, kilobytes, megabytes, etc.
* *relativeUncertainty* - the likely range of error in the measurement of the storage volume's capacity expressed as a percentage.
* *absoluteUncertainty* - the likely range of error in the measurement of the storage volume's capacity expressed as a number of units.

## AttachedStorage relationship

*AttachedStorage* identifies the IT infrastructure (such as hosts and file systems) that the *StorageVolume* is connected to.

??? info "Related Types"
    * The [KnownLocation](0025-Locations.md) relationship can link a storage volume to a location.
    * The [StoredOn](../2/0210-Data-Stores.md) relationship can link a storage volume to a data store.


--8<-- "snippets/abbr.md"
