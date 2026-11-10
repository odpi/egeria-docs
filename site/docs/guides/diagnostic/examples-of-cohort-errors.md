<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Examples of problems with an Open Metadata Repository Cohort

Members of an [open metadata repository cohort](/concepts/cohort-member) exchange registrations, type definitions and metadata changes over the cohort's Kafka topics: `<topicURLRoot>.openmetadata.repositoryservices.cohort.<cohortName>.OMRSTopic.registration`, `.types` and `.instances`.  Most cohort problems are therefore event bus problems, and start with the [Kafka diagnostics](/guides/diagnostic/postgresql-and-kafka-diagnostic-guide#apache-kafka).

Use the [cohort diagnostic APIs](/guides/diagnostic/diagnostic-apis#cohorts) to see what each member believes: its cohort descriptions, its own registration, and the remote members it knows about.

| Symptom | Likely cause | What to do |
|---|---|---|
| A server does not appear in the other members' remote member lists | It cannot reach Kafka, is using a different cohort name or `topicURLRoot`, or its registration events are not being read. | Check `OCF-KAFKA-TOPIC-CONNECTOR` messages on the new member, and compare its topic names with the existing members' (`kafka-topics.sh --list`). |
| A member that was removed still appears | It was shut down without unregistering. | Unregister it (`RuntimeManager.unregister_from_cohort()` or `.../cohort-members/{serverGUID}/cohorts/{cohortName}/unregister`), or shut it down with *shutdown and unregister* if it is being removed permanently. |
| `Cohort` records report a type conflict | Two members have different definitions for the same type, usually because they run different releases. | Bring the members to the same release, or at least to compatible type definitions. |
| Metadata created on one member is not visible on another | The `.instances` topic is not being consumed, or the receiving member's consumer group is behind. | Check the receiving member's consumer group lag on the instances topic. |
| A member rejoins and receives a flood of old events | Its consumer group was deleted, or it got a new server identifier, so it started reading from the beginning of the topic. | Expected after the configuration is recreated; it settles once it has caught up. |

Disconnecting a server from a cohort (`.../cohorts/{cohortName}/disconnect`) stops the exchange but keeps its registration, so it can rejoin cleanly; unregistering removes it from every member's registry.

--8<-- "snippets/abbr.md"
