<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Preparing for Martyn's Law

## Overview

[Ivor Padlock](/practices/coco-pharmaceuticals/personas/ivor-padlock) is keen to explore the implications of the new UK Terrorism (Protection of Premises) Act 2025 (Martyn's Law) on Coco Pharmaceuticals' annual conference in London. The number of people attending has been growing steadily, and they are now around 700 people.  

The new act kicks in for events of over 800 people.  It is expected to be enforced from 2027 and [Ivor Padlock](/practices/coco-pharmaceuticals/persona/ivor-padlock) is keen to understand the impact, in case attendance grows.  He likes to keep ahead of the game since these government initiatives tend to offer useful insights and best-practices.

## Documenting the Act using Dr.Egeria

Although the Act has been passed into law, it is not yet being enforced.  The UK government has provided guidance on how to prepare for the new law, which can be found [here](https://www.gov.uk/government/publications/terrorism-protection-of-premises-act-2025-factsheets/terrorism-protection-of-premises-act-2025-overarching-factsheet).  There is also the [Protect UK](https://www.protectuk.police.uk/) website, with a lot of useful definitions and guidance.

As Ivor reviews the new law, he uses [Dr.Egeria](/user-interfaces/dr-egeria/overview) markdown format and command processor to capture the key information.  This helps his thinking process by structuring the information in a logical way, and puts the definitions in place in Egeria for when he needs to refer to them.

Ivor begins by building a list of the key documents that he needs to understand the new law.  These are represented using [External References](/concepts/external-reference). 

As Ivor continues his reading, he begins to notice new terms and concepts in the documents.  Again he uses Dr.Egeria markdown commands to create a list of new glossary terms, each with a simple definition cut and pasted from the websites.
He decides to create a glossary to group these terms.

The Act seems to be in two sections.  He creates a Regulation governance definition for the Act and and two RegulationArticle governance definitions for the two sections.  He links the glossary to the Regulation governance definition using the [Resource List](/types/0/0019-More-Information) relationship.
He uses [GovernedBy](/types/4/0401-Governance-Definitions) relationships to link the new glossary terms to the appropriate RegulationArticle governance definitions.

## Modelling the Impact of the Act

After Ivor has captured the key information, he starts to think about the impact of the new law on Coco Pharmaceuticals' annual conference.

He realizes he needs a new role definition for the *Responsible Person* defined by the act.  This responsible person role is scoped by the conference event.

He needs information from the venue about the escape routes and other safety measures they have.  Then he can assess if they need additional safety measures.

??? info "Further Information"
    * **Egeria's Assessing a New Regulation Solution**. In this scenario, Ivor was using Egeria's [Assessing New Regulation](/egeria-solutions/assessing-new-regulation/overview) solution to build up an inventory and understanding of the new law.
    * **Egeria's Threat Modelling Solution**. After building a definition of Martyn's Law, Ivor used Egeria's [Threat Modelling](/egeria-solutions/threat-modelling/overview) solution to model the impact of the new law on Coco Pharmaceuticals' annual conference.




--8<-- "snippets/abbr.md"