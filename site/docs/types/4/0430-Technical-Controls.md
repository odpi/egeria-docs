---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0430 Technical Controls

Technical controls are [governance controls](/types/4/0420-Governance-Controls) that are implemented using technology.  They are deployed into
the IT landscape as software components and processes.

* *GovernanceRule* - defines an executable rule that can be deployed at particular points in the processing.  The implementation of this rule is identified by the *GovernanceRuleImplementation* relationship.
* *ServiceLevelObjectives* - defines the performance, availability and quality levels expected from an element attached by the [GovernedBy](/types/4/0401-Governance-Definitions) relationship.
* *GovernanceProcess* - defines an executable process that choreographs different actions the can be deployed at particular points in the processing.  The implementation of this process is identified by the *GovernanceProcessImplementation* relationship.

The places in the landscape where these elements are deployed are identified by [Governance Execution Points](/types/4/0460-Governance-Execution-Points).

![UML](0430-Technical-Controls.svg)


--8<-- "snippets/abbr.md"