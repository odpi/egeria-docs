<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0056 Resource Managers

A resource manager is a software capability that manages one or more resources.  The following classifications augment the description of a software capability ot its hosting infrastructure to describe the resources that it manages.  These classifications link to `Referencable` to allow resource managers to be identified at different levels of groanularity.

![UML](0056-Resource-Managers.svg)

## FileSystem

The `FileSystem` is a collection of stored files organized in a folder hierarchy.  They are managed by many resource managers as long as they have access privileges.

## FileManager

The `FileManager` manages a collection of files - it is typically the owner of the files and they are access through its APIs.

## AssetManager

The `AssetManager` classification represents a technology that manages metadata about resources and may also provide services to manage and/or govern the resources themselves (or at least track such actions). Data catalogs and other types of metadata catalogs are examples of asset managers.

!!! example "Examples of asset managers"
    [Amundsen :material-dock-window:](https://www.amundsen.io/amundsen/){ target=md }, [Marquez :material-dock-window:](https://marquezproject.github.io/marquez/){ target=md } and [Apache Atlas :material-dock-window:](https://atlas.apache.org){ target=md } are examples of data catalogs, and therefore of asset managers.

    An Egeria deployment using a [metadata access server](/concepts/metadata-access-server) and one or more [integration daemons](/concepts/integration-daemon) is also an asset manager.

The `AssetManager` classification on a [`SoftwareCapability`](/types/0/0042-Software-Capabilities/#softwarecapability) entity is used by the [Asset Manager OMAS](/services/omas/asset-manager/overview) to represent the third party asset manager that it is exchanging metadata with.

Identities from this third party asset manager are linked to the `AssetManager` entity using the [`ExternalIdScope`](/types/0/0017-External-Identifiers/#externalidscope) relationship.

## UserProfileManager

The `UserProfileManager` classification describes a system that manages user profile information - such as a company directory.

## UserAccessManager

The `UserAccessManager` classification describes a user directory such as LDAP.

## MasterDataManager

A `MasterDataManager` classification describes a server that manages the rationalization of master data stored in many systems.

## ContentCollectionManager

A `ContentCollectionManager` classification describes a server that manages a [collection of documents or media files](/types/2/0221-Document-Stores).

## NotificationManager

A `NotificationManager` classification describes a server that manages the distribution of [events](/types/2/0223-Events-and-Logs) to multiple destinations.

## SourceControlLibrary

A `SourceControlLibrary` classification describes a server that manages version of files related to software source and its related resources.

## ChangeManagementLibrary

A `ChangeManagementLibrary` classification describes a server that manages descriptions and decisions about potential and actual changes to the IT landscape.

## SoftwareLibrary

A `SoftwareLibrary` classification describes a server that manages the distribution of software modules and libraries in the deployment of capability to the IT landscape.




??? deprecated "Deprecated types"
    - *ContentManager* - Use *ContentCollectionManager*


--8<-- "snippets/abbr.md"
