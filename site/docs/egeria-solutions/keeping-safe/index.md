<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Keeping Safe

Security and assurance are ongoing and collaborative processes.  They are used to protect the integrity of the systems that support the business to provide, for example:

* trust in its business operations,
* the prevention of data breaches, and
* the protection of sensitive data.

> The term *system* is used here in its broadest meaning, in that it includes the collaboration of people, processes, and technology to operate the business.

Egeria's *Keeping Safe* solutions aim to provide transparency from system design through to implementation and operation, helping to engage key people in the ongoing process of improving the safety, security, and privacy of the systems used by your organization.
In addition, they help develop practical steps to handle such a situation if an unfortunate event occurs, and capture the information needed to reduce the chance of it happening again.

## Egeria's role in security

Egeria is not a security tool in the sense of a firewall, a SIEM or a penetration testing suite.  Its contribution is threefold:

1. **It maintains the information that the security team needs.**  Security work depends on knowing what there is to protect - the systems, the data they hold, the software they run, how they connect, who owns them and who uses them - and on knowing what the organization has committed to: its regulations, threats, risks, policies and controls.  This information is usually scattered across spreadsheets, documents and the heads of individuals.  Egeria brings it together as linked open metadata that is kept up to date as the systems change.
2. **It keeps open metadata itself safe and trusted.**  A complete map of an organization's systems and their weaknesses is valuable to an attacker.  Egeria's [metadata security](/features/metadata-security/overview) controls who can see and change each element, [governance zones](/features/governance-zoning/overview) restrict visibility to the people who need it, secrets are kept in [secrets stores](/concepts/secrets-store-connector) rather than in configuration, and Egeria audits its own users.  This makes open metadata a resource that the security team can rely on.
3. **It creates visibility and traceability.**  When people can see the systems they own, the risks recorded against them, and why each control exists, they start to take part.  This has an effect beyond the security team: it makes the organization's operations more efficient, and its people more vigilant.

## The Keeping Safe solutions

* [Assessing a new regulation](/egeria-solutions/assessing-new-regulation/overview) helps to extract the key information from a regulation and create a model of its contents to first help key people understand its requirements and then build a definition of how the organization is going to meet its requirements and monitor its compliance.
* [Defining the Security Strategy](/egeria-solutions/defining-security-strategy/overview) describes how to lay out your organization's approach to security making use of standard definitions from security experts and their recommended best practices.
* [Threat Modelling](/egeria-solutions/threat-modelling/overview) helps to understand the risks that an organization faces and how to prioritize, mitigate and monitor them.
* [Incident Management](/egeria-solutions/incident-management/overview) helps to manage incidents that occur in the organization and ensure that they are handled in a timely and effective manner whilst collecting appropriate data for later analysis and improvement.
* [Proactive Cataloguing](/egeria-solutions/proactive-cataloguing/overview) helps to ensure that the organization's assets are properly catalogued and that the catalog is up to date from the moment a new IT capability is deployed.
* [Auditing Users](/egeria-solutions/auditing-users/overview) helps to ensure that users are properly authenticated and authorized to access the organization's systems and data.
* [Distributed Secrets](/egeria-solutions/distributed-secrets/overview) helps to ensure that secrets are properly managed and distributed across the organization's systems and that they are properly protected.

The solutions build on one another.  The security strategy sets out the policies and controls; threat modelling identifies the risks they must address; proactive cataloguing keeps the inventory of what must be protected up to date; and incident management closes the loop by feeding what was learned back into the risks and controls.  Auditing users and distributed secrets protect Egeria itself, along with the systems it connects to.

## Before you begin

An organization's security is not the act of a single security team, nor is it provided by the presence of security software, although both play their part.  To use a clich&eacute;, security is everyone's business. So the aim of a security program is to raise awareness that everyone's actions matter.  Anyone can compromise security through careless management of passwords, missing a software test case, failing to upgrade a software package, etc. Secure practices and feedback need to be provided to all employees and external partners.

Security governance also depends on good IT systems governance.  The security team cannot patch, monitor or assess the risk of systems it does not know about, so an accurate, maintained inventory of systems - with owners, purpose, data holdings and software levels - is a precondition for almost every technical security control.  It pays to treat the systems inventory and the security asset inventory as one list, maintained once, with the IT infrastructure team as a close partner.

Egeria's security and assurance solutions provide comprehensive information gathering, linking, analysis and reporting.  This helps in the awareness and coordination of security practices between people and security tools.  It is important to also engage security experts who bring experience to the table.  Their role is to help frame the security strategy, provide guidance on the most effective approaches to mitigate the risks that an organization faces.  Organizations such as [OWASP](https://owasp.org/) provide a wealth of information on security and assurance.  Their material is quoted in the solution descriptions, where appropriate. It is built from deep experience.  By following their guidance, you can eliminate the majority of threats, leaving your teams more time to focus on aspects of security that are unique to your business.

## Key personas

* [Ivor Padlock](/practices/coco-pharmaceuticals/personas/ivor-padlock) - **Chief Security Officer** - responsible for the security and assurance of the organization's premises, systems and data.
* [Simon Burr](/practices/coco-pharmaceuticals/personas/simon-burr) - **Chief Information Security Officer** - reports to Ivor, and is responsible for monitoring, testing and validating the security of the IT systems and services, including continuous penetration testing.
* [Gary Geeke](/practices/coco-pharmaceuticals/personas/gary-geeke) - **Chief Information Officer** - maintains the systems inventory that the security program depends on.
* [Lemmie Stage](/practices/coco-pharmaceuticals/personas/lemmie-stage) - **DevOps Specialist** - keeps the catalog up to date as software is deployed and patched.

## Examples showing how to use Egeria's security and assurance solutions

* [Building a data security strategy](/practices/coco-pharmaceuticals/scenarios/building-a-data-security-strategy/overview) for Coco Pharmaceuticals around the ISO/IEC 27001 information security management system standard, linked into the company's wider governance program.
* [Assuring IT Systems Security](/practices/coco-pharmaceuticals/scenarios/assuring-it-systems-security/overview), drawing on the security monitoring and testing experience of two acquired companies to extend protection across the original Coco Pharmaceuticals systems.
* [Understanding the new UK Terrorism (Protection of Premises) Act 2025 (aka Martyn's Law)](/practices/coco-pharmaceuticals/scenarios/preparing-for-martyns-law/overview) and how it impacts Coco Pharmaceutical's annual conference in London.
* Ensure the [auditability of IT System users](/practices/coco-pharmaceuticals/scenarios/auditing-it-system-users/overview) and their access to data, keeping open metadata safe and trusted.

These scenarios are supported by others that are not primarily about security:

* [Cataloguing Infrastructure](/practices/coco-pharmaceuticals/scenarios/cataloguing-infrastructure/overview) creates the systems inventory that threat modelling and the security asset inventory are built on.
* [DevOps Cataloguing](/practices/coco-pharmaceuticals/scenarios/devops-cataloguing/overview) keeps that inventory up to date, records the software supply chain, and supports a rolling update of system software so that security patches are in place.
* [Defining Data-Enabled Employees](/practices/coco-pharmaceuticals/scenarios/defining-data-enabled-employees/overview) describes the employee education program which, although led by the data governance team, raised awareness of data security issues across the company.

--8<-- "snippets/abbr.md"
