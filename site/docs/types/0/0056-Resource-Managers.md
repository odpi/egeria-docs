<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0056 Resource Managers

A resource manager is a software capability that manages one or more resources.  The following entity types augment the description of a software capability.  

![UML](0056-Resource-Managers.svg)

## FileSystem

The `FileSystem` is a collection of stored files organized in a folder hierarchy.  They are managed by many resource managers as long as they have access privileges.  Each resource manager may access these files through a different mount point.  The effect is that the full path name of the file may differ from resource manager to resource manager.  Therefore, the attributes captured for a file system are:

* *encryption* - type of encryption used on the files.
* *format* - format used to store the files.
* *localMountPoint* - root of the file path name that is due to the resource manager's view of the file system.
* *canonicalMountPoint* - value to replace the actual mount point with when storing/retrieving metadata about a file within the file system.

The use of the localMountPoint and canonicalMountPoint is critical to allow different tools in the open metadata ecosystem to share metadata about the same files.

## FileManager

The `FileManager` entity manages a collection of files - it is typically the single owner of the files, and they are access through its APIs.  A photo management application is an example of such a file manager.

## UserProfileManager

The `UserProfileManager`entity describes a system that manages user profile information - such as a company directory.

## UserAccessManager

The `UserAccessManager` entity describes a user directory such as LDAP.

## MasterDataManager

A `MasterDataManager` entity describes a server that manages the rationalization of master data stored in many systems.

## ContentCollectionManager

A `ContentCollectionManager` entity describes a server that manages a [collection of documents or media files](/types/2/0221-Document-Stores).

## NotificationManager

A `NotificationManager` entity describes a server that manages the distribution of [events](/types/2/0223-Events-and-Logs) to multiple destinations.

## SourceControlLibrary

A `SourceControlLibrary` entity describes a server that manages version of files related to software source and its related resources.

## ChangeManagementLibrary

A `ChangeManagementLibrary` entity describes a server that manages descriptions and decisions about potential and actual changes to the IT landscape.

## SoftwareLibrary

A `SoftwareLibrary` entity describes a server that manages the distribution of software modules and libraries in the deployment of capability to the IT landscape.


--8<-- "snippets/abbr.md"
