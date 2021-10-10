<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Open Metadata Exchange Rule

The open metadata exchange rule can be used to limit the exchange of metadata in a cohort.  There are three rules that are configured in each [cohort members](/egeria-docs/concepts/cohort-member):

* *EventsToSend Rule*: controls the events that should be sent to the cohort by the cohort member.

* *EventsToProcess Rule*: controls which incoming events are received by the cohort member from the other members of the cohort.  [Instance events](/egeria-docs/concepts/cohort-events#instance-events) are passed to the:

  * [Open Metadata Access Services (OMASs)](/egeria-docs/services/omas) running in the cohort member.
  * the local repository (if any) where the EventsToSave Rule is run.
  
* *EventsToSave Rule*: controls which of the inbound events received from the cohort and passed by the EventsToProcess Rule should be saved to the local repository.

## Rule values

The open metadata exchange rule can be set to one of the following values:

* `REGISTRATION_ONLY` - Only registration exchange; no TypeDefs or metadata instances
* `JUST_TYPEDEFS` - Only registration and type definitions (TypeDefs) exchange
* `SELECTED_TYPES` - Registration plus all type definitions (TypeDefs) and metadata instances (Entities and Relationships) of selected types.
* `LEARNED_TYPES` - Registration plus all type definitions (TypeDefs) and metadata instances (Entities and Relationships) of types requested by local users to this server.
* `DESELECTED_TYPES` - Registration plus all type definitions (TypeDefs) and metadata instances (Entities and Relationships) NOT listed in selected types.
* `ALL` - Registration plus all type definitions (TypeDefs) and metadata instances (Entities and Relationships).  This is the default setting for all of the rules.

These settings are fairly course-grained.  If you need to control the flow of instance events at a more granular level then the [open metadata security connectors](/egeria-docs/features/metadata security/overview) provide control at the individual 

--8<-- "snippets/abbr.md"