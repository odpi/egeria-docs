<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->


# Governance Domain

A *Governance domain* is a focus area for governance that needs collaboration across the organization and so can not be handed to a single team.  The work associated with the domain typically includes some attention to people, process, data and technology.

* *People* may require new skills and need to embrace new/additional roles and responsibilities.  These additional tasks need to be balanced with existing workloads, and may mean that other work is delayed or abandoned.
* *Processes* may need to be defined to help people coordinate their work across the organization.
* *Data* may need to be collected to report to regulators or determine the effectiveness of the governance activities.
* *Technology* may need to be deployed to support automation, communication and new capabilities.

These changes typically result in new projects being spawned to deliver certain changes.  They can be organized under a single campaign, with nested projects and tasks used to organize the work and track progress.

A governance domain typically has a [community](/concepts/community) that is used to bring people together for education, status updates, celebrations and to provide a forum for discussion and new ideas.

![Governance Domain Examples](/guides/planning/governance-program/governance-domain-examples.svg)
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
