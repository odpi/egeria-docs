<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# Feedback Manager API

The Feedback Manager API provides the ability to retrieve and maintain feedback
about metadata elements. Feedback includes informal tags, comments, ratings and likes.
It also supports note logs.

## Key features

* **Comments**: Adding, updating, and removing comments attached to metadata elements.
  It also supports marking a comment as the "accepted answer" to a question.
* **Ratings and Likes**: Expressing sentiments about metadata elements through ratings (stars) or simple likes.
* **Informal Tags**: Creating and managing informal tags that can be attached to any metadata element
  for personal organization or community-driven categorization.
* **Note Logs**: Managing logs of notes (activity logs, journals, etc.) that can be anchored to metadata elements
  or exist independently.

## Further information

* [Informal Tag Concept](/concepts/informal-tag/)
* [Comment Concept](/concepts/comment/)
* [Rating Concept](/concepts/rating/)
* [Like Concept](/concepts/like/)
* [Note Log Concept](/concepts/note-log/)

----
Sample REST API requests can be found in [Egeria-api-feedback-manager.http](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/view-server-generic-services/feedback-manager/Egeria-api-feedback-manager.http).

---8<-- "snippets/abbr.md"






