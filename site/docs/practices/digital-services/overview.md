<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Digital Services

A **digital service** is an automated service that is of significance to its owning organization. It may be delivered via the Internet or private network.

Typically, a digital service has a well-defined interface for requesting actions and data. This interface may include one, or a combination of the following:

* A user interface, such as a browser, application (eg Mobile App), or specialized device that allows
a person to interact with the service.  
* An API that is accessed by another digital service.
* An output feed of data that other digital services can subscribe to receive a copy of this data
* An input feed of data or requests for the digital service to process.

As part of its operation, a digital service will exchange data with its callers. It may also store data and share it with third parties. A digital service may also call other digital services to provide part of its function.

Organizations today increasingly rely on digital services to transact their business with their customers, employees and business partners. The result is that data is being generated and exchanged in a complex network of digital services that belong to different organizations.

Privacy regulations such as the EU's General Data Protection Regulation require an organization to guarantee that they are only processing personal data with the consent of the **[data subject](/practices/roles/data-subject-role)**. This means an organization needs to understand and manage the personal data consumed by their digital services.

## Digital Service Lifecycle

Every digital service has a lifecycle that takes it from a good idea, to a running service that is repeatedly enhanced until the service is decommissioned and shutdown.

While the service is running, it is processing requests from its consumers, sending requests to the digital services that it is dependent on and typically accumulating data.

There may also be incidents, such as service outages and data breaches occurring while the service is running and also requests from consumers for access to their data.

Figure 1 shows the lifecycle of a digital service.  The stages shown are described below the figure.

![Figure 1](digital-service-lifecycle-stages.png)

**Figure 1**: The lifecycle of a digital service

* **Digital Service Planning** covers the work to evaluate the business value of developing and running the digital service.
  This will include creating estimates of its development costs, and cost to run plus the likely uptake of the service and
  resulting business value.  Much of this will be done by the business owner supported by an architect to sketch out the
  design of the digital service.

* **Digital Service Development** covers the implementation of the digital service plus the support mechanisms,
  business operations, launch and marketing planning for the digital service.

* **Digital Service Deployment** covers the work to push the digital service into production.

* **Digital Service Onboarding** covers the sales/recruiting process to onboard users to the digital service.

* **Digital Service Use** covers the production use of the digital service.

* **Digital Service Incident** covers the management of an incident such as an outage, upgrade of essential
  infrastructure or data breach.

Notice that the lifecycle is show as a continuous process.  
An open metadata repository can be used to maintain information about the digital service.
This can link knowledge of th business model, governance requirements and implementation, making it possible for collaboration
correct action and an audit history to be maintained throughout the lifetime of the digital service.

Figure 2 shows the metadata repository in place.

![Figure 2](digital-service-lifecycle-stages-with-metadata-repository.png)

**Figure 2**: Using a metadata repository to manage the lifecycle of a digital service

The open metadata types includes the definition of a [digital service entity](/types/7/0710-Digital-Service).
This is used in the [data privacy pack](/practices/data-privacy-pack/overview).

--8<-- "snippets/abbr.md"

