<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Cohort events

*Cohort events* are messages used to notify [members of an open metadata repository cohort](/egeria-docs/concepts/cohort-members) of changes to:

- The membership of the open metadata repository cohort.
- The types of metadata being managed by members of the open metadata repository cohort.
- The changes to the metadata instances stored by each of the members of the open metadata repository cohort.

The motivation for sending cohort events between the members of the cohort is to ensure open metadata is as widely available as security permits and access to it is as efficient as possible.  The events are broadcast to the membership of the open metadata repository cohort through one or more [cohort event topic(s)](#cohort-topics) and no replies are expected. Each member is expected to receive each event and make a [local decision](/egeria-docs/concepts/open-metadata-exchange-rule) on whether to act on it or ignore it.

## Cohort topics

A cohort can be configured to use:

- One cohort event topic for all types of cohort events
- Three cohort event topics, one for each type of OMRS event
- Both options

This is shown in figure 1.



!!! question "Which to use?"
    Using the single cohort topic is ok for small environments. However, the use of the three topics gives
    the best throughput, ensures rapid inclusion of new members in the cohort and is required for clustered members:
    when multiple instances of the same member operate in a cohort for high availability (HA).

??? attention "Notes for cohorts involving members at versions prior to 2.11"
    Versions of the OMRS prior to release 2.11 only support the single cohort topic.
    To allow a server running an older version of OMRS to join a cohort using the three topics, it is possible to
    configure the other members to use both the single topic and the three topics.

    This ensures all members see the same metadata, but the members configured to use both options will process
    all events twice. This configuration should only be used when absolutely needed and attention should be
    paid to upgrading the back-level server so it can use the three topics.

Details of configuring the different topic options can be found in the
[administration guide](/egeria-docs/guides/admin/guide).

## Enterprise event topic

The enterprise event topic combines the cohort events from all cohorts that the server is connected to and makes them available to each local [Open Metadata Access Service (OMAS)](/egeria-docs/services/omas).  It runs in memory but can be configured to also push these events to a topic managed by an event broker.

## Cohort event types

![OMRS event format (version 1)](cohort-event-format.png)

Every event has a:

- Timestamp - indicating the time the event was created.
- Originator - detailing the server that originated the message.
    - The [metadata collection id](/egeria-docs/concepts/metadata-collection-id) of the sending open metadata repository's metadata collection.  (The only time this is not set is when a message is sent from a server that does not have a local metadata repository configured.)
    - The server name, type and organization are optional descriptive fields used in audit logging and problem determination. These values are set up through the [administration services](/egeria-docs/guides/admin/guide).
- Version - the version number of the event (set to `OMRS V1.0` in the initial version).

The setting of the category determines which category-specific section is used. Each category-specific section begins with a category-specific event type that describes the type of the event, and hence the properties that will be found in the category-specific section.

If the event is reporting an error, there is also an optional error section.  The error section has an error code, error message and a target [metadata collection id](/egeria-docs/concepts/metadata-collection-id).  The target metadata collection id indicates which member of the cohort is the target for the error message.  Other members may pick up the error and act on it as well.

### Registry events

Registry events are used by metadata servers to register with a cohort.

![Figure 2](cohort-registry-event-formats.png)
> Figure 2: Different formats of a registry event

### TypeDef events

TypeDef events are used by members of a cohort to exchange information about the [open metadata types](/egeria-docs/types) they support.

![Figure 3](cohort-typedef-event-formats.png)
> Figure 3: Different formats of a TypeDef event


### Instance events

Instance events are used by members of a cohort to exchange information about changes to metadata instances.

![Figure 4](cohort-instance-event-formats.png)
> Figure 4: Different formats of an instance event

--8<-- "snippets/abbr.md"
