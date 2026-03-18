<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0423 Security Definitions

Security, particularly access control, is an important form of governance that preserves exclusive access to specific [resources](/concepts/resource) for particular *[actors](/types/1/0110-Actors)*.

![UML](0423-Security-Definitions.svg)

## UserAccount relationship

The *UserAccount* relationship links a *UserIdentity* entity that describes a userId with the [SecretsCollection](/types/2/0227-Keystores) where the user's account is defined.

## ResourcePermissions relationship

The *ResourcePermissions* relationship links a [SecurityAccessControl](/types/4/0430-Technical-Controls) with the [SecretsCollection](/types/2/0227-Keystores) where the security access control is defined.

## ServiceAccessControl entity

The *ServiceAccessControl* entity is a type of [SecurityAccessControl](/types/4/0430-Technical-Controls) that describes the permissions associated with a service.  This may cover a server or a service.  The *mappingProperties* are used to define the exact scope that the control refers to.

## SecretsCollectionSecurityList relationship

The *SecretsCollectionSecurityList* relationship links a *SecurityList* with the [SecretsCollection](/types/2/0227-Keystores) where the security list is defined.

## SecurityList entity

The *SecurityList* entity defines a list of users and nested lists that are included in a set of permissions associated with a security access control.  It is a specialized type of [Collection](/types/0/0021-Collections) so the lists can be nested using the [CollectionMembership](/types/0/0021-Collections) relationship.

## SecurityGroup entity

The *SecurityGroup* entity defines a group of users and groups that are related.

## SecurityRole entity

The *SecurityRole* entity defines a collection of users that requires the same permissions to perform the same work (role).

## AssociatedSecurityList relationship

The *AssociatedSecurityList* relationship defines which *SecurityList* to use for each type of operation defined by the *SecurityAccessControl* entity.  The `operationName` attribute defines the name of the operation being mapped.

## SecurityListMembership classification

The *SecurityListMembership* classification summarizes the list of security groups that a user should be granted.  For efficiency, each security group may be identified by its `distinguishedName` property for efficiency.  However, it may be the group's `qualifiedName`.  The *SecurityGroupMembership* classification is attached to one of the user's *[UserIdentity](/types/1/0110-Actors)* entities.

## SecurityTags classification

*SecurityTags* identify labels and properties that are used in determining which access control rules should be executed when access to a particular resource is requested.  They can be attached to [assets](/types/0/0010-Base_Model), [schema elements](/types/5/0501-Schema-Elements) and [glossaries](/types/3/0310-Glossary) depending on the scope of resource that the security tags apply to. The [synchronized access control](/features/synchronized-access-control) feature describes how security tags are set up and used.


--8<-- "snippets/abbr.md"