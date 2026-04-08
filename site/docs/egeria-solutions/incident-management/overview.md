<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


## Threat Modelling

Threat modelling is a process used to identify, analyze, and prioritize potential threats to an organization's assets, systems, and operations. It involves creating a model of the system or process being analyzed, identifying potential threats, and assessing the likelihood and impact of those threats. The goal of threat modelling is to help organizations proactively address potential security risks and vulnerabilities before they can be exploited by attackers.

Threat modelling is an essential component of the overall security strategy for any organization, as it provides a structured approach to identifying and mitigating potential security risks. By using threat modelling, organizations can better understand the potential threats to their systems and operations, and take proactive steps to protect against them.

Egeria's Threat Modelling solution provides a comprehensive approach to threat modelling, including tools and techniques for creating threat models, identifying potential threats, and assessing the likelihood and impact of those threats. The solution also includes guidance and best practices for implementing threat modelling in an organization, as well as templates and examples to help organizations get started with the process.

Overall, threat modelling is a critical component of any organization's security strategy, and Egeria's Threat Modelling solution provides a powerful tool for organizations to proactively address potential security risks and vulnerabilities.



## System Modelling



## Threat Elicitation

From Stride ... Microsoft Commerce Server information - no longer updated
During the design phase of your Web site development, you should create a threat model. This is a list of areas where your Commerce Server site is most vulnerable, the risk of an attack to each area, what you can do to mitigate the risk, and the priority assigned to implementing the mitigation. By creating a threat model, you can identify the areas where your Commerce Server installation is most vulnerable and then choose the appropriate tools and implement the best design to protect it.

The threat modeling process is as follows:

    Identify the known threats to the system.
    Rank the threats in order by decreasing risk.
    Determine how you will respond to the threats.
    Identify techniques that mitigate the threats.
    Choose the appropriate technologies from the identified techniques.

You might need to perform this process more than once because it is difficult to formulate all possible threats in one pass. Also, technology changes over time, new issues arise, and the business and technical landscape may expose new risks, or render existing threats harmless. All of these have an impact on the known threats to your system.

When you are considering threats, it is useful to ask questions such as these:

    How can an attacker change the authentication data?
    What is the impact if an attacker can read the user profile data?
    What happens if access is denied to the user profile database?

You can group threats into categories to help you formulate these kinds of pointed questions. One model you may find useful is STRIDE, derived from an acronym for the following six threat categories:

    Spoofing identity. An example of identity spoofing is illegally accessing and then using another user's authentication information, such as username and password.
    Tampering with data. Data tampering involves the malicious modification of data. Examples include unauthorized changes made to persistent data, such as that held in a database, and the alteration of data as it flows between two computers over an open network, such as the Internet.
    Repudiation. Repudiation threats are associated with users who deny performing an action without other parties having any way to prove otherwise—for example, a user performs an illegal operation in a system that lacks the ability to trace the prohibited operations. Nonrepudiation refers to the ability of a system to counter repudiation threats. For example, a user who purchases an item might have to sign for the item upon receipt. The vendor can then use the signed receipt as evidence that the user did receive the package.
    Information disclosure. Information disclosure threats involve the exposure of information to individuals who are not supposed to have access to it—for example, the ability of users to read a file that they were not granted access to, or the ability of an intruder to read data in transit between two computers.
    Denial of service. Denial of service (DoS) attacks deny service to valid users—for example, by making a Web server temporarily unavailable or unusable. You must protect against certain types of DoS threats simply to improve system availability and reliability.
    Elevation of privilege. In this type of threat, an unprivileged user gains privileged access and thereby has sufficient access to compromise or destroy the entire system. Elevation of privilege threats include those situations in which an attacker has effectively penetrated all system defenses and become part of the trusted system itself, a dangerous situation indeed.

Threat type 	Mitigation technique
Spoofing identity

    Authentication
    Protect secrets
    Do not store secrets

Tampering with data

    Authorization
    Hashes
    Message authentication codes
    Digital signatures
    Tamper-resistant protocols

Non-repudiation

    Digital signatures
    Timestamps
    Audit trails

Information disclosure

    Authorization
    Privacy-enhanced protocols
    Encryption
    Protect secrets
    Do not store secrets

Denial of service

    Authentication
    Authorization
    Filtering
    Throttling
    Quality of service

Elevation of privilege

    Run with least privilege


--8<-- "snippets/abbr.md"
