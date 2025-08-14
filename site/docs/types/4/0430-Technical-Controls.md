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

--8<-- "snippets/abbr.md"