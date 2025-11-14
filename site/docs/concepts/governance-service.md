<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Governance Service

A governance service is a specialized [connector](/concepts/connector) that implements a specific function.

--8<-- "snippets/concepts/governance-service-types.md"

## Inputs and Outputs

When a governance service is called, it is passed up to three types of input:

* The first is the [request type](governance-request-type.md) that indicates the type of request to perform.  Most governance services perform a single function and so ignore the requested type passed to it; however, if the governance service performs multiple functions, the request type is used to determine the function to perform.
* Next are the optional *request parameters*.  These are named properties that can be used to configure the behaviour of the governance service.
* Finally, are the optional [action targets](action-target.md) which are named links to metadata elements that the governance service should process.

![Inputs to a governance service](governance-service-input.svg)

Then the governance service completes, it outputs:

* One or more [guards](guard.md) that indicate the results of the processing.
* Optionally some additional request parameters and/or additional action targets that are passed on to any follow-on processing.  For example, a governance service may create a new metadata element and nominate it as a new action target.

![Outputs passed from a governance service](governance-service-output.svg)

## Handoff between governance services

This next picture shows two governance services that are steps in a [governance action process flow](governance-action-process.md).  The governance services do not call one another directly.  They operate in isolation just with the request type, request parameters and action targets they are passed.  When a governance service complete, it supplies one or more guards and optionally, some additional request parameters.  Egeria's [open governance services](/services/open-governance-services) reads the governance action process flow to determine the governance service to call next.  This next governance service is passed the request type defined in the governance action process flow and the accumulated request parameters and action targets from earlier steps. 

![Handoff between steps in a governance action process](governance-service-handoff.svg)

## Governance service specification

The names of request parameters and action targets passed to a governance service must match the names expected by its implementation.  In addition, if the governance service used the request type to determine which function to run, it is important to know the names of these request types in order to successfully call the governance service.  It would be awkward to have to review the code of the governance service to find out the names of the request type, request parameters and actions targets to use.  Similarly, when building a governance action process, it is necessary to understand the names of the guards that the governance service may produce and any additional request parameters and action targets.

To avoid users having to review its code, a governance service has a [specification](specification.md) that defines the names used in its implementation.  The specification defines lists of the following properties:

* Supported Request Types
* Supported Request Parameters
* Supported Action Targets
* Supported Templates
* Supported Configuration Properties
* Produced Guards
* Produced Request Parameters
* Produced Action Targets

The diagram maps these specification properties to the inputs and outputs of the governance service.  In addition, because the governance service is a special type of [connector](connector.md) it may also use [configuration properties](configuration-properties.md) and [templates](template.md).

![Specification Properties](governance-service-specification-properties.svg)

The specification is typically implemented in the governance service's [connector provider](connector-provider.md) so that it can be read by automated processes that are consuming the connectors.  For example, Egeria's build process reads the specifications of all of the governance services implemented in Egeria and creates open metadata elements for the specification that are linked to the metadata element for the governance service.  These metadata elements are loaded via the [content packs](/content-packs) and can be reviewed and used through the [Automated Curation API](/services/omvs/automated-curation/overview) and [Valid Metadata API](/services/omvs/valid-metadata/overview).

## Mapping and filtering

It is possible that the names used in the implementations of the governance services that are to be linked together in a governance action process flow are inconsistent.  Therefore the governance action process flow may include maps and filters to allow the [open governance services](/services/open-governance-services) to map the names from one governance service to appropriate names for the next governance services.  These maps and filters are specified in the [GovernanceActionExecutor](/types/4/0462-Governance-Action-Processes) relationship.

![Mapping names between governance services](governance-service-filter-and-map-properties-and-targets.svg)

## Implementing your own governance services

Instructions for implementing your own governance services are in the developer guide under the following sections: 

* [Writing Governance Action Services](/guides/developer/governance-action-services/overview)
* [Writing Survey Action Services](/guides/developer/survey-action-services/overview)
* [Writing Watchdog Action Services](/guides/developer/watchdog-action-services/overview)
* [Writing Repository Governance Services](/guides/developer/repository-governance-services/overview)

## Support for running governance services

A governance service can be called directly by creating an [engine action](engine-action.md).  A [governance action type](governance-action-type.md) can be used to "wrap" a call to a governance service.  The governance action type identifies the request type and can pre-define certain request parameters and action targets to simplify the call to run the governance service.  The governance service can be "wrapped" in a [step](governance-action-process-step.md) in a [governance action process](governance-action-process.md).

The API to create governance action types and governance action processes (collectively referred to a [governance actions](governance-action.md)) is called the [Action Author API](/services/omvs/action-author/overview).

The API to initiate a call to a governance service, either through an engine action, governance action type or governance action process, is called the [Automated Curation API](/services/omvs/automated-curation/overview).


--8<-- "snippets/abbr.md"