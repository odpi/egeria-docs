<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Data Processing Description

A *data processing description* is a detailed description of the effect of some data processing.  It is the mechanism used to record exactly what an organization does to an individual's data, so that this can be compared with what the individual has agreed to.

Privacy regulations such as the EU's General Data Protection Regulation (GDPR) require the data subject to agree to the processing that is performed on their data.  That agreement is normally expressed in terms of an outcome that the data subject can understand - the *purpose* of the processing, such as *fulfil an order* or *provide clinical care*.  The data processing description supplies the detail that sits underneath the purpose.

## How the pieces fit together

* A **data processing purpose** describes the expected outcome, service or value from the processing.  It is a type of [governance definition](/concepts/governance-definition) and is what the data subject actually consents to.
* A **data processing description** describes how that outcome is achieved.  The *PermittedProcessing* relationship links the purpose to the descriptions of processing that are permitted in support of it.
* A **data processing action** describes the processing performed on a single target item.  The *DetailedProcessingAction* relationship gathers the individual actions that make up a data processing description, and the *DataProcessingTarget* relationship links each action to the element whose data it acts on.

Both the data processing description and the data processing action are types of [collection](/concepts/collection).  This means detail can be nested: a coarse-grained description can be decomposed into finer-grained descriptions and actions until the level of precision required by the organization's privacy policies is reached.

Two further relationships connect these definitions to the organization's operations:

* *ApprovedPurpose* identifies the purposes that a [process](/concepts/process) or [actor](/concepts/actor) has permission to process data for.
* *DataProcessingSpecification* identifies the processing that a process or actor is actually performing.

Comparing the two is what makes it possible to demonstrate that the organization's systems and people are only doing what has been agreed - and to detect where they are not.

???+ info "Additional information"
    * The *DataProcessingDescription*, *DataProcessingAction* and their relationships are described in [Model 0485 Data Processing Purposes](/types/4/0485-Data-Processing-Purposes).  The *DataProcessingPurpose* type is described in [Model 0440 Organizational Controls](/types/4/0440-Organizational-Controls).
    * The [Privacy Officer API](/services/omvs/privacy-officer/overview) provides the operations for maintaining data processing purposes, descriptions, actions and their targets.
    * [Data Privacy](/practices/data-privacy-pack/overview) describes the wider practice that these definitions support.

--8<-- "snippets/abbr.md"
