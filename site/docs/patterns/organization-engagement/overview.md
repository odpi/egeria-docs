<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Organization Engagement

The knowledge that makes an open metadata ecosystem valuable is spread across the whole organization.  The people who understand what a data field really means, which regulation applies to a process, or why a system was built the way it was, are rarely the people running the metadata catalog.  They are busy doing their own jobs.

The *Organization Engagement* pattern is about closing that gap.  It covers the capabilities that describe your organization in open metadata, connect responsibilities to the individuals who hold them, bring people together in communities, and lower the effort of contributing to the point where a subject-matter expert can add their knowledge as part of their normal work.

## Describing the organization

Before people can be engaged, the organization itself needs to be described.  Egeria captures this from two complementary directions: how the organization is *staffed*, and what the organization *does*.

???+ info "The structure of the organization"
    [People, roles and organizations](/features/people-roles-organizations/overview) describes how an organization is represented in open metadata.  Individuals are represented by a *Person* profile, groups by a *Team* profile, and automated processes by an *ITProfile*.  Teams are organized into one or more hierarchies that reflect how the work has been divided up.

    ![The structure of an organization](/features/people-roles-organizations/organization-structure.svg)
    > The top-level organization is linked to its top-level teams, with sub-teams nested beneath them.  Each team has leader and member roles, and roles can have multiple people appointed to them.

    Profiles are linked to the *UserIdentity* entities that represent the user accounts a person or process uses.  This is what allows an action recorded in an IT system to be traced back to the person or process that performed it, and it is the foundation for [linking governance and security to roles](/features/people-roles-organizations/overview/#linking-governance-and-security-to-roles).

    The organization structure is maintained through the [People Organizer](/services/omvs/people-organizer/overview) API, with the profiles themselves managed by the [Actor Manager](/services/omvs/actor-manager/overview) API, and an individual's own view of their profile, actions and responsibilities provided by the [My Profile](/services/omvs/my-profile/overview) API.

???+ info "The business the organization is in"
    Alongside the people and teams sits a description of the business itself.  [Model 0715 Digital Business](/types/7/0715-Digital-Business) defines *BusinessCapability* to describe the responsibilities and services an organization has, structured as business domains, business areas and business services, and linked to the team that owns them.

    The *DigitalSupport* relationship then connects a business capability to the [assets](/concepts/asset) and [digital products](/concepts/digital-product) that support it, which is what allows a question such as "what does this system actually do for the business?" to be answered from the catalog rather than from memory.  The *AccountingCodes* classification records the accounting codes associated with an element, so the cost of an activity can be tracked alongside it.

    This business context is maintained through the [Digital Business](/services/omvs/digital-business/overview) API.

!!! summary "Usage"
    With both perspectives in place, the catalog can describe not just what exists, but who is responsible for it and which part of the business depends on it.  These are the two questions that turn a metadata repository into something the organization uses to run itself.

## Engaging the individual through roles

A description of an organization is not, by itself, engaging.  What engages an individual is being named.

Egeria represents responsibilities as [roles](/concepts/person-role) - effectively slots, or vacancies, in a team, project or community - that individuals are appointed to for a span of time.  A role has a scope: someone is a manager of a specific team, or the owner of specific systems, not of everything.  A role can have several people appointed to it, and the [appointment history](/features/people-roles-organizations/overview/#appointment-history) is retained, so it is possible to see who held a responsibility at a point in the past.

![Roles that an individual plays](/features/people-roles-organizations/tessa-tubes-roles.svg)
> An experienced person typically holds several roles at once, each with its own scope, skills and call on their time.

Roles are what connect a governance definition to a person's working day.  A governance responsibility that is written down but not assigned is a document; the same responsibility attached to a role, with a named appointee, is somebody's job.  The same mechanism drives the [to-dos](/concepts/to-do) that Egeria assigns when a governance action needs a human decision, and the notifications and subscriptions managed through the [Notification Manager](/services/omvs/notification-manager/overview) API that tell someone their attention is needed.

??? education "More information"
    * [ActorRole](/types/1/0118-Actor-Roles) and the [governance roles](/types/4/0445-Governance-Roles) that specialize it.
    * From release 6.1, the specific subtypes of *PersonRole* and *GovernanceRole* are deprecated in favour of the *actorRoleGroups* attribute, with the standard groupings supplied as valid metadata values in the Core Content Pack.  This makes it easier to define role types that suit your organization without extending the type system.

## Building communities

Some work does not belong to any single team.  Cross-cutting initiatives - governance programs, sustainability, data literacy - need people from across the organization who volunteer their time and expertise alongside their day job.

A [community](/concepts/community) is the anchor point for this kind of long-running, cross-organization endeavour.  Communities have members with graded roles - observer, contributor, administrator and leader - so people can participate at the level they are able to.  They gather forums for discussion, collections of useful resources and external references, and the ordinary feedback mechanisms of comments, replies, reviews, tags and likes.

Communities are maintained through the [Community Matters](/services/omvs/community-matters/overview) API, their contributions and discussion through the [Feedback Manager](/services/omvs/feedback-manager/overview) API, and the work they spawn through the [Project Manager](/services/omvs/project-manager/overview) API.

!!! summary "Usage"
    A community gives an initiative a home: somewhere to ask questions, share progress and celebrate results.  It is also how expertise is found, since the membership list of a community is a far better guide to who cares about a topic than any org chart.

## Connecting people to the governance domains

A [governance domain](/concepts/governance-domain) is an area of governance that needs collaboration across the organization, and so cannot simply be handed to one team.  Each domain is typically led by an executive, supported by a community, and delivered through projects.

This is where the previous three sections come together.  A governance domain has:

* **Governance definitions** - the drivers, policies and controls that describe what the domain is trying to achieve.  These are maintained through the [Governance Officer](/services/omvs/governance-officer/overview) API.
* **Roles** - the governance officer who leads the domain, and the owners, stewards and custodians who carry its responsibilities, each linked to the appointees who hold them.
* **A community** - to bring the people working in the domain together for education, status updates and discussion.
* **A scope** - the teams, business capabilities and resources the domain's definitions apply to.

Governance domains are defined as [valid metadata values](/guides/planning/valid-values/overview) referenced by the `domainIdentifier` property, so an organization can add domains of its own to the standard set.  This means the different governance domains can operate with their own leadership, terminology and priorities, while still sharing one description of the organization and one catalog of resources.

??? education "More information"
    [Planning for a governance program](/guides/planning/governance-program/overview) works through the setting up of a governance program in detail.

## Making it easy to contribute

None of this works if contributing is hard.  Subject-matter experts will not learn a metadata tool, and they should not have to.

[Literate governance](/concepts/literate-governance) is Egeria's answer.  Borrowing from Donald Knuth's *literate programming*, it lets governance officers, stewards and experts author a single document that explains *why* something exists in plain language, right next to the commands that *create* it.  [Dr.Egeria](/user-interfaces/dr-egeria/overview) processes these Markdown documents and creates the corresponding definitions in Egeria's knowledge graph.

![The literate governance process](/concepts/literate-governance-process.png)

Because the document is ordinary human-readable Markdown, it can be drafted in any editor, circulated for peer review, argued over, corrected and reprocessed as many times as it takes.  The command language includes report requests, so the author can check that what they intended is what actually got loaded.  The result is that the artefact people collaborate on and the artefact that configures the ecosystem are the same artefact.

Dr.Egeria is not the only low-effort route in:

* [My Egeria](/user-interfaces/my-egeria/overview) supports the multi-step tasks people perform - working through to-dos, meetings, reviews, and the management of their roles, communities and teams - as either a terminal or browser application.
* [Egeria Explorer](/user-interfaces/egeria-explorer/overview) and [The Catalog](/user-interfaces/the-catalog/overview) let people find and read the metadata without needing to know where it is stored.
* The [Feedback Manager](/services/omvs/feedback-manager/overview) API supports the smallest contributions of all - a comment, a tag, a rating - which are often where engagement starts.

## Engagement in practice

The [Coco Pharmaceuticals scenarios](/practices/coco-pharmaceuticals) show these capabilities being used together:

* [Building the multi-faceted governance team](/practices/coco-pharmaceuticals/scenarios/building-the-governance-team/overview) follows [Jules Keeper](/practices/coco-pharmaceuticals/personas/jules-keeper) as he realizes he cannot fix Coco Pharmaceuticals' problems from the data governance domain alone.  He and his colleagues divide the work across governance domains, appoint a leader to each, and capture their governance drivers as Dr.Egeria documents so that the whole leadership team can review and build on them.

* [Initiating a sustainability initiative](/practices/coco-pharmaceuticals/scenarios/sustainability-initiative/overview) shows a cross-organization program being built from scratch: a new governance domain added to the standard set, a small team drawn from finance, manufacturing and information architecture, executive sponsors, and a community that reaches the parts of the business the team does not.

!!! info "Related information"

    * [People, roles and organizations](/features/people-roles-organizations/overview) - the full description of profiles, roles, teams and their link to security.
    * [Community](/concepts/community) and [model 0140 Communities](/types/1/0140-Communities) - communities, their roles and their forums.
    * [Governance domain](/concepts/governance-domain) - what a governance domain is and how domains are defined.
    * [Literate governance](/concepts/literate-governance) - the philosophy behind Dr.Egeria's Markdown documents.

--8<-- "snippets/abbr.md"
