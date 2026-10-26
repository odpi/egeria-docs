<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Building a Data Security Strategy

[Ivor Padlock](/practices/coco-pharmaceuticals/personas/ivor-padlock) is Coco Pharmaceuticals' only security officer, responsible for both physical and IT security.  He has a lot of experience of physical security, but no real IT background.  When the [fraud around the supplier database](/practices/coco-pharmaceuticals/scenarios/investigating-suspicious-activity/overview) is detected, he engages [Sidney Seeker](/practices/coco-pharmaceuticals/personas/sidney-seeker), the fraud investigator helping with the case, as a security consultant.  On the IT side, Ivor has been relying on [Gary Geeke](/practices/coco-pharmaceuticals/personas/gary-geeke), who joined Coco Pharmaceuticals from college and has learnt IT systems management, and the security that goes with it, on the job.  Gary has been a great help, but he is no security expert either.

Ivor invites [Sidney Seeker](/practices/coco-pharmaceuticals/personas/sidney-seeker), [Gary Geeke](/practices/coco-pharmaceuticals/personas/gary-geeke) and [Lemmie Stage](/practices/coco-pharmaceuticals/personas/lemmie-stage) to a meeting to discuss the data security strategy.  Lemmie and Gary describe their processes to secure the IT systems.  They use certificates, a firewall and SSL on the internal network, along with strong passwords on administrative user accounts.

Sidney asks if the security of the systems has ever been tested, by an expert - or using advanced tools?  The answer was "no".

Sidney explained that cyber attackers are using sophisticated tools that include AI to penetrate organizations and steal information.   They have a lot of computing resources to pound an organization's systems, looking for vulnerabilities. They may also use social engineering (such as phishing) to get information from employees.
Since cyber threats are not static, and evolve rapidly, it is necessary to perform regular audits and assessments to stay one step ahead of the threats by identifying and mitigating potential vulnerabilities before they can be exploited.

![Building a Data Security Strategy](ivor-sidney-lemmie-gary-it-security-strategy-meeting.png)

Ivor realizes that this is a serious situation.  Coco Pharmaceuticals' future depends on taking care of its intellectual property and reputation.  Both are at risk from cyber attacks. It needs to take steps to protect their data and ensure that it is safe and secure. He asks Sidney to help him build a briefing for the board to raise awareness of the situation and request further investment in IT security.

Both of those exposures are later recorded as entries in the governance team's [risk register](/practices/coco-pharmaceuticals/scenarios/building-the-governance-team/overview#the-risk-register): theft of personalised treatment intellectual property, and ransomware disruption to manufacturing operations.  Ivor owns them, and both are rated Critical.


## Supporting the Data Security Strategy

A key finding of their analysis was that Ivor needed specialist help to monitor, test and improve the security of the IT systems, and Sidney recommends that the company employs more security staff.  In typical Coco Pharmaceuticals style, they employ one new person: [Simon Burr](/practices/coco-pharmaceuticals/personas/simon-burr) (known as Si to his friends) joins as Chief Information Security Officer (CISO), reporting to Ivor, who becomes the Chief Security Officer.

![Ivor welcoming Simon Burr to Coco Pharmaceuticals](ivor-welcoming-si-to-coco.png)

## Choosing a framework

Si's first recommendation is that Coco Pharmaceuticals should not invent its own security program.  The international standard for an *information security management system* (ISMS), ISO/IEC 27001:2022, already describes what a well-run security program does, and its Annex A provides a reference set of controls covering the organizational, people, physical and technological aspects of security.  Building on the standard gives Ivor a structure that auditors, hospital partners and regulators already understand, and certification against it gives patients independent assurance that their data and the research behind their treatments is protected.

Ivor, Sidney and Si write the strategy together.  They agree that it should not stand alone: the [governance leaders](/practices/coco-pharmaceuticals/scenarios/building-the-governance-team/overview) have already defined the *Cyber Resilience* business imperative, the *Cyber-Attack on Operations or Data* threat, and the obligation that *All Users Must Be Authenticated and Accountable*.  The new definitions respond to those drivers rather than restating them, so that the security program is visibly part of the company's wider governance.

## The security governance definitions

The strategy is captured as a set of [governance definitions](/concepts/governance-definition) in the `Security` [governance domain](/concepts/governance-domain).

???+ info "Governance principle"
    **Risk-Based Information Security Management** - security controls are selected and prioritised according to a documented assessment of risk, not applied uniformly.  This is the same discipline the security team uses to rate entries in the risk register, now applied inside the ISMS, with each control in the *Statement of Applicability* traceable to the risk that justifies it.

???+ info "Governance obligations"
    * **Information Assets Must Be Inventoried and Classified for the ISMS** - every asset in scope must appear in an asset inventory and be classified for its confidentiality, integrity and availability requirements.  The classification must stay consistent with the personal data classification owned by the privacy team.
    * **Third-Party and Supplier Access Must Be Risk-Assessed** - suppliers, cloud providers and hospital or research partners are assessed before they are given access, reassessed periodically, and lose their access when the relationship ends.
    * **Security Incidents Must Be Logged, Reported, and Reviewed** - a single reporting channel, known to all staff, with every incident triaged, investigated and reviewed for lessons learned.
    * **Staff Must Complete Annual Security Awareness Training** - at induction and every year after, with extra role-specific training for people who handle research or patient data.

