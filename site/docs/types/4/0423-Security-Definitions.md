<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0423 Security Definitions

Security, particularly access control, is an important form of governance that preserves exclusive access to specific [resources](/concepts/resource) for particular *[actors](/types/1/0110-Actors)*.

The security definitions in Egeria have two purposes:

* To provide information to the [server metadata security connector](/concepts/server-metadata-security-connector) when it is making [authorization decisions](/features/metadata-security/overview/#open-metadata-server-security-connector-interface).
* To provide information to an [integration connector](/concepts/integration-connector) that is [synchronizing access control information](/features/synchronized-access-control/overview) with an authorization engine.  This is used when access to resources is being controlled through open metadata by the self-service users of the open metadata servers.

Security access control decisions need to be made with very little latency because they are running in the main path of every request.  Therefore, the definitions are divided into two types:

* The definitions that control which users have access to which resources.  This can be expressed at the user, role, team, community/project, organization level.  To determine an individual's access involves navigating through multiple definitions which is too slow for operation use.
* The definitions that summarize access controls at the user and resource element level.  These values enable auditing of access and are used to configure the user directory and the resource authorization engine.


![UML](0423-Security-Definitions.svg)

## SecurityAccessControl entity

The *SecurityAccessControl* entity is a [TechnicalControl](/types/4/0420-Governance-Controls) that defines the access control lists that a user must belong to if he/she/it is to be given permission to execute a specific command.

## AssociatedGroup relationship

The *AssociatedGroup* relationship defines which *SecurityGroup* to use for each type of operation defined by the *SecurityAccessControl* entity.  The `operationName` attribute defines the name of the operation being mapped.

## SecurityGroup entity

The *SecurityGroup* represents a group of [actors](/types/1/0110-Actors) that need to be given the same access to a specific set of resources.  It includes the `distinguishedName` used in LDAP based user directories.  This is the distinguished name of the group where authorized users are listed.

## SecurityGroupMembership classification

The *SecurityGroupMembership* classification summarizes the list of security groups that a user should be granted.  For efficiency, each security group may be identified by its `distinguishedName` property for efficiency.  However, it may be the group's `qualifiedName`.  The *SecurityGroupMembership* classification is attached to one of the user's *[UserIdentity](/types/1/0110-Actors)* entities.

## SecurityTags classification

*SecurityTags* identify labels, properties and access control lists that are used in determining which access control rules should be executed when access to a particular resource is requested.  They can be attached to [assets](/types/0/0010-Base_Model), [schema elements](/types/5/0501-Schema-Elements) and [glossaries](/types/3/0310-Glossary) depending on the scope of resource that the security tags apply to. The [synchronized access control](/features/synchronized-access-control) feature describes how security tags are set up and used.


--8<-- "snippets/abbr.md"