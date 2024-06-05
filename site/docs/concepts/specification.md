<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Specification

Specifications provide the information required to understand the behaviour of a function, to call it and to interpret its results.  This is particularly important for functions that are available as a library for people to browse, select and run.

Egeria's templates, connectors and governance actions fit into this category. They can provide their own specification which can be queried through the [Automated Curation OMVS](/services/omvs/automated-curation/overview).

## Template specifications

[Templates](/concepts/template) are used to create consistent catalog entries.  They include [placeholders](/concepts/placeholder) to allow specific values to be inserted into the resulting elements during the templating process.  The names, types and descriptions are found in a template specification.

## Integration Connector Specifications

An integration connector implementation synchronizes (exchanges) metadata with particular types of third party technology.  It often picks up details of which instance of this technology it is to synchronize with through its [catalog targets](/concepts/catalog-target).  The specification for an integration connector describes the types of catalog targets it supports.

## Governance Service Specifications

[Governance Services](/concept/governance-service) provide the implementation of [governance actions](/concepts/governance-action).  They are highly configurable and tis reflects in their specification which includes:

* *Supported Request Parameters* - these are the different types of request parameters that can be used to affect the behaviour of the governance service.
* *Supported Action Targets* - these list the types of [action targets](/concepts/action-target) that the governance service can process.
* *Supported Analysis Steps* ([Survey Action Service](/concepts/survey-action-service) only) - these list the analysis steps supported by the survey action service.  They provide a description of the types of analysis performed.  Some survey action services allow you to specify which analysis steps to skip through its request parameters.
* *Produced Request Parameters* - these list the types of any new request parameters produced by the governance service.  These new request parameters will be added to (and may override) the request parameters supplied to the governance service.  If the governance service is running as a step in a [governance action process](/concepts/governance-action-process), the combined request parameters are passed on to the next step(s) in the process. 
* *Produced Action Targets* - these list the types of any new [action targets](/concepts/action-target) produced by the governance service.  These new action targets will be added to (and may override) the action targets supplied to the governance service.  If the governance service is running as a step in a [governance action process](/concepts/governance-action-process), the combined action targets are passed on to the next step(s) in the process.
* *Produced Guards* - these list the possible [guards](/concepts/guard) produced by the governance service when it completes.  It also identifies the completion status that accompanies the guard that indicates whether the governance service succeeded or failed.
* *Produced Annotation Types* ([Survey Action Service](/concepts/survey-action-service) only) - these list the different types of annotations produced by the survey action service, the data values they include and which analysis step they are produced by.



