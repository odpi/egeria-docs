<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->


# 0710 Digital Products

The digital products provide a business perspective on the services and data provided by IT.  When they are linked to the metadata that describes the IT implementation landscape, it provides traceability between the business leaders' perspective of IT and its actual implementation.  This helps to identify how the value/cost of IT delivers value to the business.

![UML](0710-Digital-Products.svg)

## DigitalProduct entity

A digital product describes a collection of digital resources that are produced for a specific type of consumer or purpose.  They conform to a specification and offer guarantees of service.  They may also have [terms and conditions](/types/4/0483-Terms-And-Conditions) associated with their use.

The *DigitalProduct* entity identifies an element that represents a digital product in metadata.  As such the *DigitalProduct* inherits from [Collection](/types/0/0021-Collections) and has the [Assets](/types/0/0010-Base-Model) for the product's digital resources attached as members.

There are different categories of digital product.  For example:

* A **data product** is an example of a digital product that delivers a collection of data.  Each consumer of the product gets the same data.
* An **insight service** is an example of a digital product that provides information based on query values from the consumer.  Different consumers may receive different results.
* An **embedded feature**, such as a smartphone app, is an example of a digital product that is running in the consumer's environment/hardware.

Digital products are designed to be shared and may be advertised in a marketplace.  They are typically owned and consumed by [teams](/types/1/0115-Teams) responsible for [business capabilities](/types/4/0440-Organizational-Controls).  There is typical a person, or team responsible for development of a digital product.  These relationships are described in [model 0715](/types/7/0715-Digital-Product-Management).

Digital products may be implemented by many [digital resources](/concepts/digital-resource) such as APIs, data sets, and data feeds. 
The design of the processes can be represented by a [Solution component](/types/7/0730-Solution-Components) and linked directly by using the [ImplementedBy](/types/7/0737-Solution-Implementation) relationship to the appropriate digital resource's [Asset](/types/0/0010-Base-Model) entity.  Alternatively, the architecture of a digital process can be described in a [solution blueprint](/types/7/0740-Solution-Blueprints) made up of [solution components](/types/7/0730-Solution-Components).  The solution components have [SolutionPorts](/types/7/0735-Solution-Ports-and-Wires) that describe the inputs and outputs of the solution components.  *SolutionLinkingWire* relationships show how they are linked together.  The solution components can then be linked to the implementing digital resources' Asset entities via the *ImplementedBy* relationship.

## DigitalProductDependency

The *DigitalProductDependency* relationship allows an organization to capture the dependencies between digital products.  The nature of the dependency is supplied in the *description* property.


--8<-- "snippets/abbr.md"