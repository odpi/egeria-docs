<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Metadata events

**OMRS events** are messages used to notify [members](../cohort/#cohort-members) of
an [open metadata repository cohort](../cohort)
of changes to:

- The membership of the open metadata repository cohort.
- The types of metadata being managed by members of the open metadata repository cohort.
- The changes to the metadata instances stored by each of the members of the open metadata repository cohort.

The motivation for sending OMRS events between the members of the open metadata repository cohort
is to ensure open metadata is as widely available as security-permitted and access to it is as efficient as possible.
The events are broadcast to the membership of the open metadata repository cohort through
one or more [OMRS event topic(s)](#omrs-event-topic) and no replies are expected.
Each member is expected to receive each event and make
a [local decision](../open-metadata-exchange-rule.md) on whether
to act on it or ignore it.

## OMRS event topic

The **OMRS event topic(s)** are one or more [topics](../../../basic-concepts/#topic)
provided through an [event broker](../../../basic-concepts#event-broker) (typically Apache Kafka)
that an [open metadata repository cohort](../cohort) uses to synchronize metadata
between metadata repositories.

They are accessed by the [Open Metadata Repository Services (OMRS)](../../omrs)
components through the [OMRS topic connector](component-descriptions/connectors/omrs-topic-connector.md).

The OMRS topic connector is a pluggable [OCF](../../frameworks/ocf.md) connector
that allows the use of different messaging infrastructures to
support the OMRS event topic(s) without affecting the implementation of the OMRS.

## OMRS events

The [OMRS event topic](#omrs-event-topic) is used to send and receive **OMRS events**.
There are [three types of OMRS events](#event-types) that are sent/received on the OMRS event topics:
_TypeDef events_ and _instance events_ are collectively called _repository events_
because they affect the contents of the open metadata repositories.

## Cohort topic(s)

A cohort can be configured to use:

- One [OMRS event topic](#omrs-event-topic) for all types of OMRS events
- Three [OMRS event topics](#omrs-event-topic), one for each type of OMRS event

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
[administration guide](../../guides/admin/configuring-registration-to-a-cohort.md).

## Enterprise OMRS event topic

The [enterprise repository services](../../omrs/#enterprise-repository-services)
combine the [OMRS events](#omrs-events) from all [open metadata repository cohorts](../cohort)
that the server is connected to and makes them available to each local
[Open Metadata Access Service (OMAS)](../omas.md).  This is called the
**enterprise OMRS event topic**. By default, it is implemented as an
[in-memory open metadata topic](../../adapters/open-connectors/event-bus-connectors/open-metadata-topic-connectors/inmemory-open-metadata-topic-connector).

## Event types

![OMRS event format (version 1)](event-format.png)

Every event has a:

- Timestamp - indicating the time the event was created.
- Originator - detailing the server that originated the message.
    - The [metadata collection ID](../metadata-repositories/#metadata-collection-id) of the sending open metadata repository's metadata collection.
      (The only time this is not set is when a message is sent from a server that does not have a
      local metadata repository configured.)
    - The server name, type and organization are optional descriptive fields used in audit logging and problem determination.
      These values are set up through the [administration services](../../guides/admin/user).
- Version - the version number of the event (set to `OMRS V1.0` in the initial version).

The setting of the category determines which category-specific section is used.
Each category-specific section begins with a category-specific event
type that describes the type of the event, and hence the properties that
will be found in the category-specific section.

If the event is reporting an error, there is also an optional error section.
The error section has an error code, error message and a target [metadata
collection ID](../metadata-repositories/#metadata-collection-id).  The target metadata collection ID
indicates which member of the cohort is the target for the error message.
Other members may pick up the error and act on it as well.

### Registry events

Registry events are used by metadata servers to register with an
[open metadata cohort](../cohort).

![Registry events](registry-event-formats.png)

### TypeDef events

TypeDef events are used by members of an
[open metadata cohort](../cohort)
to exchange information about the
[open metadata types](../../../types)
they support.

![TypeDef events](typedef-event-formats.png)

### Instance events

Instance events are used by members of an
[open metadata cohort](../cohort)
to exchange information about changes to metadata instances.

![Instance events](instance-event-formats.png)

--8<-- "snippets/abbr.md"
