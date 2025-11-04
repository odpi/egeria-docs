<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Specification

Specifications provide the information required to understand the behaviour of a function, to call it and to interpret its results.  This is particularly important for functions that are available as a library for people to browse, select and run.

Egeria's templates, connectors and governance actions fit into this category. They can provide their own specification which can be maintained by the [Valid Metadata API](/services/omvs/valid-metadata/overview) and queried through the [Automated Curation API](/services/omvs/automated-curation/overview).

## Template specifications

[Templates](/concepts/template) define patterns of metadata elements.  They are used to create consistent catalog entries.  Templates include replacement attributes and [placeholder properties](/concepts/placeholder) to allow specific values to be inserted into the new elements during the templating process.  The names, types and descriptions of the replacement attributes and placeholder properties are found in a template specification.

There are two types of specification properties for templates:

* *replacementAttribute* - Name of attribute that should be provided when using the attached template.  Replacement attributes map to the root entity of the template, or, the first occurrence of the attribute in attached relationships, classifications or entities.
* *placeholderProperty* - Placeholder names are located through the attribute values found in a template.  They are identified with double braces, for example {{variableName}}.  The value supplied is substituted for the placeholder variable.

They can be attached to a template, and maintained through the [Valid Metadata API](/services/omvs/valid-metadata/overview).

## Integration Connector Specifications

An integration connector implementation synchronizes (exchanges) metadata with particular types of third party technology.  It often picks up details of which instance of this technology it is to synchronize with through its [catalog targets](/concepts/catalog-target).  The specification for an integration connector describes the types of catalog targets it supports, and the configuration properties it understands.

These are the specification properties for integration connectors.

* *Supported Template* - Description of a template that should be used by the connector when creating new elements of a certain type.
* *Supported Configuration Property* - Description of a configuration property that is used to affect the behaviour of a connector.

They are attached to the [Integration Connector](/types/4/0464-Dynanic-Integration-Groups) entity used to define the integration connector in open metadata, and maintained through the [Valid Metadata API](/services/omvs/valid-metadata/overview).

## Governance Service Specifications

[Governance Services](/concepts/governance-service) provide the implementation of [governance actions](/concepts/governance-action).  They are highly configurable and tis reflects in their specification which includes:

* *Supported Request Type* - Description of a request type used to describe a request to a governance engine/service.
* *Supported Request Parameters* - these are the different types of request parameters that can be used to affect the behaviour of the governance service.
* *Supported Action Targets* - these list the types of [action targets](/concepts/action-target) that the governance service can process.
* *Supported Template* - Description of a template that should be used by the connector when creating new elements of a certain type.
* *supportedConfigurationProperty* - Description of a configuration property that is used to affect the behaviour of a connector.
* *Supported Analysis Steps* ([Survey Action Service](/concepts/survey-action-service) only) - these list the analysis steps supported by the survey action service.  They provide a description of the types of analysis performed.  Some survey action services allow you to specify which analysis steps to skip through its request parameters.
* *Produced Request Parameters* - these list the types of any new request parameters produced by the governance service.  These new request parameters will be added to (and may override) the request parameters supplied to the governance service.  If the governance service is running as a step in a [governance action process](/concepts/governance-action-process), the combined request parameters are passed on to the next step(s) in the process. 
* *Produced Action Targets* - these list the types of any new [action targets](/concepts/action-target) produced by the governance service.  These new action targets will be added to (and may override) the action targets supplied to the governance service.  If the governance service is running as a step in a [governance action process](/concepts/governance-action-process), the combined action targets are passed on to the next step(s) in the process.
* *Produced Guards* - these list the possible [guards](/concepts/guard) produced by the governance service when it completes.  It also identifies the completion status that accompanies the guard that indicates whether the governance service succeeded or failed.
* *Produced Annotation Types* ([Survey Action Service](/concepts/survey-action-service) only) - these list the different types of annotations produced by the survey action service, the data values they include and which analysis step they are produced by.


???+ info "Further information"
    * Retrieval of the specifications for templates, connectors and governance actions is possible through the [Automated Curation API](/services/omvs/automated-curation/overview).
    * The [Valid Metadata API](/services/omvs/valid-metadata/overview) supports maintenance of such specifications.
    * The open metadata types for specifications are defined in model [0545 - Reference Data](/types/5/0545-Reference-data).

--8<-- "snippets/abbr.md"

