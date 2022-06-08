<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Governance Action Service

--8<-- "docs/connectors/governance-action/governance-action-service-intro.md"

## Governance action context

A governance action service is passed a context as it is started. This provides access to the [request type and associated request parameters (name-value pairs)](/concepts/request-type) used to invoke the governance action service, along with its [action targets](/concepts/action-target).  There is also a client to access open metadata through the Governance Engine OMAS.

![Structure of the governance context](/frameworks/gaf/governance-action-service-with-context.svg)

The methods of the context are colour-coded.  The methods shown in white are available for all types of governance action services.  These are divided into three groups:

* Understanding the request

  * getRequestType - returns the [governance request type](/concept/governance-request-type) used to invoke the governance action service.
  * getRequestParameters - returns the name-value pairs of properties passed with the request type.
  * getRequestSourceElements - returns details of the process that invoked the governance action.
  * getActionTargetElements - returns the list of [action target](/concepts/action-target) elements that this governance action service is to work on.
  
* Performing the action

  * getOpenMetadataStore - returns a client to the Governance Engine OMAS that supports the retrieval of metadata elements, their classifications and relationships.
  * createIncidentReport - creates an [incident report](/concept/incident-report) that can provide a focal point for collaboration to resolve a particular issue.  Incident reports are often managed by an [incident management tool](/features/incident-reporting/overview).
  
* Recording the outcome of the processing

  * updateActionTargetStatus - records that the governance action service has completed processing a specific [action target](/concepts/action-target).  This is optional, but useful to show progress when a governance action process is performing action on a long list of action targets.
  * recordCompletionStatus - declares that the governance action service has completed processing.  It has three parameters:

    * completionStatus - with values:
    
      * Actioned - the governance action service has successfully completed processing.
      * Invalid - the governance action service has not performed the requested action because it is not appropriate (for example, a false positive).
      * Failed - The governance action service failed to execute the requested action.
      * Other - Undefined or unknown completion status.

    * outputGuards - the list of [guards](/concepts/guards) that are used to determine which governance action to run next.
    * newActionTargets - the list of [action targets](/concepts/action-target) that the follow-on governance services should process.
    
  * getCompletionStatus - returns the status passed on recordCompletionStatus or null if no status has been posted.  It is used to coordinate the shutdown of multiple threads operated by the governance action service.

The methods in blue are addition services offered to governance action services implementing a *watchdog* capability:

* registerListener - requests that it is called whenever certain open metadata events occur.  It is able to specify a range of conditions from receiving all event, events for particular actions (such as creation of a new metadata element), events for particular metadata types or events on particular instances.
* initiateGovernanceAction - requests that a new [governance action](/concepts/governance-action) is run.
* initiateGovernanceActionProcess - requests that a new [governance action process](/concepts/governance-action-process) is run.

The methods in purple are additional services offered to governance action services implementing a *provisioning* capability to record lineage:

* createAsset - create an asset - typically the destination of the provisioning.
* createProcess - create a representation of the provisioning process.
* createPort - create a port for the process
* createLineageMapping - create a lineage relationship.

There are no additional services for governance action services implementing a *verification* capability which is why the green box is empty.

The methods in yellow are additional services offered to governance action services implementing a *triage* capability to initiate a stewardship action:

* createToDo - create a [ToDo](/concepts/to-do) that is assigned to an individual.

The methods in red are additional services offered to governance action services implementing a *remediation* capability to make updates to open metadata.  They are divided into four groups:

* Working with metadata elements

  * createMetadataElement
  * updateMetadataElement
  * updateMetadataElementStatus
  * deleteMetadataElement

* Working with classification on a metadata element

  * classifyMetadataElement
  * reclassifyMetadataElement
  * updateClassificationStatus
  * unclassifyMetadataElement

* Working with relationships (links) between metadata elements

  * createRelatedElements
  * updateRelatedElements
  * updateRelatedElementsStatus
  * deleteRelatedElements

* Performing specialist governance actions

  * linkElementsAsPeerDuplicates
  * LinkConsolidatedDuplicate

A governance action service has a choice of base classes to extend that controls the methods provided in the governance action context:

* *GovernanceActionService* - for the complete context
* *WatchdogGovernanceActionService* - for the white and blue methods
* *ProvisioningGovernanceActionService* - for the white and purple methods
* *VerificationGovernanceActionService* - for the white and green methods
* *TriageGovernanceActionService* - for the white and yellow methods
* *RemediationGovernanceActionService* - for the white and red methods

The [Writing the governance action service connector](#writing-the-governance-action-service-connector) section provides more information on how to use the methods.

## Writing the connector provider

The connector provider for your governance action service provides the factory method to create an instance of the governance action service.  It also supports methods to describe the options that the governance action servvice provides.



## Writing the governance action service connector


### Generic methods

### Watchdog governance action service methods

--8<-- "docs/frameworks/gaf/watchdog-governance-action-service-intro.md"

### Verification governance action service methods

--8<-- "docs/frameworks/gaf/verification-governance-action-service-intro.md"

### Triage governance action service methods

--8<-- "docs/frameworks/gaf/triage-governance-action-service-intro.md"

### Remediation governance action service methods

--8<-- "docs/frameworks/gaf/remediation-governance-action-service-intro.md"

### Provisioning governance action service methods

--8<-- "docs/frameworks/gaf/provisioning-governance-action-service-intro.md"


!!! education "Next steps"

    * Configuring your governance action service - A collection of related governance action services are grouped into governance action engines for deployment. The governance action engine maps *governance action request types* to the governance action service that should be invoked along with.

      ![Structure of a governance engine definition](governance-action-engine-definitions.svg)

      These definitions are created as part of a [governance engine pack](/guides/developer/open-metdata-archives/creating-governance-engine-packs) or through the [Governance Engine OMAS](/services/omas/governance-engine/overview) and are stored in the open metadata repositories.

    * Running your governance action service - Governance action engines are hosted by the [Governance Action OMES](/services/omes/governance-action/overview) running on one or more [engine hosts](/concepts/engine-host).  The engine services run in dedicated OMAG Server called the [*engine host*](/concepts/engine-host). You can find [instructions for configuring the engine services in the engine host](/guides/admin/servers/configuring-an-engine-host/#configure-the-engine-host-services) in the administration guide.



--8<-- "snippets/abbr.md"