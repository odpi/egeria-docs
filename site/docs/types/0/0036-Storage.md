<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0036 Storage

It is common for the processing running on a [*Host*](/types/0/0030-Hosts-and-Platforms/#host) to need to persist data to storage.

![UML](0036-Storage.svg)

## StorageVolume entity

*StorageVolume* describes a persistent storage volume.

## AttachedStorage relationship

*AttachedStorage* identifies the host(s) that the StorageVolume is connected to.

--8<-- "snippets/abbr.md"
