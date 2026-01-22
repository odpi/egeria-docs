<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0430 Technical Controls

Technical controls are [governance controls](/types/4/0420-Governance-Controls) that are automated.  They are deployed into
the IT landscape as software components and data assets. 

The implementation of a technical control can be identified by the [ImplementedBy](/types/7/0737-Solution-Implementation) relationship.  This may be directly to an [Asset](/types/0/0010-Base-Model) or to a [SolutionComponent](/types/7/0730-Solution-Components).
Alternatively, [Governance Execution Points](/types/4/0460-Governance-Execution-Points) can provide a more sophisticated mapping to the implementation, particularly where the implementation is distributed and requires the collaboration of multiple components to achieve the desired behaviour.

![UML](0430-Technical-Controls.svg)


## GovernanceRule entity

The *GovernanceRule* entity defines an executable rule that can be deployed at particular points in the processing. 

## ServiceLevelObjective entity

The *ServiceLevelObjective* entity defines the performance, availability and quality levels expected from an element attached by the [GovernedBy](/types/4/0401-Governance-Definitions) relationship.

## GovernanceAction entity

The *GovernanceAction* entity defines an executable action, or sequence of actions, to support a governance requirement.

## GovernanceMetric entity

An important aspect of the governance program is the ability to measure its effectiveness and identify the activities that are delivering the highest value, or operating with the greatest efficiency etc.

A value (or collection of values) that should be captured to demonstrate the effectiveness of an aspect of the governance program is documented using the *GovernanceMetric* entity.

The associated measurements for the metric an either be stored in a data source such as a database or file, particularly if it is a lot of data or captured in a classification attached to the element that the data values describe.

## SecurityAccessControl entity

The *SecurityAccessControl* entity is a TechnicalControl that defines the access control lists that a user must belong to if he/she/it is to be given permission to execute a specific command.

## SecurityGroup entity

The *SecurityGroup* represents a group of [actors](/types/1/0110-Actors) that need to be given the same access to a specific set of resources.  It includes the `distinguishedName` used in LDAP based user directories.  This is the distinguished name of the group where authorized users are listed.



--8<-- "snippets/abbr.md"