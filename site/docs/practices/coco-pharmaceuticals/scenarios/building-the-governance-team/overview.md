<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Building the governance team

When [Jules Keeper](/practices/coco-pharmaceuticals/personas/jules-keeper) joined Coco Pharmaceuticals as the CDO, he soon realized that the execution of their business strategy to move to personalized medicine was being held back by their operational practices. Some of this was related to their use and management of data (his responsibility to fix of course), but there were broader issues relating to security, IT infrastructure management, software development and their corporate governance.  He realizes that he can not do this alone and calls his colleagues together to discuss how they proceed.

![Calling the governance leaders together](governance-leaders-meeting-in-progress.png)

They agree to divide the work amongst themselves, using the traditional governance domains to divide out the responsibilities, but maintaining the governance information using open metadata (Egeria) to be able to coordinate their work across the governance domains.

The result is as follows:

* [Jules Keeper](/practices/coco-pharmaceuticals/personas/jules-keeper) becomes the CDO and head of the DATA governance domain.
* [Ivor Padlock](/practices/coco-pharmaceuticals/personas/ivor-padlock) becomes the CISO and head of the SECURITY governance domain.
* [Faith Broker](/practices/coco-pharmaceuticals/personas/faith-broker) becomes the CPO and head of the PRIVACY governance domain.
* [Reggie Mint](/practices/coco-pharmaceuticals/personas/reggie-mint) as the CFO becomes head of the CORPORATE governance domain.
* [Gary Geeke](/practices/coco-pharmaceuticals/personas/gary-geeke) as the infrastructure lead becomes head of the IT INFRASTRUCTURE governance domain.
* [Polly Tasker](/practices/coco-pharmaceuticals/personas/polly-tasker) as the most senior software manager becomes had of the SOFTWARE DEVELOPMENT governance domain.

They also add more specialist governance leaders to the team.

* [Erin Overview](/practices/coco-pharmaceuticals/personas/erin-overview) is to lead the DATA SHARING governance domain.
* [Tessa Tube](/practices/coco-pharmaceuticals/personas/tessa-tube) is to lead the DRUG DEVELOPMENT governance domain.
* [Tom Tally](/practices/coco-pharmaceuticals/personas/tom-tally) is to lead the SUSTAINABILITY governance domain.

## Defining the governance drivers

Their first challenge is to document the **governance drivers**.  These are the business imperatives, regulations and threats that the governance team needs to focus on.

They begin with the business imperatives.  They try to capture the key concerns of their board and come up with:.

* **Personalized medicine** - the company wants to provide personalized medicine to its customers.  Initial projects in this space have provide promising.  This is a key focus of the board, and requires an extensive business transformation.  It is where the governance activity can add a lot of value.
* **Cyber Resilience** - the board recognizes that cyber-security is critical to avoid both loss of intellectual property and the ongoing operations of the business.
* **Sustainability** - sustainability is recognized by the board as a way to provide focus on the future viability of the business.

Next they think about the threats to the business, including:

* **Cyber-attacks**
* **Loss of competitiveness**
* **Insufficient talent**
* **Disruption in the supply chain**

They next list the regulations that govern the business.  These are divided into:

* **regulations that any business must adhere to**, such as financial reporting.
* **regulations that govern the drug development process**, such as the way clinical trials are conducted.
* **regulations that govern the manufacturing of pharmaceuticals**
* **regulations that govern the distribution of pharmaceuticals**

They create definitions for each of these drivers to capture the essential information needed to understand the governance requirements they represent and load them into Egeria using the [Dr Egeria](/user-interfaces/dr-egeria/overview) Markdown processor.

![The governance leadership team defining governance drivers](meeting-of-the-governance-leaders-2.png)
>The governance leadership team defining governance drivers

With the drivers in place, they agree to go back to their teams to define the responses to each of these governance drivers.

See:

* [Creating the Data Governance Program](/practices/coco-pharmaceuticals/scenarios/creating-data-governance-program/overview)
* [Creating the Security Governance Program](/practices/coco-pharmaceuticals/scenarios/building-a-data-security-strategy/overview)
* [Creating the Sustainability Governance Program](/practices/coco-pharmaceuticals/scenarios/sustainability-initiative/overview)

!!! info "Further information"

    * [Planning for a governance program](/guides/planning/governance-program/overview)
    * [Governance Definitions](/concepts/governance-definition)

    The governance definitions created by the governance leaders can be loaded into Egeria and then viewed through [Egeria Explorer](/user-interfaces/egeria-explorer/overview) in the [Quickstart](/egeria-workspaces/quick-start/overview) environment.

--8<-- "snippets/abbr.md"
