<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Process

A *process* describes an activity: a well-defined set of processing steps and decisions that drive some aspect of the organization's business.  Most processes are automated with software, but a process may equally be a manual procedure performed by a person or a team.

A process is a type of [asset](/concepts/asset).  This is deliberate - a process is something the organization owns, depends on and must govern, in exactly the same way as the data it operates on.  It can therefore be catalogued, assigned an owner, placed in a [governance zone](/concepts/governance-zone) and secured.

## Processes and lineage

Processes are what connect assets together in [lineage](/features/lineage-management/overview).  The data flowing into and out of a process is described using [ports](/types/2/0217-Ports), each with a schema describing the structure of the data it carries.  Following the ports from asset to process to asset is what produces a lineage graph.

The *ProcessHierarchy* relationship defines a parent-child relationship between processes.  This allows an abstract, business-level process to be decomposed into the lower-level processes that implement it, so that lineage can be viewed at whatever altitude the question requires.

## Describing the activity

Alongside the normal asset properties, a process records its lifecycle: *requestedTime*, *requestedStartTime*, *startTime*, *dueTime*, *lastReviewTime*, *lastPauseTime*, *lastResumeTime* and *completionTime*, together with an *activityStatus*.  The *expectedBehaviour* property describes what the person or automated process is supposed to do.

## Specializations

* A **DeployedSoftwareComponent** is a code asset deployed to implement a [software capability](/concepts/software-capability).  It records the *deployedImplementationType* and *implementationLanguage*, and its interface is described by an API schema.
* A **DeployedConnector** is a [connector](/concepts/connector) - a specialist software component providing pluggable access to third party technology through the [Open Connector Framework](/frameworks/ocf/overview).
* An **EmbeddedProcess** is a processing element nested inside a deployed software component.  A **TransientEmbeddedProcess** is one that runs only briefly - relevant because each run may have different lineage, so the start and end times are recorded on the element itself.
* A **FunctionCall** describes a call to an external function.
* A [governance action process](/concepts/governance-action-process) is the process type Egeria uses to automate its own governance.

???+ info "Additional information"
    * The *Process* entity is defined in [Model 0010 Base Model](/types/0/0010-Base-Model); its specializations are described in [Model 0215 Software Components](/types/2/0215-Software-Components).
    * [Lineage Management](/features/lineage-management/overview) describes how processes and assets link together to form lineage graphs.

--8<-- "snippets/abbr.md"
