<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0430 Development Controls

Gevelopment controls are [governance controls](/types/4/0420-Governance-Controls) that focus on fulfilling new requirements and capabilities of the organization. The work to fulfill these needs is typically defined in a [Project](/types/1/0130-Projects).

![UML](0430-Development-Controls.svg)

## Requirement entity

The *Requirement* entity defines a requirement of the organization.  It is a type of [GovernanceControl](/types/4/0420-Governance-Controls).

## ResearchQuestion entity

The *ResearchQuestion* entity defines a research question of the organization.  It is a type of [GovernanceControl](/types/4/0420-Governance-Controls).

## DataLens entity

The *DataLens* entity identifies the scope of data for a particular type of processing. The attributes of this governance definition identify the scope of the data in different dimensions such as subject area, location, time, organizational context, and regulatory framework.  It is typically attached to a collection gathering data assets for a specific purpose. 

* *minLongitude* - if the data is bound by an area, this is the longitude for bottom-left corner of the bounding box (BBOX) for the area covered by the data.
* *minLatitude* - if the data is bound by an area, this is the latitude for the bottom-left corner of the bounding box (BBOX) for the area covered by the data.
* *maxLongitude* - if the data is bound by an area, this is the longitude for top-right corner of the bounding box (BBOX) for the area covered by the data.
* *maxLatitude* - if the data is bound by an area, this is the latitude for top-right corner of the bounding box (BBOX) for the area covered by the data.
* *minHeight* - if the height above ground is relevant, this is the lowest height that the data covers.
* *maxHeight* - if the height above ground is relevant, this is the highest height that the data covers.
* *dataCollectionStartTime* - if the data is bound by time, this is the start time.
* *dataCollectionEndTime* - if the data is bound by time, this is the end time.
* *scopeElements* - map from name (such as open metadata type name) to guid of the element that defines the scope of the data.  Examples of the types of elements used to define the scope of the data are:

    * [Business Capabilities](/concepts/business-capability)
    * [Locations](/concepts/location)
    * [Subject Areas](/concepts/subject-area)
    * [Governance Definitions](/concepts/governance-definition)
    * [Teams and Organizations](/concepts/team)
    * [Person Roles](/concepts/person-role)
    * [Information Supply Chain](/concepts/information-supply-chain)
    * [Solution Blueprints](/concepts/solution-blueprint)
  
* *additionalProperties* - (inherited from Referenceable) support other properties that identify the scope of the data represented by this element.


!!! info "Additional information"

    * More information on the use of data lens in governance is in the [Data Lens](/concepts/data-lens) concept.
    * The digital resources are matched to the data lens using their [DataScope](/types/2/0210-Data-Stores) classification.  In addition, the [ScopedBy](/types/1/0120-Assignment-Scopes/) relationship.


--8<-- "snippets/abbr.md"