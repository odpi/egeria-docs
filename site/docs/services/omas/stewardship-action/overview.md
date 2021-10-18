<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/in-development.md"

# Stewardship Action Open Metadata Access Service (OMAS)

The Stewardship Action OMAS provides APIs and events for tools and applications focused on resolving issues detected in the data landscape that need a human steward to resolve.

It works in partnership with the [governance engines](/egeria-docs/concepts/governance-engine) running in [engine host servers](/egeria-docs/concepts/engine-host) to execute functions that detect, report on and implement the resolution of issues. These functions are called *[governance actions](/egeria-docs/concepts/governance-actions)*.

For example, when a change is detected in an Asset metadata entity, the governance engine may run a governance action associated with that asset. These could be:

- detect and emit an event if a new asset is created without an owner.
- create an entry in a maintenance NoteLog to record each change to the Asset.

Some actions require judgement and this is where the human steward comes in.  The [triage governance action](governance-service) creates a [to do](/egeria-docs/concepts/to-do).  This is picked up by the Stewardship Action OMAS that generates an event on its [OutTopic](/egeria-docs/concepts/out-topic).  This may be received by an external human task manager or the [Stewardship Integrator OMIS](/egeria-docs/services/omis/stewardship-integrator) to push to the human task manager.  The Stewardship Action OMAS provides APIs to perform the requested action and manage the to do through its lifecycle.

--8<-- "snippets/abbr.md"
