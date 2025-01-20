<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0475 Context Events

Context events provide a description of a particular event that occurred in the past, is in progress now, or may occur in the future.  The event may be instantaneous, or have a specific duration, and it may repeat.

Examples of context events include:

* Severe weather events.
* The start of a new regulation.
* The arrival of a new data set or the updating of an existing data set.
* A power outage.

Recording context events in open metadata allows situations that impact users, data, services, etcetera, to be recorded and used to explain why blips occurred in the past, or plan and take action to mitigate against blips in the future.

Similarly, where blips are observed, context events can be used to provide placeholders that suggest something significant happened, even though the exact details are not (yet) known.

Events may be managed by a [*Project*](/types/1/0130-Project), [*Actor*](/types/1/0110-Actors) or [*Community*](/types/1/0140-Communities).  These are linked to the *ContextEvent* entity using the [*AssignmentScope*](/types/1/0120-Assignment-Scopes) relationship.

When events are being managed, often actions are initiated.  These actions can be linked to the context events using the [*Actions*](/types/1/0137-Actions) relationship.  For example, a person may be sent a [*ToDo*](/types/1/0137-Actions) that requests that they read some documentation, acknowledge receipt of a warning, or approve additional resources.  These actions may also include an automated response that is executed via a [engine action](/types/4/0463-Engine-Actions).

A [NoteLog](/types/1/0160-Notes) can be attached to a context event or context event collection to record significant stages/steps/events that occurred during the context event(s).

![UML](0475-Context-Events.svg)

## ContextEvent entity

The *ContextEvent* entity is used to record a context event.  It is a [*Referenceable*](/types/0/0010-Base-Model) that adds the following attributes:

* *name* - a display name that describes the event.
* *description* - a more detailed description of the event.
* *eventEffect* - describes the expected effects of the event on the organization.
* *contextEventType* - describes the type of event.  Valid values for this attribute can be managed in a [valid metadata value](/guides/planning/valid-values/overview) set.
* *plannedStartDate* - provides a planned date/time when the event should start.
* *actualStartDate* - provides a definitive date/time when the event did start.
* *plannedDuration* - defines, in milliseconds, the length of time that the event is expected to last.
* *actualDuration* - defines, in milliseconds, the length of time that the event did last.
* *repeatInterval* - defines, in milliseconds, how frequently the event is expected to repeat.
* *plannedCompletionDate* - provides an expected date/time when the event is complete.
* *actualCompletionDate* - provides a date/time when the event did complete.
* *referenceEffectiveFrom* - provides a value to use in the starting effective dates for entities, relationships and classifications whose effectivity is triggered by this context event.  For example, the context event may record the date/time that a new regulation comes into force.  This value can be used to set up the effectiveFromTime in the metadata elements that are used to govern the open metadata ecosystem once the regulation comes into effect.
* *referenceEffectiveTo* - provides a value to use in the ending effective dates for entities, relationships and classifications whose effectivity is ended by this context event.  For example, the context event may record the date/time that a new regulation comes into force.  This value can be used to set up the effectiveToTime in the metadata elements that are no longer valid once the regulation comes into effect.

The attributes provide a variety of options for expressing the time window of the context event since some events name be instantaneous, others may have a longer duration, or repeat at regular intervals.  Other events may be in the future, and the exact date unknown.  Nevertheless, the organization wishes to manage the event in order to make appropriate preparations.

## ContextEventEvidence relationship

Evidence that the context event has occurred, started or is expected can appear as alerts/notification or incidents that people have raised.

Details of alerts/notifications may be stored in a digital resource such as a file or database.  These digital resources are represented as [*Assets*](/types/0/0010-Base-Model) entities in open metadata.  The *Asset* entity can be linked to the *ContextEvent* entity using the *ContextEventEvidence* relationship.

Similarly, a reported incident can be represented in open metadata using an [*IncidentReport*](/types/4/0470-Incident-Reporting) entity.  This entity can be linked to an appropriate *ContextEvent* entity using the *ContextEventEvidence* relationship.

Linking this evidence to the context event helps the people managing it to refine their approach as the timing, scope and impact becomes clearer.

## DependentContextEvent relationship

When an event is predicted, or has occurred, other events may need to be detected, recorded of initiated.  The *DependentContextEvent* relationship allows events that are created as a result of a "larger" event to be linked together.

For example, an organization receives a notification that there is going to be a severe storm.  They create a *ContextEvent* entity to represent the storm.  They also create dependent *ContextEvent* entities to represent the different activities involved in preparing for the storm, riding out the storm and recovering from the storm.  These additional events help to explain why new data was acquired, additional capacity was requested, services were curtailed, etcetera, etcetera.

The *description* attribute allows an explanation of why the dependent action is required.

## RelatedContextEvent relationship

Some events have knock on effects that result in new events.  The *RelatedContextEvent* relationship is used to record whether there is a potential relationship between context events.  For example, a context event that records a tsunami could be related to an earthquake that what detected at a similar time in a related area.

Sometime these relationships are clear, obvious and certain.  Others are less obvious and may need verification.  Hence, the attributes of this relationship allow the uncertainty, along with details of who is responsible to verify the relationship, and their current opinion.

* statusIdentifier - Status of this association.  The values are defined in the [*GovernanceStatusSet*](/types/4/0421-Governance-Classification-Levels).
* confidence - Level of confidence in the association (0=none -> 100=excellent).
* steward - Person responsible for maintaining this association.
* stewardTypeName - Type of element used to identify the steward.
* stewardPropertyName - Name of property used to identify the steward.
* source - Source of the association.
* notes - Information relating to the association.

## ContextEventCollection classification

A *ContextEventCollection* classification is used to indicate that a particular collection contains a list of context events.  It is used to group context events that are being managed together.  The collection could then be attached to, say, a [*Project*](/types/1/0130-Projects) using the [*ResourceList*](/types/0/0019-More-Information) relationship.

The optional *timeline* attribute allows a description of the timeline that summarizes the timeline of the events in the collection.

## ContextEventImpact relationship

The *ContextEventImpact* relationship allows a *ContextEvent* entity to be linked to [*Referenceable*](/types/0/0010-Base-Model) entities that describe resources that are impacted by the event.  For example, it may link a context event to a [*SoftwareServer*](/types/0/0040-Software-Servers) that is needed extra capacity to support the organization during the event.  

The *severityLevelIdentifier* attribute describes the severity of the impact on the *Referenceable* entity.  Its value is taken from the list of severities defined in the [GovernanceClassificationLevel](/types/4/0421-Governance-Classification-Levels) collection for severity levels.  The *description* allow further information on the impact to be documented.

## ContextEventForTimelineEffects relationship

The *ContextEventForTimelineEffects* relationship is used to associate a referenceable entity (typically an [*Asset*](/types/0/0010-Base-Model) or [*SchemaAttribute*](/types/5/0505-Schema-Attributes)) with a context event to show that the context event affected the data associated with the entity.  For example, consider a data store that records a server's availability.  A power outage resulted in the server being down.  The *ContextEventForTimeline* relationship can be used to associate the server availability data store with the context event describing the power outage.  When the context event's date/time/duration is viewed in conjunction with the server availability data, it is possible to understand why there was a server outage at a particular moment in time.  The context event explained why there was an outage at a particular point in time.



--8<-- "snippets/abbr.md"