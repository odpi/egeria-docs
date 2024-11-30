<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# Community Profile Open Metadata Access Service (OMAS)

The Community Profile OMAS provides APIs and events for tools and applications that are managing information about people and the way they work together.

In particular the Community Profile OMAS supports [personal profiles](/concepts/personal-profile), [organizations](/concepts/organization) and [teams](/concepts/organizations/#teams) along with  [communities](/concepts/community) of people collaborating around data.

With this information, open metadata reduces the friction between people from different silos of an organization that can prevent the effective use of data. For example, an [Asset Owner](/concepts/person-role/#asset-owner) can monitor who is using their [asset](/concepts/asset) and for what purposes.   At the same time, [consumers or assets](/concepts/person-role/#asset-consumer), such as a data scientist or business analyst, can find out which assets their colleagues are using, and any feedback that they gave, which helps to guide them to the most appropriate assets for their work.

## Is this metadata ?

Data about people and organizations is not strictly metadata.  It is main data.  This means it is a type of data that is widely duplicated across an organization's systems but mercifully slowly changing.  Open metadata is therefore only one of many systems making use of this data.

Many organizations use a centralized user directory, such as LDAP, for their employees. In addition large organizations with thousands of systems may also have a main data management (MDM) program to keep their data about people and organization's synchronized amongst their systems.

With or without MDM, it is important that the Community Profile OMAS can operate as a downstream consumer of this data, rather than operating as an independent island. This way it adds value to the organization by enabling the recording of asset ownership, use and feedback, without an excessive amount of additional administration.

## Using the Community Profile OMAS

The Community Profile OMAS may be called directly through its [Java client](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/communityprofile/client/package-summary.html).  This will call the Community Profile OMAS REST API running in the requested [metadata access server](/concepts/metadata-access-server).

The Community Profile OMAS is designed to cover many of the administrative tasks relating to managing information about people, teams and communities.

Most of the interaction with the Community Profile OMAS will be driven by individuals.

- All users will be able to manage their [personal profile](/concepts/personal-profile) and [lists of favourite assets, projects and communities](/concepts/favorite-things-collection).

- All users will be able to manage any [to dos](/concepts/to-do) that have been assigned to them.

- All users will be able to create a [community](/concepts/community) and administer it. This includes managing members, the communities resources and the notifications sent to the members.

- All users can also query the [communities](/concepts/community) and [teams](/concepts/organization/#team.md) they are a member of.

- All users will be able to search for people, teams and communities.

There is also support for an administrator to create and delete personal profiles as individuals join and leave the organization and also manage the organization's departmental structure.  The assumption is that the organization already has at least one system that manages this information, and so Community Profile OMAS is designed to be integrated with existing systems in order to keep the profiles and departmental structure up-to-date.


The Community Profile OMAS running in the [metadata access server](/concepts/metadata-access-server) is also monitoring changes to open metadata. It will emit an [event](/concepts/out-topic) whenever profile, organizational or community related metadata is created or changed in some way.  The java client provides a mechanism for third party technology to register a listener to receive these events.


## Karma points 

If an actor has an [Actor Profile](/types/1/0110-Actors), the Community Profile OMAS will reward him/her/it whenever they contribute to open metadata. These rewards are in the form of [karma points](/concepts/karma-point).

The Community Profile OMAS is responsible for maintaining the count of the karma points for an actor based on their contributions to open metadata.  It does this by listening to the metadata changes occurring in the metadata repositories and updates the personal profile of each user making a contribution.

The Community Profile OMAS java client provides a method to retrieve the current karma point total for an individual.

The access service option property *KarmaPointPlateau* indicates the multiple of karma points for an individual that results in an external event being published - the default is 500.  This means that when an individual gets to 500 karma points, an event is sent on the Community Profile OMAS Out Topic, and other event is sent when they get to 1000 karma points and so on. These events can be used to trigger additional recognition activities for the individuals concerned.

## Automated exchange of metadata about people, organizations and communities

The [Organization Integrator OMIS](/services/omis/organization-integrator/overview) supports [integration connectors](/concepts/integration-connector) that manage the exchange of metadata about people, organizations and communities with third party systems.



--8<-- "snippets/abbr.md"
