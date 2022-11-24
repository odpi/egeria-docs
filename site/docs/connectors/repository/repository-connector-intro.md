
The [repository connector](/concepts/repository-connector), and its optional [event mapper connector](/concepts/event-mmapper-connector) provide the ability to integrate a metadata repository into the open metadata ecosystem.  These connector have direct access to the connected [open metadata repository cohorts](/concepts/cohort-member).  There are two patterns of use for these connectors. 

In the first pattern, called the *native repository connector*, the [repository connector](/concepts/repository-connector) delegates all of its methods to a particular type of persistence store.  Metadata is only accessible through the Egeria APIs and it is stored as entities, relationships and classifications enabling it to support any valid type of open metadata. This type of repository connector runs as the local repository  within an Egeria [Metadata Access Store](/concepts/metadata-access-store) server.

![Native open metadata repository](/connectors/repository/native-repository-connector.svg)
> Repository connector supporting a native open metadata repository

In the second pattern, called the *adapter repository connector*, the repository connector, and an optional [event mapper connector](/concepts/event-mapper-connector), provide an adapter for a third party metadata repository so it can be a part of the open metadata ecosystem.  These connectors run in a [Repository Proxy](/concepts/repository-proxy) server.

![Adapter repository connectors](/connectors/repository/adapter-repository-connector.svg)
>  Repository connector and optional event mapper connector supporting an adapter to a third party metadata repository


--8<-- "snippets/abbr.md"


