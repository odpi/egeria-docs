<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->


# 0795 - Usage Activity

The classifications below are used to gather statistics about usage activity around an element.  They are maintained by Egeria's [metadata observability](/features/metadata-observability/overview) capability.

![UML](0795-Usage-Activity.svg)

## UsageActivity classification

The *UsageActivity* classification describes the usage activity around an anchor element and its anchored elements: how often it is explicitly retrieved, found through searches, has its properties updated, and has its attachments and feedback updated or deleted.  It can be attached to any [Referenceable](/types/0/0010-Base-Model), and is typically found on an [Asset](/types/0/0010-Base-Model), a [DigitalProduct](/types/7/0710-Digital-Products) or a [GlossaryTerm](/types/3/0330-Terms).

Each kind of activity has its own count:

* *explicitGetCount* - the number of times the element, or one of its anchored elements, has been explicitly retrieved from the repository by an identifier or name.  This indicates that it is an element of specific interest to the calling user.
* *findCount* - the number of times the element, or one of its anchored elements, has been retrieved from the repository as part of a search request.  This indicates the element's findability.
* *updatePropertyCount* - the number of times the properties of the element have been updated.
* *updateAttachmentCount* - the number of times an element anchored to the element has been created, linked, unlinked or updated.
* *updateFeedbackCount* - the number of times [feedback](/concepts/feedback) (comments, likes, ratings and informal tags) attached to the element has been added or updated.
* *deleteAttachmentCount* - the number of times an element anchored to the element has been deleted.
* *deleteFeedbackCount* - the number of times feedback (comments, likes, ratings and informal tags) attached to the element has been deleted.

All of the counts are *long* values.

### How the counts are maintained

The UsageActivity classification is maintained by the *Pepys Activity Observer* integration connector.  Each metadata access server writes an activity message to its [audit log](/concepts/audit-log) whenever a request touches an asset, digital product or glossary term, or an element [anchored](/concepts/anchor) to one of them.  Pepys listens to the servers' audit log topics and adds each message to the count for its kind of activity:

| Message                                | Activity                                                                              | Count                   |
|----------------------------------------|---------------------------------------------------------------------------------------|-------------------------|
| METADATA-OBSERVABILITY-0002, -0003     | The anchor element, or an element anchored to it, was retrieved by identifier or name | *explicitGetCount*      |
| METADATA-OBSERVABILITY-0008, -0009     | The anchor element, or an element anchored to it, was returned by a search            | *findCount*             |
| METADATA-OBSERVABILITY-0006            | The properties of the anchor element were updated                                     | *updatePropertyCount*   |
| METADATA-OBSERVABILITY-0004            | An element anchored to the anchor element was created, linked, unlinked or updated    | *updateAttachmentCount* |
| METADATA-OBSERVABILITY-0005            | Feedback (comments, likes, ratings and informal tags) was added or updated            | *updateFeedbackCount*   |
| METADATA-OBSERVABILITY-0007            | An element anchored to the anchor element was deleted                                 | *deleteAttachmentCount* |
| METADATA-OBSERVABILITY-0011            | Feedback was deleted                                                                  | *deleteFeedbackCount*   |

The creation of an anchor element (METADATA-OBSERVABILITY-0001) is not counted.  Pepys gathers the counts in memory and adds them to each element's UsageActivity classification on every refresh, so the counts are cumulative.  The activity of non-personal accounts, governance engines and Pepys itself is ignored, so that the counts reflect the activity of people and external tools.  See [The Pepys Activity Observer](/features/metadata-observability/overview#the-pepys-activity-observer) for details of its configuration.

## MemberPopularityProfile classification

The *MemberPopularityProfile* classification summarizes the usage activity around the members of an element, both in total and member by member, for each kind of activity.  It can be attached to any [Referenceable](/types/0/0010-Base-Model) that has members.  The *Lovelace Popularity Profiler* maintains it on [collections](/types/0/0021-Collections) - root collections, glossaries, data sharing hubs, collection folders and digital product catalogs - by totalling the *UsageActivity* counts of their members.  See [The Lovelace Popularity Profiler](/features/metadata-observability/overview#the-lovelace-popularity-profiler) for how a profile is built.

For each of the seven *UsageActivity* counts, the classification has a *Total* (a *long*) and a *Profile* (a *map&lt;string, long&gt;*):

* *explicitGetCountTotal* - the number of times any of the members has been explicitly retrieved from the repository by an identifier or name.
* *explicitGetCountProfile* - a map of member GUID to the number of times that member has been explicitly retrieved from the repository by an identifier or name.
* *findCountTotal* - the number of times any of the members has been retrieved from the repository as part of a search request.
* *findCountProfile* - a map of member GUID to the number of times that member has been retrieved from the repository as part of a search request.
* *updatePropertyCountTotal* - the number of times any of the members has had its properties updated.
* *updatePropertyCountProfile* - a map of member GUID to the number of times that member has had its properties updated.
* *updateAttachmentCountTotal* - the number of times any of the members has had an element anchored to it created, linked, unlinked or updated.
* *updateAttachmentCountProfile* - a map of member GUID to the number of times that member has had an element anchored to it created, linked, unlinked or updated.
* *updateFeedbackCountTotal* - the number of times any of the members has had feedback (comments, likes, ratings and informal tags) added or updated.
* *updateFeedbackCountProfile* - a map of member GUID to the number of times that member has had feedback (comments, likes, ratings and informal tags) added or updated.
* *deleteAttachmentCountTotal* - the number of times any of the members has had an element anchored to it deleted.
* *deleteAttachmentCountProfile* - a map of member GUID to the number of times that member has had an element anchored to it deleted.
* *deleteFeedbackCountTotal* - the number of times any of the members has had feedback (comments, likes, ratings and informal tags) deleted.
* *deleteFeedbackCountProfile* - a map of member GUID to the number of times that member has had feedback (comments, likes, ratings and informal tags) deleted.



--8<-- "snippets/abbr.md"
