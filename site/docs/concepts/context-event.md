<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Context Event

A *context event* describes something that happened - in the past, now, or expected in the future - that affects the performance of systems, people and organizations, and hence the data they produce.

Data does not misbehave for no reason.  A gap in a sales feed, a spike in error rates, a month where a measure is inexplicably low: something caused it.  A context event is where that cause is recorded, so that anomalies can be explained rather than merely observed - and so that known future events can be prepared for.

Examples include severe weather, the start of a new regulation, a power outage, and the arrival or update of a data set.

Where an anomaly is observed but the cause is not yet known, a context event can still be created as a placeholder.  It records that something significant happened at that point, ready for the detail to be filled in later.

## Describing the event's timing

Events vary enormously in shape: some are instantaneous, some run for weeks, some repeat, and some are still in the future with no firm date.  The context event carries planned and actual values for each aspect - *plannedStartDate* / *actualStartDate*, *plannedDuration* / *actualDuration*, *plannedCompletionDate* / *actualCompletionDate* - along with a *repeatInterval* for recurring events.

It also carries *eventEffect*, describing the expected effect on the organization, and *contextEventType*, whose values can be governed as a [valid metadata value](/guides/planning/valid-values/overview) set.

Two further properties, *referenceEffectiveFrom* and *referenceEffectiveTo*, connect the event to [effectivity dates](/features/effectivity-dates/overview) elsewhere in open metadata.  If the context event records the date a new regulation comes into force, that date can be used to switch on the governance definitions that implement the regulation and to switch off the ones it supersedes.

## Connecting the event to its consequences

* *ContextEventImpact* links the event to the resources it affects, with a *severityLevelIdentifier* recording how badly.
* *ContextEventForTimelineEffects* links the event to an [asset](/concepts/asset) or schema attribute whose data was affected.  This is what allows a dip in a server availability data set to be lined up with the power outage that caused it.
* *ContextEventEvidence* links the event to the evidence that it occurred - an alert stored in a file or database, or an [incident report](/concepts/incident-report) raised by a person.
* *DependentContextEvent* links a larger event to the events created as a result of it.  A severe storm warning, for example, spawns dependent events for preparing, riding it out and recovering - each of which explains why data was acquired, capacity requested or services curtailed.
* *RelatedContextEvent* records a possible connection between two events, such as a tsunami and an earthquake detected nearby at a similar time.  Because such connections are often uncertain, the relationship carries *confidence*, a *steward* responsible for verifying it, and *notes*.

Context events are managed by a [project](/concepts/project), [actor](/concepts/actor) or [community](/concepts/community), linked with the *AssignmentScope* relationship, and the actions taken in response - a [to do](/concepts/to-do) for a person, or an [engine action](/concepts/engine-action) for automation - are linked with the *Actions* relationship.  A [note log](/concepts/note-log) can be attached to record the significant steps as the event unfolds.

???+ info "Additional information"
    * The *ContextEvent* type and its relationships are described in [Model 0475 Context Events](/types/4/0475-Context-Events).
    * The [Time Keeper API](/services/omvs/time-keeper/overview) provides the operations for defining context events, linking their evidence, impacts and timeline effects, and relating them to each other.

--8<-- "snippets/abbr.md"
