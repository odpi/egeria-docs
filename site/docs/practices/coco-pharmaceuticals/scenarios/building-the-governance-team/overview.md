<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Building the governance team

When [Jules Keeper](/practices/coco-pharmaceuticals/personas/jules-keeper) joined Coco Pharmaceuticals as the CDO, he soon realized that the execution of their business strategy to move to personalized medicine was being held back by their operational practices. Some of this was related to their use and management of data (his responsibility to fix of course), but there were broader issues relating to security, IT infrastructure management, software development and their corporate governance.  He realizes that he can not do this alone and calls his colleagues together to discuss how they proceed.

They agree to divide the work amongst themselves, using the traditional governance domains to divide out the responsibilities, but maintaining the governance information using open metadata (Egeria) to be able to coordinate their work across the governance domains.

The result is as follows:

* [Jules Keeper](/practices/coco-pharmaceuticals/personas/jules-keeper) becomes the CDO and head of the DATA governance domain.
* [Ivor Padlock](/practices/coco-pharmaceuticals/personas/ivor-padlock) becomes the CISO and head of the SECURITY governance domain.
* [Faith Broker](/practices/coco-pharmaceuticals/personas/faith-broker) becomes the CPO and head of the PRIVACY governance domain.
* [Reggie Mint](/practices/coco-pharmaceuticals/personas/reggie-mint) as the CFO becomes head of the CORPORATE governance domain.
* [Gary Geeke](/practices/coco-pharmaceuticals/personas/gary-geeke) as the infrastructure lead becomes head of the IT INFRASTRUCTURE governance domain.
* [Polly Tasker](/practices/coco-pharmaceuticals/personas/polly-tasker) as the most senior software manager becomes had of the SOFTWARE DEVELOPMENT governance domain.

[Erin Overview](/practices/coco-pharmaceuticals/personas/erin-overview) is also appointed the CDO for IT systems.  This makes her a deputy for Jules and recognizes her role in ensure data is properly managed by IT.

Egeria includes a sample client
([docs](https://github.com/odpi/egeria/blob/master/open-metadata-resources/open-metadata-samples/access-services-samples/governance-program-client-samples/governance-leadership.md), 
[code](https://github.com/odpi/egeria/blob/master/open-metadata-resources/open-metadata-samples/access-services-samples/governance-program-client-samples/src/main/java/org/odpi/openmetadata/accessservices/governanceprogram/samples/GovernanceLeadershipSample.java))
that issues the appropriate API calls to set up this team through the
[Governance Program OMAS](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/access-services/governance-program/README.md) Governance Leadership Interface.



--8<-- "snippets/abbr.md"
