<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->


# 0710 Digital Service

The digital services provide a business perspective on the services provided by IT.  When it is linked to the metadata that describes the IT implementation landscape, it provides traceability between the business leaders' perspective of IT and its actual implementation.  This helps to identify how the value/cost of It delivers value to the business.

![UML](0710-Digital-Service.svg)

## DigitalService

The *DigitalService* entity provides a root element for a digital capability that is significant to the owning organization.  This type of capability is referred to as a [Digital Service](/practices/digital-services/overview) in open metadata.

Digital services are typically owned and consumed by business capabilities.  These relationships are described in [model 0715](/types/7/0715-Digital-Service-Ownership).

Digital services may be implemented by many [digital resources](/concepts/digital-resource) such as APIs, data sets, and software components.  This can be represented directly by using the [ImplementedBy](/types/7/0737-Solution-Implementation) relationship to link the *DigitalService* entity to a digital resource's [Asset](/types/0/0010-Base-Model) entity.  Alternatively, the architecture of a digital service can be described in a [solution blueprint](/types/7/0740-Solution-Blueprints) made up of [solution components](/types/7/0730-Solution-Components).  The solution components have [SolutionPorts](/types/7/0735-Solution-Ports-and-Wires) that describe the inputs and outputs of the solution components.  *SolutionLinkingWire* relationships show how they are linked together.  The solution components can then be linked to the implementing digital resources' Asset entities via the *ImplementedBy* relationship.

## DigitalServiceDependency

The *DigitalServiceDependency* relationship allows an organization to capture the dependencies between digital services.  The nature of the dependency is supplied in the *description* property.

## DigitalProduct

A digital product describes a collection of digital resources that are produced for a specific type of consumer or purpose.  They conform to a specification and offer guarantees of service.  They may also have [terms and conditions](/types/4/0483-Terms-And-Conditions) associated with their use.

The *DigitalProduct* classification identifies an element that represents a digital product in metadata.  As such the *DigitalProduct* classification is typically attached to a [Collection](/types/0/0021-Collections) that has the [Assets](/types/0/0010-Base-Model) for the product's digital resources attached as members.

They are designed to be shared and may be advertised in a marketplace.   There are different categories of digital product.  For example:

* A **data product** is an example of a digital product that delivers a collection of data.  Each consumer of the product gets the same data.
* An **insight service** is an example of a digital product that provides information based on query values from the consumer.  Different consumers may receive different results.
* An **embedded feature**, such as a smartphone app, is an example of a digital product that is running in the consumer's environment/hardware.

## DigitalServiceProduct

A *DigitalService* can consist of multiple *DigitalProducts*.  These products may be of different categories offering a comprehensive multichannel service. The *DigitalServiceProduct* relationship identifies the *DigitalService* that a *DigitalProduct* belongs to.

--8<-- "snippets/abbr.md"