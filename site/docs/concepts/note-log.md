<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Note log

A *note log* is an attachment to a [referenceable](/concepts/referenceable) that acts as a series of ordered notes.  The entries in a note log are [actions](/concepts/action).

Note logs are used to record what happened, in order, alongside the thing it happened to.  A [context event](/concepts/context-event) carries a note log of the significant steps as the event unfolds; a [project](/concepts/project) carries one for its meeting notes and decisions; an [asset](/concepts/asset) carries one for the significant changes made to it.  Because the entries are ordered and timestamped, the log reads as a narrative rather than as a set of unrelated comments.

An individual note can be marked with the [isPublic](/concepts/is-public) flag, giving the author control over whether it is shared with colleagues.


???+ info "Additional information"
    * The type definitions for a note log are found in [Model 0160 Notes](/types/1/0160-Notes).
    * The [Feedback Manager API](/services/omvs/feedback-manager/overview) provides the operations for maintaining note logs and their entries.


--8<-- "snippets/abbr.md"