???+ info "Governance approach"
    **ISMS Plan-Do-Check-Act Continuous Improvement Cycle** - the ISMS is operated as a continuous cycle of internal audit, management review and corrective action, rather than as a one-off compliance exercise that degrades between audits.

???+ info "Governance controls"
    * The **ISO/IEC 27001:2022** [certification type](/types/4/0482-Certifications) records the scope of the ISMS - research systems, manufacturing control systems, corporate IT and the data shared with hospital and research partners.
    * Three [governance metrics](/types/4/0420-Governance-Controls) measure how well the program is working: the *Annex A Control Implementation Rate*, the *Security Incident Mean Time to Containment*, and the *Security Awareness Training Completion Rate*.

Each new policy is linked back to the driver it responds to, and each control to the policy it implements.  For example, the supplier obligation answers the threat's implication that "data shared with external partners must be governed by agreements and monitored", and the incident obligation answers the implication that "incident response procedures must exist and be tested regularly".  Every definition is also added to Ivor's *Chief Security Officer* governance folio, so that he has a single view of everything he is accountable for.  The definitions that Si operates day to day - the ISMS cycle, the certification, the metrics and the critical cyber security risks - are also collected in Si's own *Chief Information Security Officer* folio.

!!! summary "Usage"
    Writing the strategy as linked governance definitions, rather than as a standalone document, means that the question *why do we do this?* can always be answered by following the links from a control back to the risk and the threat behind it.  It is also what lets the security program be audited from inside Egeria as the ISMS matures.

## Baking security into the business

When Ivor presents the strategy to the other governance leaders, it becomes clear that very little of it can be delivered by the security team alone.

* The asset inventory that the ISMS depends on is, in practice, the same list of systems that [Gary Geeke](/practices/coco-pharmaceuticals/personas/gary-geeke) maintains for IT infrastructure.  The security team cannot patch, monitor or scope an estate it cannot enumerate.  Rather than build a second inventory, Ivor and Gary agree that the systems inventory and the ISMS asset inventory are *the same enumeration seen from two angles*, and that it will be maintained once - in Egeria.  This makes improving IT systems governance a precondition for security governance, and turns Gary into one of Ivor's most important collaborators.
* The classification obligation has to dovetail with [Faith Broker](/practices/coco-pharmaceuticals/personas/faith-broker)'s classification of personal data.
* The supplier obligation depends on the corporate governance team knowing who the company's third parties are.
* Revoking the access of a leaver depends on human resources telling security that someone has left.
* The training obligation is delivered through the company-wide [education program](/practices/coco-pharmaceuticals/scenarios/defining-data-enabled-employees/overview) that the governance leaders are designing together.  To support it, Si writes a security glossary with Ivor and Sidney, so that words such as *threat*, *risk*, *vulnerability* and *incident* mean the same thing to everyone.

In the governance team's language, `Security` is a *systemic* domain: it addresses issues that cut across the business, in service of the domains that own the business outcomes.  The same is true of data governance, and the two programs are built in the same way - as obligations that other domains' work depends on, with the links between them maintained in open metadata.  This is how security becomes part of the way Coco Pharmaceuticals works rather than a layer applied on top of it.

??? info "Loading the security governance program"
    The Dr.Egeria Markdown file for the data security strategy is `data-security-strategy.md` in 'coco-workbooks/0. data-governance-program' of the [Quickstart](/egeria-workspaces/quick-start/overview) environment.  [Link to the directory on GitHub](https://github.com/odpi/egeria-workspaces/tree/main/coco-workbooks/0.%20data-governance-program).  It links to definitions in the data governance program and risk register, so follow the load order in the directory's `README.md`.

??? info "Loading the security glossary"
    The Dr.Egeria Markdown file for the security glossary is `security-glossary.md` in 'coco-workbooks/4. keeping-safe'.  It is loaded after `onboarding-simon-burr.md`, which records Si's arrival: his profile, the CISO role, his governance folio and his plan for his first ninety days.  [Link to the directory on GitHub](https://github.com/odpi/egeria-workspaces/tree/main/coco-workbooks/4.%20keeping-safe).  It defines 63 terms in six folders, from the CIA triad and the ISMS vocabulary through identity and access, kinds of attack and security testing, to incident response.

??? info "Viewing the security governance program"
    The definitions can be viewed through [Egeria Explorer](/user-interfaces/egeria-explorer/overview) under the **Governance Definitions** card, or through the **Collections** card by selecting **Folios** and then **Governance Folios**, where Ivor's *Chief Security Officer* folio collects them, and Si's *Chief Information Security Officer* folio collects the ones he operates.

## Next steps

With the strategy agreed, Si turns to [assuring the security of the IT systems](/practices/coco-pharmaceuticals/scenarios/assuring-it-systems-security/overview), and Gary's team continues [cataloguing the IT infrastructure](/practices/coco-pharmaceuticals/scenarios/cataloguing-infrastructure/overview) that the ISMS asset inventory rests on.

!!! education "Further information"
    * [Defining the Security Strategy](/egeria-solutions/defining-security-strategy/overview) describes the Egeria solution used in this scenario.
    * [Keeping Safe](/egeria-solutions/keeping-safe) lists Egeria's other security solutions.

--8<-- "snippets/abbr.md"
