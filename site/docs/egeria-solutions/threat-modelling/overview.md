<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


## Threat Modelling

Threat modelling is a process used to identify, analyze, and prioritize potential threats to an organization's assets, systems, and operations. It involves creating a model of the system or process being analyzed, identifying potential threats, and assessing the likelihood and impact of those threats. The goal of threat modelling is to help organizations proactively address potential security risks and vulnerabilities before they can be exploited by attackers.

Threat modelling is an essential component of the overall [security strategy](/egeria-solutions/defining-security-strategy/overview) for any organization, as it provides a structured approach to identifying and mitigating potential security risks.

Egeria's Threat Modelling solution provides a comprehensive approach to threat modelling, including tools and techniques for creating threat models, identifying potential threats, and assessing the likelihood and impact of those threats. The solution also includes guidance and best practices for implementing threat modelling in an organization, as well as templates and examples to help organizations get started with the process.

Overall, threat modelling is a critical part of any organization's security strategy, and Egeria's Threat Modelling solution provides a powerful tool for organizations to proactively address potential security risks and vulnerabilities.


## System Modelling

System modelling identifies the components of a system and their interactions.  Each component is modelled using a [Solution Component](/concepts/solution-component).  The components are connected using  [Solution Linking Wires](/concepts/connector).  The solution blueprint also shows the actors (both humans and software) that are involved in the system.  They include both the legitimate users and the bad actors.  They are modelled as [Solution Actor Roles]() and linked to the solution components using the [Solution Component Actor](/types/solution-access) relationship.

![System Modelling Components](system-modelling-components.svg)

Solution components can be nested to represent the structure of the system.  This allows the capture of system and network boundaries that are used to limit the exposure of key assets.

![System Modelling Nested Components](system-modelling-example.svg)

[Solution Blueprints](/concepts/solution_blueprint) are used to select components and roles to illustrate an aspect of the system.  This helps to create a focus and scope for a review meeting by selecting just the components that are relevant to the review, with maybe details of the context they operate in

## Threat Elicitation

Once the key system components have been identified, create a list of threats that could be exploited by an attacker.

STRIDE is an acronym describing six categories of security threats to an IT system that can be used as a checklist for identifying potential threats.
The terms that make up the stride model are:

* Spoofing - a spoofing attack is a situation in which a person or program successfully identifies as another by falsifying data, to gain an illegitimate advantage.
* Tampering - tampering is the act of modifying data or software in a way that is not authorized.
* Repudiation - repudiation is the act of denying having performed an action, such as a transaction or a message.
* Information Disclosure - information disclosure is the act of revealing sensitive information to unauthorized parties.
* Denial of Service - denial of service is the act of preventing legitimate users from accessing a system or service.
* Elevation of Privilege - elevation of privilege is the act of gaining unauthorized access to a system or resource with higher privileges than intended.


When you are considering threats, think about all types of data that could be accessed by an attacker.

You need to consider the possibility of threats to the following types of data:

* Configuration data: connection strings to databases
* Authentication data: user names and passwords stored in your Profiles database.
* Persistent data: data stored and used by Commerce Server processes such as SQL Server data, XML data, registry data, files, authentication and authorization data, and logs.
* Data that travels over communications channels: cookies, authentication information, purchasing and ordering information, and credit card numbers.
* State data: data that indicates whether the user is logged in or logged out, and data stored in shopping baskets.
* Temporary data: data that is created by the processes running the site.

It is useful to ask questions such as these:

* How can an attacker change, for example, the authentication data?
* What is the impact if an attacker can read the user profile data?
* What happens if access is denied to the user profile database?

## Prioritizing Threats

The next stage is to rank the threats by risk.  This combines a measure of impact with a measure of likelihood.

* What is the chance of an attack occurring? That is, how much effort/cost/time would be required to mount the attack? 1 = high chance, 10 = low chance
* What is the cost or damage to the component if an attack occurs? 1 = little damage, 10 = massive damage

> Risk = Damage if an attack occurs / Chance of attack. 
> 
> 1 = little risk, 10 = massive risk


## Mitigation Approaches

Starting with top-ranked threats, consider the possible following mitigation techniques.  
Typically the security strategy will set out the preferred approaches for each threat type.
However, the specifics of the technology involved may provide alternative approaches, or make such mitigation impossible - in which case, it may be time to choose different technology.

Here are some examples of mitigation techniques for different types of threat:

 | Threat type            | Mitigation technique                                         |
 |------------------------|--------------------------------------------------------------|
 | Spoofing identity      | Authentication                                               |
 |                        | Protect secrets                                              |
 |                        | Change passwords and other secrets regularly                 |
 |                        | Remove obsolete user identities                              |
 | Tampering with data    | Authorization (Governance Zones and Service Access Controls) |
 |                        | Secure storage                                               |
 |                        | Tamper-resistant network protocols                           |
 | Non-repudiation        | Digital signatures / certificates                            |
 |                        | Timestamps                                                   |
 |                        | Audit trails                                                 |
 | Information disclosure | Authorization                                                |
 |                        | Privacy-enhanced protocols                                   |
 |                        | Encryption                                                   |
 |                        | Protect secrets                                              |
 | Denial of service      | Authentication                                               |
 |                        | Authorization                                                |
 |                        | Throttling through gateway                                   |
 |                        | Quality of service                                           |
 | Elevation of privilege | Authentication                                               |
 |                        | Authorization                                                |
 |                        | Privilege separation                                         |
 |                        | Role-based access control                                    |
 |                        | Secure storage for secrets                                   |
 |                        | Tamper-resistant network protocols                           |



--8<-- "snippets/abbr.md" 
