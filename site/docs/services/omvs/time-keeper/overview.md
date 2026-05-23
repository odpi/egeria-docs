<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# Time Keeper API

The Time Keeper API enables the caller to define and manage context events.
[Context events](/concepts/context-event/) are used to record significant events
that affect the performance of systems, people and organizations - and hence impact data values.

## Key Features

The Time Keeper API provides the following capabilities:

- **Context Event Management**: Support for creating, updating, and deleting context events,
  including creation from templates to ensure consistency across the ecosystem.
- **Hierarchical and Related Events**: Capabilities for linking context events together
  to represent dependent or related event structures.
- **Evidence Tracking**: Linking context events to the evidence (e.g., reports, logs)
  that confirms the event occurred.
- **Impact Analysis**: Associating context events with the metadata elements they impact,
  helping users understand the scope of an event's influence.
- **Timeline Effects**: Linking context events to elements whose timeline or performance
  is affected by the event.
- **Search and Discovery**: Finding context events by name, search strings, or GUIDs.

## Further information

- [Context Event Concept](/concepts/context-event/)

Sample REST API requests can be found in
[Egeria-api-time-keeper.http](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/view-server-generic-services/time-keeper/Egeria-api-time-keeper.http).

---8<-- "snippets/abbr.md"






