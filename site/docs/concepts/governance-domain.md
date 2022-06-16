<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->


# Governance Domain

*Governance domains* are the areas of an organization's operation that receive specific focus from a governance point of view.

![Goverrnance Domain Examples](/services/omas/governance-program/governance-domain-examples.svg)
> Examples of different governance domains within an organization.  Each domain is typically the responsibility of a different executive in the organization.  They may use slightly different terminology and often different tools but in fact they are very similar in the way that they operate.  Egeria allows the teams from the different governance domains to collaborate and benefit from each others efforts.

Governance domains are represented by *[Governance Domain Descriptions](/types/4/0401-Governance-Definitions)* that are referenced by the *domainIdentifier* property.  This is an integer and by convention "0" means "applies to all domains".

It is possible to set up a default list of domains using the [`createStandardGovernanceDomains`](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/governanceprogram/api/GovernanceDomainInterface.html) method from the [Governance Program OMAS](/services/omas/governance-program/overview). This will give you the following governance domain definitions:

| Domain Identifier | Domain Name | Description                                                                                                           |
| :-------- | :-------- |:----------------------------------------------------------------------------------------------------------------------|
| 1 | DATA | The governance of data and its use. |
| 2 | PRIVACY | The support for data privacy. |
| 3 | SECURITY | The governance that ensures IT systems and the data they hold are secure. |
| 4 | IT_INFRASTRUCTURE | The governance of the configuration and management of IT infrastructure and the software that runs on it. |
| 5 | SOFTWARE_DEVELOPMENT | The governance of the software development lifecycle.|
| 6 | CORPORATE | The governance of the organization as a legal entity.|
| 7 | ASSET_MANAGEMENT | The governance of physical assets.| 


--8<-- "snippets/abbr.md"
