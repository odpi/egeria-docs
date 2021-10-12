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
* **Policy Administration Point (PAP)** - the tool/API used to administer policies.
* **Policy Decision Point (PDP)** - the component that evaluates policies for a specific situation and selects a
  course of action.
* **Policy Enforcement Point (PEP)** - the component thar enforces the policy decision made by the PDP.
  Usually this is the component that is used to access a resource or perform a task. 
  The PEP calls the PDP to find out what the decision that needs to be enforced and then
  enforces the resulting decision in real-time.
* **Policy Information Point (PIP)** - a component that provides additional information to the PDP
  to enable it to make a decision.
* **Policy Retrieval Point (PRP)** - a component used by the PDP to retrieve the policy details that apply to the
  situation that the PDP is evaluating. 

## Open Metadata Types

The open metadata types are implemented as classifications.  The classifications can be applied to
[Referenceables](/egeria-docs/types/0/0010-Base-Model) so that they can be used to classify
[solution components](/egeria-docs/types/7/0730-Solution-Components) during solution design and
[software server capabilities](/egeria-docs/types/0/0042-Software-Server-Capabilities) for the running implementation.


![UML](0435-Policy-Management-Capabilities.svg)


## Using the Policy Management Capabilities open metadata types

The [Digital Architecture OMAS](/egeria-docs/services/omas/digital-architecture/overview)
and [IT Infrastructure OMAS](/egeria-docs/services/omas/it-infrastructure/overview)
provide mechanisms to set up the Policy Management Capabilities classifications on metadata elements.

## Implementation of Policy Management Capabilities in Egeria

Not only does Egeria support the use of the Policy Management Capabilities in your architectures and
metadata, we have also the concepts in the design of Egeria itself.

In Egeria, the Policy Administration Point is
[Governance Program OMAS](/egeria-docs/services/omas/governance-program/overview).
Services such as 
[Governance Engine OMAS](/egeria-docs/services/omas/governance-engine/overview)
act as a Policy Retrieval Points to push policy information to external Policy Enforcement Points such as
[Apache Ranger](http://ranger.apache.org/).

Egeria's [metadata access points](/egeria-docs/concepts/metadata-access-point)
and [metadata access store](/egeria-docs/concepts/metadata-access-store)
can act as Policy Information Points.

Egeria's
[Metadata Security](/egeria-docs/features/metadata-security/overview)
module is a Policy Enforcement Point, calling the metadata security connectors as Policy Decision Points.

The [Engine Services](/egeria-docs/services/omes)
running in the [Engine Host OMAG Server](/egeria-docs/concepts/engine-host)
can act as Policy Enforcement Points. 

--8<-- "snippets/abbr.md"