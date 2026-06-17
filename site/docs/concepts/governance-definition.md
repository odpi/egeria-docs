<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->


# Governance Definition

Governance definitions are used to record precise requirements, decisions, intents around governance to help people understand what is being asked of them, why, and how their activity will be measured.

They are hard to define and are often revised as a [governance domain](/concepts/governance-domain) matures.  However, they keep the investment and metrics targeted, making it easier to measure, justify and improve.

There are three levels of governance definitions: drivers, policies and controls.

## Governance Driver

A [governance driver](/types/4/0405-Governance-Drivers) describes a motivation to act.  It may be a regulation, threat, or an aspect of the business strategy (called a business imperative) that requires a change in the organization.

## Governance Policy

[Governance policies](/types/4/0415-Governance-Responses) describe what is required of the organization.  Typically they describe the desired future state (or at least a desirable intermediate state :).  There are three main types of policies:

* Principles define the overall values and guidelines for the organization.  These help people decide how to act in a situation where there are no rules laid down.
* Obligations define specific actions or processing that must be accommodated.
* Approaches define new initiatives, best practices and ways of working that will be adopted.

They are said to be the "responses to the challenges proposed by the governance drivers" and so they are linked to their relevant governance drivers using the [GovernanceResponse](/types/4/0415-Governance-Responses) relationship.

## Governance Control

Governance is enabled through People, Process and Technology. The governance controls describe actions and activities that support achieving the governance policies that support the drivers.  Traditionally governance controls are divided into technical controls (implemented IT function) and organizational controls (training, responsibility, buddy-checking etc).  In Egeria we do not formally distinguish between technical and organization controls in the type system since the dividing line between the things that humans do and those that are automated is changing all the time. 

[Governance controls](/types/4/0425-Governance-Controls) are linked to their relevant governance policies using the [GovernanceMechanism](/types/4/0425-Governance-Controls) relationship.  They include [Governance Actions](/concepts/governance-action) and [Governance Zones](/concepts/governance-zone).

???+ info "Further information"

    Definind governance definitions appear in the following Coco Pharmaceuticals scenarios:

    * [Creating a data governance program](/practices/coco-pharmaceuticals/scenarios/creating-data-governance-program/overview)
    * [Creating a sustainability initiative](/practices/coco-pharmaceuticals/scenarios/sustainability-initiative/overview)
    
    You can browse the governance definitions using [egeria-explorer](/user-interfaces/egeria-explorer/overview) under the **Governance Definitions** tile.  They are organized by type and can be filtered by  **domainIdentifier**.  Setting up a new governance definition is through the [Governance Officer API](/services/omvs/governance-officer/overview).


--8<-- "snippets/abbr.md"
