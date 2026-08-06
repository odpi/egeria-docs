---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/tech-preview.md"

# Watchdog Action Open Metadata Engine Service (OMES)

The Watchdog Action OMES provides support for [watchdog action engines](/concepts/watchdog-action-engine) that are part of the [Open Watchdog Framework (OWF)](/frameworks/owf/overview).

## Watchdog action engines

A watchdog action engine hosts specialized governance services called [watchdog action services](/concepts/watchdog-action-service).

The Watchdog Action OMES is capable of hosting one or more [watchdog action engines](/concepts/watchdog-action-engine), and supports a REST API to request that a watchdog action engine starts a watchdog action service and to check on its progress and results.  If/when the situation being watched for occurs, a notification/action is issued to each subscriber, depending on their type.

The watchdog action engine services call the services running in a Metadata Access Server to retrieve information about the resources being monitored, and to record the notifications that the watchdog action services send.

## Long-running by design

Unlike the [Survey Action OMES](/services/omes/survey-action/overview) and [Governance Action OMES](/services/omes/governance-action/overview), whose hosted services are expected to run briefly and complete, the Watchdog Action OMES expects the watchdog action services it hosts to keep running for as long as the situation they are watching for might occur - potentially indefinitely.  If the engine host server is restarted, its watchdog action services are restarted too, rather than being left incomplete.  This is a deliberate design choice - see [Open Watchdog Framework (OWF)](/frameworks/owf/overview) for why watching for change was given its own engine service, separate from the rest of governance action processing.

--8<-- "snippets/abbr.md"
