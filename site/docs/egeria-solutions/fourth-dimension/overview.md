<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# The Fourth Dimension

Most catalogs describe the present tense.  They tell you what exists now, and when something changes, the previous answer is gone.  That is a problem whenever the question you need to answer is not about now: what did this data set look like when that report was produced?  What will be in scope when the new regulation takes effect?  Why did the numbers go strange in the second week of March?

Egeria treats time as a dimension of the metadata rather than a property of the moment you happen to ask.  There are three capabilities, and they point in different directions.

## Going backwards: `asOfTime`

Every open metadata repository keeps the history of its elements.  A query can therefore ask for what the repository held at a moment in the past, rather than what it holds now, by supplying the **`asOfTime`** option in the request body.

The time is specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, and defaults to Coordinated Universal Time if no time zone is given.  Passing null - the default - returns the current contents.

The result is the metadata *as it was known then*: the properties an element had at that time, the classifications attached to it, and the relationships that existed.  This is what allows an answer given in the past to be reconstructed and explained:

* A report was produced in April against a data set whose schema has since changed - what were the columns at the time?
* An access decision was made three months ago based on a confidentiality classification that has since been revised - what was it then?
* A lineage graph was used to justify a regulatory submission - what did that graph look like on the day?

Because `asOfTime` reaches into the repository's history rather than an audit log kept alongside it, the answer comes back as ordinary metadata elements, through the same APIs.  It is available on the retrieval operations of the [Metadata Expert](/services/omvs/metadata-expert/overview) API and the other view services built on it.

!!! tip "Two different times"
    `asOfTime` is *repository* time - when the metadata was recorded.  It should not be confused with `effectiveTime`, which is *business* time - when the thing the metadata describes is in force.  A query can use both: what did we know last Tuesday about what would be effective in January?

## Going forwards: effectivity dates

Metadata often needs to describe an arrangement that is not in force yet, or one that has ended but must be kept.  A new organizational structure takes effect at the start of the financial year.  A data sharing agreement runs until a fixed date.  A regulation applies from the moment it commences.

Every element - and every relationship and classification - can carry an **effective from** and an **effective to** date.  Together they define the window in which that element is active, which allows future arrangements to be prepared in advance and past arrangements to be retained without cluttering the present.

Queries then carry an **`effectiveTime`** option stating the moment the results should be effective for.  Null means any effective time; a value returns only what is in force then.  Because the option appears on create, update and delete requests as well, an element being connected to is resolved consistently with the time being worked in.

This is the mechanism that lets an organization stage a change:

* Load the new definitions with an effective-from date in the future.  They are present, reviewable and linked up, but invisible to ordinary queries until the date arrives.
* Set an effective-to date on the definitions they replace, so they retire automatically rather than needing to be deleted on the day.
* Query with an `effectiveTime` in the future to check what the world will look like when the change lands.

??? education "More information"
    [Historical queries and effectivity dates](/features/effectivity-dates/overview) describes the timestamps that provide this time dimension.

## Marking the moments: context events

Knowing what changed is not the same as knowing *why*.  A [context event](/concepts/context-event) records a significant moment or period - instantaneous, lasting, or repeating - that explains anomalies or changes in data and activity.  Examples include a severe weather event, the commencement of a new regulation, the arrival of a data set, or a power outage.

A context event records both what was planned and what happened - `plannedStartDate` and `actualStartDate`, `plannedDuration` and `actualDuration`, `plannedCompletionDate` and `actualCompletionDate` - along with a `contextEventType` and a description of its expected `eventEffect`.  A future event whose exact date is unknown can still be created, so preparation can begin against a placeholder.

What makes context events part of the time dimension rather than just a diary is how they connect to everything else:

| Relationship | What it records |
|--------------|-----------------|
| *ContextEventImpact* | The resources affected by the event, with a severity level - which server needed extra capacity, which system was unavailable. |
| *ContextEventForTimelineEffects* | The data whose *values* the event explains.  Attaching a power outage to a server availability data store means the dip in that data has a reason attached to it. |
| *ContextEventEvidence* | The alerts, notifications or [incident reports](/features/incident-reporting/overview) that show the event occurred or is expected. |
| *DependentContextEvent* | Events spawned by a larger one - preparing for the storm, riding it out, recovering from it. |
| *RelatedContextEvent* | Events that may be connected, with a confidence level and a steward responsible for verifying the association. |

The link back to effectivity dates is direct: a context event carries `referenceEffectiveFrom` and `referenceEffectiveTo` properties supplying the dates to use on the elements whose effectivity that event triggers or ends.  The event that records when a regulation comes into force therefore also supplies the effective-from date for every governance definition that commences with it - so the moment is recorded once and applied consistently.

Context events are maintained through the [Time Keeper](/services/omvs/time-keeper/overview) API, and can be managed by a project, an actor or a community, with [to-dos](/concepts/to-do) and engine actions attached for the work they require.

## Using the three together

The three capabilities answer different halves of the same class of question, and they are strongest in combination:

* `asOfTime` reconstructs what the ecosystem knew at a point in the past.
* Effectivity dates describe what is - or will be - in force, independently of when it was recorded.
* Context events explain why the picture changed when it did, and supply the dates that drive the change.

Together they mean that a question like *"why did this report change between March and April, and was that expected?"* is answerable from the metadata: retrieve both versions with `asOfTime`, compare what was effective in each period, and look for the context event that covers the interval.

!!! info "Related information"

    * [Historical queries and effectivity dates](/features/effectivity-dates/overview)
    * [Model 0475 Context Events](/types/4/0475-Context-Events) - the full set of context event types and relationships.
    * [Context event](/concepts/context-event) concept and the [Time Keeper](/services/omvs/time-keeper/overview) API.
    * [Finding metadata](/guides/developer/finding-metadata/overview) - the query options, including `effectiveTime`, `forLineage` and `forDuplicateProcessing`.

--8<-- "snippets/abbr.md"
