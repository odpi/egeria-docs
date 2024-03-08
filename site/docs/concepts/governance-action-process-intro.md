<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->


A *governance action process* is a predefined sequence of [engine actions](/concepts/engine-action) that are coordinated by the [Governance Engine OMAS](/services/omas/governance-engine/overview).

The steps in a governance action process are defined by linked [governance action process steps](/concepts/governance-action-process-step) stored in the open metadata ecosystem.  Each governance action process step provides the specification of the governance action to run.  The links between them show which [guards](/concepts/guard) cause the next step to be chosen and hence, the governance action to run.

The governance action process support enables governance professionals to assemble and monitor governance processes without needing to be a Java programmer.

## Examples

In the two examples below, each of the rounded boxes represent a governance action and the links between them is a possible flow - where the label on the link is the guard that must be provided by the predecessor if the linked governance action is to run.

The governance actions in example 1 are all implemented using [governance action services](/concepts/governance-action-service).  When these services complete, they supply a completion status.  If a service completed successfully, they optionally supply one or more guards and a list of [action targets](/concepts/action-target) for the subsequent governance action(s) to process.  

The first governance action in example 1 is called when a new asset is created.  For example the [Generic Element Watchdog Governance Action Service](/connectors/governance-action/generic-element-watchdog-governance-action-service) could be configured to monitor for new/refresh events for particular types of assets and initiate this governance process then this type of event occurs.

The first governance action to run is *Validate Asset*.  It retrieves the asset and tests that it has the expected classifications assigned.  The guards it produces control with actions follow.

Governance actions from the same governance action processes can run in parallel if the predecessor governance actions produces multiple guards. 

![Example 1](/concepts/governance-action-process-example-1.svg)
> **Example 1:** Governance Action Process to validate and augment a newly created asset

Governance action processes can include any [type of governance service](/concepts/governance-service).
Example 2 shows an [survey action service](/concepts/survey-action-service) amongst the [governance action services](/concepts/governance-action-service).

![Example 2](/concepts/governance-action-process-example-2.svg)
> **Example 2:** Governance Action Process to validate and augment a newly created asset

## Capturing lineage for a governance action process

The [engine actions](/concepts/engine-action) generated when a governance action process runs provide a complete audit trace of the governance services that ran and their results.  The [Governance Action Open Lineage Integration Connector](/connectors/integration/governance-action-open-lineage-integration-connector) is able to monitor the operation of the governance actions and produce [OpenLineage events](/features/lineage-management/overview/#the-openlineage-standard) to provide operational lineage for governance action processes.  Egeria is also able to [capture these events](/connectors/#capturing-and-publishing-lineage) (along with OpenLineage events from other technologies) for later analysis.

## Governance Action Process Lifecycle

The diagram below shows a governance action process assembly tool taking in information from a [governance engine pack](/concepts/governance-engine-pack) to build a governance action process flow.  This is shared with the open metadata ecosystem either through direct called to the [Governance Engine OMAS](/services/omas/governance-engone/overview) or via a [open metadata archive](/concepts/open-metadata-archive) (possibly the archive that holds the governance engine definition.

Once the definition of the governance action process is available, an instance of the process can be started, either by a [watchdog governance action service](/concepts/governance-action-service) or through a direct call to the Governance Engine OMAS.  Whichever mechanism is used, it results in the Governance Engine OMAS using the definition to choreograph the creation of [engine action](/concepts/engine-action) entities that drive the execution of the governance services in the [Engine Host](/concepts/engine-host).

![Lifecycle](/concepts/governance-action-process-lifecycle.svg)


!!! education "Further information"
    - The [0462 Governance Action Processes](/types/4/0462-Governance-Action-Processes) model shows how the governance action process flow is built out of [governance action process steps](/concepts/governance-action-process-step).
    - Governance action processes may be created using the [Governance Engine OMAS](/services/omas/governance-engine/overview) API.
    - The [Open Metadata Engine Services (OMES)](/services/omes) provide the mechanisms that support the different types of [governance engines](/concepts/governance-engine). These engines run the [governance services](/concepts/governance-service) that execute the [engine actions](/concepts/engine-action) defined by the governance action process.


