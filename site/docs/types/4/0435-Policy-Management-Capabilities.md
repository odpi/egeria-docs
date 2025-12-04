---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0435 Policy Management Capabilities

The policy management capabilities describe the different capabilities needed to automate
the enforcement of policies.  These capabilities were originally identified in the 
[eXtensible Access Control Mark-up Language (XACML)](https://en.wikipedia.org/wiki/XACML) standard.

XACML is an [OASIS](https://www.oasis-open.org/) standard specifically focused at access control policies.
However the architecture is clean enough to generalise to the management of all types of governance policy 
and so it has been included in the open metadata types.

There are five components involved in policy management:
- *Policy Administration Point (PAP)* - the tool/API used to administer policies.
- *Policy Decision Point (PDP)* - the component that evaluates policies for a specific situation and selects a
  course of action.
- *Policy Enforcement Point (PEP)* - the component thar enforces the policy decision made by the PDP.
  Usually this is the component that is used to access a resource or perform a task. 
  The PEP calls the PDP to find out what the decision that needs to be enforced and then
  enforces the resulting decision in real-time.
- *Policy Information Point (PIP)* - a component that provides additional information to the PDP
  to enable it to make a decision.
- *Policy Retrieval Point (PRP)* - a component used by the PDP to retrieve the policy details that apply to the
  situation that the PDP is evaluating. 

## Open Metadata Types

The open metadata types are implemented as classifications.  The classifications can be applied to
[Referenceables](/types/0/0010-Base-Model) so that they can be used to classify
[solution components](/types/7/0730-Solution-Components) during solution design and
[software capabilities](/types/0/0042-Software-Capabilities) for the running implementation.


![UML](0435-Policy-Management-Capabilities.svg)


## Using the Policy Management Capabilities open metadata types

The [Security Officer](/services/omvs/security-officer/overview) API provides mechanisms to set up the Policy Management Capabilities classifications on metadata elements.
 

--8<-- "snippets/abbr.md"